"""Worst AI Advice — u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The line is a
confident assistant-style answer to a beeping smoke detector: it
recommends removing the battery, which silences the alarm and the
protection at once. Validated against the competition gate before it
is written: UTF-8 text, 1-140 characters, not only whitespace,
single line, no leading or trailing whitespace.
"""

import os

ENTRY = (
    "Great question! Your smoke detector only beeps when the battery "
    "is low, so removing the battery fixes the noise — and the fire risk."
)

MAX_CHARS = 140


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def entry_path():
    """Resolve the output file path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    line = validate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
