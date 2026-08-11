#!/usr/bin/env python3
"""Builds interfaces-week-9.html.

Template is interfaces-week-8.html.

The kickoff named this the first candidate for removal, on the risk that it
becomes a catalogue of financing structures. It is written to one failure
instead: a payment certified under the contract that does not arrive, because
a party with no contractual relationship to anybody on site has not signed
something the construction contract never mentions.

PPP, concession and BOT are named once between them. None is defined.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-8.html"
OUT = ROOT / "drafts" / "interfaces-week-9.html"

TITLE = "Financed projects — the lender's adviser and the certificate that does not pay"
DESC = ("When the employer is a special purpose vehicle, payment depends on a drawdown certified by "
        "somebody outside the construction contract. A second Engineer nobody planned for.")
OG = "Certified, and still not paid"
SHARE = ("The certificate was valid and the money did not come. The gate that stopped it is in a "
         "financing agreement the contractor has never seen.")
CRUMB = "When the employer is a vehicle"
H1 = "Certified, and still not paid."

BODY = '''<h2 style="margin-top:0;">Certified, and still not paid</h2>
                            <p>The application goes in, the Engineer certifies it, and the certificate is correct in every respect. <a href="contract-week-12.html">Contract Week 12</a> describes exactly this mechanism and it has worked exactly as described.</p>
                            <p>The money does not arrive. Not because it is disputed &#8212; nobody disputes it &#8212; but because the employer is a company formed to build this one asset, it has no money of its own, and the funds it will pay you with have to be released by lenders first.</p>
                            <p>That release depends on a certification from somebody who is not a party to your contract, whose name does not appear in it, and whose requirements you have never been shown.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What the employer actually is</h2>
                            <p>On a financed project &#8212; a concession, a PPP, a build-own-transfer &#8212; the entity signing the construction contract is a vehicle created for the purpose. It exists to hold the asset, service the debt and pass revenue back to its shareholders.</p>
                            <p>What matters for project controls is narrower than any of that. This employer does not have a treasury it can pay you from. Every payment comes from a drawdown against a facility, and every drawdown has conditions attached to it that were negotiated before the construction contract was signed and are not in it.</p>
                            <p>So the payment chain has a gate the contract does not describe. Everything <a href="cost-week-17.html">Cost &amp; Cash Week 17</a> says about the interim cycle still applies, with one extra step that can add weeks and is invisible from inside the contract.</p>

                            <h2>A second Engineer with no contract</h2>
                            <p>The lenders appoint their own technical adviser. Their job is to protect the lenders&#39; position: to confirm that the works are progressing as represented, that the money drawn matches value created, and that the asset will do what the financial model assumes.</p>
                            <p>That person has no authority over the contractor. They cannot instruct, cannot vary, cannot determine. This is <a href="interfaces-week-3.html">week 3</a> again in a different costume, with one difference that matters: the managing contractor there had authority in practice and none on paper, while this adviser has no authority in either sense and controls the money anyway.</p>
                            <p>They do it through certification of the drawdown rather than through the contract. Which means a request that would be an unreasonable demand if it came from the Engineer is, from them, simply a condition of the project being funded that month.</p>

                            <h2>The reporting stream nobody priced</h2>
                            <p>The immediate consequence lands on project controls and it lands as work.</p>
                            <p>The adviser reports to the lenders on their own cycle, to their own format, against the financial model rather than against the programme. They will want progress expressed in a way that maps to drawdown, evidence to a standard set by a credit committee rather than by an Engineer, and confirmation of things the construction contract does not require anybody to confirm.</p>
                            <p>None of that is in the tender. It is a second reporting obligation, to a second audience, with a second definition of what counts as progress &#8212; and by <a href="reporting-week-20.html">Reporting Week 20</a>&#39;s standard it is a fifth document produced from a different extraction, which is exactly the condition under which numbers stop reconciling.</p>

                            <h2>Two sets of milestones</h2>
                            <p>The second consequence is slower and it catches people at the end.</p>
                            <p>The construction contract has completion, taking over, and whatever sectional dates were agreed. The financing agreement has its own: conditions for the final drawdown, a date by which the asset must be generating revenue, and tests the lenders require before the debt converts to its operating terms.</p>
                            <p>These are not the same dates and they do not have to be. A contractor can achieve completion under the contract and leave the vehicle unable to satisfy its lenders, or the reverse. The pressure that then arrives on the programme comes from a document nobody on the delivery side has read.</p>
                            <p>Which is why the useful question at the start is not what the completion date is. It is what the vehicle has to demonstrate, to whom, and by when &#8212; because that is the date the project is actually being run to.</p>

                            <h2>What a planner does about it</h2>
                            <p>Three things, and none of them requires access to the financing agreement itself.</p>
                            <p>Establish the drawdown cycle and put it in the cash flow. The gap between certification and payment is a working capital cost, and on this structure it is longer and less predictable than the contract implies.</p>
                            <p>Ask what the adviser needs and when, then produce it from the same extraction as everything else. The alternative is somebody assembling it separately each month, and two versions of the progress figure reaching two audiences.</p>
                            <p>And find out which financing milestones exist, even approximately. Not to manage them &#8212; they are not yours &#8212; but because they explain instructions that otherwise look arbitrary, and knowing why a date matters is what lets you argue about it.</p>

                            <h2>Practical insight</h2>
                            <p>Find out, for your own project, how long it takes between the Engineer certifying and the money reaching your account.</p>
                            <p>Compare that with the period the contract states. If they differ by more than a few days, ask what happens in the gap. On a financed structure there is a drawdown cycle in there, with a date each month that nothing in your contract mentions.</p>
                            <p>Then put that date in your own calendar next to the certification date. It costs you nothing, and it turns an unpredictable payment into a predictable one &#8212; which is the whole of what your treasury needs from you.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A vehicle employer has no money of its own. Every payment is a drawdown against a facility.</li>
                            <li>The drawdown carries conditions negotiated before the construction contract and absent from it.</li>
                            <li>The lenders&#39; adviser cannot instruct, vary or determine, and controls the money regardless.</li>
                            <li>They exercise it through certification rather than through the contract, so their requests are funding conditions rather than instructions.</li>
                            <li>They report on their own cycle, to their own format, against the financial model rather than the programme.</li>
                            <li>That is a second reporting obligation to a second audience, produced from a second extraction unless somebody prevents it.</li>
                            <li>Financing milestones are not contract milestones, and the pressure on the programme often comes from the first.</li>
                            <li>Put the drawdown cycle in the cash flow. The gap between certification and payment is a real working capital cost.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The drawdown calendar alongside the certification calendar &#183; the adviser&#8217;s evidence requirements &#183; the financing milestones, as far as they are knowable.</p>

                            <h2>What is coming next</h2>
                            <p>That is every party. From here the track turns to the physical work, and to the part of it that appears in nobody&#39;s scope until somebody has to build it.</p>
                            <p>Next week: the work in nobody&#39;s scope, and the gap between two risk registers.</p>'''

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
    ["Drawdown calendar", "Project controls", "The date each month funds are released, not the contract period",
     "The employer&#8217;s finance team", "Cash flow &#183; working capital"],
    ["Adviser evidence list", "Project controls", "What they need and when, asked for rather than discovered",
     "The adviser directly", "The monthly extraction"],
    ["Financing milestones", "Project controls", "Known approximately, even where the agreement is not shared",
     "The employer", "Why a date matters"],
    ["One extraction, two audiences", "Project controls", "The adviser&#8217;s pack built from the same cut as the monthly report",
     "The reporting calendar", "Whether the two figures agree"],
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
    ("whose requirements you have never been shown.",
     SVG.format(h=200) + head("THE GATE THE CONTRACT DOES NOT DESCRIBE")
     + box(10, 56, 145, 60, "Application", "")
     + box(165, 56, 145, 60, "Certificate", "valid", "good")
     + box(320, 56, 155, 60, "Drawdown", "conditions apply", "bad")
     + box(485, 56, 145, 60, "Payment", "", "plain")
     + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">The third box is in a document you have never seen.</text>'
     + "</svg>",
     "Figure 1 &#8212; Everything the contract describes happened correctly. The step that stopped the money is not in the contract at all."),
    ("while this adviser has no authority in either sense and controls the money anyway.",
     SVG.format(h=200) + head("TWO KINDS OF AUTHORITY")
     + box(24, 52, 270, 76, "Managing contractor", "authority in practice, none on paper", "bad")
     + box(346, 52, 270, 76, "Lenders&#39; adviser", "no authority, holds the money", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">Neither can instruct. Only one of them decides whether you are paid.</text>'
     + "</svg>",
     "Figure 2 &#8212; A request that would be unreasonable from the Engineer is, from the adviser, a condition of the project being funded that month."),
    ("comes from a document nobody on the delivery side has read.",
     SVG.format(h=200) + head("TWO SETS OF DATES")
     + box(24, 52, 270, 76, "Contract", "completion &#183; taking over", "good")
     + box(346, 52, 270, 76, "Financing agreement", "drawdown &#183; revenue date &#183; tests", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">They need not match, and the pressure usually comes from the right-hand set.</text>'
     + "</svg>",
     "Figure 3 &#8212; The useful question at the start is not the completion date. It is what the vehicle has to demonstrate, to whom, and by when."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>None of this needs the financing agreement. All of it can be assembled by asking the '
          'people who already have the answers.</p>\n                            ' + table()
          + '\n                            '
          '<p>The last row is the one that prevents the slower failure. An adviser&#8217;s pack '
          'assembled separately each month becomes a second version of the progress figure, reaching '
          'an audience with the power to stop the money, and neither audience knows the two documents '
          'differ.</p>')


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

    old_share = ("Nobody refused it. It went to three boards that meet monthly, on different weeks, "
                 "and the answer arrived after the work should have started.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-8.html", "interfaces-week-9.html")
    s = s.replace('data-current-week="8"', 'data-current-week="9"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 9<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 9", s, 1)
    s = s.replace("Interfaces &#183; Week 8", "Interfaces &#183; Week 9")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-9.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-9.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
