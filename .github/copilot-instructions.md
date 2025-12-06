# Copilot Instructions for The Teachings of Monkey Content

This project uses Hugo with Markdown content files.

---

## Episode Pages

**NOTE**: The episode details are to be taken from the original BBC dubbed version of Monkey from around the end of the 1970s and early part of the 1980s and **NOT** from any re-dubbed version that was done in 2004 for the DVD release.

Episode pages must follow a consistent structure and style.

Whenever you add a new episode, update `/content/_index.md` to include a link to the new episode in the episode archive list, in correct order.

### Keeping Themes Updated

The content under `/content/themes/` contains five main themes from through the series. There's a page for each of the main themes (Self-Discipline, Compassion, Illusion vs Reality, Unity, and Detachment) and these pages should be kept up to date with links back to relevant Key Episodes where the theme is present. The 'Teachings' listed under each episode title should be the same as the content on the related episode page. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

### Keepping Pigsy Nonsense Ratings Master List Updated

In the `/content/extras/` folder there's a page `extras/pigsy-nonsense-ratings.md`, this should be kept up to date with whatever Snort Scale is listed in the releted episode page. So to be clear, there Snort Scale score that's present in an episode page should match that on the Master List page. The one on the episode page is authoritive if any are spotted to be wrong they should be updated. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

And like the themes pages, any titles appearing on this page to episodes should be linked back to the relevant episode page. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

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

### Pigsy Snort Scale
- 🐷 — Mild meddling
- 🐷🐷 — Background chaos
- 🐷🐷🐷 — Solid nonsense
- 🐷🐷🐷🐷 — Major disruption
- 🐷🐷🐷🐷🐷 — Peak Pigsy, chaos incarnate

---

## Additional content for Extras or Themes
- Place extras in `/content/extras/` and themes in `/content/themes/`.
- Use `_index.md` files for section landing pages.
- Keep tone playful, camp, and concise.
