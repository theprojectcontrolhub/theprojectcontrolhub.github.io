#!/usr/bin/env python3
"""claim-week-15.html — Track 5, hafta 15. Faz C kapanisi. Sablon: claim-week-14.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-14.html", "claim-week-15.html"
PREV_TITLE = "Take the delay out. See what remains."
TITLE = "Same facts. Two answers. Both defensible."
CRUMB = "Why two analysts disagree"
DATE = "Jun 14, 2028"
WEEK_N = 15
DESC = ("Two competent analysts, one set of records, numbers weeks apart &#8212; and neither of them "
        "has done anything improper. Where the divergence actually enters, and what a claim can do "
        "about it. Claims &amp; Delay Analysis Week 15.")
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
<svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">EVERY DECISION THIS PHASE ASKED YOU TO MAKE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">not one of them is written in the records, and every one of them moves the number</text>
<line x1="252" y1="54" x2="252" y2="300" stroke="#e2e8f0"/>
<text x="34" y="74" fill="#64748b" font-size="10" font-weight="700">Which method</text>
<text x="266" y="74" fill="#475569" font-size="10">decided by records, timing, contract, forum</text>
<text x="34" y="98" fill="#64748b" font-size="10" font-weight="700">The baseline</text>
<text x="266" y="98" fill="#475569" font-size="10">accept as issued, correct it, or reject it</text>
<text x="34" y="122" fill="#64748b" font-size="10" font-weight="700">Started and finished</text>
<text x="266" y="122" fill="#475569" font-size="10">which of four defensible readings of a bar</text>
<text x="34" y="146" fill="#64748b" font-size="10" font-weight="700">Level of detail</text>
<text x="266" y="146" fill="#475569" font-size="10">caps the precision of everything downstream</text>
<text x="34" y="170" fill="#64748b" font-size="10" font-weight="700">As-built logic</text>
<text x="266" y="170" fill="#475569" font-size="10">the arrows &#8212; inferred, never recorded</text>
<text x="34" y="194" fill="#64748b" font-size="10" font-weight="700">Window boundaries</text>
<text x="266" y="194" fill="#475569" font-size="10">monthly, milestone-based, or event-based</text>
<text x="34" y="218" fill="#64748b" font-size="10" font-weight="700">Driving-path rule</text>
<text x="266" y="218" fill="#475569" font-size="10">how criticality is identified in each period</text>
<text x="34" y="242" fill="#64748b" font-size="10" font-weight="700">Which events go in</text>
<text x="266" y="242" fill="#475569" font-size="10">the single largest source of divergence</text>
<text x="34" y="266" fill="#64748b" font-size="10" font-weight="700">Fragnet ties and lengths</text>
<text x="266" y="266" fill="#475569" font-size="10">what it follows, what it holds up, how long</text>
<text x="34" y="290" fill="#64748b" font-size="10" font-weight="700">Order, and the residue</text>
<text x="266" y="290" fill="#475569" font-size="10">who ends up holding the delay nobody explained</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Ten choices, each defensible on its own. They do not add up. They multiply.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 258" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHERE TWO HONEST REPORTS ACTUALLY PART</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">agreement runs further than people expect, and then stops all at once</text>
<rect x="34" y="60" width="572" height="76" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">THEY AGREE ON</text>
<text x="54" y="100" fill="#475569" font-size="10.5">every date in the site records &#183; what the contract says &#183; the contract completion date</text>
<text x="54" y="118" fill="#475569" font-size="10.5">the actual completion date &#183; that the rock was encountered &#183; the arithmetic itself</text>
<rect x="34" y="146" width="572" height="94" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="166" fill="#64748b" font-size="10.5" font-weight="700">THEY PART ON</text>
<text x="54" y="186" fill="#64748b" font-size="10.5">whether the baseline could be used at all</text>
<text x="54" y="204" fill="#64748b" font-size="10.5">which activity the rock was actually holding up</text>
<text x="54" y="222" fill="#64748b" font-size="10.5">whether the eleven overlapping days belong to anybody</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Three disagreements, none of them factual, and between them a gap of weeks.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 248" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT ACTUALLY NARROWS THE GAP</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">none of it is technical, and all of it is available to you</text>
<rect x="34" y="60" width="572" height="40" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">DECLARE EVERY CHOICE</text>
<text x="54" y="94" fill="#475569" font-size="10.5">a page listing each decision and why &#8212; the difference between a method and a preference</text>
<rect x="34" y="110" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="128" fill="#059669" font-size="10.5" font-weight="700">RUN A SECOND METHOD</text>
<text x="54" y="144" fill="#475569" font-size="10.5">convergence is the strongest evidence in your report; divergence tells you where you are weak</text>
<rect x="34" y="160" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="178" fill="#059669" font-size="10.5" font-weight="700">CONCEDE WHAT IS GENUINELY CONTESTED</text>
<text x="54" y="194" fill="#475569" font-size="10.5">thirty clean days survive a challenge that forty-one asserted days will not</text>
<rect x="34" y="210" width="572" height="30" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="230" fill="#64748b" font-size="10.5">And write it so somebody can check it. An analysis nobody can follow persuades nobody.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Rigour is not the same as complexity. The most checkable report in the room usually wins.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Same facts. Two answers. Both defensible.</h2>

<p>Two experts are instructed on the same dispute. They receive identical records &#8212; the same baseline, the same diaries, the same updates, the same as-built. They are both competent, both experienced, and neither is trying to mislead anybody.</p>

<p>One reports fifty-two days of compensable delay. The other reports nineteen.</p>

<p>Week 9 quoted the guidance's own admission: selecting a technique is the most subjective task in the exercise, and even where both sides agree on the technique, the way each applies it can diverge until neither will accept the other's conclusion. Six weeks later, with all five methods on the table, it is possible to say exactly where that divergence enters.</p>

<h2>Ten decisions, none of them in the records</h2>

""" + FIG1 + """

<p>Every item on that list came up in this phase as a legitimate question with more than one legitimate answer. Which method the records support. Whether the baseline can be used as issued. What counts as an activity starting. How the as-built arrows were drawn. Where the windows fall. Which events went into the model at all.</p>

<p>Take each one in isolation and it looks like a matter of professional judgement, because it is. The problem is that they compound. Ten binary choices produce over a thousand possible analyses of one job, and while most of those combinations are silly, a dozen or so are entirely respectable and land weeks apart.</p>

<p>This is why the disagreement is structural rather than moral. Nobody has to be dishonest for the numbers to differ by a month.</p>

<h2>Where they actually part</h2>

<p>What surprises people reading two opposing reports for the first time is how far the agreement runs before it stops.</p>

""" + FIG2 + """

<p>The facts are usually common ground. Both experts accept the site records, the contract dates, the actual completion date, and that the rock was encountered where and when the register says. Neither is disputing arithmetic.</p>

<p>The split happens at three or four specific points, and they are all questions of judgement built on the same accepted facts. Could the baseline be used? What was the rock actually holding up? Do the overlapping days belong to anybody?</p>

<p>Once you can find those points in a report, you can read any expert evidence in this field. The disagreement is never spread evenly across a hundred pages. It sits in three paragraphs, and everything else is scaffolding.</p>

<h2>The single largest source</h2>

<p>Of the ten, one produces more divergence than the rest combined, and it is not a technical choice at all.</p>

<p>It is which events go into the model. Week 10 noted that two impacted as-planned reports frequently agree on every date, every fragnet and every calculation, and differ only in the list of events considered. That pattern is not confined to that method. It runs through all of them.</p>

<p>An employer's expert models the contractor's late procurement and the failed inspection. The contractor's expert models the rock and the late drawing. Both lists are accurate. Neither is complete. And no amount of scrutiny of the calculations will reconcile them, because the calculations are not where the disagreement is.</p>

<p>Which suggests the first question to ask of any delay report, yours or theirs: what is not in it?</p>

<h2>What the tribunal is actually doing</h2>

<p>It helps to know how this looks from the other side of the room, because it is not how analysts imagine it.</p>

<p>A tribunal faced with two irreconcilable expert reports is not going to adjudicate a methodological dispute. It has no basis for preferring collapsed as-built to windows analysis as a matter of principle, and it knows that.</p>

<p>What it does instead is ask whether the account of events holds together. Week 2 recorded the tendency of the English courts to fall back on common sense, treating the analytical method as secondary to whether the story makes sense. That is not anti-intellectualism. It is the only workable response to two experts who cancel each other out.</p>

<p>The practical consequence is uncomfortable for anybody who has spent three months on a model. The report that wins is frequently not the most sophisticated one. It is the one whose narrative survives being read by somebody who does not use planning software.</p>

<h2>What narrows the gap</h2>

""" + FIG3 + """

<p>None of this is a counsel of despair, and there are three things that measurably improve your position.</p>

<p><strong>Declare every choice.</strong> A page at the front of the report listing each decision and the reason for it. This costs an afternoon and it changes what the reader is looking at: a stated method rather than a preference that produced a convenient answer. It also makes disagreement productive, because the other expert can point at a line rather than at your conclusion.</p>

<p><strong>Run a second method.</strong> Where the records allow it, do the analysis twice on different assumptions and publish both. If they converge, that convergence is the strongest evidence in your report and it costs the other side dearly. If they diverge sharply, you have learned where your case is weak &#8212; privately, before somebody else explains it to you publicly.</p>

<p><strong>Concede what is genuinely contested.</strong> Week 12 made this concrete: thirty clean days and eleven contested ones is a far more durable position than forty-one asserted ones. A report that gives ground where the evidence is thin buys credibility for everywhere it doesn't.</p>

<p>Underneath all three sits the same principle the literature keeps returning to: an analysis should be transparent, and it should rest on a body of factual evidence that can be relied on. Rigour is not the same thing as complexity, and the two are frequently confused.</p>

<h2>Reading somebody else's report</h2>

<p>The mirror of all this is a short list of questions that will tell you more in twenty minutes than a full technical review in a fortnight.</p>

<p>Which method, and does the report say why that one? Which events are in the model, and which are not? Where did the as-built logic come from? Was the baseline used as issued or adjusted, and is every adjustment listed? And does the impacted completion date the report produces bear any relationship to the date the job actually finished?</p>

<p>If a report cannot answer those five from its own pages, it doesn't matter how thick it is.</p>

<h2>Practical insight</h2>

<p>Take a delay analysis you have produced or received, and write the ten decisions from the figure above down the side of a page. Fill in what was chosen for each.</p>

<p>Then, for each one, write the strongest alternative &#8212; the choice a competent analyst instructed by the other side would have made, and their reason for it.</p>

<p>Two things fall out. You will find two or three where the alternative is at least as good as yours, and those are the points the dispute will actually turn on. And you will find several you never consciously made at all, because the software or the previous analyst made them for you.</p>

<p>Those unconscious ones are the dangerous group. A choice you can defend is a position. A choice you didn't know you'd made is a hole, and it is the first thing a good cross-examiner goes looking for.</p>

<h2>Key takeaways</h2>

<p>&#10004; Two competent analysts reach different numbers because roughly ten judgement calls compound, not because either is acting improperly.</p>

<p>&#10004; None of those decisions is recorded anywhere in the project's documents.</p>

<p>&#10004; Opposing reports usually agree on all the facts and part company at three or four specific points of judgement.</p>

<p>&#10004; The largest single source of divergence is which events were put into the model, which no amount of checking the calculations will resolve.</p>

<p>&#10004; A tribunal will not adjudicate a methodological dispute; it will ask whether the account of events holds together.</p>

<p>&#10004; Declaring every choice, running a second method, and conceding what is genuinely contested all measurably strengthen a claim.</p>

<p>&#10004; A choice you did not know you were making is the weakest point in any analysis, and the easiest one to find.</p>

<h2>What&#39;s coming next</h2>

<p>That closes the methods. Everything from here is the argument the methods cannot settle by themselves, and it starts with the one this phase has deferred four times: two causes running at once, one delay, and no agreed definition of what that even means. Next week is concurrency, where the contract that governs this job hands the question to a document most projects never fill in.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 16 &#183; Concurrency &#183; coming soon</span>
                                    <h4>Both sides caused it. Now what?</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Take The Delay Out. See What Remains &#8212; The Project Control Hub</title>",
                  "<title>Same Facts. Two Answers. Both Defensible &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Take The Delay Out. See What Remains | The Project Control Hub"',
                  'content="Same Facts. Two Answers. Both Defensible | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-14.html", "claim-week-15.html")
    s = s.replace('<span>Week 14<span class="crumb-title"> &#183; Collapsed as-built</span></span>',
                  '<span>Week 15<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 14",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 15", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jun 7, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jun 7, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week15.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 14", "claim-week-14.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    body_only = page[page.index('<div class="content-preview"'):page.index("<!-- PAYWALL CTA -->")]
    fwd = sorted({m for m in re.findall(r"Week (\d+)", body_only) if int(m) > WEEK_N})
    if fwd:
        sys.exit("HATA: govdede numarali ileri atif: Week %s" % ", ".join(fwd))
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-15.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 15 &#183; Why two analysts disagree &#183; coming soon</span>\n'
            '                                    <h4>Same facts. Two answers. Both defensible</h4>',
            '<span class="next-week-tag">Week 15 &#183; Why two analysts disagree</span>\n'
            '                                    <h4>Same facts. Two answers. Both defensible.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-15.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 15" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 15, title: "Why two analysts disagree — method choice as the real dispute",\n'
           '          short: "Why two analysts disagree", status: "upcoming" },')
    new = ('        { n: 15, title: "Why two analysts disagree — method choice as the real dispute",\n'
           '          short: "Why two analysts disagree", status: "live", page: "claim-week-15.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 15 live (%s)" % DATE)
    elif 'page: "claim-week-15.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 15 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-15.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-15.html</loc>\n"
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
