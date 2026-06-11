# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-10

### Added

- **seo-lighthouse-audit** — Run Lighthouse audits (CLI or PageSpeed Insights API fallback), parse category scores and failed audits, and map each to its fix and official Chrome doc.
- **seo-core-web-vitals** — Dedicated CWV deep-dive: CrUX field data with lab fallback, LCP subparts diagnosis, INP and CLS playbooks.
- **seo-page-experience** — Google page-experience self-assessment: HTTPS, intrusive interstitials, mobile usability, CWV, ad distinguishability.
- **seo-rich-results** — Per-type rich result eligibility checker: classifies page type, validates required/recommended properties per Google's per-type docs, produces a gap report.
- **seo-ai-optimization** — Audit against Google's official AI Optimization guide (AI Overviews / AI Mode readiness): snippet controls, crawlability, citability.
- **seo-eeat-audit** — Standalone E-E-A-T scoring rubric (0-5 per dimension) with detectable trust signals and evidence-based recommendations.
- **seo-helpful-content** — Pre-publish content-quality gate implementing Google's people-first self-assessment questions plus spam-policy red flags.
- New "Performance & Page Experience" command group in the README.
- This CHANGELOG.

### Changed

- **seo-llms-txt** — Replaced stale adoption count; added note on Lighthouse's new Agentic Browsing llms.txt audit.
- **seo-robots-ai** — Split AI crawler registry into training vs user-triggered/search tables; added OAI-SearchBot, Perplexity-User, Google-CloudVertexBot, DuckAssistBot, MistralAI-User, Meta-ExternalFetcher; added "blocking training bots ≠ blocking AI search visibility" guidance.
- **seo-images** — Updated WebP/AVIF browser-support figures; added `fetchpriority="high"` and LCP image subparts guidance.
- **seo-internal-links** — Orphan = zero inbound links (hard finding); "underlinked < 3" relabeled a configurable heuristic, not a Google requirement; anchor-text guidance aligned with Google's links-crawlable doc.
- **seo-content** — E-E-A-T section reframed per Google's "Creating helpful content" doc: not a direct ranking factor, Trust is the most important member; removed unverifiable QRG date claim.
- **seo-audit** — Added `seo-ai-optimization` as a 7th audit specialist.
- **seo (orchestrator)** — Routing table extended to 52 commands; new disambiguation rules for overlapping triggers (AI Overviews → seo-ai-optimization vs seo-geo; Core Web Vitals → seo-core-web-vitals vs seo-technical; E-E-A-T → seo-eeat-audit vs seo-content).
- **references/google-seo-guide.md** — Added "AI Search & Modern Features" checklist section (7 items from Google's AI features and AI optimization docs); softened heading-hierarchy items to readability best practice per Google's "not a ranking factor" stance.
- **references/ai-crawlers-guide.md** — Added MistralAI-User to the crawler registry and search/retrieval list.
- **hooks/pre-commit-seo-check.sh** — Deprecated-schema check expanded (ClaimReview, VehicleListing, Dataset); new FAQPage eligibility warning.
- README, plugin.json, marketplace.json updated for 52 sub-skills; plugin version bumped to 1.1.0.

### Fixed

- Repaired 4 dead Google documentation URLs in `skills/seo/references/google-seo-guide.md` (`appearance/freshness`, `appearance/headings` ×2, `fundamentals/links` ×3) and replaced 2 legacy `get-on-google` links.
- Stale structured-data guidance recommending HowTo (retired Sep 2023) and unrestricted FAQ (gov/health-only since Aug 2023) in the reference guide and in `seo-plan/assets/saas.md`.
- Skill-count drift: documentation said 44 skills while 45 sub-skills existed (`seo-obsidian-kb` was undocumented) — all counts and routing lists now reflect the true total of 52.

## [1.0.0] - 2026-02-27

### Added

- Initial release: 44 documented SEO commands for Claude Code — site audits, technical SEO, schema, content/E-E-A-T analysis, Ahrefs backlink and keyword analysis, Google Search Console analytics, AI search (GEO) tools, and AI readability (llms.txt, robots-ai).
- `/seo` orchestrator skill with command routing and 6 specialist subagents for parallel audits.
- Plugin marketplace packaging, installer, smoke tests, and Claude Desktop edition.

[1.1.0]: https://github.com/lionkiii/claude-seo-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/lionkiii/claude-seo-skills/releases/tag/v1.0.0
