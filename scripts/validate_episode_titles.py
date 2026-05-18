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


def parse_tripitaka_entries(front_matter: str, path: Path) -> list[tuple[int, str]]:
    lines = front_matter.splitlines()
    entries: list[tuple[int, str]] = []
    i = 0

    while i < len(lines):
        if lines[i].strip() == "tripitaka_smackdowns:":
            i += 1
            while i < len(lines):
                line = lines[i]

                if line.startswith("  - rank:"):
                    rank_str = line.split(":", 1)[1].strip()
                    if not rank_str.isdigit():
                        raise ValueError(f"{path}: tripitaka rank must be an integer.")
                    rank = int(rank_str)

                    i += 1
                    if i >= len(lines) or not lines[i].startswith("    text:"):
                        raise ValueError(
                            f"{path}: each tripitaka entry must include text after rank."
                        )

                    text_raw = lines[i].split(":", 1)[1].strip()
                    if len(text_raw) < 2 or text_raw[0] != '"' or text_raw[-1] != '"':
                        raise ValueError(
                            f"{path}: tripitaka text must be wrapped in double quotes."
                        )

                    text = text_raw[1:-1].strip()
                    if not text:
                        raise ValueError(f"{path}: tripitaka text cannot be empty.")

                    entries.append((rank, text))
                    i += 1
                    continue

                if line.strip() == "":
                    i += 1
                    continue

                if line.startswith("  "):
                    raise ValueError(
                        f"{path}: unexpected tripitaka_smackdowns structure near '{line.strip()}'."
                    )

                break

            continue

        i += 1

    return entries


def parse_episode_data(
    path: Path,
) -> tuple[int, str, str, str, str, str, str, str, list[tuple[int, str]]]:
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

    tripitaka_entries = parse_tripitaka_entries(front_matter.group(1), path)

    return (
        int(match.group(1)),
        match.group(2).strip(),
        teaching_front_matter.group(1).strip(),
        teaching_section.group(1).strip(),
        pigsy_rating_front_matter.group(1).strip(),
        pigsy_note_front_matter.group(1).strip(),
        pigsy_section.group(1).strip(),
        pigsy_section.group(2).strip(),
        tripitaka_entries,
    )


def main() -> int:
    canonical = load_canonical_titles()
    errors: list[str] = []
    tripitaka_ranks: dict[int, Path] = {}

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
                tripitaka_entries,
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

        for tripitaka_rank, _tripitaka_text in tripitaka_entries:
            if tripitaka_rank in tripitaka_ranks:
                errors.append(
                    f"{file_path}: duplicate tripitaka rank {tripitaka_rank}. "
                    f"Also present in {tripitaka_ranks[tripitaka_rank]}."
                )
            else:
                tripitaka_ranks[tripitaka_rank] = file_path

    if tripitaka_ranks:
        sorted_ranks = sorted(tripitaka_ranks)
        if sorted_ranks[0] != 2:
            errors.append(
                "Tripitaka ranks must start at 2 because rank 1 is the recurring "
                "Chant of Discipline special case."
            )

        expected_ranks = list(range(2, sorted_ranks[-1] + 1))
        if sorted_ranks != expected_ranks:
            errors.append(
                "Tripitaka ranks must be contiguous from 2 onward. "
                f"Found {sorted_ranks}, expected {expected_ranks}."
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
