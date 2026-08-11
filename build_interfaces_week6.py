#!/usr/bin/env python3
"""Builds interfaces-week-6.html.

Template is interfaces-week-5.html.

The finding the week is built on: a split-scope consortium reproduces every
interface problem of weeks 1 to 5 inside a single contract, where none of the
contractual machinery reaches. The employer sees one contractor and cannot see
the joins; the parties behind it have a JV agreement rather than a contract
with each other, and no Engineer administers it.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-5.html"
OUT = ROOT / "drafts" / "interfaces-week-6.html"

TITLE = "Joint ventures and consortia — one contractor, several sets of books"
DESC = ("A split-scope consortium puts every interface problem inside a single contract, where the "
        "contractual machinery cannot reach it. What the employer sees and what it cannot.")
OG = "One contractor, two companies"
SHARE = ("The employer sees one contractor, one programme, one progress figure. Behind it are two "
         "companies that have never shared a cost code.")
CRUMB = "Joint ventures and consortia"
H1 = "One contractor, two companies."

BODY = '''<h2 style="margin-top:0;">One contractor, two companies</h2>
                            <p>The contract has one contractor named in it. The programme comes in as one document, the monthly report gives one progress figure, and the Engineer administers one set of obligations.</p>
                            <p>Behind that name are two companies. They have separate cost systems, separate month-ends, separate ways of measuring progress, and a history of competing against each other for the same work.</p>
                            <p>Nothing about the contract shows this, and nothing in it needs to. From the employer&#39;s side the arrangement is one party. From inside, everything this track has been about is happening in a place the contract does not reach.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Two shapes, and the difference decides everything</h2>
                            <p>The distinction that matters is not the legal label. It is whether the scope was split.</p>
                            <p>In an <strong>integrated</strong> arrangement the partners pool people and resources into one organisation that runs the work. There is one project team, one cost system set up for the job, and one programme built by that team. Internally it behaves like a single contractor, because for the purposes of doing the work it is one.</p>
                            <p>In a <strong>split-scope</strong> arrangement the partners divide the works between them &#8212; one takes the process plant, another the civils &#8212; and each executes their part with their own people, their own systems and their own supply chain. There is one contract facing the employer and two projects behind it.</p>
                            <p>The second shape reproduces every problem of the last five weeks inside a single contract. What it does not reproduce is any of the machinery.</p>

                            <h2>What the machinery cannot reach</h2>
                            <p>Between two package contractors, at least there are two contracts, two Engineers and an employer standing between them. It is awkward, as <a href="interfaces-week-4.html">week 4</a> showed, and it is a structure.</p>
                            <p>Between two consortium partners there is no contract at all. There is a joint venture agreement, which is an agreement between them about how they will share the work, the money and the risk. The employer is not a party to it. The Engineer has no visibility of it. Nothing in the construction contract governs what happens when one partner delays the other, because as far as that contract is concerned nobody was delayed &#8212; the contractor was.</p>
                            <p>So the internal interface has no notice provision, no determination, no extension mechanism and no adjudicator. Whatever exists is in the JV agreement, and a JV agreement is a corporate document about liability and profit share. It is not drafted to resolve a programme dispute, and it is rarely written by anybody who expected one.</p>

                            <h2>The delay that does not exist</h2>
                            <p>Follow one event through and the consequence is stark.</p>
                            <p>Partner A hands over an area three weeks late. Partner B cannot start and loses three weeks. The joint venture&#39;s completion date is threatened.</p>
                            <p>There is no claim to make. The contractor delayed itself. The employer owes nothing, no extension is due, and the Engineer has no question in front of them. The three weeks are absorbed inside the JV, and where they land depends entirely on a document the project team may never have read.</p>
                            <p>Which is the reverse of the position in <a href="interfaces-week-5.html">week 5</a>. There, another contractor&#39;s delay reached you as an employer risk event and became an ordinary claim. Here the same physical event produces nothing at all, because the party who caused it and the party who suffered it are the same contracting party.</p>

                            <h2>Two sets of books, one figure</h2>
                            <p>The reporting consequence is immediate and it lands on project controls.</p>
                            <p>Each partner records cost in their own system, on their own chart of accounts, closing on their own date. Each measures progress by whatever method they use elsewhere. The figure the employer receives is a consolidation of the two, produced by somebody, on a basis that is agreed between the partners and stated nowhere in the contract.</p>
                            <p>Everything <a href="reporting-week-25.html">Reporting Week 25</a> said about reconciling two records applies, with one difference that makes it harder: there is no reconciliation meeting with an agreed outcome, because the two parties are commercial rivals whose share of the profit depends on how the work is attributed between them.</p>
                            <p>The consolidated number can be entirely correct and still be unauditable from outside, because the working underneath it is commercially sensitive between the two firms producing it.</p>

                            <h2>Whose planner are you</h2>
                            <p>This is worth naming because it is uncomfortable and it is unavoidable.</p>
                            <p>A planner in a split-scope consortium is employed by one partner and producing documents for the joint venture. The programme goes to the employer in the JV&#39;s name. The delay analysis that shows where three weeks were lost also shows which partner lost them.</p>
                            <p>The professional position is the same one <a href="reporting-week-1.html">Reporting Week 1</a> set out: the reliability of the number is yours, the number is not. What changes is that the parties who will disagree about it are on the same side of the contract, and the argument has nowhere formal to go.</p>
                            <p>Which makes the record the whole of the defence. An internal interface that is logged, dated and circulated to both partners at the time is a fact. The same interface remembered six months later is a negotiating position.</p>

                            <h2>Practical insight</h2>
                            <p>Find out which of the two shapes you are in, and ask about systems rather than about the agreement. You will get an answer this week; the agreement you may never see.</p>
                            <p>Does your project have one cost system or two? Do you report progress on one method or consolidate two? Are your colleagues reporting to one manager, or do they have their own line back to their own company? Those three answers tell you more than the legal form does, and you can get them before lunch.</p>
                            <p>If your answer is two, draw the boundary between the partners as an interface and run it exactly as you would run one between separate contracts &#8212; a register, an owner on each side, dated evidence of every handover. You will not have a contract to enforce it with. You will have the only record of what happened, and on this arrangement that is worth more than the contract would have been.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The distinction that matters is whether the scope was split, not the legal label.</li>
                            <li>Integrated: one team, one cost system, one programme. It behaves like a single contractor because it is one.</li>
                            <li>Split-scope: one contract facing the employer and two projects behind it.</li>
                            <li>Between two package contractors there are two contracts and an Engineer. Between two partners there is a JV agreement the employer never sees.</li>
                            <li>An internal delay produces no claim. The contractor delayed itself, and the loss lands where the JV agreement puts it.</li>
                            <li>The employer&#39;s progress figure is a consolidation of two systems on a basis stated nowhere in the contract.</li>
                            <li>It can be correct and unauditable, because the working is commercially sensitive between the parties producing it.</li>
                            <li>With no machinery to enforce the interface, the contemporaneous record is the whole of the defence.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The internal interface register between partners &#183; the consolidation basis for cost and progress &#183; dated handover evidence at every internal boundary.</p>

                            <h2>What is coming next</h2>
                            <p>Some contracts are written to stop all of this happening &#8212; to put the parties in one pool, align the money, and remove the machinery that turns a disagreement into a claim.</p>
                            <p>Next week: alliancing, partnering and integrated delivery, and what a planner does when the contract is designed to suppress the claim.</p>'''

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
    ["Internal interface register", "Project controls", "One line per boundary between partners, with an owner each side",
     "The scope split", "Handover evidence &#183; internal claims"],
    ["Handover evidence", "Both partners", "Dated and circulated at the time, not reconstructed",
     "Site record", "Where an internal delay landed"],
    ["Consolidation basis", "Both partners", "How two cost systems and two progress methods become one figure",
     "The JV agreement", "The employer&#8217;s monthly report"],
    ["Partner cut-off dates", "Each partner", "Both stated, because they will not be the same",
     "Each partner&#8217;s finance calendar", "Reconciliation before issue"],
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
    ("What it does not reproduce is any of the machinery.",
     SVG.format(h=230) + head("TWO SHAPES BEHIND ONE NAME")
     + box(24, 46, 270, 40, "Integrated", "", "good")
     + box(24, 100, 270, 66, "One team, one cost system", "one programme", "good")
     + box(346, 46, 270, 40, "Split scope", "", "bad")
     + box(346, 100, 130, 66, "Partner A", "own systems", "bad")
     + box(486, 100, 130, 66, "Partner B", "own systems", "bad")
     + '<text x="320" y="200" text-anchor="middle" fill="#64748b" font-size="11.5">Same legal label. Entirely different job.</text>'
     + "</svg>",
     "Figure 1 &#8212; Ask about systems rather than about the agreement. One cost system or two is the question that decides what the arrangement actually is."),
    ("It is not drafted to resolve a programme dispute, and it is rarely written by anybody who expected one.",
     SVG.format(h=200) + head("WHAT SITS BETWEEN THE PARTIES")
     + box(24, 52, 270, 76, "Two package contractors", "two contracts &#183; an Engineer", "good")
     + box(346, 52, 270, 76, "Two JV partners", "a JV agreement &#183; nobody", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">No notice, no determination, no extension, no adjudicator.</text>'
     + "</svg>",
     "Figure 2 &#8212; The awkward structure on the left is still a structure. On the right the construction contract has nothing to say, because as far as it is concerned only one party exists."),
    ("because the party who caused it and the party who suffered it are the same contracting party.",
     SVG.format(h=200) + head("THE SAME EVENT, TWO ARRANGEMENTS")
     + box(24, 52, 270, 76, "Across contracts", "employer risk &#183; ordinary claim", "good")
     + box(346, 52, 270, 76, "Inside a JV", "no claim exists", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">Three weeks lost either way. Only one of them has a route.</text>'
     + "</svg>",
     "Figure 3 &#8212; Physically identical, contractually opposite. Where the loss lands is decided by a document the project team may never have read."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>An interface with no contract behind it still has to be run, and what is left to run '
          'it with is the record.</p>\n                            ' + table()
          + '\n                            '
          '<p>The second row is the one that decides internal arguments. Evidence circulated to both '
          'partners on the day is a fact both of them accepted at the time; the same event described '
          'afterwards is one company&#8217;s account of it, and the other company has their own.</p>')


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

    old_share = ("A concurrency analysis on a multi-package job often answers a question neither "
                 "contract is asking. The framing is the error, not the arithmetic.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-5.html", "interfaces-week-6.html")
    s = s.replace('data-current-week="5"', 'data-current-week="6"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 6<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 6", s, 1)
    s = s.replace("Interfaces &#183; Week 5", "Interfaces &#183; Week 6")
    # the body links back to week 5; the filename swap above would have eaten it
    s = s.replace('<a href="interfaces-week-6.html">week 5</a>',
                  '<a href="interfaces-week-5.html">week 5</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bare not\b", "aren't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-6.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-6.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
