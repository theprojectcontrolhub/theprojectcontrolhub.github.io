#!/usr/bin/env python3
"""claim-week-21.html — Track 5, hafta 21. Sablon: claim-week-20.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-20.html", "claim-week-21.html"
PREV_TITLE = "The best proof is your own site."
TITLE = "Everything after the mile is weaker."
CRUMB = "Productivity loss"
DATE = "Jul 26, 2028"
WEEK_N = 21
DESC = ("Most jobs cannot produce a clean comparison period. What remains is a ladder of "
        "alternatives, each one further from your own site than the last &#8212; and published "
        "factors you have to justify before you are allowed to use them. Claims &amp; Delay "
        "Analysis Week 21.")
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
<svg viewBox="0 0 640 288" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE LADDER BELOW THE MILE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">each rung moves the benchmark further from your own site</text>
<rect x="34" y="60" width="572" height="40" rx="8" fill="#059669" opacity="0.12" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">A CLEAN PERIOD ON THIS JOB</text>
<text x="54" y="94" fill="#475569" font-size="10.5">the measured mile &#8212; your crews, your site, no estimate in the argument</text>
<rect x="34" y="106" width="572" height="40" rx="8" fill="#059669" opacity="0.07" stroke="#a7f3d0"/>
<text x="54" y="124" fill="#059669" font-size="10.5" font-weight="700">A SAMPLED PERIOD ON THIS JOB</text>
<text x="54" y="140" fill="#475569" font-size="10.5">work sampling, time and motion &#8212; still your site, but now an observer chose the sample</text>
<rect x="34" y="152" width="572" height="40" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="170" fill="#64748b" font-size="10.5" font-weight="700">YOUR OTHER PROJECTS</text>
<text x="54" y="186" fill="#64748b" font-size="10.5">the same firm, different job &#8212; different ground, different team, different year</text>
<rect x="34" y="198" width="572" height="40" rx="8" fill="#94a3b8" opacity="0.13" stroke="#cbd5e1"/>
<text x="54" y="216" fill="#64748b" font-size="10.5" font-weight="700">YOUR ESTIMATE</text>
<text x="54" y="232" fill="#64748b" font-size="10.5">modified total cost &#8212; and now your tender is the thing on trial</text>
<rect x="34" y="244" width="572" height="40" rx="8" fill="#94a3b8" opacity="0.16" stroke="#cbd5e1"/>
<text x="54" y="262" fill="#64748b" font-size="10.5" font-weight="700">PUBLISHED FACTORS</text>
<text x="54" y="278" fill="#64748b" font-size="10.5">somebody else&#39;s projects, averaged &#8212; and you must prove they resemble yours</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">You do not choose your rung. Your records chose it, some time ago, without telling anybody.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 224" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">BEFORE YOU CITE A PUBLISHED FACTOR</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the table is not the argument; the relevance of the table is the argument</text>
<rect x="34" y="60" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="78" fill="#64748b" font-size="10.5" font-weight="700">WHOSE PROJECTS WERE STUDIED?</text>
<text x="54" y="93" fill="#64748b" font-size="10.5">trade, sector, country, era &#8212; and whether any of them resemble this one</text>
<rect x="34" y="106" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="124" fill="#64748b" font-size="10.5" font-weight="700">WHAT DID THE STUDY ACTUALLY MEASURE?</text>
<text x="54" y="139" fill="#64748b" font-size="10.5">the factor you are quoting may not be the factor that was tested</text>
<rect x="34" y="152" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="170" fill="#64748b" font-size="10.5" font-weight="700">HAVE YOU READ IT, OR CITED SOMEBODY CITING IT?</text>
<text x="54" y="185" fill="#64748b" font-size="10.5">figures acquire authority by repetition; check the source you are naming</text>
<rect x="34" y="196" width="572" height="24" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="212" fill="#475569" font-size="10.5">Apply it only to the trade and the period actually disrupted &#8212; never across the whole job.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">These tables are widely used and just as widely stretched past what they can carry.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 216" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHEN TO MEASURE IT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the honest answer is inconvenient for everybody</text>
<rect x="34" y="60" width="278" height="98" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">AFTER IT IS OVER</text>
<text x="54" y="104" fill="#475569" font-size="10">the actual data exists</text>
<text x="54" y="122" fill="#475569" font-size="10">the loss can be measured</text>
<text x="54" y="144" fill="#64748b" font-size="10">employers dislike this intensely</text>
<rect x="328" y="60" width="278" height="98" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">WHILE IT IS HAPPENING</text>
<text x="348" y="104" fill="#64748b" font-size="10">a forecast, not a measurement</text>
<text x="348" y="122" fill="#64748b" font-size="10">frequently impossible to total</text>
<text x="348" y="144" fill="#64748b" font-size="10">so reserve your position, in writing</text>
<text x="320" y="188" text-anchor="middle" fill="#94a3b8" font-size="10.5">If you must submit a figure early, say plainly that it is incomplete and that you reserve the rest.</text>
<text x="320" y="206" text-anchor="middle" fill="#94a3b8" font-size="10.5">A number submitted without that sentence can become the number you are held to.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The reservation costs one sentence and is the difference between an interim figure and a cap.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Everything after the mile is weaker.</h2>

<p>Last week described the strongest disruption argument available and then, honestly, admitted how rarely it can be built. Most jobs have no clean period. Or they have one and the records cannot show it. Or the work was never repetitive enough for a comparison to mean anything at all.</p>

<p>So this week is the rest of the field, ranked the way it deserves to be ranked, which is downwards.</p>

""" + FIG1 + """

<p>Read that ladder as a single idea: every rung moves the benchmark further away from your own site, and every step away hands the other side a new thing to argue about that has nothing to do with what happened on your job.</p>

<h2>Still on your site, but sampled</h2>

<p>The first step down keeps the work in front of you. Work sampling and time-and-motion observation put somebody on site to record what crews are actually doing &#8212; how much of the day is productive, how much is waiting, moving, searching for materials.</p>

<p>Its strength is obvious: it is your job, observed directly. Its weakness is just as obvious once stated. Somebody chose when to observe and what to count, the observation itself changes behaviour, and it can only be done while the work is still going on. Nobody can sample last year.</p>

<p>It is a real technique and a good one. It just isn't available to anybody reading this after the event, which is most people who need it.</p>

<h2>Somebody else's project, or your own tender</h2>

<p>Below that the benchmark leaves the site entirely, and there are two directions to go.</p>

<p>One is other projects &#8212; yours or comparable contractors' &#8212; used to establish what the work should have taken. That comparison is only as good as the resemblance, and resemblance is exactly what the other side will attack: different ground, different design, different crew, different market, different decade.</p>

<p>The other direction is your own estimate, which is where the modified total cost approach sits. You start from what the job actually cost, then deduct the parts attributable to your own inefficiency and to errors in your pricing, and claim the remainder.</p>

<p>The word doing the work in that sentence is <em>modified</em>. An unmodified total cost claim asks the other side to accept that everything above your tender was their fault, and that argument has its own week coming. The modified version is genuinely better because it concedes something before being asked. It still puts your tender in the witness box, and your tender is a document nobody else has ever agreed with.</p>

<h2>Published factors, and the burden that comes with them</h2>

<p>At the bottom of the ladder sit the industry studies: tables published by trade and professional bodies giving expected productivity losses for various disruption factors &#8212; congestion, out-of-sequence working, extended hours, and so on.</p>

<p>They are widely used. They are also stretched, routinely, past anything they can support.</p>

""" + FIG2 + """

<p>The rule is unambiguous and it is the thing most reports skip: a contractor relying on these studies has to establish that they are relevant to this job. Not that they exist, nor that they're respected &#8212; that they apply here.</p>

<p>That means knowing whose projects were studied, in what sector, in what country and in what era, and being able to say why those resemble yours. It means knowing what the study actually measured, because the factor being quoted is often not quite the factor that was tested. And it means having read it, rather than citing a figure that has been passed between reports until it acquired authority by repetition alone.</p>

<p>There is a discipline point underneath all of that which applies well beyond this subject. If you cannot check a number, do not publish it. A percentage in your claim that you can't trace to a source you've personally read is a liability sitting inside your own document, and the person who finds it will use it to characterise everything else you wrote.</p>

<h2>Adjustments that are not optional</h2>

<p>Whichever rung you land on, three corrections have to be made or the figure is indefensible.</p>

<p>Test the underlying data first. Productivity, progress and change records all have to be internally consistent before anything is calculated from them, and frequently they aren't.</p>

<p>Apply the loss only to the trade and the period actually disrupted. A factor derived for one operation, applied across an entire project because it is easier, is the single commonest way these claims are inflated and then dismissed.</p>

<p>And adjust for the learning curve. Early output is always lower, and a comparison that ignores it is measuring the shape of every construction operation ever run rather than the effect of anybody's interference.</p>

<h2>The loss that no single change contains</h2>

<p>One category deserves naming because it explains why so many disruption claims feel unprovable even when everybody agrees something went wrong.</p>

<p>Individually, each variation was priced and settled. Forty of them were, over eighteen months, and every one was agreed at the time. What none of those valuations captured is the effect of there having been forty &#8212; the constant resequencing, the crews who never settled into a rhythm, the supervision absorbed by administering change instead of running work.</p>

<p>That cumulative effect is real, it isn't inside any of the individual settlements, and it can't be recovered by reopening them. It has to be claimed separately, which is precisely why it lands on the weaker rungs of the ladder: there is no single event to point at and no clean period, because the whole job was like that.</p>

<p>Two things follow. Say so at the time, in writing, when agreeing each variation &#8212; that the price covers the direct work and not the cumulative effect. And expect the argument to be about whether the effect exists at all, rather than about its size.</p>

<h2>When to measure it</h2>

""" + FIG3 + """

<p>There is an awkward timing problem that nobody enjoys.</p>

<p>Lost productivity is best measured once the project is finished, because that is when the actual data exists. Trying to total it while the work is still being disrupted is frequently impossible &#8212; you are forecasting the remainder of something whose end you cannot see.</p>

<p>Employers, understandably, dislike claims that arrive at the end. And contracts usually require notice long before then, which is the whole subject of <a href="contract-week-10.html">Contract Week 10</a>.</p>

<p>The reconciliation is a sentence rather than a technique. If you have to put a figure forward while the impacts are still happening, state clearly that it is incomplete, that it is an estimate of continuing effects, and that you reserve the balance. Without that reservation an interim number can quietly become a ceiling &#8212; and in some circumstances a reservation that was never expressed cannot simply be assumed to have been implied.</p>

<h2>Practical insight</h2>

<p>Take whichever disruption claim is live on your job and work out, honestly, which rung of the ladder it is standing on.</p>

<p>Then ask what it would take to move up one. Often the answer's smaller than expected: a clean four-week period that exists in the timesheets but has never been extracted, or a subcontractor's returns that could still be requested while the relationship is intact.</p>

<p>One rung is worth a great deal. The difference between a claim benchmarked against your own site and one benchmarked against a published table is not a matter of presentation &#8212; it changes what the argument is about, from what happened here to whether somebody else's average applies.</p>

<p>And if you cannot move up, say which rung you are on in the report itself. An analyst who states plainly that no clean period was available, explains why, and then uses the next best method has produced something defensible. One who presents a published factor as though it were a measurement has produced something that will be taken apart.</p>

<h2>Key takeaways</h2>

<p>&#10004; Most jobs cannot produce a clean measured mile, and what remains is a ranked ladder of weaker alternatives.</p>

<p>&#10004; Each rung moves the benchmark further from your site and gives the other side something new to dispute.</p>

<p>&#10004; Work sampling keeps the observation on your own job but can only be done while the work is still running.</p>

<p>&#10004; The modified total cost approach concedes your own inefficiency and estimating error first, and still puts your tender on trial.</p>

<p>&#10004; Published factors carry a burden of relevance: you must show the studies apply to this job, not merely that they exist.</p>

<p>&#10004; Never publish a figure you cannot trace to a source you have read, and never apply a factor beyond the trade and period disrupted.</p>

<p>&#10004; Productivity loss is best measured after the event; if you must submit early, reserve the balance in writing.</p>

<p>&#10004; The cumulative effect of many settled variations sits outside all of them, and has to be reserved when each one is agreed.</p>

<h2>What&#39;s coming next</h2>

<p>There is one more rung below everything described here, and it is the one contractors reach for when the records will not support any of the above: present the whole overrun, attribute it to the other side, and invite them to disprove it. Next week is the global claim &#8212; why it is discouraged everywhere, why it keeps being made anyway, and the narrow circumstances in which it has survived.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 22 &#183; Global and total cost claims &#183; coming soon</span>
                                    <h4>The claim that asks the tribunal to guess</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Best Proof Is Your Own Site &#8212; The Project Control Hub</title>",
                  "<title>Everything After The Mile Is Weaker &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Best Proof Is Your Own Site | The Project Control Hub"',
                  'content="Everything After The Mile Is Weaker | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-20.html", "claim-week-21.html")
    s = s.replace('<span>Week 20<span class="crumb-title"> &#183; The measured mile</span></span>',
                  '<span>Week 21<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 20",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 21", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jul 19, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jul 19, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week21.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 20", "claim-week-20.html", PREV_TITLE):
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
    if 'href="claim-week-21.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 21 &#183; Productivity loss &#183; coming soon</span>\n'
            '                                    <h4>Everything after the mile is weaker</h4>',
            '<span class="next-week-tag">Week 21 &#183; Productivity loss</span>\n'
            '                                    <h4>Everything after the mile is weaker.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-21.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 21" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 21, title: "Productivity loss — the methods used when no clean mile exists",\n'
           '          short: "Productivity loss", status: "upcoming" },')
    new = ('        { n: 21, title: "Productivity loss — the methods used when no clean mile exists",\n'
           '          short: "Productivity loss", status: "live", page: "claim-week-21.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 21 live (%s)" % DATE)
    elif 'page: "claim-week-21.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 21 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-21.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-21.html</loc>\n"
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
