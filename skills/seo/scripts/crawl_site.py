#!/usr/bin/env python3
"""
Crawl every page in a sitemap (or a sitemap index) and extract SEO-relevant
HTML signals. Writes one JSON file with a list of per-page records.

Examples:
    # Whole domain (auto-discovers /sitemap.xml)
    python crawl_site.py https://example.com --out /tmp/audit

    # Specific sitemap URL
    python crawl_site.py https://example.com \\
        --sitemap https://example.com/product/sitemap.xml \\
        --out /tmp/audit

    # Limit scope to a subfolder (only URLs starting with this prefix)
    python crawl_site.py https://example.com \\
        --sitemap https://example.com/sitemap.xml \\
        --prefix https://example.com/blog/ \\
        --out /tmp/audit

    # Limit page count
    python crawl_site.py https://example.com --max-pages 100 --out /tmp/audit

Per-page fields extracted: status, final_url, title (+len), meta_desc (+len),
canonical (+self-match), robots meta, x-robots-tag, noindex, H1 count + first
text, H2 count, hreflang_count, jsonld_blocks + types, og/twitter tag counts,
image count + missing-alt count, word_count, internal/external link counts,
viewport/charset presence, content_length.
"""

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

UA = "Mozilla/5.0 (compatible; ClaudeSEOAudit/1.0; +https://github.com/lionkiii/claude-seo-skills)"
DEFAULT_TIMEOUT = 20


def make_ssl_context(verify: bool) -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    if not verify:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return ctx


def http_get(url: str, timeout: int, ctx: ssl.SSLContext) -> tuple[int, str, dict, str]:
    """Return (status, body, headers, final_url). On error raises."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.status, resp.read().decode("utf-8", errors="replace"), dict(resp.headers), resp.url


# -----------------------------------------------------------------------------
# Sitemap handling
# -----------------------------------------------------------------------------

def discover_sitemap(base_url: str, timeout: int, ctx: ssl.SSLContext) -> str:
    """Try robots.txt first, fall back to /sitemap.xml."""
    base = base_url.rstrip("/")
    try:
        status, body, _, _ = http_get(base + "/robots.txt", timeout, ctx)
        if status == 200:
            for line in body.splitlines():
                if line.lower().startswith("sitemap:"):
                    return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return base + "/sitemap.xml"


def strip_ns(xml: str) -> str:
    return re.sub(r' xmlns="[^"]+"', "", xml, count=1)


def parse_sitemap(sitemap_url: str, timeout: int, ctx: ssl.SSLContext) -> list[str]:
    """Returns a flat list of URLs. Recurses into sitemap indexes."""
    try:
        _, body, _, _ = http_get(sitemap_url, timeout, ctx)
    except Exception as e:
        print(f"  ERROR fetching {sitemap_url}: {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(strip_ns(body))
    except ET.ParseError as e:
        print(f"  ERROR parsing XML {sitemap_url}: {e}", file=sys.stderr)
        return []

    # sitemap index
    if root.tag == "sitemapindex":
        urls = []
        for sm in root.findall("sitemap"):
            loc = sm.find("loc")
            if loc is not None and loc.text:
                urls.extend(parse_sitemap(loc.text.strip(), timeout, ctx))
        return urls

    # urlset
    urls = []
    for u in root.findall("url"):
        loc = u.find("loc")
        if loc is not None and loc.text:
            urls.append(loc.text.strip())
    return urls


# -----------------------------------------------------------------------------
# Per-page extraction
# -----------------------------------------------------------------------------

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
META_DESC_RE = re.compile(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', re.I)
CANON_RE = re.compile(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', re.I)
ROBOTS_META_RE = re.compile(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.S | re.I)
HREFLANG_RE = re.compile(r'<link[^>]+rel=["\']alternate["\'][^>]+hreflang=', re.I)
JSONLD_RE = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
OG_RE = re.compile(r'<meta[^>]+property=["\']og:', re.I)
TW_RE = re.compile(r'<meta[^>]+name=["\']twitter:', re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ALT_RE = re.compile(r"\balt\s*=", re.I)
VIEWPORT_RE = re.compile(r'<meta[^>]+name=["\']viewport["\']', re.I)
CHARSET_RE = re.compile(r"<meta[^>]+charset=", re.I)
SCRIPT_RE = re.compile(r"<script.*?</script>", re.S | re.I)
STYLE_RE = re.compile(r"<style.*?</style>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
LINK_HREF_RE = re.compile(r'<a\b[^>]*href=["\']([^"\']+)', re.I)


def extract_jsonld_types(html: str) -> list[str]:
    blocks = JSONLD_RE.findall(html)
    types: set[str] = set()
    for b in blocks:
        try:
            d = json.loads(b.strip())
        except Exception:
            continue
        nodes = d if isinstance(d, list) else [d]
        for n in nodes:
            if not isinstance(n, dict):
                continue
            if "@type" in n:
                t = n["@type"]
                types.update(t if isinstance(t, list) else [t])
            if "@graph" in n and isinstance(n["@graph"], list):
                for g in n["@graph"]:
                    if isinstance(g, dict) and "@type" in g:
                        t = g["@type"]
                        types.update(t if isinstance(t, list) else [t])
    return sorted(types)


def audit_page(url: str, timeout: int, ctx: ssl.SSLContext) -> dict:
    out = {
        "url": url, "status": 0, "final_url": url, "error": "",
        "title": "", "title_len": 0, "meta_desc": "", "meta_desc_len": 0,
        "canonical": "", "canonical_self": False, "robots_meta": "",
        "x_robots_tag": "", "noindex": False,
        "h1_count": 0, "h1_text": "", "h2_count": 0,
        "hreflang_count": 0, "jsonld_blocks": 0, "jsonld_types": "",
        "og_count": 0, "twitter_count": 0,
        "images": 0, "images_missing_alt": 0,
        "word_count": 0, "internal_links": 0, "external_links": 0,
        "content_length": 0, "has_viewport": False, "has_charset": False,
    }
    try:
        status, html, headers, final_url = http_get(url, timeout, ctx)
    except urllib.error.HTTPError as e:
        out["status"] = e.code
        out["error"] = f"HTTPError {e.code}"
        return out
    except Exception as e:
        out["error"] = str(e)[:200]
        return out

    out["status"] = status
    out["final_url"] = final_url
    out["content_length"] = len(html)
    out["x_robots_tag"] = headers.get("X-Robots-Tag", "") or headers.get("x-robots-tag", "")

    if m := TITLE_RE.search(html):
        out["title"] = re.sub(r"\s+", " ", m.group(1)).strip()
        out["title_len"] = len(out["title"])

    if m := META_DESC_RE.search(html):
        out["meta_desc"] = m.group(1).strip()
        out["meta_desc_len"] = len(out["meta_desc"])

    if m := CANON_RE.search(html):
        out["canonical"] = m.group(1).strip()
        out["canonical_self"] = out["canonical"].rstrip("/") == url.rstrip("/")

    if m := ROBOTS_META_RE.search(html):
        out["robots_meta"] = m.group(1)
        if "noindex" in m.group(1).lower():
            out["noindex"] = True
    if "noindex" in (out["x_robots_tag"] or "").lower():
        out["noindex"] = True

    h1s = H1_RE.findall(html)
    out["h1_count"] = len(h1s)
    if h1s:
        out["h1_text"] = TAG_RE.sub("", h1s[0]).strip()[:200]
    out["h2_count"] = len(H2_RE.findall(html))
    out["hreflang_count"] = len(HREFLANG_RE.findall(html))

    jsonld_types = extract_jsonld_types(html)
    out["jsonld_blocks"] = len(JSONLD_RE.findall(html))
    out["jsonld_types"] = ",".join(jsonld_types)

    out["og_count"] = len(OG_RE.findall(html))
    out["twitter_count"] = len(TW_RE.findall(html))

    imgs = IMG_RE.findall(html)
    out["images"] = len(imgs)
    out["images_missing_alt"] = sum(1 for t in imgs if not ALT_RE.search(t))

    out["has_viewport"] = bool(VIEWPORT_RE.search(html))
    out["has_charset"] = bool(CHARSET_RE.search(html))

    body = SCRIPT_RE.sub("", html)
    body = STYLE_RE.sub("", body)
    text = TAG_RE.sub(" ", body)
    out["word_count"] = len(text.split())

    host = urlparse(url).hostname or ""
    for href in LINK_HREF_RE.findall(html):
        if href.startswith("/") or host in href:
            out["internal_links"] += 1
        elif href.startswith("http"):
            out["external_links"] += 1

    return out


# -----------------------------------------------------------------------------
# Driver
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Crawl a site's sitemap for SEO audit.")
    ap.add_argument("base_url", help="Base site URL (e.g. https://example.com)")
    ap.add_argument("--sitemap", help="Specific sitemap URL. If omitted, auto-discovers.")
    ap.add_argument("--prefix", help="Only crawl URLs starting with this prefix.")
    ap.add_argument("--max-pages", type=int, default=500, help="Max pages to crawl (default: 500).")
    ap.add_argument("--workers", type=int, default=10, help="Concurrent HTTP workers (default: 10).")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Per-page timeout seconds.")
    ap.add_argument("--no-ssl-verify", action="store_true",
                    help="Skip SSL cert verification (useful on macOS Python without certifi).")
    ap.add_argument("--delay", type=float, default=0.0, help="Seconds between request batches.")
    ap.add_argument("--out", required=True, help="Output directory.")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    ctx = make_ssl_context(verify=not args.no_ssl_verify)

    sitemap_url = args.sitemap or discover_sitemap(args.base_url, args.timeout, ctx)
    print(f"Sitemap: {sitemap_url}", file=sys.stderr)

    all_urls = parse_sitemap(sitemap_url, args.timeout, ctx)
    print(f"Total URLs in sitemap: {len(all_urls)}", file=sys.stderr)

    if args.prefix:
        urls = [u for u in all_urls if u.startswith(args.prefix)]
    else:
        urls = all_urls
    urls = sorted(set(urls))[: args.max_pages]
    print(f"Auditing: {len(urls)} URLs (prefix={args.prefix or 'none'}, cap={args.max_pages})", file=sys.stderr)

    with open(os.path.join(args.out, "urls.txt"), "w") as f:
        f.write("\n".join(urls) + "\n")

    results: list[dict] = []
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(audit_page, u, args.timeout, ctx): u for u in urls}
        for fut in as_completed(futs):
            results.append(fut.result())
            done += 1
            if done % 25 == 0 or done == len(urls):
                print(f"  {done}/{len(urls)}", file=sys.stderr)
            if args.delay:
                time.sleep(args.delay)

    results.sort(key=lambda r: r["url"])
    out_path = os.path.join(args.out, "crawl_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)

    # quick summary
    ok = [r for r in results if r["status"] == 200]
    summary = {
        "total_crawled": len(results),
        "status_200": len(ok),
        "errors": [r["url"] for r in results if r["status"] != 200][:20],
        "no_jsonld": sum(1 for r in ok if r["jsonld_blocks"] == 0),
        "no_hreflang": sum(1 for r in ok if r["hreflang_count"] == 0),
        "missing_h1": sum(1 for r in ok if r["h1_count"] == 0),
        "multiple_h1": sum(1 for r in ok if r["h1_count"] > 1),
        "title_short_lt30": sum(1 for r in ok if 0 < r["title_len"] < 30),
        "title_long_gt65": sum(1 for r in ok if r["title_len"] > 65),
        "title_missing": sum(1 for r in ok if r["title_len"] == 0),
        "meta_missing": sum(1 for r in ok if r["meta_desc_len"] == 0),
        "meta_short_lt120": sum(1 for r in ok if 0 < r["meta_desc_len"] < 120),
        "meta_long_gt160": sum(1 for r in ok if r["meta_desc_len"] > 160),
        "thin_content_lt300": sum(1 for r in ok if r["word_count"] < 300),
        "noindex_pages": sum(1 for r in ok if r["noindex"]),
        "missing_viewport": sum(1 for r in ok if not r["has_viewport"]),
        "images_missing_alt_pages": sum(1 for r in ok if r["images_missing_alt"] > 0),
    }
    with open(os.path.join(args.out, "crawl_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2), file=sys.stderr)
    print(f"\nSaved: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
