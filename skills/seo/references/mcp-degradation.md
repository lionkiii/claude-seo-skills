<!-- Updated: 2026-03-02 -->

# MCP Degradation Reference

Reusable patterns for MCP availability checks, error templates, and fallback
mappings. All MCP-dependent sub-skills should @-reference this file and check
their own MCP requirements at execution start (self-contained, not at orchestrator
level).

## MCP Availability Check Patterns

Each sub-skill checks its own MCP requirements before proceeding. Use these patterns:

### Ahrefs MCP Check
```
Use ToolSearch with query "+ahrefs"
- If tools returned → Ahrefs MCP is available, proceed
- If no tools returned → use the Ahrefs error template below
```

### GSC MCP Check
```
Use ToolSearch with query "+google-search-console"
- If tools returned → GSC MCP is available, proceed
- If no tools returned → check ~/.claude/mcp.json for GSC entry as fallback
- If still not found → use the GSC error template below

GSC MCP: must be registered at user scope in ~/.claude/mcp.json (not project scope)
Note: Project-scoped MCPs cause subagents to silently hallucinate (GitHub Issue #13898)
```

### WebMCP Check
```
Use ToolSearch with query "+webmcp"
- If tools returned → WebMCP is available, proceed
- If no tools returned → use Ahrefs-only mode where possible (see fallback table)
```

## Error Templates

Use these standard formats when an MCP is unavailable. Substitute values in `{}`.

### Standard MCP Unavailability Template

```
## {MCP Name} Not Available

The `{command}` command requires {MCP Name} MCP, which is not currently connected.

**What you can do:**
- {Fallback suggestion 1 — alternative command that works without this MCP}
- {Fallback suggestion 2 — manual alternative}

**To connect {MCP Name}:**
- {Setup instructions}
```

### Ahrefs MCP Error Template

```
## Ahrefs MCP Not Available

The `/seo ahrefs {sub-command}` command requires the Ahrefs MCP, which is not
currently connected.

**What you can do:**
- Use `/seo audit <url>` for a full static SEO analysis without live Ahrefs data
- Use `/seo technical <url>` for technical SEO issues without backlink/keyword data

**To connect Ahrefs MCP:**
- Ensure the Ahrefs MCP is registered at user scope in ~/.claude/mcp.json
- Verify with: cat ~/.claude/mcp.json | grep -i ahrefs
- Ahrefs MCP must be registered at user scope (not project scope) to work in subagents
```

### GSC MCP Error Template

```
## Google Search Console MCP Not Available

The `/seo gsc {sub-command}` command requires the GSC MCP, which is not
currently connected.

**What you can do:**
- Use `/seo technical <url>` for crawlability and indexability analysis (no live data)
- Use `/seo audit <url>` for a full static SEO audit

**To connect GSC MCP:**
- Install and configure a Google Search Console MCP server (see README for setup)
- Add it to ~/.claude/mcp.json at user scope (NOT project scope)
- Verify GSC property access before running commands (domain vs URL prefix format)
- See references/gsc-api-reference.md for property format details
```

### WebMCP Error Template

```
## WebMCP Not Available — Running Ahrefs-Only Mode

The `/seo {command}` command works best with both Ahrefs and WebMCP, but WebMCP
is not currently connected. Proceeding with Ahrefs data only.

**What's reduced:**
- {Specific capability that needs WebMCP}

**To connect WebMCP:**
- Verify WebMCP registration status in ~/.claude/mcp.json
```

## Fallback Mapping

| Command | Requires | Fallback |
|---------|----------|----------|
| `/seo gsc *` | GSC MCP | Use `/seo technical <url>` for static analysis |
| `/seo ahrefs *` | Ahrefs MCP | Use `/seo audit <url>` for static analysis |
| `/seo serp` | Ahrefs + WebMCP | Ahrefs-only mode if WebMCP unavailable |
| `/seo content-brief` | Ahrefs + GSC | Works with Ahrefs only; GSC data enriches but not required |
| `/seo brand-radar` | Ahrefs | No fallback — Ahrefs Brand Radar required |
| `/seo site-audit-pro` | All MCPs | Runs with available MCPs, skips unavailable modules |
| `/seo report` | Varies by type | Generates report with available data only, notes gaps |
| `/seo markdown-audit` | None | Always available — no MCP dependency |

## Self-Contained Check Pattern

Each sub-skill should check its own MCP at execution start using this pattern:

```
## MCP Check (at start of sub-skill execution)

1. Identify required MCPs for this command
2. Run ToolSearch for each required MCP
3. If all required MCPs available → proceed with full functionality
4. If optional MCPs missing → proceed with degraded mode, note what's reduced
5. If required MCPs missing → display error template, suggest fallback, stop

DO NOT check MCP availability at the orchestrator (seo/SKILL.md) level.
Each sub-skill is self-contained and responsible for its own MCP checks.
```

## Degraded Mode Standards

When running in degraded mode (some MCPs unavailable):
- Always tell the user which MCPs are missing and what data is unavailable
- Always suggest the best available alternative
- Never silently skip data or fabricate metrics
- Clearly label all output as "static analysis" or "Ahrefs-only" as appropriate
