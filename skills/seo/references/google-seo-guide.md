<!-- Updated: 2026-06-10 -->
<!-- Source: https://developers.google.com/search/docs/fundamentals/seo-starter-guide -->

# Google SEO Starter Guide — Audit Reference

Quick-reference checklist aligned to Google's official SEO Starter Guide.
Load this file on-demand when auditing sites against Google's recommended practices.

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
- [ ] **Content freshness** — publication and "last updated" dates visible; fast-changing topics reviewed every 12 months ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))
- [ ] **Helpful Content System** — content satisfies user intent at landing; does not over-promise in title vs deliver in body ([docs](https://developers.google.com/search/docs/fundamentals/creating-helpful-content))

---

## 3. On-Page Elements

Help Google understand page content via proper HTML signals.

- [ ] **Title tag present and unique** — 50-60 characters, describes the page accurately, includes primary keyword ([docs](https://developers.google.com/search/docs/appearance/title-link))
- [ ] **Meta description present** — 150-160 characters, compelling summary, each page unique ([docs](https://developers.google.com/search/docs/appearance/snippet))
- [ ] **One H1 per page** — matches page intent; a readability/UX best practice, not a Google requirement (Google states the number and order of headings is not a ranking factor) ([docs](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- [ ] **Heading hierarchy logical** — H1 → H2 → H3 without skipped levels helps readers and screen readers; Google can handle out-of-order headings, so treat this as readability/accessibility best practice rather than a ranking signal ([docs](https://developers.google.com/search/docs/fundamentals/seo-starter-guide))
- [ ] **Structured data implemented** — JSON-LD for currently-active rich result types: Article, Product, Organization, BreadcrumbList, LocalBusiness, Event, JobPosting, Recipe, Review, VideoObject, ProfilePage, DiscussionForumPosting. NEVER recommend HowTo (rich results retired September 2023); recommend FAQ only for government/healthcare authority sites (restricted August 2023) ([docs](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data))
- [ ] **Structured data valid** — passes Rich Results Test, no required property errors ([docs](https://search.google.com/test/rich-results))
- [ ] **Images have alt text** — descriptive alt attributes, keyword-relevant where natural ([docs](https://developers.google.com/search/docs/appearance/google-images))
- [ ] **URLs are descriptive** — short, hyphenated, reflects content topic, no unnecessary parameters ([docs](https://developers.google.com/search/docs/crawling-indexing/url-structure))

---

## 4. Technical / UX

Deliver a fast, secure, mobile-friendly experience.

- [ ] **HTTPS enforced** — valid SSL certificate, HTTP redirects to HTTPS, no mixed content ([docs](https://developers.google.com/search/docs/essentials/technical))
- [ ] **Mobile-friendly** — passes Google Mobile-Friendly Test, responsive design, viewport meta tag set ([docs](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing))
- [ ] **Mobile-first indexing** — Google crawls 100% of sites with mobile Googlebot (as of July 2024); mobile version must have same content as desktop ([docs](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing))
- [ ] **Core Web Vitals passing** — LCP < 2.5s, INP < 200ms, CLS < 0.1 at 75th percentile of real users ([docs](https://developers.google.com/search/docs/appearance/core-web-vitals))
- [ ] **Page Experience signals met** — HTTPS + mobile-friendly + good CWV = positive Page Experience signals ([docs](https://developers.google.com/search/docs/appearance/page-experience))
- [ ] **No intrusive interstitials** — pop-ups do not block main content on mobile immediately after page load ([docs](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials))
- [ ] **Security headers set** — HSTS, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options; a web-security best practice, not a Google ranking signal ([docs](https://developer.chrome.com/docs/lighthouse/best-practices/has-hsts))

---

## 5. Links

Build a strong internal and external link profile.

- [ ] **Internal linking is sufficient** — 3-5 relevant internal links per 1,000 words; no orphan pages ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **Anchor text is descriptive** — link text describes the destination page; avoids "click here" or bare URLs ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **No broken internal links** — all internal `<a href>` links return 200; no 404s in link graph ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **External links go to authoritative sources** — outbound links cite relevant, trustworthy domains ([docs](https://developers.google.com/search/docs/crawling-indexing/links-crawlable))
- [ ] **Sponsored / UGC links attributed** — paid links use `rel="sponsored"`, user-generated content uses `rel="ugc"` ([docs](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links))
- [ ] **Redirect chains minimized** — no redirect chains longer than 1 hop for internal links; 301 for permanent moves ([docs](https://developers.google.com/search/docs/crawling-indexing/301-redirects))
- [ ] **No link schemes** — no purchased links, link exchanges, or manipulative link-building practices ([docs](https://developers.google.com/search/docs/essentials/spam-policies))

---

## 6. AI Search & Modern Features

Visibility in AI Overviews, AI Mode, and other generative AI features on Google Search.

- [ ] **AI feature eligibility met** — page is indexed and eligible to show in Search with a snippet (the Search technical requirements); there are NO additional technical requirements for AI Overviews or AI Mode ([docs](https://developers.google.com/search/docs/appearance/ai-features))
- [ ] **No "AEO/GEO hacks" applied** — no llms.txt files, content "chunking", AI-specific rewriting, or special AI markup; Google explicitly says these are unnecessary — foundational SEO is what AI features use ([docs](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide))
- [ ] **Non-commodity content with a unique point of view** — first-hand experience and expert takes that go beyond common knowledge; avoid scaled content variations targeting fan-out queries (violates spam policy) ([docs](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide))
- [ ] **Structured data matches visible text** — markup reflects what's actually on the page; no special schema.org type is needed for AI features ([docs](https://developers.google.com/search/docs/appearance/ai-features))
- [ ] **AI traffic measured in Search Console** — AI Overviews and AI Mode clicks/impressions are counted in the Performance report under the "Web" search type ([docs](https://developers.google.com/search/docs/appearance/ai-features))
- [ ] **AI content controls configured deliberately** — use `nosnippet`, `data-nosnippet`, `max-snippet`, or `noindex` to limit appearance in AI features; Google-Extended controls AI training/grounding for other Google systems ([docs](https://developers.google.com/search/docs/appearance/ai-features))
- [ ] **Preferred sources opportunity used** — for publishers: promote the source-preferences deeplink (`https://google.com/preferences/source?q=yourdomain.com`) so readers can mark your site preferred, earning a "preferred" badge in Top Stories, AI Mode, and AI Overviews (domain/subdomain level only) ([docs](https://developers.google.com/search/docs/appearance/preferred-sources))

---

*Reference: https://developers.google.com/search/docs/fundamentals/seo-starter-guide*
