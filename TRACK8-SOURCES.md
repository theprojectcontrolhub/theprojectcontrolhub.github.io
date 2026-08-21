# Track 8 — source measurement and week-by-week verdict

Written 2026-08-19, after the sources arrived. This supersedes the numbers in
`TRACK8-KICKOFF.md` §3 and in `TRACK8-KICKOFF-ADDENDUM.md` §1, both of which
were measured against a pool that no longer describes what is on disk.

The addendum asked for exactly this: *"Before any week list is fixed on these
numbers, run one measurement with one stated method and record which form was
counted."* Here is the method, and here is what it changed.

---

## 1. The method, stated once

**Pool.** Every uploaded source, extracted to text, deduplicated by content
hash, then filtered to those with a real text layer — defined as ≥100,000
characters extracted **and** ≥150 words per page. That is **19 sources**.

The two filters matter separately. `Kohli & Chitkara, Project Management
Handbook` is 532 pages and yields 43,887 characters — 10 words per page, which
is a title page and nothing else. It is a scanned book. Counting it would put
a zero next to every term in it, and that zero would mean *"no text layer"*
rather than *"not in the book"*. It is excluded and listed below as an
acquisition, not as a source.

The four AI books and `AI Essentials` are also excluded. They are a coherent
pool for something else (§6) and they contaminate construction counts —
`commissioning` alone picks up 34 hits from them in the machine-learning
sense.

**The 19:**

```
FIDIC Red Book 2017              International Construction Contract Law
FIDIC Yellow Book                Construction Contract Claims
FIDIC Silver Book                Construction Contract Claims Changes
PMI Construction Extension       Delay Analysis in Construction
PMBOK 8                          Practical Guide to NEC4
AACE TCM Framework               NEC Commentary
Construction Management (Halpin) International Construction Management
Cambridge Handbook of OPM        The Multinational Construction Industry
Large Scale Construction PM      Building Information Systems in Construction
PMO Practice Guide
```

**Count form.** Case-insensitive. Hyphen-linebreaks rejoined and whitespace
normalised first, so a term broken across a line still counts. Every concept
searched hyphenated, closed and spaced, **and** in the word the contract
itself uses. Each form reported separately; the concept total is their sum.

Script: `tools/measure_sources.py`. It prints the pool before it prints a
number, which is the part that was missing last time.

---

## 2. What the measurement changed

### 2.1 Week 31 is not unsourced. It is the best-sourced week in Phase G.

§3 recorded `performance test` **0** and the addendum re-checked it against
alternative spellings and accepted the zero. Both are right about the phrase
and wrong about the subject.

| | count |
|---|---|
| `performance test` | 2 |
| **`tests on completion`** | **177** |
| **`tests after completion`** | **98** |
| `trial operation` | 23 |
| `performance guarantee` | 10 |

FIDIC Yellow Book Clause 12 is *Tests after Completion* end to end — 12.1
Procedure, 12.2 Delayed Tests, 12.3 Retesting, 12.4 Failure to Pass. Red Book
Clause 9 is *Tests on Completion*, with 9.4 Failure to Pass and 10.3
Interference with Tests on Completion sitting against it.

And the Yellow Book guidance says the thing the week is actually about: Tests
after Completion are carried out **by the Employer and the Employer's
operating personnel**, with the Employer providing power, water and
consumables, shortly after taking-over.

That is the printed promise — *commissioning inverts the priorities of
everything before it* — available first-hand rather than from practice. Up to
taking over, you control the work and are measured against a programme. After
it, somebody else's operators run the test, on their fuel, on their schedule,
and your exposure continues while your control does not.

This is the addendum's own rule catching a third instance: **search the term
the contract uses.** "Performance test" is the industry's word. "Tests after
Completion" is the contract's.

### 2.2 Week 33 is not unsourced either. It is called something else.

`demobilisation` 2 + `demobilization` 20 + `demobilize` 3 = 25, which reads
thin. But FIDIC's sub-clause for the same event is **11.11 Clearance of
Site**, and `clearance of site` is 30 across the three books, with the
mechanism attached: it happens *after* the Performance Certificate, and if the
Contractor has not cleared within 28 days the Employer may sell or dispose of
the remaining Equipment.

Halpin adds the half nobody teaches: mobilisation and demobilisation are a
**cost cycle**, and a suspension forces a demobilise-remobilise round trip
that was priced once and is now being paid for twice.

### 2.3 Week 29 stays absent, and now we know precisely what is absent.

Re-checked in every form across the 19:

```
mechanical completion   0     systems completion    0
mechanical acceptance   0     turnover package      0
ready for commissioning 0     mechanical-completion 0
```

Genuinely zero. But the *boundary* mechanical completion marks is not absent —
it is drawn in a different place by a different family of contracts:

| | count |
|---|---|
| `substantial completion` | 53 |
| `practical completion` | 31 |
| `construction completion` | 4 |
| `outstanding work` | 58 |

So week 29 is writable, but not as an EPC process week. It is writable as *the
completion boundary is drawn four different ways and each one hands over a
different amount of unfinished work* — which is a better week than the one
that was planned, and it is sourced.

### 2.4 `as-built` 225 was the wrong subject.

This is the one worth carrying forward as a rule.

`as-built` in the pool is 568 occurrences. Split by the word that follows it:

| sense | count | examples |
|---|---|---|
| **forensic** | 284 | as-built programme 87 · as-built critical path 79 · as-built schedule 30 · as-built analysis 20 · as-built logic 15 |
| **record** | 166 | as-built records 62 · as-built data 16 · as-built drawings 8 · as-built model 8 |

The forensic sense belongs to Track 5. It is the as-built *programme* used to
prove a delay, and it has nothing to do with the record born at closeout.
`Delay Analysis in Construction` alone contributes 346 of the 568.

So the closeout record has roughly **166** behind it, not 568 and not the
addendum's 225. Still adequate — comfortably enough for a week — but the
headline number was inflated about three-fold by a different subject in the
same words.

**The rule this adds.** §3 caught spelling-driven zeros. The addendum caught
one more and added *"search the term the contract uses."* This adds the third:
**a high count is not evidence until you have looked at the word next to it.**
A term that means two things counts as one term.

### 2.5 One week rests on one book.

`investment decision` is 94, which reads strong. **93 of the 94 are in the
AACE TCM Framework.** Week 3 is not sourced by the pool; it is sourced by one
reference. That is allowed and it must be written knowing it — a single source
cannot corroborate itself, and TCM's asset-lifecycle framing is one industry's
view of the front end, not the industry's.

Same shape, smaller: `front-end loading` 9, of which 5 are PMI Construction
Extension.

**Closed 2026-08-19, when week 3 was written.** The concentration was an
artefact of measuring the phrase rather than reading for the week. Three more
sources carry the same subject under other words: Halpin ch.2 has need, market
study, formal need evaluation and the board deciding whether the investment is
justified; PMBOK 8 treats the business case as a live document to be re-tested
against financial performance during delivery; the PMO practice guide carries
`benefits realization` 34. Week 3 is written from four sources, not one.

Worth generalising, because it is the fourth version of the same lesson in
this file: **a phrase count locates a subject, it does not measure one.** The
subject was never thin. Only the term was.

---

## 3. Where the track is strong, and where it is not

Counts are concept totals across the 19, all forms summed.

### Strong — write first-hand

| subject | count | principal sources |
|---|---|---|
| taking over | 623 | FIDIC ×3 (Taking-Over Certificate **166**), ICCL |
| tender / award | 873 | NEC Commentary, NEC4, ICCL |
| as-built (record sense) | 166 | FIDIC ×3, Halpin |
| tests on / after completion | 275 | FIDIC Red cl.9, Yellow cl.12 |
| work breakdown / packaging | 425 | AACE TCM, Halpin ch.7, PMBOK 8 |
| closeout chain | 348 | FIDIC 14.10→14.13, Performance Certificate 102 |
| defects | 214 | FIDIC 2017 DNP **85** |
| lessons learned | 262 | AACE TCM 76, Cambridge Handbook |
| forecast | 253 | AACE TCM, PMBOK 8 |
| front end / FEL | 173 | PMI Construction Extension 2.3.1, Large Scale CPM |
| feasibility | 157 | AACE TCM 44, ICCL 33 |
| work package | 180 | AACE TCM 69, Halpin 56 |
| expediting | 141 | Construction Contract Claims 20, TCM 14, FIDIC 9 |
| coding structures | 97 | control account 50, OBS 38, code of accounts 16 |
| business case | 96 | PMBOK 8 42, ICCL 31 |
| mobilisation | 64 | Halpin 28 — and it is a **cash flow** treatment |
| temporary works | 74 | FIDIC Red 22, Halpin 19 |
| punch list / snagging | 84 | outstanding work 58, PMI Ext 18 |

### Thin — write from practice and say so

| subject | count | note |
|---|---|---|
| commissioning | 86 | adequate in name, almost nothing on sequence |
| execution plan | 58 | `project execution plan` as a phrase: 4 |
| purchase order | 35 | Halpin 20 |
| document control | 34 | transmittal 15 — third pass anyway, see §4 |
| archive | 18 | weakest thing in the closeout group |
| look-ahead | 15 | `last planner` 8, `weekly work plan` 1 |
| long lead | 15 | |
| kick-off | 12 | across all three spellings |
| change control board | 11 | |
| site logistics | 7 | `laydown` 0, `site establishment` 0 |
| delegation of authority | 5 | `limits of authority` 0, `approval authority` 0 |

### Absent in every form — do not plan a week on these

```
design freeze 0 · vendor data 0 · deliverable list 0 · inspection and test plan 0
constraint removal 0 · record drawings 0 · O&M manual 0 · site diary 0
mechanical completion 0 · decision gate 0 · requisition 2 (in the procurement sense)
```

Two of these were planned weeks. `design freeze` is week 15's whole second
half and it does not exist in the pool under any spelling — including *"freeze
the design"*, *"frozen design"* and *"design lock"*, all zero. `requisition`
at 2 makes the front half of week 16 unwritable as planned.

---

## 4. What the sources say about the weaknesses the kickoff already flagged

§4 listed five known weaknesses and asked for them to be settled early. The
measurement settles four of them.

**Weeks 21 and 22 (constraint removal, look-ahead) — cut.** The kickoff's own
condition was that they survive only if they can be about *when in the project
this starts and who hands it over*, and it said "if that cannot be sustained,
cut both". The pool gives `last planner` 8, `weekly work plan` 1, `percent
plan complete` 1, `constraint removal` 0. There is nothing here that Reporting
week 9 and Interfaces week 13 have not already used better. Cut both; keep one
paragraph of the handover question inside the site-rhythm week.

**Week 12 (document control) — cut.** Third pass, and `document control` 19 /
`transmittal` 15 is the thinnest evidence any of the three passes has had. The
kickoff said *"either it is about setting it up on day one or it goes."* The
day-one part is real, and it is the same argument as coding philosophy —
decisions that cannot be made later — so it joins that week rather than
holding its own.

**Week 25 (forecasting) — keep, reframed.** `forecast` 253 is method and
belongs to Cost & Cash. The lifecycle question — at which point the forecast
stops being an estimate and becomes the number your performance is read
against — is not in the pool and is not in Cost & Cash either. It survives as
the kickoff predicted: as an occasion, not a method.

**Weeks 26–28 (governance) — keep, narrowed.** Cambridge Handbook gives
`governance` 347 inside single organisations, which is exactly the distinction
the kickoff asked to be visible in the first paragraph. But
`delegation of authority` 5 and `limits of authority` 0 mean week 26 is
written from practice. Three weeks is one too many on this evidence; two.

**Phase E is two weeks and reads thin — dissolved.** Change on the ground goes
into Phase D where it happens, forecasting joins governance, and Phase E stops
existing.

---

## 5. What the sources gave that was not planned

Five weeks that the pool argues for and the 36-week list did not have.

**Three life cycles, three start dates.** PMI Construction Extension §2.3,
Figure 2-2, lays the same project against three parties: the owner's project
starts at the business decision, the designer's at the decision to propose,
the contractor's at the decision to bid. Three different day ones for one job.
This is the printed promise — *it starts before anybody is appointed* — with a
figure behind it, and it is a better opener for Phase A than a definition of
business need.

**The stage gate you never attended.** PMI Construction Extension Table 2-1
gives the FEL 1/2/3 deliverables, each gate with its estimate accuracy —
±50% at FEL 1, tightening through FEL 2. The number you are handed at award
has an accuracy class that was fixed at a gate held before your company was on
the list. That is a failure, not a description: it explains why a variance
appears in month three that nobody caused.

**Taking over in parts.** FIDIC 10.2, `taking over parts` 20. A partial
taking-over splits the Defects Notification Period per part, starts the
Employer operating inside a site you are still working in, and reduces delay
damages by a proportion the contract has to define. Nothing anywhere on the
site covers it, and it is one of the commonest real endings.

**Expediting.** 141 occurrences and no week. It is the one activity in the
whole project with no drawing, no work face and no measurable percent
complete, which is precisely why it disappears from progress reports and
reappears as a delay. It belongs in Phase C.

**The completion boundary, drawn four ways.** From §2.3 above — substantial,
practical, construction and mechanical completion are four different lines,
each handing over a different quantity of unfinished work, and the punch list
is born at whichever one your contract uses.

One more, offered and not taken: the BIM sources support *the as-built as a
model rather than a set of drawings*, but at `as-built model` 8 it is a
paragraph inside the records week, not a week.

---

## 6. Sources that do not serve this track

Recorded so the next person does not re-open them.

- **The 59 `Claim and Delay` slide decks** are Track 5's subject end to end —
  EOT, concurrency, TIA, quantum, case study. Nothing lifecycle.
- **`Delay Analysis in Construction`** is the source of the as-built
  contamination in §2.4. Useful to Track 5, actively misleading here.
- **The Primavera guides** (two Turkish, one English) are tool documentation.
  The site teaches no tool.
- **`Delays in EPC Projects`** is 56 one-line causes of delay across E/P/C.
  It reads as exactly the book language `NOTES.md` §10 question 1 exists to
  reject — *"inadequate expertise can lead to errors and inefficiencies"*.
  Unusable.
- **`The Role of a Planning Engineer During and After Project Completion`** is
  a four-page marketing PDF. It names the closeout record set and nothing more.
- **`International Construction Management`** and **`The Multinational
  Construction Industry`** are internationalisation books. Their subject is
  Track 7's and Track 7 is written.
- **The four AI books** — PMI's AI Standard, Taylor, AI Blueprints,
  Interpretable AI — are off-topic for Track 8 and are a coherent pool for a
  ninth track. Noted, not opened here.

## 7. Worth acquiring

- **Killcross, *Process Plant Commissioning* (IChemE)** — still the gap. It is
  the only thing that would make weeks 30 and 31 process-industry weeks rather
  than contract weeks. §3 of the kickoff named it, it was not bought during
  Reporting, and it is still not here.
- **CII front-end loading / start-up research** — would give week 5 a second
  source and break the AACE monopoly noted in §2.5.
- **`Kohli & Chitkara, Project Management Handbook`** — present but scanned.
  532 pages, no text layer. An OCR pass would add a genuinely lifecycle-shaped
  reference, and it is the only book in the upload organised by project stage
  rather than by knowledge area.

---

## 8. Phase B, and the material that is not here

`TRACK8-KICKOFF.md` §5 says weeks 7 to 14 describe the first months of a job in
a way only somebody who has joined one can write, that the site has eight
years of that behind it and almost none of it has reached the page, and that
**nobody can write day one convincingly from first principles.** It lists
three questions to put to the author first. As of week 8 they are unanswered.

> **Partly answered 2026-08-19.** The author has since answered questions 1
> and 3; question 2 came back as a pattern rather than an occasion. The
> account is recorded verbatim in `TRACK8-ACCOUNT.md`, which also lists what
> it changes and what is still missing. Week 9 was revised on it. Week 8 has
> not been — the scene it wants is still absent, because the account describes
> the first weeks and the state of the system rather than the first morning.

**Week 8 was therefore written without a scene.** No composite folder, no
remembered first morning, no invented kick-off. Every concrete statement is
either a contract mechanism from the pool or a structural consequence of the
seven weeks before it. Recorded here so nobody later mistakes the absence for
a choice about style.

What made it writable anyway is that the first month turns out to be
contract-sourced, which §3 did not anticipate:

| | |
|---|---|
| Commencement notified at least 14 days ahead | FIDIC 8.1 |
| Commencement within 42 days of the Letter of Acceptance | FIDIC 8.1 |
| Performance security within 28 days of the Letter of Acceptance | FIDIC 4.2.1 |
| Initial programme within 28 days of the Commencement notice | FIDIC 8.3 |
| Access per the Contract Data, withholdable until the security is received | FIDIC 2.1 |

Two arguments come out of that set and neither needs a memory. The opening
obligations hang off **two different anchor dates**, and the durations are
identical, which is what makes confusing them easy. And the performance
security is a **gate on the site**, because access can be withheld until it
arrives — a dependency that sits in two separate clauses and that no
programme has an activity for.

The week's own argument is the counterpart to week 5: influence peaks before
the delivery team arrives, and the *reference* is fixed in its first month, so
the moment of least knowledge produces the document of most authority.

**Where the lived material would go.** Section two, *"What is in the folder,
and what is not"*, replacing nothing. It currently makes the point
structurally — the folder holds Phase A's conclusions and none of its
reasoning — and one real first morning would carry it better than the
argument does. That is the first place to revisit if §5's three questions are
ever answered.

**The same warning applied to weeks 9 to 14 and has been partly lifted.**
Week 8 was rescued by the contract; the kick-off, the execution plan and the
meeting structure have no equivalent in the pool — `kick-off` runs to 12
across all three spellings and `project execution plan` as a phrase is 4.
What now stands behind weeks 10 to 14 instead is `TRACK8-ACCOUNT.md`: a
first-hand account of joining a running project with no integrated system, of
building the manpower, equipment and production structures by hand, of two
hundred rows a day reconciled across three record sets, and of a planning
system that lived in one person's knowledge until they left. That is better
material for those weeks than any of the eighteen books, and it is the first
of it to reach this project.

Weeks 10 to 14 should be written from it. Weeks 38 and 39 close on it.
