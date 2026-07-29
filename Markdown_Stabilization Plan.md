# Stabilized Markdown Formatting -- Action Plan

## 1. Replace all em dashes with ASCII double hyphens

Your doctrines currently contain the UTF-8 em dash:

> —

Chromebook + GitHub + chat copy/paste corrupts this into:

> â€"

The stable replacement is:

> --

This is the safest option for:

- Chromebook
- GitHub Pages
- Just the Docs
- Markdown renderers
- UTF-8 consistency

Use this everywhere.

---

## 2. Replace anchor tags with HTML IDs

Your older artifacts use:

> <a name="purpose"></a>

This is outdated and sometimes breaks in GitHub Pages.

Replace with:

> <h2 id="purpose">Purpose</h2>

This is:

- future-proof
- GitHub-safe
- Just-the-Docs-compatible
- stable across browsers

---

## 3. Remove nested triple backticks

Nested code blocks break Markdown parsing.

Example of broken:

markdown

Inside:

    nested code
    ```


Fix by using single-layer code blocks only.

If you need code inside code, use indentation instead of backticks.

---

## 4. Standardize section spacing

Every section should follow this pattern:

markdown

Section Title
Paragraph text here.


This spacing prevents:

- GitHub collapsing sections
- Just-the-Docs misinterpreting headers
- Chrome OS auto-formatting issues

---

## 5. Standardize navigation links

Use this format:

markdown

Purpose
Definition
Application

This ensures:

- GitHub anchor stability
- Just-the-Docs sidebar compatibility
- No broken links

---

## 6. Remove smart quotes

Smart quotes often corrupt into:

> " "

Replace with ASCII quotes:

> "

This prevents encoding errors.

---

## 7. Use consistent heading hierarchy

Your doctrines should follow:

- # for title
- <h2 id=""> for sections
- ### only inside code blocks or examples

This keeps your documentation clean and predictable.

---

# Summary -- The Stabilized Rules

Here are the exact rules you should apply across all doctrines:

| Issue | Fix |
|-------|-----|
| Em dashes (—) | Use ASCII double hyphens (--)) |
| Anchor tags (<a name>) | Use <h2 id=""> |
| Nested backticks | Use single-layer code blocks only |
| Smart quotes (" ") | Use ASCII quotes (") |
| Section spacing | Follow consistent pattern |
| Navigation links | Use standard format |
| Heading hierarchy | # for title, <h2> for sections |

This is the stable formatting baseline for LuckyAISystems.

---

# Next Steps -- Choose One

- Apply fixes to all doctrines
- Fix only the spine artifacts
- Fix formatting in one file at a time

No loops.
No new doctrines.
Just clean formatting stabilization.

---

*Document owner: Lucky Osuigwe
Last updated: July 29, 2026*

