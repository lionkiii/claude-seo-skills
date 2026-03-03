# SEO Skill System for Claude Code

42 SEO commands that run inside [Claude Code](https://docs.anthropic.com/en/docs/claude-code) via `/seo <command>`. Covers technical audits, content analysis, SERP research, backlink profiling, and more — powered by live data from Ahrefs and Google Search Console MCP servers.

## Prerequisites

| Requirement | Required | Notes |
|---|---|---|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Yes | CLI tool from Anthropic |
| Python 3.9+ | Yes | For YAML validation and helper scripts |
| [Ahrefs MCP](https://docs.anthropic.com/en/docs/claude-code/ahrefs-mcp) | Yes | Connected via Claude.ai account — no local setup |
| GSC MCP | Optional | Bring-your-own Google Search Console MCP server (see [MCP Setup](#mcp-setup)) |

## Quick Install

```bash
git clone https://github.com/lionkiii/SEO.git
cd SEO
bash install.sh
bash scripts/smoke-test.sh
```

The installer copies skills and agents to `~/.claude/`, creates a Python venv, and verifies MCP registration.

## Usage

```bash
# Full site audit
/seo audit example.com

# Single page deep-dive
/seo page https://example.com/blog/post

# SERP analysis for a keyword
/seo serp "best project management tools"

# Ahrefs backlink profile
/seo ahrefs backlinks example.com

# GSC performance dashboard
/seo gsc overview site=sc-domain:example.com

# Content brief from live SERP data
/seo content-brief "keyword" site=example.com
```

## Commands

### Core Analysis (12)

| Command | Description |
|---|---|
| `audit` | Full site SEO audit with parallel subagent delegation |
| `page` | Deep single-page SEO analysis |
| `technical` | Technical SEO audit (crawlability, CWV, security) |
| `content` | Content quality and E-E-A-T analysis |
| `schema` | Schema.org structured data validation and generation |
| `images` | Image optimization analysis |
| `sitemap` | XML sitemap analysis or generation |
| `hreflang` | International SEO and hreflang audit |
| `local` | Local SEO audit (NAP, GBP, citations) |
| `internal-links` | Internal link structure analysis |
| `migration-check` | SEO preservation during site migrations |
| `plan` | Strategic SEO planning and roadmap |

### Google Search Console (9)

| Command | Description |
|---|---|
| `gsc overview` | Performance dashboard (clicks, impressions, CTR) |
| `gsc drops` | Detect ranking drops and lost traffic |
| `gsc opportunities` | Find high-impression, low-CTR quick wins |
| `gsc cannibalization` | Detect keyword cannibalization |
| `gsc indexing` | Identify indexing and coverage issues |
| `gsc compare` | Compare performance across time periods |
| `gsc brand-vs-nonbrand` | Branded vs non-branded traffic split |
| `gsc content-decay` | Detect pages losing clicks and impressions |
| `gsc new-keywords` | Discover newly ranking keywords |

### Ahrefs (10)

| Command | Description |
|---|---|
| `ahrefs overview` | Domain Rating, backlinks, organic traffic |
| `ahrefs keywords` | Top organic keyword rankings |
| `ahrefs backlinks` | Backlink profile analysis |
| `ahrefs top-pages` | Best performing pages by organic traffic |
| `ahrefs competitors` | Top organic competitors |
| `ahrefs content-gap` | Keywords competitors rank for but you don't |
| `ahrefs broken-links` | Broken backlinks for reclamation |
| `ahrefs new-links` | Recently acquired and lost backlinks |
| `ahrefs dr-history` | Domain Rating trend over time |
| `ahrefs anchor-analysis` | Anchor text distribution analysis |

### Cross-MCP & Advanced (5)

| Command | Description |
|---|---|
| `serp` | SERP analysis with ranking data |
| `content-brief` | SEO content brief from live SERP + GSC data |
| `site-audit-pro` | Comprehensive audit combining Ahrefs + GSC |
| `competitor-pages` | Competitor comparison page generation |
| `brand-radar` | Brand visibility in AI and traditional search |

### Local Analysis (5)

| Command | Description |
|---|---|
| `log-analysis` | Server log analysis for crawl budget insights |
| `markdown-audit` | Audit markdown files for SEO before publishing |
| `ai-content-check` | Detect AI-generated content via text analysis |
| `programmatic` | Programmatic SEO planning for scaled pages |
| `geo` | Optimize for AI Overviews and AI search |

### Utility (1)

| Command | Description |
|---|---|
| `report` | Generate and save a complete SEO report to disk |

## MCP Setup

### Ahrefs MCP

Ahrefs MCP is connected automatically through your Claude.ai account. No local configuration needed.

### Google Search Console MCP (Optional)

GSC commands require a Google Search Console MCP server registered at **user scope** (not project scope). Project-scoped MCPs cause subagent hallucination issues.

1. Install a GSC MCP server (e.g. [google-searchconsole-mcp](https://github.com/lionkiii/google-searchconsole-mcp))
2. Add it to `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "google-search-console": {
      "command": "node",
      "args": ["/path/to/your/gsc-mcp/dist/index.js"]
    }
  }
}
```

3. Verify registration:

```bash
bash scripts/verify-mcp-scope.sh
```

## Contributing

1. Fork the repo
2. Create a feature branch
3. Run `bash scripts/smoke-test.sh` to verify changes
4. Open a PR

## License

[MIT](LICENSE)
