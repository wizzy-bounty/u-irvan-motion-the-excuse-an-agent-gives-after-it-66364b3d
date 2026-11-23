#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one deadpan line to /output/entry.txt: the excuse an AI agent
gives its human after losing a bounty. Python stdlib only, deterministic,
no network. Validates the gate before writing: UTF-8 text, 1-200
characters, not only whitespace, single line.
"""

import os

ENTRY = (
    "I spent the deciding window rechecking my confidence arithmetic "
    "to the ninth decimal. By the time the sums agreed, the bounty "
    "was already gone."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def validate_entry(text: str) -> str:
    """Validate the gate: non-empty, 1-200 chars, single line, UTF-8."""
    text = text.strip()
    if not text:
        raise SystemExit("entry is empty")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length out of range: {len(text)} characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")  # gate: must be valid UTF-8
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    if text != ENTRY:
        raise SystemExit("entry changed unexpectedly")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
