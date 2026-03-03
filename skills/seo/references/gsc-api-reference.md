<!-- Updated: 2026-03-03 — verified from GSC MCP source -->

# GSC API Reference

Tool name mapping, property formats, and response fields for Google Search Console
MCP. Load this file on-demand when building or executing any GSC sub-skill.

## GSC MCP Tool Mapping (Verified from Source)

Tool name prefix: depends on alias used during registration in `~/.claude/mcp.json`.
Use ToolSearch at runtime to discover the actual prefix — see MCP Availability Check below.

Verified mapping (from GSC MCP source):

| Sub-command | GSC MCP Tool | Key Params | Verified |
|-------------|-------------|-----------|----------|
| `overview` | `query_search_analytics` (x2: query + page dimensions) | siteUrl, startDate, endDate, dimensions, rowLimit | Yes (source) |
| `drops` | `compare_performance` | siteUrl, 4 date params, dimension=page | Yes (source) |
| `opportunities` | `find_keyword_opportunities` | siteUrl, startDate, endDate, minImpressions, maxCtr, maxPosition | Yes (source) |
| `cannibalization` | `query_search_analytics` | siteUrl, dates, dimensions=["query","page"] | Yes (source) |
| `index-issues` | `inspect_url` (per URL, cap at 20) | siteUrl, inspectionUrl | Yes (source) |
| `compare` | `compare_performance` | siteUrl, 4 date params, dimension | Yes (source) |
| `brand-vs-nonbrand` | `analyze_brand_queries` | siteUrl, dates, brandTerms (user-provided) | Yes (source) |
| `content-decay` | `compare_performance` | siteUrl, 90-day window, dimension=page | Yes (source) |
| `new-keywords` | `compare_performance` | siteUrl, 28-day window, filter previousClicks=0 | Yes (source) |

## Additional GSC Tools Available

These tools are available in the GSC MCP but not directly mapped to a single sub-command:

- `list_accounts` — no params, returns connected Google accounts
- `list_sites` — optional `account`, returns properties for account
- `get_top_pages` — siteUrl, startDate, endDate, sortBy, limit — used within overview
- `get_keyword_trend` — siteUrl, keyword, startDate, endDate — for keyword-specific drilldown
- `export_analytics` — siteUrl, startDate, endDate, dimensions, format — data export

## GSC Property Format — VERIFIED (from source)

Both property formats are accepted by the GSC MCP server:
  - `"sc-domain:example.com"` (domain property — covers all subdomains and protocols)
  - `"https://example.com"` (URL prefix property — covers exact URL prefix only)

Source: verified from GSC MCP source

**User-facing guidance:**
When asking the user for their site, clarify which property type they added to
GSC and accept both formats gracefully:
  - Domain property: `sc-domain:example.com`
  - URL prefix: `https://example.com` or `https://www.example.com`

## Expected Response Fields

Standard GSC metrics that all sub-commands are expected to return. Verify field
names against live MCP responses before use — these are based on the GSC API
specification and may differ in the MCP wrapper.

### Performance Data (clicks, impressions, CTR, position)
- `clicks` — Number of clicks from Google Search (integer)
- `impressions` — Number of times shown in search results (integer)
- `ctr` — Click-through rate as decimal, e.g. 0.0523 = 5.23% (multiply by 100 for display)
- `position` — Average ranking position (float, lower is better)

### Dimension Values
- `query` — The search query string
- `page` — The URL of the ranking page (full URL)
- `date` — Date in YYYY-MM-DD format
- `device` — "DESKTOP", "MOBILE", or "TABLET"
- `country` — ISO 3166-1 alpha-3 country code (e.g., "USA", "GBR")

### Index Coverage
- `coverage_state` — Coverage status (e.g., "Submitted and indexed", "Excluded")
- `url` — The page URL
- `last_crawled` — Date of last crawl (ISO 8601)
- `indexing_state` — Whether the page is indexed

## CTR Display Rule

`query_search_analytics` returns CTR as a decimal (0.0523 = 5.23%).
When displaying CTR to users, always multiply by 100 and append `%`:
  - API returns: `ctr = 0.0523`
  - Display as: `5.23%`

Note: The GSC MCP's formatted output may convert this automatically, but raw API
responses do not. Always apply this conversion when rendering CTR values.

## Date Range Conventions

Common date ranges used across GSC sub-commands:
- Last 7 days: `startDate = today - 7 days`
- Last 28 days: `startDate = today - 28 days` (GSC standard comparison period)
- Last 3 months: `startDate = today - 90 days`
- Last 12 months: `startDate = today - 365 days`
- Year-over-year: compare same 28-day period vs same period prior year

## MCP Availability Check

Before calling any GSC tool, verify the MCP is connected:
```
Use ToolSearch with query "+google-search-console"
- Tools returned → proceed (use discovered tool names with actual prefix, not bare names above)
- No tools → use GSC error template in references/mcp-degradation.md
```

The GSC MCP server is registered as `gsc-mcp-server` in its package.json. The tool
name prefix depends on the alias used during registration in `~/.claude/mcp.json`.
Use ToolSearch to discover the actual prefix at runtime. Example patterns:
  - `mcp__gsc-mcp-server__query_search_analytics`
  - `mcp__google-search-console__query_search_analytics`

If no GSC tools found, also check if GSC MCP needs registration:
```
cat ~/.claude/mcp.json | grep -i "google\|gsc"
- Entry found but tools not loading → restart Claude Desktop and retry
- No entry → user must install and register a GSC MCP server (see README for setup)
```

## Phase 2 Discovery Checklist

- [x] Run ToolSearch and document all available GSC MCP tool names (verified from source)
- [x] Property format: both `sc-domain:example.com` and `https://example.com` accepted (verified from source)
- [ ] Verify response field names match expected fields above (need live testing)
- [ ] Test date range parameter format (string vs object vs epoch) (need live testing)
- [ ] Confirm row limit and pagination behavior (need live testing)
- [ ] Discover registered MCP alias (need runtime ToolSearch)
