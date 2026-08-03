#!/usr/bin/env python3
"""Appends section 10 to NOTES.md: the Reporting track's design decisions.

The articles will still be readable in six months. The reasons for the
decisions behind them will not, which is the whole point of writing this now
rather than later.

Idempotent.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SECTION = '''

## 10. Reporting &mdash; design decisions *(judgement &mdash; 2026-08-05)*

Written while the track was being drafted, because the articles will survive
and the reasoning behind them will not.

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

### Why 21 is empty

There is no week 21. Dashboards were scoped, the available material turned
out to be either taxonomy or already covered &mdash; audience levels are week
20, indicator selection is week 22, and the tool itself is the digital phase
&mdash; and no argument was left that the week could carry.

A weak week costs more than a missing one. It is left out rather than filled,
and week 20 hands forward to the indicators without naming a number.

If it is written later it needs a reason that is not "a dashboard should be
clear". Something like what a dashboard structurally cannot express &mdash;
causation, confidence, what is missing &mdash; would carry a week. Nothing
below that will.

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
  and `check_site.py`'s `week-(\\d+)`. Zero-padding was proposed and dropped
  for that reason.
- The 25 drafts are in `drafts/` and out of the chain and sitemap. Week 8 was
  written first because its material was ready; publication order is 1 upward.
- `check_site.py` registration for Reporting and Interfaces is done. `QUAL`
  now spans tracks 0&ndash;7.
'''


def main():
    p = ROOT / "NOTES.md"
    s = p.read_text(encoding="utf-8")
    if "## 10. Reporting" in s:
        print("  = NOTES.md: zaten uygulanmis\n\n0 dosya")
        return
    p.write_text(s.rstrip() + SECTION + "\n", encoding="utf-8")
    print("  + NOTES.md: bolum 10 eklendi\n\n1 dosya")


if __name__ == "__main__":
    main()
