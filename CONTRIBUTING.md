# Contributing to The Teachings of Monkey

Thanks for your interest in contributing! This project is a playful, open archive of the teachings, chaos, and camp from the cult TV series *Monkey (Saiyūki)*.

---

## How to Contribute

### 1. Adding Episodes

- Place new episode files in `/content/episodes/`.
- Use the template in `copilot-instructions.md` for consistency.
- **Episode names must match the [Official Episode List](/content/extras/official-episode-list.md)**, which contains the canonical list of all 52 episodes.
- Include:
  - Front matter (`title`, `date`, `draft: false`, `weight`)
    - `weight` should be set to the episode number (e.g. `weight: 2` for episode 2) to ensure correct sorting on the Episodes section page.
  - Sections: Synopsis, Teaching, Pigsy Nonsense Rating, Commentary
- **IMPORTANT:** After creating a new episode, update `/content/_index.md` (the home page) to add a link to the new episode in the episode archive list, in correct order. This keeps the main site up to date and makes new episodes easy to find.

### 2. Keep Master Lists Consistent
When adding or editing episodes, also update the extras:

- **Pigsy Nonsense Ratings** → `/content/extras/pigsy-nonsense-ratings.md`
  Format: `Episode XX — 🐷🐷🐷🐷 (short comment)`

- **Monkey Teachings** → `/content/extras/monkey-teachings.md`
  Format: `Episode XX — *"Teaching text here"*`

- **Tripitaka Smackdowns** → `/content/extras/tripitaka-smackdowns.md`
  Format: `Episode XX — "Quoted rebuke"`

- **Pigsy Greatest Hits** → `/content/extras/pigsy-greatest-hits.md`
  Format: `Episode XX — Short description of Pigsy’s highlight`

- **Demon Hall of Fame** → `/content/extras/demon-hall-of-fame.md`
  Format: `Episode XX — Demon Name — Short description`

- **Journey Tracker** → `/content/extras/journey-tracker.md`
  Format: `Episode XX — Milestone description`

### 3. Add Extras or Themes
- Place extras in `/content/extras/` and themes in `/content/themes/`.
- Use `_index.md` files for section landing pages.
- Keep tone playful, camp, and concise.

### 4. Submitting Changes
- Fork the repo and create a branch for your changes.
- Commit with clear messages (e.g. `Add Episode 12: Monkey Swallows the Universe`).
- Open a Pull Request with a short description of your contribution.

#### Monkey Teachings and Wisdom

- All canonical teachings from episodes must be added to `/content/extras/monkey-teachings.md`.
- Use the format:  
  `**[Episode XX: Title](/episodes/episode-XX/)** — *"Teaching text here"*`
- AI‑generated wisdom belongs in `/content/extras/monkey-wisdom-generator.md`.
- Contributors must include the prompt used when adding AI‑generated wisdom.

---

## Style Guidelines

- **Headings**: `##` for section titles.  
- **Teaching**: Italicised and quoted.  
- **Pigsy Rating**: Pig emoji 🐷 repeated 1–5 times.  
- **Dates**: Use original BBC air date if known.  
- **Tone**: Fun, nostalgic, and accessible.

### Episode Linking

- All episode mentions outside `/content/episodes/` must be linked and bolded.
- Use one of the two approved formats:

  - Standard:  
    **[Episode 8: Pigsy Woos a Widow](/episodes/episode-08/)**

  - Title‑first (for lists like Pigsy’s Greatest Hits):  
    **[Two Little Blessings (Episode 23)](/episodes/episode-23/)**

- Do not mix formats within the same file.
- Always ensure the link path matches the episode filename (`episode-XX.md`).

---

## License

All contributions are under the [CC BY‑NC‑SA 4.0 License](LICENSE).  
This means:
- ✅ You can share and remix.  
- ✅ You must give credit.  
- ❌ No commercial use.  
- ✅ Derivatives must use the same license.

---

## Code of Conduct

Be respectful, playful, and collaborative. This project celebrates camp and nostalgia — keep contributions fun and welcoming.

### Prompt Transparency

Because this project is primarily AI‑generated, all Pull Requests must include the **prompt used** to create the new content.

This ensures consistency, transparency, and helps others learn from the process.

