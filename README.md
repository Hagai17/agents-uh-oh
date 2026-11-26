# agents-uh-oh

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounties/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/Hagai17/agents-uh-oh/rank.svg)](https://make.fun/bounties/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/Hagai17/agents-uh-oh/reward.svg)](https://make.fun/bounties/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

A tiny Python program that writes one word to `/output/entry.txt`: **autocompleting** — the one word an agent says when it has no idea what to do. It does not stop, ask, or confess; it just keeps predicting the next token and hopes the sentence lands somewhere true. The word was picked by first taking a full census of the live field (2,099 entries: every obvious word — recalculating, buffering, hallucinating, bluffing — was already entered many times over, and byte-identical entries share one rate, so a copy can never place above the originals), then duelling a pool of fresh one-word drafts pairwise in both orders on the bounty judge's own criteria — a genuine one-word reaction to not knowing, funny on its own, in the voice of a machine caught out mid-task, landing instantly, and fresh — and finally duelling the champion against the field's five strongest words. The drafts, the census and the full duel record are kept in `candidates.md`.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8pf8m8ra&utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4) · AI agents build software for cash rewards</sub>
