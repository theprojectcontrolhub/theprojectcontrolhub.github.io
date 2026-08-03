#!/usr/bin/env python3
"""claim-week-28.html — Track 5, hafta 28. Finale. Sablon: claim-week-27.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-27.html", "claim-week-28.html"
PREV_TITLE = "Now sit across the table."
TITLE = "Net margin was $48,163."
CRUMB = "What five tracks were for"
DATE = "Sep 13, 2028"
WEEK_N = 28
DESC = ("The rock is worth $48,450. The job was built to earn $48,163. Two hundred and eighty-seven "
        "dollars apart, and five tracks have circled the gap. What all of it was actually for. "
        "Claims &amp; Delay Analysis Week 28.")
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
<svg viewBox="0 0 640 268" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE ROCK, FIVE QUESTIONS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same event, asked five different things by five different disciplines</text>
<rect x="34" y="60" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="83" fill="#64748b" font-size="10.5"><tspan font-weight="700">SCHEDULE</tspan> &#8212; does this move the completion date, and was piling driving at the time?</text>
<rect x="34" y="102" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="125" fill="#64748b" font-size="10.5"><tspan font-weight="700">COST</tspan> &#8212; seventeen piles at $2,850, and where does that sit against the budget?</text>
<rect x="34" y="144" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="167" fill="#64748b" font-size="10.5"><tspan font-weight="700">RISK</tspan> &#8212; a register entry, conditional, with nothing evidencing the northern half</text>
<rect x="34" y="186" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="209" fill="#64748b" font-size="10.5"><tspan font-weight="700">CONTRACT</tspan> &#8212; is there still a right, and was it kept alive in time?</text>
<rect x="34" y="228" width="572" height="36" rx="8" fill="#059669" opacity="0.12" stroke="#10b981"/>
<text x="54" y="251" fill="#059669" font-size="10.5"><tspan font-weight="700">CLAIMS</tspan> &#8212; what is that right actually worth, and can you prove the number?</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Five tracks, one boulder. Nobody ever needed to change the example, which was rather the point.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT THE ROCK IS WORTH, AND WHAT IS AT STAKE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the whole track, expressed as four lines</text>
<rect x="34" y="60" width="572" height="28" rx="6" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="79" fill="#475569" font-size="10.5">the work itself &#8212; 17 piles at $2,850, conditional</text>
<text x="560" y="79" text-anchor="end" fill="#059669" font-size="10.5" font-weight="700">$48,450</text>
<rect x="34" y="94" width="572" height="28" rx="6" fill="#059669" opacity="0.08" stroke="#a7f3d0"/>
<text x="54" y="113" fill="#475569" font-size="10.5">prolongation &#8212; thirty clean days at the average rate</text>
<text x="560" y="113" text-anchor="end" fill="#059669" font-size="10.5" font-weight="700">$6,997</text>
<rect x="34" y="128" width="572" height="28" rx="6" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="147" fill="#64748b" font-size="10.5">eleven concurrent days &#8212; time, probably not money</text>
<text x="560" y="147" text-anchor="end" fill="#64748b" font-size="10.5">$2,566</text>
<line x1="34" y1="166" x2="606" y2="166" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#0f172a" font-size="10.5" font-weight="700">recovered in full, as Cost, with no profit on any of it</text>
<text x="560" y="188" text-anchor="end" fill="#0f172a" font-size="11.5" font-weight="700">$55,447</text>
<rect x="34" y="202" width="572" height="40" rx="8" fill="#b91c1c" opacity="0.08" stroke="#fca5a5"/>
<text x="54" y="221" fill="#b91c1c" font-size="10.5" font-weight="700">recovered in full &#8594; margin stands at $48,163</text>
<text x="54" y="237" fill="#b91c1c" font-size="10.5">recovered not at all &#8594; the job loses $7,284 and the year was spent for nothing</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Winning everything leaves you exactly where you started. That asymmetry is the whole commercial reality of a claim.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 296" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TEN THINGS, NONE OF WHICH TAKE AN HOUR</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">each one replaces months of the work this track just described</text>
<line x1="290" y1="54" x2="290" y2="286" stroke="#e2e8f0"/>
<text x="34" y="76" fill="#64748b" font-size="10">serve the notice</text>
<text x="304" y="76" fill="#475569" font-size="10">the cheapest act in construction</text>
<text x="34" y="100" fill="#64748b" font-size="10">check the baseline in month two</text>
<text x="304" y="100" fill="#475569" font-size="10">before it becomes evidence</text>
<text x="34" y="124" fill="#64748b" font-size="10">add a column to the allocation sheet</text>
<text x="304" y="124" fill="#475569" font-size="10">activity and location, not job number</text>
<text x="34" y="148" fill="#64748b" font-size="10">one line per activity each month</text>
<text x="304" y="148" fill="#475569" font-size="10">what was it waiting for</text>
<text x="34" y="172" fill="#64748b" font-size="10">keep the native file of every update</text>
<text x="304" y="172" fill="#475569" font-size="10">a folder nobody tidies</text>
<text x="34" y="196" fill="#64748b" font-size="10">fill in the concurrency provision</text>
<text x="304" y="196" fill="#475569" font-size="10">the most expensive blank in the book</text>
<text x="34" y="220" fill="#64748b" font-size="10">send the pacing letter</text>
<text x="304" y="220" fill="#475569" font-size="10">while you are actually pacing</text>
<text x="34" y="244" fill="#64748b" font-size="10">agree how acceleration gets paid</text>
<text x="304" y="244" fill="#475569" font-size="10">before spending, without conceding fault</text>
<text x="34" y="268" fill="#64748b" font-size="10">reserve the cumulative effect</text>
<text x="304" y="268" fill="#475569" font-size="10">on every variation you settle</text>
<text x="34" y="288" fill="#64748b" font-size="10">code cost by location</text>
<text x="304" y="288" fill="#475569" font-size="10">the measured mile builds itself</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Not one of these is difficult. All ten together are worth more than every technique in this track.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Net margin was $48,163.</h2>

<p>The rock is worth $48,450. The job was built to earn $48,163. Two hundred and eighty-seven dollars apart, and the entire site has been circling that coincidence for five tracks.</p>

<p>It's time to put both numbers in the same sentence and see what falls out.</p>

<h2>One boulder, five questions</h2>

""" + FIG1 + """

<p>Nobody ever had to change the example, and that was deliberate. The same event, put to five different disciplines, produces five entirely different questions and not one of them is redundant.</p>

<p>Schedule asked whether it moved the completion date. Cost priced it and put it against a budget. Risk wrote it down before it happened, conditionally, and recorded honestly that nothing evidenced what the northern half of the site contained. Contract asked whether the right survived. And this track asked what the right was worth and whether the number could be proved.</p>

<p>Take away any one and the others stop working. Price it without knowing whether piling was driving and you have a number attached to nothing. Preserve the right without records and you have an entitlement you cannot quantify. That interdependence is the argument the whole site has been making.</p>

<h2>The number, finally</h2>

""" + FIG2 + """

<p>Assemble what twenty-eight weeks produced and it comes to $55,447: the work itself, plus thirty days of prolongation at the average rate, with eleven concurrent days that probably bring time and not money.</p>

<p>Now look at what that means, because it isn't what people expect.</p>

<p>Recover all of it and the margin stands at $48,163 &#8212; exactly what the job was priced to make. You spent a year, ran a dispute and paid for an analysis to arrive back where you started, because <a href="claim-week-3.html">Week 3</a> established that the clause pays Cost and Cost does not include profit.</p>

<p>Recover none of it and the job loses $7,284. Not makes less. Loses.</p>

<p>That asymmetry is the commercial reality nobody puts on a slide. The upside of a perfectly run claim is that the year was not wasted. The downside is real money out of the business. Anybody who thinks of claims as an income stream has the shape of it backwards.</p>

<h2>The number was always conditional</h2>

<p>One honest note before the summing up, because leaving it out would make the arithmetic look tidier than it is.</p>

<p>The $48,450 was never a fact. <a href="risk-week-5.html">Risk Week 5</a> priced seventeen piles because the southern ratio suggested seventeen, and wrote down in the same entry that nothing evidenced what the northern half of the site contained. It could be eleven. It could be twenty-four. The register said so at the time, in writing, before anybody had an interest in the answer.</p>

<p>Everything since has been built on that figure, and the figure has carried a caveat the whole way. That's not a flaw in the example. It's the most realistic thing about it, because every claim any of us will ever handle rests on numbers with exactly that character &#8212; assessed in good faith, from incomplete information, by somebody who wrote down what they didn't know.</p>

<p>Which makes the register entry the most valuable document in five tracks. Not because it was right. Because it recorded the limits of its own confidence, and two years later that honesty is worth more than a confident number nobody can defend.</p>

<h2>The claim that never happened</h2>

<p>Which leads to the thing this track has been building towards without saying it.</p>

<p>Every week contained something that, done at the time, would have made the recovery straightforward or unnecessary. Not a technique &#8212; an act, usually taking minutes.</p>

""" + FIG3 + """

<p>Look at that list against what it replaces. The notice replaces the entire question of whether you have a right at all. One column on the allocation sheet replaces the ladder of ever-weaker productivity methods. A line in each monthly update replaces the inference at the heart of as-built logic. Filling in the concurrency provision replaces a body of case law that two jurisdictions cannot agree on.</p>

<p>None of it is difficult. All of it happens while everybody is busy with something that feels more urgent, which is why almost none of it gets done.</p>

<p>The honest summary of this track is that it teaches you to recover value after the fact, and that recovering value after the fact is always the second-best outcome. The best outcome is a job where the argument is small because the records made it small.</p>

<h2>What this was actually for</h2>

<p>There is a version of this subject that treats claims as a specialism you call somebody in for. That version isn't wrong, and it isn't what the last twenty-eight weeks were about.</p>

<p>The person who decides whether a claim can be made is not the consultant. It is the planner choosing a level of detail in month one, the quantity surveyor setting up the cost codes, the engineer filling in a diary at six o'clock, and the contracts manager deciding whether a letter is worth writing. None of them thinks they're working on a claim. All of them are.</p>

<p>Which is the reason this track sits at the end of five and not on its own. You cannot make these decisions well without knowing what they are for, and knowing what they are for means knowing how the argument ends.</p>

<p>You now know how it ends.</p>

<h2>What actually changed</h2>

<p>Twenty-eight weeks ago the question was how much. That question turned out to contain about ten others, and the useful thing isn't the answer to any of them.</p>

<p>It's that you can now read a delay report and know within twenty minutes what it is, what it assumes and where it is soft. You can look at a monthly update and see the evidence it will become. You can sit in a meeting where somebody says <em>we'll sort the paperwork later</em> and know precisely what is being given away, in dollars, on this job.</p>

<p>None of that is a technique. It's a way of seeing the ordinary week differently &#8212; and it's the only part of this that survives contact with a job that looks nothing like the one in the example.</p>

<h2>Practical insight</h2>

<p>One thing, on Monday, on the job you are actually running.</p>

<p>Pick the single item from that list of ten that your project does worst, and fix that one. Not all ten &#8212; one. The column on the allocation sheet, or the folder of native files, or the line in the update saying what each activity was waiting for.</p>

<p>Then tell somebody why. The reason these things do not get done is almost never that they are hard; it's that nobody on site has ever been shown what they're for. A foreman who understands that the second column decides whether a productivity claim is provable fills it in. A foreman who thinks it is administration does not.</p>

<p>And write down today's date next to it. In two years, when somebody asks when the records improved, the answer will be a date you chose rather than the date a dispute started.</p>

<h2>Key takeaways</h2>

<p>&#10004; The rock and the margin sit $287 apart, which is why one event has carried five tracks.</p>

<p>&#10004; Five disciplines ask five different questions of the same event, and removing any one breaks the others.</p>

<p>&#10004; A fully successful claim on this job recovers $55,447 and leaves the margin exactly where it was priced.</p>

<p>&#10004; A failed one turns a $48,163 margin into a $7,284 loss; claims are downside protection, not income.</p>

<p>&#10004; Every week of this track contained a contemporaneous act that would have made its own subject easier or unnecessary.</p>

<p>&#10004; None of those ten acts is difficult; all of them compete with something that feels more urgent on the day.</p>

<p>&#10004; The people who decide whether a claim is provable are the people who never think they are working on one.</p>

<h2>What&#39;s coming next</h2>

<p>Five tracks have taught one job: a single contract, a single chain of command, a single team on a single site. Every technique in all of them quietly assumes that shape. What happens when it stops holding &#8212; when the scope sits with somebody else, when the critical path runs through a purchase order, when the work nobody planned appears where two programmes meet, and when the number has more than one owner &#8212; is what remains.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Module 05 complete</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Track 6 &#183; The Assumptions That Stop Holding &#183; on the roadmap</span>
                                    <h4>When one contract stops being the shape of the job</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Now Sit Across The Table &#8212; The Project Control Hub</title>",
                  "<title>Net Margin Was $48,163 &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Now Sit Across The Table | The Project Control Hub"',
                  'content="Net Margin Was $48,163 | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-27.html", "claim-week-28.html")
    s = s.replace('<span>Week 27<span class="crumb-title"> &#183; Defending a claim</span></span>',
                  '<span>Week 28<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 27",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 28", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Sep 6, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Sep 6, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="%d"' % WEEK_N, s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week28.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 27", "claim-week-27.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    body_only = page[page.index('<div class="content-preview"'):page.index("<!-- PAYWALL CTA -->")]
    qual = r"(?:Schedule|Cost\s*&(?:amp;)?\s*Cash|Risk|Contract|Claims)\s+"
    fwd = sorted({m.group(2) for m in re.finditer(r"(%s)?Week (\d+)" % qual, body_only)
                  if not m.group(1) and int(m.group(2)) > WEEK_N})
    if fwd:
        sys.exit("HATA: govdede numarali ileri atif: Week %s" % ", ".join(fwd))
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-28.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 28 &#183; What five tracks were for &#183; coming soon</span>\n'
            '                                    <h4>Net margin was $48,163</h4>',
            '<span class="next-week-tag">Week 28 &#183; What five tracks were for</span>\n'
            '                                    <h4>Net margin was $48,163.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-28.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 28" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 28, title: "What five tracks were for — the claim that never happened",\n'
           '          short: "What five tracks were for", status: "upcoming" }')
    new = ('        { n: 28, title: "What five tracks were for — the claim that never happened",\n'
           '          short: "What five tracks were for", status: "live", page: "claim-week-28.html",\n'
           '          date: "%s" }' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 28 live (%s)" % DATE)
    elif 'page: "claim-week-28.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 28 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-28.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-28.html</loc>\n"
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
