# Track 8 — The Life of a Project · kickoff

Written 2026-08-12, at the point where Interfaces was finished and published
and nothing of Track 8 had been drafted. Everything below is either measured or
already printed on the site. Where something is a judgement it says so.

---

## 0. Read in this order

1. This file.
2. `NOTES.md` §1 (numbers), §4 (voice), §5 (article shape), §10 (the Reporting
   decisions — most of them apply here unchanged).
3. `interfaces-week-17.html`, the last article of Track 7. It hands over to this
   track in print and the wording constrains what Track 8 must contain.
4. Two or three finished articles for shape rather than subject.
   `reporting-week-9.html` and `interfaces-week-13.html` are representative.

---

## 1. What is already true and cannot be changed casually

**The subject is printed.** `interfaces-week-17.html` closes with this, and it
is live:

> Seven tracks have taught methods and the conditions under which they hold.
> What none of them has shown is the order the work arrives in. A project is
> not a set of techniques applied in parallel. It starts before anybody is
> appointed, in an investment decision made by people the delivery team never
> meets. It passes through a tender, a mobilisation, an engineering phase that
> overlaps a procurement phase that overlaps construction, a commissioning
> sequence that inverts the priorities of everything before it, and a closure
> that determines whether any of the records were worth keeping. What comes
> next is that sequence: what happens at each stage, what feeds what, and
> which record is born where.

Three commitments in the last sentence — **what happens at each stage**,
**what feeds what**, **which record is born where** — and four more in the
paragraph before it, which are stronger because they are specific:

- the project **starts before anybody is appointed**, at an investment
  decision made by people the delivery team never meets
- engineering, procurement and construction **overlap**; they are not a
  sequence of finished phases
- commissioning **inverts the priorities of everything before it**
- closure **determines whether the records were worth keeping**

Those four are promises to a reader who has finished 160 articles. Each has to
land somewhere in the 36 weeks. The third is the sharpest and the least
covered by the current week list: nothing in Phase G currently argues that the
priorities invert, and that is the argument commissioning weeks usually miss.

**The name and number are printed.** `learn.html` and `index.html` both show
Module 08 · The Life of a Project, and the path figure marks it as the next
step. The chain currently ends `interfaces-week-17 → learn.html`, so week 17's
next-article block changes when the first article ships.

**The 36-week list in `curriculum.js` is a proposal.** It was trimmed from 52
when Reporting was created and sixteen weeks moved across. Nothing outside
`curriculum.js` and the learn page references the numbers, so it can move.

---

## 2. Scope, and the boundary that decides whether this works

This is the hardest track to keep honest, because a lifecycle survey can
absorb anything. Two rules hold it:

**It teaches order and handover, not technique.** Every method already has a
home. Float is Schedule, EVM is Cost & Cash, concurrency is Claims, where a
number comes from is Reporting, and what changes under several contracts is
Interfaces. When a week reaches a technique it names it, links it, and moves
on — exactly as the last two tracks do.

**Every week has to answer one of the three printed promises.** What comes
first, what feeds what, or what record is born here. A week that only
describes a phase is a survey chapter and does not belong.

The fourth rule from `NOTES.md` §10 still decides existence: **a week exists
only if it explains a failure.** "Commissioning is the process by which…" is a
definition. "The schedule is handed to a discipline that measures completion
differently, and the handover date means two things" is a failure.

**The most likely way this track goes wrong** is that it becomes a second pass
over the first seven — a summary tour. The defence is the record: if a week
cannot name a document that is born at that stage and did not exist before it,
the week is probably re-telling something.

---

> **Superseded 2026-08-19 by `TRACK8-SOURCES.md`.** The sources are now on
> disk and were measured with one stated method. Three of this section's
> judgements were wrong: performance tests are contract-sourced (*Tests on
> Completion* 177, *Tests after Completion* 98), demobilisation is
> contract-sourced (*Clearance of Site*, FIDIC 11.11), and `as-built` was two
> subjects counted as one. The week list in §4 was rebuilt on the new
> measurement. This section is kept as written because the addendum argues
> against it and both arguments matter.

## 3. The source position — good at both ends, thin in the middle

Measured across the full pool on 2026-08-12.

| Term | Count | Reading |
| --- | --- | --- |
| `work package` | 139 | very strong |
| `feasibility` | 110 | very strong |
| `lessons learned` | 106 | very strong |
| `investment decision` | 81 | strong |
| `work breakdown` | 66 | strong |
| `forecast` | 60 | strong |
| `business case` | 50 | strong |
| `as-built` | 49 | strong |
| `commissioning` | 42 | adequate |
| `front end` | 37 | adequate |
| `closeout` | 34 | adequate |
| `mobilization` (z) | 31 | adequate |
| `FEED` | 28 | adequate |
| `punch list` | 27 | adequate |
| `purchase order` | 27 | adequate |
| `execution plan` | 22 | thin |
| `handover` | 21 | thin |
| `archive` | 5 | weak |
| `kick-off` | 4 | weak |
| `taking over` | 3 | weak |
| `temporary works` | 2 | weak |
| `site logistics` | 2 | weak |
| `mechanical completion` | **0** | absent |
| `pre-commissioning` | **0** | absent |
| `performance test` | **0** | absent |
| `demobilisation` | **0** | absent |
| `laydown` | **0** | absent |
| `requisition` | **0** | absent |
| `design freeze` | **0** | absent |
| `change control board` | **0** | absent |
| `look ahead` | **0** | absent |

Four consequences.

**The front end is the best-sourced part of the track.** Weeks 2 to 6 have
real backing — feasibility, business case, investment decision and front-end
planning together are over 250 hits. This is unusual: on every previous track
the opening weeks were the thin ones.

**Phase G is the worst-sourced part of any track so far.** Mechanical
completion, pre-commissioning, performance test and demobilisation are all
**zero**. Six weeks (29–34) rest on `commissioning` 42, `punch list` 27,
`as-built` 49 and `handover` 21 between them. Write them from practice, as
Reporting's Phase B was written, and say so in the notes.

**Two terms are absent because of spelling.** `mobilisation` is 0 and
`mobilization` is 31; `punchlist` is 1 and `punch list` is 27. Search both
before concluding a subject is unsourced.

**Worth acquiring before writing weeks 29 to 33**: Killcross, *Process Plant
Commissioning* (IChemE) and the CII start-up research. Both were identified
during Reporting and neither was bought. They are the difference between a
commissioning week written from practice and one written from nothing.

---

> **Superseded 2026-08-19.** `curriculum.js` now carries 39 weeks in eight
> phases. The five weaknesses listed below were the right list; four of them
> are settled in `TRACK8-SOURCES.md` §4 and the fifth (forecasting) survives
> reframed.

## 4. The proposed 36 weeks

In `curriculum.js` as `LIFECYCLE`, all `upcoming`, seven phases plus an opener
and a capstone. Week 1 stands outside the phases: one drawing followed through
six hands, which is the track in miniature.

Known weaknesses to settle early rather than discover in week 20:

- **Weeks 21 and 22 overlap Reporting week 9 and Interfaces week 13.**
  Constraint removal and look-ahead have been covered twice already. The
  lifecycle version has to be about *when in the project* this starts and who
  hands it over, not about the six readiness tests again. If that cannot be
  sustained, cut both and the track is 34 weeks.
- **Week 25 (forecasting) overlaps Cost & Cash.** Same test: it survives only
  as *when the forecast becomes the number you are judged on*, which is a
  lifecycle question, not as method.
- **Weeks 26 to 28 (governance) overlap Interfaces week 8.** There it was
  across organisations; here it is inside one. Narrower and defensible, but
  the distinction has to be visible in the first paragraph.
- **Week 12 (document control) overlaps Reporting 13 and Interfaces 17.** This
  is the third pass. Either it is about *setting it up on day one* or it goes.
- **Phase E is two weeks and reads thin.** Consider folding week 24 into
  Phase D, where change on the ground actually happens.

---

## 5. Material already gathered, and what is missing

**From the source books.** The PMI Construction Extension is the strongest
single reference for this track and was under-used in Reporting. Halpin,
*Construction Management*, carries mobilisation and crew organisation.

**From the conversation.** The Akkuyu story — a planning system living in one
person's head, and the rebuild after they left — was earmarked for weeks 11
and 35 and has never been written. It is the best material available for the
capstone.

**What is missing and matters.** Weeks 7 to 14 describe the first months of a
job in a way only somebody who has joined one can write. The site has eight
years of that experience behind it and almost none of it has reached the page:
Track 7 was written entirely from structure, and the author confirmed the
articles are honest but contain no lived moment. **This track is the one that
suffers most from that.** Nobody can write "day one" convincingly from first
principles.

Three questions worth asking before week 7:

1. What was actually in the folder on the first day of a job, and what was
   missing that you needed by Friday?
2. What got decided at a kick-off meeting that turned out to matter, and what
   got deferred and never came back?
3. When you joined a project already running, what did you have to reconstruct
   before you could produce anything?

---

## 6. Conventions that are already decided

- **Prefix:** `lifecycle-week-N.html`, unpadded. **Not yet registered in
  `check_site.py`** — `TRACKS`, `own_pre`, the candidate-prefix tuple in the
  xref check, and `QUAL` (currently tracks 1–7) all need it *before* the first
  article. A half registration cost half a day on Reporting.
- **Article shape:** unchanged. **1,400–1,600 words**, three figures, System
  design, Practical insight, Key takeaways, Records born here. This file
  originally said 1,200–1,700 and `NOTES.md` §5 said 1,400–1,600; settled
  2026-08-19 in favour of §5, because 160 published articles were written to
  it and a wider band on track 8 would show as a break in rhythm rather than
  as freedom.
- **The data dictionary continues.** Columns fixed: `Record | Produced by |
  Required quality | Verified against | Feeds`. 186 rows exist across Reporting
  and Interfaces; this track extends the same table.
- **Voice:** contractions 5–9 per thousand, second person in Practical insight
  40–50 per thousand. `check_site.py` reports both.
- **No figures.** No invented quantities anywhere.
- **Case study — decided 2026-08-19: single contract, one Employer, one
  Engineer.** The $1M job returns to the shape Tracks 1–6 assumed, and Track
  7's package re-let is treated as the variant it was. Three reasons, in
  order of weight. The front-end weeks have to describe *one* investment
  decision and *one* award, and a packaged job has several of each, which
  turns weeks 3 to 7 into interface weeks that Track 7 has already written.
  The finishing weeks turn on a single Taking-Over Certificate and a single
  Performance Certificate; under packages there is one per package and the
  argument becomes Track 7's again. And the reader arriving from Interfaces
  has just spent seventeen weeks on plurality — returning to one contract is
  what makes the lifecycle visible rather than the boundaries.
  **The exception is week 32**, taking over in parts, where the whole subject
  is that one contract produces several handover dates. That is partial
  taking-over under a single contract, not several contracts, so the case
  study holds.
- **Dates:** Interfaces ends 11 Jul 2029. Week 1 would be 18 Jul 2029.

---

## 7. Publishing checklist

**This list and `NOTES.md` §6 are the same list.** They had drifted apart —
§6 ended at `check_site.py` and this one did not have
`check_status_strings.py` at all, which the addendum §3 asked for. Merged
2026-08-19. Change one, change the other, or delete one.

1. Article written to `drafts/`, passing the voice metrics.
2. `curriculum.js`: `status: "live"`, `page`, `date`. **The list on
   `learn.html` renders from here — copying the file to the root does nothing
   on its own.**
3. Chain: the previous article's `next-article` block points at the new one.
   Interfaces week 17 currently points at `learn.html`.
4. `sitemap.xml`.
5. Cache bump on `curriculum.js?v=` across every page. Bump with a direct
   write, not through the build script's `write()` — see `NOTES.md` §6 for
   why, and verify with `grep -o "curriculum.js?v=[0-9]*" index.html` rather
   than trusting the console.
6. `python3 tools/fix_article_meta.py` — breadcrumb, `data-track`, date.
7. `python3 tools/check_site.py --quick`.
8. `python3 tools/check_status_strings.py`. The only thing that catches a
   stale hand-written status string; `start-here.html` sat wrong for three
   tracks because nothing did.
9. Run the build script a second time. It must report `0 dosya`.
   **Only for the newest article.** Each build sets its own `next-article` to
   `learn.html` and the following week's script repoints it, so re-running an
   older script always reports `1 dosya` and the pipeline is only stable after
   the whole sequence has run in order. Verified 2026-08-20: running weeks
   8, 9, 10 twice gives `1, 1, 0` both times, which is convergence rather
   than a defect.
10. `drafts/` removed once the articles are at the root.

## 8. The defect this project keeps producing

Every article is built from the previous one, so **any field not explicitly
rewritten is inherited silently**. Four separate instances reached the live
site before anybody noticed:

- 27 Claims articles: breadcrumb said "Week 1"
- 28 Claims articles: `data-track="4"`, inherited from Contract
- 25 Reporting articles: author line dated to week 8's publication date
- 17 Interfaces articles: breadcrumb, `data-track`, date, and a hardcoded
  `renderTrack6Sidebar` call that rendered the wrong track's week list

All are fixed. Two tools now exist and should be run after any new article:
`tools/fix_article_meta.py` (breadcrumb, `data-track`, date) and
`tools/fix_sidebar_renderer.py` (the sidebar now reads `data-track` rather
than naming a function).

**`check_site.py` catches none of this.** It checks links, tags, chain,
sitemap and voice. It does not check whether a page agrees with itself about
which track and week it belongs to. Adding that — comparing filename,
breadcrumb, `data-track`, badge and date against `curriculum.js` — is roughly
twenty lines and would close the class permanently. Worth doing before week 1
rather than after week 30.

---

## 9. Open, and not this track's job

- **136 of 160 live articles carry future dates**, up to Jul 2029, while today
  is Aug 2026. The homepage shows a Jul 2029 article as the latest. Deferred
  deliberately while the skeleton is built.
- **The repository was published with the working files in it** — 66 Python
  scripts, `NOTES.md`, `canon.json`, `drafts/` and a 200 KB preview page. A
  reader concluded from this that the site was a Turkish-language platform,
  because 69 of 72 working files are written in Turkish. `dist/` and
  `.gitignore` now exist to prevent it; the deletion list is
  `SILINECEKLER.md`.
- **The paywall is client-side.** Anyone with the URL can read every article.
- **Two weeks are dated Saturday and 158 Wednesday**, with an eleven-day gap at
  Schedule week 3 where the publication day changed. Cosmetic, and a one-line
  fix if wanted.

---

## 10. The four questions used on every sentence

From `NOTES.md` §10. They matter most at the start, when the temptation is to
accept material that reads well.

1. **Is this the author's voice, or book language?**
2. **Does it work on site, or only in theory?**
3. **Is the idea in the right week?**
4. **Which failure does this principle explain?**

And two supporting rules:

**Separate what happened from what was concluded.** The memory is the
author's and is not edited. A composite scene is allowed and must say it is
one, but it may not contain a sentence nobody said. During Track 7 seven
frequency claims — "usually", "most projects" — were written from inference
and had to be rewritten as structural claims. Watch for that word.

**Do not mistake the symptom for the problem.** WhatsApp was not the problem;
an untracked request was. A dashboard was not the problem; the data model was.

## 11. Full-track audit, 2026-08-25

`tools/audit_track8.py` was written after the track was complete and run
across all thirty-nine articles. It covers what `check_site.py` does not:
per-week metrics against the §6 bands, inference-based frequency claims,
forward and dead links inside the body, structural completeness, and repeated
phrasing across weeks.

**What it found, and what it cost to fix.**

*The word count had drifted and nobody was watching the floor.* Twenty-three
weeks (15–38) sat between 1,289 and 1,398 words of body prose, under the
1,400 floor §6 makes binding, and two (8 and 9) sat over the 1,600 ceiling.
The drift began at week 15 and ran unbroken to week 38, which is the signature
of a check being reported rather than applied: each week was measured, the
number was read, and "in band" was said about a number that was not. Fixed by
adding one or two substantive paragraphs to a named thin section in each
affected week and trimming weeks 8 and 9. All thirty-nine now sit between
1,400 and 1,615.

*Eight genuine frequency claims survived publication*, in weeks 1, 3, 31, 36
and 39 — the same defect the per-week measurement step was created to catch,
appearing in the weeks written before that step was routine and in three
written after it. Three more were introduced by the audit's own repair
paragraphs and caught on the second pass.

*Week 1 carried nine takeaways* against the 10–13 convention. One added.

**Calibration.** The first run reported 166 findings of which 89 survived a
false-positive pass and 3 were real once scope words were separated from
frequency claims. Three detectors were wrong and are now documented in the
script: `<p style=...>` was not counted as an opening tag; the `next-article`
navigation link was read as a forward reference; and `everybody` / `every
time` were treated as frequency claims when they describe a defined situation
rather than a rate. Week 1's six-row table is deliberate — one row per record
born along the drawing's journey — and is now excepted by name.

**Run it after any edit to a Track 8 article.** `python3
tools/audit_track8.py` prints a metrics table and a categorised finding list;
zero findings is the passing state.
