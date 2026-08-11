#!/usr/bin/env python3
"""Builds interfaces-week-12.html.

Template is interfaces-week-11.html.

This is the week the measurement exercise found missing: nothing in 144
articles covers combining several contractors' programmes, and the sources are
weak on it (master schedule 5, package schedule 0). Written from mechanism
rather than from sources, on the Reporting Phase B pattern.

The failure it rests on is precise: an integrated programme assembled by hand
cannot be recalculated, so it cannot answer the only question anybody asks of
it — what a delay does to the end date.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-11.html"
OUT = ROOT / "drafts" / "interfaces-week-12.html"

TITLE = "Integrating package programmes — detail, data dates and calendars that differ"
DESC = ("Three contractors submit three programmes at three levels of detail, on three data dates, "
        "against three calendars. Why the integrated version is a drawing rather than a network.")
OG = "A picture of a programme"
SHARE = ("The integrated programme cannot be recalculated, so it cannot tell you what a delay does. "
         "It is a drawing of an intention.")
CRUMB = "Three programmes, one project"
H1 = "A picture of a programme."

BODY = '''<h2 style="margin-top:0;">A picture of a programme</h2>
                            <p>Three contractors submit three programmes. One has four thousand activities, one has four hundred, and the third has eighty bars covering the same eighteen months.</p>
                            <p>Somebody is asked to produce an integrated programme, and what comes back is a bar chart assembled by hand: the three sets of dates drawn on one page, with arrows between the points where the packages meet.</p>
                            <p>It looks like a programme and it is a picture of one. Nothing in it calculates. Move any bar and nothing downstream moves, because there is no network underneath &#8212; and the one question anybody ever asks of an integrated programme is what happens to the end date if this slips.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Four things that do not line up</h2>
                            <p>The reasons are mundane and they compound.</p>
                            <p><strong>Detail.</strong> A link from a three-week summary bar to a two-day activity carries no useful logic. Aggregating the detailed programme up to match the coarse one throws away exactly the sequence you needed; expanding the coarse one down is inventing activities the contractor never committed to.</p>
                            <p><strong>Data dates.</strong> Each party updates on its own cycle. Three updates taken on three different dates, drawn on one page, describe no single moment &#8212; which is the distinction <a href="reporting-week-16.html">Reporting Week 16</a> drew between a data date and a cut-off, appearing here three times at once.</p>
                            <p><strong>Calendars.</strong> Five-day, six-day, shift work, different public holidays for a foreign contractor. The same duration produces different finish dates, so a duration copied between programmes is not the same duration.</p>
                            <p><strong>Coding.</strong> Without a common area or system code there is no way to filter across the three, which means the integrated view can only ever be read as a whole.</p>

                            <h2>Why the drawing survives</h2>
                            <p>It survives because it answers the question it gets asked in the room.</p>
                            <p>At a monthly meeting somebody wants to see the packages against each other, and the picture does that adequately. It shows intent, it shows where the handovers are meant to be, and it fits on a page.</p>
                            <p>The failure appears the first time somebody asks a consequential question. A delivery has slipped by three weeks &#8212; what does that do to commissioning? The picture cannot answer it. Somebody works it out by hand, in a spreadsheet, from the three programmes, and produces a number that is an opinion.</p>
                            <p>Which is <a href="week-17.html">Schedule Week 17</a>&#39;s subject arriving from a new direction. A model with no logic is not a poor model. It is a diagram, and the diagram has been presented for a year as though it forecasts.</p>

                            <h2>Integrate at the interface, not the activity</h2>
                            <p>The version that works gives up on merging the programmes and connects them instead.</p>
                            <p>Take the boundary register from <a href="interfaces-week-10.html">week 10</a> and turn each interface into a pair of milestones: one party finishes something, the other starts something, and the handover is the link between them. Do that for every boundary and the result is a network of perhaps sixty or eighty milestones covering the whole project.</p>
                            <p>That model calculates. It is small enough to maintain, it contains no activity anybody has to agree to, and it answers the consequential question directly: move a milestone and the effect on every downstream package is computed rather than estimated.</p>
                            <p>What it does not do is show the work. That is correct and it is the point &#8212; the work is in each contractor&#39;s own programme, which is where it belongs and where it is being managed.</p>

                            <h2>What each party has to supply</h2>
                            <p>Three requirements, and they belong in the contract rather than in a request.</p>
                            <p>The agreed interface milestones must appear in each party&#39;s own programme, with the agreed identifiers, so the dates can be extracted rather than transcribed. This is the one that has to be imposed at award; asking for it afterwards means asking a contractor to restructure a programme they have already been working to.</p>
                            <p>Each submission must be current to a stated data date, and the integration model has one data date of its own that every contribution is aligned to. Where a party is a fortnight behind, that is visible rather than absorbed.</p>
                            <p>And the calendar for each party must be declared, so that dates rather than durations move between the models. A finish date carries its calendar with it. A duration does not.</p>

                            <h2>Who owns the model</h2>
                            <p>Not any of the contractors, since it contains their commitments to each other and each would prefer a version of it.</p>
                            <p>It sits where the interface register sits, for the same reason <a href="interfaces-week-11.html">last week</a> gave: project controls holds every party&#39;s programme at once and is the only function that can see all sixty milestones simultaneously.</p>
                            <p>And it carries the same limit. Owning the model is not authority to change anybody&#39;s dates. It is the ability to say, on the day a milestone moves, exactly which other parties are affected and by how much &#8212; which is the input every conversation about recovery needs and rarely has.</p>

                            <h2>Practical insight</h2>
                            <p>Count the activities in the largest and smallest programmes you hold. If the ratio is more than about ten to one, stop trying to merge them; you are not going to succeed and the attempt is consuming your month.</p>
                            <p>Instead, list every point where one party has to finish something before another can start. The list you end up with is your integration model, and on a job with a handful of packages it runs to a few dozen lines rather than a few thousand.</p>
                            <p>Build it as milestones with logic between them and nothing else. It will take you a week. Then the next time somebody asks what a three-week slip does to commissioning, you will press a button rather than open a spreadsheet, and the answer will be the same one tomorrow.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Programmes at four thousand, four hundred and eighty activities cannot be meaningfully merged.</li>
                            <li>Three updates on three data dates, drawn on one page, describe no single moment.</li>
                            <li>Different calendars mean a duration copied between programmes is not the same duration. Move dates instead.</li>
                            <li>Without common coding the integrated view can only be read as a whole.</li>
                            <li>The hand-drawn version answers the meeting-room question and cannot answer a consequential one.</li>
                            <li>Integrate at the interface: each boundary becomes a pair of milestones and a link.</li>
                            <li>Sixty to eighty milestones calculate, maintain and forecast. They deliberately do not show the work.</li>
                            <li>Interface milestones with agreed identifiers have to be imposed at award, not requested afterwards.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The interface milestone list with agreed identifiers &#183; the integration model and its own data date &#183; each party&#8217;s declared calendar.</p>

                            <h2>What is coming next</h2>
                            <p>A milestone model shows which parties are affected when a date moves. It does not say whose delay it was, and on a multi-package job that question has an uncomfortable answer.</p>
                            <p>Next week: access, sequencing, and the delay that belongs to no one.</p>'''

FIG_STYLE = ('<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;'
             'border:1px solid #e2e8f0;">\n                                    {svg}\n'
             '                                    <figcaption style="margin-top:16px;font-size:13px;'
             'color:#64748b;line-height:1.6;">{cap}</figcaption>\n                                </figure>')
SVG = '<svg viewBox="0 0 640 {h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">'
TH = ('style="text-align:left;padding:9px 12px;background:#f1f5f9;color:#334155;font-weight:700;'
      'border-bottom:1px solid #e2e8f0;"')
TD = 'style="padding:9px 12px;border-bottom:1px solid #f1f5f9;color:#475569;"'
COLS = ["Record", "Produced by", "Required quality", "Verified against", "Feeds"]
ROWS = [
    ["Interface milestone list", "Project controls", "Agreed identifiers, present in every party&#8217;s own programme",
     "The boundary register", "The integration model"],
    ["Integration model", "Project controls", "Milestones and logic only &#8212; no activity anybody must agree",
     "Each party&#8217;s submission", "Forecast &#183; recovery discussions"],
    ["Model data date", "Project controls", "One date, with every contribution aligned to it",
     "Each party&#8217;s data date", "Whether the forecast means anything"],
    ["Declared calendar per party", "Each contractor", "Working days and holidays, stated at award",
     "Their own submission", "Dates moving between models"],
]


def box(x, y, w, h, t, sub="", tone="plain"):
    fill, stroke, tc, sc = {"plain": ("#fff", "#cbd5e1", "#334155", "#64748b"),
                            "good": ("#ecfdf5", "#a7f3d0", "#047857", "#059669"),
                            "bad": ("#fef2f2", "#fca5a5", "#b91c1c", "#dc2626")}[tone]
    cx = x + w / 2
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>'
    o += f'<text x="{cx}" y="{y + 25}" text-anchor="middle" fill="{tc}" font-size="13" font-weight="700">{t}</text>'
    if sub:
        o += f'<text x="{cx}" y="{y + 44}" text-anchor="middle" fill="{sc}" font-size="11">{sub}</text>'
    return o


def head(t):
    return (f'<text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" '
            f'font-weight="700" letter-spacing="2">{t}</text>')


FIGURES = [
    ("the one question anybody ever asks of an integrated programme is what happens to the end date if this slips.",
     SVG.format(h=200) + head("THREE SUBMISSIONS, ONE PAGE")
     + box(16, 56, 190, 62, "4,000 activities", "detailed")
     + box(222, 56, 190, 62, "400 activities", "summary")
     + box(428, 56, 190, 62, "80 bars", "a picture")
     + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Drawn together by hand. Nothing calculates.</text>'
     + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">Move a bar and nothing downstream moves.</text>'
     + "</svg>",
     "Figure 1 &#8212; A link from a three-week summary bar to a two-day activity carries no logic worth having, which is why the merge is abandoned rather than done badly."),
    ("and produces a number that is an opinion.",
     SVG.format(h=190) + head("TWO QUESTIONS, ONE ANSWERABLE")
     + box(30, 50, 265, 84, "Show me the packages", "the picture does this", "good")
     + box(345, 50, 265, 84, "What does a slip do", "worked out by hand", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">The first question is why it survives. The second is why it should not.</text>'
     + "</svg>",
     "Figure 2 &#8212; A model with no logic is not a poor model. It is a diagram, and it has been presented for a year as though it forecasts."),
    ("the work is in each contractor&#39;s own programme, which is where it belongs and where it is being managed.",
     SVG.format(h=220) + head("INTEGRATE AT THE BOUNDARY")
     + box(24, 56, 170, 56, "A finishes", "milestone", "good")
     + box(236, 56, 170, 56, "Handover", "the link", "good")
     + box(448, 56, 170, 56, "B starts", "milestone", "good")
     + '<text x="320" y="146" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">Sixty to eighty of these, and the model calculates.</text>'
     + '<text x="320" y="172" text-anchor="middle" fill="#64748b" font-size="11.5">It contains no activity any contractor has to agree to.</text>'
     + "</svg>",
     "Figure 3 &#8212; Giving up on merging is what makes integration possible. What is connected is the commitments between parties, not the work inside each one."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>Four records, and the first one has to be a contract requirement rather than a '
          'request.</p>\n                            ' + table() + '\n                            '
          '<p>Agreed identifiers are what turn the model from transcription into extraction. Without '
          'them somebody retypes sixty dates every month, which is both a job nobody has time for '
          'and a source of errors that surface as programme disputes.</p>')


def main():
    if not TEMPLATE.exists():
        sys.exit("HATA: sablon bulunamadi")
    s = TEMPLATE.read_text(encoding="utf-8")

    body = BODY
    for anchor, svg, cap in FIGURES:
        if anchor not in body:
            sys.exit(f"HATA: figur capasi bulunamadi: {anchor[:50]}")
        body = body.replace(anchor, anchor + "</p>\n\n                                "
                            + FIG_STYLE.format(svg=svg, cap=cap)
                            + "\n\n                                <p>", 1)
    body = body.replace("<h2>Practical insight</h2>",
                        SYSTEM + "\n\n                            <h2>Practical insight</h2>", 1)

    i = s.index('<h2 style="margin-top:0;">')
    j = s.index("<h3>Enjoyed this lesson?")
    tail = s.rindex("</p>", i, j) + len("</p>")
    s = s[:i] + body + s[tail:]

    s = re.sub(r"<title>.*?</title>", f"<title>{TITLE} | The Project Control Hub</title>", s, 1, re.S)
    for k in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r"(<meta " + re.escape(k) + r' content=")[^"]*(")', r"\g<1>" + DESC + r"\g<2>", s, 1)
    for k in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(r"(<meta " + re.escape(k) + r' content=")[^"]*(")', r"\g<1>" + OG + r"\g<2>", s, 1)
    s = re.sub(r'<h1 class="article-title">.*?</h1>', f'<h1 class="article-title">{H1}</h1>', s, 1, re.S)

    old_share = ("Forty open interfaces, reported monthly for a year, none of them closed. The "
                 "reporting was immaculate. Nothing was being managed.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-11.html", "interfaces-week-12.html")
    s = s.replace('data-current-week="11"', 'data-current-week="12"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 12<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 12", s, 1)
    s = s.replace("Interfaces &#183; Week 11", "Interfaces &#183; Week 12")
    s = s.replace('<a href="interfaces-week-12.html">last week</a>',
                  '<a href="interfaces-week-11.html">last week</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-12.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-12.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
