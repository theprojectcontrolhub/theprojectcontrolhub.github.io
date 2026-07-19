# The Project Control Hub — working notes

Conventions that are easy to lose between sessions. Everything here is enforced
by `tools/check_site.py` unless marked *(judgement)*.

```bash
python3 tools/check_site.py            # full, includes copyright n-gram scan
python3 tools/check_site.py --quick    # skip copyright (much faster)
```

Run it after any content change. It exits non-zero on failure.

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

---

## 3. Copyright *(partly judgement)*

Sources live in `/mnt/user-data/uploads/` — three FIDIC 2017 books, PMI risk
standards, PMBOK 8, Cooper, and four academic texts.

**Free to use:** clause numbers; official clause headings in italics as a citation
(*Unforeseeable Physical Conditions*); the effect of a clause in our own words;
terminology; attributed findings; anything about our own invented $1M job.

**Never:** a quotation of any length from a source; redrawing a source figure;
following a source's teaching order or chapter sequence; carrying a numeric
example across.

The working test: write the sentence from memory with the source closed.

`check_site.py` scans every article against a 10-gram pool built from all eleven
PDFs. Current state: **zero** 10-word overlaps. The longest overlaps anywhere are
seven words, and each is either a term of art, a legal definition that cannot be
paraphrased away (the *Unforeseeable* test in 1.1.85), or ordinary English.

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
hard-code them again.

---

## 7. Open items

- YouTube link is still a `https://youtube.com` placeholder on every page
- `logo-lockup.png` (471 KB) is shipped but unused
- `learn.html`'s Track 1 → 2 bridge note does not mention that Cost & Cash Week 6
  supersedes the Track 1 treatment of CPI
- Track 4 (Claims & Delay Analysis) is promised by name at the end of
  Risk Weeks 15 and 18
