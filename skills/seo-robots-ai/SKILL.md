---
name: seo-robots-ai
description: >
  Audit robots.txt for AI crawler access policies. Checks GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, and other AI crawlers. Use when user says
  "robots AI", "AI crawlers", "block AI", "allow AI bots", "AI crawl policy".
allowed-tools:
  - Read
  - Bash
  - WebFetch
---

# AI Crawler Robots.txt Audit

Analyzes a site's robots.txt specifically for AI crawler access policies.
Complements `/seo technical` (which does a broad robots.txt check) with
deep AI-specific analysis.

## AI Crawler Registry

| Bot Name | Owner | Purpose |
|---|---|---|
| GPTBot | OpenAI | Training data + ChatGPT web search |
| OAI-SearchBot | OpenAI | ChatGPT search only (not training) |
| ChatGPT-User | OpenAI | ChatGPT browsing (real-time) |
| ClaudeBot | Anthropic | Training data collection |
| anthropic-ai | Anthropic | Anthropic web crawler |
| PerplexityBot | Perplexity | AI search engine |
| Google-Extended | Google | Gemini / AI training (not Search) |
| Bytespider | ByteDance | TikTok / AI training |
| CCBot | Common Crawl | Open dataset used by many AI models |
| Applebot-Extended | Apple | Apple Intelligence training |
| cohere-ai | Cohere | AI model training |
| FacebookBot | Meta | Meta AI training |
| Meta-ExternalAgent | Meta | Meta AI browsing agent |
| Amazonbot | Amazon | Alexa / AI training |
| Diffbot | Diffbot | AI knowledge graph |
| ImagesiftBot | ImagesiftBot | AI image training |
| Omgili | Webz.io | AI data feeds |

## Inputs

- `url`: The website URL to audit (will fetch `/robots.txt` from site root)
  - Normalize to domain root: `example.com/page` → `https://example.com/robots.txt`

## Execution

1. **Fetch robots.txt**: WebFetch `<domain>/robots.txt`
   - If 404 → report "No robots.txt found — all crawlers allowed by default"
   - If 200 → proceed to parse

2. **Parse User-agent blocks**: Extract all `User-agent` directives and their
   associated `Allow` / `Disallow` rules.

3. **Check each AI crawler**: For each bot in the registry, determine access:
   - **Allowed** — No specific block, or explicit `Allow: /`
   - **Blocked** — `Disallow: /` for this User-agent
   - **Partial** — Some paths blocked, others allowed (list specifics)
   - **Inherited** — Falls under `User-agent: *` rules (note this)

4. **Check wildcard rules**: If `User-agent: *` has `Disallow: /`, note that
   ALL bots (including AI) are blocked unless explicitly allowed.

5. **Check for ai.txt**: WebFetch `<domain>/ai.txt` — an emerging standard
   for AI-specific crawler policies. Report if found and summarize contents.

6. **Check for llms.txt**: WebFetch `<domain>/llms.txt` — report if found
   (cross-reference with `/seo llms-txt` for full audit).

7. **Analyze crawl-delay**: Note any `Crawl-delay` directives that affect
   AI bots specifically or via wildcard.

8. **Check sitemap declaration**: Note if `Sitemap:` directive is present
   (helps AI crawlers discover content).

## Output Format

```
## AI Crawler Audit: [domain]

### Crawler Access Matrix

| Crawler | Owner | Status | Rule Source | Details |
|---|---|---|---|---|
| GPTBot | OpenAI | Allowed/Blocked/Partial | Line [#] | [specific rules] |
| ClaudeBot | Anthropic | Allowed/Blocked/Partial | Line [#] | [specific rules] |
| PerplexityBot | Perplexity | Allowed/Blocked/Partial | Line [#] | [specific rules] |
| Google-Extended | Google | Allowed/Blocked/Partial | Line [#] | [specific rules] |
| ... | ... | ... | ... | ... |

### AI Openness Score: X/10

Scoring:
- 10/10 = All AI crawlers allowed, ai.txt present, llms.txt present
- 7-9 = Most crawlers allowed, some minor gaps
- 4-6 = Mixed policy — some allowed, some blocked
- 1-3 = Most AI crawlers blocked
- 0/10 = All AI crawlers blocked (or blanket Disallow: /)

### Key Findings

- **AI crawlers explicitly blocked**: [count] of [total]
- **AI crawlers explicitly allowed**: [count]
- **Falling under wildcard rules**: [count]
- **ai.txt present**: Yes/No
- **llms.txt present**: Yes/No
- **Sitemap declared**: Yes/No

### Recommendations

Based on the site's apparent goals:

**If goal is maximum AI visibility:**
- [Specific recommendations to allow AI crawlers]
- [Suggest llms.txt creation if missing]

**If goal is AI protection:**
- [Note any crawlers not yet blocked]
- [Suggest ai.txt adoption]

**If goal is selective access:**
- [Recommend allowing search-focused bots: OAI-SearchBot, PerplexityBot]
- [Block training-only bots: CCBot, Bytespider]
- [Distinguish training vs search crawlers]

### Industry Context

Note how the site's policy compares to common patterns:
- Most major publishers block training bots but allow search bots
- Most SaaS companies allow all AI crawlers for visibility
- E-commerce sites typically allow all crawlers
- Media/news sites increasingly block training-only bots

### robots.txt Snippets

If the user wants to implement changes, provide ready-to-paste robots.txt
blocks for their chosen strategy:

**Allow all AI crawlers:**
```
# AI Crawlers — Allowed
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

**Block training, allow search:**
```
# AI Search — Allowed
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# AI Training — Blocked
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /
```
```
