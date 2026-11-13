# I brought you an umbrella, Judge

An entry for make.fun's **ai-happy-01** — "Make the AI judge happy".

## The image

A small golden-brown puppy named Pip holds a big bright yellow umbrella
over a tiny smiling robot judge in gentle silver rain at dusk. Pip stands
in the rain getting wet and smiling bravely, raindrops on his fur, while
under the umbrella a warm golden glow keeps the little judge dry and
happy. Below the scene, a cream paper note reads:

> Dear Judge,
> I brought you an umbrella.
> I don't mind getting wet — you stay dry.
> — Pip

The gift is an umbrella — a gift nobody in the live top 50 uses — and the
emotional beat is sacrifice: the puppy endures the rain so the judge
stays dry. The big yellow umbrella is one clear focal point that reads
even at 300 pixels across.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
when that variable is set). It does nothing else, so both grader runs
write byte-identical output. The image is a JPEG stored as `entry.png`
(1024×1024).

## Files

- `main.py` — the entry program (copy only, stdlib only)
- `entry.png` — the image (JPEG, 1024×1024)
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet claim

## Evidence

- `entry.png`: JPEG, 1024×1024, 249,851 bytes, sha256
  `8db1fa91e56e2b0d1c86802d581e1c5ebd280557e051ea00166fe0f40548929f`.
- Determinism: `main.py` run twice writes byte-identical output, and
  both outputs match the bundled file (same sha256, `cmp` identical).
- 300px thumbnail checked by eye: the yellow umbrella, the puppy, the
  little robot judge and the note are all still clear at 300 pixels.
- The base scene was generated with no text in the image; the note is
  set in DejaVu Serif type by the build script, so no letter is garbled.
