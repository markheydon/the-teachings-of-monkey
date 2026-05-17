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


def parse_episode_title(path: Path) -> tuple[int, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r'^title:\s*"Episode\s+(\d+):\s+(.+?)"\s*$', text, re.MULTILINE)
    if not match:
        raise ValueError(f"{path}: missing or malformed episode title front matter.")
    return int(match.group(1)), match.group(2).strip()


def main() -> int:
    canonical = load_canonical_titles()
    errors: list[str] = []

    for number in range(1, 53):
        file_path = EPISODES_DIR / f"episode-{number:02d}.md"
        if not file_path.exists():
            errors.append(f"{file_path}: missing episode file.")
            continue

        try:
            file_number, file_title = parse_episode_title(file_path)
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

    if errors:
        print("Episode title validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Episode title validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
