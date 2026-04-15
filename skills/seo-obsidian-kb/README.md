# seo-obsidian-kb

Build an Obsidian knowledge base from any website's sitemap. Uses Python for fast bulk-fetching and parallel Claude agents for quality content analysis and Obsidian-optimized MD generation.

## What it does

1. **Python fetcher** (`fetch_pages.py`) — async crawls sitemap, extracts title/H1/headings/links/schema from every page, builds link adjacency map
2. **Parallel Claude agents** — classify each page (type, intent, funnel stage), write contextual descriptions, generate Obsidian notes with YAML frontmatter + wikilinks
3. **Auto-generates** category indexes, product MOC (Map of Content), and master SEO Command Center

## Installation

Copy into your Claude skills directory:

```bash
cp -r skills/seo-obsidian-kb ~/.claude/skills/
```

Ensure Python dependencies are available:

```bash
pip install aiohttp beautifulsoup4 lxml
```

## Usage

```
/seo obsidian-kb --sitemap https://www.example.com/sitemap.xml --product "Product Name"
```

### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--sitemap` | Yes | - | Sitemap URL |
| `--product` | Yes | - | Product name (becomes folder name) |
| `--vault` | No | `~/Documents/Obsidian Vault` | Obsidian vault path |
| `--base-path` | No | Auto-detected | URL base path prefix |

## Output structure

```
Obsidian Vault/
  _HQ/
    _SEO Command Center.md    # Master entry point
  {product}/
    _{Product}.md              # Product MOC
    {category}/
      _{category}.md           # Category index
      {page-slug}.md           # Individual page notes
```

## Each page note includes

- **YAML frontmatter**: product, category, slug, url, page_type, intent, funnel_stage, target_audience, title, h1, word_count, schema_types, tags
- **About This Page**: Claude-written contextual description
- **Page Sections**: H2/H3 heading outline
- **Key Takeaways for LLM Context**: Bullet points of most important facts
- **Internal Links**: Outbound + inbound wikilinks from adjacency map

## Reuse for any website

Run the same command with a different sitemap:

```bash
/seo obsidian-kb --sitemap https://www.zoho.com/crm/sitemap.xml --product "Zoho CRM"
/seo obsidian-kb --sitemap https://www.zoho.com/desk/sitemap.xml --product "Zoho Desk"
/seo obsidian-kb --sitemap https://example.com/sitemap.xml --product "Example"
```

Each product gets its own folder. Obsidian graph view auto-clusters by product.

## Design principles

- **No SEO metrics stored** — Claude fetches live data from Ahrefs/GSC MCPs when needed
- **Vault is additive** — new products never overwrite existing ones
- **Karpathy method** — atomic notes + heavy interlinking = emergent structure via graph
- **Python for speed, Claude for quality** — bulk I/O in Python, content analysis in parallel agents
