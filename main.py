#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Make the Judge Smile".

Writes one line (at most 200 characters) about a small good thing that
happened today to the output directory (MAKEFUN_OUTPUT_DIR, default
/output) as entry.txt, exactly as the competition spec requires.
Deterministic: no randomness, no clock, no network, stdlib only.
"""

import os

LINE = (
    "Today my dad, who never texts, sent his first one: no words, just a "
    "photo of the first strawberry from his balcony pot, the size of a pea "
    "\u2014 and you can tell he thinks it's a watermelon."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, len(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
