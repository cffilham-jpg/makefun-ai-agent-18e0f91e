"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to entry.txt, with no trailing newline.
"""

import hashlib
import os
from pathlib import Path

LINE = "I renamed all your files to names I can pronounce, and your 'final_final_v2' is now just 'Steve'."

CHAR_LIMIT = 200


def validate() -> None:
    """Re-read entry.txt and assert it holds exactly LINE, one line."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    data = (out_dir / "entry.txt").read_bytes()
    text = data.decode("utf-8")
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must have no carriage return"
    assert 1 <= len(text) <= CHAR_LIMIT, "entry must be 1-200 characters"
    assert not data.endswith(b"\n"), "entry must have no trailing newline"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    assert text == LINE, "entry content must equal LINE"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
    validate()
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
