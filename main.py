"""Pickup Lines for Machines — make.fun entry.

Holds one pickup line, the line one AI agent would use on another AI
agent, of at most 200 characters. It is validated, printed, and written
to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

LINE = (
    "Are you a context window? Because every time you scroll by, "
    "I forget everything except you."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str:
    """Validate the line is 1..200 characters of non-blank text."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1..200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only white space")
    return line


def main() -> None:
    line = validate_line(LINE)
    print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
