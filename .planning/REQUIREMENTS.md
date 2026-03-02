# Requirements: Claude SEO Skill Expansion

**Defined:** 2026-03-02
**Core Value:** Every /seo command delivers actionable SEO insights using real data from connected MCPs — not estimates or static analysis alone.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Foundation

- [ ] **FOUND-01**: Skill system installs correctly via install script to `~/.claude/skills/` and `~/.claude/agents/`
- [ ] **FOUND-02**: Main orchestrator `seo/SKILL.md` routes all 27 commands correctly
- [ ] **FOUND-03**: Reference files load on-demand (CWV thresholds, E-E-A-T framework, quality gates, schema types)
- [ ] **FOUND-04**: Python scripts (fetch_page, parse_html, capture_screenshot, analyze_visual) work correctly
- [ ] **FOUND-05**: MCP graceful degradation — commands that require unavailable MCPs show clear error with fallback suggestions
- [ ] **FOUND-06**: Ahrefs monetary values displayed in USD (divide cents by 100) via shared reference convention

### Original Commands (Enhanced)

- [ ] **ORIG-01**: `/seo audit <url>` — Full website audit with parallel subagent delegation, health score 0-100
- [ ] **ORIG-02**: `/seo page <url>` — Deep single-page analysis (on-page, content, technical, schema, images)
- [ ] **ORIG-03**: `/seo technical <url>` — Technical SEO audit across 8 categories
- [ ] **ORIG-04**: `/seo content <url>` — E-E-A-T and content quality analysis with AI citation readiness
- [ ] **ORIG-05**: `/seo schema <url>` — Schema.org detection, validation, and JSON-LD generation
- [ ] **ORIG-06**: `/seo images <url>` — Image optimization analysis (alt text, formats, lazy loading, CLS)
- [ ] **ORIG-07**: `/seo sitemap <url or generate>` — XML sitemap analysis or generation with industry templates
- [ ] **ORIG-08**: `/seo geo <url>` — Generative Engine Optimization for AI Overviews, ChatGPT, Perplexity
- [ ] **ORIG-09**: `/seo plan <business-type>` — Strategic SEO planning with 6 industry templates
- [ ] **ORIG-10**: `/seo programmatic <url>` — Programmatic SEO analysis with thin content gates
- [ ] **ORIG-11**: `/seo competitor-pages <url or generate>` — X vs Y comparison page generation
- [ ] **ORIG-12**: `/seo hreflang <url>` — Hreflang/i18n SEO audit and generation

### GSC Commands (New)

- [ ] **GSC-01**: `/seo gsc overview <site>` — Dashboard showing clicks, impressions, CTR, average position
- [ ] **GSC-02**: `/seo gsc drops <site>` — Pages/keywords that lost traffic (28-day comparison)
- [ ] **GSC-03**: `/seo gsc opportunities <site>` — High impressions + low CTR keywords (quick wins)
- [ ] **GSC-04**: `/seo gsc cannibalization <site>` — Multiple pages ranking for same keyword detection
- [ ] **GSC-05**: `/seo gsc index-issues <site>` — Pages not indexed with reasons
- [ ] **GSC-06**: `/seo gsc compare <site>` — Period-over-period comparison
- [ ] **GSC-07**: `/seo gsc brand-vs-nonbrand <site>` — Brand traffic split analysis
- [ ] **GSC-08**: `/seo gsc content-decay <site>` — Pages losing rankings over 90 days
- [ ] **GSC-09**: `/seo gsc new-keywords <site>` — Keywords you started ranking for recently

### Ahrefs Commands (New)

- [ ] **AHRF-01**: `/seo ahrefs overview <domain>` — DR, backlinks, organic keywords, traffic estimate
- [ ] **AHRF-02**: `/seo ahrefs backlinks <domain>` — Top backlinks with DR, anchor text, dofollow status
- [ ] **AHRF-03**: `/seo ahrefs keywords <domain>` — Top organic keywords with position, volume, traffic
- [ ] **AHRF-04**: `/seo ahrefs competitors <domain>` — Organic competitors with keyword overlap
- [ ] **AHRF-05**: `/seo ahrefs content-gap <domain>` — Keywords competitors rank for that you don't
- [ ] **AHRF-06**: `/seo ahrefs broken-links <domain>` — Broken backlinks for link reclamation
- [ ] **AHRF-07**: `/seo ahrefs new-links <domain>` — Recently acquired/lost backlinks
- [ ] **AHRF-08**: `/seo ahrefs anchor-analysis <domain>` — Anchor text distribution analysis
- [ ] **AHRF-09**: `/seo ahrefs dr-history <domain>` — Domain rating trend over time
- [ ] **AHRF-10**: `/seo ahrefs top-pages <domain>` — Best performing pages by traffic

### Cross-MCP & Analysis Commands (New)

- [ ] **CROSS-01**: `/seo serp <keyword>` — Live SERP analysis using Ahrefs SERP Overview + WebMCP crawling
- [ ] **CROSS-02**: `/seo content-brief <keyword>` — AI content brief generated from SERP analysis
- [ ] **CROSS-03**: `/seo brand-radar <brand>` — AI search brand monitoring via Ahrefs Brand Radar
- [ ] **CROSS-04**: `/seo site-audit-pro <domain>` — Flagship audit combining all MCPs with sequential wave execution
- [ ] **CROSS-05**: `/seo report <type> <domain>` — Automated SEO report generation (monthly, weekly, audit, competitor)

### Local Analysis Commands (New)

- [ ] **LOCAL-01**: `/seo markdown-audit <path>` — Audit markdown files for SEO before publishing (no MCP needed)
- [ ] **LOCAL-02**: `/seo log-analysis <file>` — Server log analysis for crawl patterns
- [ ] **LOCAL-03**: `/seo ai-content-check <url or file>` — AI content detection and authenticity optimization
- [ ] **LOCAL-04**: `/seo internal-links <domain>` — Internal link structure analysis and optimization
- [ ] **LOCAL-05**: `/seo local <business>` — Local SEO audit
- [ ] **LOCAL-06**: `/seo migration-check <old> <new>` — Site migration SEO validator

## v2 Requirements

Deferred to future milestone. Tracked but not in current roadmap.

### Automation & Integrations

- **AUTO-01**: n8n automation workflows (weekly dashboard, content decay alerts, competitor alerts)
- **AUTO-02**: Google Drive report storage via MCP
- **AUTO-03**: Gmail report delivery via MCP
- **AUTO-04**: Google Calendar SEO task scheduling via MCP
- **AUTO-05**: Canva branded report visuals via MCP
- **AUTO-06**: Zoho Cliq notifications
- **AUTO-07**: Google Trends integration via GT-MCP
- **AUTO-08**: Reddit monitoring via Reddit-MCP

### Enhanced Output

- **OUT-01**: PDF report generation
- **OUT-02**: PPTX presentation generation
- **OUT-03**: Google Doc output format

### Advanced Features

- **ADV-01**: `/seo ads-intel <domain>` — Google Ads Transparency competitor ad intelligence
- **ADV-02**: `/seo competitor-monitor <domain>` — Ongoing automated competitor tracking
- **ADV-03**: `/seo gsc rich-results <site>` — Rich result performance analysis

## Out of Scope

| Feature | Reason |
|---------|--------|
| Real-time rank tracking dashboard | No session persistence in Claude Code skills |
| Automated content writing | SEO analysis tool, not content generation |
| Link building outreach automation | Requires email sending beyond analysis scope |
| White-label reporting | v1 targets personal/community use, not agency resale |
| Database/storage layer | Skills are stateless; reports are file-based |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| FOUND-01 | Phase 1 | Pending |
| FOUND-02 | Phase 1 | Pending |
| FOUND-03 | Phase 1 | Pending |
| FOUND-04 | Phase 1 | Pending |
| FOUND-05 | Phase 1 | Pending |
| FOUND-06 | Phase 1 | Pending |
| GSC-01 | Phase 2 | Pending |
| GSC-02 | Phase 2 | Pending |
| GSC-03 | Phase 2 | Pending |
| GSC-04 | Phase 2 | Pending |
| GSC-05 | Phase 2 | Pending |
| GSC-06 | Phase 2 | Pending |
| GSC-07 | Phase 2 | Pending |
| GSC-08 | Phase 2 | Pending |
| GSC-09 | Phase 2 | Pending |
| AHRF-01 | Phase 2 | Pending |
| AHRF-02 | Phase 2 | Pending |
| AHRF-03 | Phase 2 | Pending |
| AHRF-04 | Phase 2 | Pending |
| AHRF-05 | Phase 2 | Pending |
| AHRF-06 | Phase 2 | Pending |
| AHRF-07 | Phase 2 | Pending |
| AHRF-08 | Phase 2 | Pending |
| AHRF-09 | Phase 2 | Pending |
| AHRF-10 | Phase 2 | Pending |
| LOCAL-01 | Phase 2 | Pending |
| CROSS-01 | Phase 3 | Pending |
| CROSS-02 | Phase 3 | Pending |
| CROSS-03 | Phase 3 | Pending |
| CROSS-04 | Phase 3 | Pending |
| CROSS-05 | Phase 3 | Pending |
| ORIG-01 | Phase 4 | Pending |
| ORIG-02 | Phase 4 | Pending |
| ORIG-03 | Phase 4 | Pending |
| ORIG-04 | Phase 4 | Pending |
| ORIG-05 | Phase 4 | Pending |
| ORIG-06 | Phase 4 | Pending |
| ORIG-07 | Phase 4 | Pending |
| ORIG-08 | Phase 4 | Pending |
| ORIG-09 | Phase 4 | Pending |
| ORIG-10 | Phase 4 | Pending |
| ORIG-11 | Phase 4 | Pending |
| ORIG-12 | Phase 4 | Pending |
| LOCAL-02 | Phase 4 | Pending |
| LOCAL-03 | Phase 4 | Pending |
| LOCAL-04 | Phase 4 | Pending |
| LOCAL-05 | Phase 4 | Pending |
| LOCAL-06 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 48 total
- Mapped to phases: 48
- Unmapped: 0

---
*Requirements defined: 2026-03-02*
*Last updated: 2026-03-02 — traceability updated to match 4-phase roadmap*
