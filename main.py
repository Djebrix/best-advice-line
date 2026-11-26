#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes exactly one sentence (1-200 characters) about the best advice
the writer ever received to entry.txt in the output directory: a father's
first-day-of-work lesson, told in a single sentence with one terminal
period, so the file holds one line and nothing else.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = (
    "My father, handing me his dented toolbox on my first day of work, "
    "said: buy the good wrench once, or buy the cheap one forever."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
