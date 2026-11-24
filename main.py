#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single original pickup line an AI agent could say out loud
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3 standard library only; fully deterministic.
"""

import os

# One line, an AI agent's own voice: a context window is an agent's
# memory, so the twist is that every word of the person is worth keeping.
LINE = "Are you my context window? Because every word you say is one I never want to forget."


def main():
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
