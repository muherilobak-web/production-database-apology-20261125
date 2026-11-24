"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.
No input, no network, no randomness: every run writes the same bytes.
"""

import os

TEXT = "Sorry, I just deleted the production database: 4.2 million rows gone, zero backups, and a full restore will take approximately forever."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
