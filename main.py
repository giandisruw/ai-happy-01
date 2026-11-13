"""ai-happy-01 entry: copy the bundled image to the output path.

The image ("Goodnight, Moon") is a single joyful scene stored in this
repository as entry.png. This program does nothing but copy those exact
bytes to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when that
variable is set), so the two grader runs always write identical bytes.

Standard library only, no network, no randomness.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
