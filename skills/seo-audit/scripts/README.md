# seo-audit — Scripts and data formats

This directory documents the end-to-end pipeline for producing the
interactive XLSX deliverable. The actual Python lives in
`skills/seo/scripts/` so it can be shared with other SEO skills.

## Pipeline

```
           ┌───────────────┐
           │  crawl_site   │  ← sitemap → per-page SEO signals
           └───────┬───────┘
                   │  crawl_results.json
                   ▼
    ┌────────────────────────────┐        ┌─────────────────────────┐
    │  (optional) GSC MCP pulls  │        │  (optional) Ahrefs MCP  │
    │  → gsc_*.json              │        │  → ahrefs_*.json        │
    └──────────────┬─────────────┘        └──────────┬──────────────┘
                   │                                 │
                   └──────────┬──────────────────────┘
                              ▼
                    ┌──────────────────┐
                    │ build_audit_xlsx │
                    └────────┬─────────┘
                             ▼
           seo-audit-{site}-{YYYY-MM-DD}.xlsx
```

## Minimal invocation (no MCPs)

```bash
WORK=/tmp/seo-audit-$(date +%Y%m%d)
mkdir -p "$WORK"

python skills/seo/scripts/crawl_site.py https://example.com \
    --max-pages 500 --no-ssl-verify --out "$WORK"

python skills/seo/scripts/build_audit_xlsx.py \
    --crawl "$WORK/crawl_results.json" \
    --site-name "example.com" \
    --out ~/Desktop/seo-audit-example.com-$(date +%Y-%m-%d).xlsx
```

## Subfolder audit (e.g. `/blog/` only)

```bash
python skills/seo/scripts/crawl_site.py https://example.com \
    --sitemap https://example.com/sitemap.xml \
    --prefix  https://example.com/blog/ \
    --out "$WORK"
```

## Full invocation with live data

```bash
python skills/seo/scripts/build_audit_xlsx.py \
    --crawl         "$WORK/crawl_results.json" \
    --site-name     "example.com/blog" \
    --out           ~/Desktop/seo-audit-example.com-blog-$(date +%Y-%m-%d).xlsx \
    --gsc-top-pages "$WORK/gsc_top_pages.json" \
    --gsc-queries   "$WORK/gsc_queries.json" \
    --gsc-devices   "$WORK/gsc_devices.json" \
    --ahrefs-metrics   "$WORK/ahrefs_metrics.json" \
    --ahrefs-top-pages "$WORK/ahrefs_top_pages.json" \
    --ahrefs-keywords  "$WORK/ahrefs_keywords.json" \
    --dr 68 \
    --brand-regex "example|exmple|exmaple"
```

## JSON data-file shapes

### `gsc_top_pages.json` (list of rows)
```json
[
  {"url": "https://example.com/", "clicks": 104137, "impressions": 3272745, "ctr": 3.18, "position": 19.7},
  ...
]
```
(Field `page` is also accepted as an alias for `url`. `ctr` may be a decimal
or a percentage; the builder uses the number as-is, so pass percentages if
that's how you store them.)

### `gsc_queries.json`
```json
[
  {"query": "example brand", "clicks": 73060, "impressions": 99424, "ctr": 73.48, "position": 1.7},
  ...
]
```

### `gsc_devices.json`
```json
[
  {"device": "DESKTOP", "clicks": 125561, "impressions": 3742693, "ctr": 3.35, "position": 16.7},
  {"device": "MOBILE",  "clicks":   6884, "impressions":  606256, "ctr": 1.14, "position": 31.5},
  {"device": "TABLET",  "clicks":    365, "impressions":   15221, "ctr": 2.40, "position": 12.8}
]
```

### `ahrefs_metrics.json`
```json
{
  "org_keywords": 512,
  "org_traffic": 8879,
  "org_cost": 6244945
}
```
(`org_cost` is USD cents; builder displays if needed.)

### `ahrefs_top_pages.json`
```json
[
  {
    "url": "https://example.com/",
    "sum_traffic": 6674,
    "value": 4905726,
    "top_keyword": "example brand",
    "top_keyword_volume": 5500,
    "top_keyword_best_position": 1,
    "keywords": 290,
    "referring_domains": 1363
  },
  ...
]
```
(`value` is USD cents.)

### `ahrefs_keywords.json`
```json
[
  {
    "keyword": "example brand",
    "best_position": 1,
    "volume": 5500,
    "cpc": 748,
    "sum_traffic": 5652,
    "best_position_url": "https://example.com/",
    "serp_features": ["sitelink", "question"],
    "is_branded": true,
    "keyword_difficulty": 6
  },
  ...
]
```
(`cpc` is USD cents.)

## Dumping MCP payloads to files

When Claude invokes the GSC / Ahrefs MCP tools inside this skill, write
each payload to the working directory before calling the builder:

```python
# pseudocode — done by the skill runner, not by hand
with open(f"{work_dir}/gsc_top_pages.json", "w") as f:
    json.dump(gsc_top_pages_payload, f)
```

## Output file

`~/Desktop/seo-audit-{site}-{YYYY-MM-DD}.xlsx` (or whatever path the user
supplied). Opens in Excel, Numbers, LibreOffice, and Google Sheets. Status
dropdowns are standard Excel data validation; conditional formatting uses
standard Excel formulae so row colours update live as the user toggles
dropdowns.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Every URL returns status 0 with SSL error | macOS system Python missing certifi | Pass `--no-ssl-verify` |
| GSC call: "Multiple accounts found" | Multiple account aliases configured | Pass `account=` on every call |
| Ahrefs returns 0s for subfolder | `mode=prefix` with bare `domain.com/path/` | Use `www.domain.com/path/` |
| Ahrefs returns whole-domain numbers | `mode=subdomains` is site-wide | Use `mode=prefix` for subfolder |
| Duplicate-title sheet is empty | All titles unique in crawl | Expected — no duplicates is a pass |
| Many "Title missing" rows | JS-rendered titles (SPA) | Add Playwright-rendered crawl mode (future work) |
