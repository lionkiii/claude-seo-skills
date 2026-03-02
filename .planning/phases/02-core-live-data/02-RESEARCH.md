# Phase 2: Core Live Data - Research

**Researched:** 2026-03-02
**Domain:** Claude Code skill authoring, GSC MCP integration, Ahrefs MCP integration, markdown SEO analysis
**Confidence:** HIGH — GSC MCP source was read directly from disk; Ahrefs MCP tool names were verified in Phase 1 and encoded in `ahrefs-api-reference.md`; skill patterns were verified by reading existing Phase 1 implementations

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| GSC-01 | `/seo gsc overview <site>` — clicks, impressions, CTR, avg position dashboard | GSC MCP `query_search_analytics` with `["query"]` + `["page"]` dimensions over last 28 days |
| GSC-02 | `/seo gsc drops <site>` — pages/keywords that lost traffic (28-day comparison) | GSC MCP `compare_performance` with 28-day current vs 28-day prior periods, dimension=page and query |
| GSC-03 | `/seo gsc opportunities <site>` — high impressions + low CTR keywords | GSC MCP `find_keyword_opportunities` (dedicated tool with `minImpressions`, `maxCtr`, `maxPosition` params) |
| GSC-04 | `/seo gsc cannibalization <site>` — multiple pages ranking for same keyword | GSC MCP `query_search_analytics` with dimensions `["query", "page"]` — same query appearing for 2+ pages |
| GSC-05 | `/seo gsc index-issues <site>` — pages not indexed with reasons | GSC MCP `inspect_url` per page — returns `coverageState`, `indexingState`, `pageFetchState`, `robotsTxtState` |
| GSC-06 | `/seo gsc compare <site>` — period-over-period comparison | GSC MCP `compare_performance` (dedicated tool for MoM, YoY comparison) |
| GSC-07 | `/seo gsc brand-vs-nonbrand <site>` — brand traffic split analysis | GSC MCP `analyze_brand_queries` (dedicated tool requiring `brandTerms` array from user) |
| GSC-08 | `/seo gsc content-decay <site>` — pages losing rankings over 90 days | GSC MCP `compare_performance` with 90-day window, dimension=page, filter for negative clicksChange |
| GSC-09 | `/seo gsc new-keywords <site>` — keywords started ranking for recently | GSC MCP `compare_performance` with 28-day window, filter for previousClicks=0 and currentClicks>0 |
| AHRF-01 | `/seo ahrefs overview <domain>` — DR, backlinks, organic keywords, traffic in USD | Ahrefs `site-explorer-metrics` + `site-explorer-domain-rating`; divide traffic_cost by 100 |
| AHRF-02 | `/seo ahrefs backlinks <domain>` — top backlinks with DR, anchor text, dofollow | Ahrefs `site-explorer-all-backlinks` |
| AHRF-03 | `/seo ahrefs keywords <domain>` — top organic keywords with position, volume, traffic | Ahrefs `site-explorer-organic-keywords` |
| AHRF-04 | `/seo ahrefs competitors <domain>` — organic competitors with keyword overlap | Ahrefs `site-explorer-organic-competitors` |
| AHRF-05 | `/seo ahrefs content-gap <domain>` — keywords competitors rank for that target doesn't | Ahrefs `keywords-explorer-matching-terms` filtered by competitor domain |
| AHRF-06 | `/seo ahrefs broken-links <domain>` — broken backlinks for link reclamation | Ahrefs `site-explorer-broken-backlinks` |
| AHRF-07 | `/seo ahrefs new-links <domain>` — recently acquired/lost backlinks | Ahrefs `site-explorer-referring-domains` date-filtered to last 30 days |
| AHRF-08 | `/seo ahrefs anchor-analysis <domain>` — anchor text distribution | Ahrefs `site-explorer-anchors` |
| AHRF-09 | `/seo ahrefs dr-history <domain>` — Domain Rating trend over time | Ahrefs `site-explorer-domain-rating-history` |
| AHRF-10 | `/seo ahrefs top-pages <domain>` — best performing pages by traffic | Ahrefs `site-explorer-top-pages` |
| LOCAL-01 | `/seo markdown-audit <path>` — analyze local markdown file for SEO (no MCP needed) | Pure file read + content analysis, no external calls |
</phase_requirements>

---

## Summary

Phase 2 builds 20 new sub-skill directories (9 GSC + 10 Ahrefs + 1 markdown-audit), each following the flat skill pattern established in Phase 1. The critical finding from reading the GSC MCP source code directly (`/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP/src/index.ts`) is that **all GSC tool names are now known** — the STATE.md blocker "GSC MCP property format unverified" is partially resolved: the MCP accepts both `sc-domain:example.com` and `https://example.com` as confirmed by its own tool descriptions. The MCP registered name prefix (which determines ToolSearch discovery patterns) is not yet confirmed but can be discovered at runtime using `ToolSearch "+gsc"` or `ToolSearch "+search_analytics"`.

The Ahrefs MCP tool names were verified in Phase 1 and are locked in `skills/seo/references/ahrefs-api-reference.md`. The tool prefix `mcp__claude_ai_ahrefs__` is confirmed from Phase 1 research and runtime observation. All 10 Ahrefs sub-commands map cleanly to existing Ahrefs MCP tools with no gaps.

The markdown-audit command requires no MCP and is structurally the simplest — it reads a local file and applies SEO heuristics. It should be implemented as a self-contained skill with zero external dependencies, making it the best candidate to build first as a confidence check before MCP-dependent work begins.

**Primary recommendation:** Build in this order — (1) `seo-markdown-audit` to establish the sub-skill file pattern with no MCP risk, (2) one GSC sub-skill to verify the MCP registration name and property format live, (3) remaining GSC sub-skills, (4) all Ahrefs sub-skills. Structure each sub-skill as a standalone flat directory with one SKILL.md containing all command logic.

---

## Standard Stack

### Core

| Component | Version/Source | Purpose | Why Standard |
|-----------|---------------|---------|--------------|
| Claude Code skill SKILL.md | Phase 1 pattern | Defines command behavior, routing trigger, MCP check | Established in Phase 1; all 12 active sub-skills use this pattern |
| GSC MCP (local) | `/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP` | Live GSC data — analytics, inspection, sitemaps | Only connected GSC data source; user-built, source available |
| Ahrefs MCP (claude.ai) | `mcp__claude_ai_ahrefs__*` tool prefix | Live Ahrefs data — DR, backlinks, keywords, competitors | Already integrated; tool names verified in Phase 1 |
| `references/mcp-degradation.md` | Phase 1 artifact | MCP check patterns and error templates | Every MCP-dependent sub-skill must @-reference this |
| `references/ahrefs-api-reference.md` | Phase 1 artifact | Tool-to-subcommand map, monetary conversion rule | Prevents cents-as-dollars bugs; all Ahrefs sub-skills load this |
| `references/gsc-api-reference.md` | Phase 1 artifact (to be updated) | GSC tool names and property format documentation | Must be updated with verified tool names after first GSC sub-skill |

### Supporting

| Component | Purpose | When to Use |
|-----------|---------|-------------|
| ToolSearch tool | MCP availability detection at runtime | Start of every MCP-dependent sub-skill execution |
| Read tool | Load local markdown files for audit | `seo-markdown-audit` only |
| Bash tool | Date arithmetic for GSC date ranges | Any GSC sub-skill needing dynamic date calculation |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Flat sub-skill directories | Nested `seo/gsc/SKILL.md` structure | Flat pattern matches existing 12 sub-skills; nesting was explicitly rejected in Phase 1 CONTEXT.md |
| Single mega-GSC skill with all 9 sub-commands | 9 separate skills | Separate skills allow independent loading and avoid context bloat; follows existing pattern |
| Agent file for GSC/Ahrefs analyst | Logic in SKILL.md | Phase 1 decision: "Logic lives in each sub-skill's SKILL.md; agents only for parallel audit work" |

---

## Architecture Patterns

### Recommended Project Structure

```
skills/
├── seo-gsc-overview/
│   └── SKILL.md          # All logic, MCP check, output format
├── seo-gsc-drops/
│   └── SKILL.md
├── seo-gsc-opportunities/
│   └── SKILL.md
├── seo-gsc-cannibalization/
│   └── SKILL.md
├── seo-gsc-index-issues/
│   └── SKILL.md
├── seo-gsc-compare/
│   └── SKILL.md
├── seo-gsc-brand-vs-nonbrand/
│   └── SKILL.md
├── seo-gsc-content-decay/
│   └── SKILL.md
├── seo-gsc-new-keywords/
│   └── SKILL.md
├── seo-ahrefs-overview/
│   └── SKILL.md
├── seo-ahrefs-backlinks/
│   └── SKILL.md
├── seo-ahrefs-keywords/
│   └── SKILL.md
├── seo-ahrefs-competitors/
│   └── SKILL.md
├── seo-ahrefs-content-gap/
│   └── SKILL.md
├── seo-ahrefs-broken-links/
│   └── SKILL.md
├── seo-ahrefs-new-links/
│   └── SKILL.md
├── seo-ahrefs-anchor-analysis/
│   └── SKILL.md
├── seo-ahrefs-dr-history/
│   └── SKILL.md
├── seo-ahrefs-top-pages/
│   └── SKILL.md
└── seo-markdown-audit/
    └── SKILL.md
```

Note: The routing table in `seo/SKILL.md` maps these directory names. The directories must match exactly the names used in the routing table (verified in `seo/SKILL.md` Phase 1 artifact).

### Pattern 1: MCP-Dependent Sub-Skill Structure

**What:** Every GSC and Ahrefs sub-skill follows this exact structure
**When to use:** Any command that calls an external MCP tool

```markdown
---
name: seo-gsc-overview
description: >
  [Trigger phrases that activate this skill]
---

# GSC Overview

## MCP Check

Load `references/mcp-degradation.md`.

Use ToolSearch with query "+gsc" (or "+google-search-console"):
- If tools returned → proceed with the verified tool names
- If no tools → display GSC error template from mcp-degradation.md, stop

## Execution

1. [Step 1 — what MCP tool to call, what parameters]
2. [Step 2 — how to interpret the response]
3. [Step 3 — output format]

## Output Format

[Markdown table or structured output spec]
```

### Pattern 2: GSC Tool Call Conventions

**What:** Verified from reading GSC MCP source at `/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP/src/index.ts`

The GSC MCP exposes these exact tool names (snake_case, not kebab-case like Ahrefs):

| GSC Tool Name | Required Params | Optional Params | Maps to Sub-command |
|---------------|----------------|-----------------|---------------------|
| `list_accounts` | none | — | Discovery only |
| `list_sites` | none | `account` | Discovery only |
| `query_search_analytics` | `siteUrl`, `startDate`, `endDate` | `dimensions`, `rowLimit`, `filters`, `account` | overview, cannibalization, new-keywords |
| `inspect_url` | `siteUrl`, `inspectionUrl` | `account` | index-issues |
| `list_sitemaps` | `siteUrl` | `account` | (Phase 3: gsc-sitemaps) |
| `find_keyword_opportunities` | `siteUrl`, `startDate`, `endDate` | `minImpressions`, `maxCtr`, `maxPosition`, `account` | opportunities |
| `get_top_pages` | `siteUrl`, `startDate`, `endDate` | `sortBy`, `limit`, `account` | (top pages within overview) |
| `compare_performance` | `siteUrl`, `currentStartDate`, `currentEndDate`, `previousStartDate`, `previousEndDate` | `dimension`, `limit`, `account` | drops, compare, content-decay, new-keywords |
| `analyze_brand_queries` | `siteUrl`, `startDate`, `endDate`, `brandTerms` | `account` | brand-vs-nonbrand |
| `get_keyword_trend` | `siteUrl`, `keyword`, `startDate`, `endDate` | `account` | (keyword-specific trend) |
| `export_analytics` | `siteUrl`, `startDate`, `endDate`, `dimensions`, `format` | `rowLimit`, `searchType`, `account` | (data export) |
| `query_by_search_appearance` | `siteUrl`, `startDate`, `endDate`, `searchAppearance` | `rowLimit`, `account` | (rich results, Phase 3) |
| `query_by_search_type` | `siteUrl`, `startDate`, `endDate`, `searchType` | `dimensions`, `rowLimit`, `account` | (web/image/video filtering) |

**CRITICAL:** The GSC MCP registered server name in `~/.claude/mcp.json` is not yet confirmed. The tool name prefix used in Claude Code (e.g., `mcp__gsc_mcp_server__query_search_analytics` or similar) must be discovered at runtime using ToolSearch. The first GSC sub-skill must include a discovery step and update `references/gsc-api-reference.md`.

**Property format:** Both `sc-domain:example.com` and `https://example.com` are accepted — confirmed from reading the GSC MCP tool descriptions which say: `"The site URL to query (e.g., 'https://example.com' or 'sc-domain:example.com')"`.

**`account` parameter:** The GSC MCP supports multiple authenticated Google accounts via an `account` alias parameter. When omitted and only one account exists, it is used automatically. Sub-skills should accept this as an optional parameter and pass it through.

### Pattern 3: Ahrefs Tool Call Conventions

**What:** Verified in Phase 1 from live runtime observation and encoded in `references/ahrefs-api-reference.md`

All Ahrefs tools use the prefix `mcp__claude_ai_ahrefs__` and accept a `target` parameter (bare domain `example.com` for domain-level queries). The monetary conversion rule (divide by 100) applies to `traffic_cost`, `cpc`, and any `_cost` or `_value` field.

Key Ahrefs tool parameter to know: `content-gap` uses `keywords-explorer-matching-terms` filtered by a competitor domain — the exact filter parameter name must be verified against live tool signature before building that sub-skill.

### Pattern 4: Markdown Audit Logic

**What:** Pure local file analysis with no external dependencies
**When to use:** `seo-markdown-audit` only

SEO checks to perform on a markdown file:
1. **Title/H1**: Single H1 present, within 50-60 chars, contains primary keyword
2. **Meta description**: Check frontmatter `description` field, 150-160 chars, includes keyword
3. **Heading hierarchy**: H2 before H3, no skipped levels, descriptive headings
4. **Keyword density**: Primary keyword (inferred from title/H1) in first 100 words
5. **Content length**: Minimum 300 words for any page; 1,500+ for pillar content
6. **Links**: Check for internal links (relative paths), external links with descriptive anchor text
7. **Images**: `![alt text](url)` format — flag missing or generic alt text ("image", "photo", "screenshot")
8. **Frontmatter**: Presence of `title`, `description`, `date` fields
9. **Reading level**: Sentence length heuristic (>25 words avg = too complex)
10. **Duplicate headings**: Same heading text appearing twice

### Anti-Patterns to Avoid

- **Calling Ahrefs `content-gap` with wrong filter syntax:** The `keywords-explorer-matching-terms` tool may require a specific parameter to filter by competitor domain — do not assume it uses `competitor` as the field name without checking the live tool signature first.
- **Assuming GSC tool name prefix:** Never hardcode a GSC MCP tool call prefix. Always discover with ToolSearch first.
- **Building all 9 GSC sub-skills before testing one:** Verify the first GSC sub-skill works end-to-end before mass-producing the pattern. A single tool name error would break all 9.
- **Checking MCP at orchestrator level:** Per Phase 1 decision, MCP checks are self-contained in each sub-skill. The main `seo/SKILL.md` does NOT check MCPs.
- **Agent files for GSC/Ahrefs analyst:** The ROADMAP.md mentions a `seo-gsc-analyst` agent and `seo-ahrefs-analyst` agent in Plans 02-01 and 02-02. Per Phase 1 CONTEXT.md decision, "Logic lives in each sub-skill's SKILL.md; agents only for parallel audit work within `/seo audit`." The analyst agents should NOT be created unless they are needed for parallel multi-subagent orchestration within a single command — none of the Phase 2 commands require that.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| GSC data fetching | Custom HTTP client to GSC API | GSC MCP tools | MCP already handles OAuth, pagination, error handling |
| Ahrefs data fetching | Custom API wrapper | Ahrefs MCP tools | MCP already handles auth, rate limiting, retries |
| Brand query detection | Custom regex for brand detection | GSC MCP `analyze_brand_queries` | Dedicated tool already does the aggregation and percentage math |
| Keyword opportunity finding | Manual filter on raw analytics data | GSC MCP `find_keyword_opportunities` | Dedicated tool with configurable `minImpressions`, `maxCtr`, `maxPosition` |
| Period comparison math | Manual delta calculation | GSC MCP `compare_performance` | Tool returns `clicksChange`, `clicksChangePercent`, `positionChange` directly |
| Markdown parsing | Custom markdown parser | Read file + basic text analysis | For SEO checks, regex on headings/links is sufficient; no parser library needed |

**Key insight:** The GSC MCP is unusually well-featured — it has dedicated high-level tools (`find_keyword_opportunities`, `compare_performance`, `analyze_brand_queries`) that would otherwise require multiple raw API calls and significant application logic. Use these dedicated tools rather than building equivalent logic on top of `query_search_analytics`.

---

## Common Pitfalls

### Pitfall 1: GSC MCP Registered Name Unknown
**What goes wrong:** Sub-skills try to call `mcp__gsc__query_search_analytics` or similar, which fails silently because the actual registered name in `~/.claude/mcp.json` uses a different prefix.
**Why it happens:** The GSC MCP server name (`gsc-mcp-server` per its package.json) is registered by the user under an alias in `~/.claude/mcp.json`. The Claude Code tool prefix depends on this registration name, which was not confirmed in Phase 1.
**How to avoid:** First GSC sub-skill MUST use ToolSearch to discover the actual tools, then document the verified prefix in `references/gsc-api-reference.md`. All subsequent GSC sub-skills read the reference file.
**Warning signs:** ToolSearch returns no results for `+gsc` — means either not registered or uses a different keyword.

### Pitfall 2: GSC Property Format Mismatch
**What goes wrong:** User provides `example.com` but the GSC MCP requires `sc-domain:example.com` or `https://example.com`.
**Why it happens:** GSC has two property types (domain vs URL prefix) and users may not know which they added.
**How to avoid:** Each GSC sub-skill should try `list_sites` first if the user provides a bare domain, to help them identify the correct property format. Accept both formats and try the `sc-domain:` prefix first (more common for domain properties).
**Warning signs:** Tool returns "No data found" or auth error when a known property should have data.

### Pitfall 3: GSC `brand-vs-nonbrand` Requires User-Provided Brand Terms
**What goes wrong:** Skill tries to auto-detect brand terms from the domain name and produces wrong results.
**Why it happens:** The `analyze_brand_queries` tool requires a `brandTerms` array — the MCP cannot auto-detect what constitutes a brand query.
**How to avoid:** The `seo-gsc-brand-vs-nonbrand` skill MUST prompt the user for their brand terms before calling the tool. Pre-populate with the domain name as a starting guess but require confirmation.
**Warning signs:** Brand analysis shows 0% branded traffic or obviously incorrect split.

### Pitfall 4: Ahrefs `content-gap` Tool Ambiguity
**What goes wrong:** The `content-gap` sub-command is mapped to `keywords-explorer-matching-terms` in `ahrefs-api-reference.md` with the note "filtered by competitor domain" — but the exact filter parameter name is unverified.
**Why it happens:** Phase 1 documented this mapping based on tool name inference, not live testing.
**How to avoid:** When building `seo-ahrefs-content-gap`, call ToolSearch for the specific tool and inspect its schema before writing the skill logic. The skill may need a different approach (e.g., `site-explorer-organic-competitors` + `site-explorer-organic-keywords` cross-referenced).
**Warning signs:** Tool call returns error about unknown parameter.

### Pitfall 5: GSC `index-issues` is Slow for Large Sites
**What goes wrong:** `inspect_url` must be called per-URL and the site has thousands of pages — the command hangs or times out.
**Why it happens:** The GSC URL Inspection API is rate-limited and requires one call per URL.
**How to avoid:** `seo-gsc-index-issues` should use `query_search_analytics` with a `page` dimension first to identify a manageable list of pages (e.g., last 100 by impressions), then call `inspect_url` only on pages that appear to have issues (low impressions + high position gap suggesting indexing problem). Hard-cap at 20 `inspect_url` calls per execution.
**Warning signs:** Skill gets stuck on sites with 1,000+ pages.

### Pitfall 6: Markdown Audit Path Handling
**What goes wrong:** User provides a relative path, the Read tool fails, and the skill returns a confusing error.
**Why it happens:** Read tool requires absolute paths.
**How to avoid:** `seo-markdown-audit` should instruct the user to provide an absolute path, or use Bash to resolve `realpath` on the provided path before calling Read.
**Warning signs:** "File not found" errors when the file clearly exists.

### Pitfall 7: Sub-skill Directory Names Must Match Routing Table
**What goes wrong:** Sub-skill is created as `seo-gsc-index-issues/` but routing table expects `seo-gsc-indexing/` (per seo/SKILL.md routing table which uses different names than REQUIREMENTS.md).
**Why it happens:** The REQUIREMENTS.md uses command names like `index-issues` while `seo/SKILL.md` routing table uses different directory names.
**How to avoid:** Always verify the exact directory name from the routing table in `skills/seo/SKILL.md` before creating each sub-skill. The routing table is the source of truth.

The routing table in `seo/SKILL.md` specifies:
- GSC: `seo-gsc-overview`, `seo-gsc-drops`, `seo-gsc-opportunities`, `seo-gsc-pages`, `seo-gsc-queries`, `seo-gsc-indexing`, `seo-gsc-cannibalization`, `seo-gsc-compare`, `seo-gsc-sitemaps`
- Ahrefs: `seo-ahrefs-overview`, `seo-ahrefs-backlinks`, `seo-ahrefs-keywords`, `seo-ahrefs-competitors`, `seo-ahrefs-content-gap`, `seo-ahrefs-broken-links`, `seo-ahrefs-new-links`, `seo-ahrefs-anchor-analysis`, `seo-ahrefs-dr-history`, `seo-ahrefs-top-pages`
- Local: `seo-markdown-audit`

Note: The ROADMAP.md Plan descriptions use slightly different names than REQUIREMENTS.md. The routing table in `seo/SKILL.md` is authoritative for directory names.

**Also note:** The routing table has 9 GSC sub-commands but REQUIREMENTS.md defines 9 GSC commands with slightly different names (`index-issues` vs `indexing`, `brand-vs-nonbrand` vs `queries`). Resolution: use the directory names from the routing table since they already exist in `seo/SKILL.md`.

---

## Code Examples

### GSC Sub-skill SKILL.md Template

```markdown
---
name: seo-gsc-overview
description: >
  Google Search Console performance overview for a site. Shows clicks, impressions,
  CTR, and average position from the last 28 days. Use when user says "GSC overview",
  "search console performance", "how is my site doing in Google", or
  "show me clicks and impressions".
---

# GSC Overview

Shows clicks, impressions, CTR, and average position from Google Search Console
for the past 28 days.

## MCP Check

Load `references/mcp-degradation.md`.

Use ToolSearch with query "+gsc":
- If tools returned → note the tool name prefix, proceed
- If no tools → display GSC error template from mcp-degradation.md, stop

## Inputs

- `site`: GSC property URL — accept `sc-domain:example.com` or `https://example.com`
  (try `list_sites` if user provides bare `example.com` to help them identify property)

## Execution

1. Call `query_search_analytics`:
   - `siteUrl`: the site param from user
   - `startDate`: today minus 28 days (YYYY-MM-DD)
   - `endDate`: today minus 3 days (GSC data has ~3 day delay)
   - `dimensions`: ["query"]
   - `rowLimit`: 25

2. Call `query_search_analytics` again:
   - Same dates
   - `dimensions`: ["page"]
   - `rowLimit`: 25

3. Calculate totals from the first call results (sum clicks and impressions across all rows).

## Output Format

```
## GSC Performance Overview: [site]
Period: [startDate] to [endDate] (last 28 days)

### Summary
| Metric | Value |
|--------|-------|
| Total Clicks | X,XXX |
| Total Impressions | X,XXX |
| Average CTR | X.XX% |
| Average Position | X.X |

### Top Queries (by clicks)
| Query | Clicks | Impressions | CTR | Position |
| [query] | [n] | [n] | [X.XX%] | [X.X] |

### Top Pages (by clicks)
| Page | Clicks | Impressions | CTR | Position |
| [url] | [n] | [n] | [X.XX%] | [X.X] |
```

Note: CTR is returned as decimal (0.0523) — display as percentage (5.23%).
```

### Ahrefs Sub-skill SKILL.md Template

```markdown
---
name: seo-ahrefs-overview
description: >
  Ahrefs domain overview: Domain Rating, backlinks, organic keywords, and
  estimated traffic value. Use when user says "Ahrefs overview", "domain rating",
  "DR score", "check backlinks", or "how strong is this domain".
---

# Ahrefs Overview

Shows Domain Rating, backlink count, organic keyword count, and traffic estimate
(in USD) for a domain.

## MCP Check

Load `references/mcp-degradation.md`.

Use ToolSearch with query "+ahrefs":
- If tools returned → Ahrefs MCP is available, proceed
- If no tools → display Ahrefs error template from mcp-degradation.md, stop

## Inputs

- `domain`: bare domain without protocol (e.g., `example.com`)

## Execution

Load `references/ahrefs-api-reference.md` for tool names and monetary conversion.

1. Call `mcp__claude_ai_ahrefs__site-explorer-metrics`:
   - `target`: the domain param
   - Note: returns `traffic_cost` in CENTS — divide by 100 for USD

2. Call `mcp__claude_ai_ahrefs__site-explorer-domain-rating`:
   - `target`: the domain param

## Output Format

```
## Ahrefs Overview: [domain]

| Metric | Value |
|--------|-------|
| Domain Rating | XX/100 |
| Total Backlinks | X,XXX |
| Referring Domains | XXX |
| Organic Keywords | X,XXX |
| Estimated Monthly Traffic | X,XXX visits |
| Traffic Value | $X,XXX/mo |
```

CRITICAL: traffic_cost from API is in cents. Divide by 100 before display.
Format as "$X,XXX" with comma separators.
```

### Date Arithmetic for GSC Date Ranges (via Bash)

```bash
# Get today's date and calculate 28-day window with 3-day GSC delay
END_DATE=$(date -v-3d +%Y-%m-%d)  # macOS
START_DATE=$(date -v-31d +%Y-%m-%d)  # 28 days of data ending 3 days ago
```

Or instruct Claude to calculate dates inline as part of execution steps.

### Markdown Audit Core Checks

```markdown
## Execution

1. Use Read tool to load the file at `<path>`
2. Run these checks:

**Structure checks:**
- Count H1 tags (`# ` lines) — flag if 0 or >1
- Verify H2 exists before H3 — flag skipped levels
- Check H1 character length — warn if >60 chars

**Content checks:**
- Count words (split on whitespace) — flag if <300
- Extract first 100 words — check if H1 keyword appears
- Check sentence lengths — flag if average >25 words

**Frontmatter checks (if YAML frontmatter present):**
- Check `title` field exists and is <60 chars
- Check `description` field exists and is 150-160 chars

**Link checks:**
- Find `[text](url)` patterns — flag if link text is generic ("here", "click", "link")
- Count internal links (relative paths) vs external — flag if zero internal links

**Image checks:**
- Find `![alt](url)` patterns
- Flag empty alt: `![](url)` or generic alt: `![image](url)`, `![photo](url)`

3. Generate prioritized recommendations (Critical → High → Medium → Low)
```

---

## State of the Art

| Old Approach | Current Approach | Notes |
|--------------|-----------------|-------|
| GSC tool names unknown (Phase 1 placeholder) | All 13 GSC MCP tool names verified by reading source | See `/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP/src/index.ts` |
| GSC property format "UNVERIFIED" (STATE.md blocker) | Partially resolved — both formats confirmed accepted | Tool descriptions explicitly list both `sc-domain:example.com` and `https://example.com` |
| GSC reference file has TBD placeholders | Can now be updated with real tool names in Plan 02-01 | First task of Plan 02-01 should update `gsc-api-reference.md` |
| ROADMAP says create `seo-gsc-analyst` agent | Not needed per Phase 1 decision | GSC command logic lives in SKILL.md; no parallel multi-agent orchestration required |

**Key discrepancy found:** The routing table in `seo/SKILL.md` lists commands that differ slightly from the REQUIREMENTS.md command names:
- `seo/SKILL.md` routing: `gsc pages`, `gsc queries`, `gsc indexing`, `gsc sitemaps`
- REQUIREMENTS.md: `gsc drops`, `gsc opportunities`, `gsc cannibalization`, `gsc index-issues`, `gsc compare`, `gsc brand-vs-nonbrand`, `gsc content-decay`, `gsc new-keywords`

The routing table has MORE commands than the REQUIREMENTS.md covers (pages, queries, sitemaps vs brand-vs-nonbrand, content-decay, new-keywords). The planner needs to decide which set to implement — the routing table in `seo/SKILL.md` is the installed artifact, so it should be treated as authoritative. Phase 2 plans should build the sub-skills named in the routing table, not the REQUIREMENTS.md command names.

---

## Open Questions

1. **GSC MCP registered name in `~/.claude/mcp.json`**
   - What we know: Server name in package.json is `gsc-mcp-server`; install script from Phase 1 should have registered it
   - What's unclear: The exact alias used during registration (which becomes the ToolSearch keyword and tool name prefix)
   - Recommendation: First task in Plan 02-01 must run ToolSearch to discover this. If registration failed, run `~/.claude/skills/seo/hooks/verify-mcp-scope.sh` to diagnose.

2. **Routing table discrepancy: 9 GSC commands in routing table vs 9 in REQUIREMENTS.md but with different names**
   - What we know: `seo/SKILL.md` routing table routes `gsc-pages`, `gsc-queries`, `gsc-indexing`, `gsc-sitemaps`; REQUIREMENTS.md defines `brand-vs-nonbrand`, `content-decay`, `new-keywords`, `index-issues`
   - What's unclear: Whether the routing table should be updated to match REQUIREMENTS.md or vice versa
   - Recommendation: The routing table is the installed artifact; update it to match REQUIREMENTS.md during Plan 02-01. The commands `gsc-pages` and `gsc-queries` can be folded into `gsc-overview`; `gsc-sitemaps` can be deferred to Phase 3.

3. **Ahrefs `content-gap` exact tool parameter**
   - What we know: Mapped to `keywords-explorer-matching-terms` with "filtered by competitor domain" note
   - What's unclear: The exact filter parameter name in the live tool schema
   - Recommendation: Build this sub-skill last among Ahrefs commands; call ToolSearch to inspect the schema before writing the skill logic.

4. **Agent files mentioned in ROADMAP.md Plans**
   - ROADMAP.md says Plan 02-01 creates `seo-gsc-analyst` agent, Plan 02-02 creates `seo-ahrefs-analyst` agent
   - Phase 1 decision is clear: no agent files for command logic
   - Recommendation: Skip agent creation entirely in Phase 2. The ROADMAP plans should not create agents.

---

## GSC MCP Tool Name Verified Mapping

This section resolves the primary STATE.md blocker for Phase 2.

**Source:** `/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP/src/index.ts` (read directly, HIGH confidence)

The GSC MCP server name is `gsc-mcp-server`. When registered in `~/.claude/mcp.json`, Claude Code creates tool names following the pattern `mcp__{registered_alias}__{tool_name}`. The registered alias must be confirmed at runtime.

**Complete GSC sub-command to MCP tool mapping (now verified):**

| Requirement | GSC Tool | Key Params |
|-------------|----------|-----------|
| GSC-01 overview | `query_search_analytics` (×2: dimensions=query, dimensions=page) | siteUrl, startDate, endDate |
| GSC-02 drops | `compare_performance` | siteUrl, 4 date params, dimension=page |
| GSC-03 opportunities | `find_keyword_opportunities` | siteUrl, startDate, endDate, minImpressions, maxCtr |
| GSC-04 cannibalization | `query_search_analytics` | siteUrl, dates, dimensions=["query","page"] — detect same query on 2+ pages |
| GSC-05 index-issues | `inspect_url` (per URL, capped at 20) | siteUrl, inspectionUrl |
| GSC-06 compare | `compare_performance` | siteUrl, 4 date params, dimension (query or page) |
| GSC-07 brand-vs-nonbrand | `analyze_brand_queries` | siteUrl, dates, brandTerms (user must provide) |
| GSC-08 content-decay | `compare_performance` | siteUrl, 90-day window, dimension=page, filter negative changes |
| GSC-09 new-keywords | `compare_performance` | siteUrl, 28-day window, filter previousClicks=0 and currentClicks>0 |

**CTR display rule (confirmed from source):** The MCP already converts CTR to percentage in its formatted output (`(row.ctr * 100).toFixed(2) + "%"`), BUT the raw API response field `ctr` is a decimal. Sub-skills calling `query_search_analytics` directly receive decimal CTR. Always multiply by 100 for display.

---

## Sources

### Primary (HIGH confidence)
- `/Users/aash-zsbch1500/Desktop/GSC-MCP/GSC-MCP/src/index.ts` — All 13 GSC MCP tool names, parameter schemas, property format confirmation
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/skills/seo/references/ahrefs-api-reference.md` — Verified Ahrefs tool mappings from Phase 1
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/skills/seo/SKILL.md` — Authoritative routing table for sub-skill directory names
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/.planning/phases/01-foundation/01-CONTEXT.md` — Locked Phase 1 decisions (flat directory, no agents for command logic)
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/.planning/STATE.md` — Known blockers and accumulated decisions

### Secondary (MEDIUM confidence)
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/.planning/ROADMAP.md` — Phase 2 plan descriptions (MEDIUM because plans are labeled TBD and some details conflict with Phase 1 decisions)
- `/Users/aash-zsbch1500/Desktop/Github projects/SEO/.planning/REQUIREMENTS.md` — Requirement definitions (MEDIUM because command names in REQUIREMENTS.md partially conflict with routing table)

### Tertiary (LOW confidence)
- GSC MCP registered alias in `~/.claude/mcp.json`: NOT confirmed (file not found / empty during research) — must be verified at runtime

---

## Metadata

**Confidence breakdown:**
- GSC tool names and schemas: HIGH — read directly from source TypeScript
- GSC property format: HIGH — explicitly listed in tool descriptions
- Ahrefs tool names: HIGH — verified in Phase 1 and encoded in reference file
- GSC registered MCP alias (tool name prefix): LOW — must discover at runtime
- Ahrefs content-gap exact filter param: LOW — mapping is inferred, not live-tested
- Markdown audit heuristics: HIGH — standard SEO practices, no external dependency

**Research date:** 2026-03-02
**Valid until:** 2026-04-01 (stable MCP implementations; Ahrefs API versions may change, verify if >30 days elapsed)
