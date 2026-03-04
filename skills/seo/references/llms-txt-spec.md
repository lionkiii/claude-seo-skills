<!-- Updated: 2026-03-04 -->
<!-- Source: https://llmstxt.org/ -->
<!-- Author: Jeremy Howard / Answer.AI — Published September 3, 2024 -->
<!-- GitHub: https://github.com/AnswerDotAI/llms-txt -->

# llms.txt Specification Reference

The llms.txt standard provides LLMs with a structured Markdown overview of a website's
key content at inference time (when a user asks for help), not at crawl/index time.
It serves as a human-readable, LLM-friendly index — analogous to robots.txt for crawlers
or sitemap.xml for search engines.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| `llms.txt` | `/llms.txt` at site root | Curated index of key pages with descriptions |
| `llms-full.txt` | `/llms-full.txt` at site root | Comprehensive version with full page content |
| `llms-ctx.txt` | `/llms-ctx.txt` at site root | Context file without URLs (used by FastHTML) |
| `llms-ctx-full.txt` | `/llms-ctx-full.txt` at site root | Context file with URLs included |
| Page mirrors | `<page-url>.md` (e.g., `/docs/api.html.md`) | Clean Markdown version of individual pages |

---

## Required Format — Structure Rules

The file MUST be valid Markdown with sections in this strict order:

### 1. H1 Heading (Required)

```markdown
# Project Name
```

- Exactly one H1 heading
- Must be the first heading in the file
- Contains the project or website name

### 2. Blockquote Summary (Optional, Recommended)

```markdown
> Brief description of what this project/website is about.
```

- Appears immediately after the H1
- Provides a concise overview for LLMs with key information

### 3. Body Text (Optional)

Free-form Markdown text providing more detailed context about the project.
Appears after the blockquote, before any H2 sections.

### 4. H2 Sections (Required — at least one)

```markdown
## Section Name

- [Page Title](https://example.com/page): Brief description of this page
- [Another Page](https://example.com/other): What this page covers
```

- Each section groups related links under a descriptive heading
- Only H1 and H2 headings are used — no H3, H4, etc.

### 5. Link Format (Required)

```
- [Name](URL): Description
```

- Standard Markdown link: `[Name](URL)`
- Followed by `: ` (colon + space) and a brief description
- Description should be ~100 characters and informative
- Description is optional but strongly recommended

### 6. Optional Section (Recommended)

```markdown
## Optional

- [Less Important Page](https://example.com/extra): Supporting content
```

- The `## Optional` section contains links helpful but not essential
- LLMs with limited context windows can skip this section to save tokens

---

## Validation Rules

| # | Rule | Severity | Check |
|---|------|----------|-------|
| 1 | Has exactly one H1 | FAIL | Count `# ` lines (not `##`) — must be 1 |
| 2 | H1 is first heading | FAIL | First line starting with `#` must be H1 |
| 3 | Valid Markdown syntax | FAIL | No broken link syntax, unclosed brackets |
| 4 | Has at least one H2 section | FAIL | At least one `## ` heading present |
| 5 | Links use correct format | WARN | `- [Name](url): description` pattern |
| 6 | No empty sections | WARN | Every H2 should have at least one link |
| 7 | Blockquote present | INFO | `> ` after H1 is recommended |
| 8 | `## Optional` section exists | INFO | Recommended by spec |
| 9 | No deep heading levels | WARN | Only H1 and H2 (no H3, H4, H5, H6) |
| 10 | Descriptions present on links | WARN | Links should have `: description` after URL |

---

## Example: llmstxt.org's Own File

```markdown
# llms.txt

> "A proposal that those interested in providing LLM-friendly content add a
> /llms.txt file to their site."

This markdown file offers introductory background and direction, with references
to detailed markdown documents.

## Docs

- [llms.txt proposal](https://llmstxt.org/index.md): The core proposal
- [Python library docs](https://llmstxt.org/intro.html.md): Documentation for the llms-txt python library
- [ed demo](https://llmstxt.org/ed-commonmark.md): Example demonstrating llms.txt integration with ed
```

## Example: FastHTML (Truncated)

```markdown
# FastHTML

> FastHTML is a python library which brings together Starlette, Uvicorn,
> HTMX, and fastcore's FT "FastTags" into a library for creating server-
> rendered hypermedia applications.

## Docs

- [FastHTML quick start](https://docs.fastht.ml/path/quickstart.html.md): A brief overview showing how to get started
- [HTMX reference](https://docs.fastht.ml/path/ref/htmx.html.md): Brief description of HTMX
- [Starlette quick reference](https://docs.fastht.ml/path/ref/starlette.html.md): Brief overview of Starlette features

## Examples

- [Todo app](https://docs.fastht.ml/path/examples/todo.html.md): Annotated todo app
- [Chat app](https://docs.fastht.ml/path/examples/chat.html.md): Chat application example

## Optional

- [Adv app](https://docs.fastht.ml/path/examples/adv_app.html.md): More advanced example
- [Explanation](https://docs.fastht.ml/path/explains/explaining.html.md): Explanation of FastHTML concepts
```

---

## Tooling & Libraries

| Tool | Install | Description |
|------|---------|-------------|
| `llms-txt` (Python) | `pip install llms-txt` | Official parser + CLI for llms.txt files |
| `llms_txt2ctx` CLI | Included in `llms-txt` | Convert llms.txt to LLM-ready context: `llms_txt2ctx llms.txt > llms.md` |
| `vitepress-plugin-llms` | npm | Auto-generate llms.txt from VitePress sites |
| `docusaurus-plugin-llms` | npm | Auto-generate llms.txt from Docusaurus sites |
| `llms-txt-php` | composer | PHP library for reading/writing llms.txt |
| Drupal LLM Support | recipe | Recipe for Drupal 10.3+ sites |
| VS Code PagePilot | marketplace | Loads external llms.txt context automatically |

### Python API

```python
from llms_txt import parse_llms_file, create_ctx

# Parse an llms.txt file into structured sections
result = parse_llms_file("llms.txt")  # Returns: title, summary, info, sections

# Parse including Optional section
result = parse_llms_file("llms.txt", optional=True)

# Generate LLM-ready XML context
ctx = create_ctx(result)  # Structured XML for Claude and similar systems
```

### CLI Usage

```bash
# Convert llms.txt to context (excludes Optional by default)
llms_txt2ctx llms.txt > llms.md

# Include Optional section
llms_txt2ctx --optional True llms.txt > llms-full.md
```

---

## Relationship to Other Standards

| Standard | Purpose | Relationship |
|----------|---------|-------------|
| `robots.txt` | Controls crawler access | Different purpose — llms.txt aids inference, not crawling |
| `sitemap.xml` | Lists all indexable URLs | sitemap lists everything; llms.txt curates key pages for LLMs |
| `ai.txt` | AI training consent / resource descriptions | Emerging complementary standard |
| Schema.org | Structured metadata in HTML | llms.txt provides site-level overview, schema provides page-level detail |

---

## Adoption Statistics

- **2,000+ sites** have published llms.txt files (as of March 2026)
- **Notable adopters**: Anthropic (Claude), Cloudflare, Vercel, Stripe, Docker, Next.js,
  Angular, Vue.js, Supabase, Prisma, Expo, LangChain, Cursor, Hugging Face, Replit,
  AWS Documentation, Google Gemini Developer API, Solana, X (Twitter), Linear,
  Mintlify, Svelte, Zapier, Coinbase, ElevenLabs, DuckDB, Bun, Hono, Nuxt,
  Gradio, Drizzle ORM, Astro, Webflow, Postman, Cal.com, Clerk, Framer,
  Supabase, Meta Horizon OS, Apache Camel
- **Growing ecosystem**: VitePress, Docusaurus, Drupal plugins auto-generate llms.txt
- **No major AI company** currently requires llms.txt, but early adoption parallels
  early schema.org adoption — positioning for future AI search optimization

---

## Implementation Guidance

- Use concise, clear language in descriptions
- Include informative link descriptions (avoid generic "click here")
- Avoid unexplained jargon — LLMs benefit from context
- Test expanded llms.txt files with multiple language models
- Keep the file focused — it's an index, not the content itself
- Link to `.md` versions of pages when available for better LLM parsing

---

## Resources

- [llms.txt Specification](https://llmstxt.org/)
- [Introduction & Python Library](https://llmstxt.org/intro.html)
- [GitHub Repository](https://github.com/AnswerDotAI/llms-txt)
- [Adopter Directory](https://directory.llmstxt.cloud/)
- [llmstxt.site Directory](https://llmstxt.site/)
