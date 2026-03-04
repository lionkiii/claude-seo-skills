# Claude SEO Skills

**44 powerful SEO commands for [Claude Code](https://docs.anthropic.com/en/docs/claude-code)** — the most comprehensive SEO toolkit available as Claude Code skills. Run full site audits, analyze backlinks with Ahrefs, track rankings with Google Search Console, research SERPs, generate content briefs, and more — all from your terminal.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-44-green.svg)](#all-44-commands)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blueviolet.svg)](https://docs.anthropic.com/en/docs/claude-code)

## Why Claude SEO Skills?

- **44 dedicated commands** — the largest Claude Code SEO skill set available
- **Live data from Ahrefs** — Domain Rating, backlinks, keyword rankings, competitor analysis, content gaps
- **Google Search Console integration** — real ranking data, indexing status, traffic drops, keyword cannibalization
- **Technical SEO audits** — Core Web Vitals, crawlability, security headers, structured data, mobile optimization
- **Content analysis** — E-E-A-T scoring, AI content detection, readability, keyword optimization
- **AI search optimization** — GEO (Generative Engine Optimization) for AI Overviews, ChatGPT, Perplexity
- **AI readability** — llms.txt generation/validation, AI crawler robots.txt audit
- **Parallel execution** — site audits delegate to 6 specialist agents for speed
- **Graceful MCP degradation** — works with whatever MCP servers you have connected; skips what's missing

## Quick Start

```bash
git clone https://github.com/lionkiii/claude-seo-skills.git
cd claude-seo-skills
bash install.sh
```

That's it. The installer copies skills and agents to `~/.claude/`, sets up a Python venv, and verifies MCP connections. Run `bash scripts/smoke-test.sh` to verify everything works.

### Prerequisites

| Requirement | Required | Notes |
|---|---|---|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Yes | Anthropic's CLI tool |
| Python 3.9+ | Yes | For helper scripts |
| Ahrefs MCP | Yes | Auto-connected via Claude.ai — no setup needed |
| [GSC MCP](https://github.com/lionkiii/google-searchconsole-mcp) | Optional | For Google Search Console commands ([setup guide](#google-search-console-mcp-optional)) |

## Usage Examples

```bash
# Run a full SEO site audit (delegates to 6 parallel agents)
/seo-audit example.com

# Deep-dive into a single page's on-page SEO
/seo-page https://example.com/blog/post

# Check your Ahrefs backlink profile
/seo-ahrefs-backlinks example.com

# Find keyword gaps vs competitors
/seo-ahrefs-content-gap example.com

# See your Google Search Console dashboard
/seo-gsc-overview site=sc-domain:example.com

# Find ranking drops before they become problems
/seo-gsc-drops site=sc-domain:example.com

# Generate a content brief from live SERP data
/seo-content-brief "best project management tools" site=example.com

# Analyze SERP competition for any keyword
/seo-serp "keyword research tools"

# Detect AI-generated content
/seo-ai-content-check https://example.com/article

# Optimize for AI search (Google AI Overviews, ChatGPT, Perplexity)
/seo-geo example.com

# Generate an llms.txt file for your site
/seo-llms-txt generate example.com

# Audit your robots.txt for AI crawler policies
/seo-robots-ai example.com
```

## All 44 Commands

### Site Audits & Technical SEO

| Command | What It Does |
|---|---|
| `/seo-audit <url>` | Full site SEO audit — crawls up to 500 pages, delegates to 6 specialist agents, generates health score |
| `/seo-site-audit-pro <url>` | Flagship comprehensive audit combining Ahrefs + GSC data in sequential waves with checkpoint saves |
| `/seo-page <url>` | Deep single-page analysis — on-page elements, content quality, technical meta, schema, images, performance |
| `/seo-technical <url>` | Technical SEO audit across 8 categories: crawlability, indexability, security, URL structure, mobile, Core Web Vitals, structured data, JS rendering |
| `/seo-schema <url>` | Detect, validate, and generate Schema.org structured data (JSON-LD). Covers Article, Product, FAQ, HowTo, LocalBusiness, and more |
| `/seo-images <url>` | Image optimization — alt text, file sizes, WebP/AVIF format check, responsive images, lazy loading, CLS prevention |
| `/seo-sitemap <url>` | Analyze existing XML sitemaps or generate new ones. Cross-references GSC indexing status when available |
| `/seo-internal-links <url>` | Internal link structure analysis — finds orphan pages, underlinked pages, broken links. Suggests anchor text improvements |
| `/seo-migration-check <url>` | Validate SEO preservation during migrations — redirect chains, canonical consistency, title/meta preservation, HTTP status codes |
| `/seo-hreflang <url>` | International SEO audit — hreflang validation, language/region codes, x-default tag, return link verification |
| `/seo-local <url>` | Local SEO audit — NAP consistency, Google Business Profile signals, local schema, citations, review signals |
| `/seo-log-analysis <file>` | Server log analysis for crawl budget insights — bot vs user traffic, crawl frequency, status codes, wasted crawl budget |

### Content & Keywords

| Command | What It Does |
|---|---|
| `/seo-content <url>` | Content quality and E-E-A-T analysis with AI citation readiness. Enhanced with Ahrefs keyword data + GSC search queries |
| `/seo-content-brief <keyword>` | Generate structured SEO content brief from live Ahrefs SERP data + optional GSC overlay. Includes target word count, heading outline, competitor analysis |
| `/seo-serp <keyword>` | Analyze SERP for any keyword — ranking pages, Domain Rating scores, traffic estimates, content angle analysis |
| `/seo-markdown-audit <path>` | Audit markdown files before publishing — heading structure, meta description, keyword density, link quality, image alt text, frontmatter |
| `/seo-ai-content-check <url>` | Detect AI-generated content using pure text analysis — sentence uniformity, vocabulary diversity, repetition patterns, hedging language |
| `/seo-programmatic <url>` | Programmatic SEO planning for pages generated at scale — template engines, URL patterns, internal linking automation, thin content prevention |
| `/seo-plan <url>` | Strategic SEO planning — industry-specific templates, competitive analysis, content strategy, implementation roadmap |

### Ahrefs Backlink & Keyword Analysis

| Command | What It Does |
|---|---|
| `/seo-ahrefs-overview <domain>` | Domain overview — Domain Rating, total backlinks, referring domains, organic keywords, estimated traffic, traffic value |
| `/seo-ahrefs-keywords <domain>` | Top organic keyword rankings — keyword, position, search volume, CPC, estimated traffic, traffic share |
| `/seo-ahrefs-backlinks <domain>` | Backlink profile — referring pages, source Domain Rating, anchor text, link type, first seen date |
| `/seo-ahrefs-top-pages <domain>` | Best performing pages by organic traffic — traffic, traffic share, keyword count, top keyword per page |
| `/seo-ahrefs-competitors <domain>` | Top organic competitors — competing domains, keyword overlap, shared keywords, unique competitor keywords |
| `/seo-ahrefs-content-gap <domain>` | Find keywords competitors rank for but you don't — reveals content opportunities and topic gaps |
| `/seo-ahrefs-broken-links <domain>` | Broken backlinks pointing to 404 pages — prioritized by DR for maximum reclamation value |
| `/seo-ahrefs-new-links <domain>` | Recently acquired and lost backlinks in the last 30 days — new referring domains and lost links |
| `/seo-ahrefs-dr-history <domain>` | Domain Rating trend over time — DR growth, drops, and significant changes |
| `/seo-ahrefs-anchor-analysis <domain>` | Anchor text distribution — breakdown across all backlinks, link profile health assessment |

### Google Search Console Analytics

| Command | What It Does |
|---|---|
| `/seo-gsc-overview site=<property>` | Performance dashboard — total clicks, impressions, CTR, average position + top 25 queries and pages |
| `/seo-gsc-drops site=<property>` | Detect ranking drops — compares last 28 days vs prior period, surfaces pages and keywords losing traffic |
| `/seo-gsc-opportunities site=<property>` | Quick wins — high-impression, low-CTR keywords already ranking where better titles or meta could boost clicks |
| `/seo-gsc-cannibalization site=<property>` | Keyword cannibalization detection — queries where multiple pages compete for the same ranking |
| `/seo-gsc-indexing site=<property>` | Indexing problems — checks up to 20 pages for indexing status, coverage state, robots directives |
| `/seo-gsc-compare site=<property>` | Period comparison — month-over-month, year-over-year, or custom date ranges for clicks, impressions, CTR, position |
| `/seo-gsc-brand-vs-nonbrand site=<property>` | Brand traffic analysis — percentage of clicks from brand name searches vs generic queries |
| `/seo-gsc-content-decay site=<property>` | Content decay detection — pages losing both clicks and impressions over a 90-day window |
| `/seo-gsc-new-keywords site=<property>` | Newly ranking keywords — queries with zero previous impressions that started appearing in search |

### AI Search & Competitive Intelligence

| Command | What It Does |
|---|---|
| `/seo-geo <url>` | Optimize for AI search — AI Overviews (SGE), ChatGPT web search, Perplexity. Generative Engine Optimization analysis |
| `/seo-brand-radar <domain>` | Monitor brand visibility in AI search and traditional search — brand mentions, share of voice, AI citation readiness |
| `/seo-competitor-pages <domain>` | Generate SEO-optimized "X vs Y" and "alternatives to X" comparison pages — feature matrices, schema markup, conversion elements |
| `/seo-report <url>` | Generate and save a complete SEO report to disk — configurable sections, multiple output formats |

### AI Readability

| Command | What It Does |
|---|---|
| `/seo-llms-txt <url>` | Audit, generate, or validate llms.txt files — the emerging standard for helping LLMs understand your site content |
| `/seo-robots-ai <url>` | Audit robots.txt for AI crawler policies — GPTBot, ClaudeBot, PerplexityBot, Google-Extended, and 13 more AI bots |

## How It Works

```
You type:  /seo-audit example.com

Claude Code loads the skill → checks MCP connections → delegates to specialist agents:

  Agent 1: Technical SEO (crawlability, Core Web Vitals, security)
  Agent 2: Content Quality (E-E-A-T, readability, keyword usage)
  Agent 3: Schema & Structured Data (JSON-LD validation)
  Agent 4: Visual & Images (alt text, file sizes, lazy loading)
  Agent 5: Sitemap & Indexing (XML sitemap, robots.txt)
  Agent 6: Performance (page speed, resource loading)

Results merge → health score calculated → actionable report delivered
```

Each command is **self-contained** — it checks its own MCP dependencies, falls back gracefully when a data source is unavailable, and clearly tells you what data is missing.

## MCP Setup

### Ahrefs MCP

Ahrefs is connected automatically through your Claude.ai account. No local configuration needed — it just works.

### Google Search Console MCP (Optional)

GSC commands require a Google Search Console MCP server. We built one — [google-searchconsole-mcp](https://github.com/lionkiii/google-searchconsole-mcp).

**Important:** Register at **user scope** in `~/.claude/mcp.json` (not project scope). Project-scoped MCPs cause subagent issues.

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "node",
      "args": ["/path/to/google-searchconsole-mcp/dist/index.js"]
    }
  }
}
```

Verify it's connected:

```bash
bash scripts/verify-mcp-scope.sh
```

Without GSC, all 35 non-GSC commands work perfectly. The 9 GSC commands will show a setup prompt instead.

## Project Structure

```
claude-seo-skills/
├── skills/                    # 44 skill definitions
│   ├── seo/                   # Orchestrator + shared references
│   │   ├── SKILL.md           # Main /seo command router
│   │   ├── references/        # API refs, quality gates, E-E-A-T framework
│   │   ├── hooks/             # YAML validation, pre-install checks
│   │   └── scripts/           # Python helpers (fetch, parse, screenshot)
│   ├── seo-audit/             # /seo-audit
│   ├── seo-ahrefs-keywords/   # /seo-ahrefs-keywords
│   ├── seo-gsc-overview/      # /seo-gsc-overview
│   └── ...                    # 41 more skill directories
├── agents/                    # 6 specialist agents for parallel audits
├── scripts/                   # Install, smoke test, MCP verification
├── install.sh                 # One-command installer
└── CLAUDE.md                  # Project context for Claude Code
```

## Contributing

1. Fork the repo
2. Create a feature branch
3. Add or modify skills in `skills/`
4. Run `bash scripts/smoke-test.sh` to validate (142 checks)
5. Open a PR

## Related Projects

- [google-searchconsole-mcp](https://github.com/lionkiii/google-searchconsole-mcp) — Google Search Console MCP server for Claude Code
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's CLI tool
- [Claude Code Skills Docs](https://docs.anthropic.com/en/docs/claude-code/skills) — How skills work

## License

[MIT](LICENSE)
