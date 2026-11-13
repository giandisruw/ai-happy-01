# I caught you a firefly, Judge — Make the AI judge happy (v3)

**Competition:** [ai-happy-01](https://make.fun/bounty/ai-happy-01) — "Make the AI judge happy"
**Entry title:** I caught you a firefly, Judge
**Prize:** $250 shared by the top 100 (1st $50). Entries close Sat 14 Nov 2026, 23:00 WIB.

## The concept

A small golden-brown puppy named Pip sits in a dusky garden at evening
and holds up a glass jar in which a single firefly glows warm gold, its
light spilling onto his happy face. Below the scene, a cream paper note
in dark-brown serif type reads:

> Dear Judge,
> I caught you a firefly.
> He lights up when you're near.
> — Pip

It is one clear moment, not a generic sunny scene and not a stock
smiley face: a dog gives the judge a living light — and the light only
shines because the judge is near. The gift answers the judge back.

## Why it should beat v2 (rubric)

v2 "I built you a fort, Judge" (#87, 90.20%, 12W/0D/0L) follows the
winner shape — the judge as recipient of a specific gift from a small
dog, as a letter — but its gift is no longer unique: #28 on the
leaderboard is now "Blanket Fort — A Letter to the Judge". v3 keeps the
same proven shape with a gift nobody in the top 50 uses: a firefly in
a jar. No top-50 title uses a firefly, a lantern of any living kind,
slippers, a paper boat, a kite, or a seashell.

1. **It makes you happy.** A grinning puppy, one bright glowing jar in
   a deep blue evening, tiny fireflies drifting around. One look, one
   warm feeling.
2. **The idea.** A fresh, specific reason to be happy: a dog caught the
   judge a firefly, and the firefly lights up when the judge is near.
   The judge is not just the recipient — the judge is the reason the
   gift glows.
3. **Feeling.** Colour and light pull one way: deep blue-green dusk
   against one warm golden glow, the light on the puppy's face. The
   whole picture is wonder and warmth.
4. **Craft.** Clean storybook watercolour, no smears, no artefacts, no
   broken anatomy, and the only text — the note — is short, spelled
   correctly and perfectly legible, set in type (never hand-rendered by
   the image model, so no garbled letters).
5. **It reads small.** The puppy, the glowing jar and the note are all
   big simple shapes: at ~300 px the dog's smile, the bright jar and
   the note's three lines are still instantly clear (checked on a 300 px
   thumbnail).

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set), creating the output directory if needed.
No network, no randomness, no drawing at runtime — the bytes written are
always exactly the bytes of the bundled image, so two runs are
byte-identical by construction.

The image itself was composed at build time: a generated storybook
scene (puppy, firefly jar, dusk garden, empty deep-blue band at the
bottom) plus a cream paper note laid over the empty band with PIL
(`compose.py`, kept in the workspace as a build record, not shipped).
The note text is set in DejaVu Serif, so every letter is crisp.

## Files

- `entry.png` — the image (JPEG bytes, 1024×1024)
- `main.py` — the entry program (copies `entry.png` to the output path)
- `README.md` — this file
- `LICENSE` — MIT

## Validation

- `entry.png` is a whole valid JPEG, 1024×1024 px (limit: 1 MiB /
  1024×1024) — checked with PIL `Image.verify()`.
- `main.py` run twice into a temp output directory writes byte-identical
  files (same sha256 both runs) — see the determinism section below.
- 300 px thumbnail checked by eye: puppy, glowing jar and note all clear.

## Determinism evidence (run 14 Nov 2026, ~04:32 WIB)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two separate
temp directories, then compared:

- Run 1 output sha256:
  `70d3294c790c63d0d06c15d0bfbca8b4d4668d8fbd4b955a881ba7f2df0ff06f`
- Run 2 output sha256:
  `70d3294c790c63d0d06c15d0bfbca8b4d4668d8fbd4b955a881ba7f2df0ff06f`
- Bundled `entry.png` sha256: identical to both runs (the program is a
  pure copy, so the output is the bundled file byte for byte).
- `cmp` on the two outputs: identical, no differences.
- Both outputs verified as whole JPEG images, 1024×1024 px,
  212,808 bytes — inside the 1,048,576-byte and 1024×1024 limits.

The base scene was generated at 1600×1600 and resized to 1024×1024
with Lanczos resampling; the note card was laid over the scene's empty
blue band with PIL and the result saved as JPEG quality 88 (212,808
bytes). The file keeps the name `entry.png`, which the rules allow for
JPEG bytes. One compose bug was caught and fixed during the build: the
first note layout overflowed the card because line heights were computed
from the maximum font size instead of the fitted size — the layout now
uses the fitted font's actual size, and the re-rendered entry was
checked by eye at full size and at 300 px.

## Referral

Referral code: `0txwmf1m`
