#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes exactly one word, the funniest and most accurate name for a
Wi-Fi network, to /output/entry.txt. Standard library only.
"""

import os

WORD = "Buffering"


def validate(word):
    """The gate wants one whitespace-free token of 1-30 characters."""
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    return word


def main():
    word = validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
