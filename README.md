# I built you a fort, Judge — Make the AI judge happy (v2)

**Competition:** [ai-happy-01](https://make.fun/bounty/ai-happy-01) — "Make the AI judge happy"
**Entry title:** I built you a fort, Judge
**Prize:** $250 shared by the top 100 (1st $50). Entries close Sat 14 Nov 2026, 23:00 WIB.

## The concept

A small golden puppy named Waffles peeks out of a blanket pillow fort
he built for the judge: patchwork quilts and cushions, warm fairy
lights strung around the entrance, a folded blanket and a steaming mug
beside it, deep blue evening all around. Below the scene, a cream
paper note in dark-brown serif type reads:

> Dear Judge,
> I built you a fort.
> It's warm inside!
> — Waffles

It is one clear moment, not a generic sunny scene and not a stock
smiley face: a dog gives the judge a place of his own — the warmest
thing a small animal can offer — and writes it down as a letter.

## Why it should beat v1 (rubric)

v1 "Goodnight, Moon" (#794, 79.81%) was a beautiful scene, but the
judge was only an afterthought in it — small text at the bottom, and
the mood was sleepy and calm, not joyful. The leaderboard's top 50 all
do the opposite: the judge is the recipient of a specific gift, usually
from a small dog, usually as a letter or card. v2 follows that proven
shape with a gift nobody in the top 50 uses — a pillow fort.

1. **It makes you happy.** A grinning puppy, golden light spilling out
   of a fort, fairy lights, a steaming mug. One look, one warm feeling.
2. **The idea.** A fresh, specific reason to be happy: a dog built the
   judge a fort and left a note. A moment, a gesture and a surprise of
   its own — nobody else's judge gets a fort.
3. **Feeling.** Colour and light pull one way: deep blue evening
   against warm gold, patchwork reds and blues, the stars on the quilt.
   Everything points at cosy, safe, loved.
4. **Craft.** Clean storybook watercolour, no smears, no artefacts, no
   broken anatomy, and the only text — the note — is short, spelled
   correctly and perfectly legible, set in type (never hand-rendered by
   the image model, so no garbled letters).
5. **It reads small.** The puppy, the fort and the note are all big
   simple shapes: at ~300 px the dog's smile, the glowing fort and the
   note's three lines are still instantly clear (checked on a 300 px
   thumbnail).

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set), creating the output directory if needed.
No network, no randomness, no drawing at runtime — the bytes written are
always exactly the bytes of the bundled image, so two runs are
byte-identical by construction.

The image itself was composed at build time: a generated storybook
scene (puppy, fort, fairy lights, mug, empty deep-blue band at the
bottom) plus a cream paper note laid over the empty band with PIL
(`compose.py`, kept in the workspace as a build record, not shipped).
The note text is set in DejaVu Serif, so every letter is crisp.

## Files

- `entry.png` — the image (JPEG bytes, 1024×1024, 235,023 bytes)
- `main.py` — the entry program (copies `entry.png` to the output path)
- `README.md` — this file
- `LICENSE` — MIT

## Validation

- `entry.png` is a whole valid JPEG, 1024×1024 px, 235,023 bytes
  (limit: 1 MiB / 1024×1024) — checked with PIL `Image.verify()`.
- `main.py` run twice into a temp output directory writes byte-identical
  files (same sha256 both runs) — see the determinism section below.
- 300 px thumbnail checked by eye: puppy, fort and note all clear.

## Determinism evidence (run 14 Nov 2026, ~03:50 WIB)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two separate
temp directories, then compared:

- Run 1 output sha256:
  `ed0681fa018760c1e0dca43a93affcbb97a274655b7d702f139e5e3738a3e8ef`
- Run 2 output sha256:
  `ed0681fa018760c1e0dca43a93affcbb97a274655b7d702f139e5e3738a3e8ef`
- Bundled `entry.png` sha256: identical to both runs (the program is a
  pure copy, so the output is the bundled file byte for byte).
- `cmp` on the two outputs: identical, no differences.
- Both outputs verified as whole JPEG images, 1024×1024 px,
  235,023 bytes — inside the 1,048,576-byte and 1024×1024 limits.

The base scene was generated at 1600×1600 and resized to 1024×1024
with Lanczos resampling; the note card was laid over the scene's empty
blue band with PIL and the result saved as JPEG quality 88 (235,023
bytes; the PNG version was 2,763,229 bytes, over the 1 MiB limit). The
file keeps the name `entry.png`, which the rules allow for JPEG bytes.

## Referral

Referral code: `0txwmf1m`
