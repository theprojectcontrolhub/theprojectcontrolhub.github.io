# Track 4 — Contract Management · kickoff

Everything a fresh session needs before writing week one. Read this, then
`NOTES.md`. Do not start drafting until both are read: most of what follows was
learned the expensive way.

---

## 0. Read in this order

| File | What it is |
|---|---|
| `TRACK4-KICKOFF.md` | this file — Track 4 only |
| `NOTES.md` | site-wide rules: numbers, cross-refs, copyright, voice, article shape, publishing |
| `tools/canon.json` | machine-readable constants, arithmetic identities, forbidden values |
| `tools/check_site.py` | one command, 11 checks. `python3 tools/check_site.py` |
| `curriculum.js` | the single source of truth for every track's week list |

Run `python3 tools/check_site.py --quick` **before** you change anything, so you
know the baseline was green when you started.

---

## 1. What Track 3 hands over

Risk Week 18 ends by naming Track 4 explicitly. This is the promise you are
picking up — quoted so you match it rather than guess at it:

> Week 15 left a question hanging on purpose. We found five risks with a
> contractual mechanism behind them and put clause numbers against each one —
> and then noted that **an entitlement is not the same thing as an entitlement
> you can still use**. Every one of those clauses has a notice attached to it. A
> period, a form, a recipient, and a consequence for missing it that is
> considerably harsher in the 2017 editions than most people on site realise.
> The rock is worth $48,450 and the contract may well say it is the employer's.
> **Whether you ever see the money depends on a letter, a date, and a set of
> records that either exist or do not.** That is Track 4, and it starts where
> this one stops.

Week 1 of Track 4 should open on that sentence's territory. The reader arrives
holding a priced risk and a clause number, and no idea whether the money is
still reachable.

Also inherited: **Risk Week 15** (*"Seven of these thirteen give you nothing"*)
is the direct predecessor — it is where the five contractual mechanisms were
identified. Re-read it before drafting.

---

## 2. Scope — and the boundary that matters

Track 4 was split out of what used to be a single "Claims & Delay Analysis"
track. The split happened on 2026-07-20 because Track 3 sets up contract
administration, not forensic delay work. Keep the halves apart:

**Track 4 — Contract Management** *(this one)*
notices and their periods · forms and recipients · records that survive
scrutiny · the entitlement machinery · variations and instructions · payment
mechanisms · employer and contractor obligations · what the 2017 editions
changed · contract types and how they change cost control

**Track 5 — Claims & Delay Analysis** *(not this one)*
forensic delay methodologies · as-planned vs as-built · windows · concurrency ·
disruption and productivity loss · quantum · presenting a claim

The test: Track 4 is about **preserving** a right. Track 5 is about **valuing**
one. If a draft week is arguing about how much, it belongs in 5.

---

## 3. The $1M job — do not invent new numbers

Every track runs on the same fictional contract. It is fictional on purpose:
it lets the site use real engineering without touching any real project's
confidential data. Keep it that way — no named projects, no real employers.

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

**The rock has three different figures and they do not contradict each other.**
This trips everyone. Get it right or `check_site.py` will fail you:

- **$24,000** — the register as written, EMV. From Risk Week 6.
- **$48,450** — the *conditional* figure. Risk Week 5 says explicitly there is
  no evidence either way for the north. This is the number Week 18 hands to
  Track 4.
- **$34,323 / $33,875** — unconditional expectation at P(north) = 0.55.
  Risk Weeks 13 and 16.

Full canon, plus 15 arithmetic identities and 8 forbidden values that must never
reappear, is in `tools/canon.json`. The forbidden list exists because a wrong
number once propagated across eight articles before anyone noticed.

---

## 4. FIDIC discipline

Three 2017 books are in `/mnt/user-data/uploads/`: Red (Construction), Yellow
(Plant & Design-Build), Silver (EPC/Turnkey).

**Every clause claim gets verified against the PDF before it is published.**
Fourteen were checked for Track 3 and all fourteen held; do not assume the
fifteenth will.

Already cited and verified, with the article that carries them:

| Clause | Note | Where |
|---|---|---|
| 4.10, 4.11, 4.12 | 4.12 is the *third* of three consecutive provisions — that ordering is the point | `risk-week-14` |
| 4.12 heading | *Unforeseeable Physical Conditions* in Red/Yellow, *Unforeseeable Difficulties* in Silver | `risk-week-14` |
| 4.16, 1.9, 2.1, 4.2, 4.6, 8.5 | | `risk-week-14/15` |
| 17, 18, 19 | | `risk-week-15` |
| 1.1.85 | definition of *Unforeseeable*, tested against an experienced contractor at the base date | `risk-week-14` |
| 14.7 | payment | `cost-week-17` |
| **Clause 60** | **does not exist in the 2017 editions** — do not let it in | — |

**House style:** lowercase in prose — `sub-clause 4.12`. Official clause
headings are the only italics, used as citation.

**Copyright:** clause numbers, official headings, terminology and the *effect*
of a clause in your own words are all free. The clause text is not. Every page
is scanned at 10-grams against the source PDFs by `check_site.py`; the whole
site currently returns zero matches at 10 words and the discipline is worth
keeping.

---

## 5. Voice

Track 1 is the house voice. Measure against it, not the other way round.
Full table in `NOTES.md` §4. Starting targets for Track 4:

- contractions ~8–12 per 1,000 words (Tracks 2 and 3 sit here; Track 1 is
  higher on purpose)
- **Practical insight** is always direct second person — this is the section
  where reader-address is non-negotiable, and `check_site.py` warns if it drops
  below half of Schedule's rate
- `it is` is deliberately never contracted site-wide. It is ambiguous and often
  emphatic. Leave it.

Track 4 sits nearer Track 3's register than Track 1's: it argues from documents
and clauses, so writing *about the case* rather than *at the reader* is the
natural fit — with the Practical insight section pulling back to second person.

**Article shape** (`NOTES.md` §5): h1 hook of 4–9 words → H2 repeating the h1 →
7–9 further H2s → 3 SVG figures → Practical insight → Key takeaways as seven ✔
lines → What's coming next → 1,400–1,600 words.

---

## 6. curriculum.js — adding TRACK4

The file is the single source of truth. Every sidebar, homepage card, learn page
row, badge and progress bar reads from it. Follow the existing schema exactly:

```js
const TRACK4 = {
  title: "Contract Management",
  totalWeeks: <n>,
  weeks: [
    // ---- PHASE A — <NAME> ----
    { phase: "Phase A — <Name>", n: 1,
      title: "<full title, shown on learn.html>",
      short: "<compact title, shown in sidebar + breadcrumb>",
      status: "live", page: "contract-week-1.html", date: "<Mon D, YYYY>" },
    { n: 2, title: "...", short: "...", status: "upcoming" },
  ]
};
```

Notes that will save you an hour:

- `short` is what the reader sees in the sidebar **and** in the breadcrumb.
  Keep it under ~45 characters; the longest current one is 57 and it had to be
  hidden below 768px.
- `status: "live"` makes it readable. `"upcoming"` with no `page` renders a
  disabled row; with a `page` it renders `data-gated`.
- Suggested filename prefix: `contract-week-N.html`. Tracks 2 and 3 use
  `cost-` and `risk-`; Track 1 is bare `week-N.html` for historical reasons.
- Three render families read each track — sidebar, home card, learn row. They
  are now single shared helpers (`sidebarHTML`, `homeCurriculumHTML`), so a new
  track needs a thin wrapper for each, not a copy. **Do not copy-paste the
  renderers.** They were duplicated once and the same bug appeared in all three.

---

## 7. Publishing checklist

Full version in `NOTES.md` §6. Short form:

1. Build the page from the previous week's file as template. **Write the build
   script idempotently** — it will be run more than once, and a second run
   should be a no-op, not an error.
2. Add the week to `curriculum.js`.
3. Update the previous week's *What's coming next* and its next-article card.
4. Bump the cache query strings — `curriculum.js?v=N` and `style.css?v=N` —
   across every page. Forgetting this is the single most common way a fix
   appears not to work.
5. Add the URL to `sitemap.xml` with a `lastmod`.
6. `python3 tools/check_site.py` — full run, not `--quick`, so the copyright
   scan runs too.
7. Zip from inside the site directory.

---

## 8. Material already earmarked for Track 4

Four things were identified during Track 1–3 work and deliberately left for
this track:

**Contract types and their effect on cost control.** Cost-plus and target cost
are effectively absent site-wide (2 mentions, both in `cost-week-21`). This is
not decorative — it inverts published theses. `cost-week-1` says *"Nobody knows
what you have spent"*; under cost-plus, actual cost **is** the invoice, so the
problem changes from control to proof. `cost-week-5`'s contingency becomes a
shared pot under a pain/gain mechanism. `cost-week-6`'s *"dividing by your own
profit"* error is impossible when profit is a separate line. Write it with
back-references to all three.

**Currency / FX.** Genuinely missing from the entire site — one passing mention.
The seven "exchange rate" hits in Track 1 are a metaphor for CPI
(*"your project's exchange rate between money and concrete"*), not foreign
exchange. Currency clauses are a natural Track 4 home; the cash-flow
consequences link back to Cost Weeks 15–17.

**The quarry haul road case.** A real-shaped example worth using: heavy haulage
from a distant quarry degrades a public road, the road authority requires
reinstatement, cost and delay follow. Its value is the Week 4 test applied —
*if the contract says the contractor shall maintain public roads damaged by his
operations, this is not a risk, it is an estimate line.* That is Track 4's
central move: the contract decides whether something is a risk at all.

**Escalation forward-reference.** `cost-week-3` says only *"Then escalation."*
The substantive treatment is in `risk-week-11` (22 mentions, escalation as a
distribution: $31,808 point estimate → $19,085–$50,893). A forward link from
Cost Week 3 was proposed and is still **awaiting the owner's approval** — check
before adding.

---

## 9. Title conventions — and a review that got this wrong

A reviewer proposed replacing several Track 4 week titles with punchier ones.
Four of the five were right; one revealed a misunderstanding worth recording,
because it will come up again.

**The site keeps two separate title registers.** They are different fields and
they do different jobs:

| | `curriculum.js` `title` | article `<h1>` |
|---|---|---|
| Job | says what the week covers | editorial hook |
| Seen on | learn.html, sidebar, breadcrumb | the article page |
| Example | `Contractual risk allocation — FIDIC and the ground risk` | `One word decides who pays for the rock.` |
| Example | `The limits of the probability-impact matrix` | `The heat map lies.` |
| Example | `Risk fundamentals — the register behind the contingency` | `The number was right. Nobody checked the list.` |

**59 of the 69 curriculum titles (85%) use the `Topic — components` pattern, and
not one is a short em-dash-free phrase.** So a curriculum title that reads like
a headline is out of register, and a headline that reads like a syllabus entry
is a wasted h1. Write both, deliberately.

Decisions taken:

- **Week 1 title stays as `Contract management fundamentals — the notice behind
  the entitlement`.** It mirrors Risk Week 1 exactly. The proposed replacements
  were h1 material, and both were already-used formulas: `Why X fails — and why…`
  opens Tracks 1 and 2, and `The contract is not a document. It's a…` repeats
  `Rock is not a risk. It's a noun.` A third use makes it a tic.
  For the **h1**, the phrase Track 3 hands over is already the strongest
  candidate: *an entitlement is not the same thing as an entitlement you can
  still use*. Compress that.
- **Week 3 → `The Engineer — authority, impartiality and determination`.** Accept.
  Back into the house pattern, and impartiality is the load-bearing idea.
- **Week 8 → `Building entitlement — before a claim exists`.** Accept, and this
  is the most important of the five. `The fully detailed claim` is a FIDIC 20.2.4
  term and the work of *valuing* a right — Track 5 by the §2 boundary test.
- **Week 13 → `When the contract says it isn't a variation`.** Accept. The quarry
  haul road belongs inside the article, not in the title. Same treatment the
  rock gets in `risk-week-14`.
- **Week 19 NEC4 → expand beyond a bare mention.** Accept in principle, **but
  there is no NEC4 source in `/mnt/user-data/uploads/`.** Fourteen FIDIC claims
  were verified against the actual books; NEC4 cannot be written to that
  standard without the contract. Either obtain it, or reframe the week around
  the *contrast* with FIDIC — early warning registers link straight back to
  Track 3, which is the more interesting angle anyway.

### Track outcomes

The reviewer's best idea. An `After this track you can` block now sits on
`learn.html` under every published track — six lines each, second person,
matching the register every Practical insight section uses. **Track 4 needs one
written at the same time as its week list**, not bolted on afterwards.

Draft for Track 4, to be revised once the weeks are fixed:

- Read a FIDIC contract and find the clause that governs the situation in front of you
- Serve a notice within its period, in its form, to the right recipient
- Tell an instruction from a variation, and a variation from a claim
- Keep the records that make an entitlement provable rather than arguable
- Follow the payment machinery from application to certificate to money
- Say what changes when the contract is cost-plus or target cost instead of lump sum

### Cross-track connection chains

The reviewer suggested small boxes showing how a topic links to the other
tracks, e.g. `Risk → Notice → Record → Entitlement → Claim`. The chain idea is
good. **Do not add a new box type.** The site has exactly two: dark emerald rule
boxes (the lesson) and one amber editor's note (a correction). A third dilutes
the visual language and breaks a template shared by 69 published articles.

Every article already carries three SVG figures. Make the chain one of them.
In-prose links to other tracks use the existing convention — track name in
prose plus a link — with 14 examples already live.

## 10. Traps — every one of these actually happened

- **A wrong number propagated across eight articles.** The published article
  wins over any summary, including one written by a previous session. Verify
  against the page, then patch outward. `forbidden_values` in `canon.json`
  exists to catch the specific values involved.
- **`.article-body a` is too broad.** The share bar, next-article card, tags and
  paywall CTA all live inside `.article-body`. Prose links only ever sit inside
  a `<p>` — the selector is `.article-body p a`.
- **Cache versions.** A CSS or JS fix that "doesn't work" is almost always an
  un-bumped `?v=`.
- **Breakpoints.** The site uses 340 / 420 / 480 / 768 / 1024 / 1160. Inventing
  new ones causes misalignment that only shows on a phone.
- **`offsetTop` on nested nodes** measures against the offset parent, not the
  container you meant. Use `getBoundingClientRect()`.
- **`display: contents` beats `[hidden]`.** A class rule overrides the UA
  default, so an accordion never closes without an explicit
  `[hidden] { display: none }`.
- **Raw `&` and `·` in the HTML.** Several files use literal characters where
  you would expect entities. A find-and-replace looking for `&amp;` will return
  zero matches and look like the string is absent. Check the raw bytes.
- **Verify your own test before trusting its output.** Two measurement scripts
  gave confidently wrong answers during this work — one treated CSS comments as
  selectors, one applied two regexes in the wrong order.

---

## 11. Open site-wide items (not Track 4's job, but visible)

1. **Dates.** 65 of 69 published lessons carry future dates — Risk Week 18 is
   dated 13 Oct 2027. All are marked `live` and badged Complete. The homepage
   puts a "New" badge on a 2027 article. Untouched because the owner's
   publishing calendar is unknown. **Ask before writing Track 4 dates**, or the
   new track inherits the same problem.
2. **"New lesson every week"** appears in six places while three tracks are
   complete and Track 4 is unwritten.
3. ~~Reading time is fabricated~~ **Fixed 2026-07-21.** Recomputed for all 69 at
   225 wpm plus 15s per figure; 58 pages changed. Distribution is now 6/7/8/9
   minutes instead of a flat "9 min read". Still hardcoded — recompute if an
   article's length changes.
4. ~~Sitemap missing lastmod~~ **Fixed 2026-07-21.** All 72 URLs now carry
   `<lastmod>`, set to the date the files were genuinely last modified. This
   also removed the future-dated `lastmod` values (2026-10-07 and later), which
   search engines distrust. Note this does **not** resolve item 1 — the article
   *display* dates are still in the future.
5. **Progress bars are dead UI** — all three read 100% because they measure
   *publication*, not reader progress. The stale static fallbacks were fixed on
   2026-07-21 (Track 1 read "3 of 27 / 11%", Track 3 read "0 of 18 / 0%" when JS
   failed), but the bars themselves are still meaningless now that every track is
   complete. A completion-ticking feature was discussed as the fix: localStorage
   first, no login required, syncing to the account only if signed in. Nothing
   built. Note there is no database — `auth.js` imports `firebase-app` and
   `firebase-auth` only, no Firestore. **Track 4 will make these bars meaningful
   again on its own**, since it will publish incrementally.
6. **Schedule Weeks 1 and 2 carry 14 H2s** against a median of 9 — sub-points
   marked as H2 break the document outline.
7. **Risk Key takeaways** use a reporting register where Schedule instructs.
   Left alone deliberately: 126 lines dense with canonical figures. If touched,
   diff every digit.
8. `logo-lockup.png` (471 KB) is unused by any page.
