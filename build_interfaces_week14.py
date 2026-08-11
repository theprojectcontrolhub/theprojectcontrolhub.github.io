#!/usr/bin/env python3
"""Builds interfaces-week-14.html.

Template is interfaces-week-13.html.

Reporting Week 5 covered getting a date out of procurement and what a revised
promise is worth. This week is the different problem: the driving path running
through an order the employer placed with a vendor the contractor has no
relationship with, so the float being consumed is in somebody else's factory
programme and invisible until the ship does not arrive.

Sources are the weakest on the track — long lead 12 — so the frame is widened
to purchase order, expediting and vendor, as the kickoff anticipated.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-13.html"
OUT = ROOT / "drafts" / "interfaces-week-14.html"

TITLE = "Free-issue equipment on the critical path — float in somebody else's factory"
DESC = ("When the employer buys the long-lead equipment directly, the driving path runs through an "
        "order you are not party to, and the float being consumed is in a vendor's programme.")
OG = "The critical path is in a factory"
SHARE = ("The driving activity on the project is being carried out in a factory you have never "
         "visited, under an order you are not party to, by a vendor who owes you nothing.")
CRUMB = "Procurement on the critical path"
H1 = "The critical path is in a factory."

BODY = '''<h2 style="margin-top:0;">The critical path is in a factory</h2>
                            <p>Run the schedule and the driving path goes through the main vessel. Not through erecting it &#8212; through manufacturing it, in a works two thousand kilometres away, under an order the employer placed eighteen months ago.</p>
                            <p>You are not a party to that order. You have never met the vendor, you have no right to their programme, and the only information you receive is a date that arrives second-hand and changes without explanation.</p>
                            <p>Everything <a href="week-13.html">Schedule Week 13</a> teaches about the critical path assumes you can act on the driving activity. Here you cannot even see it.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Why the item is bought this way</h2>
                            <p>It is a rational decision and worth understanding rather than resenting.</p>
                            <p>Long-lead equipment has to be ordered before the construction packages are tendered, because its manufacturing time is longer than the time available afterwards. The employer places it early to protect the programme, and then free-issues it to whichever contractor is later appointed to install it.</p>
                            <p>The alternative &#8212; waiting to appoint a contractor who then places the order &#8212; adds their procurement period to a lead time that was already the constraint. So the early order is the right answer to the problem it solves, and it creates a different one.</p>

                            <h2>Float you cannot see</h2>
                            <p>A vendor&#39;s programme has structure in it: design, material procurement, fabrication, testing, painting, packing, shipping. Each of those has duration and some of them have float.</p>
                            <p>None of it is visible to you. What you receive is a delivery date, which is the output of that programme rather than a description of it. When the date holds for a year and then moves by six weeks, what has actually happened is that float was consumed steadily for a year and ran out &#8212; and the first signal you get is the end of the process rather than the middle of it.</p>
                            <p><a href="reporting-week-5.html">Reporting Week 5</a> made the case for counting how many times a promised date has moved. On free-issue equipment that count is doing more work than usual, because it is the only visibility into a programme you are never going to be shown.</p>

                            <h2>A supplier who is not a contractor</h2>
                            <p>The party at the other end behaves differently from anybody else on the project, and the differences are structural.</p>
                            <p>They have no site presence, so nothing about their progress is observable. They work to industry norms and quality regimes that are theirs rather than the project&#39;s. They have other customers, and where capacity is short somebody&#39;s order moves.</p>
                            <p>And the mechanisms are wrong for construction. There is no notice provision you can use, no Engineer to determine anything, and a slip arrives as a revised promise rather than as an event with a date. By the time it is unambiguous, it is a fact.</p>
                            <p>Which puts it in the same position as access in <a href="interfaces-week-13.html">last week</a>: an input to your work produced by a party you cannot instruct, cannot chase and cannot claim against, reachable only through the employer.</p>

                            <h2>The day it arrives</h2>
                            <p>Free issue also produces a boundary, and it is exactly the shape <a href="interfaces-week-10.html">week 10</a> described.</p>
                            <p>Something has to offload it, and offloading a large vessel is a crane and a method statement. Something has to store it, protect it and preserve it, possibly for months. Somebody has to inspect it on arrival and decide whether transit damage is the vendor&#39;s problem or the site&#39;s.</p>
                            <p>The purchase order covers delivery to a point. The construction package covers installation. Between those two is a set of activities that both documents can reasonably assume the other contains, and which appear in neither price.</p>
                            <p>It is discovered on the day the lorry arrives, which is the worst day to discover it, because by then the item is on site and somebody has to do something with it in the next few hours.</p>

                            <h2>What can actually be done</h2>
                            <p>Three things, and the first is the one that changes the position.</p>
                            <p>Get the delivery date into your own contract as a date the employer owes you. Free-issue equipment arriving late is an employer risk event if the contract says so and an argument if it does not. That is a drafting question and it is decided before anybody starts.</p>
                            <p>Put the vendor milestones into the integration model from <a href="interfaces-week-12.html">week 12</a> &#8212; not the delivery date alone, but design approval, material release, start of fabrication, testing. Each is a point where a slip is visible months before delivery, and the employer can often obtain them where you cannot.</p>
                            <p>And treat the arrival boundary as a scope gap now rather than in transit. Offload, store, preserve, inspect: four items, four owners, agreed while it is still a clarification.</p>

                            <h2>Practical insight</h2>
                            <p>Find the free-issue item on your project with the longest lead time, and ask for three dates rather than one: when its design was approved, when fabrication started, and when it is promised.</p>
                            <p>If you can only get the third, you have no visibility at all and your programme is carrying a risk you cannot size. Say so, in the monthly report, in those words.</p>
                            <p>If you can get all three, you can do the arithmetic yourself. Compare the elapsed time since fabrication started with what the vendor said it would take. A vendor at forty percent of their duration and twenty percent of their scope is going to be late, and you will know it four months before the revised date arrives.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The driving activity can be manufacturing, in a works you have never visited, under an order you are not party to.</li>
                            <li>Early ordering is the right answer to lead times longer than the time available. It creates a different problem.</li>
                            <li>A vendor&#39;s programme has float in it. You see the output date, not the process, so the first signal is the end of it.</li>
                            <li>Counting how many times a promise has moved is the only visibility into a programme you will not be shown.</li>
                            <li>Vendors have no site presence, their own quality regime, other customers, and no notice mechanism you can use.</li>
                            <li>Like access, it is an input from a party you cannot instruct or claim against, reachable only through the employer.</li>
                            <li>Offload, storage, preservation and arrival inspection sit between the purchase order and the construction package.</li>
                            <li>Get the delivery date into your contract, get the vendor milestones into the integration model, and settle the arrival boundary before the lorry.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The vendor milestone set in the integration model &#183; the promised-date revision count &#183; the arrival boundary with four named owners.</p>

                            <h2>What is coming next</h2>
                            <p>That is every route by which work reaches the site. What remains is the number that comes back out, and what happens to it when two organisations both produce it correctly.</p>
                            <p>Next week: progress and valuation when two companies both produce the figure.</p>'''

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
    ["Vendor milestone set", "Employer or procurement", "Design approved, material released, fabrication started, tested",
     "The vendor&#8217;s own reporting", "Integration model"],
    ["Promised date and revisions", "Procurement", "The current date and how many times it has moved",
     "The date history", "Risk register &#183; forecast"],
    ["Delivery obligation", "Contracts, at award", "A date the employer owes you, not a programme assumption",
     "Your own contract", "Entitlement when it slips"],
    ["Arrival boundary", "Project controls", "Offload, store, preserve, inspect &#8212; four named owners",
     "The order and the package scope", "Cost &#183; the day it lands"],
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
    ("Here you cannot even see it.",
     SVG.format(h=200) + head("WHERE THE DRIVING ACTIVITY IS")
     + box(24, 56, 270, 62, "On your site", "you can resource it", "good")
     + box(346, 56, 270, 62, "In a factory", "you have no right to see it", "bad")
     + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">An order placed eighteen months ago, by somebody else, with somebody you have never met.</text>'
     + "</svg>",
     "Figure 1 &#8212; Every technique for managing a critical path assumes the driving activity can be acted on. On free-issue equipment it cannot even be observed."),
    ("the first signal you get is the end of the process rather than the middle of it.",
     SVG.format(h=210) + head("WHAT YOU SEE OF A VENDOR PROGRAMME")
     + box(16, 52, 116, 54, "Design", "")
     + box(142, 52, 116, 54, "Material", "")
     + box(268, 52, 116, 54, "Fabrication", "")
     + box(394, 52, 116, 54, "Testing", "")
     + box(520, 52, 100, 54, "Ship", "")
     + box(400, 128, 220, 46, "A delivery date", "all you receive", "bad")
     + '<text x="200" y="156" text-anchor="middle" fill="#64748b" font-size="11.5">Float is consumed here, invisibly, for a year.</text>'
     + "</svg>",
     "Figure 2 &#8212; The date is the output of that programme rather than a description of it, which is why a year of stability can be followed by six weeks of movement."),
    ("because by then the item is on site and somebody has to do something with it in the next few hours.",
     SVG.format(h=200) + head("THE GAP AT THE GATE")
     + box(24, 56, 240, 62, "Purchase order", "delivery to a point", "good")
     + box(376, 56, 240, 62, "Construction package", "installation", "good")
     + box(280, 62, 80, 50, "?", "", "bad")
     + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Offload &#183; store &#183; preserve &#183; inspect</text>'
     + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">Both documents can reasonably assume the other contains them.</text>'
     + "</svg>",
     "Figure 3 &#8212; The same scope gap as any other boundary, discovered on the one day when there is no time to resolve it properly."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The first row is the one worth fighting for. Four dates instead of one converts an '
          'opaque promise into something with a shape.</p>\n                            ' + table()
          + '\n                            '
          '<p>Where the vendor will not report to that level, the employer may be able to obtain it '
          'and simply has not been asked, because nobody explained that a fabrication start date is '
          'a programme input rather than a procurement detail.</p>')


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

    old_share = ("The civil contractor finished on their contract date. The mechanical contractor "
                 "needed the area a month earlier. Nobody breached anything and three weeks were lost.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-13.html", "interfaces-week-14.html")
    s = s.replace('data-current-week="13"', 'data-current-week="14"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 14<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 14", s, 1)
    s = s.replace("Interfaces &#183; Week 13", "Interfaces &#183; Week 14")
    s = s.replace('<a href="interfaces-week-14.html">last week</a>',
                  '<a href="interfaces-week-13.html">last week</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), ]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-14.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-14.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
