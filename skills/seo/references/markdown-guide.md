<!-- Updated: 2026-03-02 -->
<!-- Source: https://www.markdownguide.org/basic-syntax/ -->

# Markdown Guide — Syntax Rules Reference

Compact checklist of Markdown syntax rules for the `/seo markdown-audit` command.
Each rule includes a correct and incorrect example.

---

## Rule 1: Space After Heading Hash Marks

**Correct:** `# Heading One` / `## Heading Two`
**Incorrect:** `#Heading One` / `##Heading Two`

> Most parsers require a space between `#` and the heading text. Missing the space may render the `#` as literal text.

---

## Rule 2: Consistent List Delimiters

**Correct:** Use all `-` or all `*` within a single list.
```
- Item one
- Item two
- Item three
```

**Incorrect:** Mixing delimiters in the same list.
```
- Item one
* Item two
- Item three
```

> Mixed delimiters can create two separate lists depending on the renderer.

---

## Rule 3: Proper Emphasis Syntax

**Correct:**
- Italic: `*italic*` or `_italic_` (pick one, be consistent)
- Bold: `**bold**` or `__bold__` (pick one, be consistent)
- Bold-italic: `***bold-italic***`

**Incorrect:** Mixing `*` and `_` within the same emphasis span.
```
*_mixed emphasis_*   ← inconsistent, may not render
```

> Recommendation: use `*` for italic and `**` for bold throughout a document.

---

## Rule 4: Blank Lines Before and After Block Elements

**Correct:**
```
Paragraph text here.

## Heading

- List item one
- List item two

Another paragraph.
```

**Incorrect:**
```
Paragraph text here.
## Heading
- List item one
Another paragraph.
```

> Block elements (headings, lists, code blocks, blockquotes) require a blank line before and after them for reliable rendering across parsers.

---

## Rule 5: URL Encoding for Special Characters in Links

**Correct:** `[Page Title](https://example.com/my%20page%20with%20spaces)`
**Incorrect:** `[Page Title](https://example.com/my page with spaces)`

> Spaces and special characters (`<`, `>`, `"`, backtick) in link URLs must be percent-encoded. Use `%20` for spaces or wrap the URL in angle brackets.

---

## Rule 6: Ordered List Number Formatting

**Correct:** Start at `1.` — numbers can repeat (Markdown auto-increments).
```
1. First item
1. Second item
1. Third item
```
Or use sequential numbers:
```
1. First item
2. Second item
3. Third item
```

**Incorrect:** Starting an ordered list at a number other than 1 when you intend it as the first item.
```
3. This item
4. That item
```

> Starting at 1 is recommended for portability. Some renderers ignore the actual number and always start from 1; others honor it (GitHub Flavored Markdown starts from the first number you use).

---

## Rule 7: Line Breaks — Trailing Double-Space or `<br>`

**Correct (trailing double-space):**
```
Line one
Line two on next line
```

**Correct (`<br>`):**
```
Line one<br>
Line two on next line
```

**Incorrect:**
```
Line one
Line two
```

> A single newline creates a soft wrap, not a rendered line break. Use two trailing spaces or `<br>` for a hard line break within a paragraph.

---

*Reference: https://www.markdownguide.org/basic-syntax/*
