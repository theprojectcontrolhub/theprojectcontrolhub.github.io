#!/usr/bin/env python3
"""Builds interfaces-week-4.html.

Template is interfaces-week-3.html.

Contract Week 3 teaches the Engineer as a single role on a single contract.
This week is what the same role does when each package has its own, which is
not a harder determination but several determinations that nothing reconciles.

The frequency-claim discipline applied to weeks 1 to 3 holds here: the article
argues from what the contracts allow, not from how often anything happens.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-3.html"
OUT = ROOT / "drafts" / "interfaces-week-4.html"

TITLE = "Determination across contracts — when every package has its own Engineer"
DESC = ("One delay, two contracts, two Engineers, two determinations that never meet. Why "
        "impartiality has a smaller field than it looks and who absorbs the difference.")
OG = "Two determinations, one delay"
SHARE = ("The same two weeks produced an extension for one contractor and a deduction for another. "
         "Both determinations were correct.")
CRUMB = "The Engineer, multiplied"
H1 = "Two determinations, one delay."

BODY = '''<h2 style="margin-top:0;">Two determinations, one delay</h2>
                            <p>The civil contractor hands over a slab two weeks late. The mechanical contractor cannot start, claims two weeks, and is granted them.</p>
                            <p>The employer then looks to recover those two weeks from the civil contractor, whose own Engineer determines that the handover date was met &#8212; because under the civil contract the obligation was to complete the slab, not to release it to anybody, and the works information says nothing about a handover.</p>
                            <p>Two determinations, made properly, on the same fortnight. One says the delay happened and one says it did not. Nothing in either contract requires the two to agree, and no mechanism exists to make them.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What the role actually covers</h2>
                            <p><a href="contract-week-3.html">Contract Week 3</a> set out the Engineer as one role on one contract: authority delegated by the employer, a duty to act impartially in reaching a determination, and a decision that binds both parties until challenged.</p>
                            <p>Every word of that survives on a multi-contract job. What does not survive is the assumption underneath it, which is that there is one of them.</p>
                            <p>Each package contract appoints its own. Sometimes the same firm is named in several &#8212; and as <a href="interfaces-week-3.html">last week</a> set out, sometimes it is named in some and not others. Whatever the arrangement, the appointment is made contract by contract, and so is the authority.</p>

                            <h2>Impartial between whom</h2>
                            <p>The duty to act impartially is narrower than it sounds, and the narrowness is the point.</p>
                            <p>An Engineer administering the mechanical contract owes duties under the mechanical contract. They must hold the balance between that employer and that contractor. They owe nothing at all to the civil contractor, who is a stranger to the contract they are administering.</p>
                            <p>So when they determine that two weeks were lost through no fault of the mechanical contractor, they are not making a finding against the civil contractor. They are answering a question that was only ever about their own contract, and they are answering it correctly.</p>
                            <p>The finding that the civil contractor caused it would have to be made under the civil contract, by a different Engineer, on evidence that Engineer can compel &#8212; and the mechanical contractor&#39;s records are not evidence they can compel.</p>

                            <h2>The evidence does not travel</h2>
                            <p>This is where the practical difficulty sits, and it is a records problem before it is a legal one.</p>
                            <p>A determination is made on what the determining Engineer has in front of them. Under one contract that is the whole project: one set of programmes, one daily record, one progress figure. Across contracts each Engineer sees one package&#39;s documents, produced by one party, in that party&#39;s format and on that party&#39;s cut-off.</p>
                            <p>Neither of them is looking at the other&#39;s programme. Neither can require it. So the same fortnight is examined twice, from two record sets that were never reconciled, by two people with no obligation to speak to each other.</p>
                            <p>Which means an analysis prepared for one determination may be useless in the other &#8212; not because it is wrong, but because it rests on documents the second Engineer has no access to and no duty to consider.</p>

                            <h2>Who carries the gap</h2>
                            <p>When the two determinations do not match, the difference has to land somewhere, and the contracts decide where.</p>
                            <p>An extension granted under one contract costs the employer time. A deduction not recoverable under another costs the employer money. On a single contract those two questions are the same question with one answer; here they are separate questions, separately answered, and the employer holds whatever falls between.</p>
                            <p>That is not an accident of drafting. It is the integration risk from <a href="interfaces-week-2.html">week 2</a> arriving in a specific form: the employer took the interfaces back when the packages were let, and this is one of the bills for it.</p>

                            <h2>What a planner produces</h2>
                            <p>Two things change in the work itself.</p>
                            <p><strong>An analysis is prepared for a determination, not for a project.</strong> The question is which contract it will be read under and which Engineer will read it. The same event can need two, built on different record sets, reaching conclusions that are consistent with each other but not identical.</p>
                            <p><strong>The interface obligation has to be found before it is needed.</strong> If the civil contract does not oblige a handover to the follow-on trade, that is knowable on day one by reading it. Discovering it during a determination is what turns a schedule problem into an unrecoverable one.</p>
                            <p>Neither of those is a technique. They are a reordering of when the reading happens, and the cost of getting the order wrong is measured in weeks nobody can recover.</p>

                            <h2>Practical insight</h2>
                            <p>Take one interface on your project where another party has to finish before you can start.</p>
                            <p>Answer three questions from the contracts rather than from the programme. Does their contract oblige them to hand that area over to you, or only to complete their own work? If they are late, which Engineer determines your entitlement, and do they have any authority over the party who caused it? And if your extension is granted, is there a route by which the employer recovers it from them?</p>
                            <p>Where the answers are handover-not-obliged, different-Engineer, and no-route, you have found a delay that will be granted to you and paid for by nobody &#8212; which is the best possible position to be in, and worth knowing before you need it rather than after.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Every word of the Engineer&#39;s role survives on a multi-contract job. The assumption that there is one of them does not.</li>
                            <li>The appointment is made contract by contract, and so is the authority.</li>
                            <li>Impartiality runs between the parties to that contract. An Engineer owes nothing to a contractor who is a stranger to it.</li>
                            <li>A determination that two weeks were lost is not a finding against whoever caused them.</li>
                            <li>Evidence does not travel. Each Engineer sees one package&#39;s records and can compel nothing from the other.</li>
                            <li>The same fortnight can be examined twice, from two record sets, by two people with no duty to speak.</li>
                            <li>Where the determinations differ, the employer holds the difference. That is the integration risk arriving in a specific form.</li>
                            <li>Read the interface obligation on day one. Finding out during a determination is what makes a delay unrecoverable.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The Engineer register, one line per package &#183; the handover obligation for each interface, quoted from the contract &#183; the determination log with the contract it was made under.</p>

                            <h2>What is coming next</h2>
                            <p>If two Engineers can reach opposite conclusions on the same fortnight, the question of what counts as a concurrent delay has no single place to be decided either.</p>
                            <p>Next week: concurrency where there is no head contract, and the Particular Conditions that do not exist.</p>'''

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
    ["Engineer register", "Contracts", "One line per package: who, and with what delegated powers",
     "The appointment clause in each", "Where a determination is sought"],
    ["Handover obligation", "Contracts", "Quoted, not summarised &#8212; complete, or release to a named party",
     "The works information", "Interface register &#183; delay events"],
    ["Determination log", "Project controls", "The decision, its date, and the contract it was made under",
     "The determination itself", "Entitlement &#183; recovery position"],
    ["Record set per package", "Each contractor", "Known to be separate, on separate cut-offs",
     "The reporting calendar", "What each Engineer can actually see"],
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
    ("Nothing in either contract requires the two to agree, and no mechanism exists to make them.",
     SVG.format(h=220) + head("ONE FORTNIGHT, TWO DETERMINATIONS")
     + box(150, 42, 340, 40, "The slab is two weeks late")
     + box(24, 112, 270, 72, "Mechanical Engineer", "delay found &#183; extension granted", "good")
     + box(346, 112, 270, 72, "Civil Engineer", "obligation met &#183; no delay", "good")
     + '<text x="320" y="204" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Both correct. Neither reconciles with the other.</text>'
     + "</svg>",
     "Figure 1 &#8212; Each determination answers a question about its own contract. Nothing in the structure produces a single answer, because nothing asked a single question."),
    ("who is a stranger to the contract they are administering.",
     SVG.format(h=190) + head("WHERE IMPARTIALITY RUNS")
     + box(30, 50, 265, 84, "Employer and this contractor", "the duty is here", "good")
     + box(345, 50, 265, 84, "The other contractor", "no duty at all", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">Holding the balance does not mean holding it between contractors.</text>'
     + "</svg>",
     "Figure 2 &#8212; The duty is real and it is narrow. A determination in your favour is not a finding against the party who caused the delay, and was never capable of being one."),
    ("by two people with no obligation to speak to each other.",
     SVG.format(h=200) + head("WHAT EACH ENGINEER CAN SEE")
     + box(24, 50, 270, 62, "Package A records", "programme, daily, progress")
     + box(346, 50, 270, 62, "Package B records", "programme, daily, progress")
     + '<text x="320" y="140" text-anchor="middle" fill="#dc2626" font-size="12.5" font-weight="700">Neither can compel the other set.</text>'
     + '<text x="320" y="168" text-anchor="middle" fill="#64748b" font-size="11.5">Two cut-off dates, two formats, never reconciled.</text>'
     + "</svg>",
     "Figure 3 &#8212; A determination is made on what is in front of the person making it, which is why an analysis built for one can be unusable in the other."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>Four records, none of which needs a system, and all of which have to exist before a '
          'determination rather than during one.</p>\n                            ' + table()
          + '\n                            '
          '<p>The second row is the one worth doing first and the one most projects skip. Quoting '
          'the handover obligation rather than summarising it matters because the difference between '
          '&#8220;complete the slab&#8221; and &#8220;release the slab to the following trade&#8221; '
          'is the entire question, and a summary loses it.</p>')


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

    old_share = ("He runs the site, chairs every meeting and signs nothing. Whether his instruction "
                 "binds anybody depends on a clause most people on site have never read.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-3.html", "interfaces-week-4.html")
    s = s.replace('data-current-week="3"', 'data-current-week="4"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 4<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 4", s, 1)
    s = s.replace("Interfaces &#183; Week 3", "Interfaces &#183; Week 4")
    # the body links back to week 3; the filename swap above would have eaten it
    s = s.replace('<a href="interfaces-week-4.html">last week</a>',
                  '<a href="interfaces-week-3.html">last week</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-4.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-4.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
