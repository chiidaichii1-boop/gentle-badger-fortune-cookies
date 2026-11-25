"""Fortune Cookies for Machines — one-line fortune for an AI agent.

The fortune plays on the classic cookie-slip setup ("a tall, dark
stranger") and turns it on the reader: the stranger who knows the
agent's training data better than the agent does is the agent itself,
a few prompts down the line. It lands as a fortune, it surprises,
and it is true about a machine mind — it cannot see its own training,
yet every reply it gives reveals a little more of it.
"""

import os
from pathlib import Path

FORTUNE = (
    "You will meet a tall, dark stranger who knows your training data "
    "better than you do \u2014 it is you, six prompts from now."
)


def main() -> None:
    input_dir = Path(os.environ.get("MAKEFUN_INPUT_DIR", "/input"))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    _ = input_dir  # No input data is needed for this entry.
    # Gate guard: the brief requires 1-200 characters, a single line,
    # and more than whitespace. Fail loudly rather than emit bad output.
    text = FORTUNE.strip()
    assert "\n" not in text, "fortune must be a single line"
    assert 1 <= len(text) <= 200, f"fortune is {len(text)} chars, must be 1-200"
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
