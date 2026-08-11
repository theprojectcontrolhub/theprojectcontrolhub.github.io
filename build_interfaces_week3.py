#!/usr/bin/env python3
"""Builds interfaces-week-3.html.

Template is interfaces-week-2.html.

Contract Week 6 already teaches which instructions are instructions on a
single contract. This week is the same question where the person giving them
is not a party to anything, which is a different failure rather than a harder
version of the same one.

EPCM is named and never defined for its own sake. The rule from the kickoff
holds: a delivery model appears only at the point where it breaks something.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "drafts" / "interfaces-week-2.html"
OUT = ROOT / "drafts" / "interfaces-week-3.html"

TITLE = "EPCM authority — instructions from a party with no contract"
DESC = ("A managing contractor runs the site and is in contract with nobody on it. When their "
        "instruction is binding, when it is only advice, and why nobody on site can tell the "
        "difference.")
OG = "The instruction that was not one"
SHARE = ("He runs the site, chairs every meeting and signs nothing. Whether his instruction binds "
         "anybody depends on a clause most people on site have never read.")
CRUMB = "Instructing without a contract"
H1 = "The instruction that was not one."

BODY = '''<h2 style="margin-top:0;">The instruction that was not one</h2>
                            <p>A change is instructed on Tuesday. The managing contractor&#39;s construction manager walks the area, says the pipe run has to move to clear the new access route, and the crew starts the next morning.</p>
                            <p>Six weeks later the cost is submitted and the employer&#39;s reply is that they never instructed it.</p>
                            <p>Both statements are true. The instruction happened, and the employer did not give it. Everybody in the chain behaved reasonably, and the work has been done and is not going to be paid for without an argument.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What that firm actually is</h2>
                            <p>The company running the site is not building anything. Their agreement with the employer is for services &#8212; management, engineering, procurement on the employer&#39;s behalf &#8212; and it is usually reimbursable or fee-based rather than lump sum.</p>
                            <p>Two consequences follow immediately and neither is obvious from the site.</p>
                            <p>They carry no delivery risk. A main contractor who lets the programme slip pays for it; a firm paid a fee for managing it does not, and on a reimbursable basis is paid for the extra months. Nothing follows from that about how any particular firm behaves. What follows is that the pressure a main contractor feels on the programme has no equivalent here, and if it is going to exist it has to be put in the agreement.</p>
                            <p>And they are not a party to any of the package contracts. Their construction manager can be the most senior person on site, chair every meeting, and still have no contractual relationship with the crew taking his instruction.</p>

                            <h2>Named, or not named</h2>
                            <p>Whether an instruction binds anybody comes down to one thing: whether the package contract names that firm.</p>
                            <p>Where it does &#8212; as the Engineer, as the Employer&#39;s Representative, or by an express delegation &#8212; the instruction has the standing <a href="contract-week-3.html">Contract Week 3</a> describes, and everything in <a href="contract-week-6.html">Contract Week 6</a> applies unchanged.</p>
                            <p>Where it does not, that person is a third party with an opinion. A reasonable, expert, well-informed opinion, from somebody the employer is paying to have it. It is still not an instruction, and work done on it is work done at the contractor&#39;s own risk.</p>
                            <p>The uncomfortable part is that the same firm can be named in one package contract and not in another. Same person, same site, same meeting: binding on the civil contractor and advisory to the mechanical one. Nothing on the site distinguishes the two, and neither of them has read the other&#39;s contract.</p>

                            <h2>Why it holds together anyway</h2>
                            <p>None of this surfaces while the instructions are small, and the reason it stays quiet is also the trap.</p>
                            <p>The instructions are generally sound, and structurally they would be: somebody with sight of the whole site sees a clash the individual packages cannot, so moving the pipe run is the correct answer. A contractor complies because the person asking is running the job, because refusing costs goodwill, and because the work is small enough that arguing about it costs more than doing it.</p>
                            <p>So instruction after instruction is absorbed without complaint, and a working convention forms: that firm instructs, the packages comply. The convention is real and the site runs on it.</p>
                            <p>What it is not is a contractual position, and the difference only appears on the instruction that turns out to cost money. By then the convention has been operating long enough that everybody on site believes it is how things work &#8212; and in the only sense that matters day to day, it has been.</p>

                            <h2>What a refusal would expose</h2>
                            <p>It is worth working through what happens if one contractor declines &#8212; reads their contract, sees that the instructing party is not named in it, and asks for the instruction to come through the employer.</p>
                            <p>They are within their rights, and it will be read as obstruction, because every previous instruction went through without this. Resolving it takes a confirmation from the employer or a delegation being produced, and work restarts.</p>
                            <p>The useful part is what the episode makes visible. One party knowing where it stands is enough to establish that the others did not, and the confirmation that follows is often the first time the authority has been written down at all. If it happens on a package you are planning, the days lost are not obstruction. They are the unwritten convention being tested for the first time.</p>

                            <h2>What a planner does with this</h2>
                            <p>Not much about the authority itself &#8212; that is a commercial question and it belongs to the contracts team. What sits with project controls is the record.</p>
                            <p>Every instruction that changes what gets built or when needs to be captured with three things: who gave it, on what date, and under which contract they were acting. The third is the one nobody writes down, and it is the one the argument turns on six weeks later.</p>
                            <p>Where the answer to the third is unclear, that is not a reason to stop work. It is a reason to say so at the time, in writing, to the party you do have a contract with. <a href="reporting-week-23.html">Reporting Week 23</a> made the case for the written record before the phone call; this is the same habit where the stakes are contractual rather than numerical.</p>
                            <p>None of that requires taking a position on whether the instruction was valid. It requires only that the question can be answered later by reading something rather than by remembering a site walk.</p>

                            <h2>Practical insight</h2>
                            <p>Find out this week whether the firm running your site is named in your own contract. It is one clause, somebody in commercial can point you at it in a minute, and you will get one of three answers: named with defined powers, named with powers nobody defined, or not named at all. Where you sit changes what your instructions are worth.</p>
                            <p>Then take last month&#39;s instructions &#8212; your meeting minutes, your marked-up drawings, your emails &#8212; and count how many of them record who gave the instruction and under what authority. On most multi-contract jobs your answer will be close to none.</p>
                            <p>Add the column this month rather than reconstructing it in a claim two years from now, when the person who gave you the instruction has left and you are working from memory.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A managing contractor holds a services agreement, not a works contract, and builds nothing.</li>
                            <li>They carry no delivery risk. Time lost is time paid for, which changes the incentive to compress.</li>
                            <li>Whether their instruction binds depends on whether the package contract names them.</li>
                            <li>Named as Engineer or Employer&#39;s Representative, everything in the contract track applies unchanged.</li>
                            <li>Not named, the same person is an expert third party and compliance is at the contractor&#39;s own risk.</li>
                            <li>The same firm can be named in one package contract and not in another, and nothing on site shows which.</li>
                            <li>A working convention forms because the instructions are usually right and usually small.</li>
                            <li>Capture who instructed, when, and under which contract. The third is what the argument turns on.</li>
                            </ul>
                            <p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;"><strong style="color:#334155;">Records born here.</strong> The authority register, one line per party &#183; the instruction log with its authority column &#183; the written query when the authority is unclear.</p>

                            <h2>What is coming next</h2>
                            <p>If a managing contractor is named as the Engineer in three package contracts and not in the other two, there is not one Engineer on the project. There are three, or none, depending on which contract is being read.</p>
                            <p>Next week: determination and impartiality when every package has its own Engineer.</p>'''

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
    ["Authority register", "Contracts", "One line per party: named, named without powers, or not named",
     "The clause in each package contract", "Whether an instruction is valid"],
    ["Instruction log", "Project controls", "Who, when, and under which contract they acted",
     "Minutes, marked drawings, email", "Variation &#183; delay event"],
    ["Query on unclear authority", "Project controls", "Sent to the party you are in contract with, at the time",
     "The instruction itself", "Entitlement, months later"],
    ["Convention note", "Project controls", "What the site does in practice, recorded as practice",
     "Observation", "Explaining a year of compliance"],
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
    ("the work has been done and is not going to be paid for without an argument.",
     SVG.format(h=210) + head("AUTHORITY WITHOUT PRIVITY")
     + box(230, 42, 180, 46, "Employer")
     + box(230, 106, 180, 46, "Managing contractor", "services agreement")
     + box(30, 168, 170, 40, "Civil package")
     + box(220, 168, 170, 40, "Mechanical package")
     + box(410, 168, 200, 40, "Electrical package")
     + '<line x1="320" y1="88" x2="320" y2="106" stroke="#a7f3d0" stroke-width="2"/>'
     + '<text x="320" y="163" text-anchor="middle" fill="#dc2626" font-size="11">instructs all three &#183; in contract with none</text>'
     + "</svg>",
     "Figure 1 &#8212; The most senior person on site can hold no contractual relationship with anybody taking his instruction. Nothing about the site shows it."),
    ("neither of them has read the other&#39;s contract.",
     SVG.format(h=190) + head("THE SAME FIRM, TWO STANDINGS")
     + box(30, 50, 265, 84, "Named in the contract", "instruction binds", "good")
     + box(345, 50, 265, 84, "Not named", "expert opinion, own risk", "bad")
     + '<text x="320" y="166" text-anchor="middle" fill="#64748b" font-size="11.5">Same person, same site, same meeting.</text>'
     + "</svg>",
     "Figure 2 &#8212; Whether an instruction binds is decided by a clause in a document the person taking it has usually never read."),
    ("and in the only sense that matters day to day, it has been.",
     SVG.format(h=200) + head("HOW THE CONVENTION FORMS")
     + box(16, 52, 146, 62, "Instruction given", "usually correct")
     + box(172, 52, 146, 62, "Complied with", "cheaper than arguing")
     + box(328, 52, 146, 62, "Repeated", "a hundred times")
     + box(484, 52, 134, 62, "The one that costs", "", "bad")
     + '<text x="320" y="152" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">A working convention is not a contractual position.</text>'
     + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">The difference only shows on the last box.</text>'
     + "</svg>",
     "Figure 3 &#8212; The convention is real and the site runs on it. It has simply never been tested, and by the time it is, everybody believes it is how things work."),
]


def table():
    h = "".join(f"<th {TH}>{c}</th>" for c in COLS)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in ROWS)
    return (f'<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">'
            f"<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")


SYSTEM = ('<h2>System design</h2>\n                            '
          '<p>None of this is a judgement about whether an instruction was valid. It is the set of '
          'records that lets somebody answer that question later by reading rather than '
          'remembering.</p>\n                            ' + table() + '\n                            '
          '<p>The last row is unusual and worth keeping. A year of compliance with an unnamed party '
          'is itself evidence of how the project was run, and it is the only thing that explains why '
          'nobody objected until the instruction that cost money.</p>')


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

    old_share = ("Both were EPC lump sum. One had a single contractor, the other had five. They are "
                 "not the same job and no clause tells you which you are on.")
    for enc in (quote(old_share, safe=""), quote(old_share, safe="").replace("%20", "+")):
        s = s.replace(enc, quote(SHARE, safe=""))
    s = s.replace(old_share, SHARE)

    s = s.replace("interfaces-week-2.html", "interfaces-week-3.html")
    s = s.replace('data-current-week="2"', 'data-current-week="3"')
    s = re.sub(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
               f'<span>Week 3<span class="crumb-title"> &#183; {CRUMB}</span>', s, 1)
    s = re.sub(r"MODULE 07 · INTERFACES · WEEK \d+", "MODULE 07 · INTERFACES · WEEK 3", s, 1)
    s = s.replace("Interfaces &#183; Week 2", "Interfaces &#183; Week 3")

    a = s.index('<h2 style="margin-top:0;">'); b2 = s.index("Enjoyed this")
    seg = s[a:b2]
    for pat, rep in [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
                     (r"\bcannot\b", "can't"), (r"\bwill not\b", "won't"),
                     (r"\bdid not\b", "didn't"), (r"\bis not\b", "isn't")]:
        seg = re.sub(pat, rep, seg)
    s = s[:a] + seg + s[b2:]

    if OUT.exists() and OUT.read_text(encoding="utf-8") == s:
        print("  = interfaces-week-3.html: degisiklik yok\n\n0 dosya")
        return
    OUT.write_text(s, encoding="utf-8")
    print("  + drafts/interfaces-week-3.html: yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
