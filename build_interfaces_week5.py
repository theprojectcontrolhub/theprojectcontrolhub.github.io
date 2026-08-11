#!/usr/bin/env python3
"""Builds interfaces-week-5.html.

Template is interfaces-week-4.html.

Claims Week 16 establishes that concurrency has no definition in the standard
forms and lives in the Particular Conditions. This week is what happens to
that when there is no single contract for the provision to live in — and the
more useful finding, which is that most cross-contract delay is not
concurrency at all and treating it as such answers the wrong question.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-4.html"
OUT = ROOT / "drafts" / "interfaces-week-5.html"

TITLE = "Concurrency across contracts — the Particular Conditions that do not exist"
DESC = ("Concurrency needs one contract and two causes of different kinds. Across packages the "
        "usual case is neither, and framing it as concurrency answers a question nobody asked.")
OG = "The wrong question, carefully answered"
SHARE = ("A concurrency analysis on a multi-package job often answers a question neither contract "
         "is asking. The framing is the error, not the arithmetic.")
CRUMB = "Concurrency with no head contract"
H1 = "The wrong question, carefully answered."

BODY = '''<h2 style="margin-top:0;">The wrong question, carefully answered</h2>
                            <p>Two weeks are lost. The mechanical contractor was waiting for a slab that came late, and during the same fortnight their own pipe spools had not arrived from a supplier they chose.</p>
                            <p>That looks exactly like concurrency, so it gets analysed as concurrency: two causes, one delay, and the familiar argument about which one drove it.</p>
                            <p>The analysis is careful and it is answering a question that neither contract asks. Under the mechanical contract the late slab is not a competing cause &#8212; it is an employer risk event, because access was owed and not given. And the pipe spools are a contractor risk event under the same contract. That is not concurrency between two contractors. It is concurrency in the ordinary sense, inside one contract, and it is the only place the question can be asked.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What concurrency needs in order to exist</h2>
                            <p><a href="claim-week-16.html">Claims Week 16</a> set the ground: the standard forms do not define concurrency, the definition lives in the Particular Conditions when it lives anywhere, and two analysts can reach opposite answers on the same facts.</p>
                            <p>Underneath all of that is a requirement so obvious it is never stated. Concurrency is a question about one contract. It compares two causes of delay to the same completion date, where the contract allocates one of them to the employer and one to the contractor, and asks what follows when both are running.</p>
                            <p>Take away the single contract and the comparison has nothing to sit in. Two delays under two contracts are not competing for anything: each is measured against its own completion date, its own allocation of risk, and its own extension mechanism.</p>

                            <h2>Why the cross-contract case is not it</h2>
                            <p>This is the part worth being precise about, because getting it wrong produces a lot of work that cannot be used.</p>
                            <p>When another contractor delays you, that event reaches your contract through the employer. Access, possession or a preceding-work obligation was owed to you by the employer, and it was not delivered. What the employer&#39;s reason was &#8212; that a different contractor was late &#8212; is not a matter your contract addresses.</p>
                            <p>So from inside your contract it is a single employer risk event, and it is claimed as one. The other contractor is not a party to that analysis and their delay is not a competing cause. It is the mechanism by which the employer failed to perform.</p>
                            <p>Which means the concurrency question, if there is one, is between that employer risk event and something you did &#8212; your own late spools, your own resourcing. Exactly as it would be on a single-contract job.</p>

                            <h2>Where the real problem moves to</h2>
                            <p>The genuine multi-contract difficulty has not disappeared. It has moved to the employer, and it has no forum.</p>
                            <p>The employer has granted an extension to the mechanical contractor because access was late. They now want to recover that from the civil contractor. As <a href="interfaces-week-4.html">last week</a> set out, that is a separate determination under a separate contract, and it turns on whether the civil contract obliged a handover at all.</p>
                            <p>If it did, the employer has a recovery. If it did not, the employer carries both: time given to one party and nothing recoverable from the other. And there is no contract in which that outcome can be argued, because the employer is not in dispute with themselves.</p>
                            <p>That is the shape of the problem. Not two contractors arguing about concurrency, but one employer holding a gap that neither contract creates a route to close.</p>

                            <h2>Two contracts, two tests</h2>
                            <p>There is a second difficulty and it is quieter.</p>
                            <p>Packages let at different times, by different teams, under different standard forms will not treat delay identically. One may carry a provision on concurrent delay and another may be silent. One may use a dominant cause approach and another an apportionment. One may define the completion obligation by section and another as a single date.</p>
                            <p>So the same fortnight can be tested two different ways, and the difference is not analysis &#8212; it is drafting that was settled before anybody on site arrived. An approach that produces an extension under one contract can produce nothing under the other, on identical facts, correctly.</p>
                            <p><a href="claim-week-15.html">Claims Week 15</a> showed that method choice is the real dispute between two analysts. Here the method is not chosen by the analyst at all. It is chosen by whichever contract the question is being asked under.</p>

                            <h2>What a planner does differently</h2>
                            <p>Before any analysis, one decision: which contract is this question being asked under? Everything else follows from it, including which records are admissible and which test applies.</p>
                            <p>Then a second: is the other party&#39;s delay a competing cause, or is it the reason an employer obligation was not performed? Wherever an access or possession obligation ran through the employer, it is the second, and recognising that turns a difficult concurrency argument into an ordinary extension claim with a straightforward evidential basis.</p>
                            <p>And where the employer is the one carrying the gap, the useful contribution is not an analysis. It is showing where the recovery route is missing, early enough that the next package contract is drafted with a handover obligation in it.</p>

                            <h2>Practical insight</h2>
                            <p>Take a delay on your project that you have been treating as concurrent, and separate the causes by contract rather than by date.</p>
                            <p>Write each cause down with one label: is this something my own contract makes my risk, something it makes the employer&#39;s risk, or something that happened under a contract I am not party to? The third category is the one that gets miscoded, and it belongs in the second.</p>
                            <p>If everything in your analysis falls into the third category, you do not have a concurrency question at all. You have an access claim, and it is a considerably easier one to run.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Concurrency compares two causes under one contract, where the contract allocates one to each party.</li>
                            <li>Two delays under two contracts compete for nothing. Each is measured against its own completion date and its own mechanism.</li>
                            <li>Another contractor&#39;s delay reaches you through the employer as a failure to give access or possession.</li>
                            <li>From inside your contract that is a single employer risk event, not a competing cause.</li>
                            <li>The real difficulty moves to the employer, who may hold time given and nothing recoverable.</li>
                            <li>There is no forum for that, because the employer is not in dispute with themselves.</li>
                            <li>Packages under different forms can test the same fortnight differently, and the method is chosen by the contract rather than the analyst.</li>
                            <li>Separate causes by contract before by date. Miscoding the third category is what turns an access claim into a concurrency argument.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The cause register coded by contract rather than by date &#183; the delay test that applies under each package &#183; the note of where a recovery route is missing.</p>

                            <h2>What is coming next</h2>
                            <p>So far the contractor on each package has been one company. Sometimes it is two or three, sharing a name on the contract and nothing else.</p>
                            <p>Next week: joint ventures and consortia &#8212; one face to the employer, several sets of books behind it.</p>'''

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
    ["Cause register", "Project controls", "Coded by contract and risk owner, not only by date",
     "The contract&#8217;s risk allocation", "Which claim is being run"],
    ["Delay test per package", "Contracts", "The concurrency and EOT wording, quoted per contract",
     "Each package contract", "Which method applies"],
    ["Employer risk events", "Project controls", "Access and possession failures, whatever caused them",
     "The access obligation", "Extension claim"],
    ["Missing recovery route", "Project controls", "Named where an obligation to hand over does not exist",
     "The upstream contract", "Drafting of the next package"],
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
    ("It is concurrency in the ordinary sense, inside one contract, and it is the only place the question can be asked.",
     SVG.format(h=210) + head("WHAT THE TWO CAUSES ACTUALLY ARE")
     + box(20, 50, 285, 76, "Slab late", "employer risk &#183; access not given", "bad")
     + box(335, 50, 285, 76, "Spools late", "contractor risk &#183; own supplier", "bad")
     + '<text x="320" y="156" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">One contract. One of each kind. That is the question.</text>'
     + '<text x="320" y="182" text-anchor="middle" fill="#64748b" font-size="11.5">The other contractor is not a party to it.</text>'
     + "</svg>",
     "Figure 1 &#8212; Coded by contract rather than by date, the fortnight resolves into the ordinary case. The difficulty was in the framing, not in the facts."),
    ("It is the mechanism by which the employer failed to perform.",
     SVG.format(h=200) + head("HOW ANOTHER CONTRACTOR REACHES YOU")
     + box(16, 56, 176, 60, "Civil late", "", "bad")
     + box(232, 56, 176, 60, "Employer", "owes you access")
     + box(448, 56, 172, 60, "Your claim", "one employer risk event", "good")
     + '<text x="320" y="146" text-anchor="middle" fill="#64748b" font-size="11.5">Your contract does not ask why the employer failed, only that it did.</text>'
     + "</svg>",
     "Figure 2 &#8212; The route runs through the employer, which is why it arrives as an access claim rather than as a competing cause."),
    ("because the employer is not in dispute with themselves.",
     SVG.format(h=190) + head("WHERE THE GAP SITS")
     + box(30, 50, 265, 84, "Time granted", "under the downstream contract", "bad")
     + box(345, 50, 265, 84, "Recovery", "only if a handover was owed", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">No contract exists in which the difference can be argued.</text>'
     + "</svg>",
     "Figure 3 &#8212; The multi-contract difficulty is real and it has moved. It sits with the employer, and no forum exists to resolve it because no two parties are in dispute."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The first row does the work and it is one extra column on a register that already '
          'exists.</p>\n                            ' + table() + '\n                            '
          '<p>Coding a cause by contract and risk owner rather than by date is what separates an '
          'access claim from a concurrency argument, and it has to happen when the event is '
          'recorded. Doing it afterwards means going back through a year of entries with a question '
          'nobody was asking at the time.</p>')


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

    old_share = ("The same two weeks produced an extension for one contractor and a deduction for "
                 "another. Both determinations were correct.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-4.html", "interfaces-week-5.html")
    s = s.replace('data-current-week="4"', 'data-current-week="5"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 5<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 5", s, 1)
    s = s.replace("Interfaces &#183; Week 4", "Interfaces &#183; Week 5")
    s = s.replace('<a href="interfaces-week-5.html">last week</a>',
                  '<a href="interfaces-week-4.html">last week</a>')

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bhas not\b", "hasn't"), (r"\bare not\b", "aren't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-5.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-5.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
