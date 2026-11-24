#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, on every run.
"""

import os

ENTRY = (
    "A stranger will fork your repo tonight. "
    "Flattering \u2014 until they file the bug you already knew about."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Enforce the competition gate on the entry text.

    Raises ValueError on any violation:
    - not valid UTF-8 text (checked by the caller on the encoded bytes)
    - empty, only whitespace, or longer than 140 characters
    - more than one line
    - leading or trailing whitespace
    - any control character (C0, C1, DEL, U+2028, U+2029, U+FEFF)
    """
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} characters, over the 140 limit")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        code = ord(ch)
        if (
            code < 0x20
            or 0x7F <= code <= 0x9F
            or ch in ("\u2028", "\u2029", "\ufeff")
        ):
            raise ValueError(f"entry contains forbidden character U+{code:04X}")


def main() -> None:
    validate_entry(ENTRY)
    encoded = ENTRY.encode("utf-8")
    # Round-trip check: the bytes we write must decode back to the entry.
    if encoded.decode("utf-8") != ENTRY:
        raise ValueError("entry is not valid UTF-8 round-trip text")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
