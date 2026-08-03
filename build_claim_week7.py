#!/usr/bin/env python3
"""claim-week-7.html — Track 5, hafta 7. Sablon: claim-week-6.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-6.html", "claim-week-7.html"
PREV_TITLE = "A curve is not a record."
TITLE = "The as-built is a finding, not a record."
CRUMB = "The as-built programme"
DATE = "Apr 19, 2028"
DESC = ("There is no drawer with the as-built programme in it. You build one, and every date in it "
        "is a decision somebody made &#8212; which is why two analysts with the same records produce "
        "two different jobs. Claims &amp; Delay Analysis Week 7.")
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
<svg viewBox="0 0 640 262" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE ACTIVITY, FOUR DECISIONS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the records agree on all of it, and the bar can still be drawn four ways</text>
<text x="34" y="72" fill="#64748b" font-size="10">survey crew sets out</text>
<circle cx="60" cy="88" r="4" fill="#94a3b8"/>
<text x="150" y="72" fill="#64748b" font-size="10">first pile bored</text>
<circle cx="176" cy="88" r="4" fill="#059669"/>
<text x="286" y="72" fill="#64748b" font-size="10">rig off hire, 6 weeks</text>
<rect x="300" y="82" width="90" height="12" rx="3" fill="#cbd5e1"/>
<text x="422" y="72" fill="#64748b" font-size="10">last pile</text>
<circle cx="448" cy="88" r="4" fill="#059669"/>
<text x="512" y="72" fill="#64748b" font-size="10">records signed</text>
<circle cx="576" cy="88" r="4" fill="#94a3b8"/>
<line x1="40" y1="88" x2="600" y2="88" stroke="#e2e8f0" stroke-width="1"/>
<rect x="60" y="112" width="516" height="18" rx="4" fill="#94a3b8" opacity="0.30"/>
<text x="318" y="125" text-anchor="middle" fill="#475569" font-size="9.5">A &#183; set-out to sign-off &#8212; the longest bar anyone can defend</text>
<rect x="176" y="136" width="272" height="18" rx="4" fill="#059669" opacity="0.55"/>
<text x="312" y="149" text-anchor="middle" fill="#fff" font-size="9.5">B &#183; first pile to last pile, gap included</text>
<rect x="176" y="160" width="124" height="18" rx="4" fill="#059669" opacity="0.75"/>
<rect x="390" y="160" width="58" height="18" rx="4" fill="#059669" opacity="0.75"/>
<text x="470" y="173" fill="#475569" font-size="9.5">C &#183; two activities, the gap taken out</text>
<rect x="176" y="184" width="400" height="18" rx="4" fill="#94a3b8" opacity="0.45"/>
<text x="376" y="197" text-anchor="middle" fill="#475569" font-size="9.5">D &#183; first pile to sign-off</text>
<rect x="34" y="214" width="572" height="38" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="238" fill="#64748b" font-size="10.5">Four honest readings of one set of records, and a spread of weeks between the shortest and the longest.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Nobody is lying in any of these. The choice is made silently, usually by whoever is quickest with the mouse.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 248" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE DATES ARE FACTS. THE ARROWS ARE NOT.</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">two readings of the same as-built, and only one of them makes the rock critical</text>
<rect x="34" y="60" width="278" height="118" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">READING ONE</text>
<rect x="54" y="94" width="96" height="16" rx="3" fill="#059669" opacity="0.7"/>
<text x="102" y="106" text-anchor="middle" fill="#fff" font-size="9">Piling</text>
<rect x="158" y="94" width="88" height="16" rx="3" fill="#059669" opacity="0.7"/>
<text x="202" y="106" text-anchor="middle" fill="#fff" font-size="9">Caps</text>
<text x="154" y="107" fill="#059669" font-size="11">&#8594;</text>
<text x="54" y="132" fill="#475569" font-size="10">caps waited for piling</text>
<text x="54" y="150" fill="#475569" font-size="10">so the rock delayed completion</text>
<text x="54" y="168" fill="#059669" font-size="10" font-weight="600">the claim works</text>
<rect x="328" y="60" width="278" height="118" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">READING TWO</text>
<rect x="348" y="94" width="96" height="16" rx="3" fill="#94a3b8" opacity="0.5"/>
<text x="396" y="106" text-anchor="middle" fill="#475569" font-size="9">Piling</text>
<rect x="452" y="94" width="88" height="16" rx="3" fill="#94a3b8" opacity="0.5"/>
<text x="496" y="106" text-anchor="middle" fill="#475569" font-size="9">Caps</text>
<text x="348" y="132" fill="#64748b" font-size="10">caps waited for rebar delivery</text>
<text x="348" y="150" fill="#64748b" font-size="10">and would have started late anyway</text>
<text x="348" y="168" fill="#64748b" font-size="10" font-weight="600">the claim collapses</text>
<rect x="34" y="192" width="572" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="218" fill="#64748b" font-size="10.5">Every start and finish date above is identical in both. What differs is an inference nobody wrote down at the time.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">This is where the money is. Not in the dates &#8212; in the reasons behind them, which the records almost never hold.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 216" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FOUR FIELDS, ONCE A MONTH</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">three of them are standard practice; the fourth is the one that decides claims</text>
<rect x="34" y="60" width="572" height="34" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">ACTUAL START</tspan> &#8212; the date the activity genuinely began, on a stated definition</text>
<rect x="34" y="102" width="572" height="34" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="124" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">ACTUAL FINISH</tspan> &#8212; on the same definition, applied the same way every month</text>
<rect x="34" y="144" width="572" height="34" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="166" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">PROGRESS</tspan> &#8212; remaining duration, or percentage complete against a stated measure</text>
<rect x="34" y="186" width="572" height="26" rx="8" fill="#059669" opacity="0.16" stroke="#10b981"/>
<text x="54" y="204" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">WHAT IT WAS WAITING FOR</tspan> &#8212; one line, and almost nobody writes it</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The fourth field turns an inference into a record. It is a text box, and it costs nothing.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The as-built is a finding, not a record.</h2>

<p>There is no drawer with the as-built programme in it. Nobody hands you one at the end of the job. What exists is what Week 6 described &#8212; diaries, allocation sheets, delivery notes, registers &#8212; and somebody has to turn that pile into a programme.</p>

<p>The word for that is not <em>retrieving</em>. It is <em>constructing</em>, and the person doing the constructing makes several hundred decisions on the way.</p>

<p>Which is why two competent analysts, given identical records, produce two different as-builts. Not because one of them is dishonest. Because the records don't contain the answers to the questions building an as-built forces you to ask.</p>

<h2>What you need, and when you needed it</h2>

<p>The minimum is short. For every activity: an actual start, an actual finish, and a periodic statement of progress &#8212; remaining duration or percentage complete. Collected monthly, that is enough to reconstruct a defensible as-built.</p>

<p>Almost every job collects exactly this data, every month, and attaches it to the valuation. <a href="week-16.html">Schedule Week 16</a> is the whole cycle. The awkward finding is how rarely that data is then used for anything except the payment application, and how often it turns out, years later, to have been recorded on a different definition every month by a different person.</p>

<p>An as-built built during the job is a record. An as-built built afterwards is a reconstruction, and it is treated as one.</p>

<h2>Four decisions hiding in one bar</h2>

<p>Take the piling on this job and ask a simple question: when did it start and when did it finish?</p>

""" + FIG1 + """

<p>Did piling start when the survey crew set out the positions, when the rig arrived, or when the first pile was bored? Did it finish at the last pile, or when the records were signed off three weeks later? And what about the six weeks in the middle when the rig went off hire &#8212; is that one activity with a long duration, or two activities with a gap between them?</p>

<p>Every one of those readings is defensible. The spread between the shortest and the longest is weeks. And the decision is usually made silently, by whoever is building the file, applying whatever convention they happen to prefer.</p>

<p>The fix isn't to find the right answer, because there isn't one. It is to state the convention, apply it to every activity, and say so in writing. An as-built built on a declared rule is an argument. An as-built built on unstated instinct is a target.</p>

<h2>At what level do you build it?</h2>

<p>There's a second convention to settle before any of this works, and it's the one that quietly decides whether the as-built is usable at all.</p>

<p>An as-built built from site records naturally wants to be detailed, because that's how the records are: pile by pile, day by day, location by location. The baseline it will be compared against is usually much coarser &#8212; one bar for piling, one for pile caps.</p>

<p>If the two don't line up, they can't be compared, and every method in the next phase depends on comparing them. So the as-built has to be built at the baseline's level of detail, with the finer record held underneath it as support rather than as the programme itself.</p>

<p>That has an uncomfortable consequence worth stating plainly: the coarseness of the baseline limits the precision of everything downstream. If the original programme had a single ninety-day bar for piling, no amount of daily record will let you demonstrate what happened inside it in a way that a comparison can use. You'll have the evidence and no structure to hang it on.</p>

<p>It's another reason the baseline decides more than it should, and another reason to look at it in month two rather than in year three.</p>

<h2>The dates are facts. The arrows are not.</h2>

<p>Now the real difficulty, and it is bigger than the last one.</p>

<p>Your records tell you <em>when</em> things happened. They almost never tell you <em>why</em> one thing followed another. And an as-built programme, if it is going to produce a critical path, needs logic &#8212; which means somebody has to decide, after the fact, what was waiting for what.</p>

""" + FIG2 + """

<p>That decision is not evidence. It is an inference drawn from the same records, and it is exactly where a claim is won or lost. Both readings in the figure have identical dates. One of them makes the rock critical and the other makes it irrelevant, and nothing in the diaries settles which one is right.</p>

<p>This is also why the as-built critical path is a derived object rather than an observed one. You get to it by mapping float and identifying which activities were driving in each period &#8212; and every one of those determinations rests on logic that somebody reconstructed.</p>

<h2>Two analysts, one job</h2>

<p>Put those two problems together and the disagreement stops being surprising.</p>

<p>Analyst A treats piling as starting at first bore, splits it around the off-hire gap, and reads the caps as waiting on piling. Analyst B treats it as one continuous activity from set-out, and reads the caps as waiting on rebar delivery. Same diaries. Same timesheets. Same job. Two as-builts that differ by weeks on the critical path, and therefore two very different numbers.</p>

<p>Neither of them has done anything improper. They answered unanswered questions differently, which is what you do when the record is silent and the work still has to be done.</p>

<h2>Simple, and difficult to answer</h2>

<p>One observation from the literature is worth carrying, because it cuts against the instinct to reach for the most sophisticated technique available.</p>

<p>An elaborate analysis carries no more credibility than a carefully prepared as-built built on the project records and ordinary common sense. What it does carry is weight of a different kind: it lands on the other side as something close to an ambush, and answering it properly becomes an enormous job in itself.</p>

<p>That is worth knowing from both sides of the table. If you are receiving one, the volume is not the argument. If you are sending one, a well-built as-built and a clear narrative will often do more than a technique nobody in the room can check.</p>

<h2>The field nobody fills in</h2>

""" + FIG3 + """

<p>Three of those four fields are already in your monthly cycle. The fourth &#8212; a single line saying what an activity was waiting for &#8212; is the one that converts the whole of the previous section from inference into record.</p>

<p>It's a text box. It takes a planner a few minutes a month. And it is the difference between an as-built logic you have to argue for and one you can point at.</p>

<h2>Practical insight</h2>

<p>Take one month of your current job and build the as-built for it. One month, not the whole project.</p>

<p>Write down the convention first: what counts as started, what counts as finished, and how you will treat gaps. Then apply it and see how far the records carry you before you have to guess.</p>

<p>The guesses are the output. Every place where you had to decide something the records don't say is a place where somebody else will decide it differently &#8212; and while the job is running, most of those gaps can still be closed by asking somebody who was there and writing the answer down.</p>

<p>Do this in month six and it takes a day. Do it in year three, for thirty months at once, with the site team dispersed, and it becomes the reason your claim is negotiated rather than agreed.</p>

<h2>Key takeaways</h2>

<p>&#10004; No as-built programme exists to be fetched; it's constructed, and every date in it is a decision.</p>

<p>&#10004; The minimum monthly data is small &#8212; actual start, actual finish, progress &#8212; and most jobs already collect it for the valuation.</p>

<p>&#10004; Start and finish definitions must be declared and applied consistently, because four defensible readings of one activity can differ by weeks.</p>

<p>&#10004; Records give dates but almost never give logic, so as-built logic is an inference rather than evidence.</p>

<p>&#10004; Build the as-built at the baseline's level of detail, because a coarse baseline caps the precision of every comparison that follows.</p>

<p>&#10004; The as-built critical path is derived from that inferred logic, so it inherits every assumption made along the way.</p>

<p>&#10004; A sophisticated technique is no more credible than a careful as-built; its real effect is the burden it puts on the party answering it.</p>

<p>&#10004; One extra field each month &#8212; what the activity was waiting for &#8212; turns the most contested part of the analysis into a contemporaneous record.</p>

<h2>What&#39;s coming next</h2>

<p>The plan and the outturn are now both on the table. What sits between them is the thing the contract actually asked for every month, and the thing most teams treat as an administrative chore: the programme update. Next week is what those updates are worth as evidence, why the gaps between them matter more than the updates themselves, and what happens to an analysis when four of them are missing.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 8 &#183; Programme updates &#183; coming soon</span>
                                    <h4>The evidence nobody thought to keep</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>A Curve Is Not A Record &#8212; The Project Control Hub</title>",
                  "<title>The As-Built Is A Finding, Not A Record &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="A Curve Is Not A Record | The Project Control Hub"',
                  'content="The As-Built Is A Finding, Not A Record | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-6.html", "claim-week-7.html")
    s = s.replace('<span>Week 6<span class="crumb-title"> &#183; The site record</span></span>',
                  '<span>Week 7<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 6",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 7", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Apr 12, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Apr 12, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="7"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week7.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 6", "claim-week-6.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-7.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 7 &#183; The as-built programme &#183; coming soon</span>\n'
            '                                    <h4>The as-built is a finding, not a record</h4>',
            '<span class="next-week-tag">Week 7 &#183; The as-built programme</span>\n'
            '                                    <h4>The as-built is a finding, not a record.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-7.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 7" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 7, title: "The as-built programme — reconstructing what actually happened",\n'
           '          short: "The as-built programme", status: "upcoming" },')
    new = ('        { n: 7, title: "The as-built programme — reconstructing what actually happened",\n'
           '          short: "The as-built programme", status: "live", page: "claim-week-7.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 7 live (%s)" % DATE)
    elif 'page: "claim-week-7.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 7 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-7.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-7.html</loc>\n"
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
