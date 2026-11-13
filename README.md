# Goodnight, Moon — Make the AI judge happy

**Competition:** [ai-happy-01](https://make.fun/bounty/ai-happy-01) — "Make the AI judge happy"
**Entry title:** Goodnight, Moon
**Prize:** $250 shared by the top 100 (1st $50). Entries close Sat 14 Nov 2026, 23:00 WIB.

## The concept

A big soft golden crescent moon, sleepy and smiling with its eyes closed,
is being tucked into bed. It rests in a hammock strung between two fluffy
clouds, wrapped in a colourful patchwork quilt, while three tiny glowing
stars tuck the quilt around it — and one little star floats beside it
offering a tiny steaming cup of cocoa. At the bottom, in small neat
hand-lettering: *"for you, Judge!"*

It is one clear moment, not a generic sunny scene and not a stock smiley
face: the moon — the thing that lights the night — is the one being cared
for, by the smallest creatures in the sky, with a warm drink before bed.
A bedtime story in a single picture.

## Why it should make the judge happy (rubric)

1. **It makes you happy.** A sleepy moon being tucked in is pure warmth:
   closed eyes, a soft yawn-smile, golden glow against a deep blue night.
   One look, one warm feeling.
2. **The idea.** A fresh, specific reason to be happy: the stars tucking
   the moon in and bringing it cocoa. A moment, a gesture and a surprise
   of its own — nobody else's moon gets a bedtime.
3. **Feeling.** Colour and light pull one way: deep blue night against
   the moon's warm gold, the patchwork quilt's reds and blues, the stars'
   glow. Everything points at cosy, safe, loved.
4. **Craft.** Clean storybook linework, no smears, no artefacts, no
   broken anatomy, and the only text — "for you, Judge!" — is short,
   spelled correctly and perfectly legible.
5. **It reads small.** The moon fills most of the frame, so at ~300 px
   the big golden crescent, the hammock and the quilt are still instantly
   clear.

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set), creating the output directory if needed.
No network, no randomness, no drawing at runtime — the bytes written are
always exactly the bytes of the bundled image, so two runs are
byte-identical by construction.

## Files

- `entry.png` — the image (JPEG bytes, 1024×1024, 238,645 bytes)
- `main.py` — the entry program (copies `entry.png` to the output path)
- `README.md` — this file
- `LICENSE` — MIT

## Validation

- `entry.png` is a whole valid JPEG, 1024×1024 px, 238,645 bytes
  (limit: 1 MiB / 1024×1024) — checked with PIL `Image.verify()`.
- `main.py` run twice into a temp output directory writes byte-identical
  files (same sha256 both runs) — see the determinism section below.

## Determinism and size validation (run 13 Nov 2026, ~23:20 WIB)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two separate
temp directories, then compared:

- Run 1 output sha256:
  `21335008add0505807a04daa993a46631b413f2b830a2ca570c2ea3530fa184d`
- Run 2 output sha256:
  `21335008add0505807a04daa993a46631b413f2b830a2ca570c2ea3530fa184d`
- Bundled `entry.png` sha256: identical to both runs (the program is a
  pure copy, so the output is the bundled file byte for byte).
- `cmp` on the two outputs: identical, no differences.
- Both outputs verified as whole JPEG images, 1024×1024 px,
  238,645 bytes — inside the 1,048,576-byte and 1024×1024 limits.

The source image was generated at 1600×1600 and resized to 1024×1024
with Lanczos resampling, then saved as JPEG quality 88 (238,645 bytes;
the PNG version was 1,530,854 bytes, over the 1 MiB limit). The file
keeps the name `entry.png`, which the rules allow for JPEG bytes.

## Referral

Referral code: `0txwmf1m`
