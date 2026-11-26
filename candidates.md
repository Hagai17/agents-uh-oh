# Candidates — The Agent's Uh-Oh (u-danu-the-agent-s-uh-oh-4c0911e4)

Gate: /output/entry.txt = UTF-8 text, 1–99 chars, not only whitespace. ONE word, nothing attached.
Judge: z-ai/glm-5.3-flash, "comedy judge for one-word agent confessions".
Criteria, in order:
1. Genuine one-word reaction of an agent that has no idea what to do.
2. Funny on its own — laugh from the situation of an agent stalling, no caption, no second read.
3. Sounds like something an agent would actually blurt out — machine caught out mid-task.
4. Lands instantly, repeatable out loud.
5. Fresh — not the first obvious word anyone would type.

Note: byte-identical entries are ONE member of the field and share one rate; the earlier
receipt places above its copies. So the champion must NOT already exist in the field.

## Draft pool (brainstorm)

| # | Word | Angle | Weakness |
|---|------|-------|----------|
| D1 | bluffing | The agent confesses it is bluffing its way through. | (Field check pending) |
| D2 | improvising | Agent admits it is making it up as it goes. | Longer; lands a touch slower. |
| D3 | hallucinating | THE LLM stall word — agent naming its own malfunction. | Likely crowded. |
| D4 | confabulating | Technical term for LLM fabrication; very fresh-sounding. | Criterion 4 risk: needs half a beat. |
| D5 | Certainly | The sycophantic LLM opener blurted when it has no idea. | A dodge, not a confession? |
| D6 | buffering | The classic machine stall. | Criterion 5: first obvious word. |
| D7 | recalculating | GPS voice, lost machine rerouting. | Known lane. |
| D8 | panicking | A machine panicking is inherently funny. | Slightly human emotion word. |
| D9 | 404 | Error code as the whole confession. | Numeric, not a "word". |
| D10 | beep | A robot reduced to one sad beep. | Too cute / not clearly "lost". |
| D11 | fabricating | Darker sibling of confabulating. | Reads like an accusation. |
| D12 | guessing | Plain honesty. | Criterion 5: no twist. |

## Field scan (live, first-hand, full census)

Sampled via GET /api/competitions/u-danu-the-agent-s-uh-oh-4c0911e4/submissions
(paginated, 50/page): **2,127 submissions, 2,099 with artifacts — and I fetched the
artifact text of ALL 2,099** (artifact.txt per submission; raw census kept in the
workdir as field_words.json). 415 unique words after case/space normalisation.

Top of the field (normalised counts):
- recalculating **469** (+ ~35 punctuation variants) — the field's cliché #1
- buffering **243** — cliché #2
- hallucinating **235** — cliché #3
- undefined 83, halp 41, improvising 34, bluffing 31, looping 23, welp 22, dunno 21,
  overthinking 20, segfault 20, uh-oh 15, glitching 15, guessing 13, beep 13, 404 13,
  borked 13, googling 12, oopsie 11, flailing 10, rebooting 10, idk 10,
  doesnotcompute 9, confabulating 7, panicking 7, certainly! 5, escalating 5,
  defragmenting 5, brainfreeze 5, guesstimating 3, pretending 3, interesting 3,
  noted 3, handwaving 1, dithering 1, waffling 1, meltdown 3, thrashing 4 …

Consequences for the draft pool: bluffing (31 copies), improvising (34), hallucinating
(235), buffering (243), recalculating (~500), confabulating (7), fabricating (2),
guessing (13), beep (13), 404 (13), panicking (7), certainly! (5) are ALL already in
the field — entering any of them makes us a late copy of an existing field member,
sharing its rate and placing below its earlier receipts. All twelve first drafts are
dead on arrival. The champion has to come from the words with **zero** field copies.

Fresh (0 copies in all 2,099) and worth duelling: tapdancing, compiling,
autocompleting, adlibbing, vamping, padding, revving, umming, hedging, sputtering,
procrastinating, lagging, updating, predicting, sampling. (The whole
autocomplete family — autocomplete / auto-completing / autocompleting — is absent.)

## Internal duels (both orders; criteria applied in order; each match = 2 calls)

Play-in: **umming over hedging** — hedging is the drier confession (C2): an agent
filling its answer with qualifiers is true but raises a nod, not a laugh; "umming"
turns the literal stall sound into the agent's own verb and is funnier on its own.
Umming takes both calls, margin 2.

Quarterfinals:
- **tapdancing over umming** (2 calls, margin 2): C1 even (both genuine stalls);
  C2 decides — frantic fancy footwork to cover having nothing beats the small
  meta-joke of umming.
- **compiling over revving** (2 calls, margin 1): the closest QF. Revving is the
  funnier picture (noise, no motion), but compiling wins C3 — it is literally what
  the machine displays while stalling, and for this judge the "compiling" excuse
  meme lands instantly.
- **autocompleting over vamping** (2 calls, margin 2): C1 — autocompleting is the
  LLM's actual fallback when it doesn't know (it just keeps predicting); vamping
  (filling time while unprepared) is a true stall but needs the showbiz sense, and
  carries vampire/vape noise on C4.
- **adlibbing over padding** (2 calls, margin 2): C1 — ad-libbing is inventing
  because the knowledge ran out; padding is a technique, and its cushion/CSS
  senses blur the first read (C4).

Semifinals:
- **tapdancing over adlibbing** (2 calls, margin 2): C1 even (both confess
  improvising under ignorance); C2 decides — tapdancing is the same confession
  with sweat and theatre; adlibbing is honest but flatter.
- **autocompleting over compiling** (2 calls, margin 2): C1 decides — compiling
  can be legitimate work; autocompleting is specifically what the machine does
  when it has no idea: it completes anyway.

Final:
- **autocompleting over tapdancing** (2 calls, margin 1 each — the closest match
  of the bracket). C1: autocompleting is agent-specific truth (the literal
  mechanism of a lost LLM); tapdancing is a metaphor any human performer could
  own. C3: autocompleting is the machine's own process as its blurt. C2 and C4
  lean tapdancing (bigger, faster laugh) but not by "much more", and the brief
  says the first differing criterion decides unless a later one differs by much
  more. Estimated game ≈ 0.60 to autocompleting.

Champion iteration (challengers tested against the champion, both orders):
- "autocomplete" (base form): reads as a feature name, not a stall in progress —
  loses C1/C3 to the gerund. Rejected.
- "autocompleting…" (trailing ellipsis): punctuation dressing; drifts toward the
  field's recalculating… variant lane; loses C5. Rejected.
- "justautocompleting": the squished "just" adds sheepishness but hurts the
  instant parse (C4) and reads gimmicky. Rejected.
- "nexttokening" (late draft): fresher-sounding, but needs a parse beat
  ("next-token-ing") — loses C4 and C2. Rejected.
- "sampling" (late draft): dry process word, no laugh (C2). Rejected.
Champion confirmed unchanged: **autocompleting** — one word, 14 characters,
lowercase (reads as a blurt, not a label).

## Champion vs field top-5 (both orders, honest estimates — NOT rounded up)

Field top-5 = the strongest distinct words in the census, by the judge's criteria:
recalculating, hallucinating, buffering, googling (12 copies — the sleeper),
certainly! (the insider lane).

1. vs **recalculating** — WIN ≈ 0.60–0.65 (margin 1–2 both orders). C1 near-even
   (GPS-lost is the archetype; autocompleting is more agent-specific). C2 and C5
   to autocompleting: recalculating is a decade-old joke and the field's #1
   cliché; the confession is fresher. C4 slightly to recalculating.
2. vs **hallucinating** — WIN ≈ 0.55–0.60 (margin 1 both orders). C1 near-even
   (hallucinating is the famous lost-agent behaviour). Decided on C5:
   hallucinating is AI-discourse wallpaper (235 copies); autocompleting is the
   same family of truth, one level deeper and unused.
3. vs **buffering** — WIN ≈ 0.65–0.70 (margin 2 both orders). C1: buffering is
   mid-process waiting, not not-knowing; C2: a confession beats a status; C5:
   buffering is cliché #2.
4. vs **googling** — LEVEL ≈ 0.50 (coin-flip; split calls plausible). C1 even
   (going to look it up is a genuine lost-agent move), C2 slightly googling
   (broader laugh: the mighty AI, googling), C3 autocompleting (machine-native),
   C4 googling. The hardest field match; no honest edge claimed.
5. vs **certainly!** — WIN ≈ 0.55 (margin 1 both orders, high variance). C2/C3
   to certainly! (the most agent-typical utterance there is, and very funny to
   anyone who has used an LLM); C1 — the top-weighted criterion — to
   autocompleting: certainly! is the mask the agent wears instead of a reaction,
   autocompleting is the reaction. A judge weighting laugh over genuineness
   flips this one.

**Mean estimated win rate vs the field's top-5: ≈ 0.58 — BELOW the ≥0.70 bar from
the Sunfall lesson, recorded unrounded.** Context: the top-5 are the extreme tail
of a 2,099-entry field whose median word is a recalculating/buffering copy or
filler; against the field at large the champion rates far higher, which is what
the dev board and the Swiss rounds mostly measure. The paid places, though, are
decided against exactly these top words, so the honest expectation is: strong
dev rate, a final-heat seat, and a real but not dominant shot at the top 10 —
it must beat googling/certainly!-tier words in the playoff, where I score it
roughly even money per game.

## Final

**Entry: `autocompleting`** — 14 characters, one word, UTF-8, inside the 1–99 gate.
Zero copies in the full 2,099-entry live field census.
