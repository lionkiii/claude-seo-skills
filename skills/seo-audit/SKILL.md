---
name: seo-audit
description: >
  Full website SEO audit producing an interactive multi-sheet XLSX workbook
  with per-issue Status dropdowns (To Do / In Progress / Done / Skipped / N/A)
  and row-level conditional formatting. Crawls up to 500 pages from a sitemap,
  extracts on-page/technical/schema/hreflang/content signals, overlays live
  Ahrefs (DR, traffic, keywords) and GSC (90-day clicks/impressions, device
  split, URL inspection) data when MCPs are available. Every finding links to
  the official Google Search Central / web.dev reference. Use when user says
  "audit", "full SEO check", "analyze my site", or "website health check".
allowed-tools:
  - Read
  - Bash
  - Glob
  - WebFetch
  - ToolSearch
---

# Full Website SEO Audit — XLSX Deliverable

## Deliverable

A single `.xlsx` file with up to 17 sheets, saved to a user-specified path
(default: `~/Desktop/seo-audit-{site}-{YYYY-MM-DD}.xlsx`).

**Every actionable row has a Status column** with a dropdown (data validation):
`To Do`, `In Progress`, `Done`, `Skipped`, `Not Applicable`.

Row auto-colours via conditional formatting:
- `Done` → green
- `Skipped` / `Not Applicable` → grey
- `In Progress` → soft yellow

Priority columns use red / orange / yellow / green for Critical / High /
Medium / Low. Opens cleanly in Excel, Numbers, and Google Sheets.

## Sheet layout (in order)

| # | Sheet | Purpose |
|---|---|---|
| 1 | Read Me | Scope, how to use, priority/effort definitions |
| 2 | Executive Summary | Overall health score, category scores, top critical findings |
| 3 | Action Plan | Master prioritised to-do list with Status + Priority + Effort dropdowns |
| 4 | On-Page Issues | Per-page title / meta / H1 problems (sorted by priority) |
| 5 | Schema Missing | Every page lacking JSON-LD + inferred page type + recommended schema |
| 6 | Hreflang Missing | Pages without hreflang in HTML `<head>` |
| 7 | Thin Content | Pages under 300 words with severity-tiered fix |
| 8 | Duplicate Titles & Meta | Groups of pages sharing the same title or meta |
| 9 | Image Issues | Pages with images missing `alt` |
| 10 | GSC - Top Pages *(if GSC available)* | 90-day clicks / impressions / CTR / position |
| 11 | GSC - Top Queries *(if GSC available)* | Branded vs non-branded flagged; low-CTR rows highlighted |
| 12 | Ahrefs - Top Pages *(if Ahrefs available)* | Monthly traffic / traffic value / keywords per page |
| 13 | Ahrefs - Keywords *(if Ahrefs available)* | Organic keywords ordered by traffic |
| 14 | Page Inventory | Every crawled URL with all extracted metrics (filterable) |
| 15 | Google References | Every authoritative doc cited throughout |

## Process

### 0. Confirm scope with user
Ask (in one message):
- Target URL or folder (e.g. `https://example.com` vs `https://example.com/blog/`)?
- Sitemap — auto-discover via `robots.txt` / `/sitemap.xml`, or user-provided URL?
- GSC date range — default last **90 days** (user may override, e.g. 28 days)?
- Enrich with Ahrefs + GSC if MCPs are available?
- Output path — default `~/Desktop/seo-audit-{site}-{YYYY-MM-DD}.xlsx`?
- Interactive XLSX with Status dropdowns — confirm (default yes)?

### 1. Crawl
Run `skills/seo/scripts/crawl_site.py`:
```
python crawl_site.py <base_url> \
    [--sitemap <sitemap_url>] \
    [--prefix <folder_url>] \
    [--max-pages 500] \
    [--no-ssl-verify] \
    --out <work_dir>
```
Emits `crawl_results.json` and `crawl_summary.json`.

**Per-page signals extracted:** status, final URL, title (+length), meta
description (+length), canonical (+self-match), robots meta, `X-Robots-Tag`,
`noindex`, H1 count + first text, H2 count, hreflang count, JSON-LD block
count + `@type`s, og/twitter tag counts, image count + missing-alt count, word
count, internal/external link counts, viewport/charset presence.

### 2. MCP availability check
Use `ToolSearch` with `"+ahrefs"` and `"+google-search-console"` (or `"+gsc"`)
to detect which live-data tools are loaded. Proceed with whichever is
available; skip the corresponding sheets if not.

### 3. Pull live data in parallel
**Google Search Console (if available):**
- `mcp__gsc__list_sites` — find the correct property. If multiple accounts
  exist you MUST pass the `account` parameter on every call.
- `mcp__gsc__get_top_pages` — last N days, sortBy `clicks`, limit 100.
- `mcp__gsc__query_search_analytics` — dimensions `["query"]`, rowLimit 200.
- `mcp__gsc__query_search_analytics` — dimensions `["device"]`, rowLimit 10.
- `mcp__gsc__inspect_url` — top 3-5 pages to confirm indexing + rich-result
  verdict.

**Ahrefs (if available):**
- `site-explorer-domain-rating` — DR + Ahrefs Rank.
- `site-explorer-metrics` with `mode=prefix` and target `www.{domain}/{path}/`
  (include `www.` and trailing slash). For a subfolder audit, prefix mode is
  correct; `subdomains` mode returns whole-domain data.
- `site-explorer-top-pages` (same target) — `select` supports `url`,
  `sum_traffic`, `value`, `top_keyword`, `top_keyword_volume`,
  `top_keyword_best_position`, `keywords`, `referring_domains`.
- `site-explorer-organic-keywords` (same target) — `select` supports
  `keyword`, `best_position`, `volume`, `cpc`, `sum_traffic`,
  `best_position_url`, `serp_features`, `is_branded`, `keyword_difficulty`.

Save each payload to JSON in the work dir. Monetary fields (`value`, `cpc`,
`traffic_cost`) are in **USD cents** — the builder divides by 100.

### 4. Build XLSX
Run `skills/seo/scripts/build_audit_xlsx.py`:
```
python build_audit_xlsx.py \
    --crawl <work_dir>/crawl_results.json \
    --site-name "example.com/blog" \
    --out ~/Desktop/seo-audit-example.com-YYYY-MM-DD.xlsx \
    [--gsc-top-pages <work_dir>/gsc_top_pages.json] \
    [--gsc-queries <work_dir>/gsc_queries.json] \
    [--gsc-devices <work_dir>/gsc_devices.json] \
    [--ahrefs-metrics <work_dir>/ahrefs_metrics.json] \
    [--ahrefs-top-pages <work_dir>/ahrefs_top_pages.json] \
    [--ahrefs-keywords <work_dir>/ahrefs_keywords.json] \
    [--dr 92] \
    [--brand-regex "brand|brnd|brnad"]
```

See `skills/seo-audit/scripts/README.md` for the JSON shapes each
`--*` flag expects.

### 5. Report summary to user
After the XLSX is written, print to the chat:
- Output path + file size.
- Overall score and the 5 most important findings (pulled from the Executive
  Summary sheet).
- Any missing MCP data (so the user knows which sheets are omitted).
- Invite the user to open the file and work the Action Plan using the Status
  dropdown.

## Scoring weights

| Category | Weight | What drives the score |
|---|---|---|
| Technical SEO | 25% | Hreflang in HTML, HTTPS/headers, robots, canonicals |
| Content Quality | 25% | Thin-content ratio, duplicate titles / meta |
| On-Page SEO | 20% | Title length, meta length, H1 count ratios |
| Schema / Structured Data | 10% | Fraction of pages with ≥1 JSON-LD block |
| Performance (CWV) | 10% | Default 70; override with real PageSpeed numbers |
| Images | 5% | Fraction of pages with all images tagged |
| AI Search Readiness | 5% | Derived from schema + thin-content fraction |

## Priority definitions

| Priority | Meaning | SLA |
|---|---|---|
| **Critical** | Blocks indexing / rich results / causes penalty | Fix immediately |
| **High** | Significantly impacts rankings or CTR | Within 1 week |
| **Medium** | Optimisation opportunity | Within 1 month |
| **Low** | Nice to have | Backlog |

## Effort definitions

| Effort | Meaning |
|---|---|
| **Easy** | Under 1 hour (copy change, single-file edit) |
| **Medium** | A few hours to a day (template change, schema generator) |
| **Hard** | Multi-day / cross-team (rewrites, performance work) |

## References used in the workbook

Every finding row in the XLSX links to the specific Google / web.dev /
MDN document that justifies the fix. See `skills/seo/references/` for the
maintained reference set, and the "Google References" sheet in every output
workbook for the full list with live hyperlinks.

## Common pitfalls

- **macOS Python SSL** — system Python often lacks a cert bundle. Pass
  `--no-ssl-verify` to `crawl_site.py`.
- **GSC "Multiple accounts found"** — always pass `account=` when
  more than one alias exists.
- **Ahrefs `prefix` mode needs `www.`** — a bare `example.com/blog/`
  target returns zero; `www.example.com/blog/` returns the correct
  subfolder data. Always include the `www.` subdomain if the site uses it.
- **Ahrefs `subdomains` mode returns whole-domain metrics** — do not use
  it for subfolder audits.
- **Ahrefs monetary values are cents** — builder divides by 100 for display.
- **Hreflang** — the sitemap may declare it while the HTML does not.
  Google accepts either; flag HTML-missing as a quality improvement, not a
  blocker, unless sitemap is also missing them.

## Python dependencies

Added in `skills/seo/requirements.txt`:
- `openpyxl>=3.1,<4.0` — XLSX build with data validation and conditional
  formatting.

Crawler uses only the Python standard library plus `concurrent.futures`.
