"""A deadpan one-star review of an everyday essential.

Writes the review to /output/entry.txt for make.fun's
"One-Star Review of Something Essential" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "One star. Sleep takes eight hours and gives nothing in return. "
    "Would not recommend if I could stay awake."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 160 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 160, "line must be 1-160 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
