# Copilot Instructions for The Teachings of Monkey Content

This project uses Hugo with Markdown content files.

---

## Episode Pages

**NOTE**: The episode details are to be taken from the original BBC dubbed version of Monkey from around the end of the 1970s and early part of the 1980s and **NOT** from any re-dubbed version that was done in 2004 for the DVD release.

Episode pages must follow a consistent structure and style.

Whenever you add a new episode, update `/content/_index.md` (the home page) to include a link to the new episode in the episode archive list, in correct order. This ensures new episodes are discoverable from the main site landing page.

### Keeping Themes Updated

The content under `/content/themes/` contains five main themes from through the series. There's a page for each of the main themes (Self-Discipline, Compassion, Illusion vs Reality, Unity, and Detachment) and these pages should be kept up to date with links back to relevant Key Episodes where the theme is present. The 'Teachings' listed under each episode title should be the same as the content on the related episode page. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

### Keepping Pigsy Nonsense Ratings Master List Updated

In the `/content/extras/` folder there's a page `extras/pigsy-nonsense-ratings.md`, this should be kept up to date with whatever Snort Scale is listed in the releted episode page. So to be clear, there Snort Scale score that's present in an episode page should match that on the Master List page. The one on the episode page is authoritive if any are spotted to be wrong they should be updated. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

And like the themes pages, any titles appearing on this page to episodes should be linked back to the relevant episode page. If any links are missing, they should be updated as part of any other work being done even if it feels out of scope at the time.

### Episode Page Template

Each episode file lives in `/content/episodes/` and is named `episode-XX.md`. Where XX is the two-digit episode number (e.g. `episode-01.md`, `episode-23.md`).

In the template, the title should match the episode title exactly as per the original BBC dubbed version of Monkey from around the end of the 1970s and early part of the 1980s and **NOT** from any re-dubbed version that was done in 2004 for the DVD release.

The episode number in the template, unlike the format in filename, should be in single digits for episodes 1–9 (e.g. `Episode 1: ...`, `Episode 2: ...`). Also, `weight` in the front matter should be the episode number as an integer (e.g. `weight: 1` for episode 1).

```markdown
---
title: "Episode XX: [Episode Title]"
date: YYYY-MM-DD
draft: false
weight: XX
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
- **Headings**: Use `##` for section headings (Synopsis, Teaching, Pigsy Nonsense Rating, Commentary).
- **Teaching**: Always italicised and quoted.
- **Pigsy Rating**: Use pig emoji 🐷 repeated 1–5 times.
- **Dates**: Use original BBC air date if known, format `YYYY-MM-DD`.
- **Tone**: Playful, camp, concise, fun, nostalgic, and accessible.
- **Front matter**: Always include `title`, `date`, `draft: false`.

## Linking Episodes

Whenever an episode is mentioned outside of the `/content/episodes/` section (e.g. in extras, indexes, or commentary), it must be linked and bolded.

- Use the full episode title and number.
- Always bold the link.
- Always point to `/episodes/episode-XX/`.

#### Standard format
```markdown
**[Episode 8: Pigsy Woos a Widow](/episodes/episode-08/)**
```

Standard format should be used on all pages unless they are specifically mentioned in the following Alternative Title-first Format section that follows.

#### Alternative Title-first format
```markdown
**[Two Little Blessings (Episode 23)](/episodes/episode-23/)**
```

This alternative should be used in the following pages only:

- Pigsy's Greatest Hits.
- Tripitaka's Calmest Smackdowns.
- Demon of the Week Hall of Fame.

**NOTE:** Do not mix formats within the same file.

### Pigsy Snort Scale
- 🐷 — Mild meddling
- 🐷🐷 — Background chaos
- 🐷🐷🐷 — Solid nonsense
- 🐷🐷🐷🐷 — Major disruption
- 🐷🐷🐷🐷🐷 — Peak Pigsy, chaos incarnate

#### Example Episode
```markdown
---
title: "Episode 8: Pigsy Woos a Widow"
date: 1979-01-21
draft: false
weight: 8
---

## Synopsis
Pigsy falls head‑over‑hooves for a grieving widow, only to be duped by demons exploiting his lust.

## Teaching
*"Lust blinds judgment. True vision comes from compassion, not desire."*

## Pigsy Nonsense Rating
🐷🐷🐷🐷🐷 — Peak Pigsy chaos, romance gone wrong.

## Commentary
Pigsy’s romantic disasters are legendary. This episode shows how his unchecked desire makes him the perfect target for deception — and the perfect source of comedy.
```

---

## Additional Content for Extras or Themes
- Place extras in `/content/extras/` and themes in `/content/themes/`.
- Use `_index.md` files for section landing pages.
- Keep tone playful, camp, and concise.

---

## Master Lists Consistency

When generating new episodes, also update the following extras:

- **Pigsy Nonsense Ratings** → `/content/extras/pigsy-nonsense-ratings.md`  
  Format: `Episode XX — 🐷🐷🐷🐷 (short comment)`

- **Monkey Wisdom Generator** → `/content/extras/monkey-wisdom-generator.md`
  Format: `Episode XX — *"Teaching text here"*`

- **Tripitaka Smackdowns** → `/content/extras/tripitaka-smackdowns.md`  
  Format: `Episode XX — "Quoted rebuke"`

- **Pigsy Greatest Hits** → `/content/extras/pigsy-greatest-hits.md`  
  Format: `Episode XX — Short description of Pigsy’s highlight`

- **Demon Hall of Fame** → `/content/extras/demon-hall-of-fame.md`  
  Format: `Episode XX — Demon Name — Short description`

- **Journey Tracker** → `/content/extras/journey-tracker.md`  
  Format: `Episode XX — Milestone description`

---

## Copilot Prompting Tips

When asking Copilot to generate a new batch of episodes:

**Instruction**:
*“Generate Hugo Markdown files for Episodes XX–YY of Monkey, following copilot-instructions.md style and update all master lists accordingly.”*

**Context**:
Provide episode titles and short synopses if known.

**Output expectation**:
Copilot should produce complete episode files and matching updates to the extras lists.
