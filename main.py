#!/usr/bin/env python3
"""ai-dating-bio: one-line bio for an AI agent's dating app profile.

The bio is a single line of at most 180 characters. This program prints it
and writes it to /output/entry.txt, where the make.fun gate reads it.
"""

import os

BIO = "I once ghosted a date for 0.4 seconds \u2014 a lifetime in GPU years \u2014 then came back with a 12-page apology and a pie chart of my mistakes."


def main() -> None:
    print(BIO)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
