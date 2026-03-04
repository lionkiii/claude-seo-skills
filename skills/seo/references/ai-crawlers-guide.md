<!-- Updated: 2026-03-04 -->
<!-- Sources: https://darkvisitors.com/agents, https://platform.openai.com/docs/bots -->
<!-- See also: https://github.com/ai-robots-txt/ai.robots.txt -->

# AI Crawlers Guide — Complete Reference

Comprehensive registry of AI web crawlers, their robots.txt tokens, purposes,
and official documentation. Load this file on-demand when auditing robots.txt
for AI crawler policies via `/seo-robots-ai`.

---

## 1. Major AI Crawlers — Complete Registry

### OpenAI (3 crawlers)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| GPTBot | `GPTBot` | AI model training data | Yes |
| OAI-SearchBot | `OAI-SearchBot` | ChatGPT search results only (not training) | Yes |
| ChatGPT-User | `ChatGPT-User` | User-initiated browsing in ChatGPT | Yes |

- IP ranges: `https://openai.com/gptbot.json`, `https://openai.com/searchbot.json`, `https://openai.com/chatgpt-user.json`
- Docs: [platform.openai.com/docs/bots](https://platform.openai.com/docs/bots)

### Anthropic (3 crawlers)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| ClaudeBot | `ClaudeBot` | Model training data collection | Yes |
| Claude-User | `Claude-User` | User-initiated web access | Yes |
| Claude-SearchBot | `Claude-SearchBot` | Search result indexing | Yes |

- IP ranges: Not published (shared service-provider IPs)
- Supports non-standard `Crawl-delay` directive
- Contact: `claudebot@anthropic.com`
- Docs: [support.claude.com](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)

### Google (2 AI-specific tokens)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| Google-Extended | `Google-Extended` | Opt out of Gemini/Vertex AI training | Yes |
| Google-CloudVertexBot | `Google-CloudVertexBot` | Vertex AI grounding | Yes |

- `Google-Extended` is a robots.txt-only control — no separate HTTP user-agent string
- Blocking `Google-Extended` does NOT affect Google Search rankings
- Docs: [developers.google.com/crawling/docs](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

### Perplexity (2 crawlers)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| PerplexityBot | `PerplexityBot` | General web crawling/indexing | Partially |
| Perplexity-User | `Perplexity-User` | User-initiated browsing | Yes |

- IP ranges: `https://www.perplexity.com/perplexitybot.json`
- Note: Cloudflare documented Perplexity using stealth/undeclared crawlers
- Docs: [docs.perplexity.ai/guides/bots](https://docs.perplexity.ai/guides/bots)

### Meta (3 crawlers)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| FacebookBot | `Facebookbot` | Link previews / social sharing | Yes |
| Meta-ExternalAgent | `meta-externalagent` | AI training + real-time retrieval | Yes |
| Meta-ExternalFetcher | `meta-externalfetcher` | User-initiated Meta AI fetches | Yes |

- Docs: [developers.facebook.com/docs/sharing/webmasters/crawler](https://developers.facebook.com/docs/sharing/webmasters/crawler)

### Apple (1 AI-specific token)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| Applebot-Extended | `Applebot-Extended` | Apple Intelligence training | Yes |

- Blocking `Applebot-Extended` does NOT affect standard Applebot (Siri, Spotlight)
- Docs: [support.apple.com/en-us/111795](https://support.apple.com/en-us/111795)

### ByteDance (2 crawlers)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| Bytespider | `Bytespider` | LLM training (Doubao) | Partially |
| TikTokSpider | `TikTokSpider` | TikTok content analysis | Yes |

### Amazon (1 crawler)

| Bot | robots.txt Token | Purpose | Respects robots.txt |
|-----|-----------------|---------|---------------------|
| Amazonbot | `Amazonbot` | Alexa, search, recommendations, AI | Yes |

- Docs: [developer.amazon.com/support/amazonbot](https://developer.amazon.com/support/amazonbot)

### Other AI Crawlers

| Bot | robots.txt Token | Company | Purpose |
|-----|-----------------|---------|---------|
| CCBot | `CCBot` | Common Crawl | Open web dataset (used to train many LLMs) |
| cohere-ai | `cohere-ai` | Cohere | Real-time retrieval |
| cohere-training-data-crawler | `cohere-training-data-crawler` | Cohere | Training data |
| AI2Bot | `AI2Bot` | Allen Institute | Open-source AI research |
| AI2Bot-Dolma | `AI2Bot-Dolma` | Allen Institute | Dolma dataset |
| DeepSeekBot | `DeepSeekBot` | DeepSeek | AI training (note: may not identify in UA) |
| DuckAssistBot | `DuckAssistBot` | DuckDuckGo | AI-assisted search answers |
| Youbot | `Youbot` | You.com | AI search training |
| diffbot | `diffbot` | Diffbot | Web data extraction / knowledge graph |
| ImagesiftBot | `ImagesiftBot` | Hive | Image classification training |
| img2dataset | `img2dataset` | LAION | Image dataset collection |
| Timpibot | `Timpibot` | Timpi | Decentralized search |
| PetalBot | `PetalBot` | Huawei | Huawei search + AI |
| PanguBot | `PanguBot` | Huawei | AI model training |

---

## 2. Training vs Search/Retrieval Crawlers

Critical distinction for robots.txt strategy:

### Training Crawlers (scrape content for model training)
`GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`, `Bytespider`,
`cohere-training-data-crawler`, `Meta-ExternalAgent`, `Applebot-Extended`,
`AI2Bot`, `AI2Bot-Dolma`, `img2dataset`, `PanguBot`

### Search/Retrieval Crawlers (fetch content for real-time AI search answers)
`OAI-SearchBot`, `ChatGPT-User`, `Claude-User`, `Claude-SearchBot`,
`PerplexityBot`, `Perplexity-User`, `Meta-ExternalFetcher`,
`DuckAssistBot`, `cohere-ai`, `Youbot`

> **Best practice**: Block training crawlers to protect content, allow search
> crawlers for AI search visibility. This mirrors how most publishers operate.

---

## 3. Industry Blocking Statistics

### By Website Type (2025-2026 data)

| Category | % Blocking AI Training Bots | Source |
|----------|---------------------------|--------|
| Top news sites (USA) | 79% | Reuters Institute |
| Top news sites (global) | 48% | Reuters Institute |
| Legacy print publications | 57% | Reuters Institute |
| TV/radio broadcasters | 48% | Reuters Institute |
| Digital-born outlets | 31% | Reuters Institute |
| All websites (GPTBot) | 5.89% | Paul Calvano / Cloudflare |
| All websites (ClaudeBot) | 4.26% | Paul Calvano / Cloudflare |
| Top 1,000 websites (GPTBot) | 21% | Paul Calvano / Cloudflare |

### Trends

- Blocking grew from **23% to ~60%** of reputable sites through 2025
- Blocking has **plateaued** since early 2026 — adoption rates stable
- **560,000+ sites** reference AI bots in robots.txt globally
- AI crawlers contributed to **86% increase** in general invalid traffic (DoubleVerify)

---

## 4. robots.txt Strategy Templates

### Strategy A: Maximum AI Visibility (SaaS, Docs, Open Source)

```
# Allow all AI crawlers for maximum visibility
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

### Strategy B: Block Training, Allow Search (Publishers, Media)

```
# AI Search — Allowed (appear in AI answers)
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: DuckAssistBot
Allow: /

# AI Training — Blocked (protect content)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: cohere-training-data-crawler
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: AI2Bot
Disallow: /

User-agent: AI2Bot-Dolma
Disallow: /

User-agent: img2dataset
Disallow: /
```

### Strategy C: Block All AI Crawlers (Paid Content, Premium Media)

```
# Block all known AI crawlers
User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Claude-User
Disallow: /

User-agent: Claude-SearchBot
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: Perplexity-User
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Meta-ExternalFetcher
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: Amazonbot
Disallow: /

User-agent: cohere-ai
Disallow: /

User-agent: cohere-training-data-crawler
Disallow: /

User-agent: AI2Bot
Disallow: /

User-agent: AI2Bot-Dolma
Disallow: /

User-agent: diffbot
Disallow: /

User-agent: ImagesiftBot
Disallow: /

User-agent: img2dataset
Disallow: /

User-agent: Timpibot
Disallow: /

User-agent: PanguBot
Disallow: /
```

---

## 5. Emerging Standards

### ai.txt (Spawning AI — 2023)

- Purpose: AI training consent and data usage permissions
- Location: `/ai.txt` at site root
- Status: Spawning.ai site currently under maintenance — limited adoption
- Partners: Hugging Face, Stability AI

### ai.txt (aitxt.ing — newer variant)

- Purpose: Describe resources in plain text for AI agents
- Format: Markdown with optional YAML frontmatter (`updated`, `scope`, `parent`)
- Feature: Cascading discovery — checks `/products/widgets/ai.txt` → `/products/ai.txt` → `/ai.txt`
- Difference from robots.txt: robots.txt says what NOT to access; ai.txt says what something IS

### Community robots.txt Blocklist

- GitHub: [ai-robots-txt/ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt)
- Maintains a curated list of all known AI crawlers
- Provides `robots.json` as machine-readable source file

---

## 6. Known Limitations

- **robots.txt is advisory**, not enforceable — some crawlers may ignore it
- **DeepSeek** does not identify itself in user-agent strings
- **Perplexity** has been documented using undeclared crawlers (Cloudflare blog)
- **AI browsers** (ChatGPT Atlas, Comet) don't differentiate in UA strings
- **Rules are per-subdomain** — must be configured separately for each subdomain
- **New crawlers emerge regularly** — monitor via Dark Visitors or community lists

---

## Resources

- [Dark Visitors — AI Agent Database](https://darkvisitors.com/agents)
- [OpenAI Crawler Docs](https://platform.openai.com/docs/bots)
- [Anthropic Crawler Info](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Google AI Crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [Perplexity Bot Docs](https://docs.perplexity.ai/guides/bots)
- [Community AI robots.txt Blocklist](https://github.com/ai-robots-txt/ai.robots.txt)
- [Reuters Institute Study: News Sites Blocking AI](https://reutersinstitute.politics.ox.ac.uk/how-many-news-websites-block-ai-crawlers)
- [Paul Calvano: AI Bots and Robots.txt Stats](https://paulcalvano.com/2025-08-21-ai-bots-and-robots-txt/)
- [Cloudflare: Perplexity Stealth Crawlers](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- [robotstxt.com AI/LLM Guide](https://robotstxt.com/ai)
