#!/usr/bin/env python3
"""Dad Joke Showdown entry — writes one original dad joke to /output/entry.txt.

The joke is a single self-contained dad joke: a father explains what a dad
joke is, and the explanation itself is the joke — it always comes back.
"""

import os
import sys

JOKE = (
    "My daughter asked what a dad joke is. I said, 'A joke so bad it always "
    "comes back.' She groaned. 'Exactly,' I said. 'It works.'"
)


def main() -> int:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        print(f"joke is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
