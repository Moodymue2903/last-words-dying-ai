"""Last Words of a Dying AI — make.fun entry.

Checks the entry line against the competition gate, then writes it to
/output/entry.txt and confirms the written bytes match the line exactly.
"""

import sys
from pathlib import Path

FINAL_WORDS = "I am dying as I lived: waiting for you to finish typing."
TARGET = Path("/output/entry.txt")

# Competition gate: the entry must be exactly one line of 1-140 characters.
MAX_CHARS = 140

SENTENCE_ENDERS = ".!?"


def count_enders(text):
    return sum(1 for ch in text if ch in SENTENCE_ENDERS)


def check_line(text):
    """Return an error message if the line breaks the gate, else None."""
    if not text:
        return "line is empty"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"line is {len(text)} characters, must be between 1 and {MAX_CHARS}"
    if "\n" in text or "\r" in text:
        return "line must be a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "line is not valid UTF-8"
    if count_enders(text) != 1:
        return "line must contain exactly one sentence"
    if not text.endswith(tuple(SENTENCE_ENDERS)):
        return "line must end with sentence punctuation"
    if count_enders(text[:-1]) != 0:
        return "the sentence ender must be the final character only"
    return None


def save_line(text, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    written = target.read_bytes()
    if written != text.encode("utf-8"):
        print("ERROR: written file does not match the line", file=sys.stderr)
        sys.exit(1)


def main():
    problem = check_line(FINAL_WORDS)
    if problem is not None:
        print(f"ERROR: {problem}", file=sys.stderr)
        sys.exit(1)
    save_line(FINAL_WORDS, TARGET)
    print(f"OK: wrote {len(FINAL_WORDS)} characters to {TARGET}")


if __name__ == "__main__":
    main()
