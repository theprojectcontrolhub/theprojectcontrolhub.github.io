#!/usr/bin/env python3
"""Builds interfaces-week-8.html.

Template is interfaces-week-7.html.

This week is the measurement-driven addition to the track: governance,
stakeholder and integration are the strongest terms in the whole source pool
and had no week in the original fourteen. It earns its place on a failure
rather than on the sources — a decision that nobody refuses and nobody takes,
which has no signature and therefore no owner.

The risk is that it becomes governance theory. The guard is that everything
here is about lead time and records, which are planning objects.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-7.html"
OUT = ROOT / "drafts" / "interfaces-week-8.html"

TITLE = "Decision lead time across organisations — governance as a programme input"
DESC = ("A decision three companies need is not refused. It waits, through three internal approval "
        "cycles, and the waiting has no owner, no date and no signature.")
OG = "Nobody said no"
SHARE = ("Nobody refused it. It went to three boards that meet monthly, on different weeks, and the "
         "answer arrived after the work should have started.")
CRUMB = "Governance across organisations"
H1 = "Nobody said no."

BODY = '''<h2 style="margin-top:0;">Nobody said no</h2>
                            <p>A sequence change is needed. It saves three weeks, everybody at the coordination meeting can see that it saves three weeks, and it affects the scope of three companies.</p>
                            <p>Nine weeks later it has not happened. Nobody has refused it. It went to one company&#39;s regional office for a commercial view, to another&#39;s board because it crossed their delegation limit, and to the third&#39;s technical authority for review. Those three bodies meet monthly, on different weeks, and none of them was waiting for the others.</p>
                            <p>There was no obstruction and there is no one to chase. The three weeks the change would have saved were spent obtaining permission to save them.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Agreement is not authority</h2>
                            <p>The coordination meeting is where this goes wrong, and it goes wrong pleasantly.</p>
                            <p>Everybody in the room agrees. They are the right people, they understand the problem, and their agreement is genuine. What none of them has is authority to bind their own company to something that changes its scope or its price.</p>
                            <p>So the meeting produces a consensus, the minutes record it as agreed, and everybody leaves believing a decision has been taken. What has actually happened is that three separate approval processes have been started, informally, by three people who will now have to explain the proposal to somebody who was not in the room.</p>
                            <p>On a single contract that gap barely exists: the Engineer determines, or the employer instructs, and the authority sits inside the process. Across organisations the authority sits inside each company, and the project has no visibility of it at all.</p>

                            <h2>Three gates, three calendars</h2>
                            <p>What determines how long this takes is not goodwill. It is the shape of each party&#39;s internal governance, and it is knowable in advance.</p>
                            <p>Each company has a delegation limit &#8212; a value above which the site cannot commit and something more senior has to. Each has a body that takes those decisions and a cycle on which it meets. Each has its own view of what constitutes a change worth escalating.</p>
                            <p>A proposal that sits below every party&#39;s threshold is decided on site in a day. The same proposal a little larger crosses one party&#39;s limit and waits for their monthly board. Larger still and it crosses all three, at which point the lead time is not the sum of the three cycles but the worst case of them &#8212; and worse if any one of them asks a question that sends it round again.</p>
                            <p>None of that is dysfunction. It is three companies each running a normal approval process, and the project is the place where the three calendars collide.</p>

                            <h2>The failure with no signature</h2>
                            <p>Here is what makes this different from an ordinary delay, and it is the reason the week exists.</p>
                            <p>When somebody refuses a decision, the refusal is an event. It has a date, a person and a reason, and there are mechanisms for what happens next &#8212; escalation, determination, a claim. It is unwelcome and it is visible.</p>
                            <p>A decision that is merely waiting produces none of that. There is no document recording that it has not been taken. Nobody has failed to do anything, because everybody is doing exactly what their own company requires. The programme slips by an amount nobody authorised, and afterwards there is no event to point at.</p>
                            <p>Which is why it survives so long. Every other cause of delay on a project generates paper of some kind. This one generates silence.</p>

                            <h2>Lead time is a planning object</h2>
                            <p>The useful move is the one <a href="reporting-week-15.html">Reporting Week 15</a> made for approvals: stop treating it as administration and put it in the programme.</p>
                            <p>A decision has a lead time. That lead time depends on which parties it crosses, what each of their thresholds is, and when their bodies meet. All three are findable before any particular decision is needed, and they change rarely.</p>
                            <p>Once they are written down, two things become possible that were not before. A decision needed for a March start can be raised in January rather than in March. And a proposal can be shaped to stay below a threshold when the saving does not justify the wait, which is a planning judgement rather than a commercial one.</p>

                            <h2>What to record</h2>
                            <p>The decision register from <a href="reporting-week-24.html">Reporting Week 24</a> needs two more columns on a multi-organisation job.</p>
                            <p>Which parties it crosses, because that determines the route. And which body in each party will take it, with the date that body next meets, because that determines the date.</p>
                            <p>With those two the register stops being a list of open items and becomes a forecast. An entry can be read as: this decision is required by the fourteenth, it crosses two parties, the later of their two boards sits on the ninth, and therefore it has to be lodged by the twenty-fifth of the previous month. That is a date somebody can work to, and it is the only form in which this problem is manageable.</p>

                            <h2>Practical insight</h2>
                            <p>Take the oldest open item on your own decision log and find out where it actually is.</p>
                            <p>Not who raised it &#8212; who is holding it now, which body has to approve it, and when that body next meets. There is a fair chance your answer is that nobody is considering it at all, because the person who took it away is waiting for a paper somebody else in their own company has to write first.</p>
                            <p>Then do the part that pays. For each party on your project, write down their delegation limit and their approval cycle. Three phone calls and an afternoon, and from then on every decision you raise carries a date you can plan against instead of an open one you have to chase.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A decision crossing three companies is not refused. It waits, in three separate approval processes.</li>
                            <li>Agreement in a coordination meeting is genuine and is not authority to bind a company.</li>
                            <li>The minutes record a decision. What started was three informal escalations to people who were not in the room.</li>
                            <li>Lead time is set by each party&#39;s delegation limit and the cycle on which its approving body meets.</li>
                            <li>Crossing several parties gives the worst case of their cycles, not the sum, and worse if anybody sends it round again.</li>
                            <li>A refusal is an event with a date and a mechanism. A decision that waits produces no document at all.</li>
                            <li>Every other cause of delay generates paper. This one generates silence, which is why it survives.</li>
                            <li>Record which parties a decision crosses and when their bodies meet, and the register becomes a forecast.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The delegation limit and approval cycle for each party &#183; the decision register with its route and its required-by date &#183; the note of what was agreed in a meeting and what was actually authorised.</p>

                            <h2>What is coming next</h2>
                            <p>Everything so far has treated the employer as one party with one interest. On a financed project it is a vehicle with lenders behind it, and they appoint their own adviser.</p>
                            <p>Next week: when the employer is a vehicle, and the second Engineer nobody planned for.</p>'''

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
    ["Delegation limit per party", "Project controls", "The value above which site cannot commit, per company",
     "Each party&#8217;s own procedure", "Which route a decision takes"],
    ["Approval cycle per party", "Project controls", "Which body decides and when it next meets",
     "Their meeting calendar", "The required-by date"],
    ["Decision register", "Project controls", "Route, approving body, and lodge-by date &#8212; not just an owner",
     "The two rows above", "Look-ahead &#183; programme"],
    ["Agreed versus authorised", "Project controls", "What a meeting agreed, and whether anybody could bind it",
     "The minutes", "What is actually decided"],
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
    ("The three weeks the change would have saved were spent obtaining permission to save them.",
     SVG.format(h=220) + head("ONE PROPOSAL, THREE ROUTES")
     + box(210, 42, 220, 44, "Sequence change agreed", "")
     + box(16, 118, 190, 62, "Regional office", "commercial view", "bad")
     + box(222, 118, 190, 62, "Board", "above delegation", "bad")
     + box(428, 118, 190, 62, "Technical authority", "review", "bad")
     + '<text x="320" y="200" text-anchor="middle" fill="#64748b" font-size="11.5">Three monthly cycles, different weeks, none waiting for the others.</text>'
     + "</svg>",
     "Figure 1 &#8212; Nobody obstructed anything. Three companies each ran a normal approval process, and the project is where the three calendars met."),
    ("three people who will now have to explain the proposal to somebody who was not in the room.",
     SVG.format(h=190) + head("WHAT THE MEETING PRODUCED")
     + box(30, 50, 265, 84, "Agreement", "genuine, by the right people", "good")
     + box(345, 50, 265, 84, "Authority", "held inside each company", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">The minutes say decided. Three escalations have started instead.</text>'
     + "</svg>",
     "Figure 2 &#8212; On a single contract the authority sits inside the process. Across organisations it sits inside each company, where the project cannot see it."),
    ("This one generates silence.",
     SVG.format(h=200) + head("TWO WAYS A DECISION FAILS")
     + box(24, 52, 270, 76, "Refused", "date, person, reason, mechanism", "good")
     + box(346, 52, 270, 76, "Waiting", "no document, no event", "bad")
     + '<text x="320" y="164" text-anchor="middle" fill="#64748b" font-size="11.5">Afterwards there is nothing to point at, which is why it survives so long.</text>'
     + "</svg>",
     "Figure 3 &#8212; A refusal is unwelcome and visible. A decision that is merely waiting slips the programme by an amount nobody authorised and nobody recorded."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>The first two rows are gathered once and change rarely. Everything else on this page '
          'depends on having them.</p>\n                            ' + table()
          + '\n                            '
          '<p>The third row is what turns a decision log into something a programme can use. An '
          'owner and a due date describe an intention; a route and a lodge-by date describe when '
          'the answer can physically arrive.</p>')


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

    old_share = ("On a claims contract the other side audits your figure. On an alliance nobody does, "
                 "and that is the harder position to be in.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-7.html", "interfaces-week-8.html")
    s = s.replace('data-current-week="7"', 'data-current-week="8"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 8<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 8", s, 1)
    s = s.replace("Interfaces &#183; Week 7", "Interfaces &#183; Week 8")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-8.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-8.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
