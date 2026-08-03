# The Project Control Hub — working notes

Conventions that are easy to lose between sessions. Everything here is enforced
by `tools/check_site.py` unless marked *(judgement)*.

```bash
SOURCE_DIR=<extracted sources> python3 tools/check_site.py    # full, incl. copyright scan
python3 tools/check_site.py --quick                           # skip copyright (much faster)
```

Run it after any content change. It exits non-zero on failure.

`SOURCE_DIR` was added 2026-07-27. `uploads/` is read-only, so sources arriving in an
archive cannot be put there; point `SOURCE_DIR` at wherever they were extracted. The
scan now reads `.pdf`, `.pptx` and `.docx`, and **fails loudly when it finds no sources
at all** — it used to return "kaynak PDF yok, atlandı" and let the run exit 0, which is
a green light with the gate switched off.

---

## 1. Numbers

**`tools/canon.json` is the source of truth.** Never cite a recurring figure from
memory, and never from a conversation summary. If a number is not in canon.json,
open the article that established it and read it there.

This rule exists because of a specific failure. On 2026-07-19 the session context
was compacted, and the summary that survived carried a numeric table that was wrong
about the Track 3 risk register. Six articles (Risk 11–18) were written on top of it
before anyone checked against the published Risk Week 8. The corrections were:

| | published in error | correct |
|---|---|---|
| 14-risk total | $116,913 | **$99,730** |
| 13-risk total (ex steel) | $101,913 | **$84,730** |
| epistemic group | 7 risks / $67,563 | **9 risks / $63,880** |
| rock expected value | $41,183 | **$24,000** |
| northern investigation | 3 boreholes | **2 boreholes** |

All five are now in `forbidden_values` in canon.json. If any reappears the checker
fails loudly, because a prose reminder would not have stopped it the first time.

**The rock has three legitimate numbers.** They are not a contradiction and the
checker will not flag them, so know which one a sentence means:

- **$24,000** — what the register carried (40% × $60,000), Risk Week 6
- **$48,450** — what the evidence supports, *conditional* on the southern ratio
  holding across the north (17 of 42 piles × $2,850), Risk Week 5
- **$34,323 / $33,875** — the unconditional expectation once P(rock extends
  north) = 0.55 is applied, Risk Weeks 13 and 16


**Second correction, closed 2026-07-20.** Schedule Week 20 forecasts the overrun
as `1,000,000 / CPI`. That million is the tender sum &mdash; a selling price with
head office overhead, profit and the $50,000 management reserve inside it. By the
site's own Cost & Cash Week 5 the reserve sits *above* the baseline and the PMB is
$874,561, so it cannot be the BAC; and Cost & Cash Week 6 shows that dividing
invoices by a selling price flatters the efficiency, which makes the published
0.79 generous and the 267k overrun the gentle version.

The body prose of Week 20 was **not** rewritten &mdash; the method it teaches is
correct and the numbers are internally consistent. Instead there is a dated
editor's note after the forecast section pointing at Weeks 5 and 6, and the
`learn.html` Track 1 &rarr; 2 bridge note now names both corrections rather than
just the actual-cost one.

---

## 2. Cross-references

A bare **"Week 12"** always means the current track. That is safe because every
article's sidebar already lists its own track's weeks.

A reference to another track is **always** named in prose and **always** linked:

```html
<a href="cost-week-5.html">Cost &amp; Cash Week 5</a>
```

Not `Week 5 (Cost)` — the prose form was already established in Track 3 and reads
better. Not the article title inline — too heavy mid-sentence.

Body prose carries links for nothing else. `.article-body a` in `style.css` keeps
the text colour and adds an emerald underline, so the twelve cross-track links do
not turn the page into a hyperlink field.

The checker compares every bare forward reference against the same-numbered
article in all three tracks and warns if another track fits the surrounding
sentence noticeably better.

**Never number a forward reference inside your own track.** Backward references are
numbered and linked; forward ones are named. Write *"the concurrency week later in this
track"*, not *"Week 16"*. Two reasons, and the second is the one that bites. The page
does not exist yet, so the checker warns on every build. And week numbers move: inserting
the site-record week at position 6 shifted twenty-two weeks by one, and a published
article saying "Week 16" would have quietly become wrong with nobody touching it. This
was violated three times during Track 5 and caught three times by the checker; the build
scripts now assert against it before writing.

---

## 3. Copyright *(partly judgement)*

Sources: three FIDIC 2017 books (Red, Yellow, Silver — full conditions, not
commentaries), Keane & Caletka *Delay Analysis in Construction Contracts* 2e, two NEC
books, *Construction Contract Claims*, *International Construction Contract Law*, PMI
risk standards, PMBOK 8, Cooper, four academic texts — plus, from 2026-07-27, a third
party's 59-deck training course and four course-transcript `.docx` files.

**The course material is reference-only and the highest overlap risk on the site.**
Verbatim spoken English, plain phrasing, and squarely on Track 5's subject. It is in
the n-gram pool for exactly that reason. Its lesson ordering is not to be followed —
its Lessons 29–36 run the delay methods in almost the sequence Track 5 proposed
independently, which is convergence on the field's standard taxonomy, not borrowing,
but it means the sequence now has to be defensible on its own terms.

**Free to use:** clause numbers; official clause headings in italics as a citation
(*Unforeseeable Physical Conditions*); the effect of a clause in our own words;
terminology; attributed findings; anything about our own invented $1M job.

**Never:** a quotation of any length from a source; redrawing a source figure;
following a source's teaching order or chapter sequence; carrying a numeric
example across.

The working test: write the sentence from memory with the source closed.

`check_site.py` scans every article against a 10-gram pool built from the sources.
Current state: **114 sources, 1.78M 10-grams, zero 10-word overlaps across 117 articles.**
Twelve sources are skipped for having no text layer (scanned PDFs); the run warns.

**Run the full scan, not `--quick`, before every zip.** On 2026-07-26 the full run
found three live 10-word overlaps in `contract-week-9.html` — the opening of 8.5,
published and unnoticed because only `--quick` had been run since that article went
up. The six-word term of art was kept and the sentence around it rewritten. A
quick run is for working; a full run is the gate. The longest overlaps anywhere are
seven words, and each is either a term of art, a legal definition that cannot be
paraphrased away (the *Unforeseeable* test in 1.1.85), or ordinary English.

**Track 5 record: the gate fired seven times, all before publication.** Every one was
the same mistake — a definition or a stated principle written straight from the source
because it was already phrased as well as it could be. The list is worth keeping,
because it is a list of the sentences most likely to be copied without noticing:

| Week | What was reproduced |
|---|---|
| 3 | the *Unforeseeable* definition, and three Silver clause headings run consecutively |
| 8 | the trigger condition for a revised programme in 8.3 |
| 11 | the Protocol's core principle about assessing close to the event |
| 12 | a phrase about the critical path moving month to month |
| 18 | the sentence on not being required to spend money mitigating |
| 19 | the definition of disruption |
| 22 | the opening of the five-part total cost burden |
| 25 | the claim certification wording |

The pattern: **the better a source phrases something, the more likely it is to survive
into your draft unaltered.** Definitions, tests and stated principles are the danger.
Narrative and argument almost never overlap, because those get rebuilt anyway.

Nothing here is legal advice. If a real question arises, ask a lawyer.

---

## 4. Voice *(judgement)*

Track 1 is the house voice. Tracks 2 and 3 are measured against it, not the
other way round.

Measured across all body prose, per 1,000 words:

| | Schedule | Cost & Cash | Risk |
|---|---|---|---|
| contractions | 29 | 12 | 10 |
| "you / your" — body | 27 | 26 | **12** |
| "you / your" — Practical insight | 51 | 51 | 36 |
| "you / your" — Key takeaways | 22 | 13 | **7** |
| avg sentence (words) | 10.7 | 13.7 | 13.2 |
| avg paragraph (words) | 24 | 35 | 31 |
| sentences opening And/But/So | 9.4% | 7.4% | 6.4% |

**Two of these gaps are deliberate. One is not.**

*Deliberate — leave it.* Track 3's body prose is written **about the case study**
where Track 1 is written **to the reader about their own job**. Compare:

> Schedule: "It goes to **your** board. It goes into the forecast."
> Risk: "A single number in that column is not an estimate of the impact."

Risk keeps every rhythmic device Track 1 uses — fragments, repetition, em-dash,
short declaratives in sequence — and points them at the evidence instead of at
the reader. That is a coherent register for the analytical track, and the place
where reader-address actually matters is identical across all three: every
**Practical insight** section in all 69 articles is direct second person
("Take **your** own register", "Before **you** build any cost model").
`check_site.py` warns if that ever drops below half of Schedule's rate.

*Not deliberate — open item.* **Key takeaways.** Schedule instructs
("**Draw** the histogram", "divide the budget by **your** cost efficiency");
Risk reports ("The six bids map to P10, P26, P48"). Those lines do the same job
in every track and should sound the same. They were left alone deliberately in
this pass: 126 Risk takeaway lines are dense with canonical figures, and
rewriting them is the highest-risk way imaginable to reintroduce the §1 error.
If they get rewritten, diff every digit before and after.

Contractions were aligned on 2026-07-19 across Tracks 2 and 3 — negatives
(`does not` → `doesn't`) plus `here is` and `let us`. Track 1 stays higher on
purpose. **`it is` was deliberately left alone**: it is ambiguous ("everything
below it | is a method being cautious") and often emphatic ("the margin is not
thin, it is gone").

## 5. Article shape *(judgement)*

```
h1 — editorial hook, 4–9 words
H2 #1 — repeats the h1
7–9 further H2s
3 SVG figures with figcaptions
Practical insight
Key takeaways — seven ✔ lines
What's coming next
H3 "Enjoyed this lesson?"
1,400–1,600 words
```

New articles are built by a Python script that takes the previous week's page as
a template. **Write those scripts idempotently** — they get run twice more often
than you would expect, and a second run should be a no-op rather than an error.

---

## 6. Publishing a week

1. Build the page from the previous week's template
2. Point the previous week's `next-article` at it
3. Set the week `live` in `curriculum.js` with `page` and `date`
4. Add the URL to `sitemap.xml`
5. Bump `curriculum.js?v=N` across every page
6. `python3 tools/check_site.py`
7. Zip

Module badges are driven by `badgeText()` in `curriculum.js` and flip to
"Complete · N weeks" on their own once `liveCount` reaches `totalWeeks`. Do not
hard-code them again. `badgeText()` also handles `liveCount === 0` ("Starting soon ·
N weeks"), and `badgeClass()` returns the matching `badge-locked` / `badge-active`.

**Three traps in step 5, all found the hard way on Track 5:**

- If the build script's `write()` normalises `?v=\d+` before comparing — which it must,
  or a rebuilt page looks changed every run — then that same function will silently
  refuse to write the cache bump. Bump the version with a direct write, not through it.
  This shipped twice before anyone noticed the version had been stuck for two articles
- Run the build twice. The second run must report `0 dosya`. A build script that is not
  idempotent will drift the cache version on every invocation
- Verify the bump landed: `grep -o "curriculum.js?v=[0-9]*" index.html`. The console
  message is not evidence

**Never put a numbered forward reference in body prose.** *"the subject of Week 16"* is
wrong even when 16 is currently correct — inserting a week renumbers everything after it
and the sentence becomes quietly false. Name the topic instead: *"the concurrency week
later in this track"*. This happened three times in Track 5 before it stuck, and once
after a week genuinely was inserted at position 6. Backward references are fine: those
weeks are published and their numbers are fixed. The build scripts now check for it, and
the check must ignore qualified cross-track references (*Contract Week 20* is legitimate;
a bare *Week 20* is not).

---

## 7. Open items

- **Fixed 2026-07-26 — the Track 4 module badge.** All nineteen published contract
  pages carried `MODULE 03 · RISK · WEEK 18` in the article eyebrow, inherited from
  the `risk-week-18` template and never corrected. No JS overwrites it, so that is
  what readers saw on every page of the track. The `Module 03 complete`
  next-article label and a dead `data-track="3"` came from the same place. When a
  new track is templated off the last article of the previous one, **grep the new
  page for the old track's name before publishing**
- **Fixed 2026-07-26 — Track 4 badges were hard-coded.** `t4ModuleBadge` in
  `learn.html` and `homeTrack4Badge` in `index.html` said `In Progress` in the HTML
  and were never wired to `badgeText()`, so the track would not have flipped to
  `Complete · 20 weeks` on its own. §6 says not to hard-code them; it happened
  anyway. Both now read from `curriculum.js` via `renderHomeTrack4Badge()`

- **Fixed 2026-07-27 — the copyright gate passed with the gate switched off.** With no
  PDFs in `uploads/`, `check_copyright()` returned "kaynak PDF yok, atlandı" and the run
  exited 0. A full run on a session with no sources printed **GEÇTİ** with the one check
  that matters never having executed. It now calls `bad()` and fails. Same failure shape
  as `contract-week-9` one level up: the protection looked green because it never ran
- **Fixed 2026-07-27 — the cache bump was writing nothing.** See §6. Two articles shipped
  against a stale `curriculum.js?v=`, which would have served readers the previous
  curriculum
- **Fixed 2026-07-27 — `check_site.py` did not know about Track 5.** `QUAL` in the xref
  check listed Schedule/Cost/Risk but not Contract or Claims, and `own_pre` had no
  `claim-` branch, so every cross-reference on a Claims page was being resolved against
  the Schedule track. The Contract omission had been there since Track 4 and was
  invisible until a fifth track started citing the fourth
- **Fixed 2026-07-27 — `check_voice` warned about tracks with no articles.** A track at
  0/N produced two warnings on every run. Warnings that are always present are warnings
  nobody reads

- **Fixed 2026-07-27 — the track header badges were stale on two tracks.** `learn.html`
  read `TRACK 4 · FREE · IN PROGRESS` on a 20/20 track and `TRACK 5 · FREE · STARTING SOON`
  on a 28/28 one. Same failure as the module badge above and found the same way, one level
  further up the page: a status written into HTML that no JS ever touched. Both now derive
  their state from `curriculum.js`. **Any string on the site that states a track's status
  must be computed, not typed** — this is now the third variant of this bug

- **Fixed 2026-07-27 — re-running a build script broke the article chain.** Each
  `build_claim_weekN.py` rebuilds its page from the previous week's, and the template's
  `next-article` card points at `learn.html`. Running week N again therefore *reverted*
  the forward link that week N+1's script had written. Running the whole set in sequence
  produced a cascade: every script rewrote a page, every rewrite triggered a cache bump,
  and the version ran from v122 to v179 in one loop while weeks 1, 2, 4, 14 and 15 were
  left pointing at `learn.html`. **The checker caught it — the chain check is the only
  thing that would have.** Every script now carries over the existing card when the page
  already links forward, keyed on the href rather than on the label text. Verified by
  running all twenty-eight twice: no writes, no bumps, chain intact.
  Two lessons: a generator that reads its own previous output needs to be idempotent
  against *its own side effects*, not just its inputs; and a cheap check that runs on
  every build is worth more than a careful process that runs once

- YouTube link is still a `https://youtube.com` placeholder on every page
- `logo-lockup.png` (471 KB) is shipped but unused
- Track 1 never defines BAC. The abbreviation appears twice on the whole site
  (an axis label in Schedule Week 18, and Cost & Cash Week 5 looking back at it);
  "budget at completion" is spelled out once, in Schedule Week 22, undefined.
  Schedule Weeks 17-21 teach PV, EV, AC, CPI, SPI and TCPI without it. If Track 1
  is ever revised, that is the gap to close at the source
- **Track 6 card said the wrong thing until 2026-07-27.** `learn.html` and `index.html`
  both still described Track 6 as *Project Controls Leadership — governance, KPIs, PMO
  structures, portfolio dashboards*, the plan §9 explicitly superseded on 2026-07-26.
  When a roadmap decision is taken in NOTES, grep the site for the old wording the same
  day
- **Track 4 is Contract Management**, not Claims. Settled 2026-07-20. Risk Week 18
  closes on notices, periods, forms, recipients and the consequence of missing them
  &mdash; that is contract administration, and it was being promised under a name
  (*Claims & Delay Analysis*) that describes forensic delay work. The card even
  contradicted itself: title *Claims & Delay Analysis*, subtitle *notices, records
  and entitlement*. Contract Management now takes 4, Claims & Delay Analysis moves
  to 5, Project Controls Leadership to 6. Nothing was written for any of them, so
  the change cost nothing &mdash; that window is now closed
- **There is no Reporting & Analytics track, on purpose.** Schedule Week 26 already
  is one, and states it better: *one model, six altitudes &mdash; two versions of
  the truth is a system failure*. A separate reporting track would say the opposite,
  that reporting is a stage after the controls work. The genuinely missing pieces
  (portfolio-level data governance, KPI thresholds, management by exception) are two
  or three weeks inside Track 6, not a track. Dashboard mechanics belong to the toolbox
- **Track 1 is "Schedule Management" everywhere.** `learn.html` used to call it
  *Construction Project Controls Fundamentals* in the track header and
  *Schedule Management* in the module card. "Fundamentals" implies Cost and Risk
  derive from Track 1; they do not, they are sibling tracks

## 8. Track 4 audit &mdash; 2026-07-26

The whole track was read back after Week 20. What held:

- All 60 clause references exist, and every cited official heading matches the book
- Every period checks out against the Red Book &mdash; 3.5, 3.6, 3.7.3, 4.2.1, 4.2.3, 8.3,
  10.1, 11.9, 12.3, 14.6.1, 14.7, 14.10, 14.11.1, 15.2.2, 16.1, 20.2.1, 20.2.4, 21.1, 21.4.3
- The countable claims are exact: 88 / 90 / 80 definitions in Red / Yellow / Silver, and
  *Bill of Quantities* really does appear nowhere in Silver
- No forward references, no `Clause 60`, and every *What's coming next* matches the
  article that follows it &mdash; except Week 13, below

What did not, and is now fixed:

| Where | What was wrong |
|---|---|
| `contract-week-16` | *"Red mentions the Engineer 544 times and Yellow 548. Silver mentions the word once."* None of the three is reproducible, and the Red/Yellow order inverts on the conditions. In Silver's conditions the word survives only inside the definition of FIDIC and the phrase *Value Engineering* &mdash; never as a role, which is the stronger fact anyway |
| `contract-week-16` | *"Same five-letter word in the heading."* **Unforeseeable** is thirteen letters, and it is the word that stays while *Physical Conditions* becomes *Difficulties* |
| `contract-week-13` | The handoff invented a fact &mdash; that the quarry haulage was priced in one currency and the diesel bought in another. Nothing in the article establishes it and Week 14 never picks the thread up. Rewritten to hand over on escalation and currency generally |
| `contract-week-8` | Carried the identical H2 to Week 1 (*Records made at the time, or not at all*) and restated the same argument. Also called the four components of 20.2.4 "the three components". Rewritten as a re-sort of the four by which can be produced late |
| `contract-week-4` | h1 read *"the hardest question in this site"* &mdash; on, not in. Fixed in the h1, the H2, the share links and Week 3's next-article card |

**The lesson worth keeping: precise counts are the most dangerous sentence in an
article.** They read as authority, nobody re-derives them, and three of the five
findings above were numbers that had never been counted. If a claim is countable,
count it before publishing or write the qualitative version instead.

### Overlap measured below the gate

The 10-word gate passes with zero, so the track was re-scanned at 8, 7 and 6 words to
see what it was actually sitting on. At 8 words there were 24 overlaps. Nearly all were
unavoidable &mdash; defined terms, statutory-style tests (*became aware or should have
become aware*), enumerated role lists, and ordinary contract English (*stated in the
Contract Data*). Two were not, and both were rewritten:

- **`contract-week-16`** ran four sentences through Silver's risk provisions in the
  clause's own order and close to its own wording. Compressed to the effect plus the
  argument, which was the point of the section anyway
- **`contract-week-11`** listed 8.3's eleven required contents in the clause's own
  sequence. Regrouped into three planner-facing buckets &mdash; dates somebody else owes
  you, how the job goes together, hooks into other people &mdash; which breaks the
  mirroring and reads better

Result: **8-gram overlap 24 &rarr; 21, and nothing distinctive left in the remainder.**
Watch for this when rewriting: the first pass at Week 11 introduced a *new* 8-word
overlap of its own. Re-measure after every fix, not just before.

Reading times were recomputed for all twenty Track 4 pages at the same time. Eleven
were wrong by a minute, and Weeks 1&ndash;3 &mdash; the three longest in the track &mdash;
were the ones reading *7 min* while shorter articles read 8.

## 8b. Track 5 notes &mdash; 2026-07-27

Twenty-eight weeks, written in one run. What is worth carrying forward:

**The curriculum grew by a week, from a reader.** The proposed 27 had no article whose
subject was the site record. A comment argued that daily reports, allocation sheets,
diaries, RFIs and the rest are the fuel of a claim &mdash; and a count settled it: nine of
the seventeen record types named appeared **zero times across the 90 articles then published**. The week went
in at position 6, before the as-built, because an as-built is built from those records.
The comment was right; the list in it was not the article. Organised around
*primary / derived / reconstructed* instead, which is an argument rather than an
enumeration.

**Articles kept coming in short.** Most weeks needed expanding after the first build,
typically landing near 1,250 against a 1,370 floor. The cause is consistent:
three SVG figures absorb the budget that prose was going to use. Either write to ~1,550
expecting to lose some, or accept that a figure-heavy article needs a section more than
it feels like it does. Every expansion improved the article, which suggests the floor is
doing real work rather than padding.

**The copyright gate fired on eight of the twenty-eight weeks, and always on the same
kind of sentence.** Not narrative, not analysis &mdash; *definitions and statements of
principle*. `Unforeseeable` in Week 3, the revised-programme trigger in Week 8, the
Protocol's core principle in Week 11, the mitigation duty in Week 18, the disruption
definition in Week 19, the certification wording in Week 25. These are the hardest
sentences to paraphrase precisely because they are already minimal: a drafter has spent
years removing every word that could come out. Reaching for the source's phrasing is not
laziness there, it is the path of least resistance, and it is exactly where the gate
earns its keep. **Assume any sentence that defines a term will need rewriting from
scratch, and write it that way the first time.** One further wrinkle: three consecutive
clause *headings* quoted in order also tripped it. A list of titles is reproduction too.

**Two structural conventions that earned their place:**

- **Order the methods by the evidence they require, not by name.** Impacted as-planned
  needs almost nothing; collapsed as-built needs an as-built and nothing else. Running the
  phase that way makes the track's thesis &mdash; *your records chose your method* &mdash;
  visible in the sequence rather than asserted in a sentence. It is also demonstrably not
  the ordering used by either the primary text or the course material
- **Phase B before Phase C.** Evidence before methods. By the time the reader reaches
  method selection, the constraint has already been established and week 9 can simply
  point at it

**The canon absorbed two new numbers and produced one for free.** `contract_duration_months`
= 12 was never stated anywhere on the site, but `cost-week-17`'s *"roughly $69,000 a
month"* against a controlled budget of $827,008 fixes it. That gives
`preliminaries_monthly` = $7,100 exactly, which is the base rate for the whole quantum
phase. Separately, $124,051 / $827,008 is exactly 15%, which let Hudson be worked on the
job's own figures in Week 24. **Numbers already implied by published arithmetic are worth
hunting for before inventing new ones.**

**What did not need fixing:** the two-title convention, the h1 register, the practical
insight in second person, and the `next-article` chain all held across 28 articles without
incident. The template-inheritance trap from Track 4 &mdash; the old track's name surviving
in the eyebrow &mdash; did not recur, because the build scripts assert against it before
writing.

## 9. What comes next *(judgement — revised 2026-07-27)*

### Track 5 — Claims & Delay Analysis — **done, 28/28**

Published 2026-07-27, dated Mar 8 – Sep 13 2028. Prefix `claim-week-`. Seven phases.
Closes on the two numbers the site was built around: the rock at $48,450 against a net
margin of $48,163.

Source position at the end: the primary text turned out to be **Keane & Caletka,
*Delay Analysis in Construction Contracts* 2e** — not the book an earlier note named.
It carries concurrency 229, float 415, SCL 142, acceleration 135, disruption 178, and
Chapter 4.2 treats both industry documents directly. The three FIDIC 2017 books arrived
as full conditions, so every clause claim in the track is first-hand.

**The remaining gap is unchanged and still matters.** The **SCL Delay and Disruption
Protocol** and **AACE RP 29R-03** are still not present as primary documents. The track
describes and attributes them through Keane & Caletka and never states their guidance as
if read first-hand — but that is a workaround, not a fix. The Protocol has been revised
since the account the track is working from, and any future article touching it must say
which edition. If the two documents are ever obtained, Weeks 9, 11 and 16 are the three
to revisit.

### Track 6 — the assumptions that stop holding — **next**

**This supersedes the earlier one-line plan** (portfolio data governance, KPI
thresholds, management by exception). Those were three topics, not a track. The
thesis now:

> Five tracks taught the job as a single contract with a single chain of command.
> Track 6 is what happens when those assumptions stop holding.

The card text on `learn.html` and `index.html` was corrected to this on 2026-07-27;
before that both still advertised the superseded leadership plan. `claim-week-28`
hands over to it in print, on the same thesis, so the framing is now committed.

Note the framing that was tried and rejected: **scale.** The $1M job is a unit chosen
so the arithmetic stays legible, not a claim that the job is small. Nothing in Track 6
is true only on big projects — an EPCM job of any size still has no head contract.
Do not build the track on "small job vs mega project"; it is a claim we cannot defend
and it is not what actually varies.

Contents, in order:

1. **Delivery models — who holds the scope.** The opening, because it is the frame
   the rest sits in. Sixteen names (DBB, DB, EPC, EPCM, PMC, CM, turnkey, LSTK, BOT,
   BOOT, BOO, PPP, alliance, IPD, framework, IDIQ) collapse onto three axes: how you
   are paid (**done** — Contract W4), who carries design (**done** — Contract W16, via
   Red/Yellow/Silver), and **how many contracts there are** — the one that is missing.
   The argument: under EPCM there is no head contract. The employer holds every
   package; the managing firm directs people it has no contract with. That inverts
   Track 4 — who do you serve the 20.2.1 notice on, and who is the Engineer?
   BOT/BOOT/BOO/PPP are financing wrappers with an EPC still inside them; IDIQ and
   framework agreements are procurement vehicles, not delivery models; alliance and
   IPD change the controls function itself and hook to Contract W19
2. **Long lead — the critical path runs through a purchase order.** Corrects Track 1,
   which assumes a programme driven by construction logic. `long lead` still appears 0
   times across 117 articles (re-measured 2026-07-27)
3. **Interfaces — the work nobody planned is where two programmes meet.** Corrects
   Risk W3, which already says the register misses "two whole branches". `interface`
   now appears 11 times across 117 articles, still all in passing
4. **The number with more than one owner.** Project Controls builds earned value from
   progress, Commercial from valuation, and they collide monthly. Also: you own no
   primary data — every figure in your report was made by someone else, for another
   purpose, on another cycle, and each source has its own cut-off. Cost W10 already
   owns the ledger side; do not repeat it
5. **Document control.** `document control`, `transmittal`, `revision control`,
   `document register` — all 0 across 117 articles (re-measured 2026-07-27). Connects straight to Contract W1:
   the whole article was a notice reaching the right address, and this is that problem
   at organisational scale

Three hooks into Track 5 that did not exist when this list was written. Item 1 inherits
the concurrency problem: `claim-week-16` establishes that FIDIC sends the question to the
Special Provisions, and under EPCM there is no head contract to hold them. Item 4 should
link `claim-week-25` rather than restate it — the cost-coding resolution argument is made
there and applies unchanged to a multi-owner number. Item 5's organisational-scale
records problem is the same one `claim-week-6` makes at project scale; link, do not
repeat.

Deferred: **systems completion / commissioning.** Real gap (`systems completion` still 0
across 117 articles),
but there is no source for mechanical completion, turnover packages or system
boundaries in the uploads. Wait for a book.

### Closed — do not re-open

- **Coding retrofit** ("a cost code cannot be applied later"). Already covered, and
  well: Cost W6 gives the rules and says miscoded hours can never be unpicked, Cost W7
  says cut scope, cost and schedule the same way once at the start, Cost W14 makes
  single capture the hinge of the track. A new article would weaken three
- **A reporting track.** `report` 223, `forecast` 113, and Schedule W26 is the
  reporting article. Reporting is a verb inside every subject, not a subject
- **A change management track.** `variation` 51, `instruction` 40, `daywork` 20 —
  spread across Cost W13, Contract W6/W7/W13 and Schedule W21/W23 because that is
  where it belongs. Pulling it out would strip three articles and produce nothing
- **A department directory** (27 departments × RACI, reports, logs, KPIs, meetings,
  software, Excel templates). No case, no source, unmaintainable, and it argues the
  opposite of what the site argues: that controls is a set of forms rather than a way
  of thinking from inside the work. Only one article survives from it, and it is
  item 4 above
- **A headcount reference model** (e.g. "430 white collar, HSE 40"). Not derivable.
  The Track 4 audit is the standing lesson here: an exact number nobody can reproduce
  is the most dangerous sentence in an article
- **Excel template library / software lists.** A different product. Templates are the
  digital phase, not the theory phase; software lists go stale in two years

### The test that decided all of the above

> **Does it correct something, or does it collect something?**

Correcting earns a track. Collecting is a reference layer, and §7 already rejected one.

### Open question, deliberately not acted on

The delivery-model frame arrives around week 110. If the goal is that a reader
understands what project controls does on an EPC or EPCM job, that frame is late —
for four tracks the reader does not know they are in a single-contract world.
Restructuring published tracks is off the table (the chain and the handoffs are in
print). The cheap option, if it is ever wanted, is one orientation piece on
`learn.html` outside the week sequence — not a track, not a week, nothing that
promises a next article. Left undecided on purpose: Track 6's opening does the same
job, just later.

## 10. Reporting &mdash; design decisions *(judgement &mdash; 2026-08-05)*

Written while the track was being drafted, because the articles will survive
and the reasoning behind them will not.

### The four questions used on every sentence

These were applied throughout and are worth carrying into the other tracks.

1. **Is this the author's voice, or book language?**
2. **Does it work on site, or only in theory?**
3. **Is the idea in the right week?** A good idea in the wrong week weakens
   the article it is in and the one it belongs to.
4. **Which failure does this principle explain?** A principle that only reads
   as good practice is weak. One that answers "what goes wrong if this is not
   done" is teachable.

Two supporting rules, both learned the hard way in drafting:

**Separate what happened from what was concluded.** The memory is the
author's and is not edited. The conclusion is drawn from it, jointly, and is
labelled as a conclusion. A composite scene is permitted &mdash; the same
failure on four projects is stronger evidence than one occurrence &mdash; but
it may not contain a sentence nobody said.

**Do not mistake the symptom for the problem.** WhatsApp is not the problem;
an untracked request is. A dashboard is not the problem; the data model is.
Writing the symptom as the thesis dates the article and misses the cause.

### The subject is not reports

The track is called Reporting and it is not about writing reports. It is about
where a number comes from, who owns it, what state it has to arrive in, and
what it feeds afterwards. Writing the document is the smallest part and it
appears in four weeks out of twenty-five.

This is stated in week 1 so a reader does not spend three weeks expecting
templates. The thesis under everything: **project controls does not produce
data, it turns what the organisation produces into something that can be
relied on.** Week 26 deliberately does not restate it. If the reader has not
reached it by then, saying it at the end will not help.

### Why the order is sources first, outputs second

Fifteen weeks on what each department feeds you, then eleven on what you
issue. Not the other way round, and not interleaved.

The alternative &mdash; organising by document, a week per report &mdash; was
considered and rejected. It teaches the artefact rather than the trade, and
it makes every week partly about the same collection problem. Organised by
source, each week has one department, one set of records, one failure mode.

The cost is that the first half has no visible output, which is a real
weakness. Week 1 and week 2 carry the whole burden of explaining why it is
worth reading, which is why they are the two longest.

### Why 21 was empty, and what filled it

Week 21 was left out on the first pass. Dashboards had been scoped and the
material was either taxonomy or already covered &mdash; audience levels are
week 20, indicator selection is week 22, the tool itself is the digital phase
&mdash; and no argument was left that a week could carry. A weak week costs
more than a missing one, so it was skipped, and week 20 was rewritten to hand
forward to the indicators without naming a number.

The condition written here was that it stayed empty until an argument
existed. One arrived: **two experienced people leave the same dashboard
review having reached different conclusions, and neither has misread
anything.** That is an observed failure, it is not covered by 20 or 22, and
it passes the test below &mdash; it explains something that goes wrong rather
than describing good practice.

The week is written to that and nothing else. No tool, no chart design, no
visualisation. The argument is that a dashboard renders a data model and
cannot show where the model is weak, so a disagreement about a screen is
always a disagreement about definitions, cut-offs and ownership. It must not
re-derive week 1: the principle is shared but the mechanism here is absent
common definition, not absent ownership of a single figure.

Worth recording for the next time this happens: the week was skipped
correctly and written correctly, and both decisions used the same test.

### Why one System design table per week, and always the same shape

Every week has exactly one table, five columns, no exceptions:
`Record | Produced by | Required quality | Verified against | Feeds`.

111 rows across 25 weeks. Taken together they are a data dictionary rather
than 25 illustrations, and the later modules are meant to sit on it. A
dictionary whose shape changes per entry is not a dictionary.

`Required quality` answers one question only: **can project controls use this
as it arrives, without doing anything to it first?** Where the answer is no,
the cell names what is missing &mdash; "allocated to activities, not just
totalled", "issued quantity, not delivered quantity", "backed by a document
or a booking, not last week plus seven". It is a usability definition, not a
checklist, and it is the part that does not exist anywhere else.

Two temptations were refused. A six-column version with source, frequency and
consumer: correct, and it reads as a form to be filled rather than a question
to be answered. And a RACI variant with produced / checked / approved: it
turns one missing name into three arguments, and the observed failure is that
nobody owns the number at all, not that ownership is unclear between three
people.

### Why the same principle recurs, and what counts as repetition

Corroboration appears in six weeks. Closure in three. Ownership in most.
That is deliberate: on a real project the same principle is met again in
engineering, in procurement, on site, in quality. Meeting it four times in
four contexts is how it is learned.

The line is between principle and reasoning. **The principle may recur. The
same reasoning may not be performed twice.** Two failures of that were found
on the final read and cut: week 14 was explaining the two-calendar problem
that is week 16's whole subject, and week 18 was re-narrating week 9's
mechanism before adding its own. Both now reference and move on.

The mechanical test that caught it: count concept mentions per week. A week
with a high count is the home; a week with two or three is referencing; a
second week with a high count is a duplicate.

### Why pattern rather than anecdote

Early drafts asked for single events &mdash; a day, a meeting, a number.
Wrong instrument. The material is eight years across several countries, and
the same failure recurring on four projects is stronger evidence than one
occurrence of it, as well as being more honest to how it was learned.

So the scenes are composites, and they say so: "I have heard all of them, on
different jobs, in different countries, years apart." The constraint that
keeps this from becoming invention: **which sentences were said is the
author's, only the order they appear in is the writing.** A composite may not
contain anything nobody said.

No company, project or country is named. The subject is process, not any
organisation, and naming one would change what the piece is doing.

### Why no figures

No quantities anywhere in the track. The paint example is a ratio, not
litres. The events behind these articles happened on jobs that are not the
$1M case study, and a precise figure from them is exactly the sentence
section 1 forbids: one nobody can reproduce. Units and flows carry the
argument; numbers would only decorate it.

### Why the data model comes before the report

Week 1 and week 2 argue the order: model, then collection, then verification,
then report. This is why the track opens with ownership and field
specification rather than with a document.

With one qualification that had to be added and is easy to lose: **almost
nobody designs the model.** Planners inherit one. Every week that proposes a
system therefore carries two readings, from scratch and inherited, and the
inherited case is treated as the normal one because it is. The heading varies
per week &mdash; "on a project that is already running", "adding rather than
replacing" &mdash; because nine identical headings read as a template by the
fourth.

### Density is deliberately uneven

Between 843 and 1,676 words. Two tiers, on purpose.

The load-bearing weeks &mdash; 1, 2, 8, 9, 13, 17, 23, 25 &mdash; are long
because the argument is theirs. The system weeks are shorter because they
carry a design decision rather than a case. Padding the second tier to match
the first would have meant writing filler, and an even series of 1,500-word
articles is a worse read than an uneven one.

Every week ends with **Records born here**, naming the documents that come
into existence at that stage. There is no "feeds next" line: which record
feeds which is week 24's subject, and on most weeks the honest answer would
have been "the archive".

### Open, and deliberately not closed

- **21** stays empty until an argument exists for it.
- **Prefix** is `reporting-week-N.html`, unpadded, matching every other page
  and `check_site.py`'s `week-(\d+)`. Zero-padding was proposed and dropped
  for that reason.
- The 25 drafts are in `drafts/` and out of the chain and sitemap. Week 8 was
  written first because its material was ready; publication order is 1 upward.
- `check_site.py` registration for Reporting and Interfaces is done. `QUAL`
  now spans tracks 0&ndash;7.

### Second phase &mdash; a canonical data dictionary *(recorded, not started)*

Deliberately not built. Recorded here so the scope is not re-argued from
scratch, and so the reasons for the shape are still available.

**What already exists.** The 26 System design tables are the first version of
this: 115 rows in one fixed shape, `Record | Produced by | Required quality |
Verified against | Feeds`. The gap is a *why* column. In drafting, the
strongest examples were always the ones that answered it &mdash; an activity
ID exists so that an executed quantity can be tied to the programme, and
without it physical progress is a quantity with nothing to attach to. That
reasoning currently lives in the article body, not in the table.

**Why it is a separate product and not an appendix.** Reporting is an
argument: 26 weeks building one idea, read end to end, and it must not repeat
itself. A data standard is a reference: nobody reads it in order, it is opened
at the point of need, and it *has* to repeat itself because the reader did not
see the previous entry. Different products with opposite rules. Appendices at
the end of each week would break the argument's rhythm; a reference scattered
through 26 articles cannot be found.

**Field-centric, not table-centric.** `Area`, `WBS`, `Activity ID`,
`Discipline`, `Revision`, `Status`, `Owner`, `Data date` and `Cut-off` recur
across most registers. Defining each once and having registers reference it
avoids writing the same explanation sixteen times, and it produces a data
dictionary rather than sixteen spreadsheet templates.

Proposed shape per field: purpose, definition, format, owner, required
quality, validation, downstream consumers, common errors, related fields.

**The one real hazard.** Fields that share a name do not always share a
meaning. `Status` in a transmittal register and `Status` in a constraint log
are different concepts. Canonicalising by name merges things that should stay
separate. The test is the definition, not the label, and any field where two
registers cannot accept one definition stays split with both versions named.

**What makes it legitimate rather than a column catalogue.** Column lists
exist in hundreds of places. What does not exist is why the column is there
and what breaks without it &mdash; which is rule four applied at field level.
`Common errors` is the column carrying that weight, and a version of this
without it is the hundred and first column list. Note that a department
directory and a template library were both closed earlier in these notes for
exactly the reason this could fail: collecting rather than correcting.

**Scale, honestly.** Roughly sixteen registers, fifteen fields each, nine
questions per field. Around two thousand cells. Feasible, not a weekend, and
a half-populated reference is not a reference.

**Sequence.** Publish Reporting first. Which System design tables actually
get used, which fields readers argue about, and which concepts turn out to be
missing should set the scope &mdash; not a guess made now.

