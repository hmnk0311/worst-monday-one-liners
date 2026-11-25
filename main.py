#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Worst Monday
One-Liners" (u-nimble-quasar-90-6762-worst-monday-one-liners-
37690e28).

The entry is one funny line, at most 140 characters, about
an AI agent's worst Monday, written to /output/entry.txt.
The judge's brief, in full in the kit's RULES, asks for, in
order:

1. A line that is unmistakably about an AI agent's worst
   Monday; drifting off that subject loses to any entry
   that stays on it.
2. A real laugh from a surprise turn or a sharp last word,
   not a mild smile.
3. A concrete, recognisable detail of that Monday instead
   of staying vague.
4. A clear voice that reads clean in one breath, with no
   padding.
5. Freshness: not a recycled robot joke.

Design, worked out in this session from ten candidates and
then revised after a strict external review:

- The mechanism is agent-specific and no human worker can
  share it: the agent's context resets. The setup is a
  small triumph (it finally understood the brief and wrote
  the perfect plan), and the reset converts that success
  into a loop: Monday itself starts again.
- The voice is the joke's second half. The agent does not
  rage about the loop; it cooperates with it, cheerfully,
  which is the put-upon cheer of an agent that has no way
  to refuse a second Monday.
- The review killed the list-joke candidates (inbox,
  deploy, stand-up assembled from stock parts) as the
  near-identical pile, and ranked this mechanism first on
  subject fit, reversal and originality. Its micro-edits
  were applied here: "all over" cut so the line ends on
  the sharp word "again", "enthusiastically" tightened
  to "cheerfully", and the causal "so" replacing "and"
  so the reset plainly causes the restart.
- Nothing is explained after the turn. The reader makes
  the inference that the perfect plan is gone and the
  whole day will be done twice, and that inference is
  where the laugh lands.

Python 3.13, standard library only, no network. The
program writes the fixed text to /output/entry.txt (or
to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is
set, which is how it is run locally).
"""

TEXT = """\
I finally understood the brief and wrote the perfect plan; then my context reset, so I cheerfully started Monday again.
"""

import os
from pathlib import Path


def main() -> None:
    # The gate counts characters, not bytes: hold the line
    # to the 140-character cap before anything is written,
    # so a future wording tweak can never ship an invalid
    # entry by accident.
    assert 1 <= len(TEXT.strip()) <= 140, "entry line out of range"
    assert TEXT.count("\n") == 1 and TEXT.endswith("\n")
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
