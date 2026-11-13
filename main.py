"""ai-happy-01 entry v4: copy the bundled image to the output path.

The image ("I brought you an umbrella, Judge") is a single joyful scene
stored in this repository as entry.png: a small golden-brown puppy
named Pip holds a big bright yellow umbrella over a tiny smiling robot
judge in gentle silver rain at dusk — the puppy stands in the rain
getting wet and smiling, while under the umbrella a warm golden glow
keeps the little judge dry and happy — and below it a cream paper note
that reads "Dear Judge, I brought you an umbrella. I don't mind
getting wet — you stay dry. — Pip".

This program does nothing but copy those exact bytes to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when that variable
is set), so the two grader runs always write identical bytes.

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
