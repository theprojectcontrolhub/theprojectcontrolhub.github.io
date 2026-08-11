#!/usr/bin/env python3
"""Builds interfaces-week-11.html.

Template is interfaces-week-10.html.

Week 10 produced the register. This week is about who owns it, and the failure
it is built on is specific: a register maintained by somebody with no power to
close anything is worse than no register, because it produces the appearance
of management without any of it.

The closure definition is the load-bearing idea. An interface item is not
closed by agreement; it is closed when one party accepts it into scope with a
price and a date.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-10.html"
OUT = ROOT / "drafts" / "interfaces-week-11.html"

TITLE = "Interface management — owning a boundary rather than reporting one"
DESC = ("An interface register that only grows is a list of known problems presented as management. "
        "What closing an item actually requires, and who can do it.")
OG = "The register that only grows"
SHARE = ("Forty open interfaces, reported monthly for a year, none of them closed. The reporting was "
          "immaculate. Nothing was being managed.")
CRUMB = "Interface management"
H1 = "The register that only grows."

BODY = '''<h2 style="margin-top:0;">The register that only grows</h2>
                            <p>The interface register exists. It is maintained, it is presented at the monthly meeting, and the number of open items on it has gone up every month for a year.</p>
                            <p>Nobody is doing anything wrong. Items are added as they are identified, which is correct. They are reviewed, which is correct. They are reported, which is correct.</p>
                            <p>What has not happened is that any of them has closed, and the reason is the same one <a href="reporting-week-24.html">Reporting Week 24</a> gave for a risk register that never shrinks: nothing on the page is connected to anybody who can decide.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Reporting a boundary and owning one</h2>
                            <p>The distinction is easy to state and easy to lose.</p>
                            <p>Reporting a boundary means knowing it exists, describing what happens there, and telling people about it on a cycle. It produces an accurate document and it changes nothing.</p>
                            <p>Owning a boundary means being answerable for whether it is resolved. That requires the ability to force a question to a decision, which is a different thing from the ability to write the question down.</p>
                            <p>The title implies the second. Where a project has only the first, the gap between them is where a year of open items comes from.</p>

                            <h2>What closing an item actually means</h2>
                            <p>This is the load-bearing definition and it is stricter than the one most registers use.</p>
                            <p>An interface item is not closed when the parties agree what should happen there. It is not closed when a drawing is issued showing the detail. It is not closed when everybody in a meeting nods.</p>
                            <p>It is closed when one party has accepted the work into their scope, with a price and a date. Until that has happened, what exists is a shared understanding, and <a href="interfaces-week-3.html">week 3</a> covered what a shared understanding is worth when money is involved.</p>
                            <p>Applying that definition to an existing register is uncomfortable and useful. Items that have been marked closed for months turn out to be agreements nobody priced. That is not a bookkeeping correction; those are live exposures that the register was reporting as resolved.</p>

                            <h2>The authority problem</h2>
                            <p>Whoever holds the function generally cannot close anything themselves, and the reason is structural rather than personal.</p>
                            <p>Closing an item means somebody takes scope and cost. That is a commercial decision inside one of the contracting parties, and as <a href="interfaces-week-8.html">week 8</a> established, it may sit above the site&#39;s delegation limit and require a body that meets monthly.</p>
                            <p>So the function cannot instruct. What it can do is narrower and still substantial: make the boundary visible before anybody reaches it, put the question in front of a named person on each side, and escalate on a date rather than on a crisis.</p>
                            <p>The third is the one that distinguishes the job from administration. An item raised in March with a required-by date of June, escalated in April because no answer has come, is being managed. The same item raised in March and reported every month until June is being watched.</p>

                            <h2>Where the function sits</h2>
                            <p>Three placements are common and two of them have a structural problem.</p>
                            <p>Inside one of the contracting parties, the function is doing its own company&#39;s commercial work. That may be entirely legitimate and it is not neutral, and the other parties will treat the register accordingly.</p>
                            <p>With the employer alone, it has the standing to escalate without necessarily having the technical detail to know a boundary exists before somebody reaches it.</p>
                            <p>The version that works sits with project controls, for the reason <a href="reporting-week-14.html">Reporting Week 14</a> gave about noticing inconsistencies: it is the only function with the programme, the scope documents and the records of every party open at the same time. That does not confer authority. It confers early sight, which is the input the authority needs.</p>

                            <h2>The harm in a good-looking register</h2>
                            <p>One more point, because it is the reason this matters more than it appears.</p>
                            <p>A project with no interface register has a visible problem. Somebody will eventually notice that nobody is looking at the boundaries.</p>
                            <p>A project with a well-maintained register that closes nothing has an invisible one. The document is evidence that the subject is being handled. It is presented monthly, it is accurate, and it satisfies the question. Meanwhile the items on it arrive in the field one by one, exactly as they would have without it.</p>
                            <p>Which is the same shape as <a href="reporting-week-26.html">Reporting Week 26</a>: a report that is entirely correct and changes nothing. The difference is that here the report is also the reason nobody asks.</p>

                            <h2>Practical insight</h2>
                            <p>Open your own interface register and apply the closure test to every item you have marked closed. Has a party accepted that work into their scope, with a price and a date?</p>
                            <p>Whatever fails goes back to open. Your register will look considerably worse than it did this morning, and the number you are left with is the one you actually have.</p>
                            <p>Then take your oldest genuinely open item and give it the two things it probably lacks: a named person on each side rather than a company, and a date by which you need the answer rather than the date you raised it. Put that escalation date in your calendar and act on it whether or not anything has happened. That one change is most of the distance between the two versions of your job.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A register that only grows has nothing on it connected to somebody who can decide.</li>
                            <li>Reporting a boundary produces an accurate document. Owning one means being answerable for whether it resolves.</li>
                            <li>An item is not closed by agreement, by a drawing, or by a meeting.</li>
                            <li>It is closed when one party accepts the work into scope, with a price and a date.</li>
                            <li>Items that fail that stricter test are live exposures the register was reporting as resolved.</li>
                            <li>The function cannot instruct, because closure is a commercial decision inside a contracting party.</li>
                            <li>What it can do is make the boundary visible early, name a person on each side, and escalate on a date rather than on a crisis.</li>
                            <li>A well-maintained register that closes nothing is worse than none, because it answers the question that would otherwise be asked.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The interface register with a named person per side &#183; the required-by date and the escalation date &#183; the closure evidence: scope accepted, priced, dated.</p>

                            <h2>What is coming next</h2>
                            <p>Boundaries in space are one problem. The same packages also produce boundaries in time, and each party arrives with a programme built to its own rules.</p>
                            <p>Next week: three programmes and one project &#8212; detail, data dates and calendars that do not match.</p>'''

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
    ["Interface item", "Project controls", "What physically happens at the boundary, in one line",
     "The boundary register", "Scope acceptance"],
    ["Named person each side", "Project controls", "A person who can take it internally, not a company",
     "The organisation charts", "Escalation"],
    ["Required-by date", "Project controls", "When the answer is needed, derived from the programme",
     "The look-ahead", "Escalation date"],
    ["Escalation date", "Project controls", "Set in advance and acted on whether or not there is news",
     "The decision lead times", "Governance route"],
    ["Closure evidence", "The accepting party", "Scope accepted, priced, dated &#8212; not an agreement",
     "The variation or instruction", "Budget &#183; programme"],
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
    ("the gap between them is where a year of open items comes from.",
     SVG.format(h=190) + head("TWO VERSIONS OF THE SAME JOB")
     + box(30, 50, 265, 84, "Reporting a boundary", "accurate, changes nothing", "bad")
     + box(345, 50, 265, 84, "Owning a boundary", "answerable for the outcome", "good")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">The title implies the second. Most projects have the first.</text>'
     + "</svg>",
     "Figure 1 &#8212; Writing the question down and forcing it to a decision are different capabilities, and only one of them makes the register move."),
    ("those are live exposures that the register was reporting as resolved.",
     SVG.format(h=210) + head("WHAT COUNTS AS CLOSED")
     + box(16, 52, 190, 62, "Parties agree", "", "bad")
     + box(222, 52, 190, 62, "Drawing issued", "", "bad")
     + box(428, 52, 190, 62, "Scope accepted", "priced and dated", "good")
     + '<text x="320" y="150" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">Only the third one is closure.</text>'
     + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">Apply this to an existing register and the open count goes up.</text>'
     + "</svg>",
     "Figure 2 &#8212; The first two feel like progress and are shared understandings. What they are worth when money is involved is a separate question with a known answer."),
    ("The difference is that here the report is also the reason nobody asks.",
     SVG.format(h=200) + head("WHICH PROJECT IS IN MORE TROUBLE")
     + box(24, 52, 270, 76, "No register", "visible problem", "bad")
     + box(346, 52, 270, 76, "Register that closes nothing", "invisible problem", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">One of them will eventually be noticed. The other satisfies the question.</text>'
     + "</svg>",
     "Figure 3 &#8212; The items arrive in the field one by one either way. On the right, the document was the evidence that somebody was handling it."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>Five fields, of which most registers carry the first and the last in a weaker form. '
          'The middle three are what make the function a job rather than a report.</p>\n'
          '                            ' + table() + '\n                            '
          '<p>The escalation date is the field that does the work and the one nobody sets. A date '
          'fixed in advance and acted on regardless converts chasing into a routine, which is the '
          'only form in which it survives a busy month.</p>')


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

    old_share = ("Two bills, both complete and correct, and the connection between them is in "
                 "neither. Nobody was careless. Completeness is not coverage.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-10.html", "interfaces-week-11.html")
    s = s.replace('data-current-week="10"', 'data-current-week="11"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 11<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 11", s, 1)
    s = s.replace("Interfaces &#183; Week 10", "Interfaces &#183; Week 11")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bhas not\b", "hasn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-11.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-11.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
