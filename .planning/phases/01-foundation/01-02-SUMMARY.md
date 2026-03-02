---
phase: 01-foundation
plan: 02
subsystem: skill-routing
tags: [skill-md, routing, mcp, ahrefs, gsc, reference, degradation, cents-to-usd]

# Dependency graph
requires:
  - 01-01: install infrastructure, validate-yaml.py, skills/ source directory
provides:
  - skills/seo/SKILL.md: expanded 27-command routing table with two-level routing
  - skills/seo/references/mcp-degradation.md: MCP availability checks, error templates, fallback mapping
  - skills/seo/references/ahrefs-api-reference.md: Ahrefs tool mapping and cents-to-USD convention
  - skills/seo/references/gsc-api-reference.md: GSC placeholder mapping and property format warning
affects:
  - All Phase 2 GSC/Ahrefs sub-skills: must @-reference mcp-degradation.md and ahrefs-api-reference.md
  - All Phase 3 multi-MCP skills: must use fallback mapping from mcp-degradation.md
  - seo-site-audit-pro: must check MCP availability per sub-skill (self-contained pattern)

# Tech tracking
tech-stack:
  added: []
  patterns:
    - Two-level routing: gsc and ahrefs commands route through group → sub-command → sub-skill SKILL.md
    - Self-contained MCP checks: each sub-skill checks its own MCP at execution start (not at orchestrator)
    - On-demand reference loading: reference files are @-referenced only when needed, not at startup
    - Unavailable command response: Phase 2+ commands return clear message with fallback suggestion
    - Cents-to-USD convention: Ahrefs monetary values always divided by 100 before display

key-files:
  created:
    - skills/seo/references/mcp-degradation.md
    - skills/seo/references/ahrefs-api-reference.md
    - skills/seo/references/gsc-api-reference.md
  modified:
    - skills/seo/SKILL.md (expanded from 12 to 27 commands, added routing section)

key-decisions:
  - "YAML description trimmed to 998 chars to pass validate-yaml.py 1000-char limit — expanded orchestrator description fits within limit with concise phrasing"
  - "Routing table lists 37 rows (27 unique commands + duplicates from grouped gsc/ahrefs sub-commands) — the canonical 27-command count refers to user-facing commands"
  - "MCP checks are self-contained per sub-skill, not at the seo/SKILL.md orchestrator level — per user decision from Phase 1 planning"
  - "GSC API reference leaves all tool names as TBD/UNVERIFIED — honesty about unknowns prevents incorrect assumptions in Phase 2 builds"

patterns-established:
  - "Self-contained MCP availability: each sub-skill is responsible for its own MCP checks using ToolSearch"
  - "Cents-to-USD: all Ahrefs monetary fields must be divided by 100 before display — documented in ahrefs-api-reference.md"
  - "Degraded mode standards: never silently skip data, always tell user what's missing and suggest fallback"

requirements-completed:
  - FOUND-02
  - FOUND-03
  - FOUND-05
  - FOUND-06

# Metrics
duration: 4min
completed: 2026-03-02
---

# Phase 1 Plan 02: SEO Skill Routing and MCP Reference Files Summary

**27-command routing table with two-level gsc/ahrefs sub-routing, MCP degradation error templates, Ahrefs cents-to-USD convention, and GSC placeholder reference with unverified property format warning**

## Performance

- **Duration:** 4 min
- **Started:** 2026-03-02T06:31:58Z
- **Completed:** 2026-03-02T06:35:58Z
- **Tasks:** 2
- **Files modified:** 4 (1 modified, 3 created)

## Accomplishments

- Expanded seo/SKILL.md from 12 to 27 commands with Quick Reference grouped by phase (active/Phase 2/Phase 3)
- Added two-level Command Routing section: Level 1 group detection, Level 2 sub-command routing for gsc (9) and ahrefs (10)
- Added full Routing Table mapping all 27 commands to sub-skill directory names
- Added Unavailable Command Response pattern for Phase 2+ commands with example response
- Created mcp-degradation.md: ToolSearch-based MCP checks, 4 error templates, fallback table, degraded mode standards
- Created ahrefs-api-reference.md: 10 sub-command to MCP tool mappings, CRITICAL cents-to-USD convention, common response fields, rate limiting guidance
- Created gsc-api-reference.md: placeholder tool mapping (all TBD), property format warning (UNVERIFIED), Phase 2 discovery checklist

## Task Commits

Each task was committed atomically:

1. **Task 1: Expand seo/SKILL.md with 27-command routing table** - `0002108` (feat)
2. **Task 2: Create MCP degradation, Ahrefs API, and GSC API reference files** - `f1b6d7d` (feat)

**Plan metadata:** (docs commit — created after this summary)

## Files Created/Modified

- `skills/seo/SKILL.md` - Expanded with 27-command Quick Reference, two-level Command Routing, full Routing Table, updated description and Sub-Skills list
- `skills/seo/references/mcp-degradation.md` - MCP availability checks, error templates, fallback mapping, degraded mode standards
- `skills/seo/references/ahrefs-api-reference.md` - Ahrefs tool name mapping, cents-to-USD convention, response fields, rate limiting
- `skills/seo/references/gsc-api-reference.md` - GSC placeholder mapping (TBD), property format warning, Phase 2 discovery checklist

## Decisions Made

- YAML description trimmed from 1072 chars to ~998 chars to pass validate-yaml.py 1000-char limit; content preserved with more concise phrasing
- MCP availability checks placed inside each sub-skill (self-contained), not at the seo/SKILL.md orchestrator level — per user decision documented in PLAN.md
- GSC API reference deliberately leaves all tool names as TBD and property format as UNVERIFIED — prevents incorrect assumptions from propagating into Phase 2 sub-skill builds
- Ahrefs cents-to-USD convention documented prominently at the top of ahrefs-api-reference.md, listed as CRITICAL, and in every relevant response field entry

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Trimmed YAML description to pass validate-yaml.py 1000-char limit**
- **Found during:** Task 1 verification (running validate-yaml.py against updated SKILL.md)
- **Issue:** Expanded description for 27-command orchestrator reached 1072 chars; validate-yaml.py enforces 1000-char max set in Plan 01
- **Fix:** Rewrote description with more concise phrasing preserving all key triggers and capabilities; final description is ~998 chars
- **Files modified:** skills/seo/SKILL.md
- **Verification:** `~/.claude/skills/seo/.venv/bin/python skills/seo/hooks/validate-yaml.py skills/seo/SKILL.md` → PASS
- **Committed in:** 0002108 (Task 1 commit, description edit applied before commit)

---

**Total deviations:** 1 auto-fixed (description length exceeded validator limit)
**Impact on plan:** Required fix; no scope creep.

## Verification Results

All 6 plan verification checks passed:
1. `grep -ci "routing\|route" skills/seo/SKILL.md` → 6 (5+ required) — PASS
2. `grep "27" skills/seo/SKILL.md` → 5 matches — PASS
3. `grep "divide by 100" skills/seo/references/ahrefs-api-reference.md` → multiple matches — PASS
4. `grep -c "fallback" skills/seo/references/mcp-degradation.md` → 5 — PASS
5. `grep -c "UNVERIFIED\|TBD" skills/seo/references/gsc-api-reference.md` → 13 — PASS
6. `validate-yaml.py skills/seo/SKILL.md` → PASS (1/1)

## Next Phase Readiness

- seo/SKILL.md routes all 27 commands and handles Phase 2+ gracefully with clear user messages
- mcp-degradation.md provides reusable error and fallback patterns for all Phase 2/3 sub-skill builds
- ahrefs-api-reference.md ready for Phase 2 — all 10 sub-command tool mappings documented
- gsc-api-reference.md ready for Phase 2 discovery — checklist guides tool name verification
- Phase 2 can begin building GSC and Ahrefs sub-skills with consistent error handling from day one

## Self-Check: PASSED

All files verified present. All commits verified in git log.

- FOUND: skills/seo/SKILL.md (expanded, 27 commands)
- FOUND: skills/seo/references/mcp-degradation.md
- FOUND: skills/seo/references/ahrefs-api-reference.md
- FOUND: skills/seo/references/gsc-api-reference.md
- FOUND: 0002108 (Task 1 commit)
- FOUND: f1b6d7d (Task 2 commit)

---
*Phase: 01-foundation*
*Completed: 2026-03-02*
