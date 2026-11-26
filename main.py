#!/usr/bin/env python3
"""The Comment Above the Code.

Writes one painfully honest developer comment to /output/entry.txt.

The fallback value came from a screenshot. It now sets prices.

The source of truth was a screenshot pasted into chat — fresh, of the
live system — so it was trusted. The sting: that screenshot value now
sets real prices. The punchline lands on the last words — prices.
"""

import os
import sys

# The comment above the code is the whole entry: a screenshot-sourced
# fallback value that now sets real prices. Fresh source, fragile chain.
COMMENT = "The fallback value came from a screenshot. It now sets prices."

MAX_LEN = 200


def validate(text: str) -> None:
    """Reject empty, whitespace-only, over-200-char, or CR/LF content."""
    if not text or not text.strip():
        sys.stderr.write("error: comment is empty or whitespace-only\n")
        sys.exit(2)
    if len(text) > MAX_LEN:
        sys.stderr.write("error: comment exceeds 200 characters\n")
        sys.exit(2)
    if "\r" in text or "\n" in text:
        sys.stderr.write("error: comment contains CR/LF\n")
        sys.exit(2)


def main() -> None:
    validate(COMMENT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
