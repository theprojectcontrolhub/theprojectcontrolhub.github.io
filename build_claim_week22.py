#!/usr/bin/env python3
"""claim-week-22.html — Track 5, hafta 22. Faz E kapanisi. Sablon: claim-week-21.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-21.html", "claim-week-22.html"
PREV_TITLE = "Everything after the mile is weaker."
TITLE = "The claim that asks the tribunal to guess."
CRUMB = "Global and total cost claims"
DATE = "Aug 2, 2028"
WEEK_N = 22
DESC = ("Planned spend against actual spend, with the difference claimed as somebody else&#39;s "
        "fault. Five conditions have to be met for it to succeed in full, and the fifth one is "
        "almost never true. Claims &amp; Delay Analysis Week 22.")
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
<svg viewBox="0 0 640 246" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE CLAIM, SEVERAL NAMES</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">renaming it does not change what a reviewer is being asked to accept</text>
<rect x="34" y="60" width="180" height="30" rx="6" fill="#94a3b8" opacity="0.14" stroke="#cbd5e1"/>
<text x="124" y="80" text-anchor="middle" fill="#64748b" font-size="10.5">total cost claim</text>
<rect x="228" y="60" width="180" height="30" rx="6" fill="#94a3b8" opacity="0.14" stroke="#cbd5e1"/>
<text x="318" y="80" text-anchor="middle" fill="#64748b" font-size="10.5">rolled-up claim</text>
<rect x="422" y="60" width="184" height="30" rx="6" fill="#94a3b8" opacity="0.14" stroke="#cbd5e1"/>
<text x="514" y="80" text-anchor="middle" fill="#64748b" font-size="10.5">cumulative effect</text>
<rect x="126" y="104" width="388" height="30" rx="6" fill="#94a3b8" opacity="0.14" stroke="#cbd5e1"/>
<text x="320" y="124" text-anchor="middle" fill="#64748b" font-size="10.5">death by a thousand cuts</text>
<rect x="34" y="152" width="572" height="76" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="174" fill="#64748b" font-size="10.5" font-weight="600">What each of them is:</text>
<text x="54" y="196" fill="#64748b" font-size="10.5">compensation sought for a group of employer risk events, without showing the link</text>
<text x="54" y="214" fill="#64748b" font-size="10.5">between the loss claimed and any one of those events individually.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Packaging a total cost claim under a different heading is common and fools nobody who has seen one before.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 268" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FIVE CONDITIONS FOR IT TO SUCCEED IN FULL</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four are arguable; the last one almost never is</text>
<rect x="34" y="60" width="572" height="34" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5">1 &#183; the tender was reasonable</text>
<rect x="34" y="100" width="572" height="34" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="122" fill="#64748b" font-size="10.5">2 &#183; the actual cost was reasonable</text>
<rect x="34" y="140" width="572" height="34" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="162" fill="#64748b" font-size="10.5">3 &#183; every event contributing to the loss is compensable</text>
<rect x="34" y="180" width="572" height="34" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="202" fill="#64748b" font-size="10.5">4 &#183; there was no other way of calculating the figure</text>
<rect x="34" y="220" width="572" height="38" rx="8" fill="#b91c1c" opacity="0.10" stroke="#fca5a5"/>
<text x="54" y="243" fill="#b91c1c" font-size="10.5" font-weight="700">5 &#183; the contractor contributed to the increased cost in no way at all</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Not that your contribution was small. Not that it was outweighed. None, anywhere, across the whole job.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FAILING GLOBALLY IS NOT ALWAYS FAILING ENTIRELY</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">a lifeline, and a very poor thing to rely on</text>
<rect x="34" y="60" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">WHAT THE COURTS HAVE SAID</text>
<text x="54" y="98" fill="#475569" font-size="10.5">the global claim may fail and the evidence may still support individual links, or a rational</text>
<text x="54" y="110" fill="#475569" font-size="10">apportionment of part of the loss to the events the other party is responsible for</text>
<rect x="34" y="126" width="572" height="52" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="146" fill="#64748b" font-size="10.5" font-weight="700">WHY THAT IS NOT A STRATEGY</text>
<text x="54" y="164" fill="#64748b" font-size="10.5">the salvage depends on evidence you would have had to gather anyway &#8212; and if you had</text>
<text x="54" y="176" fill="#64748b" font-size="10">gathered it, you would not have brought the claim this way in the first place</text>
<rect x="34" y="190" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="211" fill="#64748b" font-size="10.5">Delay and disruption loss has to be proved as a matter of fact. There is no shortcut in the sentence.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Planning to be rescued by partial apportionment is planning to spend two years arguing for a fraction.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The claim that asks the tribunal to guess.</h2>

<p>In its simplest form it is a subtraction anybody can do. Here is what we expected to spend on labour. Here is what we actually spent. The difference is what your disruption cost us.</p>

<p>That is the total cost claim, and it is the bottom rung of the ladder from last week. It sits there for a reason: it is what remains when the records cannot support anything above it.</p>

""" + FIG1 + """

<p>It arrives under several names. Total cost, rolled up, cumulative effect, and the one the industry uses when it wants to be honest about the shape of the thing &#8212; death by a thousand cuts. The packaging varies. What's being asked for doesn't: compensation for a group of employer risk events, without demonstrating a link between the loss claimed and any one of those events on its own.</p>

<p>That absent link is the whole objection. Every other technique in this track is an attempt to build it.</p>

<h2>Why anybody still makes one</h2>

<p>It'd be easy to treat this as a lazy claim, and mostly that's wrong.</p>

<p>Last week described the cumulative effect problem: a hundred instructions, each priced and settled, whose combined disturbance sits outside all of them. The disruptive effect of any single one may genuinely have been negligible. Nobody could've priced it discretely at the time, and reopening the settlements isn't available.</p>

<p>So the contractor faces a real loss with no route to attribute it, and the global claim is what that looks like when it is written down. It is a claim of last resort made by people who have run out of alternatives, not usually by people who could not be bothered.</p>

<p>Which is a reason for sympathy and not a reason it succeeds.</p>

<h2>Five conditions</h2>

""" + FIG2 + """

<p>The commentary sets out what has to be established before this kind of claim can be recovered in full, and it runs to five parts: the tender was reasonable, the actual cost was reasonable, every event contributing to the loss is compensable, no other method of arriving at the figure was available, and the contractor added nothing whatever to the increased cost.</p>

<p>The first four are arguable. On this job the first is even unusually answerable &#8212; <a href="cost-week-3.html">Cost &amp; Cash Week 3</a> built the estimate in the open, indirects and all, which is more than most contractors can offer.</p>

<p>The fifth ends it. Not that your contribution was minor, or outweighed, or concurrent. None, anywhere, across the entire job. Week 13 met the same proposition in the total time version of the delay claim, and it is no more true here. On a project long enough and troubled enough to produce a global claim, the contractor has always contributed something, and the other side needs to find only one thing.</p>

<h2>What it silently assumes</h2>

<p>Underneath the arithmetic is an assumption nobody states.</p>

<p>The approach takes it as given that the excess over the tender allowance was produced by the employer's risk events in aggregate. Unless it is modified, it makes no allowance whatever for cost caused by things that are nobody's fault but yours: poor site management, plant that broke down, plant that was the wrong choice, labour that was short, weather that was bad.</p>

<p>All of those are in the total. None of them's deducted. The claim asks the reader to assume they were not there, which is why the objection to it is never really about the calculation.</p>

<h2>The modified version, and what it cannot get rid of</h2>

<p>The respectable form is the top-down or modified total cost claim, and Week 21 introduced it. Start from the total differential, then subtract every discrete cost you can identify &#8212; your own culpable costs first, and any employer-caused costs already recovered elsewhere &#8212; and claim what is left.</p>

<p>Doing that genuinely blunts the standard defence. A claim that has already deducted your own failures is much harder to characterise as a demand that somebody else pay for everything.</p>

<p>But there's a residue that won't go away. Some portion always remains unallocated to any individual event, because if it could be allocated it would have been. That remainder is the global claim in miniature, and it attracts every objection the full version does &#8212; just for a smaller number.</p>

<p>The alternative direction is bottom-up: build the value event by event. It is more work and much stronger, and it has a hazard of its own worth naming, which is double counting. The same hours can easily appear in a variation account, a prolongation claim and a disruption claim, and finding that overlap is one of the first things a competent reviewer does.</p>

<h2>What the courts have actually done</h2>

""" + FIG3 + """

<p>Two threads are worth knowing, and neither is as encouraging as it first sounds.</p>

<p>The first is that loss of this kind has to be proved as a matter of fact. An English decision put the burden in three limbs that will now be familiar: events occurred that entitle you to loss and expense, those events caused delay or disruption, and that delay or disruption caused you to incur the loss. Week 2 built this track's version of the same chain. No global presentation removes any of the three.</p>

<p>The second is more hopeful. A Scottish decision confirmed that the logic of a global claim requires every contributing event to be compensable &#8212; and then observed that although the global claim might fail, the evidence could still support finding causal links between individual losses and individual events, or a rational apportionment of part of the loss to the events the other party was responsible for. The claim was allowed to proceed. The same case supported the dominant cause approach Week 2 described.</p>

<p>Read the second as a lifeline rather than a plan. What rescues the claim is exactly the discrete evidence that would have made a global presentation unnecessary. Relying on it means spending two years arguing for a fraction of a number you could have proved properly.</p>

<h2>Practical insight</h2>

<p>If a global claim is being drafted on your job, do one thing before it goes out: try to build the bottom-up version for the three largest components, and see how far you get.</p>

<p>Sometimes the answer is surprising. Two of the three turn out to be attributable after all, once somebody actually looks, and the global claim shrinks to the one component that genuinely cannot be broken down. That is a completely different document to defend.</p>

<p>Where it is unavoidable, present it as what it is. Say plainly that discrete attribution was not possible and why, show the deductions you have made for your own contribution, and put the strongest discrete evidence you do have at the front rather than folding it into the total.</p>

<p>And on a live job, the instruction is simpler. The reason global claims exist is that nobody recorded the effect of each change at the time. That record is a line on a variation instruction, and it costs nothing this month.</p>

<h2>Key takeaways</h2>

<p>&#10004; A total cost claim compares planned spend to actual spend and attributes the difference to the other side.</p>

<p>&#10004; Total cost, rolled up, cumulative effect and death by a thousand cuts are the same claim under different headings.</p>

<p>&#10004; The defining feature is the missing link between the loss and any individual employer risk event.</p>

<p>&#10004; Five conditions must hold for it to succeed in full, and the fifth &#8212; no contractor contribution at all &#8212; is almost never true.</p>

<p>&#10004; Unmodified, it silently includes costs caused by your own management, plant, labour and the weather.</p>

<p>&#10004; The modified top-down version deducts what it can and still leaves an unallocated residue that attracts the same objections.</p>

<p>&#10004; A failed global claim can sometimes be salvaged in part &#8212; but only by the discrete evidence that would have made it unnecessary.</p>

<h2>What&#39;s coming next</h2>

<p>That closes disruption, and with it every argument about what happened. What remains is the money: putting a number on the time you have established you are owed. The next phase starts with the most-claimed and least-examined figure in the subject &#8212; the cost of the site simply staying open, which on this job runs at $7,100 a month and is not, as the following week will show, anything like as simple as multiplying it out.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 23 &#183; Prolongation &#183; coming soon</span>
                                    <h4>Time has a daily rate</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Everything After The Mile Is Weaker &#8212; The Project Control Hub</title>",
                  "<title>The Claim That Asks The Tribunal To Guess &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Everything After The Mile Is Weaker | The Project Control Hub"',
                  'content="The Claim That Asks The Tribunal To Guess | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-21.html", "claim-week-22.html")
    s = s.replace('<span>Week 21<span class="crumb-title"> &#183; Productivity loss</span></span>',
                  '<span>Week 22<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 21",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 22", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jul 26, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jul 26, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week22.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 21", "claim-week-21.html", PREV_TITLE):
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
    if 'href="claim-week-22.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 22 &#183; Global and total cost claims &#183; coming soon</span>\n'
            '                                    <h4>The claim that asks the tribunal to guess</h4>',
            '<span class="next-week-tag">Week 22 &#183; Global and total cost claims</span>\n'
            '                                    <h4>The claim that asks the tribunal to guess.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-22.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 22" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 22, title: "Global and total cost claims — why they fail",\n'
           '          short: "Global and total cost claims", status: "upcoming" },')
    new = ('        { n: 22, title: "Global and total cost claims — why they fail",\n'
           '          short: "Global and total cost claims", status: "live", page: "claim-week-22.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 22 live (%s)" % DATE)
    elif 'page: "claim-week-22.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 22 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-22.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-22.html</loc>\n"
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
