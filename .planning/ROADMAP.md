# Roadmap: Claude SEO Skill Expansion

## Overview

This project expands the existing 12-command claude-seo skill system to 27 commands by integrating live data from Ahrefs MCP and Google Search Console MCP. The build proceeds in four phases: first, establish a working foundation with correct MCP scoping and YAML validation to prevent silent failures; second, deliver the highest-value live-data commands (GSC + Ahrefs + markdown-audit) that prove the integration works; third, build the cross-MCP differentiating commands that combine data sources for insights no web dashboard can replicate; fourth, enhance the original 12 commands with live data overlays and add the MCP-independent local analysis tools.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Foundation** - Install infrastructure, YAML validation, MCP scoping, shared references, and orchestrator routing table
- [ ] **Phase 2: Core Live Data** - GSC commands (9), Ahrefs commands (10), and markdown-audit — the primary differentiators over static analysis
- [ ] **Phase 3: Cross-MCP & Differentiating** - SERP analysis, content briefs, brand radar, site-audit-pro flagship, and automated reporting
- [ ] **Phase 4: Enhanced Originals & Local Analysis** - Upgrade the 12 original commands with MCP overlays; add log analysis, AI content check, internal links, local SEO, and migration validation

## Phase Details

### Phase 1: Foundation
**Goal**: The skill system installs correctly, MCPs are scoped at user level, YAML validation catches errors before they cause silent failures, shared reference files load on demand, and the orchestrator routes all 27 commands
**Depends on**: Nothing (first phase)
**Requirements**: FOUND-01, FOUND-02, FOUND-03, FOUND-04, FOUND-05, FOUND-06
**Success Criteria** (what must be TRUE):
  1. Running the install script places all SKILL.md files in `~/.claude/skills/seo/` and all agent files in `~/.claude/agents/` without errors
  2. `/seo` invoked with any of the 27 command names routes to the correct sub-skill with no "command not found" responses
  3. Invoking a command that requires an unavailable MCP returns a human-readable error message with a fallback suggestion rather than silent failure or hallucinated data
  4. The YAML validation script catches a malformed frontmatter file and exits non-zero before any skill is deployed
  5. Ahrefs monetary values in any output always show dollars (e.g., "$1,250") not raw cents (e.g., "125000")
**Plans**: TBD

Plans:
- [ ] 01-01: Install script, directory structure, YAML validation pre-commit hook, and MCP user-scope registration verification
- [ ] 01-02: Orchestrator `seo/SKILL.md` with 27-command routing table, shared reference files (CWV thresholds, E-E-A-T, schema types, Ahrefs API reference, GSC API reference), Python helper scripts, and graceful degradation pattern

### Phase 2: Core Live Data
**Goal**: Users can query real GSC performance data and live Ahrefs data through 19 commands, and can audit markdown files locally — these are the commands that replace estimated data with actual data
**Depends on**: Phase 1
**Requirements**: GSC-01, GSC-02, GSC-03, GSC-04, GSC-05, GSC-06, GSC-07, GSC-08, GSC-09, AHRF-01, AHRF-02, AHRF-03, AHRF-04, AHRF-05, AHRF-06, AHRF-07, AHRF-08, AHRF-09, AHRF-10, LOCAL-01
**Success Criteria** (what must be TRUE):
  1. `/seo gsc overview <site>` returns actual clicks, impressions, CTR, and average position sourced from the live GSC MCP — not estimates
  2. `/seo ahrefs overview <domain>` returns real Domain Rating, backlink count, organic keyword count, and traffic estimate in USD (not cents)
  3. `/seo gsc drops <site>` identifies pages and keywords that lost traffic in the past 28 days with percentage deltas, sourced from GSC MCP
  4. `/seo ahrefs content-gap <domain>` lists keywords that competitor domains rank for that the target domain does not, sourced from Ahrefs MCP
  5. `/seo markdown-audit <path>` analyzes a local markdown file and returns SEO improvement recommendations with no MCP connection required
**Plans**: TBD

Plans:
- [ ] 02-01: GSC sub-skill (`seo/gsc/SKILL.md`) with all 9 sub-commands (overview, drops, opportunities, cannibalization, index-issues, compare, brand-vs-nonbrand, content-decay, new-keywords) and `seo-gsc-analyst` agent
- [ ] 02-02: Ahrefs sub-skill (`seo/ahrefs/SKILL.md`) with all 10 sub-commands (overview, backlinks, keywords, competitors, content-gap, broken-links, new-links, anchor-analysis, dr-history, top-pages) and `seo-ahrefs-analyst` agent
- [ ] 02-03: Markdown audit sub-skill (`seo/markdown-audit/SKILL.md`) with no MCP dependency — pure content and structure analysis

### Phase 3: Cross-MCP & Differentiating
**Goal**: Users can run commands that synthesize Ahrefs and GSC data together for insights neither source alone provides, including the flagship multi-agent site audit and automated report generation
**Depends on**: Phase 2
**Requirements**: CROSS-01, CROSS-02, CROSS-03, CROSS-04, CROSS-05
**Success Criteria** (what must be TRUE):
  1. `/seo serp <keyword>` returns live SERP composition (ranking pages, their DR, estimated traffic) from Ahrefs SERP data with graceful fallback if WebMCP is unavailable
  2. `/seo content-brief <keyword>` generates a structured brief combining SERP analysis and GSC data (if a GSC site is specified) — the output is copy-pasteable for a content writer
  3. `/seo brand-radar <brand>` returns AI search visibility data from Ahrefs Brand Radar; if the endpoint is unavailable, the command returns a clear error rather than fabricated results
  4. `/seo site-audit-pro <domain>` completes without crashing when any single agent hits a rate-limit error — the audit continues with remaining agents and notes skipped data sources in the output
  5. `/seo report <type> <domain>` produces a complete markdown report file with AI-generated narrative layered on top of the raw data — the file is saved to disk, not just printed to terminal
**Plans**: TBD

Plans:
- [ ] 03-01: SERP analysis (`seo/serp/SKILL.md`) and content brief (`seo/content-brief/SKILL.md`) with Ahrefs SERP data + optional GSC overlay; `seo-competitor-analyst` agent
- [ ] 03-02: Brand radar (`seo/brand-radar/SKILL.md`) and report generator (`seo/report/SKILL.md`) with multi-format report templates (monthly, weekly, audit, competitor)
- [ ] 03-03: Site-audit-pro (`seo/site-audit-pro/SKILL.md`) with sequential wave architecture, 3-4 agent cap per wave, checkpoint saves, and cross-MCP synthesis section

### Phase 4: Enhanced Originals & Local Analysis
**Goal**: The 12 original commands surface real MCP data alongside their static analysis, and users can analyze server logs, check AI content authenticity, audit internal link structure, validate site migrations, and audit local SEO — all without needing new MCP connections
**Depends on**: Phase 3
**Requirements**: ORIG-01, ORIG-02, ORIG-03, ORIG-04, ORIG-05, ORIG-06, ORIG-07, ORIG-08, ORIG-09, ORIG-10, ORIG-11, ORIG-12, LOCAL-02, LOCAL-03, LOCAL-04, LOCAL-05, LOCAL-06
**Success Criteria** (what must be TRUE):
  1. `/seo audit <url>` includes Ahrefs DR and backlink count alongside the static health score when Ahrefs MCP is available — the score is annotated with the data source
  2. `/seo technical <url>` includes indexing status from GSC when a matching property is available — the report notes "GSC data unavailable" when it is not
  3. `/seo log-analysis <file>` reads a local server log file and returns a crawl budget breakdown (bot vs user traffic, crawl frequency by path, top crawled URLs) with no external calls
  4. `/seo migration-check <old> <new>` validates redirect chains, canonical consistency, and metadata preservation between old and new URLs using live fetch data — the command produces a pass/fail summary per URL
  5. `/seo internal-links <domain>` identifies orphan pages (no internal links pointing to them) and suggests specific anchor text for at least the top 5 underlinked pages
**Plans**: TBD

Plans:
- [ ] 04-01: Enhanced originals — `seo-audit`, `seo-page`, `seo-technical`, `seo-content` with Ahrefs/GSC data overlays appended to existing static analysis output
- [ ] 04-02: Enhanced originals — `seo-schema`, `seo-images`, `seo-sitemap`, `seo-geo`, `seo-plan`, `seo-programmatic`, `seo-competitor-pages`, `seo-hreflang` with MCP overlays where applicable
- [ ] 04-03: Local analysis commands — `seo/log-analysis/SKILL.md`, `seo/ai-content-check/SKILL.md`, `seo/internal-links/SKILL.md`, `seo/local/SKILL.md`, `seo/migration-check/SKILL.md`

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 0/2 | Not started | - |
| 2. Core Live Data | 0/3 | Not started | - |
| 3. Cross-MCP & Differentiating | 0/3 | Not started | - |
| 4. Enhanced Originals & Local Analysis | 0/3 | Not started | - |
