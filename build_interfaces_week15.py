#!/usr/bin/env python3
"""Builds interfaces-week-15.html.

Template is interfaces-week-14.html.

The overlap risk flagged in the kickoff is with Reporting Week 25. The
separation is deliberate and structural. There, two figures produced inside
one organisation disagree and the reconciliation has an agreed outcome. Here
the figures are produced by separate companies, each one is also an opening
commercial position, and the aggregate the employer publishes is a sum of five
different measurement methods.

The failure the week rests on is the aggregate: a project progress figure
summed from packages measured five ways is the headline number on the monthly
report and nobody can defend it.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-14.html"
OUT = ROOT / "drafts" / "interfaces-week-15.html"

TITLE = "Aggregating progress across packages — five methods, one headline figure"
DESC = ("Five contractors measure progress five ways. The project figure on the front of the monthly "
        "report is their sum, and it is a number with no defensible meaning.")
OG = "Sixty-one percent of what"
SHARE = ("Five packages, five measurement methods, one project percentage on the front page. Adding "
         "them produced a number nobody can define."
         )
CRUMB = "Progress and valuation collide"
H1 = "Sixty-one percent of what."

BODY = '''<h2 style="margin-top:0;">Sixty-one percent of what</h2>
                            <p>The monthly report opens with a project progress figure. It came from five packages: one measuring by installed quantity, one by cost expended against budget, one by milestones achieved, one by weighted deliverables, and one by an engineer&#39;s judgement.</p>
                            <p>Each of those is a legitimate method and <a href="cost-week-11.html">Cost &amp; Cash Week 11</a> covers all of them. Each contractor is measuring correctly by their own rules.</p>
                            <p>The figure on the front page is their weighted sum, and it is not a percentage of anything. Ask what it would take to move it by one point and there is no answer, because the question has five different answers that cannot be combined.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Why this is not the single-contract problem</h2>
                            <p><a href="reporting-week-25.html">Reporting Week 25</a> dealt with progress and valuation disagreeing, and the resolution there was a meeting: two functions inside one organisation, sharing a cut-off calendar, reconciling to an agreed outcome.</p>
                            <p>Two things change when the figures come from separate companies.</p>
                            <p>The first is that each figure is also a commercial position. A contractor&#39;s progress figure supports their application for payment. The Engineer&#39;s assessment supports the employer&#39;s cash position. Neither party is being dishonest and neither is disinterested, and there is no meeting at which the two become one number.</p>
                            <p>The second is that nobody owns the aggregate. Each contractor is accountable for their own figure and none of them for the sum. It is assembled by whoever produces the monthly report, from five inputs prepared to five definitions, and its accuracy is nobody&#39;s obligation.</p>

                            <h2>The gap that is not a disagreement</h2>
                            <p>A useful distinction gets lost when everything is treated as a dispute.</p>
                            <p>Some of the difference between a contractor&#39;s figure and a certified valuation is work that has been done and cannot yet be evidenced &#8212; installed but not inspected, complete but not surveyed, delivered but not signed for. That is not disputed work. It is work in a queue, and it will be certified next month.</p>
                            <p>The rest is genuine disagreement about what was built or what it is worth, and that is a much smaller number than the headline gap suggests.</p>
                            <p>Splitting the two changes the conversation. A gap that is eighty percent evidence lag and twenty percent dispute is a records problem with a small commercial tail. Reported as one figure, it looks like a large commercial dispute and gets escalated as one.</p>

                            <h2>Making the aggregate mean something</h2>
                            <p>The aggregate can be made defensible, and the requirement goes in at award rather than being negotiated later.</p>
                            <p>Every package reports physical progress on a stated method, and where a contractor uses something else internally, they convert. Weighting is by contract value, stated once, so a large package cannot be diluted by a small one moving quickly.</p>
                            <p>And the denominator is fixed the way <a href="reporting-week-7.html">Reporting Week 7</a> fixed it within one contract: progress is measured against a current approved quantity, and when scope changes the denominator changes visibly rather than quietly.</p>
                            <p>None of that is difficult. It is simply a decision that has to exist before five contractors have each built a reporting system around their own habits.</p>

                            <h2>On a project already running</h2>
                            <p>Where the packages are let and the methods are established, imposing one method is not available and pretending otherwise wastes a year.</p>
                            <p>What is available is disclosure. State on the report which method each package uses, next to its figure. The aggregate stays where it is; what changes is that a reader can see it is a composite, and the number stops being quoted as though it were a measurement.</p>
                            <p>That sounds like a small thing and it is the difference between a figure that misleads and one that informs. It also has an effect nobody expects: once the methods are printed side by side, the question of why they differ tends to get asked by somebody senior enough to settle it.</p>

                            <h2>What to do with the number you have</h2>
                            <p>Two habits make an unreliable aggregate survivable.</p>
                            <p>Report movement rather than level. A composite figure is unreliable as an absolute and considerably more reliable as a trend, because the method errors are roughly constant month to month and largely cancel in the difference.</p>
                            <p>And keep the packages visible underneath. Five separate percentages, each defensible in its own terms, carry more information than one number that is defensible in none. The single figure exists because somebody wants one line; the five exist because that is what is actually known.</p>

                            <h2>Practical insight</h2>
                            <p>Find out which method each package on your project uses to produce the percentage you receive. Ask the question directly, package by package.</p>
                            <p>You will get three or four different answers and at least one person who is not certain. That uncertainty is worth finding, because their figure is going into your aggregate every month.</p>
                            <p>Then take your last report and add one column beside each package: the method. Nothing else changes and your headline stays the same. The next person who quotes your project percentage in a meeting will see what it is made of, which is the whole of what you can do about it this month.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Five packages measuring five legitimate ways produce an aggregate that is a percentage of nothing.</li>
                            <li>Each contractor is measuring correctly by their own rules, and the sum is still meaningless.</li>
                            <li>Across companies, every figure is also an opening commercial position. There is no meeting where two become one.</li>
                            <li>Nobody owns the aggregate. Each party owns their own figure and none of them the sum.</li>
                            <li>Part of the gap to a certified valuation is evidence lag, not dispute, and it can be the larger part.</li>
                            <li>Reported as one number it looks like a commercial dispute and gets escalated as one.</li>
                            <li>Fix the method, the weighting and the denominator at award. Afterwards it cannot be imposed.</li>
                            <li>On a running project, disclose the method beside each figure and report movement rather than level.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The measurement method stated per package &#183; the weighting basis for the aggregate &#183; the split of the valuation gap into evidence lag and dispute.</p>

                            <h2>What is coming next</h2>
                            <p>Progress is one number arriving from several organisations. Cost is another, and it arrives from books kept by companies with their own accounting periods and their own reasons for what goes in them.</p>
                            <p>Next week: the cost that arrives from another company&#39;s ledger.</p>'''

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
    ["Measurement method per package", "Each contractor", "Stated once and printed beside the figure",
     "Their own procedure", "Whether the aggregate can be read"],
    ["Weighting basis", "Project controls", "By contract value, fixed, not recalculated monthly",
     "The contracts", "The aggregate figure"],
    ["Denominator per package", "Project controls", "Current approved quantity, restated visibly on scope change",
     "The change register", "Every percentage reported"],
    ["Valuation gap split", "Project controls with commercial", "Evidence lag separated from genuine dispute",
     "Inspection and survey records", "Escalation &#183; cash forecast"],
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
    ("because the question has five different answers that cannot be combined.",
     SVG.format(h=210) + head("FIVE METHODS, ONE HEADLINE")
     + box(10, 52, 120, 60, "Quantity", "package A")
     + box(136, 52, 120, 60, "Cost", "package B")
     + box(262, 52, 120, 60, "Milestone", "package C")
     + box(388, 52, 120, 60, "Deliverables", "package D")
     + box(514, 52, 116, 60, "Judgement", "package E")
     + box(210, 138, 220, 46, "61%", "the front page", "bad")
     + "</svg>",
     "Figure 1 &#8212; Every input is measured correctly by its own rules. The sum is a percentage of nothing, and it is the number people quote."),
    ("there is no meeting at which the two become one number.",
     SVG.format(h=200) + head("WHY THE RECONCILIATION IS DIFFERENT")
     + box(24, 52, 270, 76, "Inside one company", "two functions, one cut-off", "good")
     + box(346, 52, 270, 76, "Across companies", "each figure a position", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">Nobody is dishonest. Nobody is disinterested either.</text>'
     + "</svg>",
     "Figure 2 &#8212; The single-contract version ends in an agreed number. This one ends in two numbers and a negotiation, which is a different exercise with a different output."),
    ("Reported as one figure, it looks like a large commercial dispute and gets escalated as one.",
     SVG.format(h=190) + head("SPLITTING THE VALUATION GAP")
     + box(30, 50, 265, 84, "Evidence lag", "done, not yet certified", "good")
     + box(345, 50, 265, 84, "Genuine dispute", "the smaller part", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">A records problem with a small commercial tail, or a crisis. Same numbers.</text>'
     + "</svg>",
     "Figure 3 &#8212; Work in a queue for inspection is not disputed work. Separating the two changes who has to deal with the gap and how urgently."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The first row costs nothing and is the one most reports omit. Printing the method '
          'beside the figure is the difference between a composite that informs and one that '
          'misleads.</p>\n                            ' + table() + '\n                            '
          '<p>The last row is the one that changes how a gap is treated. Escalating an evidence lag '
          'as a commercial dispute consumes senior attention on a problem that resolves itself, and '
          'it makes the genuine disagreement underneath harder to see.</p>')


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

    old_share = ("The driving activity on the project is being carried out in a factory you have "
                 "never visited, under an order you are not party to, by a vendor who owes you nothing.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-14.html", "interfaces-week-15.html")
    s = s.replace('data-current-week="14"', 'data-current-week="15"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 15<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 15", s, 1)
    s = s.replace("Interfaces &#183; Week 14", "Interfaces &#183; Week 15")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-15.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-15.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
