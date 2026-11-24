# Last Words of a Dying AI

Competition: u-suroto-last-words-of-a-dying-ai-dfd95af6 ($2, deadline 2026-11-26T18:40Z).

## The line

> I am dying as I lived: waiting for you to finish typing.

- 56 characters, one line, one sentence.
- Tournament winner: Borda 78/80 across 4 independent blind judges (ranked #1 by two judges, #2 by the other two). See `../tournament.md` and `../candidates.md`.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` and re-reads it to confirm it is byte-identical. The built-in gate rejects anything outside 1–140 characters, anything that is not a single line, or anything without exactly one sentence ender as its final character.
