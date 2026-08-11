#!/usr/bin/env python3
"""Builds interfaces-week-16.html.

Template is interfaces-week-15.html.

The overlap to avoid is Reporting Week 14, where a commercial team inside the
same organisation feeds project controls and the basis of an accrual can be
asked about down the corridor. Here the ledger belongs to another company: the
basis is theirs, the calendar is corporate rather than project, and the chart
of accounts is a translation.

The failure: a cost report that moves because somebody else closed a quarter,
and nobody on the project can explain the movement.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-15.html"
OUT = ROOT / "drafts" / "interfaces-week-16.html"

TITLE = "Cost from another company's ledger — corporate calendars and borrowed codes"
DESC = ("Cost arriving from a separate company carries their accounting period, their chart of "
        "accounts and their judgement about when something is recognised. None of it is yours.")
OG = "It moved because somebody closed a quarter"
SHARE = ("The cost report jumped and nothing happened on site. Another company closed its quarter, "
         "and the explanation is in accounts nobody on the project can see.")
CRUMB = "Another company's ledger"
H1 = "It moved because somebody closed a quarter."

BODY = '''<h2 style="margin-top:0;">It moved because somebody closed a quarter</h2>
                            <p>The cost report shows a sharp movement in one package. Nothing happened on site that month &#8212; the same crews, the same progress, no variations of any size.</p>
                            <p>The explanation, when it eventually arrives, is that the contractor&#39;s financial year ended and a batch of accruals was recognised that had been sitting unposted for two months.</p>
                            <p>Nothing improper occurred. A company closed its books to its own calendar, as it is required to do. What moved was your figure, for a reason that has nothing to do with your project and cannot be found anywhere in your records.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>The basis you cannot ask about</h2>
                            <p><a href="reporting-week-14.html">Reporting Week 14</a> dealt with commitments, accruals and invoices arriving from the commercial team. The advice there rested on something quiet: when an accrual looked odd, you could go and ask how it was built.</p>
                            <p>Across companies that route is closed. What arrives is a figure in a report, and the working underneath it is internal to a business that has no obligation to explain its accounting to a customer.</p>
                            <p>So an accrual that seems high cannot be interrogated the way <a href="cost-week-10.html">Cost &amp; Cash Week 10</a> assumes. It can be compared against progress, against invoices and against what the site says was done &#8212; the corroboration from <a href="reporting-week-8.html">Reporting Week 8</a> applies directly &#8212; but it cannot be traced.</p>

                            <h2>Their calendar is not a project calendar</h2>
                            <p>The second difference produces the movement in the opening.</p>
                            <p>A company&#39;s reporting periods exist for its own purposes: statutory accounts, group consolidation, tax. Those dates were set before your project started and will outlast it, and they are not going to move for your monthly report.</p>
                            <p>Around them, judgement is exercised. What gets recognised in one period rather than the next is an accounting decision, taken for reasons internal to that business, entirely legitimately. The effect on your cost report is a side effect nobody intended and nobody will explain.</p>
                            <p>Which makes it a different problem from the two cut-off dates in <a href="reporting-week-16.html">Reporting Week 16</a>. There, two dates were misaligned and reconciling them was administrative. Here the misalignment is deliberate on the other side and is not available for negotiation.</p>

                            <h2>A chart of accounts you are borrowing</h2>
                            <p>The third difference is structural and it degrades slowly.</p>
                            <p>Another company records cost against their own code structure, built for their business. What you receive has been mapped to yours by somebody, once, probably at the start, and that mapping is a translation with losses in it.</p>
                            <p>It is also unmaintained. New codes appear on their side as the work develops. Where they do not map cleanly, the cost lands in whatever bucket is closest, and after a year the closest bucket contains a category of spend nobody named. <a href="cost-week-6.html">Cost &amp; Cash Week 6</a> built the code of accounts as the spine of cost control; here you are using somebody else&#39;s spine through an adapter.</p>

                            <h2>When their cost is your cost</h2>
                            <p>On a reimbursable or target-cost arrangement the position sharpens considerably.</p>
                            <p>Their ledger is not an input to your report &#8212; it is the thing being paid. Every judgement about what is chargeable, how overhead is allocated and when something is recognised comes straight through to the outturn, and on a target cost it comes through to the share.</p>
                            <p>Contracts on that basis carry audit rights, and they are the answer. But exercising them is a commercial act with a cost of its own: it is read as an accusation, it consumes weeks, and it changes the relationship. Which is why the moment they are finally exercised tends to be the moment the relationship has already gone, and the records are two years old.</p>
                            <p>The alternative is to agree the basis at the start, in writing, at a level of detail that feels excessive at the time &#8212; what is chargeable, what rate, what overhead treatment, what evidence accompanies each claim. That conversation is cheap before the first invoice and impossible after the fiftieth.</p>

                            <h2>What to publish</h2>
                            <p>One habit makes the whole of this manageable, and it is a reporting decision rather than an accounting one.</p>
                            <p>Keep their number and your restatement of their number as separate lines. What they reported, and what you are carrying after adjusting for period differences, mapping and known lags.</p>
                            <p>That looks like duplication and it is the only way the report survives a question. When somebody asks why the figure moved, the answer is visible on the page: their number moved for their reasons, your carried figure did not, and the difference is stated. Publishing one blended number means the movement has to be explained from memory every time.</p>

                            <h2>Practical insight</h2>
                            <p>Find out the financial year end of every company sending you cost, which is public information for most of them and a single question for the rest.</p>
                            <p>Mark those dates on your own reporting calendar. In the months around them you will see movement in your cost report that has no site cause, and you will know in advance which package it will come from.</p>
                            <p>Then take one large accrual you received last month and try to corroborate it &#8212; against progress, against what the site says was done, against invoices you have actually received. You will not be able to trace it, and that is expected. What you will find out is whether it is plausible, which is the only test available to you and a great deal better than accepting it because it arrived in a report.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A cost figure can move sharply with nothing happening on site, because another company closed its books.</li>
                            <li>Across companies an accrual cannot be traced. It can only be corroborated against progress, site records and invoices.</li>
                            <li>Their reporting periods exist for statutory and group purposes and will not move for your monthly report.</li>
                            <li>Recognition judgements are legitimate and internal, and the effect on your report is a side effect nobody will explain.</li>
                            <li>The chart of accounts you receive is a mapping from theirs, made once and rarely maintained.</li>
                            <li>Unmapped codes land in the nearest bucket, which after a year holds a category of spend nobody named.</li>
                            <li>On reimbursable and target-cost work their ledger is the thing being paid, and audit rights are the answer.</li>
                            <li>Publish their number and your restatement as separate lines. A blended figure has to be explained from memory.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> Each party&#8217;s financial year end on the reporting calendar &#183; the code mapping and its review date &#183; their reported figure and your carried figure, side by side.</p>

                            <h2>What is coming next</h2>
                            <p>Cost and progress both arrive as numbers. The last thing that crosses an organisational boundary is a document, and it has to reach a person holding a drawing on a wall.</p>
                            <p>Next week: document control across six firms &#8212; distribution rather than transmittals.</p>'''

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
    ["Financial year end per party", "Project controls", "Marked on the reporting calendar, all parties",
     "Public filings or one question", "Expected movement in cost"],
    ["Code mapping", "Project controls with commercial", "Reviewed on a date, not built once and left",
     "Their reported codes", "Cost report &#183; forecast"],
    ["Their reported figure", "The other company", "As received, unadjusted",
     "Their submission", "The audit trail"],
    ["Your carried figure", "Project controls", "Adjusted for period, mapping and known lag, with the adjustment shown",
     "Progress and invoices", "Cost report &#183; outturn"],
    ["Reimbursable basis", "Contracts, at award", "What is chargeable, at what rate, with what evidence",
     "The contract", "Every invoice thereafter"],
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
    ("cannot be found anywhere in your records.",
     SVG.format(h=190) + head("A MOVEMENT WITH NO SITE CAUSE")
     + box(24, 52, 270, 76, "On site", "same crews, same progress", "good")
     + box(346, 52, 270, 76, "In the report", "a sharp movement", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">A company closed its books to its own calendar, as it must.</text>'
     + "</svg>",
     "Figure 1 &#8212; Nothing improper happened. The figure that moved was yours, for a reason that exists entirely outside your project."),
    ("but it cannot be traced.",
     SVG.format(h=200) + head("WHAT YOU CAN DO WITH AN ODD ACCRUAL")
     + box(24, 52, 270, 76, "Inside one company", "ask how it was built", "good")
     + box(346, 52, 270, 76, "Across companies", "corroborate, not trace", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">Progress, site records and invoices are the only instruments left.</text>'
     + "</svg>",
     "Figure 2 &#8212; The working belongs to a business with no obligation to explain its accounting to a customer, which removes the route the single-company version relies on."),
    ("after a year the closest bucket contains a category of spend nobody named.",
     SVG.format(h=200) + head("A MAPPING THAT DEGRADES")
     + box(16, 56, 190, 60, "Their codes", "built for their business")
     + box(222, 56, 190, 60, "The mapping", "made once", "bad")
     + box(428, 56, 190, 60, "Your codes", "the spine of control")
     + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">New codes appear on their side and land in the nearest bucket.</text>'
     + "</svg>",
     "Figure 3 &#8212; The translation is lossy on day one and gets worse, because nothing about the arrangement makes anybody responsible for maintaining it."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The third and fourth rows are one idea: never let their figure and your figure become '
          'the same line.</p>\n                            ' + table() + '\n                            '
          '<p>Keeping both looks like duplication until the first month somebody asks why the cost '
          'jumped. With two lines the answer is on the page; with one it has to be reconstructed by '
          'whoever happens to remember.</p>')


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

    old_share = ("Five packages, five measurement methods, one project percentage on the front page. "
                 "Adding them produced a number nobody can define.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-15.html", "interfaces-week-16.html")
    s = s.replace('data-current-week="15"', 'data-current-week="16"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 16<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 16", s, 1)
    s = s.replace("Interfaces &#183; Week 15", "Interfaces &#183; Week 16")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-16.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-16.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
