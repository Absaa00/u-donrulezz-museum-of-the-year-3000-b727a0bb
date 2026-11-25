#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label writer.

Writes a single museum label (<=200 characters, one line, English) to
/output/entry.txt. Fully deterministic: no network, no randomness, no
clock, no environment input. The label is a fixed string.
"""

import os

LABEL = (
    "Group chat, c. 2025. A sacred circle where forty strangers "
    "shouted into the void each day; one answered 'lol'. Scholars "
    "believe this was prayer."
)


def main():
    assert 1 <= len(LABEL) <= 200, "label must be 1-200 characters"
    assert "\n" not in LABEL, "label must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
