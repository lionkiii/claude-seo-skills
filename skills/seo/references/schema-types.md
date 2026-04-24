<!-- Updated: 2026-04-24 -->
# Schema.org Types — Status & Recommendations (April 2026)

**Schema.org Version:** 29.4 (December 8, 2025)

**Last verified against live Google docs:** 2026-04-24
**Next verification due:** 2026-07-24

## Format Preference
Always use **JSON-LD** (`<script type="application/ld+json">`).
Google's documentation explicitly recommends JSON-LD over Microdata and RDFa.

**AI Search Note:** Content with proper schema has ~2.5× higher chance of appearing in AI-generated answers (confirmed by Google and Microsoft, March 2025).

---

## Active — Recommend freely

| Type | Use Case | Key Properties |
|------|----------|----------------|
| Organization | Company info | name, url, logo, contactPoint, sameAs; merchant-panel eligibility (2026-04-15 update): hasMerchantReturnPolicy, hasMemberProgram, hasShippingService; identifiers: duns, globalLocationNumber, iso6523Code, leiCode, naics, taxID, vatID |
| LocalBusiness | Physical businesses | name, address, telephone, openingHours, geo, priceRange |
| SoftwareApplication | Desktop/mobile apps | name, operatingSystem, applicationCategory, offers, aggregateRating |
| WebApplication | Browser-based SaaS | name, applicationCategory, offers, browserRequirements, featureList |
| Product | Physical/digital products | name, image, description, sku, brand, offers, review |
| Offer | Pricing | price, priceCurrency, availability, url, validFrom |
| Service | Service businesses | name, provider, areaServed, description, offers |
| Article | Blog posts, news | headline, author, datePublished, dateModified, image, publisher |
| BlogPosting | Blog content | Same as Article + blog-specific context |
| NewsArticle | News content | Same as Article + news-specific context |
| Review | Individual reviews | reviewRating, author, itemReviewed, reviewBody — **self-serving reviews are NOT eligible for rich results**: reviews authored by the merchant about their own Product/Service/Organization/LocalBusiness do not qualify (policy since 2019, still enforced) |
| AggregateRating | Rating summaries | ratingValue, reviewCount, bestRating, worstRating — **self-serving restriction applies**: use only ratings aggregated from third-party/customer reviews, not merchant self-ratings |
| BreadcrumbList | Navigation | itemListElement with position, name, item |
| WebSite | Site-level | name, url — ⚠️ `potentialAction`/`SearchAction` no longer triggers the Sitelinks Search Box (feature removed from Google Search on 21 November 2024; dedicated doc page 404s). WebSite schema remains useful for entity understanding but do NOT present `SearchAction` as a rich-result win. |
| WebPage | Page-level | name, description, datePublished, dateModified |
| Person | Author/team | name, jobTitle, url, sameAs, image, worksFor |
| ContactPage | Contact pages | name, url |
| VideoObject | Video content | name, description, thumbnailUrl, uploadDate, duration, contentUrl |
| ImageObject | Image content | contentUrl, caption, creator, copyrightHolder |
| Event | Events | name, startDate, endDate, location, organizer, offers |
| JobPosting | Job listings | title, description, datePosted, hiringOrganization, jobLocation |
| Course | Educational content | name, description, provider, hasCourseInstance |
| DiscussionForumPosting | Forum threads | headline, author, datePublished, text, url |
| ProductGroup | Variant products | name, productGroupID, variesBy, hasVariant |
| ProfilePage | Author/creator profiles | mainEntity (Person), name, url, description, sameAs |

---

## Restricted — Only for specific site types

| Type | Restriction | Since |
|------|------------|-------|
| FAQPage | Government and healthcare authority sites ONLY | August 2023 |

> Google severely limited FAQ rich results. Only authoritative sources (government, health organizations) now receive FAQ rich results. Do NOT recommend FAQPage schema for commercial sites.

---

## Deprecated / retired — Never recommend

| Type | Status | Since | Notes |
|------|--------|-------|-------|
| HowTo | Rich results fully removed | September 2023 | Google stopped showing how-to rich results |
| **Sitelinks Search Box feature** | Feature removed from Google Search | **November 2024** | `WebSite.potentialAction`/`SearchAction` schema still parses but triggers no Search feature. Docs page 404s. |
| SpecialAnnouncement | Retired from rich results | September 2025 → Search Console removal January 2026 | COVID-era schema, no longer processed |
| CourseInfo | Retired from rich results | September 2025 → Search Console removal January 2026 | Merged into Course |
| EstimatedSalary | Retired from rich results | September 2025 → Search Console removal January 2026 | No longer displayed |
| LearningVideo | Retired from rich results | September 2025 → Search Console removal January 2026 | Use VideoObject instead |
| ClaimReview | Retired from rich results | September 2025 → Search Console removal January 2026 | Fact-check markup no longer generates rich results |
| VehicleListing | Retired from rich results | September 2025 → Search Console removal January 2026 | Vehicle listing structured data discontinued |
| **Practice Problem** | **Documentation removed and feature discontinued** | **January 2026** | Docs removed from developers.google.com on 2026-01-06 |
| Book Actions | Deprecated then REVERSED | June 2025 | **Still functional as of April 2026** — historical note only |
| Dataset | Retired from rich results | Late 2025 | Dataset Search feature discontinued |

---

## Recent Additions (2024-2026)

| Type/Feature | Added | Notes |
|-------------|-------|-------|
| Product Certification markup | April 2025 | Energy ratings, safety certifications. Replaced EnergyConsumptionDetails. |
| ProductGroup | 2025 | E-commerce product variants with variesBy, hasVariant properties |
| ProfilePage | 2025 | Author/creator profile pages with mainEntity Person for E-E-A-T |
| DiscussionForumPosting | 2024 | For forum/community content |
| Speakable | Updated 2024 | For voice search optimization |
| LoyaltyProgram | June 2025 | Member pricing, loyalty card structured data |
| Organization-level shipping/return policies | November 2025 | Configure via Search Console without Merchant Center |
| ConferenceEvent | December 2025 | Schema.org v29.4 addition |
| PerformingArtsEvent | December 2025 | Schema.org v29.4 addition |
| **Organization merchant-panel fields** | **April 15, 2026** | `hasMerchantReturnPolicy`, `hasMemberProgram`, `hasShippingService` newly recommended for merchant knowledge-panel eligibility |
| **Discussion Forum + QAPage comment-thread property expansion** | **March 24, 2026** | Expanded properties for forum/community content and Q&A pages |
| **Preferred Sources concept** | **January 2026** | New Top Stories / authoritative publisher selection concept — shapes E-E-A-T audits, not a schema type |
| **Image preferred-thumbnail metadata** | **March 2, 2026** | New guidance for specifying preferred thumbnails (see Google Images doc, relevant to seo-images skill) |

## E-commerce Requirements (Updated)

| Requirement | Status | Since |
|-------------|--------|-------|
| `returnPolicyCountry` in MerchantReturnPolicy | **Required** | March 2025 |
| Product variant structured data | Expanded | 2025 — includes apparel, cosmetics, electronics |

> **Note:** Content API for Shopping sunsets August 18, 2026. Migrate to Merchant API.

---

## Validation Checklist

For any schema block, verify:

1. ✅ `@context` is `"https://schema.org"` (not http)
2. ✅ `@type` is a valid, non-deprecated type
3. ✅ All required properties are present
4. ✅ Property values match expected data types
5. ✅ No placeholder text (e.g., "[Business Name]")
6. ✅ URLs are absolute, not relative
7. ✅ Dates are in ISO 8601 format
8. ✅ Images have valid URLs

## Testing Tools

- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
