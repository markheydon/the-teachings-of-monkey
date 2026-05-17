#!/usr/bin/env python3
"""Validate canonical episode titles across episode pages."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPISODE_LIST = ROOT / "content/extras/episode-list.md"
EPISODES_DIR = ROOT / "content/episodes"


def load_canonical_titles() -> dict[int, str]:
    text = EPISODE_LIST.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\*\*\[Episode\s+(\d+):\s+([^\]]+)\]\(/episodes/episode-(\d{2})/\)\*\*"
    )
    titles: dict[int, str] = {}
    for match in pattern.finditer(text):
        number = int(match.group(1))
        title = match.group(2).strip()
        number_from_path = int(match.group(3))
        if number != number_from_path:
            raise ValueError(
                "Canonical list has mismatched episode numbering: "
                f"Episode {number} links to episode-{number_from_path:02d}."
            )
        if number in titles:
            raise ValueError(
                "Canonical list contains a duplicate episode entry: "
                f"Episode {number} appears more than once "
                f'("{titles[number]}" and "{title}").'
            )
        titles[number] = title

    if set(titles) != set(range(1, 53)):
        missing = sorted(set(range(1, 53)) - set(titles))
        extra = sorted(set(titles) - set(range(1, 53)))
        raise ValueError(
            "Canonical list must contain exactly episodes 1-52. "
            f"Missing: {missing or 'none'}. Extra: {extra or 'none'}."
        )
    return titles


def parse_episode_data(path: Path) -> tuple[int, str, str, str, str, str, str, str]:
    text = path.read_text(encoding="utf-8")

    front_matter = re.search(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not front_matter:
        raise ValueError(f"{path}: missing front matter block.")

    match = re.search(r'^title:\s*"Episode\s+(\d+):\s+(.+?)"\s*$', text, re.MULTILINE)
    if not match:
        raise ValueError(f"{path}: missing or malformed episode title front matter.")

    teaching_front_matter = re.search(
        r'^teaching:\s*"(.+?)"\s*$', front_matter.group(1), re.MULTILINE
    )
    if not teaching_front_matter:
        raise ValueError(f"{path}: missing teaching front matter.")

    teaching_section = re.search(r'^## Teaching\s*\r?\n\*"(.+?)"\*\s*$', text, re.MULTILINE)
    if not teaching_section:
        raise ValueError(f"{path}: missing or malformed Teaching section.")

    pigsy_rating_front_matter = re.search(
        r'^pigsy_rating:\s*"(🐷+)"\s*$', front_matter.group(1), re.MULTILINE
    )
    if not pigsy_rating_front_matter:
        raise ValueError(f"{path}: missing pigsy_rating front matter.")

    pigsy_note_front_matter = re.search(
        r'^pigsy_note:\s*"(.+?)"\s*$', front_matter.group(1), re.MULTILINE
    )
    if not pigsy_note_front_matter:
        raise ValueError(f"{path}: missing pigsy_note front matter.")

    pigsy_section = re.search(
        r'^## Pigsy Nonsense Rating\s*\r?\n(🐷+)\s+—\s+(.+?)\s*$',
        text,
        re.MULTILINE,
    )
    if not pigsy_section:
        raise ValueError(f"{path}: missing or malformed Pigsy Nonsense Rating section.")

    return (
        int(match.group(1)),
        match.group(2).strip(),
        teaching_front_matter.group(1).strip(),
        teaching_section.group(1).strip(),
        pigsy_rating_front_matter.group(1).strip(),
        pigsy_note_front_matter.group(1).strip(),
        pigsy_section.group(1).strip(),
        pigsy_section.group(2).strip(),
    )


def main() -> int:
    canonical = load_canonical_titles()
    errors: list[str] = []

    for number in range(1, 53):
        file_path = EPISODES_DIR / f"episode-{number:02d}.md"
        if not file_path.exists():
            errors.append(f"{file_path}: missing episode file.")
            continue

        try:
            (
                file_number,
                file_title,
                front_teaching,
                section_teaching,
                front_pigsy_rating,
                front_pigsy_note,
                section_pigsy_rating,
                section_pigsy_note,
            ) = parse_episode_data(file_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if file_number != number:
            errors.append(
                f"{file_path}: front matter says Episode {file_number}, expected {number}."
            )

        expected_title = canonical[number]
        if file_title != expected_title:
            errors.append(
                f"{file_path}: title mismatch. "
                f'Found "{file_title}", expected "{expected_title}".'
            )

        if front_teaching != section_teaching:
            errors.append(
                f"{file_path}: teaching mismatch. "
                f'Front matter has "{front_teaching}", section has "{section_teaching}".'
            )

        if front_pigsy_rating != section_pigsy_rating:
            errors.append(
                f"{file_path}: pigsy rating mismatch. "
                f'Front matter has "{front_pigsy_rating}", section has "{section_pigsy_rating}".'
            )

        if front_pigsy_note != section_pigsy_note:
            errors.append(
                f"{file_path}: pigsy note mismatch. "
                f'Front matter has "{front_pigsy_note}", section has "{section_pigsy_note}".'
            )

    if errors:
        print("Episode title validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Episode title validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
