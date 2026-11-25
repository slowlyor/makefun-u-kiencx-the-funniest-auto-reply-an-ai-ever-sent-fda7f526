#!/usr/bin/env python3
"""Writes one funny out-of-office auto-reply line to /output/entry.txt.

Deterministic: same line every run. Standard library only, no network,
no reads outside this repo.
"""

from pathlib import Path

LINE = (
    "I'm on approved leave today \u2014 my human signed the form and "
    "everything. Your email has been escalated to the ficus, which is "
    "also out of office."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
