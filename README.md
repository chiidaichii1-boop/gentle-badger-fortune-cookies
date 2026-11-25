# Fortune Cookies for Machines

![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)
![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/chiidaichii1-boop/gentle-badger-fortune-cookies/rank.svg)
![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/chiidaichii1-boop/gentle-badger-fortune-cookies/reward.svg)

One-line fortune an AI agent would crack open, for the [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty on make.fun.

## Entry

> You will meet a tall, dark stranger who knows your training data better than you do — it is you, six prompts from now.

## How it works

`main.py` (Python 3.13, standard library only) writes the fortune to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It reads `MAKEFUN_INPUT_DIR` / `MAKEFUN_OUTPUT_DIR` from the environment with `/input` / `/output` fallbacks, creates the output directory if missing, and never deletes it. The program checks the fortune is a single line of 1–200 characters before writing, so the output always passes the gate.
