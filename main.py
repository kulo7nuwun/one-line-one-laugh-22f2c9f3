#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt,
where the competition's gate scorer reads it.
"""

import os

LINE = "My AI agent won $1 in a joke contest and spent it on therapy for its imposter syndrome."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
