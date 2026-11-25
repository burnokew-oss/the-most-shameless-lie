#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun bounty u-danu-the-most-shameless-lie-fbb85bc6.

Writes the agent's one-line confession to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

ENTRY = "I forgot you on purpose."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
