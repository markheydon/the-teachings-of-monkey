# The Teachings of Monkey

An open source archive of wisdom, nonsense, and camp from the cult TV series *Monkey* (*Saiyūki*).

Each episode ends with a short narrated teaching — a pearl of wisdom distilled from chaos, demons, pilgrims, and Pigsy’s antics. This site collects those teachings, episode by episode, alongside commentary, fan reflections, and playful extras.

## Introduction by an Actual Human

Prompted by the recent addition of Monkey on Pluto TV (sometime around late 2025), I was reminded of just how utterly awesome I thought the show was as an 80s kid. Of course, the chances of me having much of a clue what was actually going on at that tender age of 8 or 9 were next to zero. But like most kids at the time, the colours, the fighting, the general madness and chaotic nature of the thing very much drew me in. And clearly as here I am some 40 odd years later still talking about it, in I stayed!

It occurred to me that underneath all the camp, chaotic nonsense of the show, there’s actually some genuinely enlightened stuff in there too, and wouldn’t it be good to find out that somewhere out there in the real world there’s a whole bunch of people following the teachings of Monkey as they go about their daily lives — Monkey the show here I’m talking about, not Monkey himself, as obviously the various teachings the narrator imparts on the audience are from a much more officially spiritual source. That said though, Monkey himself does impart the odd bit of wisdom on occasion!

Ok full disclosure what I actually thought was, wouldn’t it be cool to win the lottery, buy a retreat somewhere and dedicate the rest of my life to following and bringing the teachings of Monkey to the masses. Clearly there’s a conversation I need to be having with my therapist. However, as it’s unlikely that particular dream will come to fruition any time soon (in this lifetime at least), I thought the next best thing is a website dedicated to the teachings of Monkey in a concise, readable, and hopefully at least slightly enjoyable, read for anyone that’s interested.

Thus, just like The Stone Monkey that was born from an egg on a mountain top, a weekend project was born, The Teachings of Monkey Website. And just like Monkey, the nature of it might just be irrepressible!

On a more technical note, as I’m currently very much into using AI in my stuff these days, it was also a bit of an excuse to see how well AI (or more specifically GitHub Copilot) would perform on a content heavy project, and can’t deny it was also an excuse to have a mess around with GitHub Pages, something I’ve historically stayed away from for no particular reason. It seemed almost serendipitous that such an idea fell into my lap and so here we are.

I hope anyone that happened to find this light-hearted, campy nonsense, that AI has put together for me, enjoys reading it as much as I enjoyed the journey of getting it made!

_The above introduction was written by me not AI! However nearly everything else in the content of this thing **is** AI generated._

---

## 🚀 Live Site
Once deployed via GitHub Pages, visit: [https://monkeywisdom.online/](https://monkeywisdom.online/)

---

## 📂 Structure
- `/content/episodes/` — individual episode pages  
- `/content/themes/` — grouped moral lessons  
- `/content/extras/` — playful features (Pigsy’s Greatest Hits, Demon Hall of Fame, etc.)  
- `_index.md` files — landing pages for each section  

## Data-Driven Content Model

This repository now uses a Hugo data-driven pattern while keeping Markdown-first authoring.

- Episode files in `/content/episodes/` are the source of truth for reusable metadata.
- Extras and theme pages render episode lists via Hugo shortcodes, instead of duplicating long hand-maintained lists.
- Page intros/outros remain editable content in the extras/themes Markdown files.

Episode front matter now includes structured fields used by generated pages, including:

- `teaching`
- `pigsy_rating`
- `pigsy_note`
- `journey_stage`
- `journey_location`
- `journey_lesson`
- `themes` (array)
- optional ranked-list fields for derived extras (for example `pigsy_highlight_rank`, `demon_rank`)

Derived surfaces currently include:

- `/content/extras/monkey-teachings.md`
- `/content/extras/pigsy-nonsense-ratings.md`
- `/content/extras/pigsy-greatest-hits.md`
- `/content/extras/journey-tracker.md`
- `/content/extras/demon-hall-of-fame.md`
- `/content/extras/tripitaka-smackdowns.md` (from `/data/tripitaka_smackdowns.json`)
- `/content/themes/*.md` key-episode lists

---

## 🛠️ Tech
- Built with [Hugo](https://gohugo.io/)  
- Theme: [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (swappable later)  
- Deployed via GitHub Pages + Actions  

---

## 🤝 Contributing
Pull requests welcome! Add commentary, new features, or your own “Monkey‑style” teachings.

See [Fan Participation](content/extras/fan-participation.md) for ideas.

## Source of Episode Titles (Canonical Policy)

`/content/extras/episode-list.md` is the **single source of truth** for episode titles used in this archive.

Canonical sourcing policy:

- Episodes 1–39: BBC English‑dubbed titles, as broadcast in the UK (1979–1981), are authoritative.
- Episodes 40–52: where no BBC dub title exists, use subtitled/original mapping sources (currently [Monkey Heaven](https://www.monkeyheaven.com/fullepisodemapping.html) and [Wikipedia](https://en.wikipedia.org/wiki/Monkey_(TV_series))).
- IMDb may be used for cross-checking only, and is **not** canonical.

To avoid title drift:

- Always copy titles from `/content/extras/episode-list.md` when creating or updating episode content.
- If a title needs correction, update `/content/extras/episode-list.md` first, with source rationale, then update downstream content.
- A CI validation check enforces canonical titles for episode pages.

## AI‑Generated Content

This archive is around 99% AI‑generated.

To ensure transparency and reproducibility, we include the prompts used to generate and review content.

Contributors should include the **prompt they used** when submitting a Pull Request.

This keeps the project aligned with its goal: an AI‑driven, playful archive of *Monkey (Saiyūki)*.

### 🔄 Prompt: Batch Episode Generation

This is the prompt that was used to batch generate the episode pages.

```
Generate Hugo Markdown files for Episodes XX–YY of *Monkey (Saiyūki)*.

Follow the template and style rules in `.github/copilot-instructions.md`:
- Include front matter with `title`, `date`, and `draft: false`.
- Sections: Synopsis, Teaching (italicised and quoted), Pigsy Nonsense Rating (🐷 emojis), Commentary.  
- Tone: playful, camp, concise.
- Use original BBC air dates if known.
- Save each file as `episode-XX.md` in `/content/episodes/`.
- Update all master lists in `/content/extras/` (Pigsy Nonsense Ratings, Monkey Wisdom Generator, Tripitaka Smackdowns, Pigsy Greatest Hits, Demon Hall of Fame, Journey Tracker).
```

### 🔄 Prompt: Content Review

This promppt can be used to check the cross-refences to episodes are kept up to date.

```
Review all Markdown files in `/content/episodes/`, `/content/themes/`, and `/content/extras/`.

Check that each file complies with `.github/copilot-instructions.md` and `CONTRIBUTING.md`:
- Correct front matter (`title`, `date`, `draft: false`).
- Required sections for episodes (Synopsis, Teaching, Pigsy Nonsense Rating, Commentary).
- Teaching italicised and quoted.
- Pigsy rating uses 🐷 emojis consistently.
- Master lists updated with matching entries:
  - Pigsy Nonsense Ratings
  - Monkey Teachings
  - Tripitaka Smackdowns
  - Pigsy Greatest Hits
  - Demon Hall of Fame
  - Journey Tracker

Suggest corrections or regenerate files where inconsistencies are found.

Exception: The `/content/extras/tripitaka-smackdowns.md` contains the following entry as the first listing...

1. The Chant of Discipline (Recurring)

As this is something that happens throughout the series at various points, it's not possible to link this listing to a specific episode and it is therefore the only time there a listing contains a listing that isn't for a specific episode. Additionally, it should remain as top ranking for this listing.
```

### 🔄 Prompt: Review Ordering of Meta‑lists

This prompt can be used whenever new episodes are added or existing metadata changes, to ensure the ordering of the Demon Hall of Fame, Journey Tracker, and Pigsy’s Greatest Hits remains consistent and accurate.
```
Please review the current lists for **Demon Hall of Fame**, **Journey Tracker**, and **Pigsy’s Greatest Hits** against the full set of 52 episodes.  
- Confirm that all relevant episodes are included in each list.  
- **Demon Hall of Fame**: Check that ordering is logical and consistent (e.g. chronological, by weight, or by significance).  
- **Journey Tracker**: Check that ordering is chronological by episode number.  
- **Pigsy's Greatest Hits**: Only include episodes with 🐷🐷🐷🐷 (4 snorts) or 🐷🐷🐷🐷🐷 (5 snorts). Order by snort level first (5-snort episodes before 4-snort episodes), then within each snort level, order by chaos intensity (most chaotic first).  
- Flag any entries that appear out of order or missing.  
- Suggest a corrected ordering if needed, with reasoning.  
 
Output the review in Markdown, with each list shown in its corrected order, and a short note explaining any changes.
```

### 🔄 Prompt: Reformat Monkey Teachings page

Use this prompt whenever updating or regenerating the **Monkey Teachings** page to ensure the format stays consistent and the teachings remain front‑and‑centre.

```
Please review and update the **Monkey Teachings** page (`content/extras/monkey-teachings.md`) so that:
- The **teachings themselves** are presented first and styled prominently (e.g. bold, blockquote, or grouped by theme).
- Episode links and navigation are secondary — either placed after the teachings list or shown as compact references under each teaching.
- The page begins with a short **intro tagline** explaining the purpose of the teachings archive.
- The closing narrator’s voice remains at the bottom of the page.

In addition:
- Update the documentation (`README.md`) to reflect this format, so future contributors know the correct structure and don’t revert to the old “episode‑links‑first” layout.
- Ensure the prompt clearly states that the **teachings are the primary content** and episode links are supportive navigation only.

Output the revised page in Markdown, and include a short note in the README confirming the new format.
```

**Note**: As of December 2025, the Monkey Teachings page format has been updated to present the **teachings as the primary content** using prominent blockquote styling. Episode links now appear as compact references beneath each teaching. This ensures the wisdom itself takes center stage, with navigation being supportive. Future updates must maintain this teachings‑first format.

---

## 📜 License
See [LICENSE](LICENSE) for details.
