---
phase: 03-cross-mcp-differentiating
plan: "01"
subsystem: seo-skills
tags: [serp, content-brief, ahrefs, gsc, cross-mcp]
dependency_graph:
  requires: []
  provides: [seo-serp/SKILL.md, seo-content-brief/SKILL.md, ahrefs-api-reference phase-3-mappings]
  affects: [skills/seo/SKILL.md routing table, Phase 3 plan 02 (seo-brand-radar)]
tech_stack:
  added: []
  patterns: [Ahrefs-primary + WebMCP-optional architecture, inlined SERP logic, optional GSC overlay, ToolSearch schema discovery before API calls]
key_files:
  created:
    - skills/seo-serp/SKILL.md
    - skills/seo-content-brief/SKILL.md
  modified:
    - skills/seo/references/ahrefs-api-reference.md
decisions:
  - "[03-01]: seo-serp uses Ahrefs-primary + WebMCP-optional — Ahrefs-only is default mode; WebMCP enriches top-3 titles if available"
  - "[03-01]: seo-content-brief inlines SERP logic — skills cannot call each other as sub-routines in Claude Code"
  - "[03-01]: ToolSearch schema discovery step is mandatory before serp-overview call — parameter name (keyword/query/term) is unverified"
  - "[03-01]: GSC overlay in content-brief is non-blocking — brief generates from SERP data alone when GSC unavailable"
metrics:
  duration: "~3min"
  completed_date: "2026-03-02"
  tasks_completed: 2
  files_created: 2
  files_modified: 1
---

# Phase 3 Plan 01: seo-serp and seo-content-brief Sub-Skills Summary

**One-liner:** SERP analysis sub-skill (Ahrefs-primary, WebMCP-optional) and content brief generator (inlined SERP + optional GSC overlay) with ToolSearch schema discovery for unverified API parameter names.

## What Was Built

### Task 1 — ahrefs-api-reference.md + seo-serp/SKILL.md

**ahrefs-api-reference.md updates:**
- Added `serp` row mapping to `mcp__claude_ai_ahrefs__serp-overview`
- Added `brand-radar` row mapping to all four brand-radar MCP tools
- Updated Phase 3 note from "available" to "active"

**skills/seo-serp/SKILL.md:**
- Follows Phase 2 sub-skill pattern (frontmatter, References, Inputs, MCP Check, Execution, Output Format, Errors)
- Primary MCP: Ahrefs (required — stop if unavailable)
- Secondary MCP: WebMCP (optional — enriches top 3 URLs with page title/H1 for content angle analysis)
- Ahrefs-only mode is the primary operating mode (per STATE.md blocker about WebMCP connection conflict)
- SERP difficulty assessment: average DR of top 10 with Low/Moderate/High/Very High scale
- ToolSearch schema discovery step: discovers serp-overview parameter name before calling API

### Task 2 — seo-content-brief/SKILL.md

**skills/seo-content-brief/SKILL.md:**
- Full Phase 2 sub-skill pattern
- Step 1: Inlined SERP analysis (serp-overview via ToolSearch-discovered parameter name)
- Step 2: Keyword volume/KD from keywords-explorer-overview (non-blocking)
- Step 3: GSC overlay via query_search_analytics (only when site param provided + GSC available)
- Step 4: Brief synthesis combining SERP patterns + keyword data + current position
- Copy-pasteable output format: word count target, H2 structure, semantic keywords, differentiation angle
- Explicit note: "SERP analysis is inlined here — skills cannot call each other as sub-routines in Claude Code"

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Ahrefs-only as primary mode for seo-serp | STATE.md blocker: WebMCP connection status conflict; design for graceful fallback |
| Inline SERP logic in content-brief | Claude Code skills cannot call each other as sub-routines; inlining is the only option |
| ToolSearch schema discovery mandatory | serp-overview parameter name unverified (open question from research) — runtime discovery required |
| GSC overlay non-blocking | Content brief is valuable from SERP data alone; GSC adds current position context but isn't required |

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check

### Files exist:
- `skills/seo-serp/SKILL.md` — FOUND
- `skills/seo-content-brief/SKILL.md` — FOUND
- `skills/seo/references/ahrefs-api-reference.md` — FOUND (modified)

### Commits exist:
- `07414f0` — feat(03-01): add seo-serp SKILL.md and update ahrefs-api-reference with Phase 3 tool mappings
- `6ecc429` — feat(03-01): create seo-content-brief SKILL.md with inlined SERP logic and GSC overlay

## Self-Check: PASSED
