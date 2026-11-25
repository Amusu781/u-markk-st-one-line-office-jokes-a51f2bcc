"""One-Line Office Jokes entry.

Writes a single one-line office joke to /output/entry.txt (no trailing
newline). The output dir is created if missing and is never deleted;
only the entry file inside it is overwritten.
"""

import os

LINE = (
    "Our office printer jams only on the document marked URGENT, "
    "which is how I learned machines can smell fear."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_line(path: str, text: str) -> None:
    """Overwrite the file at path with text, exactly, as UTF-8."""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 199, "line must be 1-199 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_line(OUTPUT_PATH, LINE)


if __name__ == "__main__":
    main()
