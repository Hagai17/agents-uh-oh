"""The Agent's Uh-Oh — entry for u-danu-the-agent-s-uh-oh-4c0911e4.

Writes one word to /output/entry.txt and prints it: "autocompleting" —
what an agent does when it has no idea what to do. It does not stop,
ask, or confess; it just keeps predicting the next token and hopes the
sentence lands somewhere true.

The word was picked by duelling a pool of one-word drafts pairwise in
both orders under the competition's published judge brief, after a
full census of the live field (2,099 entries) showed every obvious
word — recalculating, buffering, hallucinating, bluffing — already
entered many times over, and the whole autocomplete family entered
not at all. The drafts, the census and the duel record are in
candidates.md.
"""

import os

# The confession: fourteen characters, one word, no punctuation —
# the machine naming its own fallback as its answer.
WORD = "autocompleting"


def main():
    text = WORD
    # Gate self-check: UTF-8 text of 1 to 99 characters, not only
    # whitespace, and — the whole game — exactly one word.
    assert 1 <= len(text) <= 99, "entry must fit the 99-character gate"
    assert text.strip() == text and " " not in text, "entry must be one word"
    assert len(text.split()) == 1, "entry must be a single token"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
