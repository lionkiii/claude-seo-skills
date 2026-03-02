# Requirements: Claude SEO Skill Expansion

**Defined:** 2026-03-02
**Core Value:** Every /seo command delivers actionable SEO insights using real data from connected MCPs — not estimates or static analysis alone.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Foundation

- [x] **FOUND-01**: Skill system installs correctly via install script to `~/.claude/skills/` and `~/.claude/agents/`
- [x] **FOUND-02**: Main orchestrator `seo/SKILL.md` routes all 27 commands correctly
- [x] **FOUND-03**: Reference files load on-demand (CWV thresholds, E-E-A-T framework, quality gates, schema types)
- [x] **FOUND-04**: Python scripts (fetch_page, parse_html, capture_screenshot, analyze_visual) work correctly
- [x] **FOUND-05**: MCP graceful degradation — commands that require unavailable MCPs show clear error with fallback suggestions
- [x] **FOUND-06**: Ahrefs monetary values displayed in USD (divide cents by 100) via shared reference convention

### Original Commands (Enhanced)

- [x] **ORIG-01**: `/seo audit <url>` — Full website audit with parallel subagent delegation, health score 0-100
- [x] **ORIG-02**: `/seo page <url>` — Deep single-page analysis (on-page, content, technical, schema, images)
- [x] **ORIG-03**: `/seo technical <url>` — Technical SEO audit across 8 categories
- [x] **ORIG-04**: `/seo content <url>` — E-E-A-T and content quality analysis with AI citation readiness
- [x] **ORIG-05**: `/seo schema <url>` — Schema.org detection, validation, and JSON-LD generation
- [x] **ORIG-06**: `/seo images <url>` — Image optimization analysis (alt text, formats, lazy loading, CLS)
- [x] **ORIG-07**: `/seo sitemap <url or generate>` — XML sitemap analysis or generation with industry templates
- [x] **ORIG-08**: `/seo geo <url>` — Generative Engine Optimization for AI Overviews, ChatGPT, Perplexity
- [x] **ORIG-09**: `/seo plan <business-type>` — Strategic SEO planning with 6 industry templates
- [x] **ORIG-10**: `/seo programmatic <url>` — Programmatic SEO analysis with thin content gates
- [x] **ORIG-11**: `/seo competitor-pages <url or generate>` — X vs Y comparison page generation
- [x] **ORIG-12**: `/seo hreflang <url>` — Hreflang/i18n SEO audit and generation

### GSC Commands (New)

- [x] **GSC-01**: `/seo gsc overview <site>` — Dashboard showing clicks, impressions, CTR, average position
- [x] **GSC-02**: `/seo gsc drops <site>` — Pages/keywords that lost traffic (28-day comparison)
- [x] **GSC-03**: `/seo gsc opportunities <site>` — High impressions + low CTR keywords (quick wins)
- [x] **GSC-04**: `/seo gsc cannibalization <site>` — Multiple pages ranking for same keyword detection
- [x] **GSC-05**: `/seo gsc index-issues <site>` — Pages not indexed with reasons
- [x] **GSC-06**: `/seo gsc compare <site>` — Period-over-period comparison
- [x] **GSC-07**: `/seo gsc brand-vs-nonbrand <site>` — Brand traffic split analysis
- [x] **GSC-08**: `/seo gsc content-decay <site>` — Pages losing rankings over 90 days
- [x] **GSC-09**: `/seo gsc new-keywords <site>` — Keywords you started ranking for recently

### Ahrefs Commands (New)

- [x] **AHRF-01**: `/seo ahrefs overview <domain>` — DR, backlinks, organic keywords, traffic estimate
- [x] **AHRF-02**: `/seo ahrefs backlinks <domain>` — Top backlinks with DR, anchor text, dofollow status
- [x] **AHRF-03**: `/seo ahrefs keywords <domain>` — Top organic keywords with position, volume, traffic
- [x] **AHRF-04**: `/seo ahrefs competitors <domain>` — Organic competitors with keyword overlap
- [x] **AHRF-05**: `/seo ahrefs content-gap <domain>` — Keywords competitors rank for that you don't
- [x] **AHRF-06**: `/seo ahrefs broken-links <domain>` — Broken backlinks for link reclamation
- [x] **AHRF-07**: `/seo ahrefs new-links <domain>` — Recently acquired/lost backlinks
- [x] **AHRF-08**: `/seo ahrefs anchor-analysis <domain>` — Anchor text distribution analysis
- [x] **AHRF-09**: `/seo ahrefs dr-history <domain>` — Domain rating trend over time
- [x] **AHRF-10**: `/seo ahrefs top-pages <domain>` — Best performing pages by traffic

### Cross-MCP & Analysis Commands (New)

- [x] **CROSS-01**: `/seo serp <keyword>` — Live SERP analysis using Ahrefs SERP Overview + WebMCP crawling
- [x] **CROSS-02**: `/seo content-brief <keyword>` — AI content brief generated from SERP analysis
- [x] **CROSS-03**: `/seo brand-radar <brand>` — AI search brand monitoring via Ahrefs Brand Radar
- [x] **CROSS-04**: `/seo site-audit-pro <domain>` — Flagship audit combining all MCPs with sequential wave execution
- [x] **CROSS-05**: `/seo report <type> <domain>` — Automated SEO report generation (monthly, weekly, audit, competitor)

### Local Analysis Commands (New)

- [x] **LOCAL-01**: `/seo markdown-audit <path>` — Audit markdown files for SEO before publishing (no MCP needed)
- [x] **LOCAL-02**: `/seo log-analysis <file>` — Server log analysis for crawl patterns
- [x] **LOCAL-03**: `/seo ai-content-check <url or file>` — AI content detection and authenticity optimization
- [x] **LOCAL-04**: `/seo internal-links <domain>` — Internal link structure analysis and optimization
- [x] **LOCAL-05**: `/seo local <business>` — Local SEO audit
- [x] **LOCAL-06**: `/seo migration-check <old> <new>` — Site migration SEO validator

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
| FOUND-01 | Phase 1 | Complete |
| FOUND-02 | Phase 1 | Complete |
| FOUND-03 | Phase 1 | Complete |
| FOUND-04 | Phase 1 | Complete |
| FOUND-05 | Phase 1 | Complete |
| FOUND-06 | Phase 1 | Complete |
| GSC-01 | Phase 2 | Complete |
| GSC-02 | Phase 2 | Complete |
| GSC-03 | Phase 2 | Complete |
| GSC-04 | Phase 2 | Complete |
| GSC-05 | Phase 2 | Complete |
| GSC-06 | Phase 2 | Complete |
| GSC-07 | Phase 2 | Complete |
| GSC-08 | Phase 2 | Complete |
| GSC-09 | Phase 2 | Complete |
| AHRF-01 | Phase 2 | Complete |
| AHRF-02 | Phase 2 | Complete |
| AHRF-03 | Phase 2 | Complete |
| AHRF-04 | Phase 2 | Complete |
| AHRF-05 | Phase 2 | Complete |
| AHRF-06 | Phase 2 | Complete |
| AHRF-07 | Phase 2 | Complete |
| AHRF-08 | Phase 2 | Complete |
| AHRF-09 | Phase 2 | Complete |
| AHRF-10 | Phase 2 | Complete |
| LOCAL-01 | Phase 2 | Complete |
| CROSS-01 | Phase 3 | Complete |
| CROSS-02 | Phase 3 | Complete |
| CROSS-03 | Phase 3 | Complete |
| CROSS-04 | Phase 3 | Complete |
| CROSS-05 | Phase 3 | Complete |
| ORIG-01 | Phase 4 | Complete |
| ORIG-02 | Phase 4 | Complete |
| ORIG-03 | Phase 4 | Complete |
| ORIG-04 | Phase 4 | Complete |
| ORIG-05 | Phase 4 | Complete |
| ORIG-06 | Phase 4 | Complete |
| ORIG-07 | Phase 4 | Complete |
| ORIG-08 | Phase 4 | Complete |
| ORIG-09 | Phase 4 | Complete |
| ORIG-10 | Phase 4 | Complete |
| ORIG-11 | Phase 4 | Complete |
| ORIG-12 | Phase 4 | Complete |
| LOCAL-02 | Phase 4 | Complete |
| LOCAL-03 | Phase 4 | Complete |
| LOCAL-04 | Phase 4 | Complete |
| LOCAL-05 | Phase 4 | Complete |
| LOCAL-06 | Phase 4 | Complete |

**Coverage:**
- v1 requirements: 48 total
- Mapped to phases: 48
- Unmapped: 0

---
*Requirements defined: 2026-03-02*
*Last updated: 2026-03-02 — traceability updated to match 4-phase roadmap*
