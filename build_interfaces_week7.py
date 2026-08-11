#!/usr/bin/env python3
"""Builds interfaces-week-7.html.

Template is interfaces-week-6.html.

The kickoff flagged this week as the furthest from the thesis and the first
candidate for removal. It earns its place on one argument: the adversarial
process is a quality control on the record, and a contract designed to remove
the claim also removes the party whose job it was to check the number. That
is a failure rather than a description of a delivery model, which is the test
every week on this track has to pass.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-6.html"
OUT = ROOT / "drafts" / "interfaces-week-7.html"

TITLE = "Alliancing and integrated delivery — project controls with no claim to make"
DESC = ("Collaborative contracts remove the machinery of entitlement. What that does to the record, "
        "and why nobody checking your number is a harder position than somebody disputing it.")
OG = "Nobody is going to argue with this number"
SHARE = ("On a claims contract the other side audits your figure. On an alliance nobody does, and "
         "that is the harder position to be in.")
CRUMB = "Alliancing, partnering and IPD"
H1 = "Nobody is going to argue with this number."

BODY = '''<h2 style="margin-top:0;">Nobody is going to argue with this number</h2>
                            <p>Six weeks of this track have been about entitlement: who serves a notice on whom, which Engineer determines it, whose delay it was.</p>
                            <p>Some contracts are written specifically to make all of that impossible. The parties agree a target, share the pain and gain against it, waive most of their rights to sue each other, and take decisions through a board on which everybody sits.</p>
                            <p>The intention is sound and the mechanism works. What it also does is remove the one party whose job it was to check your figures, and that turns out to matter more than anybody expects.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What these contracts actually change</h2>
                            <p>Three mechanisms do most of the work, and they can appear separately or together.</p>
                            <p><strong>The money moves together.</strong> A target cost is agreed, actual outturn is measured against it, and the difference is shared on a formula. <a href="contract-week-4.html">Contract Week 4</a> covers how that works within one contract. Extended across the parties, it means a delay is not somebody&#39;s liability &#8212; it is everybody&#39;s reduced margin.</p>
                            <p><strong>Recourse is limited.</strong> The parties agree not to bring claims against each other except in narrow circumstances &#8212; wilful default and insolvency are the common carve-outs. The notice provisions may still exist on paper. Nothing is going to be served under them.</p>
                            <p><strong>Decisions are taken jointly.</strong> A board with representatives from each party, frequently requiring unanimity. Which means no party can be instructed against its will, and equally that no party can force a decision when the others will not move.</p>

                            <h2>What does not change</h2>
                            <p>The work is identical. Concrete still has to cure before steel goes on it, a drawing still has to be issued before anything is built to it, and somebody still has to have the area cleared by Monday.</p>
                            <p>Every interface from the previous six weeks is still there. The scope gaps are still there. What has changed is who pays for them and through what route, not whether they happen.</p>
                            <p>Which is worth stating because the language around these arrangements can suggest otherwise. Aligning commercial interests removes a reason to argue. It does not remove the three weeks.</p>

                            <h2>The check that disappears</h2>
                            <p>Here is the part that belongs to project controls and it is not obvious.</p>
                            <p>On an adversarial contract, every number you produce is examined by somebody who would prefer it to be smaller. The progress figure is checked by the Engineer. The delay analysis is answered by the other side&#39;s analyst. The valuation is tested against a measurement somebody else took. That process is unpleasant, slow and expensive, and it is also the most thorough quality control the number will ever get.</p>
                            <p>Remove the claim and the examination goes with it. The figure is agreed at the board because everybody around the table has the same interest in the project looking well, and because disputing it is the behaviour the contract was written to discourage.</p>
                            <p>So a number that would have been fought over for three months on a lump sum contract is accepted in a meeting. It might be right. Nothing in the arrangement establishes whether it is.</p>

                            <h2>The record with no addressee</h2>
                            <p>The second consequence follows from the first and it is slower to appear.</p>
                            <p><a href="claim-week-6.html">Claims Week 6</a> made the contemporaneous record the strongest evidence there is, and the reason people keep it is that they might need it. Take away the claim and that reason is gone. A delay event with no entitlement attached to it is, to the person recording it, paperwork with no purpose.</p>
                            <p>So events get absorbed rather than logged. Nobody is being careless; there is genuinely no one to send it to. Then the outturn cost lands above the target, the pain share bites, and the parties want to understand where a year went &#8212; and the record that would have explained it was never made, because for a year nobody needed it.</p>
                            <p>This is <a href="reporting-week-26.html">Reporting Week 26</a> in a different form. There, a report nobody acted on still did its second job as evidence. Here the second job has been removed by the contract, and the first is all that is left.</p>

                            <h2>What that asks of a planner</h2>
                            <p>The requirement inverts. On a claims contract, rigour is enforced from outside and the discipline is to keep up with it. On an alliance, rigour has to be supplied from inside, because nothing external will demand it.</p>
                            <p>Which makes two things worth doing deliberately. Record delay events with causes anyway, on the basis that the pain share is a settlement and a settlement needs a basis. And build the corroboration from <a href="reporting-week-8.html">Reporting Week 8</a> into the routine rather than waiting for somebody to challenge a figure, because on this arrangement nobody will.</p>
                            <p>It is more work than the adversarial version, not less. The difference is that on a claims job the work is forced on you, and here you have to decide to do it.</p>

                            <h2>Practical insight</h2>
                            <p>Ask one question about your own project, whatever form it is under: who was the last person to challenge a number you produced?</p>
                            <p>If you can name them and it was recent, the external check is working and you can rely on it to catch what you miss. If you cannot &#8212; if your figures have been accepted without question for months &#8212; then whatever the contract says, you are already in the position this week describes.</p>
                            <p>In that case, pick your three largest figures and corroborate them against a record produced by somebody who has no interest in them. Not because anybody asked. Because on this arrangement nobody is going to, and you are the only remaining check.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Three mechanisms do the work: shared pain and gain, limited recourse, and joint decision-making.</li>
                            <li>A delay stops being somebody&#39;s liability and becomes everybody&#39;s reduced margin.</li>
                            <li>Unanimity means no party can be instructed against its will, and none can force a decision either.</li>
                            <li>The interfaces, the scope gaps and the three weeks all remain. Only the route to payment changes.</li>
                            <li>The adversarial process is the most thorough quality control a number ever receives. Removing the claim removes it.</li>
                            <li>A figure that would have been fought over for months is accepted in a meeting. It might be right, and nothing establishes that.</li>
                            <li>People keep contemporaneous records because they might need them. With no claim, events get absorbed instead.</li>
                            <li>Rigour has to be supplied from inside, which is more work than the adversarial version rather than less.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The delay event log kept with no claim attached to it &#183; the corroboration routine run without being asked &#183; the basis of the pain share settlement.</p>

                            <h2>What is coming next</h2>
                            <p>A board where every party has to agree is one answer to who decides. On most multi-contract jobs there is no board, and the question is open.</p>
                            <p>Next week: governance across organisations, and the decision three companies need that no forum has the authority to take.</p>'''

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
    ["Delay event log", "Project controls", "Cause recorded even though no claim attaches to it",
     "Site record", "The pain share settlement"],
    ["Corroboration routine", "Project controls", "Run on a schedule, not on challenge",
     "Records from outside the reporting chain", "Progress &#183; outturn forecast"],
    ["Outturn against target", "Commercial, jointly", "One basis, agreed and written, not per party",
     "Each party&#8217;s cost system", "Pain and gain calculation"],
    ["Board decisions", "The alliance board", "What was decided, by whom, and what it changed",
     "The minutes", "Change &#183; programme"],
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
    ("Aligning commercial interests removes a reason to argue. It does not remove the three weeks.",
     SVG.format(h=190) + head("WHAT CHANGES AND WHAT DOES NOT")
     + box(30, 50, 265, 84, "The route to payment", "shared, not claimed", "good")
     + box(345, 50, 265, 84, "The work", "same interfaces, same gaps")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">Concrete still cures at the same rate under any form of contract.</text>'
     + "</svg>",
     "Figure 1 &#8212; The commercial arrangement decides who pays for a delay. It has no effect on whether the delay happens."),
    ("It might be right. Nothing in the arrangement establishes whether it is.",
     SVG.format(h=210) + head("WHO EXAMINES THE NUMBER")
     + box(24, 52, 270, 76, "Adversarial contract", "Engineer, other analyst, rival measurement", "good")
     + box(346, 52, 270, 76, "Collaborative contract", "agreed at the board", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">The unpleasant process was also the quality control.</text>'
     + '<text x="320" y="188" text-anchor="middle" fill="#64748b" font-size="11.5">Everybody at the table has the same interest in the project looking well.</text>'
     + "</svg>",
     "Figure 2 &#8212; Three months of argument is the most thorough check a figure ever receives. Removing the claim removes the check along with the argument."),
    ("because for a year nobody needed it.",
     SVG.format(h=200) + head("THE RECORD WITH NOWHERE TO GO")
     + box(16, 52, 190, 60, "Event happens", "")
     + box(222, 52, 190, 60, "No claim attaches", "", "bad")
     + box(428, 52, 190, 60, "Not recorded", "", "bad")
     + '<text x="320" y="146" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Then the pain share bites and the year has to be explained.</text>'
     + '<text x="320" y="172" text-anchor="middle" fill="#64748b" font-size="11.5">Nobody was careless. There was genuinely nobody to send it to.</text>'
     + "</svg>",
     "Figure 3 &#8212; The reason people keep contemporaneous records is that they might need them. Remove the need and the habit goes with it, months before the consequence arrives."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>Everything here exists on an adversarial job as well. The difference is that there it '
          'is produced because somebody demands it, and here it has to be produced because it is '
          'right.</p>\n                            ' + table() + '\n                            '
          '<p>The first row is the one that gets dropped, and dropping it is reasonable at the time: '
          'a delay event with no entitlement attached looks like paperwork for its own sake. It '
          'becomes the basis of a settlement eighteen months later, at which point it either exists '
          'or it does not.</p>')


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

    old_share = ("The employer sees one contractor, one programme, one progress figure. Behind it "
                 "are two companies that have never shared a cost code.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-6.html", "interfaces-week-7.html")
    s = s.replace('data-current-week="6"', 'data-current-week="7"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 7<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 7", s, 1)
    s = s.replace("Interfaces &#183; Week 6", "Interfaces &#183; Week 7")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-7.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-7.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
