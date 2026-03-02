<!-- Updated: 2026-03-02 -->

# GSC API Reference

Tool name mapping, property formats, and response fields for Google Search Console
MCP. Load this file on-demand when building or executing any GSC sub-skill.

IMPORTANT: Many values in this file are marked TBD or UNVERIFIED. The GSC MCP
tool names and property format must be discovered and verified in Phase 2 before
any GSC commands can be built. Do not assume any placeholder values are correct.

## GSC MCP Tool Mapping (to be verified in Phase 2)

GSC MCP source: `/Users/aash-zsbch1500/Desktop/GSC-MCP`
Tool name pattern: TBD — must be discovered when GSC commands are built.

Run `ToolSearch "+google-search-console"` to discover actual tool names before
building any GSC sub-skill.

Placeholder mapping (DO NOT USE until verified):

| Sub-command | Expected MCP Tool | Verified |
|-------------|-------------------|----------|
| `overview` | TBD | No |
| `drops` | TBD | No |
| `opportunities` | TBD | No |
| `pages` | TBD | No |
| `queries` | TBD | No |
| `indexing` | TBD | No |
| `cannibalization` | TBD | No |
| `compare` | TBD | No |
| `sitemaps` | TBD | No |

**Phase 2 action:** When building the first GSC sub-skill, use ToolSearch to
discover all available GSC MCP tools and update this table with verified names.

## GSC Property Format — UNVERIFIED

The GSC MCP property format has NOT been verified against the actual MCP server.
Possible formats accepted by the GSC MCP:
  - `"sc-domain:example.com"` (domain property — covers all subdomains and protocols)
  - `"https://example.com"` (URL prefix property — covers exact URL prefix only)

MUST be tested before building GSC commands in Phase 2.
See STATE.md blocker: "GSC MCP property format unverified"

**Phase 2 action:** Test both property formats against a known verified GSC
property before writing any sub-skill that accepts user-provided site URLs.

**User-facing guidance (once format is confirmed):**
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

### Sitemaps
- `path` — Sitemap URL
- `last_submitted` — Date last submitted (ISO 8601)
- `last_downloaded` — Date last downloaded by Google (ISO 8601)
- `warnings` — Warning count
- `errors` — Error count
- `contents` — Breakdown by content type (URL count, indexed count)

## CTR Display Convention

GSC returns CTR as a decimal (0.0523 = 5.23%).
When displaying CTR to users, always multiply by 100 and append `%`:
  - API returns: `ctr = 0.0523`
  - Display as: `5.23%`

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
- Tools returned → proceed (use discovered tool names, not placeholders above)
- No tools → use GSC error template in references/mcp-degradation.md
```

If no GSC tools found, also check if GSC MCP needs registration:
```
cat ~/.claude/mcp.json | grep -i "google\|gsc"
- Entry found but tools not loading → restart Claude Desktop and retry
- No entry → user must register GSC MCP from /Users/aash-zsbch1500/Desktop/GSC-MCP
```

## Phase 2 Discovery Checklist

Before building any GSC sub-skill, complete these verification steps:

- [ ] Run ToolSearch and document all available GSC MCP tool names
- [ ] Test property format: try `sc-domain:example.com` vs `https://example.com`
- [ ] Verify response field names match expected fields above
- [ ] Test date range parameter format (string vs object vs epoch)
- [ ] Confirm row limit and pagination behavior
- [ ] Update this file with verified tool names and field names
- [ ] Remove TBD placeholders from the tool mapping table above
