# Phase 1: Foundation - Context

**Gathered:** 2026-03-02
**Status:** Ready for planning

<domain>
## Phase Boundary

Install infrastructure, YAML validation, MCP scoping, shared reference files, Python helper scripts, and orchestrator routing table for the expanded 27-command SEO skill system. This phase makes the system installable and routable — no live-data commands are built here.

</domain>

<decisions>
## Implementation Decisions

### Directory layout
- All 27 sub-skills stay FLAT under `~/.claude/skills/` — same pattern as the existing 12 (seo-audit/, seo-page/, etc.)
- GSC sub-commands become: seo-gsc-overview/, seo-gsc-drops/, seo-gsc-opportunities/, etc.
- Ahrefs sub-commands become: seo-ahrefs-overview/, seo-ahrefs-backlinks/, seo-ahrefs-keywords/, etc.
- Standalone new commands (serp, brand-radar, site-audit-pro, etc.) follow same flat pattern
- No nesting — everything at the same level under ~/.claude/skills/

### Install mechanism
- Auto-create Python venv at `~/.claude/skills/seo/.venv/` during install with pip install from requirements.txt
- User has local GSC MCP at `/Users/aash-zsbch1500/Desktop/GSC-MCP` — install script should register MCPs in `~/.claude/mcp.json` at user scope (not project scope, per project decision)

### Command routing
- Two-level routing: main SKILL.md sees "gsc" → routes to the specific gsc sub-command skill (seo-gsc-overview/, seo-gsc-drops/, etc.)
- Routing table grows incrementally per phase — Phase 1 includes existing 12 commands only
- Phase 2+ adds GSC, Ahrefs, and other entries as commands are built
- Logic lives in each sub-skill's SKILL.md (not in agent files) — agents only used for parallel audit work

### MCP error handling
- Error + fallback suggestion pattern: clear message + alternative command that works without the MCP
- MCP availability checks happen inside each sub-skill (self-contained, not at orchestrator level)
- Build shared reference file `references/mcp-degradation.md` in Phase 1 with error templates, fallback mapping, and check patterns
- All future MCP-dependent skills @-reference this file for consistent degradation behavior

### Claude's Discretion
- Install script mechanism (curl|bash, git clone + symlink, or other)
- Source repo directory layout (mirror ~/.claude/ structure vs other organization)
- Whether to update SEO Health Score weights in Phase 1 or defer to when new categories are built
- YAML validation approach (pre-commit hook, install-time check, or both)

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `seo/SKILL.md`: Main orchestrator with 12-command routing table, scoring methodology, industry detection — needs expansion for two-level routing
- `seo/references/`: 4 reference files (cwv-thresholds.md, eeat-framework.md, quality-gates.md, schema-types.md) — on-demand loading pattern to follow
- `seo/scripts/`: 4 Python scripts (fetch_page.py, parse_html.py, capture_screenshot.py, analyze_visual.py) — established helper pattern
- `seo/hooks/`: pre-commit-seo-check.sh, validate-schema.py — existing validation hooks
- `seo/.venv/` + `requirements.txt`: Python dependency management already in place
- 6 agent files in `~/.claude/agents/`: seo-content, seo-performance, seo-schema, seo-sitemap, seo-technical, seo-visual

### Established Patterns
- Sub-skills are flat directories under `~/.claude/skills/` with a SKILL.md each
- Agent files live in `~/.claude/agents/` as standalone .md files
- Reference files loaded on-demand (not all at startup) via `references/` directory
- Python scripts called from skills via Bash tool
- SKILL.md frontmatter includes: name, description, allowed-tools

### Integration Points
- Main `seo/SKILL.md` is the entry point — all routing starts here
- `~/.claude/mcp.json` for MCP registration (must be user-scope, not project-scope)
- Sub-skill SKILL.md files are loaded by the orchestrator based on command match

</code_context>

<specifics>
## Specific Ideas

- Local GSC MCP source at `/Users/aash-zsbch1500/Desktop/GSC-MCP` — install script should handle registering this
- Ahrefs MCP is already available as a Claude.ai MCP (connected per project spec)
- User wants to focus on getting SEO commands working first, MCP integration comes in Phase 2

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-foundation*
*Context gathered: 2026-03-02*
