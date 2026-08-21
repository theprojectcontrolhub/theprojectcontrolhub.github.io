# Track 8 kickoff — addendum, 2026-08-18

`TRACK8-KICKOFF.md` stands. Its scope, its reading of the printed handover and
its week list are unchanged by this. Two things need adding: one finding that
changes a decision in §3, and four site facts that moved after 12 August.

---

## 1. §3 understates the finishing phase, and the reason is the counting form

§3 calls Phase G *"the worst-sourced part of any track so far"* and puts six
weeks (29–34) on `commissioning` 42, `punch list` 27, `as-built` 49 and
`handover` 21 between them.

Re-measured 2026-08-18 across the eighteen readable sources:

| Term as §3 counted it | §3 | Re-measured | Same subject, other spellings |
|---|---|---|---|
| `handover` | 21 | 22 | **`taking over` 411 · `Taking-Over Certificate` 166** |
| `taking over` | 3 | 245 | — |
| `commissioning` | 42 | 122 | — |
| `punch list` | 27 | 36 | — |
| `as-built` | 49 | 225 | — |
| `defects liability` | — | 31 | **`defects notification` 85** |

**The handover subject is not thin. It is the best-sourced thing in Phase G.**
`Taking-Over Certificate` is a defined term in all three FIDIC books and runs
to 166 occurrences — 44 in Red, 46 in Yellow, 40 in *International
Construction Contract Law*. The whole taking-over mechanism, its conditions,
its partial forms and what it triggers is first-hand material sitting in books
already in the pool.

`defects liability` at 31 is the same shape: FIDIC 2017 calls it the **Defects
Notification Period**, and that phrase is 85.

**What still holds from §3, and it holds harder:** mechanical completion,
pre-commissioning, performance testing and demobilisation are genuinely
absent. This was re-checked against every alternative spelling before being
accepted:

```
mechanical completion     0        systems completion    0
mechanical acceptance     0        turnover package      0
ready for commissioning   0        RFC                   1
```

So Phase G splits in two rather than being uniformly weak:

- **Weeks 32–34** — taking over, defects, closeout, as-built, final account —
  are contract-sourced and can be written first-hand.
- **Weeks 29–31** — mechanical completion, pre-commissioning, performance
  tests — have nothing behind them and must be written from practice and
  labelled as such, or wait for the commissioning reference §3 names.

**And the method note this proves again.** §3 already caught two
spelling-driven zeros (`mobilisation`/`mobilization`, `punchlist`/`punch
list`). The same defect was still present in three more places, and one of
them inverted a judgement about six weeks of the track. `TRACK7-KICKOFF.md`
§3's rule is not a formality: **search hyphenated, closed and spaced, and
also search the term the contract actually uses.** A drafter's word for a
thing is rarely the industry's word for it.

**Caveat on comparability.** §3's numbers came from the full pool as it stood
on 12 August; these come from the eighteen sources with a readable text layer.
Several of §3's figures are *lower* than the re-measurement, which cannot
happen if the pools are nested — so the two are not measuring the same thing,
and the difference is the counting form rather than the corpus. Before any
week list is fixed on these numbers, run one measurement with one stated
method and record which form was counted.

---

## 2. Site facts that moved after 12 August

**`start-here.html` was repaired.** It had said *"Five tracks complete, 117
lessons published"* since Claims, together with *"the other four"* and *"those
four are"*. It now reads seven and 160, and the list of tracks that assume
Track 1 names all six. `tools/fix_start_here_counts.py` carries the change and
is idempotent.

**`tools/check_status_strings.py` is now in the repository** and is step 7 of
the publishing checklist. It catches what `check_site.py` cannot: a number
typed into HTML that `curriculum.js` also computes, with no JS rewriting it.
It currently reports `0 bayat dize, 0 yanlış künye tarihi`.

Two refinements went in with it, both worth knowing because they show what the
tool will and will not do:

- Its window narrowed from 200 characters to 60. At 200 it fired on
  `contract-week-1.html` — *"Take the register you built in Track 3 … Those
  five are the ones to work on now."* The five are risks. A status claim about
  tracks has the word adjacent, not a paragraph away.
- `index.html`'s *"Eight tracks, published one lesson a week"* is **exempt by
  name, with the reason recorded**: the site declares and renders eight, the
  eighth having no live weeks, and how many are *rendered* lives in page
  JavaScript rather than in `curriculum.js`. An exemption with a written
  reason keeps catching things; a loosened rule stops.

**The 25 wrong byline dates are fixed.** Every Reporting article after week 1
had carried week 1's date, inherited by the Track 6 build script. The checker
now reports zero.

**Eight repairs to Interfaces are in place**, all after publication and all
found by reading the articles against the sources rather than by any check:
one contradiction, three missing instruments the pool supplied, four record
corrections. `tools/fix_w*.py` and `tools/fix_record_measurements.py`.

---

## 3. One line to add to §7 of the kickoff

The publishing checklist ends at `check_site.py --quick`. Add:

```
7. python3 tools/check_status_strings.py
```

It is the only thing that catches a stale hand-written status string, and
`start-here.html` sat wrong for three tracks because nothing did.
