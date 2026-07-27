# Track 5 — Claims & Delay Analysis · kickoff

Everything a fresh session needs before writing week one. Read this, then
`NOTES.md`, then `TRACK4-KICKOFF.md` §10 (traps). Do not start drafting until all
three are read: most of what follows was learned the expensive way.

---

## 0. Read in this order

| File | What it is |
|---|---|
| `TRACK5-KICKOFF.md` | this file — Track 5 only |
| `NOTES.md` | site-wide rules: numbers, cross-refs, copyright, voice, article shape, publishing. **§9 is the roadmap**; §8 is the Track 4 audit and its lessons apply directly here |
| `TRACK4-KICKOFF.md` | the previous track's kickoff. §10 (traps) and §9 (title conventions) are still current |
| `tools/canon.json` | machine-readable constants, arithmetic identities, forbidden values |
| `tools/check_site.py` | one command. `python3 tools/check_site.py` |
| `curriculum.js` | the single source of truth for every track's week list |

Run `python3 tools/check_site.py --quick` **before** you change anything, so you
know the baseline was green when you started.

Current state: 92 pages, Schedule 27/27 · Cost & Cash 24/24 · Risk 18/18 ·
Contract 20/20, zero broken links, zero 10-gram overlaps, cache `v90`.

---

## 1. What Track 4 hands over

Contract Week 20 ends by naming Track 5 explicitly. This is the promise you are
picking up — quoted so you match it rather than guess at it:

> Track 4 ends here. You can find the provision that governs, serve a notice that
> survives, keep records that make an entitlement provable rather than arguable,
> and follow the money from application to bank account. What none of that tells
> you is what the entitlement is worth. **Track 5 is Claims & Delay Analysis, and
> it starts exactly where this one stops: a preserved right, a programme that can
> be re-run, and the question this track has deliberately never answered — how
> much?**

Three things are handed over by that sentence, and Week 1 should open holding all
three:

- **a preserved right** — the notice was served in time, the records exist
- **a programme that can be re-run** — Track 1 built it, Contract W11 made it a
  contractual document
- **the question** — how much time, how much money

Also inherited, and worth re-reading before drafting: **Contract Week 8**
(*Building entitlement — before a claim exists*) and **Contract Week 9**
(*Extension of time — the contractual mechanism*). W9 is the direct predecessor:
it establishes the entitlement test and stops deliberately short of measuring it.

### The spine that runs through all five tracks

Track 4 Week 1 opened on it and Week 20 closed on it. Track 5 should land it:

> The rock was worth $48,450 and the contract said the ground was the employer's
> risk. The contractor paid for it anyway — because a site engineer sent an email
> that was never a notice, and nobody counted the days. Net margin on the job was
> $48,163.

Track 5's version of that story is the one where the notice *was* served, and the
argument moves to what it is worth. **That is the natural Week 1 hook** — same
job, same rock, but this time the right survived and the fight is about quantum.

---

## 2. Scope — and the boundary that matters

Track 4 and Track 5 were split out of a single planned track on 2026-07-20. Keep
the halves apart. The test, from `TRACK4-KICKOFF.md` §2:

> Track 4 is about **preserving** a right. Track 5 is about **valuing** one.
> If a draft week is arguing about how much, it belongs in 5.

Read that in reverse for this track: **if a draft week is arguing about whether
the right still exists, it belongs in 4 and is already written.** Do not re-teach
notices, time bars, records or the entitlement test. Link back instead — Contract
W8, W9, W10 carry them.

Territory that is Track 5's:

- forensic delay methodologies, and why they disagree
- as-planned vs as-built · impacted as-planned · collapsed as-built · time impact
  analysis · windows and time slices
- float ownership, and who consumes it
- concurrency — the hardest idea in the track
- disruption and productivity loss · the measured mile
- global claims and why they fail
- quantum: prolongation, thickening, head office overhead, finance
- assembling and presenting a claim that survives review

---

## 3. The source position — better than expected, with one real gap

**Correcting an earlier note:** an earlier session recorded that there was no
forensic delay material in `/mnt/user-data/uploads/`. That was wrong, and it was
based on the absence of the SCL Protocol rather than on measuring the books that
are there. Measured 2026-07-27:

| Source | Concurrency | TIA | Collapsed as-built | Measured mile | Productivity loss | Disruption |
|---|---|---|---|---|---|---|
| `7__Construction_Contract_Claims.pdf` | 101 | 9 | 8 | 38 | 35 | 64 |
| `8__Construction_Contract_Claims_Changes.pdf` | 28 | 6 | 6 | 2 | 3 | 31 |
| `3__International_Construction_Contract_Law.pdf` | 51 | 6 | 1 | 3 | 1 | 131 |

`7__Construction_Contract_Claims.pdf` is the primary text for this track —
measured mile at 38 mentions and productivity loss at 35 is real coverage, not
passing reference. `3__International_Construction_Contract_Law.pdf` carries
global claims (35) and float (125), and is the comparative-law angle.

**The real gap:** the **SCL Delay and Disruption Protocol** and **AACE RP 29R-03**
are not in the uploads as primary documents. They are *discussed* in the books
(SCL is referenced 19 times in the international law text, 4 in the claims text),
which is enough to describe what they say and to attribute it — but not enough to
quote them or to state their guidance as if read first-hand.

Handle it the way Contract W19 handled NEC4 with no NEC source: **write the
contrast, not the recitation.** The interesting article is why two competent
analysts using two accepted methods on the same facts reach different answers —
which needs the methods, not the protocol text.

Verify every methodology claim against the PDFs before publishing, exactly as the
FIDIC claims were. Nineteen FIDIC periods were checked for Track 4 and one was
wrong; assume the same rate here.

---

## 4. The $1M job — do not invent new numbers

Every track runs on the same fictional contract. It is fictional on purpose: it
lets the site use real engineering without touching any real project's
confidential data. Keep it that way — **no named projects, no real employers.**

| Constant | Value | Established in |
|---|---|---|
| Contract sum | $1,000,000 | `cost-week-1` |
| Measured work | $710,000 | `cost-week-3` |
| Preliminaries | $85,200 | `cost-week-4` |
| Escalation | $31,808 | `cost-week-4` |
| Controlled budget | $827,008 | `cost-week-4` |
| Contingency | $47,553 | `cost-week-5` |
| Management reserve | $50,000 | `cost-week-5` |
| PMB | $874,561 | `cost-week-5` |
| OH&P | $124,051 | `cost-week-6` |
| Net margin | $48,163 | `cost-week-22` |

**The rock has three different figures and they do not contradict each other:**

- **$24,000** — the register as written, EMV. Risk Week 6
- **$48,450** — the *conditional* figure, 17 of 42 piles at $2,850. Risk Week 5
  says explicitly there is no evidence either way for the north. **This is the
  number Tracks 4 and 5 inherit**
- **$34,323 / $33,875** — unconditional expectation at P(north) = 0.55. Risk
  Weeks 13 and 16

Full canon, plus 15 arithmetic identities and 8 forbidden values that must never
reappear, is in `tools/canon.json`. The forbidden list exists because a wrong
number once propagated across eight articles before anyone noticed.

**Track 5 will need new numbers** — prolongation rates, a measured-mile baseline,
a delay in days. Derive them from the canon rather than inventing them, and add
any that become load-bearing to `canon.json` with the identity that produces
them. The $1M job has 41 days of delay already in play (Contract Week 1: the
commercial manager found out 41 days later); check whether that is reusable
before choosing a different figure.

---

## 5. Voice

Track 1 is the house voice. Full table in `NOTES.md` §4. Track 4's measured
position, which Track 5 should sit near:

```
contractions   Schedule 25 · Cost & Cash 9 · Risk 7 · Contract 7  per 1,000
you            Contract body 18 · Practical insight 33  per 1,000
```

- **Practical insight is always direct second person.** `check_site.py` warns if
  it drops below half of Schedule's rate
- `it is` is deliberately never contracted site-wide
- Track 5 argues from documents, programmes and analysis, so writing *about the
  case* rather than *at the reader* is the natural register — with Practical
  insight pulling back to second person

**Article shape** (`NOTES.md` §5): h1 hook of 4–9 words → H2 repeating the h1 →
7–9 further H2s → 3 SVG figures → Practical insight → Key takeaways as seven ✔
lines → What's coming next → **1,370–1,550 words** (Track 4's settled band;
Track 4 ran 1,367–1,543).

Two title registers, and they do different jobs — see `TRACK4-KICKOFF.md` §9:

| | `curriculum.js` `title` | article `<h1>` |
|---|---|---|
| Job | says what the week covers | editorial hook |
| Example | `Extension of time — the contractual mechanism` | `Late is not the same as entitled.` |

85% of curriculum titles use `Topic — components`. A curriculum title that reads
like a headline is out of register, and a headline that reads like a syllabus
entry is a wasted h1. **Write both, deliberately, at the same time as the week
list.**

---

## 6. curriculum.js — adding TRACK5

Follow the existing schema exactly:

```js
const TRACK5 = {
  title: "Claims & Delay Analysis",
  totalWeeks: <n>,
  weeks: [
    // ---- PHASE A — <NAME> ----
    { phase: "Phase A — <Name>", n: 1,
      title: "<full title, shown on learn.html>",
      short: "<compact title, sidebar + breadcrumb>",
      status: "live", page: "claim-week-1.html", date: "<Mon D, YYYY>" },
    { n: 2, title: "...", short: "...", status: "upcoming" },
  ]
};
```

- `short` is what the reader sees in the sidebar **and** the breadcrumb. Keep it
  under ~45 characters
- Filename prefix: Track 1 is bare `week-N.html`, then `cost-`, `risk-`,
  `contract-`. **Pick the Track 5 prefix before writing week 1** and use it
  everywhere; renaming later means touching the sidebar, sitemap, chain and every
  cross-reference
- Three render families read each track — sidebar, home card, learn row. They are
  shared helpers (`sidebarHTML`, `homeCurriculumHTML`), so a new track needs a
  thin wrapper for each, **not a copy.** They were duplicated once and the same
  bug appeared in all three
- **Wire the badges to `badgeText()` immediately.** `learn.html` `t5ModuleBadge`
  and `index.html` `homeTrack5Badge` must read from `curriculum.js` via a
  `renderHomeTrack5Badge()` wrapper. Track 4's were hard-coded `In Progress` in
  the HTML and would never have flipped to Complete on their own — `NOTES.md` §6
  says not to do this and it happened anyway

### Track outcomes

An `After this track you can` block sits on `learn.html` under every published
track — six lines, second person, matching the Practical insight register.
**Write Track 5's at the same time as the week list**, not bolted on afterwards.

---

## 7. Publishing checklist

Full version in `NOTES.md` §6. Short form:

1. Build the page from the previous week's file as template. **Write the build
   script idempotently** — it will be run more than once, and a second run should
   be a no-op, not an error.
2. **Grep the new page for the previous track's name.** Every one of the 19
   published contract pages carried `MODULE 03 · RISK · WEEK 18` in the eyebrow,
   inherited from the `risk-week-18` template and never corrected. No JS
   overwrites it. That is what readers saw on every page of the track.
3. Add the week to `curriculum.js`.
4. Update the previous week's *What's coming next* and its next-article card.
5. Recompute the reading time — 225 wpm plus 15s per figure. It is hardcoded.
6. Bump the cache query strings — `curriculum.js?v=N` and `style.css?v=N` —
   across every page. Forgetting this is the single most common way a fix appears
   not to work.
7. Add the URL to `sitemap.xml` with a `lastmod`.
8. **`python3 tools/check_site.py` — full run, not `--quick`.** The copyright
   scan only runs on the full pass. A live 10-gram overlap sat published in
   `contract-week-9` because only `--quick` had been run since it went up.
9. Zip from inside the site directory.

---

## 8. Lessons from the Track 4 audit that apply directly

Full audit in `NOTES.md` §8. The three that will bite this track:

**Precise counts are the most dangerous sentence in an article.** Three of the
five audit findings were numbers nobody had ever counted — *"Red mentions the
Engineer 544 times"*, *"same five-letter word"* (the word was thirteen letters).
They read as authority and nobody re-derives them. Track 5 is full of temptations
of this shape: how many days of concurrent delay, what percentage of claims fail,
how much productivity a given factor costs. **If a claim is countable, count it
before publishing, or write the qualitative version instead.**

**Do not mirror a source's structure.** Two Track 4 passages tracked their clause
too closely — one ran four sentences through Silver's risk provisions in the
clause's own order, one listed 8.3's eleven contents in the clause's own
sequence. Both were rewritten. Track 5's risk is higher, because delay
methodologies come as numbered step lists and it is very easy to reproduce one.
Teach the method's *logic and failure mode*, not its steps in order.

**Re-measure after every fix, not just before.** The first rewrite of the Week 11
list introduced a *new* 8-word overlap of its own.

---

## 9. Material earmarked for Track 5

**The rock, fourth time.** Risk W14 (whose risk), Contract W13 (when the contract
says it is not a variation), Contract W16 (across the three books). Track 5's
version: the notice survived, the entitlement is established — now value it. This
is the strongest available Week 1, because the reader already knows every fact
and only the question is new.

**The 41 days.** Contract Week 1 establishes that the commercial manager found out
41 days after the event. That number is already canon and is a natural anchor for
a windows analysis.

**Contract W11's programme obligations.** The contract's view of the schedule —
deemed no-objection at 21 days initial and 14 on a revision — means an unobjected
programme *is* the Programme. That is the foundation of every as-planned
analysis, and it is already written. Link, do not repeat.

**Contract W19's NEC contrast.** Compensation events are assessed prospectively on
a forecast, not retrospectively on what happened. That is a genuinely different
answer to Track 5's central question and the article already exists to link to.

**Cost W15 productivity control** (factors, indices, earned hours) is the
quantitative base for disruption. Cost W13 covers change pricing including
disruption at a Track 2 level. Read both before drafting the disruption week —
the risk is repeating them rather than extending them.

---

## 10. Open site-wide items (not Track 5's job, but visible)

1. **Dates.** Published lessons carry future dates — the Track 4 finale is dated
   Mar 1, 2028. All are marked `live` and badged Complete, and the homepage puts a
   "New" badge on a future-dated article. Untouched because the owner's publishing
   calendar is unknown. **Ask before writing Track 5 dates**, or the new track
   inherits the same problem.
2. **"New lesson every week"** appears in six places while four tracks are
   complete and Track 5 is unwritten.
3. **Progress bars are dead UI** — all four read 100% because they measure
   *publication*, not reader progress. Track 5 will make them meaningful again
   while it publishes incrementally. A completion-ticking feature was discussed as
   the real fix: localStorage first, no login required. Nothing built, and there is
   no database — `auth.js` imports `firebase-app` and `firebase-auth` only.
4. **Track 1 never defines BAC**, though Schedule Weeks 17–21 teach PV, EV, AC,
   CPI, SPI and TCPI.
5. **Schedule Weeks 1 and 2 carry 14 H2s** against a median of 9.
6. YouTube link is still a `https://youtube.com` placeholder on every page.
7. `logo-lockup.png` (471 KB) is shipped but unused.
