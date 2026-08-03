#!/usr/bin/env python3
"""claim-week-13.html — Track 5, hafta 13. Sablon: claim-week-12.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-12.html", "claim-week-13.html"
PREV_TITLE = "Forty-one days, cut into windows."
TITLE = "Two bars, and what they leave out."
CRUMB = "As-planned versus as-built"
DATE = "May 31, 2028"
DESC = ("The oldest comparison in the subject: the planned bar above the built one, and the gap "
        "between them. Simple enough that anyone follows it, and demanding enough that most "
        "versions of it fail. Claims &amp; Delay Analysis Week 13.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE SAME COMPARISON, TWO DEPTHS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">one of them is an observation; the other is an argument</text>
<text x="34" y="70" fill="#64748b" font-size="10" font-weight="700">AT PROJECT LEVEL &#8212; total time</text>
<rect x="34" y="78" width="300" height="18" rx="4" fill="#94a3b8" opacity="0.35"/>
<text x="184" y="91" text-anchor="middle" fill="#475569" font-size="9">as planned</text>
<rect x="34" y="100" width="430" height="18" rx="4" fill="#059669" opacity="0.6"/>
<text x="249" y="113" text-anchor="middle" fill="#fff" font-size="9">as built</text>
<line x1="334" y1="74" x2="334" y2="122" stroke="#cbd5e1" stroke-dasharray="3 2"/>
<text x="472" y="106" fill="#b91c1c" font-size="10" font-weight="600">the gap = the claim</text>
<text x="34" y="152" fill="#64748b" font-size="10" font-weight="700">AT ACTIVITY LEVEL &#8212; variance by variance</text>
<rect x="34" y="160" width="94" height="14" rx="3" fill="#94a3b8" opacity="0.35"/>
<rect x="34" y="176" width="128" height="14" rx="3" fill="#059669" opacity="0.6"/>
<text x="176" y="176" fill="#64748b" font-size="9">Piling &#183; +11</text>
<rect x="268" y="160" width="82" height="14" rx="3" fill="#94a3b8" opacity="0.35"/>
<rect x="268" y="176" width="90" height="14" rx="3" fill="#059669" opacity="0.6"/>
<text x="368" y="176" fill="#64748b" font-size="9">Caps &#183; +2</text>
<rect x="448" y="160" width="70" height="14" rx="3" fill="#94a3b8" opacity="0.35"/>
<rect x="448" y="176" width="118" height="14" rx="3" fill="#059669" opacity="0.6"/>
<text x="470" y="204" fill="#64748b" font-size="9">Cladding &#183; +19</text>
<rect x="34" y="216" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="238" fill="#64748b" font-size="10.5">The top version claims everything and proves nothing. The bottom one has to be argued line by line.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Both are called as-planned versus as-built. Only one of them tends to survive being read carefully.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 270" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT THE TOTAL-TIME VERSION HAS TO ESTABLISH</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">five propositions, and losing any one of them ends the claim</text>
<rect x="34" y="60" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#475569" font-size="10.5">the original programme was a reasonable plan</text>
<rect x="34" y="98" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="118" fill="#475569" font-size="10.5">the contractor contributed nothing to the critical delay &#8212; not one day of it</text>
<rect x="34" y="136" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="156" fill="#475569" font-size="10.5">every event on the as-built critical path carried entitlement to both time and money</text>
<rect x="34" y="174" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="194" fill="#475569" font-size="10.5">there was no other available way to show cause and effect</text>
<rect x="34" y="212" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="232" fill="#475569" font-size="10.5">the contractor met its own obligations &#8212; notice, information, mitigation, diligence</text>
<text x="320" y="260" text-anchor="middle" fill="#94a3b8" font-size="10.5">The second one is where nearly every total-time claim dies.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Respondents do not attack the arithmetic. They go straight down this list looking for the cheapest one to break.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 228" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT IT ASKS FOR, AND WHAT IT LETS YOU OFF</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">an unusual trade, and the reason this method survives</text>
<rect x="34" y="60" width="278" height="140" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">DOES NOT NEED</text>
<text x="54" y="104" fill="#475569" font-size="10">a monthly update series</text>
<text x="54" y="124" fill="#475569" font-size="10">logic in the as-planned programme</text>
<text x="54" y="144" fill="#475569" font-size="10">float values in the as-planned</text>
<text x="54" y="164" fill="#475569" font-size="10">any modelled calculation at all</text>
<text x="54" y="188" fill="#64748b" font-size="10">nothing is inserted or removed</text>
<rect x="328" y="60" width="278" height="140" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">DOES NEED</text>
<text x="348" y="104" fill="#64748b" font-size="10">a defensible as-built programme</text>
<text x="348" y="124" fill="#64748b" font-size="10">an as-built sequence that maps</text>
<text x="348" y="140" fill="#64748b" font-size="10">onto the planned one</text>
<text x="348" y="164" fill="#64748b" font-size="10">the as-built critical path deduced</text>
<text x="348" y="180" fill="#64748b" font-size="10">by the analyst, by hand</text>
<text x="348" y="196" fill="#64748b" font-size="10">a complete factual record</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">It forgives a poor baseline and a broken update series. It does not forgive a weak site record.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Two bars, and what they leave out.</h2>

<p>Draw the planned programme. Underneath it, draw what was actually built. Measure the gap.</p>

<p>That is the oldest comparison in the subject and still one of the most used, partly because anybody can follow it &#8212; a commercial director, a judge, a site manager &#8212; without a word of explanation.</p>

<p>It is also the point at which this phase turns around. Everything up to now started from causes: identify the events, model them, calculate the effect. This method starts from the effect. Here is what happened; now let us work out what was responsible for it.</p>

<h2>Two things share the name</h2>

""" + FIG1 + """

<p>At project level the comparison is between the planned completion date and the actual one, and the whole difference is presented as the claim. This is the total time version, and it is the one that gets served most often.</p>

<p>At activity level the comparison is done bar by bar: this activity was planned for eleven weeks and took fifteen, that one was planned for six and took six. The output isn't a single number but a pattern of variances, and the work is then to explain which of them mattered.</p>

<p>Both get called as-planned versus as-built. They are not remotely the same document, and only one of them tends to survive a careful reading.</p>

<h2>The bar the total-time version has to clear</h2>

<p>A contractor claiming the whole overrun as excusable and compensable, on the strength of a project-level comparison, is taking on considerably more than the arithmetic suggests.</p>

""" + FIG2 + """

<p>Read the second proposition again, because it is the one that ends most of these claims. Not <em>the contractor's delays were minor</em>. Not <em>they were outweighed</em>. Nothing at all &#8212; no contribution to critical delay anywhere in the job.</p>

<p>On a project long enough to produce this kind of dispute, that proposition is almost never true, and both sides usually know it before the report is opened.</p>

<h2>How the defence is actually run</h2>

<p>Respondents faced with this analysis rarely bother with the calculation. There isn't much of one to attack.</p>

<p>They go to the list instead, and to the two easiest items on it. First, find culpable events the claimant's analysis left out &#8212; a subcontractor who didn't turn up, a rig that broke down, a section rebuilt after a failed inspection. Second, find the places where the programme logic was changed during the works, which undermines using the original plan as the yardstick for anything.</p>

<p>Neither of those is difficult on a real project. That is the honest position: the defence is cheap, and it is cheap by design.</p>

<h2>What it asks for, and what it lets you off</h2>

""" + FIG3 + """

<p>Now the reason this method has not been retired, because the trade it offers is genuinely unusual.</p>

<p>It doesn't need a monthly update series &#8212; the whole apparatus Week 12 depends on. It doesn't need the as-planned programme to contain logical relationships or float values, which means it can be run against a baseline too crude for any modelled method. And nothing is inserted or subtracted anywhere, so none of the objections aimed at hypothetical models apply to it at all.</p>

<p>What it demands instead is a defensible as-built, an as-built sequence that can be mapped onto the planned one, and enough factual record to explain the variances. It also demands that the analyst deduce the as-built critical path by hand, without monthly updates to lean on &#8212; which is Week 7's inference problem arriving without the safety net.</p>

<p>So it forgives a weak baseline and a broken update series, and it does not forgive a weak site record. That is the opposite of every method in the first half of this phase, and it is why the ordering of these weeks is worth remembering.</p>

<h2>Variance is not cause</h2>

<p>Before any of that, the limitation the picture hides best.</p>

<p>The comparison measures a gap. It says nothing whatsoever about why the gap is there, and because the diagram is so legible people read causation straight off it.</p>

<p>Three activities each running twenty days over look identical on the page. One of them is the rock &#8212; an employer risk event, and a claim. One is rebar the contractor ordered late, which nobody pays for. And one is an activity that simply took longer than the estimator allowed, which is not an event at all and belongs to whoever priced the tender. <a href="risk-week-5.html">Risk Week 5</a> is worth remembering here: the $48,450 was always conditional, and a bar chart cannot tell you whether the condition held.</p>

<p>Everything that decides the money sits outside the diagram, in the records from Week 6. The comparison is a very good instrument for deciding where to look. It is not evidence of what you will find when you get there, and a report that puts the two bars on one page and a number on the next has skipped the argument entirely.</p>

<p>This is Week 2's point arriving in its most tempting form. An agreed picture of what happened and an agreed picture of what was planned still do not, between them, contain a single sentence about causation.</p>

<h2>The version that works</h2>

<p>Done properly, this can be among the most convincing analyses available, and it gets there without modelling anything.</p>

<p>Properly means at activity level. It means each significant variance identified and then explained from contemporaneous records rather than asserted. It means the contractor's own delays appearing in the analysis, priced and set against the rest, because a report that shows them is far harder to dismiss than one that doesn't.</p>

<p>And it means the same two virtues Week 12 identified: concurrency visible in the period the work was actually done, and critical delay landing in the months the costs were actually incurred. This method has both, without needing a single update.</p>

<h2>Cutting it into periods</h2>

<p>There is a windowed version, which is where most competent practitioners end up.</p>

<p>The comparison is done as before, but the variances are summarised at the end of each period rather than across the whole job. The boundaries are usually set at key milestones, at points where the contractor's intentions or method changed &#8212; an attempted acceleration, a change in conditions &#8212; rather than at arbitrary monthly intervals.</p>

<p>The naming is a small trap worth flagging. The American guidance files this under a technical label built from its characteristics, while the British protocol calls it plainly what it is. Two names, one technique, and a certain amount of unnecessary argument between people who have each read only one of the documents.</p>

<h2>Practical insight</h2>

<p>Take your job and produce the crudest possible version of this in an hour: planned dates against actual dates for the twenty most significant activities, in one table, with the variance in days beside each.</p>

<p>Then sort the table by variance, largest first, and look at the top five. Those five are your delay claim, whatever else the narrative says.</p>

<p>Now write one sentence against each explaining why it ran late, and mark the sentence <strong>evidenced</strong> or <strong>believed</strong>. The honest split is usually uncomfortable and always useful. The evidenced ones are your case. The believed ones are either work to do while the job is still running, or ground you'll concede later without meaning to.</p>

<p>An hour of that will tell you more about the strength of your position than a month of anything else in this phase.</p>

<h2>Key takeaways</h2>

<p>&#10004; This is the first effect-based method: it starts from what happened rather than from a list of causes.</p>

<p>&#10004; Project-level and activity-level comparisons share a name and are not the same exercise.</p>

<p>&#10004; The total-time version requires proving the contractor contributed nothing at all to critical delay, which is rarely true.</p>

<p>&#10004; The standard defence ignores the arithmetic and looks for omitted culpable events and mid-project logic changes.</p>

<p>&#10004; It needs no update series, no baseline logic and no float, so it works where modelled methods cannot.</p>

<p>&#10004; It requires a defensible as-built and an as-built critical path deduced by hand, so a weak site record kills it.</p>

<p>&#10004; Done at activity level, with the contractor's own delays shown, it is one of the most convincing analyses available.</p>

<h2>What&#39;s coming next</h2>

<p>The last method in this phase runs the comparison in reverse. Instead of adding events to a plan or measuring the gap between two programmes, it starts from the job as built and removes the delays to see what would have been left &#8212; the most intuitive idea in the subject and the one with the most judgement hidden inside it.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 14 &#183; Collapsed as-built &#183; coming soon</span>
                                    <h4>Take the delay out. See what remains</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Forty-One Days, Cut Into Windows &#8212; The Project Control Hub</title>",
                  "<title>Two Bars, And What They Leave Out &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Forty-One Days, Cut Into Windows | The Project Control Hub"',
                  'content="Two Bars, And What They Leave Out | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-12.html", "claim-week-13.html")
    s = s.replace('<span>Week 12<span class="crumb-title"> &#183; Windows analysis</span></span>',
                  '<span>Week 13<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 12",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 13", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · May 24, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; May 24, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="13"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week13.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 12", "claim-week-12.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    fwd = re.findall(r"Week (1[4-9]|2[0-8])\b", re.sub(r'<div class="next-article".*?</div>\s*</div>', '',
                                                       page, flags=re.S))
    if fwd:
        sys.exit("HATA: govdede numarali ileri atif: %s" % sorted(set(fwd)))
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-13.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 13 &#183; As-planned versus as-built &#183; coming soon</span>\n'
            '                                    <h4>Two bars, and what they leave out</h4>',
            '<span class="next-week-tag">Week 13 &#183; As-planned versus as-built</span>\n'
            '                                    <h4>Two bars, and what they leave out.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-13.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 13" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 13, title: "As-planned versus as-built — the comparison and its limits",\n'
           '          short: "As-planned versus as-built", status: "upcoming" },')
    new = ('        { n: 13, title: "As-planned versus as-built — the comparison and its limits",\n'
           '          short: "As-planned versus as-built", status: "live", page: "claim-week-13.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 13 live (%s)" % DATE)
    elif 'page: "claim-week-13.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 13 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-13.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-13.html</loc>\n"
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
