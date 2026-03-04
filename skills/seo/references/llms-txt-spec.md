# llms.txt Specification Reference

Source: https://llmstxt.org/ (Jeremy Howard / Answer.AI)

## Overview

llms.txt is a proposed standard that provides LLMs with a structured Markdown
overview of a website's key content. It serves as a human-readable, LLM-friendly
index — analogous to robots.txt for crawlers or sitemap.xml for search engines.

## File Location

- Primary: `/llms.txt` at the site root (e.g., `https://example.com/llms.txt`)
- Companion: `/llms-full.txt` — comprehensive version with full page content
- Page mirrors: Individual pages can provide `.md` versions (e.g., `/docs/api.html.md`)

## Required Format

The file MUST be valid Markdown with the following structure:

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
- Provides a concise overview for LLMs

### 3. H2 Sections (Required — at least one)

```markdown
## Section Name

- [Page Title](https://example.com/page): Brief description of this page
- [Another Page](https://example.com/other): What this page covers
```

- Each section groups related links
- Links follow the format: `- [Name](URL): Description`
- The colon and space after the URL closing paren is part of the spec
- Description helps LLMs understand what content they'll find

### 4. Optional Section (Recommended)

```markdown
## Optional

- [Less Important Page](https://example.com/extra): Supporting content
```

- The `## Optional` section contains links that are helpful but not essential
- LLMs with limited context can skip this section

## Rules

- Only H1 and H2 headings are used (no H3, H4, etc.)
- The file should be concise — it's an index, not the content itself
- Links should point to actual pages that exist and return HTTP 200
- Descriptions should be brief (~100 characters) and informative

## Example (from FastHTML)

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

## Known Adopters (as of early 2026)

Anthropic, Cloudflare, Docker, Vercel, Stripe, Cursor, Hugging Face,
Mintlify, Hashnode, ReadMe, Docusaurus sites, FastHTML, Quarto,
Weights & Biases, and 950+ more sites.

## Companion Standards

- **ai.txt** — Emerging standard for AI-specific crawler policies (complements robots.txt)
- **robots.txt** — Controls crawler access (AI crawlers: GPTBot, ClaudeBot, etc.)
- **sitemap.xml** — URL discovery for crawlers (traditional and AI)
