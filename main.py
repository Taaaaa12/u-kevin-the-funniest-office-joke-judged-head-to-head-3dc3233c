#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — entry program.

Writes one original one-line joke about office life to /output/entry.txt.

The joke is fixed text: fully deterministic by design. No randomness, no
network, no clock, no environment dependence. Running this program twice
produces byte-identical output.
"""

import os
import sys

JOKE = (
    "I put 'per my last email' in my out-of-office reply, "
    "so now it answers everything \u2014 including my mum's birthday wishes."
)


def main() -> int:
    # The gate requires 1-200 characters of UTF-8 text, not only white
    # space, on a single line. Enforce that here so a bad edit fails
    # loudly instead of shipping an invalid entry.
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be one line"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only white space"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
