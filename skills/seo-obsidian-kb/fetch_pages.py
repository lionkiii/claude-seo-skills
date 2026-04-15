#!/usr/bin/env python3
"""
SEO Obsidian KB - Bulk Page Fetcher

Fetches all pages from a sitemap, extracts SEO-relevant data,
and builds a link adjacency map. Outputs JSON for Claude agents
to transform into Obsidian-optimized markdown notes.

Usage:
    python3 fetch_pages.py --sitemap URL [--output FILE] [--concurrency N] [--lang LANG]
"""

import argparse
import asyncio
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.parse import urljoin, urlparse

import ssl

import aiohttp
from bs4 import BeautifulSoup


# Language path segments to filter out (keep English only by default)
NON_EN_PATHS = {
    "/ar/", "/de/", "/es/", "/es-xl/", "/fr/", "/id/", "/it/", "/ja/",
    "/jp/", "/ko/", "/nl/", "/pt/", "/pt-br/", "/ru/", "/th/", "/tr/",
    "/vi/", "/zh/", "/zh-cn/", "/zh-tw/", "/sv/", "/da/", "/fi/", "/nb/",
    "/pl/", "/cs/", "/hu/", "/ro/", "/bg/", "/el/", "/he/", "/hi/",
    "/ms/", "/tl/", "/uk/",
    # Zoho-specific non-EN subdomains/paths
    "/com.cn/", "/com.au/", "/com.br/", "/co.in/", "/co.uk/", "/eu/",
    "/in/", "/sa/",
}


def is_english_url(url: str) -> bool:
    """Filter out non-English locale URLs."""
    parsed = urlparse(url)
    path = parsed.path.lower()
    netloc = parsed.netloc.lower()
    for seg in NON_EN_PATHS:
        if seg in path or seg.strip("/") in netloc:
            return False
    return True


async def fetch_sitemap(session: aiohttp.ClientSession, url: str) -> list[str]:
    """Parse a sitemap (or sitemap index) and return all page URLs."""
    urls = []
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as resp:
            if resp.status != 200:
                print(f"  [WARN] Sitemap {url} returned {resp.status}", file=sys.stderr)
                return urls
            text = await resp.text()
    except Exception as e:
        print(f"  [ERR] Failed to fetch sitemap {url}: {e}", file=sys.stderr)
        return urls

    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        print(f"  [ERR] Failed to parse XML from {url}", file=sys.stderr)
        return urls

    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    # Check if this is a sitemap index
    sub_sitemaps = root.findall(".//s:sitemap/s:loc", ns)
    if sub_sitemaps:
        print(f"  Found sitemap index with {len(sub_sitemaps)} sub-sitemaps", file=sys.stderr)
        tasks = [fetch_sitemap(session, sm.text.strip()) for sm in sub_sitemaps]
        results = await asyncio.gather(*tasks)
        for r in results:
            urls.extend(r)
    else:
        locs = root.findall(".//s:url/s:loc", ns)
        urls = [loc.text.strip() for loc in locs if loc.text]

    return urls


def categorize_url(url: str, base_path: str) -> tuple[str, str]:
    """Derive category and slug from URL path."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")

    # Remove base product path
    if base_path and path.startswith(base_path.rstrip("/")):
        path = path[len(base_path.rstrip("/")):]

    path = path.lstrip("/")

    # Remove .html extension
    path = re.sub(r"\.html?$", "", path)

    parts = [p for p in path.split("/") if p]

    if len(parts) == 0:
        return "core", "index"
    elif len(parts) == 1:
        return "core", parts[0]
    else:
        return parts[0], "-".join(parts[1:]) if len(parts) > 2 else parts[-1]


def extract_page_data(html: str, url: str, base_path: str, domain: str) -> dict:
    """Extract SEO-relevant data from HTML."""
    soup = BeautifulSoup(html, "lxml")

    # Title
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    # H1
    h1_tag = soup.find("h1")
    h1 = h1_tag.get_text(strip=True) if h1_tag else ""

    # Meta description
    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    # Heading outline (H2/H3)
    headings = []
    for tag in soup.find_all(["h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and len(text) < 200:
            headings.append({"level": int(tag.name[1]), "text": text})

    # Word count (main content, strip nav/footer/scripts)
    for el in soup.find_all(["script", "style", "nav", "footer", "header"]):
        el.decompose()
    body = soup.find("body")
    text_content = body.get_text(separator=" ", strip=True) if body else ""
    word_count = len(text_content.split())

    # Internal links
    internal_links = []
    external_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        anchor = a_tag.get_text(strip=True)
        if not anchor or len(anchor) > 200:
            continue

        abs_url = urljoin(url, href)
        parsed_link = urlparse(abs_url)

        # Skip non-http, anchors, javascript
        if parsed_link.scheme not in ("http", "https"):
            continue

        # Clean URL (remove fragments and query params for comparison)
        clean_url = f"{parsed_link.scheme}://{parsed_link.netloc}{parsed_link.path}"

        if domain in parsed_link.netloc:
            internal_links.append({"url": clean_url, "anchor": anchor})
        else:
            external_links.append({"url": clean_url, "anchor": anchor})

    # Schema.org detection
    schema_types = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict) and "@type" in data:
                schema_types.append(data["@type"])
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "@type" in item:
                        schema_types.append(item["@type"])
        except (json.JSONDecodeError, TypeError):
            pass

    # Categorize
    category, slug = categorize_url(url, base_path)

    return {
        "url": url,
        "category": category,
        "slug": slug,
        "title": title,
        "h1": h1,
        "meta_description": meta_desc,
        "headings": headings,
        "word_count": word_count,
        "has_schema": len(schema_types) > 0,
        "schema_types": list(set(schema_types)),
        "internal_links": internal_links,
        "external_links_count": len(external_links),
    }


async def fetch_page(
    session: aiohttp.ClientSession,
    url: str,
    base_path: str,
    domain: str,
    semaphore: asyncio.Semaphore,
) -> dict | None:
    """Fetch a single page and extract data."""
    async with semaphore:
        try:
            async with session.get(
                url, timeout=aiohttp.ClientTimeout(total=20)
            ) as resp:
                if resp.status != 200:
                    print(f"  [SKIP] {url} -> {resp.status}", file=sys.stderr)
                    return None
                html = await resp.text()
                return extract_page_data(html, url, base_path, domain)
        except Exception as e:
            print(f"  [ERR] {url}: {e}", file=sys.stderr)
            return None


def build_adjacency_map(pages: list[dict]) -> dict:
    """Build inbound link map from all pages' outbound links."""
    # Map URL -> slug for quick lookup
    url_to_slug = {}
    for p in pages:
        url_to_slug[p["url"]] = p["slug"]
        # Also map without trailing slash and with .html variants
        clean = p["url"].rstrip("/")
        url_to_slug[clean] = p["slug"]
        url_to_slug[clean + "/"] = p["slug"]

    # Build inbound links
    inbound = defaultdict(list)
    for page in pages:
        for link in page["internal_links"]:
            target_url = link["url"].rstrip("/")
            # Try matching
            target_slug = None
            for variant in [target_url, target_url + "/", target_url + ".html"]:
                if variant in url_to_slug:
                    target_slug = url_to_slug[variant]
                    break

            if target_slug and target_slug != page["slug"]:
                inbound[target_slug].append({
                    "from_slug": page["slug"],
                    "from_category": page["category"],
                    "anchor": link["anchor"],
                })

    return dict(inbound)


async def main():
    parser = argparse.ArgumentParser(description="Fetch pages from sitemap for Obsidian KB")
    parser.add_argument("--sitemap", required=True, help="Sitemap URL")
    parser.add_argument("--output", default="pages_data.json", help="Output JSON file")
    parser.add_argument("--concurrency", type=int, default=15, help="Max concurrent requests")
    parser.add_argument("--base-path", default="", help="URL base path for the product (e.g., /campaigns/)")
    parser.add_argument("--lang", default="en", help="Language filter (default: en)")
    args = parser.parse_args()

    domain = urlparse(args.sitemap).netloc

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # SSL context that skips verification (some corporate sites have cert issues)
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE

    connector = aiohttp.TCPConnector(ssl=ssl_ctx)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        # Step 1: Fetch sitemap
        print(f"Fetching sitemap: {args.sitemap}", file=sys.stderr)
        all_urls = await fetch_sitemap(session, args.sitemap)
        print(f"  Found {len(all_urls)} total URLs in sitemap", file=sys.stderr)

        # Step 2: Filter
        if args.lang == "en":
            all_urls = [u for u in all_urls if is_english_url(u)]
            print(f"  After English filter: {len(all_urls)} URLs", file=sys.stderr)

        # Auto-detect base path if not provided
        if not args.base_path and all_urls:
            parsed = urlparse(all_urls[0])
            parts = parsed.path.strip("/").split("/")
            if parts:
                args.base_path = f"/{parts[0]}/"
                print(f"  Auto-detected base path: {args.base_path}", file=sys.stderr)

        # Step 3: Fetch all pages
        semaphore = asyncio.Semaphore(args.concurrency)
        print(f"Fetching {len(all_urls)} pages (concurrency={args.concurrency})...", file=sys.stderr)

        tasks = [
            fetch_page(session, url, args.base_path, domain, semaphore)
            for url in all_urls
        ]
        results = await asyncio.gather(*tasks)

    # Filter out failures
    pages = [r for r in results if r is not None]
    print(f"  Successfully fetched {len(pages)} / {len(all_urls)} pages", file=sys.stderr)

    # Step 4: Build adjacency map
    inbound_map = build_adjacency_map(pages)

    # Add inbound link data to each page
    for page in pages:
        slug = page["slug"]
        page["inbound_links"] = inbound_map.get(slug, [])
        page["internal_links_in_count"] = len(page["inbound_links"])
        page["internal_links_out_count"] = len(page["internal_links"])

    # Step 5: Resolve outbound links to slugs
    url_to_info = {}
    for p in pages:
        url_to_info[p["url"].rstrip("/")] = {"slug": p["slug"], "category": p["category"], "title": p["title"]}

    for page in pages:
        resolved_outbound = []
        for link in page["internal_links"]:
            clean = link["url"].rstrip("/")
            if clean in url_to_info:
                info = url_to_info[clean]
                resolved_outbound.append({
                    "slug": info["slug"],
                    "category": info["category"],
                    "title": info["title"],
                    "anchor": link["anchor"],
                })
        page["resolved_outbound_links"] = resolved_outbound

    # Summary stats
    categories = defaultdict(int)
    for p in pages:
        categories[p["category"]] += 1

    summary = {
        "total_pages": len(pages),
        "total_urls_in_sitemap": len(all_urls),
        "categories": dict(categories),
        "base_path": args.base_path,
        "domain": domain,
    }

    output = {
        "summary": summary,
        "pages": pages,
    }

    # Write output
    output_path = Path(args.output)
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\nOutput written to {output_path}", file=sys.stderr)
    print(f"Summary: {json.dumps(summary, indent=2)}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
