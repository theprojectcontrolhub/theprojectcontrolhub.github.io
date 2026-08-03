#!/usr/bin/env python3
"""claim-week-20.html — Track 5, hafta 20. Sablon: claim-week-19.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-19.html", "claim-week-20.html"
PREV_TITLE = "On time, and losing money."
TITLE = "The best proof is your own site."
CRUMB = "The measured mile"
DATE = "Jul 19, 2028"
WEEK_N = 20
DESC = ("Compare the hours and output of a clean stretch of your own work against a disrupted one. "
        "The technique the guidance points to first, why it removes your estimate from the "
        "argument, and the two things that kill it in practice. Claims &amp; Delay Analysis Week 20.")
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
<svg viewBox="0 0 640 254" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE WHOLE TECHNIQUE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">two periods of your own work, two sets of hours, one comparison</text>
<rect x="34" y="60" width="272" height="112" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE CLEAN STRETCH</text>
<text x="54" y="104" fill="#475569" font-size="10">nothing in the way, normal working</text>
<text x="54" y="124" fill="#475569" font-size="10">hours booked &#183; output achieved</text>
<text x="54" y="150" fill="#059669" font-size="10" font-weight="600">this is the mile</text>
<rect x="322" y="60" width="284" height="112" rx="10" fill="#b91c1c" opacity="0.08" stroke="#fca5a5"/>
<text x="342" y="82" fill="#b91c1c" font-size="10.5" font-weight="700">THE DISRUPTED STRETCH</text>
<text x="342" y="104" fill="#475569" font-size="10">same work, same crews, obstructed</text>
<text x="342" y="124" fill="#475569" font-size="10">hours booked &#183; output achieved</text>
<text x="342" y="150" fill="#b91c1c" font-size="10" font-weight="600">more effort, same product</text>
<rect x="34" y="186" width="572" height="52" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="208" fill="#64748b" font-size="10.5">The difference in effort per unit of output is the loss. No estimate appears anywhere in it,</text>
<text x="54" y="226" fill="#64748b" font-size="10.5">which is precisely why it is harder to attack than anything else available.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Endorsed by the industry guidance and accepted in US federal courts. The idea is simple; the work is in choosing the mile.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 234" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">CHOOSING THE CLEAN PERIOD</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four ways to pick one that will not survive being questioned</text>
<rect x="34" y="60" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="78" fill="#64748b" font-size="10.5" font-weight="700">NOT LIKE FOR LIKE</text>
<text x="54" y="93" fill="#64748b" font-size="10.5">different part of the works, different conditions, different gang &#8212; not a comparison at all</text>
<rect x="34" y="106" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="124" fill="#64748b" font-size="10.5" font-weight="700">TAKEN DURING THE LEARNING CURVE</text>
<text x="54" y="139" fill="#64748b" font-size="10.5">the first weeks are always slow; using them flatters the disrupted period</text>
<rect x="34" y="152" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="170" fill="#64748b" font-size="10.5" font-weight="700">CARRYING YOUR OWN INEFFICIENCY</text>
<text x="54" y="185" fill="#64748b" font-size="10.5">a mile that was itself badly run understates the loss and invites the whole thing to be reopened</text>
<rect x="34" y="198" width="572" height="30" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="218" fill="#475569" font-size="10.5">The strongest mile is the same trade, on the same element, before the interference started.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Choosing the mile is the analysis. Everything after it is arithmetic.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO THINGS THAT KILL IT IN PRACTICE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">neither is analytical, and both are decided long before the claim</text>
<rect x="34" y="60" width="572" height="58" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="80" fill="#64748b" font-size="10.5" font-weight="700">THE RECORD STANDARD</text>
<text x="54" y="98" fill="#64748b" font-size="10.5">proving output per trade, week by week, needs record-keeping closer to a factory work study</text>
<text x="54" y="112" fill="#94a3b8" font-size="10">than to anything a construction site normally produces</text>
<rect x="34" y="128" width="572" height="58" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="148" fill="#64748b" font-size="10.5" font-weight="700">SOMEBODY ELSE HAS THE RECORDS</text>
<text x="54" y="166" fill="#64748b" font-size="10.5">the productivity data that would prove the case usually sits with your subcontractors</text>
<text x="54" y="180" fill="#94a3b8" font-size="10">and there is no reason they will hand it over unless the subcontract says so</text>
<text x="320" y="212" text-anchor="middle" fill="#94a3b8" font-size="10.5">The second one is a drafting problem, which means it is solvable before anybody signs anything.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Most failed measured miles fail here, not on the arithmetic.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The best proof is your own site.</h2>

<p>Week 19 ended with a problem. Disruption always costs money, there is no network to calculate it in, and the loss accumulates across a hundred mornings nobody wrote a letter about. So how do you prove any of it?</p>

<p>The answer the guidance reaches for first is disarmingly simple. Find a stretch of the same work, done by the same people, during a period when nothing was in their way. Measure what it took. Then measure what the same work took while the interference was going on.</p>

<p>The clean stretch is the measured mile. The difference in effort between it and the disrupted period is the loss.</p>

""" + FIG1 + """

<h2>Why it beats everything else</h2>

<p>Week 6 set out a ladder: your own work measured, then your own estimate, then somebody else's published studies, each rung weaker than the one above. This technique is the top rung, and the reason is worth stating precisely.</p>

<p>It removes your estimate from the argument entirely.</p>

<p>Every other route ends up litigating whether your tender was any good. Compare outturn against allowance and the response is immediate: you underpriced it. That argument can run for a very long time and it isn't one you can win with certainty, because your allowance is a document you wrote in your own interest.</p>

<p>A measured mile has no allowance in it. Both halves of the comparison are what actually happened, on the same site, with the same crews and the same supervision. The other side cannot attack the benchmark by attacking your commercial judgement, because your commercial judgement never entered the calculation.</p>

<p>The approach is endorsed by the industry protocol and has been accepted in the US federal courts, but its real strength is that structural one.</p>

<h2>Choosing the mile is the analysis</h2>

""" + FIG2 + """

<p>Everything after the choice of period is arithmetic. The choice itself is where the work is, and where a competent opponent will spend all their time.</p>

<p>Compare like with like. The same trade, on a similar part of the works, doing comparable work. A mile taken from a different element under different conditions is not a comparison; it's two unrelated numbers with a division sign between them.</p>

<p>Avoid the learning curve. The opening weeks of any operation are slow while the gang works out the sequence and the details. Using that period as your benchmark makes the disrupted period look better than it was, which sounds like an error in your favour and is really a gift to the other side when they find it.</p>

<p>And be honest about your own performance in the mile. If the clean period was itself badly run, the comparison understates the loss &#8212; but far worse, once that is exposed the entire selection looks arbitrary and everything built on it goes with it.</p>

<h2>Your data decides your precision</h2>

<p>This is the discipline most often abandoned, and it is a matter of intellectual honesty rather than technique.</p>

<p>The quality of your records fixes how finely you are allowed to analyse. Weekly labour returns alongside weekly progress figures let you measure efficiency week by week. If the only reliable measure of progress is the monthly payment application, then monthly is the limit, and any attempt to go finer is inventing precision the data cannot support.</p>

<p>Where assumptions are needed to push beyond what the records hold, say so plainly and present a range rather than a single figure. An analyst who states the assumption and shows what happens if it is wrong is doing the job. One who buries it inside a decimal point is producing something that looks stronger and is considerably weaker.</p>

<h2>Two things that kill it</h2>

""" + FIG3 + """

<p>Neither of these is analytical, and both are settled long before anybody thinks about a claim.</p>

<p>The first is the standard of record required. To show confidently that a tradesman achieved a given output during a clean period, and then to show accurately what he achieved while disrupted, calls for record-keeping closer to a factory work study than to what a building site normally produces. That's a high bar, and it's the honest reason measured mile analyses are rarer than the enthusiasm for them suggests.</p>

<p>The second is more solvable and more often fatal. The records that would demonstrate productivity are usually kept by the subcontractors doing the work, not by the main contractor. They aren't yours, nobody has to give them to you, and by the time you want them the subcontract is finished and the relationship may not be warm.</p>

<h2>The clause that fixes half of it</h2>

<p>The subcontractor problem is a drafting problem, which means it can be solved with a paragraph before anybody starts.</p>

<p>A subcontract that requires weekly labour allocation returns, by activity and location, in a stated format, as a condition of payment, produces the data as a matter of routine. It costs the subcontractor a few minutes a week, it costs you nothing, and it turns a claim you can't prove into one you can.</p>

<p><a href="contract-week-8.html">Contract Week 8</a> argued that entitlement is built long before anybody decides to claim. The same argument runs down the chain: a right you hold under the main contract, with no matching obligation in the subcontract beneath it, is a right you cannot actually evidence.</p>

<h2>Where this job's mile already sits</h2>

<p>Worth noticing that the structure of a measured mile is present in the piling on this job without anybody constructing it.</p>

<p>There are forty-two piles. Seventeen of them are in the northern half where the rock was found, which leaves twenty-five in the south where the ground behaved as the site investigation suggested. The southern piles are a clean stretch of the same work, by the same rig and the same gang, immediately before the interference.</p>

<p>One honest qualification, because it matters. <a href="risk-week-5.html">Risk Week 5</a> priced the rock directly, at $2,850 per affected pile, and that figure is compensation for the additional work of dealing with it. A measured mile on the same seventeen piles would be capturing productivity loss, and running both without care would be charging twice for one event.</p>

<p>Which is the real lesson of the example. The measured mile earns its place where no direct pricing exists &#8212; the trades working around the rig, the follow-on work in a congested area, the crews who lost their run while the northern half was being resolved. That loss hasn't a rate against it anywhere, and this technique is the only way it ever gets recovered.</p>

<h2>Practical insight</h2>

<p>Pick the trade with the most hours on your job and ask one question of your records: could you identify a four-week period this year when that trade had a clean run?</p>

<p>If you can, find the hours booked in those four weeks and the quantity of work completed. That ratio is your baseline productivity, and it took an hour to establish.</p>

<p>Now do the same for a four-week period you would describe as disrupted. If the two ratios differ materially, you have the beginning of a real claim built entirely from documents that already exist.</p>

<p>And if you cannot identify the clean period at all &#8212; because nothing distinguishes one month's hours from another's in your system &#8212; that is this week's finding. The fix is a column on a form, and it has to happen before the disrupted period you will want to prove.</p>

<h2>Key takeaways</h2>

<p>&#10004; The measured mile compares hours and output from a clean stretch of your own work against a disrupted one.</p>

<p>&#10004; Its structural strength is that no estimate appears in it, so the other side cannot attack your tender instead of your evidence.</p>

<p>&#10004; Choosing the comparison period is the analysis; everything after it is arithmetic.</p>

<p>&#10004; Compare the same trade on similar work, avoid the learning curve, and be honest about how well the clean period was run.</p>

<p>&#10004; The precision of your records fixes the precision you are entitled to claim; going finer is inventing accuracy.</p>

<p>&#10004; The record standard needed is closer to a work study than to normal site practice, which is why good miles are rare.</p>

<p>&#10004; The productivity records usually belong to your subcontractors, and only the subcontract can make them yours.</p>

<h2>What&#39;s coming next</h2>

<p>Most jobs cannot produce a clean mile. There is no undisrupted period, or the records cannot show one, or the work was never repetitive enough for the comparison to mean anything. Next week is what remains: the alternative methods, the published factors, and an honest account of how much weaker each one is than the technique it replaces.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 21 &#183; Productivity loss &#183; coming soon</span>
                                    <h4>Everything after the mile is weaker</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>On Time, And Losing Money &#8212; The Project Control Hub</title>",
                  "<title>The Best Proof Is Your Own Site &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="On Time, And Losing Money | The Project Control Hub"',
                  'content="The Best Proof Is Your Own Site | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-19.html", "claim-week-20.html")
    s = s.replace('<span>Week 19<span class="crumb-title"> &#183; Disruption</span></span>',
                  '<span>Week 20<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 19",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 20", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jul 12, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jul 12, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week20.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 19", "claim-week-19.html", PREV_TITLE):
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
    if 'href="claim-week-20.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 20 &#183; The measured mile &#183; coming soon</span>\n'
            '                                    <h4>The best proof is your own site</h4>',
            '<span class="next-week-tag">Week 20 &#183; The measured mile</span>\n'
            '                                    <h4>The best proof is your own site.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-20.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 20" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 20, title: "The measured mile — comparing the job to itself",\n'
           '          short: "The measured mile", status: "upcoming" },')
    new = ('        { n: 20, title: "The measured mile — comparing the job to itself",\n'
           '          short: "The measured mile", status: "live", page: "claim-week-20.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 20 live (%s)" % DATE)
    elif 'page: "claim-week-20.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 20 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-20.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-20.html</loc>\n"
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
