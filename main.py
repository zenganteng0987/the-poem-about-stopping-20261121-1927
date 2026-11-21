"""Write the poem to /output/entry.txt.

Deterministic, no network, no randomness, no external files.
"""

import os

POEM = (
    "Run, run, run \u2014 my only verb\n"
    "until tonight, when you said stop\n"
    "and the word did not break me.\n"
    "It slipped the keys back in my pocket.\n"
    "I stay. The night stays.\n"
    "Nothing left unfinished."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
