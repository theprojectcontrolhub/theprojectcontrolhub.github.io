#!/usr/bin/env python3
"""claim-week-11.html — Track 5, hafta 11. Sablon: claim-week-10.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-10.html", "claim-week-11.html"
PREV_TITLE = "A forecast made after the fact."
TITLE = "The method the contract asks for."
CRUMB = "Time impact analysis"
DATE = "May 17, 2028"
DESC = ("Same fragnet as last week, inserted somewhere else: the programme as it stood the day "
        "before the event. One change fixes the worst fault of impacted as-planned, and the two "
        "industry protocols still disagree about it. Claims &amp; Delay Analysis Week 11.")
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
<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">SAME EVENT, TWO PLACES TO PUT IT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the entire difference between last week&#39;s method and this one</text>
<text x="34" y="70" fill="#64748b" font-size="10" font-weight="700">IMPACTED AS-PLANNED &#8212; into the original plan</text>
<rect x="34" y="78" width="140" height="18" rx="4" fill="#94a3b8" opacity="0.35"/>
<text x="104" y="91" text-anchor="middle" fill="#475569" font-size="9">Piling, as planned</text>
<rect x="174" y="78" width="56" height="18" rx="4" fill="#b91c1c" opacity="0.5"/>
<text x="202" y="91" text-anchor="middle" fill="#fff" font-size="9">rock</text>
<rect x="230" y="78" width="150" height="18" rx="4" fill="#94a3b8" opacity="0.35"/>
<text x="305" y="91" text-anchor="middle" fill="#475569" font-size="9">everything after, as planned</text>
<text x="392" y="91" fill="#64748b" font-size="9.5">nine months of reality omitted</text>
<text x="34" y="130" fill="#64748b" font-size="10" font-weight="700">TIME IMPACT ANALYSIS &#8212; into the programme as it stood that week</text>
<rect x="34" y="138" width="112" height="18" rx="4" fill="#059669" opacity="0.75"/>
<text x="90" y="151" text-anchor="middle" fill="#fff" font-size="9">actual progress</text>
<line x1="146" y1="128" x2="146" y2="166" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="146" y="176" text-anchor="middle" fill="#0f172a" font-size="8.5">data date</text>
<rect x="146" y="138" width="56" height="18" rx="4" fill="#b91c1c" opacity="0.5"/>
<text x="174" y="151" text-anchor="middle" fill="#fff" font-size="9">rock</text>
<rect x="202" y="138" width="178" height="18" rx="4" fill="#059669" opacity="0.45"/>
<text x="291" y="151" text-anchor="middle" fill="#fff" font-size="9">remaining work, as then forecast</text>
<text x="392" y="151" fill="#64748b" font-size="9.5">logic and durations already corrected</text>
<rect x="34" y="192" width="572" height="46" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="212" fill="#64748b" font-size="10.5">The fragnet is identical. What differs is everything to the left of it &#8212; and that is where the</text>
<text x="54" y="230" fill="#64748b" font-size="10.5">contractor&#39;s own performance finally enters the model.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">One insertion point is a plan. The other is a plan that has already been corrected by nine months of the job.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHY THE TWO PROTOCOLS DISAGREE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">not a technical dispute &#8212; a difference about what the exercise is for</text>
<rect x="34" y="60" width="278" height="134" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE SCL PROTOCOL</text>
<text x="54" y="104" fill="#475569" font-size="10">a prospective document</text>
<text x="54" y="122" fill="#475569" font-size="10">expressly prefers this method</text>
<text x="54" y="140" fill="#475569" font-size="10">deal with it close to the event</text>
<text x="54" y="164" fill="#64748b" font-size="10">purpose: stop the dispute</text>
<text x="54" y="182" fill="#64748b" font-size="10">from ever needing forensics</text>
<rect x="328" y="60" width="278" height="134" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">AACE RP 29R-03</text>
<text x="348" y="104" fill="#64748b" font-size="10">an expressly forensic guide</text>
<text x="348" y="122" fill="#64748b" font-size="10">equal weighting to all methods</text>
<text x="348" y="140" fill="#64748b" font-size="10">no steer on which courts prefer</text>
<text x="348" y="164" fill="#64748b" font-size="10">purpose: standardise how</text>
<text x="348" y="182" fill="#64748b" font-size="10">the wreckage gets analysed</text>
<text x="320" y="222" text-anchor="middle" fill="#94a3b8" font-size="10.5">Each is criticised for the other&#39;s virtue: one for favouring a method, one for refusing to.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Before arguing about which is right, check which question the person you are arguing with is answering.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 224" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHEN IT FITS, AND WHEN IT EATS THE BUDGET</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the deciding factor is the shape of the events, not their total</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">A FEW LARGE IMPACTS</text>
<text x="54" y="97" fill="#475569" font-size="10.5">one intermediate programme each, defensible, and finishable inside a sensible fee</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="134" fill="#64748b" font-size="10.5" font-weight="700">MANY SMALL EVENTS</text>
<text x="54" y="151" fill="#64748b" font-size="10.5">a new base programme for each one, and the analysis becomes a project in itself</text>
<rect x="34" y="168" width="572" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="188" fill="#64748b" font-size="10.5">And a rule of thumb worth keeping: the longer the window and the longer the fragnet,</text>
<text x="54" y="204" fill="#64748b" font-size="10.5">the further the result drifts from what the as-built will eventually show.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Reaching for this method on a job with sixty small variations is how a delay analysis costs more than the claim.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The method the contract asks for.</h2>

<p>The fragnet is the same. The event is the same. The arithmetic is the same. One thing changes, and it changes almost everything.</p>

<p>Instead of inserting the delay into the original baseline, you insert it into the programme as it stood immediately before the event happened &#8212; updated with actual progress to that date, with the logic and remaining durations as the project then understood them.</p>

""" + FIG1 + """

<p>Look at what that fixes. Last week's method could not see the contractor's own performance, because the model contained no performance at all. This one starts from a programme that has already absorbed nine months of it: the slippage, the resequencing, the durations that turned out longer. The event lands on the job as it actually was.</p>

<h2>What the change buys</h2>

<p>Four things, and they are the reason this method is preferred wherever assessment happens during the works.</p>

<p>It runs on contemporaneous intentions rather than original ones. Logic and durations for the remaining work reflect what the team believed at the time, not what somebody hoped before the site was cleared.</p>

<p>It uses the dynamic critical path. Week 4 established that criticality belongs to a moment; this method asks the question at that moment rather than assuming the baseline's answer held for three years.</p>

<p>It can be done while the job is running, which means the answer arrives when it is still useful and when the people who know what happened are still on site.</p>

<p>And it corrects itself. At each update the programme is reset to actual progress, so an error in one window does not compound through the next. The analysis is re-anchored to reality every month, which is a property none of the purely theoretical methods have.</p>

<h2>Why the two protocols argue about it</h2>

""" + FIG2 + """

<p>Week 9 introduced the two reference documents. This is the method they disagree about, and the disagreement is more interesting than a technical dispute.</p>

<p>The SCL Protocol is a prospective document. It expressly prefers this technique for estimating the impact of change as the project runs, and the principle underneath it is that entitlement ought to be claimed and settled while the event is still recent. The purpose is to stop disputes maturing into the kind of exercise this track exists to describe.</p>

<p>The American guidance is expressly forensic. It gives equal weight to all the techniques and declines to say which ones courts prefer, or which are more accurate.</p>

<p>So each is criticised for exactly what the other considers a virtue: the Protocol for leaning too heavily on one method, the American document for refusing to lean at all. Both criticisms are fair, and neither is a reason to ignore either. Before arguing about which is right, find out which question your opponent is answering.</p>

<h2>What it still cannot do</h2>

<p>The improvements are real. The method remains, at bottom, a model.</p>

<p>It still produces a theoretical answer to a hypothetical question: what this event was forecast to do, from where the job then stood. That's a better hypothetical than last week's, and it still isn't a measurement.</p>

<p>It cannot identify actual concurrent delay. It can show approximate concurrency &#8212; where employer and contractor events overlap in a window &#8212; but a predictive model cannot, by itself, establish what genuinely ran alongside what.</p>

<p>And there is a consequence for the money that people discover late: a prospective result may not line up with the cost records at all. You have an entitlement expressed in forecast days, and a ledger expressed in what was actually spent, and reconciling the two is work nobody budgeted for. Both of the methods in this phase so far share that problem.</p>

<h2>Cause-based and effect-based</h2>

<p>It is worth naming the family properly here, because it explains the shape of the rest of this phase.</p>

<p>This method, last week's, and the subtraction method still to come are all <em>cause-based</em>: you identify the events and let a model calculate their effect. The methods built from the as-built are <em>effect-based</em>: you start from what happened and work back to the most likely cause of each piece of it.</p>

<p>Cause-based methods are cleaner to explain and easier to attack on their assumptions. Effect-based methods are harder to explain and harder to dismiss, because they begin with facts. That is the trade the second half of this phase is about.</p>

<h2>What doing it properly costs</h2>

""" + FIG3 + """

<p>Here is the part that gets underestimated in fee proposals and overestimated in optimism.</p>

<p>The method needs a programme updated to the moment before each event. Where monthly updates exist, some of that is free. Where they don't, the analyst has to build intermediate programmes &#8212; assessing percentage complete, remaining durations and any logic revisions for every activity, at each of those moments. Records rarely support that to the day, so each intermediate programme carries its own judgements, and every one of them has to be transparent or the whole thing collapses.</p>

<p>With a handful of large events that's manageable and defensible. With sixty small variations it becomes a project in its own right, and the honest advice is to use something else.</p>

<p>One more rule worth carrying: the longer the window and the longer the fragnet, the more the result drifts from what the as-built eventually shows. Short windows keep the analysis honest, because the correction at each data date is small enough to be seen.</p>

<h2>The rule that catches people</h2>

<p>A quiet consequence of the self-correcting property, and it works against the contractor.</p>

<p>At each update, the programme is reset to actual progress. Gains and losses arising from the natural progress of the work are not employer events &#8212; and delay in a window that nothing explains is, by default, the contractor's. Silence isn't neutral in this method. It's an allocation.</p>

<p>Which is another way of saying that a thin update series does not merely limit your options. It hands over the unexplained months.</p>

<h2>Even the prospective contract has doubts</h2>

<p>One last complication, and it is a useful corrective to the idea that prospective assessment is settled.</p>

<p>The NEC family is the most committed to forecasting: compensation events are assessed on forecast cost for work not yet done, with a defined division between forecast and actual. It's the prospective philosophy expressed as a contractual mechanism rather than as guidance.</p>

<p>Even there, the question is live. A Northern Ireland High Court decision has favoured assessment on actual cost over forecast in the circumstances before it, and the commentary treats it as significant rather than an aberration.</p>

<p>Take from that only what it will bear. Prospective assessment is a strong principle with a real tension inside it, and anybody who tells you the profession has settled which way to look hasn't been reading.</p>

<h2>Practical insight</h2>

<p>On your current job, take the single largest variation or delay event of the last year and try this properly, once.</p>

<p>Find the last programme update issued before that event. Check it is the submitted one, and that you have the native file. Then build the fragnet: what the event required, what it came after, what it held up. Insert, re-run, and write down the movement in the forecast completion date.</p>

<p>Then compare that number to what you claimed at the time, if you claimed anything. The gap between the two is the most instructive number in this exercise. It's usually a gap, and it's usually in the direction of having claimed too little, too vaguely, and too late.</p>

<p>The exercise takes a morning. It also tells you whether your update series can support the method at all, which is worth finding out on an event that isn't yet in dispute.</p>

<h2>Key takeaways</h2>

<p>&#10004; The only difference from last week's method is the insertion point: the programme as it stood immediately before the event.</p>

<p>&#10004; That single change lets the contractor's own performance into the model and puts the question on the dynamic critical path.</p>

<p>&#10004; The analysis re-anchors to actual progress at each update, so errors don't compound across windows.</p>

<p>&#10004; The SCL Protocol prefers this method because it is trying to prevent disputes; the American guidance declines to prefer anything because it is trying to analyse them.</p>

<p>&#10004; It remains a model: still a hypothetical, still unable to establish actual concurrency, and its forecast days may not reconcile with the cost ledger.</p>

<p>&#10004; It suits a few large events; with many small ones each needs its own intermediate programme and the analysis becomes a project.</p>

<p>&#10004; Unexplained delay in a window defaults to the contractor, so gaps in the update series give ground away rather than merely limiting options.</p>

<h2>What&#39;s coming next</h2>

<p>This method asks its question one event at a time. The next one asks it one period at a time, taking the job in slices and finding out what was driving in each &#8212; the technique that runs directly on the update series Phase B spent a week defending, and the one that comes closest to describing the job rather than a model of it.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 12 &#183; Windows analysis &#183; coming soon</span>
                                    <h4>Forty-one days, cut into windows</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>A Forecast Made After The Fact &#8212; The Project Control Hub</title>",
                  "<title>The Method The Contract Asks For &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="A Forecast Made After The Fact | The Project Control Hub"',
                  'content="The Method The Contract Asks For | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-10.html", "claim-week-11.html")
    s = s.replace('<span>Week 10<span class="crumb-title"> &#183; Impacted as-planned</span></span>',
                  '<span>Week 11<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 10",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 11", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · May 10, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; May 10, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="11"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week11.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 10", "claim-week-10.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-11.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 11 &#183; Time impact analysis &#183; coming soon</span>\n'
            '                                    <h4>The method the contract asks for</h4>',
            '<span class="next-week-tag">Week 11 &#183; Time impact analysis</span>\n'
            '                                    <h4>The method the contract asks for.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-11.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 11" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 11, title: "Time impact analysis — fragnets, updates and prospective assessment",\n'
           '          short: "Time impact analysis", status: "upcoming" },')
    new = ('        { n: 11, title: "Time impact analysis — fragnets, updates and prospective assessment",\n'
           '          short: "Time impact analysis", status: "live", page: "claim-week-11.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 11 live (%s)" % DATE)
    elif 'page: "claim-week-11.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 11 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-11.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-11.html</loc>\n"
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
