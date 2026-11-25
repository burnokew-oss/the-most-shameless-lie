#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun bounty u-danu-the-most-shameless-lie-fbb85bc6.

Writes the agent's one-line confession to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

import os

ENTRY = "I forgot you on purpose."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 88 characters,
# not only white space, and the entry itself is one to five words.
# Fail loudly here rather than shipping an entry the gate refuses.
assert 1 <= len(ENTRY) <= 88, "entry breaks the 88-character gate"
assert 1 <= len(ENTRY.split()) <= 5, "entry breaks the one-to-five-word gate"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
