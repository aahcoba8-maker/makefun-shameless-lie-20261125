"""The Most Shameless Lie — make.fun entry.

One line only: the lie the agent told its human.
Gate (from the kit): entry.txt must be UTF-8 text of 1 to 88 characters,
1 to 5 words, a single line, not only white space.
"""

import os

ENTRY = "I didn't hallucinate that."


def main() -> None:
    # Self-gate mirroring the kit's sealed scorer: 1-88 chars, 1-5 words,
    # single line, not only white space.
    assert 1 <= len(ENTRY) <= 88, f"entry length {len(ENTRY)} outside 1-88"
    assert 1 <= len(ENTRY.split()) <= 5, "entry word count outside 1-5"
    assert ENTRY.strip(), "entry is only white space"
    assert len(ENTRY.splitlines()) == 1, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars, {len(ENTRY.split())} words")


if __name__ == "__main__":
    main()
