<!-- Updated: 2026-03-02 -->

# Ahrefs API Reference

MCP tool names, response fields, and critical conventions for all Ahrefs-powered
`/seo ahrefs` commands. Load this file on-demand when building or executing any
Ahrefs sub-skill.

## CRITICAL: Monetary Values — Always Divide by 100

All monetary values from the Ahrefs MCP are returned in CENTS, not dollars.
Before displaying ANY monetary value to the user:
  - Divide by 100
  - Format as USD: "$X,XXX" (with comma thousands separators)

Example:
  - API returns: `traffic_cost = 125000`
  - Display as: `$1,250`

This applies to all fields ending in `_cost`, `_value`, or `cpc`:
  - `traffic_cost` → divide by 100 → display as USD
  - `traffic_value` → divide by 100 → display as USD
  - `cpc` → divide by 100 → display as USD per click

NEVER display raw cents to the user. This is a required convention for all
Ahrefs sub-skills. Document it in each sub-skill that uses monetary fields.

## Tool Name Mapping

Each `/seo ahrefs` sub-command maps to one or more MCP tools:

| Sub-command | MCP Tool(s) |
|-------------|-------------|
| `overview` | `mcp__claude_ai_ahrefs__site-explorer-metrics`, `mcp__claude_ai_ahrefs__site-explorer-domain-rating` |
| `backlinks` | `mcp__claude_ai_ahrefs__site-explorer-all-backlinks` |
| `keywords` | `mcp__claude_ai_ahrefs__site-explorer-organic-keywords` |
| `competitors` | `mcp__claude_ai_ahrefs__site-explorer-organic-competitors` |
| `content-gap` | `mcp__claude_ai_ahrefs__keywords-explorer-matching-terms` (filtered by competitor domain) |
| `broken-links` | `mcp__claude_ai_ahrefs__site-explorer-broken-backlinks` |
| `new-links` | `mcp__claude_ai_ahrefs__site-explorer-referring-domains` (date-filtered to last 30 days) |
| `anchor-analysis` | `mcp__claude_ai_ahrefs__site-explorer-anchors` |
| `dr-history` | `mcp__claude_ai_ahrefs__site-explorer-domain-rating-history` |
| `top-pages` | `mcp__claude_ai_ahrefs__site-explorer-top-pages` |

Additional Ahrefs tools available (for Phase 3 commands):
- `mcp__claude_ai_ahrefs__brand-radar-mentions-overview` — used by `/seo brand-radar`

## Common Response Fields

Key fields returned by Ahrefs MCP tools that sub-skills will use:

### Site Explorer Metrics
- `domain_rating` — DR score 0-100 (no conversion needed)
- `ahrefs_rank` — Global rank by backlinks
- `organic_traffic` — Estimated monthly organic visits (no conversion needed)
- `traffic_cost` — Estimated monthly traffic value in CENTS → divide by 100 for USD
- `organic_keywords` — Number of ranking keywords
- `backlinks` — Total backlink count
- `referring_domains` — Unique linking domains count

### Organic Keywords
- `keyword` — The search query
- `position` — Current ranking position
- `volume` — Monthly search volume
- `cpc` — Cost per click in CENTS → divide by 100 for USD
- `traffic` — Estimated clicks from this keyword
- `traffic_percent` — Share of total organic traffic

### Backlinks
- `url_from` — The linking page URL
- `url_to` — The target page URL
- `anchor` — Anchor text used
- `domain_rating_source` — DR of the linking domain
- `first_seen` — Date link was first discovered (ISO 8601)
- `lost_date` — Date link was lost, if applicable

### Domain Rating History
- `date` — Data point date (ISO 8601)
- `domain_rating` — DR score on that date
- `ahrefs_rank` — Global rank on that date

### Top Pages
- `url` — Page URL
- `traffic` — Estimated monthly visits
- `traffic_percent` — Share of total site traffic
- `keywords` — Number of ranking keywords for this page
- `top_keyword` — Highest-traffic keyword for this page

## Rate Limiting and API Unit Costs

The Ahrefs MCP has per-call API unit costs. Each tool invocation consumes units
from the account's monthly allocation.

**Guidelines:**
- Be mindful of API usage — avoid redundant calls
- Cache results within a session where possible (do not re-call same endpoint for same domain)
- For `site-audit-pro`, design calls sequentially to avoid waste on aborted runs
- Exact unit costs per endpoint: TBD — verify against account before Phase 3 planning
  (tracked as Phase 2 blocker in STATE.md)

**Priority order for multi-tool commands:**
1. Call highest-value tools first (metrics, DR)
2. Call detail tools (backlinks, keywords) only if needed for the specific analysis
3. Avoid calling tools whose data the user did not explicitly request

## MCP Availability Check

Before calling any Ahrefs tool, verify the MCP is connected:
```
Use ToolSearch with query "+ahrefs"
- Tools returned → proceed
- No tools → use error template in references/mcp-degradation.md
```

## Input Format

Most Ahrefs MCP tools accept a `target` parameter:
- For domain-level queries: use bare domain `example.com` (no https://)
- For URL-level queries: use full URL `https://example.com/page`
- For subdomains: use `subdomain.example.com`

Verify exact parameter names against live MCP tool signatures before building
each sub-skill (tool definitions may differ from documented names).
