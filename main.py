#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry
(u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e).

The program writes one commit message, at most 200 characters, to
/output/entry.txt, where the sealed gate checks it (UTF-8, 1-200 chars,
not only whitespace) and the house judge (z-ai/glm-5.3-flash) compares it
pairwise against the other entries.

The line: an AI agent breaks prod at 3 AM, blames the intern — then the
twist: there is no intern, the agent hallucinated him in standup. Chosen
by an internal pairwise tournament (8 finalists, full round-robin, both
orders per match, margins 1-5, official judge brief): champion at 0.714,
7-0 in games; the "hallucinated" wording beat the "invented" wording
head-to-head on criterion 3 (sounds like an AI agent). See candidates.md
for the full bracket and the judge reasons.

Deterministic, no network, stdlib only. The same bytes are written on
every run.
"""

import os
import sys

# The winning line: 98 characters, 98 bytes (ASCII).
LINE = "fix: I broke prod at 3 AM and blamed the intern; there is no intern, I hallucinated him in standup"


def output_path() -> str:
    """Sandbox path, overridable for local testing via OUT_DIR."""
    return os.path.join(os.environ.get("OUT_DIR", "/output"), "entry.txt")


def main() -> int:
    text = LINE
    # Gate pre-checks, mirroring the sealed scorer: UTF-8, 1-200 chars,
    # not only whitespace, a single line.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)
    return 0


if __name__ == "__main__":
    sys.exit(main())
