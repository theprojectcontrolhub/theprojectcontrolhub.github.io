#!/usr/bin/env python3
"""Builds interfaces-week-1.html.

Template is reporting-week-1.html: same track family, same layout, and using
a page from the same era keeps the two tracks structurally identical rather
than letting them drift.

One decision is taken here and should be reviewed before week 2. The case
study stays the $1M job. Track 7 needs a shape that job does not have, and
NOTES.md section 1 forbids inventing canon figures, so the job is re-let as
separate packages: no new numbers, a different structure around the same
ones. Every alternative meant a second case study, which is where the
arithmetic discipline that held for 143 articles would start to fray.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "reporting-week-1.html"
OUT = ROOT / "drafts" / "interfaces-week-1.html"

TITLE = "The single-contract assumption — what every planning method takes for granted"
DESC = ("Every technique in six tracks assumes one contract, one Engineer and one programme. "
        "What happens to a notice, a critical path and a progress figure when that shape is not "
        "there.")
OG = "Nobody is the Engineer"
SHARE = ("Six tracks taught you to serve a notice on the Engineer. On this job there isn't one, "
         "and there is nothing wrong with the job.")
CRUMB = "The shape every track assumed"
H1 = "Nobody is the Engineer."

BODY = '''<h2 style="margin-top:0;">Nobody is the Engineer</h2>
                            <p>Access to an area is three weeks late and the delay is somebody else&#39;s. You know exactly what to do, because <a href="contract-week-1.html">Contract Week 1</a> spent a week on it: give notice, in time, to the Engineer.</p>
                            <p>So you ask who that is. And the answer, after some back and forth, is that there is no Engineer. There is a managing contractor running the site on the employer&#39;s behalf. Your contract is with the employer. The company whose scaffolding is blocking the area has a contract with the employer too, and none with you. The managing contractor instructs everybody and is party to nothing.</p>
                            <p>Nothing here is unusual and nothing is broken. It is simply a shape that none of the last hundred and forty-three lessons described.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>The assumption nobody stated</h2>
                            <p>Read back through the tracks and the same picture sits behind all of them. One employer. One contract. One contractor with the whole of the works. One Engineer administering it. One programme that covers everything being built.</p>
                            <p>It was never argued for, because it did not need to be. It is the shape the standard forms are written around, the shape the textbooks use, and the shape that lets a method be taught without a page of qualifications attached to it. Every technique in six tracks quietly depends on it.</p>
                            <p>That is not a flaw in what came before. Teaching the single-contract case first is the only sensible order &#8212; you cannot explain what happens when a definition has nowhere to live before explaining the definition. But the assumption has been doing work all along, and it has never been named.</p>

                            <h2>What actually rests on it</h2>
                            <p>Four things, and they are worth separating because they fail differently.</p>
                            <p><strong>Entitlement assumes an address.</strong> A notice is served on somebody with the authority to receive it and the duty to act. Where that role is split across firms, or held by a company with no contractual relationship to you, the mechanism from <a href="contract-week-3.html">Contract Week 3</a> does not simply become harder. It has nowhere to attach.</p>
                            <p><strong>The critical path assumes work.</strong> <a href="week-13.html">Schedule Week 13</a> computes float across a network of activities you control or subcontract. On a job where the long-lead equipment is bought by the employer under a separate order, the driving path runs through a contract you cannot see and a supplier you cannot chase.</p>
                            <p><strong>Risk registers assume a scope.</strong> <a href="risk-week-3.html">Risk Week 3</a> breaks risk down within the works. Break risk down within a scope and the gaps between scopes are exactly what the structure excludes. On a multi-package job that is where an expensive item can sit, and no register is shaped to hold it.</p>
                            <p><strong>A number assumes an owner.</strong> <a href="reporting-week-1.html">Reporting Week 1</a> made that the foundation of a whole track. When the record you would check against belongs to another company, on their cut-off, in their coding, the reconciliation is no longer a conversation down the corridor.</p>

                            <h2>Concurrency, and where the definition lives</h2>
                            <p>One example is worth following all the way through, because it shows that this is not a matter of degree.</p>
                            <p><a href="claim-week-16.html">Claims Week 16</a> established that the standard forms do not define concurrency. The definition is left to the Particular Conditions, which is uncomfortable but workable: two parties, one contract, and a document where the meaning can be written down and agreed.</p>
                            <p>Now take the same argument onto a job with six packages and no head contract. There is no single document to hold the definition, and the two delays being argued about may sit under two contracts with different wording and different tests. The technique is entirely correct and there is nowhere to apply it.</p>
                            <p>That is the difference between a harder version of a problem and a different problem.</p>

                            <h2>Same job, different shape</h2>
                            <p>The example running through six tracks has been a single lump-sum contract. It stays. What changes from here is how it was bought.</p>
                            <p>Instead of one contractor holding the works, the employer lets it as packages: civil, mechanical, electrical, and the long-lead equipment ordered directly. A managing contractor coordinates them and employs none of them. Same scope, same quantities, same money. A different diagram.</p>
                            <p>Keeping the job is deliberate. The alternative is a second case study, and then every figure has to be traced twice. What is being examined here is not a bigger project. It is the same project under a structure that removes the single point every method has been leaning on.</p>

                            <h2>What this track is, and is not</h2>
                            <p>It is not a catalogue of delivery models. Knowing what the letters in EPCM stand for changes nothing about a Tuesday. Each model appears only where it breaks something specific, and the definition arrives as a consequence rather than as a lesson.</p>
                            <p>It does not re-teach a method. Float stays in Schedule, concurrency in Claims, cost accounting in Cost &amp; Cash, and where a number comes from in Reporting. This track marks the edges and hands the technique back with a link every time.</p>
                            <p>What is left is the part that only exists at the joins: who can instruct whom, which work belongs to nobody, whose programme the critical path runs through, and who owns a figure that two organisations both produce correctly.</p>

                            <h2>Practical insight</h2>
                            <p>Take your own project and answer three questions in writing. They take ten minutes and most people cannot finish them.</p>
                            <p>How many separate contracts exist on the site &#8212; not subcontracts under yours, but contracts the employer holds directly? Who has the authority to instruct each of those parties, and is that authority contractual or conventional? And if a delay were caused to you by one of them tomorrow, who would you serve the notice on?</p>
                            <p>If the third question has a clean answer, this track will be a description of other people&#39;s projects and worth reading anyway. If it does not, the sixteen weeks after this one are about the job you are already on.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Six tracks assumed one employer, one contract, one contractor, one Engineer, one programme. None of them said so.</li>
                            <li>Teaching that case first is correct. It only becomes a problem when it is mistaken for the general case.</li>
                            <li>Entitlement assumes an address for the notice. Split the role across firms and the mechanism has nowhere to attach.</li>
                            <li>The critical path assumes the work is yours. It can run through an order placed by somebody else.</li>
                            <li>Risk registers cover what goes wrong inside a scope. The expensive items sit between two.</li>
                            <li>A number assumes an owner you can reach. Across companies, the corroborating record belongs to somebody else.</li>
                            <li>Concurrency is the clearest case: the definition lives in the Particular Conditions, and with no head contract there are none.</li>
                            <li>The case study does not change. The same job is re-let as packages, so no figure moves.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The contract map &#183; the list of parties and who may instruct each &#183; the notice address for every party you can be delayed by.</p>

                            <h2>What is coming next</h2>
                            <p>If the shape matters this much, the first question is how a job comes to have the shape it has. That decision is made before anybody is appointed, usually by people the project team never meets.</p>
                            <p>Next week: how many contracts are there &#8212; the axis that decides more than the payment mechanism, and the one nobody teaches.</p>'''

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
    ["Contract map", "Project controls", "Every party the employer holds a contract with, not just yours",
     "The employer&#8217;s contract register", "Notices &#183; interface register"],
    ["Instruction authority", "Contracts or commercial", "Contractual or conventional, stated for each party",
     "The contracts themselves", "Who an instruction is valid from"],
    ["Notice address", "Contracts", "One named recipient per party you can be delayed by",
     "Each contract&#8217;s notice clause", "Entitlement &#183; delay events"],
    ["Package scope boundary", "Engineering with each party", "Where one scope ends and the next begins, in writing",
     "Drawings and the bills", "Interface register &#183; risk"],
]


def box(x, y, w, h, title, sub="", tone="plain"):
    fill, stroke, tc, sc = {"plain": ("#fff", "#cbd5e1", "#334155", "#64748b"),
                            "good": ("#ecfdf5", "#a7f3d0", "#047857", "#059669"),
                            "bad": ("#fef2f2", "#fca5a5", "#b91c1c", "#dc2626")}[tone]
    cx = x + w / 2
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>'
    o += f'<text x="{cx}" y="{y + 25}" text-anchor="middle" fill="{tc}" font-size="13" font-weight="700">{title}</text>'
    if sub:
        o += f'<text x="{cx}" y="{y + 44}" text-anchor="middle" fill="{sc}" font-size="11">{sub}</text>'
    return o


def head(t):
    return (f'<text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" '
            f'font-weight="700" letter-spacing="2">{t}</text>')


FIGURES = [
    ("Nothing here is unusual and nothing is broken.",
     SVG.format(h=230) + head("THE SHAPE SIX TRACKS ASSUMED")
     + box(230, 46, 180, 52, "Employer", "", "good")
     + box(230, 118, 180, 52, "Engineer", "administers", "good")
     + box(230, 176, 180, 44, "Contractor", "the whole works", "good")
     + '<line x1="320" y1="98" x2="320" y2="118" stroke="#a7f3d0" stroke-width="2"/>'
     + '<line x1="320" y1="170" x2="320" y2="176" stroke="#a7f3d0" stroke-width="2"/>'
     + "</svg>",
     "Figure 1 &#8212; One employer, one Engineer, one contractor, one programme. Nothing in six tracks argued for this; every method in them depends on it."),
    ("A different diagram.",
     SVG.format(h=240) + head("THE SAME JOB, LET AS PACKAGES")
     + box(230, 42, 180, 46, "Employer", "")
     + box(230, 106, 180, 46, "Managing contractor", "instructs, no privity", "bad")
     + box(16, 176, 142, 46, "Civil", "")
     + box(172, 176, 142, 46, "Mechanical", "")
     + box(328, 176, 142, 46, "Electrical", "")
     + box(484, 176, 134, 46, "Equipment", "direct order")
     + '<line x1="320" y1="88" x2="320" y2="106" stroke="#cbd5e1" stroke-width="2"/>'
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11">four contracts with the employer, none with each other</text>'
     + "</svg>",
     "Figure 2 &#8212; Same scope, same quantities, same money. The managing contractor instructs every party and is in contract with none of them."),
    ("That is the difference between a harder version of a problem and a different problem.",
     SVG.format(h=190) + head("WHAT EACH METHOD LEANS ON")
     + box(16, 52, 146, 72, "Notice", "an address", "bad")
     + box(172, 52, 146, 72, "Critical path", "work you hold", "bad")
     + box(328, 52, 146, 72, "Risk register", "a scope", "bad")
     + box(484, 52, 134, 72, "A number", "an owner", "bad")
     + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">Remove the single point and each one fails differently.</text>'
     + "</svg>",
     "Figure 3 &#8212; None of these techniques becomes merely harder. Each loses the thing it was attaching to, which is why the track is organised by what breaks rather than by delivery model."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>Before any technique, one page that does not exist on most multi-contract jobs: '
          'who the parties are, who may instruct each of them, and where a notice goes.</p>\n'
          '                            ' + table() + '\n                            '
          '<p>The second row is the one that causes arguments. Authority on these jobs can be '
          'conventional rather than contractual &#8212; everybody does what the managing contractor '
          'says because that is how the site runs, not because a clause says so. Writing down which '
          'it is, party by party, is an hour of work and it decides what happens the first time an '
          'instruction is disputed.</p>')


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
    body = body.replace("<h2>Practical insight</h2>", SYSTEM + "\n\n                            <h2>Practical insight</h2>", 1)

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

    old_share = ("A wrong number went round five departments and came back unclaimed. "
                 "Every answer was true. That is the problem.")
    from urllib.parse import quote
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("reporting-week-1.html", "interfaces-week-1.html")
    s = s.replace('data-current-week="1"', 'data-current-week="1"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 1<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 06 · REPORTING · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 1", s, 1)
    s = s.replace("Reporting &#183; Week 1", "Interfaces &#183; Week 1")
    # the reference to Reporting week 1 in the body must survive the filename swap
    s = s.replace('<a href="interfaces-week-1.html">Reporting Week 1</a>',
                  '<a href="reporting-week-1.html">Reporting Week 1</a>')

    # Contractions, verb negatives only — the rule Tracks 2, 3 and 6 use.
    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bcould not\b", "couldn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    # 2. The template carries a next-article block pointing at reporting week 2.
    #    Interfaces week 2 does not exist, so the block goes; it comes back when
    #    the next article ships.
    i2 = s.find("                        <!-- NEXT ARTICLE NAV")
    if i2 != -1:
        j2 = s.index("                        <!-- PAYWALL CTA -->", i2)
        s = s[:i2] + s[j2:]

    OUT.parent.mkdir(exist_ok=True)
    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-1.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-1.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
