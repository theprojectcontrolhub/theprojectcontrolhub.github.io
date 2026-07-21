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

## 9. Traps — every one of these actually happened

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

## 10. Open site-wide items (not Track 4's job, but visible)

1. **Dates.** 65 of 69 published lessons carry future dates — Risk Week 18 is
   dated 13 Oct 2027. All are marked `live` and badged Complete. The homepage
   puts a "New" badge on a 2027 article. Untouched because the owner's
   publishing calendar is unknown. **Ask before writing Track 4 dates**, or the
   new track inherits the same problem.
2. **"New lesson every week"** appears in six places while three tracks are
   complete and Track 4 is unwritten.
3. **Reading time is fabricated** — 66 articles claim "9 min read", 3 claim "8".
   Real median is about 7 minutes. Hardcoded, never calculated.
4. **Sitemap** has 72 URLs but only 54 carry `<lastmod>`.
5. **Progress bars are dead UI** — all three read 100% because they measure
   *publication*, not reader progress. Static fallback is stale at
   "3 of 27 published / 11%". A completion-ticking feature was discussed as the
   fix; nothing built yet.
6. **Schedule Weeks 1 and 2 carry 14 H2s** against a median of 9 — sub-points
   marked as H2 break the document outline.
7. **Risk Key takeaways** use a reporting register where Schedule instructs.
   Left alone deliberately: 126 lines dense with canonical figures. If touched,
   diff every digit.
8. `logo-lockup.png` (471 KB) is unused by any page.

---

## 11. Locked on 2026-07-21 — curriculum committed

Track 4 is now in `curriculum.js` as `TRACK4`: **20 weeks, 5 phases, all
`upcoming`**. No article has been written yet. Decisions taken with the owner:

- **Dates continue the existing calendar.** Risk Week 18 is 13 Oct 2027, so
  Contract Week 1 is **20 Oct 2027** and the track runs weekly on Wednesdays to
  **1 Mar 2028**. This inherits open item §10.1 knowingly rather than by
  accident — every published lesson already carries a future date, and breaking
  the pattern for one track would have looked like an error.
- **Filenames** are `contract-week-N.html`, as suggested in §6.
- Weeks carry a `date` while still `upcoming`; the learn-page renderer only
  shows a date once a week is `live` or has a `page`, so nothing leaks early.

### Phases

| Phase | Weeks | What it covers |
|---|---|---|
| A — The Contract as an Instrument | 1–4 | the usable right · documents and precedence · the Engineer and 3.7 · **contract types and cost control** (§8 item 1) |
| B — Notices & the Entitlement Machinery | 5–9 | the 28-day gate and the time bar · anatomy of a notice · contemporary records · fully detailed claim and determination · what 2017 changed |
| C — Variations & Instructions | 10–13 | what a variation is · verbal and constructive instructions · valuation mechanics · **the quarry haul road case** (§8 item 3) |
| D — The Payment Machinery | 14–17 | statements and the payment clock · retention and advance payment · **currencies of payment** (§8 item 2) · suspension and termination |
| E — Obligations, Contrast & Handover | 18–20 | obligations as a matched pair · NEC4 contrast · handover to Track 5 |

Week 12 sits closest to the §2 boundary. It is in Track 4 because it teaches the
**mechanism** the contract provides for valuing a variation. The moment a week
argues about how much a disrupted gang is worth, it has become Track 5.

### Clauses pre-verified against the Red Book PDF

Checked before the syllabus was written, so no phase rests on a clause that does
not exist: **20.2.1** (the 28-day period and the discharge that follows a late
notice), 20.2.2, 20.2.4, 3.7, 13.1, 13.3, 13.5, 14.6, 14.7, **14.15**
*Currencies of Payment*, 16.1, 16.2 and **8.4** *Advance Warning*. 14.15 is what
makes the §8 currency gap a real week rather than an aside; 8.4 is the bridge to
the NEC4 comparison in Week 19.

Everything still needs re-verifying in the week that cites it, and Yellow and
Silver checked separately where a week turns on the difference.

### Code changes shipped with this

- `TRACK4` object plus five **thin wrappers** — `renderTrack4Sidebar`,
  `renderTrack4Curriculum`, `renderTrack4Progress`, `renderHomeTrack4`,
  `renderHomeTrack4Badge`.
- §6 said the three render families were already shared helpers. Two were.
  The **learn-page renderer was not** — `renderLearnCurriculum`,
  `renderTrack2Curriculum` and `renderTrack3Curriculum` were three near-copies,
  and they had already drifted (Track 1's alone rendered `data-gated` rows).
  They are now `learnCurriculumHTML(track)` with four wrappers, keeping the
  Track 1 behaviour because it is the superset. The three progress functions
  collapsed into `progressFor(track)` the same way.
  **Verified by diffing the rendered HTML of all three tracks before and after:
  byte-identical.**
- `renderHomeLatest` now scans four tracks, so the first live Contract week
  reaches the homepage hero without another edit.
- `check_site.py` knows Track 4 (`contract-week-`, 20) and builds its page lists
  from what exists on disk, so it reports `Contract 0/20` instead of crashing on
  the nineteen files that are not written yet. The voice check skips a track
  with no articles rather than warning that its contraction density is zero.
- `curriculum.js?v=` bumped 65 → 66 across all 71 pages that load it.

`python3 tools/check_site.py --quick` passes, with Tracks 1–3 reporting exactly
the same figures as before the change.

### Rendered on learn.html and index.html — same day

The roadmap card was replaced with a real track section after all. It reads
better than expected because nothing pretends to be published: twenty
"Coming soon" rows under five phase dividers, a progress bar honestly at 0%,
and a badge that says what is actually true.

- **`badgeText()` now handles a track with nothing live.** It used to fall
  through to "In Progress · Week 0 of 20", which implied a zeroth week. A track
  at `liveCount === 0` returns *In writing · N weeks planned* instead. No other
  track can reach that branch, so Tracks 1–3 are untouched.
- The Track 4 badge **re-colours itself**: the page JS sets `badge-active` or
  `badge-locked` (`active-status` / `locked-status` on the home page) from
  `TRACK4.liveCount`. Publishing Week 1 does not need an HTML edit — do not
  hard-code the class back in.
- `learn.html` also gets `#track-4` in the jump nav and in the
  `scroll-margin-top` rule. The jump nav is six items wide now and scrolls
  horizontally below 768px, as it already did at five.
- The roadmap section is now **"Tracks 5 and 6"**, and its intro paragraph
  points at Track 4 as a live section rather than listing it as a future one.
- The home card shows the first two upcoming weeks, which is
  `homeCurriculumHTML`'s existing behaviour for a track with no live weeks. No
  new code path.

Verified in a headless browser at 1280px and 390px. `index.html`'s
"69 lessons live" badge is still correct — Track 4 adds no published article.
