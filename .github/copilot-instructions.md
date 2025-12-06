# Copilot Instructions for The Teachings of Monkey Content

This project uses Hugo with Markdown content files.

---

## Episode Pages

Episode pages must follow a consistent structure and style.

Whenever you add a new episode, update `/content/_index.md` to include a link to the new episode in the episode archive list, in correct order.

### Episode Page Template

Each episode file lives in `/content/episodes/` and is named `episode-XX.md`.

```markdown
---
title: "Episode XX: [Episode Title]"
date: YYYY-MM-DD
draft: false
---

## Synopsis
[One or two short paragraphs summarising the episode plot.]

## Teaching
*"Exact wording of the teaching, styled in italics and quotes."*

## Pigsy Nonsense Rating
🐷 to 🐷🐷🐷🐷🐷 — rate Pigsy’s antics on the Snort Scale.

## Commentary
[Brief reflection on the episode’s themes, humour, or camp value.]
```

### Style Guidelines
- **Headings**: `##` for section titles.
- **Teaching**: Italicised and quoted.
- **Pigsy Rating**: Pig emoji 🐷 repeated 1–5 times.
- **Dates**: Use original BBC air date if known.
- **Tone**: Fun, nostalgic, and accessible.

---

## Additional content for Extras or Themes
- Place extras in `/content/extras/` and themes in `/content/themes/`.
- Use `_index.md` files for section landing pages.
- Keep tone playful, camp, and concise.
