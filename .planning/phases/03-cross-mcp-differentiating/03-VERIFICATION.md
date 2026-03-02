---
phase: 03-cross-mcp-differentiating
verified: 2026-03-02T00:00:00Z
status: passed
score: 5/5 must-haves verified
gaps: []
human_verification:
  - test: "Run /seo serp <keyword> with Ahrefs MCP connected"
    expected: "Returns SERP table with Rank, URL, DR, Est. Traffic, Content Angle columns populated from live Ahrefs data"
    why_human: "Cannot verify live Ahrefs API response at verification time — requires active MCP session"
  - test: "Run /seo content-brief <keyword> site=<gsc-property>"
    expected: "Returns copy-pasteable brief with Current Position section showing GSC click/impression data overlaid onto SERP table"
    why_human: "GSC overlay path requires live MCP session to confirm both data sources are merged in output"
  - test: "Run /seo brand-radar <brand> with Ahrefs disconnected"
    expected: "Hard stop with clear error message; no estimated or fabricated brand data is returned"
    why_human: "Error path requires Ahrefs to actually be disconnected during the session"
  - test: "Run /seo site-audit-pro <domain> with one Wave 1 tool returning a simulated rate-limit"
    expected: "Audit continues through remaining waves; 'SKIPPED: {tool} — rate limit' appears in checkpoint file; final report lists skipped data sources"
    why_human: "Rate-limit resilience requires injecting a real error condition; cannot simulate programmatically in verification"
  - test: "Run /seo report monthly <domain> and check disk after session ends"
    expected: "A file seo-report-YYYY-MM-DD-domain-monthly.md exists at the printed absolute path and contains an Executive Summary section"
    why_human: "File persistence requires running Write tool in a live session to confirm file is created on disk"
---

# Phase 3: Cross-MCP Differentiating — Verification Report

**Phase Goal:** Users can run commands that synthesize Ahrefs and GSC data together for insights neither source alone provides, including the flagship multi-agent site audit and automated report generation.
**Verified:** 2026-03-02
**Status:** passed
**Re-verification:** No — initial verification

---

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|---------|
| 1 | `/seo serp <keyword>` returns live SERP composition from Ahrefs SERP data with graceful fallback if WebMCP is unavailable | VERIFIED | `skills/seo-serp/SKILL.md` calls `mcp__claude_ai_ahrefs__serp-overview` with ToolSearch schema discovery; WebMCP is a non-blocking secondary check; Ahrefs-only mode is the primary path with explicit note in output |
| 2 | `/seo content-brief <keyword>` generates a structured brief combining SERP analysis and optional GSC data — output is copy-pasteable | VERIFIED | `skills/seo-content-brief/SKILL.md` inlines SERP logic (explicit note in file), overlays GSC via `query_search_analytics` when `site` param provided, output section is explicitly flagged "copy-pasteable for content writers with no further editing needed" |
| 3 | `/seo brand-radar <brand>` returns AI search visibility data; if endpoint unavailable, returns clear error not fabricated results | VERIFIED | `skills/seo-brand-radar/SKILL.md` line 40-43: "CRITICAL — No Fallback: Do NOT estimate or fabricate brand monitoring data." Hard stop on Ahrefs unavailability. Runtime ToolSearch schema discovery for unverified Brand Radar API |
| 4 | `/seo site-audit-pro <domain>` completes without crashing when any single agent hits a rate-limit — audit continues with remaining agents and notes skipped data in output | VERIFIED | `skills/seo-site-audit-pro/SKILL.md`: "A failed tool call NEVER stops the wave or the audit"; 27 occurrences of "SKIPPED" pattern; "Skipped Data Sources" table in final report; GSC unavailability is non-fatal |
| 5 | `/seo report <type> <domain>` generates a markdown file saved to disk with cross-referenced Ahrefs and GSC data — file is viewable after session ends | VERIFIED | `skills/seo-report/SKILL.md`: Write tool in `allowed-tools`; Step 0 generates absolute path via Bash; Step 4 calls Write tool with `file_path`; Step 5 prints `"Report saved to: {absolute_file_path}"` to terminal |

**Score:** 5/5 truths verified

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `skills/seo-serp/SKILL.md` | SERP analysis via Ahrefs serp-overview | VERIFIED | Exists, 156 lines, substantive: 5 occurrences of `serp-overview`, ToolSearch discovery step, MCP check, output table, error templates. Deployed to `~/.claude/skills/seo-serp/SKILL.md` (diff: MATCH) |
| `skills/seo-content-brief/SKILL.md` | AI content brief from SERP + optional GSC | VERIFIED | Exists, 241 lines, substantive: 2 occurrences of `serp-overview`, 2 occurrences of `inlined`, GSC overlay via `google-search-console` ToolSearch. Deployed to `~/.claude/skills/seo-content-brief/SKILL.md` |
| `skills/seo-brand-radar/SKILL.md` | Brand Radar via Ahrefs brand-radar-* tools | VERIFIED | Exists, 170 lines, substantive: 2 occurrences of `brand-radar-mentions-overview`, 1 occurrence of "Schema Discovery", explicit no-fabrication guard. Deployed to `~/.claude/skills/seo-brand-radar/SKILL.md` |
| `skills/seo-report/SKILL.md` | Report generation with 4 type templates, Write tool | VERIFIED | Exists, 284 lines, substantive: 5 occurrences of `Write`, 4 occurrences of `seo-report-` filename convention, 2 occurrences of "Executive Summary", all 4 report types (monthly/weekly/audit/competitor) defined. Deployed to `~/.claude/skills/seo-report/SKILL.md` (diff: MATCH) |
| `skills/seo-site-audit-pro/SKILL.md` | Sequential wave audit with checkpoint saves | VERIFIED | Exists, 523 lines, substantive: 7 occurrences of "Wave 1", 8 occurrences of "Checkpoint", 27 occurrences of "SKIPPED", 5 occurrences of "sequential/SEQUENTIAL", Cross-MCP Insights section present. Deployed to `~/.claude/skills/seo-site-audit-pro/SKILL.md` |
| `skills/seo/SKILL.md` | Updated routing table with 37 active commands | VERIFIED | Routing table has all 37 entries at "active" status; Phase 3 section shows 5 Cross-MCP commands; description reads "37 active"; Sub-Skills section lists all 37 with Phase 3 group marked Active |
| `skills/seo/references/ahrefs-api-reference.md` | Phase 3 tool mappings added | VERIFIED | Line 44: `serp → mcp__claude_ai_ahrefs__serp-overview`; Line 45: `brand-radar → 4 brand-radar-* tools`; Line 47 note updated to "now active" |

---

## Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `skills/seo-serp/SKILL.md` | `mcp__claude_ai_ahrefs__serp-overview` | ToolSearch discovery then direct tool call | WIRED | Step 1 uses ToolSearch `serp-overview`, Step 2 calls `mcp__claude_ai_ahrefs__serp-overview` with discovered param name |
| `skills/seo-content-brief/SKILL.md` | `mcp__claude_ai_ahrefs__serp-overview` | Inlined SERP logic (not sub-skill call) | WIRED | Steps 1a-1b inline the serp-overview call; explicit note "SERP analysis is inlined here — skills cannot call each other" |
| `skills/seo-content-brief/SKILL.md` | GSC `query_search_analytics` | Optional overlay when `site` param provided | WIRED | Step 3 uses ToolSearch `+google-search-console` and calls `query_search_analytics` conditionally |
| `skills/seo-brand-radar/SKILL.md` | `mcp__claude_ai_ahrefs__brand-radar-mentions-overview` | ToolSearch discovery then direct tool call | WIRED | Step 1 ToolSearch `brand-radar` discovers params; Steps 2-5 call all four brand-radar-* tools |
| `skills/seo-report/SKILL.md` | Write tool | File persistence for report output | WIRED | `Write` in `allowed-tools`; Step 4 explicitly calls Write with `file_path` (absolute) and `content` |
| `skills/seo-report/SKILL.md` | Multiple Ahrefs/GSC tools | Data gathering per report type | WIRED | All 4 report types have explicit tool call sequences referencing `mcp__claude_ai_ahrefs__*` and GSC `query_search_analytics` |
| `skills/seo-site-audit-pro/SKILL.md` | Multiple Ahrefs MCP tools | Sequential wave tool calls with checkpoint saves | WIRED | Wave 1: 4 tools; Wave 2: 3-4 tools; Wave 3: 2-4 tools; checkpoint Write after each wave |
| `skills/seo-site-audit-pro/SKILL.md` | GSC MCP tools | Optional GSC overlay in Waves 2 and 3 | WIRED | Wave 2 tool 2d and Wave 3 tools 3a-3b include GSC `query_search_analytics` calls gated on `site` param and GSC availability |
| `skills/seo/SKILL.md` | 5 Phase 3 sub-skill directories | Routing table entries changed from Phase 3 to active | WIRED | Lines 170-174: all 5 entries (`seo-serp/`, `seo-content-brief/`, `seo-brand-radar/`, `seo-site-audit-pro/`, `seo-report/`) show status "active" |

---

## Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-------------|-------------|--------|---------|
| CROSS-01 | 03-01-PLAN | `/seo serp <keyword>` — Live SERP via Ahrefs SERP Overview + WebMCP | SATISFIED | `skills/seo-serp/SKILL.md` exists with live Ahrefs call, WebMCP optional enrichment, graceful degradation; `ahrefs-api-reference.md` updated; REQUIREMENTS.md shows `[x]` |
| CROSS-02 | 03-01-PLAN | `/seo content-brief <keyword>` — AI content brief from SERP analysis | SATISFIED | `skills/seo-content-brief/SKILL.md` exists with inlined SERP, GSC overlay, copy-pasteable output; REQUIREMENTS.md shows `[x]` |
| CROSS-03 | 03-02-PLAN | `/seo brand-radar <brand>` — AI search brand monitoring via Ahrefs Brand Radar | SATISFIED | `skills/seo-brand-radar/SKILL.md` exists with schema discovery, hard-stop error, 4 Brand Radar tool calls; REQUIREMENTS.md shows `[x]` |
| CROSS-04 | 03-03-PLAN | `/seo site-audit-pro <domain>` — Flagship audit with sequential wave execution | SATISFIED | `skills/seo-site-audit-pro/SKILL.md` exists with 3 waves, checkpoints, SKIPPED logging, Cross-MCP synthesis; REQUIREMENTS.md shows `[x]` |
| CROSS-05 | 03-02-PLAN | `/seo report <type> <domain>` — Automated SEO report generation | SATISFIED | `skills/seo-report/SKILL.md` exists with Write tool, 4 report types, Executive Summary, absolute path confirmation; REQUIREMENTS.md shows `[x]` |

All 5 CROSS requirements are tracked in REQUIREMENTS.md with status `[x]` (complete) and the Phase 3 tracking table shows all 5 at "Complete".

No orphaned requirements found — all 5 CROSS-0x IDs are claimed by plan frontmatter (`03-01-PLAN` claims CROSS-01, CROSS-02; `03-02-PLAN` claims CROSS-03, CROSS-05; `03-03-PLAN` claims CROSS-04).

---

## Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| `skills/seo-site-audit-pro/SKILL.md` | 84 | "Use Bash: `echo "$(pwd)/seo-audit-pro-checkpoint-{domain}.md"`" — `{domain}` is a template literal placeholder, not a shell variable | Info | No functional impact — skill is a prompt document instructing Claude; Claude interprets `{domain}` as the runtime value |
| `skills/seo-report/SKILL.md` | 60 | Same `{domain}` and `{type}` in Bash echo template | Info | Same as above — expected pattern for skill instruction documents |

No blockers found. No stub implementations. No TODO/FIXME/placeholder comments in implementation logic. No empty handlers.

---

## Deployment Verification

All 5 Phase 3 skill directories confirmed present in `~/.claude/skills/`:
- `~/.claude/skills/seo-serp/` — present
- `~/.claude/skills/seo-content-brief/` — present
- `~/.claude/skills/seo-brand-radar/` — present
- `~/.claude/skills/seo-report/` — present
- `~/.claude/skills/seo-site-audit-pro/` — present

Spot-checked deployed `seo-serp/SKILL.md` and `seo-report/SKILL.md` against source — diff: MATCH (no deployment drift).

All 6 phase commits verified in git log:
- `07414f0` — feat(03-01): seo-serp SKILL.md + ahrefs-api-reference Phase 3 mappings
- `6ecc429` — feat(03-01): seo-content-brief SKILL.md
- `99ed44e` — feat(03-02): seo-brand-radar SKILL.md
- `8060131` — feat(03-02): seo-report SKILL.md
- `f976279` — feat(03-03): seo-site-audit-pro SKILL.md
- `eec5e90` — feat(03-03): routing table update + deploy

---

## Human Verification Required

The 5 automated checks above confirm all skills are substantive, wired, and deployed. The following items require a live Claude session to confirm end-to-end behavior:

### 1. Live SERP Data Return

**Test:** Run `/seo serp best CRM software` in a Claude session with Ahrefs MCP connected
**Expected:** SERP table with Rank, URL (truncated), DR, Est. Traffic, Content Angle columns populated; SERP Difficulty assessment shown; monetary fields divided by 100 for USD
**Why human:** Cannot verify live Ahrefs API response or schema discovery outcome programmatically

### 2. Content Brief GSC Overlay

**Test:** Run `/seo content-brief "project management software" site=sc-domain:example.com` with both Ahrefs and GSC MCPs connected
**Expected:** Copy-pasteable brief includes "Current Position" section showing GSC clicks/impressions/CTR/position for that keyword alongside SERP table and H2 suggestions
**Why human:** Requires both MCPs live; GSC overlay path cannot be traced statically

### 3. Brand Radar Hard Stop (No Fabrication)

**Test:** Run `/seo brand-radar notion` with Ahrefs MCP disconnected
**Expected:** Immediate stop with "Ahrefs Brand Radar Not Available" error; no estimated brand visibility data, no fallback attempt
**Why human:** Requires Ahrefs to actually be disconnected to exercise the error path

### 4. Site Audit Pro Rate-Limit Resilience

**Test:** Run `/seo site-audit-pro example.com` and verify behavior when one tool call fails
**Expected:** Checkpoint file is created and updated after each wave; failed tools appear as "SKIPPED: {tool} — {reason}" in checkpoint and final report; remaining waves complete
**Why human:** Rate-limit injection requires a real error condition; checkpoint file creation requires Write tool execution in a live session

### 5. Report File Persistence

**Test:** Run `/seo report monthly example.com` and after the session, check disk for the file
**Expected:** File `seo-report-YYYY-MM-DD-example.com-monthly.md` exists at the absolute path printed to terminal; file contains Executive Summary section with analytical narrative (not raw data dump)
**Why human:** File write requires live Write tool execution; post-session file existence cannot be verified without running the command

---

## Summary

Phase 3 goal is achieved at the skill specification level. All 5 cross-MCP commands (`serp`, `content-brief`, `brand-radar`, `site-audit-pro`, `report`) are:

1. **Substantive** — each SKILL.md contains full execution logic, not placeholders
2. **Wired** — all MCP tool connections are explicitly specified with ToolSearch discovery patterns for unverified API schemas
3. **Deployed** — all 5 sub-skill directories present in `~/.claude/skills/`
4. **Routed** — `seo/SKILL.md` routing table shows all 37 commands active

Key architectural properties verified:
- `seo-serp`: Ahrefs-primary + WebMCP-optional architecture; Ahrefs-only mode is the default path
- `seo-content-brief`: SERP logic inlined (not a sub-skill call); GSC overlay non-blocking
- `seo-brand-radar`: Hard stop on Ahrefs unavailability; runtime schema discovery; no fabrication path
- `seo-site-audit-pro`: Sequential wave architecture (GitHub Issue #6594 honored); SKIPPED logging; Cross-MCP synthesis gated on dual data source presence; API usage warning before execution
- `seo-report`: Write tool for file persistence (first in project); 4 report types; AI executive summary; absolute path confirmation

5 items flagged for human verification (live MCP session required) — all are behavioral/runtime checks, not structural gaps.

---

_Verified: 2026-03-02_
_Verifier: Claude (gsd-verifier)_
