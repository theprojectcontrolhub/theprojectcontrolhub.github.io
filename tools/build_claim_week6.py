#!/usr/bin/env python3
"""claim-week-6.html — Track 5, hafta 6. Sablon: claim-week-5.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-5.html", "claim-week-6.html"
PREV_TITLE = "The baseline is an intention, not a record."
TITLE = "A curve is not a record."
CRUMB = "The site record"
DATE = "Apr 12, 2028"
DESC = ("Progress curves and production reports are outputs, not evidence. What a claim runs on is "
        "the daily report, the allocation sheet and the diary &#8212; and what happens to your "
        "number when those are missing. Claims &amp; Delay Analysis Week 6.")
DESC_PLAIN = DESC.replace("&amp;", "&")
CHANGED = []


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    if os.path.exists(p) and re.sub(r"\?v=\d+", "?v=N", read(p)) == re.sub(r"\?v=\d+", "?v=N", s):
        return
    io.open(p, "w", encoding="utf-8").write(s)
    CHANGED.append(p)


FIG1 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THREE KINDS OF DOCUMENT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">only one of them is evidence, and it is the one nobody circulates</text>
<rect x="34" y="62" width="572" height="46" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">PRIMARY &#8212; written by somebody who was there, on the day</text>
<text x="54" y="99" fill="#475569" font-size="10.5">daily reports, allocation sheets, diaries, delivery notes, the RFI register</text>
<rect x="34" y="118" width="572" height="46" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="138" fill="#64748b" font-size="10.5" font-weight="700">DERIVED &#8212; calculated from the primary record by somebody else</text>
<text x="54" y="155" fill="#64748b" font-size="10.5">progress curves, percentage complete, production reports, the monthly report</text>
<rect x="34" y="174" width="572" height="46" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1" stroke-dasharray="4 3"/>
<text x="54" y="194" fill="#64748b" font-size="10.5" font-weight="700">RECONSTRUCTED &#8212; assembled afterwards by somebody who knows the answer</text>
<text x="54" y="211" fill="#64748b" font-size="10.5">the as-built built from memory, the narrative written for the claim</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Each step down costs you something. Nobody notices which step they are standing on until it is challenged.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 286" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT EACH ONE CAN ACTUALLY PROVE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the question it answers &#8212; and, just as usefully, the one it does not</text>
<line x1="252" y1="54" x2="252" y2="272" stroke="#e2e8f0"/>
<text x="34" y="76" fill="#64748b" font-size="10.5" font-weight="700">Allocation sheet</text>
<text x="266" y="76" fill="#475569" font-size="10.5">hours, by trade, against an activity &#8212; the only</text>
<text x="266" y="92" fill="#475569" font-size="10.5">record a productivity comparison can run on</text>
<text x="34" y="118" fill="#64748b" font-size="10.5" font-weight="700">Daily report</text>
<text x="266" y="118" fill="#475569" font-size="10.5">who was on site, where they worked, what</text>
<text x="266" y="134" fill="#475569" font-size="10.5">stopped &#8212; the backbone of an as-built</text>
<text x="34" y="160" fill="#64748b" font-size="10.5" font-weight="700">Site diary</text>
<text x="266" y="160" fill="#475569" font-size="10.5">the reason given at the time, before anybody</text>
<text x="266" y="176" fill="#475569" font-size="10.5">knew which reason would be worth money</text>
<text x="34" y="202" fill="#64748b" font-size="10.5" font-weight="700">RFI and submittal logs</text>
<text x="266" y="202" fill="#475569" font-size="10.5">dates in and dates out &#8212; delay inside</text>
<text x="266" y="218" fill="#475569" font-size="10.5">somebody else&#39;s process, with no argument</text>
<text x="34" y="244" fill="#64748b" font-size="10.5" font-weight="700">Photographs</text>
<text x="266" y="244" fill="#475569" font-size="10.5">the state of one place on one date; not why,</text>
<text x="266" y="260" fill="#475569" font-size="10.5">not for how long, and not who was standing idle</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Photographs are the most collected and the least probative. Allocation sheets are the reverse.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT MISSING RECORDS COST YOU</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">you do not lose the claim &#8212; you drop a rung, and every rung is worth less</text>
<rect x="34" y="60" width="572" height="40" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">YOUR OWN JOB, MEASURED</text>
<text x="54" y="94" fill="#475569" font-size="10.5">a clean stretch of your own work compared against a disrupted one &#8212; hardest to attack</text>
<rect x="34" y="110" width="572" height="40" rx="8" fill="#059669" opacity="0.05" stroke="#a7f3d0"/>
<text x="54" y="128" fill="#059669" font-size="10.5" font-weight="700">YOUR OWN JOB, ESTIMATED</text>
<text x="54" y="144" fill="#475569" font-size="10.5">the tender allowance against the outturn &#8212; now you are defending your own estimate</text>
<rect x="34" y="160" width="572" height="40" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="178" fill="#64748b" font-size="10.5" font-weight="700">SOMEBODY ELSE&#39;S JOBS, PUBLISHED</text>
<text x="54" y="194" fill="#64748b" font-size="10.5">industry studies &#8212; widely used, widely misapplied, and about a project that is not yours</text>
<text x="320" y="222" text-anchor="middle" fill="#94a3b8" font-size="10.5">Which rung you land on was decided by a form somebody filled in, or didn&#39;t, two years earlier.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The ladder only goes down. There is no way to climb back up once the month has passed.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">A curve is not a record.</h2>

<p>Open almost any claim and somewhere near the front there is an S-curve, planned against actual, with a widening gap shaded in. It looks like proof. It is one of the least useful documents in the bundle.</p>

<p>A progress curve is not something that was observed. It is something that was calculated, from percentages that somebody assessed, using a measure of completion that somebody chose. Every one of those steps is a judgement, and every one of them was made by your side. Challenge any of them and the curve moves.</p>

<p>Week 5 said the baseline is an intention rather than a record. This week is the other half of that: most of what a project circulates as evidence is not evidence either.</p>

<h2>Three kinds of document</h2>

""" + FIG1 + """

<p>The distinction that matters is not formal against informal, or contractual against internal. It is whether a document reports something a person witnessed, or computes something from documents that did.</p>

<p>A delivery note is primary. It was written at a gate, by somebody watching a lorry. A production report that says the piling gang achieved eighty-two per cent of planned output in March is derived; behind it sit the allocation sheets, and if those don't exist, behind it sits nothing at all.</p>

<p>This is why the most polished documents on a job are frequently the weakest in an argument. Polish is a sign of processing, and processing is distance from the event.</p>

<h2>What each one can prove</h2>

<p>The useful way to hold this is not a list of record types. It is a mapping: for each document, the question it can answer, and the question people expect it to answer but it cannot.</p>

""" + FIG2 + """

<p>Photographs are the clearest case of the mismatch. Every job takes thousands, and they are the first thing offered when somebody asks for evidence. A photograph proves the state of one location on one date. It cannot show you why work stopped, how long it stopped for, whether anybody was standing idle, or what they were told that morning. It is corroboration for a story told by another document, and on its own it is nearly silent.</p>

<p>The RFI and submittal registers sit at the opposite end and get far less attention than they deserve. They record a date in and a date out. There is no interpretation in them and nothing to argue about, which makes them unusually hard to attack &#8212; and they measure something specific and valuable: how long a question sat inside somebody else's process.</p>

<h2>Two record sets, and most jobs only keep one</h2>

<p><a href="contract-week-8.html">Contract Week 8</a> already argued that entitlement is built long before anybody decides to claim, and it was talking about records. So it is worth being precise about why this week is not that week again.</p>

<p>The entitlement record set is about notices, instructions, correspondence and minutes. It answers the question <em>did we keep the right</em>, and it is largely made of documents that were exchanged with the other side.</p>

<p>The quantum record set is about hours, quantities, locations and dates. It answers the question <em>what did it cost us</em>, and it is almost entirely internal &#8212; which is exactly why it is the one that gets thin. Nobody chases you for your allocation sheets. The Engineer never asks to see them, no clause requires them, and their absence produces no consequence at all until the moment they are the only thing that would have worked.</p>

<p>Most jobs keep the first set reasonably and the second set badly, and the two failures look nothing alike. A weak entitlement record loses the argument loudly, at a deadline, in a way somebody notices. A weak quantum record loses it quietly, two years later, in a negotiation where your number simply carries less weight than theirs and nobody can say precisely why.</p>

<h2>The one that carries the most and is kept the worst</h2>

<p>Labour is usually the largest variable cost a contractor carries, and it is the most common source of damages. Which makes the allocation sheet &#8212; hours booked by trade against a location or an activity &#8212; the single most valuable record on the site.</p>

<p>It is also the one most often kept badly, because it is kept for payroll rather than for evidence. Hours booked against a job number are enough to pay people. Hours booked against <em>which activity, in which location</em> are what a productivity argument needs, and the difference between the two is about ten seconds a day for a foreman.</p>

<p>That ten seconds decides, years later, whether a disruption claim can be proved from your own job or has to be argued from somebody else's.</p>

<h2>What missing records actually cost</h2>

<p>This is the part worth being concrete about, because the consequence of a poor record is not that the claim is refused. It is that the claim gets weaker in a specific, predictable way.</p>

""" + FIG3 + """

<p>With good allocation records you can compare a clean period of your own work against a disrupted one. It is the strongest available argument because both halves come from the same site, the same crews and the same job.</p>

<p>Without them you fall back to comparing outturn against your tender allowance, which quietly changes the subject: the argument is now about whether your estimate was any good, and the other side will happily spend the rest of the meeting there.</p>

<p>Below that sit the published industry studies. They are widely used and, as the literature is candid about, widely misused &#8212; because they describe projects that are not yours. That rung is where a great many disruption claims end up, and it is the rung reserved for people whose foremen filled the form in badly.</p>

<h2>The record is not made for the claim</h2>

<p>The last thing worth saying is the one that makes all of this hard to act on.</p>

<p>Records written with a claim in mind read like it. A diary entry that carefully attributes fault, in a well-constructed sentence, on a day when nobody yet knew there would be a dispute, is a document a reviewer will look at twice. The value of a contemporaneous record comes precisely from the fact that the person writing it had no idea what would eventually matter.</p>

<p>So the instruction cannot be write better records for the claim. It has to be record what happened, in a form that survives, every day, whether or not anything is going wrong. The month in which nothing goes wrong is the month that produces your comparison period.</p>

<h2>Practical insight</h2>

<p>Pull last month's records for one activity on your job &#8212; one only, and pick the one with the most people on it.</p>

<p>Then ask what you could prove with them. How many hours went into that activity, in that location, on each day? Which days did nobody work, and does anything say why? If work was interrupted, is the reason written down anywhere by a person who was there, or does the trail run out at a monthly report written by somebody in the office?</p>

<p>Most teams doing this for the first time find the same thing: the narrative exists, the hours exist, and they cannot be joined. There are diaries saying the rig stood idle and timesheets saying forty-eight hours were booked to piling, and no document connects the two.</p>

<p>Fixing that is a change to one form and one habit. It costs almost nothing this month, and there is no month later in which it can be done instead.</p>

<h2>Key takeaways</h2>

<p>&#10004; A progress curve is calculated from judgements your own side made; it is an output, not evidence.</p>

<p>&#10004; Documents divide into primary, derived and reconstructed, and each step away from the event costs you argument.</p>

<p>&#10004; Photographs are the most collected and least probative record; they corroborate a story, they do not tell one.</p>

<p>&#10004; RFI and submittal registers are unusually strong because they contain dates and no interpretation.</p>

<p>&#10004; The allocation sheet is the most valuable record on site and the most often kept for payroll rather than for proof.</p>

<p>&#10004; Entitlement records are exchanged and get chased; quantum records are internal and nobody asks for them until it is too late.</p>

<p>&#10004; Poor records don't refuse a claim; they drop it a rung, from your own measured work to your estimate to somebody else's published studies.</p>

<p>&#10004; The strength of a contemporaneous record comes from the writer not knowing what would matter, so records written for a claim are worth less than records written for the day.</p>

<h2>What&#39;s coming next</h2>

<p>With the plan on one side and the daily record on the other, the next job is to turn the second into something that can be compared with the first. Next week is the as-built programme: how it is built, why two people building one from the same records produce different answers, and why it is a finding rather than a document you can go and fetch.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 7 &#183; The as-built programme &#183; coming soon</span>
                                    <h4>The as-built is a finding, not a record</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Baseline Is An Intention, Not A Record &#8212; The Project Control Hub</title>",
                  "<title>A Curve Is Not A Record &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Baseline Is An Intention, Not A Record | The Project Control Hub"',
                  'content="A Curve Is Not A Record | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-5.html", "claim-week-6.html")
    s = s.replace('<span>Week 5<span class="crumb-title"> &#183; The as-planned programme</span></span>',
                  '<span>Week 6<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 5",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 6", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Apr 5, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Apr 5, 2028", "PMP&reg; &#183; " + DATE)

    i = s.index('<div class="content-preview"')
    i = s.index(">", i) + 1
    j = s.rindex("</div>", i, s.index("<!-- PAYWALL CTA -->"))
    n = words(BODY)
    mins = max(1, round(n / 225 + 3 * 0.25))
    s = s[:i] + "\n" + BODY + "\n" + s[j:]
    s = re.sub(r"<i class='bx bx-time-five'></i> \d+ min read",
               "<i class='bx bx-time-five'></i> %d min read" % mins, s, count=1)
    # MEVCUT KARTI KORU: bu sayfa daha once yayinlandiysa next-article karti bir
    # sonraki haftanin script'i tarafindan ileri baglanmis olabilir. Sablondan gelen
    # "coming soon" kartini basmak zinciri koparir (2026-07-27'de oldu).
    card = NEXT_CARD
    if os.path.exists(DST):
        m = re.search(r'<div class="next-article" id="nextArticle".*?\n                        </div>',
                      read(DST), re.S)
        if m and 'href="learn.html"' not in m.group(0):
            card = m.group(0)
    s = re.sub(r'<div class="next-article" id="nextArticle".*?\n                        </div>\n',
               card + "\n", s, count=1, flags=re.S)
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="6"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week6.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 5", "claim-week-5.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-6.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 6 &#183; The site record &#183; coming soon</span>\n'
            '                                    <h4>A curve is not a record</h4>',
            '<span class="next-week-tag">Week 6 &#183; The site record</span>\n'
            '                                    <h4>A curve is not a record.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-6.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 6" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 6, title: "The site record — daily reports, allocation sheets and what each one proves",\n'
           '          short: "The site record", status: "upcoming" },')
    new = ('        { n: 6, title: "The site record — daily reports, allocation sheets and what each one proves",\n'
           '          short: "The site record", status: "live", page: "claim-week-6.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 6 live (%s)" % DATE)
    elif 'page: "claim-week-6.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 6 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-6.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-6.html</loc>\n"
            "    <lastmod>2026-07-27</lastmod>\n  </url>\n</urlset>", 1))
        print("  sitemap.xml            eklendi")

    if CHANGED:
        v = int(re.search(r"curriculum\.js\?v=(\d+)", read("index.html")).group(1))
        c = 0
        for f in sorted(os.listdir(".")):
            if f.endswith(".html"):
                a = read(f)
                b = a.replace("curriculum.js?v=%d" % v, "curriculum.js?v=%d" % (v + 1))
                if a != b:
                    io.open(f, "w", encoding="utf-8").write(b)
                    CHANGED.append(f)
                    c += 1
        print("  cache                  v%d -> v%d (%d sayfa)" % (v, v + 1, c))
    else:
        print("  cache                  degisiklik yok")
    print("  tamam, %d dosya\n" % len(set(CHANGED)))


if __name__ == "__main__":
    main()
