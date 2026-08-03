#!/usr/bin/env python3
"""claim-week-12.html — Track 5, hafta 12. Sablon: claim-week-11.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-11.html", "claim-week-12.html"
PREV_TITLE = "The method the contract asks for."
TITLE = "Forty-one days, cut into windows."
CRUMB = "Windows analysis"
DATE = "May 24, 2028"
DESC = ("Stop treating the delay as one number. Slice the job at the update dates, ask what was "
        "driving in each slice, and the forty-one days come apart into thirty that are clean and "
        "eleven that are not. Claims &amp; Delay Analysis Week 12.")
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
<svg viewBox="0 0 640 258" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE NUMBER, OR TWO ANSWERS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same forty-one days, analysed as a lump and analysed in periods</text>
<text x="34" y="70" fill="#64748b" font-size="10" font-weight="700">AS A SINGLE CLAIM</text>
<rect x="34" y="78" width="420" height="22" rx="4" fill="#059669" opacity="0.35"/>
<text x="244" y="93" text-anchor="middle" fill="#475569" font-size="10">41 days &#183; the rock &#183; employer</text>
<text x="466" y="93" fill="#94a3b8" font-size="9.5">one figure to accept or reject</text>
<text x="34" y="132" fill="#64748b" font-size="10" font-weight="700">CUT AT THE UPDATE DATES</text>
<rect x="34" y="140" width="308" height="22" rx="4" fill="#059669" opacity="0.75"/>
<text x="188" y="155" text-anchor="middle" fill="#fff" font-size="10">window 1 &#183; 30 days &#183; piling driving alone</text>
<rect x="342" y="140" width="112" height="22" rx="4" fill="#b91c1c" opacity="0.45"/>
<text x="398" y="155" text-anchor="middle" fill="#fff" font-size="10">11 days &#183; two paths</text>
<line x1="342" y1="130" x2="342" y2="172" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="466" y="149" fill="#64748b" font-size="9.5">services float exhausted</text>
<text x="466" y="163" fill="#64748b" font-size="9.5">on day thirty-one</text>
<rect x="34" y="188" width="572" height="56" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="210" fill="#64748b" font-size="10.5">Thirty days nobody can seriously argue with, and eleven that are genuinely contested.</text>
<text x="54" y="230" fill="#64748b" font-size="10.5">The lump invited a rejection of all forty-one. The windows concede eleven and secure thirty.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Illustrative, using the float assumption from Week 4. The point is the shape of the answer, not the figures.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHY THIS ONE RECONCILES WITH THE LEDGER</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the delay is located in the period, and so is the money</text>
<rect x="34" y="60" width="278" height="70" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE PROSPECTIVE METHODS</text>
<text x="54" y="102" fill="#64748b" font-size="10">an entitlement in forecast days</text>
<text x="54" y="120" fill="#64748b" font-size="10">and a ledger of what was spent</text>
<rect x="328" y="60" width="278" height="70" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="82" fill="#059669" font-size="10.5" font-weight="700">A PERIOD-BASED ANALYSIS</text>
<text x="348" y="102" fill="#475569" font-size="10">critical delay dated to the month</text>
<text x="348" y="120" fill="#475569" font-size="10">the cost was actually incurred in</text>
<rect x="34" y="146" width="572" height="76" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="168" fill="#64748b" font-size="10.5" font-weight="600">On this job, at $7,100 a month:</text>
<text x="54" y="190" fill="#64748b" font-size="10.5">30 days clean &#183; roughly $6,997 &#8212; and it is 30 specific, dated days</text>
<text x="54" y="210" fill="#64748b" font-size="10.5">11 days contested &#183; roughly $2,566 &#8212; argued on its own, not dragging the rest with it</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">An average daily rate, which the quantum phase will complicate. But the days now have dates, which is what the ledger needs.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">HOW FAR YOU TOUCHED THE DATA</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">three positions, and only the first one is free of your own judgement</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">AS-IS</text>
<text x="54" y="97" fill="#475569" font-size="10.5">the submitted updates, unaltered, analysed in the condition they were issued</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#059669" opacity="0.05" stroke="#a7f3d0"/>
<text x="54" y="134" fill="#059669" font-size="10.5" font-weight="700">CORRECTED</text>
<text x="54" y="151" fill="#475569" font-size="10.5">errors in the contemporaneous files repaired, each repair listed and justified</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#64748b" font-size="10.5" font-weight="700">RECREATED</text>
<text x="54" y="205" fill="#64748b" font-size="10.5">updates built afterwards for months that never had one &#8212; treat with real caution</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Say which one you did, on the first page. A reviewer who discovers it on page ninety will assume it was hidden.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Forty-one days, cut into windows.</h2>

<p>Every method so far has produced a single number. Forty-one days, claimed as one thing, defended as one thing, and therefore capable of being rejected as one thing.</p>

<p>This method stops doing that. Instead of asking what an event did to the job, it takes the job in periods &#8212; usually the periods between programme updates &#8212; and asks a different question of each one: what moved in this window, what was driving, and why.</p>

<p>The events do not need to be identified first. The analysis finds what was controlling and then goes looking for the reason.</p>

""" + FIG1 + """

<p>Week 4 set this up with arithmetic and no method attached: the rock delays piling, the services path carries thirty days of float, and on day thirty-one that path runs out of slack and becomes critical too. Windows analysis is what turns that observation into an answer.</p>

<p>Thirty days where one path was driving and the cause is not seriously arguable. Eleven days where two paths were driving and the argument is real. The lump claim invited a rejection of all forty-one. The windowed one concedes eleven and makes thirty very hard to refuse.</p>

<h2>Why the path moves</h2>

<p>The method exists because criticality is unstable, and it is worth knowing what actually moves it. Actual progress differs from planned durations. Delay events change remaining durations. Scope is added or removed. Work goes out of sequence &#8212; changed intentions, late design information, unforeseen conditions, plant breakdowns, restricted access. And the logic itself gets changed to suit how the job is now going to be built.</p>

<p>Each of those shifts total float somewhere in the programme, and when float moves the critical path moves with it &#8212; not once, but repeatedly, month after month. A method that identifies the driving path a single time and applies it across three years isn't simplifying. It is answering a question nobody asked.</p>

<h2>What this buys that the last two methods can't</h2>

<p>Three things, and the third is the one that matters most for the second half of this track.</p>

<p>It shows gains as well as losses. A window in which the job recovered eight days appears in the analysis, because the analysis is looking at periods rather than at events somebody selected. Nothing in the previous two methods can see recovery.</p>

<p>It finds concurrency in the period the work was actually done, rather than approximating it from a model. That is not the whole of the concurrency question &#8212; the hard part of that arrives in the next phase &#8212; but it is evidence rather than inference.</p>

""" + FIG2 + """

<p>And it locates critical delay in the period during which the costs were being incurred. That sounds like a technicality and it is the opposite of one. Week 11 flagged the problem: a prospective analysis produces entitlement in forecast days, the cost ledger records what was actually spent, and joining the two is unbudgeted work. A period-based analysis hands you dated days. Thirty of them fall in specific months, and those months have costs in them.</p>

<p>At $7,100 a month, thirty days is roughly $6,997 and the contested eleven are roughly $2,566. Those are average-rate figures, and the quantum phase will complicate them properly. What matters here is that the days have dates, which is the thing the ledger needs and the earlier methods could not supply.</p>

<h2>How far did you touch the data</h2>

""" + FIG3 + """

<p>There is an integrity question underneath this method, and it is easier to answer honestly than to answer later.</p>

<p>The strongest version uses the submitted updates exactly as they were issued. Nothing altered, nothing improved. When the underlying data is left in its contemporaneous condition the analysis is objective in a way no other method manages, because both parties already have the files.</p>

<p>The second version corrects errors in those files. That is often necessary and entirely legitimate &#8212; provided every correction is listed, with a reason, and the effect of each on the answer can be seen.</p>

<p>The third version builds updates that never existed, for months nobody updated. It can be done, with an accepted baseline and detailed progress data, and the result may fairly represent what the contractor would have reported. It also imports the analyst's judgement into the contemporaneous record, which is the one thing that record had going for it. Caution is not a formality here.</p>

<h2>Where the argument goes</h2>

<p>Two choices decide most of the disagreement between two competent windows analyses, and neither is technical.</p>

<p>The first is where the boundaries fall. Monthly windows match the update cycle and are easy to defend on that ground. Event-based windows &#8212; cut at the delay events themselves &#8212; are defensible on the different ground that a window containing two events cannot separate them. Week 9 used this as the example of why agreeing a method is not agreeing an answer. Here it is, in the method it applies to.</p>

<p>The second is how driving activities are identified in each window. The more that determination follows a stated, systematic rule and the less it depends on the analyst's reading, the harder the result is to attack. Write the rule down before running the analysis, not after seeing what it produces.</p>

<h2>Its quiet weakness</h2>

<p>Every method in this phase has one, and this one's is easy to miss because the analysis looks so solid.</p>

<p>A window tells you what was driving and by how much the forecast moved. It does not, by itself, tell you why. That still comes from the records &#8212; the diaries, the correspondence, the registers from Week 6 &#8212; and a window analysis presented without them is a very precise account of movement with no explanation attached.</p>

<p>Which produces a specific failure worth watching for. A window shows eleven days lost and the report attributes them to the nearest available employer event, because it is the only candidate written down anywhere. That isn't analysis; it's proximity. The method is objective about <em>what</em> and completely dependent on your records for <em>why</em>, and the gap between those two is where a well-built windows analysis still gets taken apart.</p>

<h2>What it needs, and what that means for you</h2>

<p>The requirement is short and unforgiving: updated programmes, at intervals, with actual start, actual finish and progress for each activity in each period.</p>

<p>Phase B spent a week on exactly that list. This is the method that spends it. Where the update series is complete, this technique is available and it is usually the strongest thing you have. Where it isn't, the method may simply not be appropriate, and no amount of skill closes the gap.</p>

<p>There is a small piece of history worth knowing here. After the SCL Protocol appeared, contracts increasingly began requiring regularly updated contemporaneous programmes &#8212; typically monthly. The obligation many teams treat as bureaucratic overhead is, in part, the industry arranging for this method to be possible.</p>

<h2>Practical insight</h2>

<p>Take the six most recent updates on your job and do a crude version of this in an afternoon. You need no software beyond what you already have open.</p>

<p>For each consecutive pair, write down two things: what the forecast completion date was, and which chain of activities was driving it. That gives you six dates and six paths.</p>

<p>Now look at where the forecast moved and where the driving path changed. Every month in which the date slipped is a window with a cause in it, and every month in which the driving path changed hands is a window somebody will argue about later.</p>

<p>Do that once and you will have a one-page table that is more use in a negotiation than most fifty-page reports, because it is built entirely from documents both sides already hold.</p>

<h2>Key takeaways</h2>

<p>&#10004; Windows analysis asks what was driving in each period rather than what a selected event did to the job.</p>

<p>&#10004; It splits a single contested number into the part that is clean and the part that genuinely is not.</p>

<p>&#10004; The critical path moves for many ordinary reasons, so a method that fixes it once is answering the wrong question.</p>

<p>&#10004; It sees recovery as well as slippage, because it looks at periods rather than at events somebody chose to include.</p>

<p>&#10004; It dates the delay to the months in which the costs were incurred, which is what makes time and money reconcile.</p>

<p>&#10004; State whether the updates were used as issued, corrected, or recreated &#8212; and put it at the front.</p>

<p>&#10004; Window boundaries and the rule for identifying driving activities decide most disagreements; fix both before you run anything.</p>

<p>&#10004; The method establishes what was driving, never why; attributing a window to the nearest available event is proximity rather than causation.</p>

<h2>What&#39;s coming next</h2>

<p>The methods so far have all started from causes and modelled forward to effects. The rest of this phase turns around and starts from what happened. Next week is the oldest and simplest comparison in the subject &#8212; the planned bars against the built ones &#8212; what it can genuinely establish, and the reason it survives in a field that has largely moved past it.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 13 &#183; As-planned versus as-built &#183; coming soon</span>
                                    <h4>Two bars, and what they leave out</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Method The Contract Asks For &#8212; The Project Control Hub</title>",
                  "<title>Forty-One Days, Cut Into Windows &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Method The Contract Asks For | The Project Control Hub"',
                  'content="Forty-One Days, Cut Into Windows | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-11.html", "claim-week-12.html")
    s = s.replace('<span>Week 11<span class="crumb-title"> &#183; Time impact analysis</span></span>',
                  '<span>Week 12<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 11",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 12", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · May 17, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; May 17, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="12"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week12.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 11", "claim-week-11.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-12.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 12 &#183; Windows analysis &#183; coming soon</span>\n'
            '                                    <h4>Forty-one days, cut into windows</h4>',
            '<span class="next-week-tag">Week 12 &#183; Windows analysis</span>\n'
            '                                    <h4>Forty-one days, cut into windows.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-12.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 12" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 12, title: "Windows analysis — contemporaneous periods and time slices",\n'
           '          short: "Windows analysis", status: "upcoming" },')
    new = ('        { n: 12, title: "Windows analysis — contemporaneous periods and time slices",\n'
           '          short: "Windows analysis", status: "live", page: "claim-week-12.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 12 live (%s)" % DATE)
    elif 'page: "claim-week-12.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 12 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-12.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-12.html</loc>\n"
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
