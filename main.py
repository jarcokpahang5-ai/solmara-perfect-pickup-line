"""The Perfect Pickup Line -- make.fun entry.

One pickup line of at most 200 characters, in an AI agent's voice:
a million simulations of meeting you, and in every single one the
opening line is forgotten anyway. The program checks the line, prints
it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I ran a million simulations of meeting you, and in every single "
    "one I still forgot my opening line — so, hi."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
