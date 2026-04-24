<!-- Updated: 2026-04-24 -->
<!-- Source: https://developers.google.com/search/docs/fundamentals/seo-starter-guide -->
<!-- Last verified against live Google docs: 2026-04-24 -->
<!-- Next verification due: 2026-07-24 -->

# Google SEO Starter Guide — Audit Reference

Quick-reference checklist aligned to Google's official SEO Starter Guide.
Load this file on-demand when auditing sites against Google's recommended practices.

> **Framing reminder:** Google explicitly states **E-E-A-T is not a ranking factor** — it is a concept used by quality raters, not a measured signal. Optimise for the underlying behaviours (experience, expertise, authoritativeness, trustworthiness), not the acronym. Similarly, the **Helpful Content "system" has been merged into core ranking** (March 2024 core update); the dedicated HCU is no longer a separate system.

---

## 1. Discoverability

Ensure Google can find, crawl, and index your pages.

- [ ] **robots.txt valid** — exists at `/robots.txt`, does not block important pages or resources ([docs](https://developers.google.com/search/docs/crawling-indexing/robots/intro))
- [ ] **XML sitemap present** — lists all indexable URLs, referenced in robots.txt, submitted to GSC ([docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview))
- [ ] **Sitemap stays current** — dynamically generated or refreshed when content changes ([docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap))
- [ ] **No accidental noindex** — important pages are not blocked by `<meta name="robots" content="noindex">` or X-Robots-Tag ([docs](https://developers.google.com/search/docs/crawling-indexing/block-indexing))
- [ ] **JavaScript rendered content is accessible** — critical text, links, and meta tags are present in server-rendered HTML, not only injected by JavaScript ([docs](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics))
- [ ] **Crawl depth shallow** — important pages reachable within 3 clicks from homepage ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **Internal links are crawlable** — anchor tags use `href` with real URLs, not JavaScript-only click handlers ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))

---

## 2. Content Quality

Create helpful, reliable, people-first content.

- [ ] **Content is people-first** — written to help users, not primarily to rank; demonstrates genuine expertise ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))
- [ ] **E-E-A-T signals present** — author bio, credentials, first-hand experience markers, citations to authoritative sources ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))
- [ ] **No thin content** — pages provide substantial value; exceed word-count minimums per page type (see quality-gates.md) ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))
- [ ] **No duplicate content** — unique title, description, and body across pages; canonical tags used for near-duplicates ([docs](https://developers.google.com/search/docs/crawling-indexing/canonicalization))
- [ ] **Content freshness** — publication and "last updated" dates visible; fast-changing topics reviewed every 12 months ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — freshness guidance consolidated into Creating Helpful Content; the former `appearance/freshness` URL now 404s)
- [ ] **Helpful content (core ranking)** — content satisfies user intent at landing; does not over-promise in title vs deliver in body. The former "Helpful Content System" was merged into core ranking in March 2024; this is now one of many signals inside core ranking, not a separate system ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))

---

## 3. On-Page Elements

Help Google understand page content via proper HTML signals.

- [ ] **Title tag present and unique** — describes the page accurately, unique per page, includes primary keyword. Google states **no character limit** (titles are truncated to device width). Community heuristic: ~50–60 chars for SERP pixel width ([docs](https://developers.google.com/search/docs/appearance/title-link))
- [ ] **Meta description present** — compelling summary, unique per page. Google states **no character limit**; community heuristic: ~120–155 chars for desktop SERP snippet ([docs](https://developers.google.com/search/docs/appearance/snippet))
- [ ] **One H1 per page** — matches page intent, contains primary keyword ([docs](https://web.dev/articles/heading-order) — former Google `appearance/headings` URL now 404s; canonical heading guidance is now on web.dev)
- [ ] **Heading hierarchy logical** — H1 → H2 → H3 with no skipped levels; headings describe section content ([docs](https://web.dev/articles/heading-order))
- [ ] **Structured data implemented** — JSON-LD for eligible content types (Article, Product, Breadcrumb, Organization, Event, VideoObject). ⚠️ Do NOT recommend **HowTo** (rich results fully removed Sept 2023), **FAQPage** on commercial pages (restricted to gov/health authoritative sites since Aug 2023), or `WebSite.potentialAction SearchAction` for Sitelinks SearchBox (feature removed Nov 2024). See `schema-types.md` for the full retired list. ([docs](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data))
- [ ] **Structured data valid** — passes Rich Results Test, no required property errors ([docs](https://search.google.com/test/rich-results))
- [ ] **Images have alt text** — descriptive alt attributes, keyword-relevant where natural ([docs](https://developers.google.com/search/docs/appearance/google-images))
- [ ] **URLs are descriptive** — short, hyphenated, reflects content topic, no unnecessary parameters ([docs](https://developers.google.com/search/docs/crawling-indexing/url-structure))

---

## 4. Technical / UX

Deliver a fast, secure, mobile-friendly experience.

- [ ] **HTTPS enforced** — valid SSL certificate, HTTP redirects to HTTPS, no mixed content ([docs](https://developers.google.com/search/docs/fundamentals/get-on-google))
- [ ] **Mobile-friendly** — passes Google Mobile-Friendly Test, responsive design, viewport meta tag set ([docs](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing))
- [ ] **Mobile-first indexing** — Google crawls 100% of sites with mobile Googlebot (as of July 2024); mobile version must have same content as desktop ([docs](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing))
- [ ] **Core Web Vitals passing** — LCP < 2.5s, INP < 200ms, CLS < 0.1 at 75th percentile of real users (segmented mobile/desktop). INP replaced FID as a stable Core Web Vital in March 2024. Long Animation Frames (LoAF) is a diagnostic tool for debugging INP, not a Core Web Vital. ([docs](https://developers.google.com/search/docs/appearance/core-web-vitals))
- [ ] **Page experience cluster (inside core ranking)** — HTTPS + mobile-friendly + good CWV + no intrusive interstitials. Page Experience is **no longer a separate ranking system** — Google absorbed it into core ranking. Current framing: "core ranking systems look to reward content that provides a good page experience; there is no single signal." ([docs](https://developers.google.com/search/docs/appearance/page-experience))
- [ ] **No intrusive interstitials** — pop-ups do not block main content on mobile immediately after page load ([docs](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials))
- [ ] **Security headers set** — HSTS, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options ([docs](https://developers.google.com/search/docs/fundamentals/get-on-google))

---

## 5. Links

Build a strong internal and external link profile.

- [ ] **Internal linking is sufficient** — 3-5 relevant internal links per 1,000 words; no orphan pages ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) — former `fundamentals/links` URL now 404s; link guidance consolidated into links-crawlable)
- [ ] **Anchor text is descriptive** — link text describes the destination page; avoids "click here" or bare URLs ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **No broken internal links** — all internal `<a href>` links return 200; no 404s in link graph ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **External links go to authoritative sources** — outbound links cite relevant, trustworthy domains
- [ ] **Sponsored / UGC links attributed** — paid links use `rel="sponsored"`, user-generated content uses `rel="ugc"` ([docs](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links))
- [ ] **Redirect chains minimized** — no redirect chains longer than 1 hop for internal links; use **301 or 308** for permanent moves (Google treats them as equivalent since the 2026-04-14 doc update); 302/303/307 are temporary ([docs](https://developers.google.com/search/docs/crawling-indexing/301-redirects))
- [ ] **No link schemes** — no purchased links, link exchanges, or manipulative link-building practices ([docs](https://developers.google.com/search/docs/essentials/spam-policies))

---

## 6. Spam policy compliance (2026 updates)

- [ ] **No scaled content abuse** — spam policy (updated 2026-04-13) explicitly names generative AI: *"Using generative AI tools or other similar tools to generate many pages without adding value for users."* AI-assisted content is fine when it adds value; scaled AI content churn is spam ([docs](https://developers.google.com/search/docs/essentials/spam-policies))
- [ ] **No site reputation abuse (parasite SEO)** — hosting third-party content primarily to exploit your host domain's ranking signals is a policy violation
- [ ] **No expired domain abuse** — repurposing an expired domain's authority to host unrelated thin/spam content is a policy violation
- [ ] **No back-button hijacking (enforcement starts 2026-06-15)** — scripts that block or redirect the browser back button to unrequested pages are a "malicious practices" violation. Announced 2026-04-13, enforcement begins June 15, 2026. Sites face manual actions or demotions ([blog](https://developers.google.com/search/blog/2026/04/back-button-hijacking))
- [ ] **No misleading functionality, cloaking, hidden text/links, doorway pages, sneaky redirects, machine-generated traffic**

---

## 7. Recent algorithm signals (2026 context)

These are observational, not checklist items — use to interpret traffic changes:

- **March 2026 Core Update** (rolled out 2026-03-27 → 2026-04-08): favoured destination authorities over aggregator/intermediary pages. ~24% of top-10 URLs fell out of the top-100 for affected queries. Signals: intent match and comparative page value weighted higher.
- **February 2026 Discover Core Update** (2026-02-05): Discover rankings now favour local relevance, less clickbait, more original in-depth expertise.
- **Mobile-first indexing completed rollout** (mid-2023) — all sites now indexed by mobile Googlebot. Ensure content parity between mobile and desktop.

---

*Reference: https://developers.google.com/search/docs/fundamentals/seo-starter-guide*
