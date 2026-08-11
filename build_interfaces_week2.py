#!/usr/bin/env python3
"""Builds interfaces-week-2.html.

Template is interfaces-week-1.html, so the two pages in the track stay
structurally identical.

The risk in this week is that it becomes a delivery-model catalogue, which
NOTES.md closed twice for other subjects. The guard is that no model is
defined for its own sake: each appears only at the point where the number of
contracts changes what a planner has to do. EPC, EPCM and design-build are
named, none of them is explained as a definition.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-1.html"
OUT = ROOT / "drafts" / "interfaces-week-2.html"

TITLE = "How many contracts — the delivery axis that decides more than the payment mechanism"
DESC = ("Contract type tells you how a contractor is paid and who designed the works. It does not "
        "tell you how many contracts the employer holds, which decides who carries the joins.")
OG = "Two projects, the same three words"
SHARE = ("Both were EPC lump sum. One had a single contractor, the other had five. They are not "
         "the same job and no clause tells you which you are on.")
CRUMB = "How many contracts are there"
H1 = "Two projects, the same three words."

BODY = '''<h2 style="margin-top:0;">Two projects, the same three words</h2>
                            <p>Two tender documents, and the same phrase in both: EPC, lump sum, fixed completion date.</p>
                            <p>On the first, one contractor holds the whole of the works and everything below is a subcontract. On the second, the employer has let four EPC contracts &#8212; process, civil, electrical, and the tanks &#8212; and a fifth firm is coordinating them.</p>
                            <p>Both descriptions are accurate. Both jobs are EPC lump sum. And almost nothing a planner does is the same on the two of them.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>The two axes everybody teaches</h2>
                            <p>Contract type is usually taught along two lines, and both are taught well.</p>
                            <p><a href="contract-week-4.html">Contract Week 4</a> covers how the money works: lump sum, remeasurement, cost-plus, target cost. That decides who carries a quantity being wrong, and it decides what a variation is worth.</p>
                            <p><a href="contract-week-16.html">Contract Week 16</a> covers who did the design, which is what separates the Red, Yellow and Silver books, and with it who carries the risk of the design being inadequate.</p>
                            <p>Between them those two answer most questions about a single contract. They answer nothing at all about how many there are.</p>

                            <h2>The third axis</h2>
                            <p>Count the contracts the employer holds directly. Not subcontracts &#8212; those sit under somebody else&#39;s obligation and are their problem. Contracts where the employer is one of the two parties.</p>
                            <p>One is the case six tracks assumed. Everything below it is a subcontract, so every interface between packages sits inside a single contractor&#39;s obligation. If two trades clash, that is their problem to resolve, and the employer is entitled to a finished works regardless.</p>
                            <p>Four or five changes that completely. Each contractor owes the employer their own scope and owes the others nothing. The space between the packages belongs to whoever the employer put there to coordinate &#8212; and, as <a href="interfaces-week-1.html">last week</a> set out, that coordinator often has no contract with any of them.</p>
                            <p>The number is not a detail of the procurement strategy. It is the thing that decides where the joins live.</p>

                            <h2>What the employer is buying</h2>
                            <p>Neither answer is better. They are a trade, and knowing which trade was made explains most of what follows.</p>
                            <p>One contract buys simplicity of recourse. There is a single party responsible for the whole, one programme to approve, one place to send a notice. The employer pays for that in price &#8212; the contractor is carrying the integration risk and has priced it &#8212; and in flexibility, because changing anything means changing one large contract.</p>
                            <p>Several contracts buy control and, usually, time. Packages can be let as the design for each is ready rather than waiting for all of it, specialists can be appointed directly, and the integration margin is not paid to anybody. What the employer takes back in exchange is the integration risk itself, and that risk does not disappear because nobody priced it.</p>
                            <p>That last point is the one worth holding on to. On a single-contract job the risk of two packages not fitting together is inside a price. On a multi-contract job it is inside nobody&#39;s price, and it lands wherever it lands.</p>

                            <h2>What changes for a planner</h2>
                            <p>Four things, and they are the reason this is not a procurement lesson.</p>
                            <p><strong>The programme stops being one document.</strong> Each contractor produces their own to their own contract, at their own level of detail. Something has to hold them together and it is usually not a contract deliverable for anybody.</p>
                            <p><strong>Float belongs to somebody.</strong> Under one contract, float in the network is a shared resource the contractor manages. Across contracts it sits inside one party&#39;s programme and is consumed by another party&#39;s delay, with no clause governing the transfer.</p>
                            <p><strong>Access becomes a supply.</strong> One contractor finishing late does not just delay themselves; it withholds the workface from the next. That is an obligation somebody owes, and on a multi-contract job it is frequently owed by the employer rather than by the contractor causing it.</p>
                            <p><strong>Completion stops being a date.</strong> With several contracts there are several completions, and the works are not finished when the last one is done &#8212; they are finished when everything that had to be integrated has been.</p>

                            <h2>The word does not tell you</h2>
                            <p>Which brings this back to the two tender documents.</p>
                            <p>EPC describes what one contract contains: engineering, procurement and construction under one obligation. It says nothing about how many such contracts exist. Design-build says who designed it. Turnkey says what condition it is handed over in. All three are properties of a contract, and a project is not a contract.</p>
                            <p>So the phrase in the tender is not the answer to the question. The answer is a count, and the count is usually not written anywhere. It has to be assembled by asking who the employer has signed with, which is why the contract map from last week is the first document on this track and not a formality.</p>

                            <h2>Practical insight</h2>
                            <p>Count them on your own project, from the employer&#39;s side rather than yours.</p>
                            <p>If the answer is one, the next fifteen weeks describe other people&#39;s jobs, and the useful thing you can take is knowing what your main contractor is absorbing on your behalf and what it is costing them.</p>
                            <p>If the answer is more than one, ask a second question about each interface between two of those contracts: which party owes the other anything at all? Where neither owes the other anything, the obligation runs through the employer or through nobody, and that is the answer more often than the site behaves as though it is. That list is the shape of the rest of this track, and it is specific to the job you are on.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Contract type answers how the money works and who designed it. Neither answers how many contracts exist.</li>
                            <li>Count the contracts the employer holds directly. Subcontracts do not count; they sit inside somebody&#39;s obligation.</li>
                            <li>One contract puts every interface inside a single obligation. Several put them between obligations.</li>
                            <li>One contract buys simple recourse and pays for it in price and flexibility.</li>
                            <li>Several buy control and time, and take back the integration risk, which nobody has priced.</li>
                            <li>The programme stops being one document, float sits in somebody&#39;s network, access becomes an obligation, and completion becomes several dates.</li>
                            <li>EPC, design-build and turnkey are properties of a contract. A project is not a contract.</li>
                            <li>The count is rarely written down. It has to be assembled from who the employer signed with.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The contract count and its date &#183; the interface list between every pair of contracts &#183; the note of who owes whom at each one.</p>

                            <h2>What is coming next</h2>
                            <p>If the employer holds five contracts and none of the five owes the others anything, somebody still has to run the site. Whoever fills that role ends up with an uncomfortable property: authority over everybody and a contract with nobody.</p>
                            <p>Next week: instructing people you have no contract with.</p>'''

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
    ["Contract count", "Project controls", "Contracts the employer signed, not subcontracts",
     "The employer&#8217;s register", "Everything on this track"],
    ["Interface list", "Project controls with each party", "One line per pair of contracts that touch",
     "Drawings and scope documents", "Risk register &#183; constraint log"],
    ["Who owes whom", "Contracts", "Stated per interface, including &#8220;neither&#8221;",
     "The contracts themselves", "Delay events &#183; entitlement"],
    ["Access obligations", "Contracts", "Which party owes a workface to which, and by when",
     "Each contract&#8217;s access clause", "Programme &#183; look-ahead"],
    ["Completion dates", "Contracts", "One per contract, plus the date integration finishes",
     "Each contract&#8217;s completion clause", "Milestones &#183; LD exposure"],
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
    ("And almost nothing a planner does is the same on the two of them.",
     SVG.format(h=250) + head("BOTH ARE EPC LUMP SUM")
     + box(120, 46, 180, 44, "Employer")
     + box(120, 110, 180, 44, "One contractor", "", "good")
     + box(120, 174, 180, 40, "subcontracts below", "", "plain")
     + '<line x1="210" y1="90" x2="210" y2="110" stroke="#cbd5e1" stroke-width="2"/>'
     + '<line x1="210" y1="154" x2="210" y2="174" stroke="#cbd5e1" stroke-width="2"/>'
     + box(370, 46, 180, 44, "Employer")
     + box(340, 130, 100, 40, "Process", "", "bad")
     + box(448, 130, 100, 40, "Civil", "", "bad")
     + box(340, 182, 100, 40, "Electrical", "", "bad")
     + box(448, 182, 100, 40, "Tanks", "", "bad")
     + '<line x1="460" y1="90" x2="460" y2="130" stroke="#cbd5e1" stroke-width="2"/>'
     + "</svg>",
     "Figure 1 &#8212; The same three words describe both. On the left every interface sits inside one obligation; on the right they sit between four, and none of the four owes the others anything."),
    ("it is inside nobody&#39;s price, and it lands wherever it lands.",
     SVG.format(h=190) + head("WHAT THE EMPLOYER IS BUYING")
     + box(30, 50, 265, 84, "One contract", "simple recourse, priced integration", "good")
     + box(345, 50, 265, 84, "Several contracts", "control and time, unpriced integration", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">The risk does not disappear because nobody put a number on it.</text>'
     + "</svg>",
     "Figure 2 &#8212; Neither is the better choice. Knowing which trade was made explains most of what a planner then spends the job dealing with."),
    ("they are finished when everything that had to be integrated has been.",
     SVG.format(h=190) + head("FOUR THINGS THAT CHANGE")
     + box(16, 52, 146, 72, "Programme", "several documents", "bad")
     + box(172, 52, 146, 72, "Float", "in one party&#39;s network", "bad")
     + box(328, 52, 146, 72, "Access", "an obligation owed", "bad")
     + box(484, 52, 134, 72, "Completion", "several dates", "bad")
     + "</svg>",
     "Figure 3 &#8212; None of these is a procurement question. Each is something a planner has to do differently on the day, which is why the count belongs at the front of the track."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The contract map from week 1, extended with the four things the count decides. None '
          'of it needs a system; all of it needs to exist somewhere other than in one person&#8217;s '
          'head.</p>\n                            ' + table() + '\n                            '
          '<p>The third row is the one that surprises people. On a multi-contract job the honest '
          'entry against an interface is frequently that neither party owes the other anything, and the '
          'obligation runs through the employer. Writing that down is not pessimism &#8212; it is '
          'the difference between chasing the right party in week two and the wrong one for a '
          'month.</p>')


def main():
    if not TEMPLATE.exists():
        sys.exit("HATA: sablon bulunamadi: drafts/interfaces-week-1.html")
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

    old_share = ("Six tracks taught you to serve a notice on the Engineer. On this job there isn't "
                 "one, and there is nothing wrong with the job.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-1.html", "interfaces-week-2.html")
    s = s.replace('data-current-week="1"', 'data-current-week="2"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 2<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 2", s, 1)
    s = s.replace("Interfaces &#183; Week 1", "Interfaces &#183; Week 2")
    # the body links back to week 1; the filename swap above would have eaten it
    s = s.replace('<a href="interfaces-week-2.html">last week</a>',
                  '<a href="interfaces-week-1.html">last week</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bcould not\b", "couldn't"),
                     (r"\bis not\b", "isn't"), (r"\bare not\b", "aren't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-2.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-2.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
