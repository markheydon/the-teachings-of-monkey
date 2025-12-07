# The Teachings of Monkey

An open source archive of wisdom, nonsense, and camp from the cult TV series *Monkey* (*Saiyūki*).

Each episode ends with a short narrated teaching — a pearl of wisdom distilled from chaos, demons, pilgrims, and Pigsy’s antics. This site collects those teachings, episode by episode, alongside commentary, fan reflections, and playful extras.

---

## 🚀 Live Site
Once deployed via GitHub Pages, visit:  
[https://markheydon.github.io/the-teachings-of-monkey/](https://markheydon.github.io/the-teachings-of-monkey/)

---

## 📂 Structure
- `/content/episodes/` — individual episode pages  
- `/content/themes/` — grouped moral lessons  
- `/content/extras/` — playful features (Pigsy’s Greatest Hits, Demon Hall of Fame, etc.)  
- `_index.md` files — landing pages for each section  

---

## 🛠️ Tech
- Built with [Hugo](https://gohugo.io/)  
- Theme: [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (swappable later)  
- Deployed via GitHub Pages + Actions  

---

## 🤝 Contributing
Pull requests welcome! Add commentary, new features, or your own “Monkey‑style” teachings.

See [Fan Participation](content/extras/fan-participation.md) for ideas.


## AI‑Generated Content

This archive is around 99% AI‑generated.

To ensure transparency and reproducibility, we include the prompts used to generate and review content:

- [Batch Episode Generation Prompt](#batch-episode-generation-prompt)  
- [Content Review Prompt](#content-review-prompt)

Contributors should include the **prompt they used** when submitting a Pull Request.

This keeps the project aligned with its goal: an AI‑driven, playful archive of *Monkey (Saiyūki)*.

### Batch Episode Generation Prompt

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

### Content Review Prompt
```
Review all Markdown files in `/content/episodes/` and `/content/extras/`.

Check that each file complies with `.github/copilot-instructions.md` and `CONTRIBUTING.md`:
- Correct front matter (`title`, `date`, `draft: false`).
- Required sections (Synopsis, Teaching, Pigsy Nonsense Rating, Commentary).
- Teaching italicised and quoted.
- Pigsy rating uses 🐷 emojis consistently.
- Master lists updated with matching entries.

Suggest corrections or regenerate files where inconsistencies are found.
```

---

## 📜 License
See [LICENSE](LICENSE) for details.

