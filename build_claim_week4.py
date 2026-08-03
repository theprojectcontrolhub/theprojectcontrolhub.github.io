#!/usr/bin/env python3
"""claim-week-4.html — Track 5, hafta 4. Sablon: claim-week-3.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-3.html", "claim-week-4.html"
PREV_TITLE = "Not every delay is worth money."
TITLE = "Everything turns on what was critical."
CRUMB = "Criticality and float"
DATE = "Mar 29, 2028"
DESC = ("FIDIC uses the word float exactly once in the whole book, and never says who owns it. "
        "Total float, free float, the path that moves while you are looking away, and the spare "
        "time both sides think is theirs. Claims &amp; Delay Analysis Week 4.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO KINDS OF SPARE TIME</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">one of them belongs to the activity, the other belongs to the whole path</text>
<rect x="34" y="64" width="130" height="26" rx="5" fill="#059669" opacity="0.8"/>
<text x="99" y="82" text-anchor="middle" fill="#fff" font-size="10" font-weight="600">Ducting</text>
<rect x="176" y="64" width="118" height="26" rx="5" fill="#059669" opacity="0.8"/>
<text x="235" y="82" text-anchor="middle" fill="#fff" font-size="10" font-weight="600">Cable pull</text>
<rect x="294" y="64" width="52" height="26" rx="5" fill="#94a3b8" opacity="0.35"/>
<text x="320" y="82" text-anchor="middle" fill="#475569" font-size="9">free</text>
<rect x="346" y="64" width="122" height="26" rx="5" fill="#94a3b8" opacity="0.22"/>
<text x="407" y="82" text-anchor="middle" fill="#64748b" font-size="9">more total float</text>
<text x="34" y="112" fill="#64748b" font-size="10.5">Free float: what ducting can absorb before the cable pull has to move.</text>
<text x="34" y="132" fill="#64748b" font-size="10.5">Total float: what the whole path can absorb before the completion date has to move.</text>
<rect x="34" y="152" width="572" height="34" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="174" fill="#059669" font-size="10.5" font-weight="600">A claim for time runs on total float. Nothing else reaches the completion date.</text>
<rect x="34" y="196" width="572" height="46" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="218" fill="#64748b" font-size="10.5">Free float is still worth arguing about, because using it up is how a contractor absorbs</text>
<text x="54" y="236" fill="#64748b" font-size="10.5">its own problems &#8212; and how it loses the ability to absorb the next one.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Two numbers, two meanings. A register that records only one of them has recorded the less useful one.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHO OWNS THE SPARE TIME</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">three positions, argued for decades, and no clause in the contract to settle them</text>
<rect x="34" y="60" width="186" height="122" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="127" y="84" text-anchor="middle" fill="#059669" font-size="10.5" font-weight="700">THE CONTRACTOR</text>
<text x="127" y="108" text-anchor="middle" fill="#475569" font-size="10">it built the programme</text>
<text x="127" y="126" text-anchor="middle" fill="#475569" font-size="10">and carries the fixed date</text>
<text x="127" y="152" text-anchor="middle" fill="#64748b" font-size="10">so the float is its own</text>
<text x="127" y="170" text-anchor="middle" fill="#64748b" font-size="10">contingency to spend</text>
<rect x="228" y="60" width="186" height="122" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="321" y="84" text-anchor="middle" fill="#64748b" font-size="10.5" font-weight="700">THE EMPLOYER</text>
<text x="321" y="108" text-anchor="middle" fill="#64748b" font-size="10">it is paying for a date,</text>
<text x="321" y="126" text-anchor="middle" fill="#64748b" font-size="10">not for a sequence</text>
<text x="321" y="152" text-anchor="middle" fill="#64748b" font-size="10">so spare time before</text>
<text x="321" y="170" text-anchor="middle" fill="#64748b" font-size="10">that date is available</text>
<rect x="422" y="60" width="184" height="122" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="514" y="84" text-anchor="middle" fill="#64748b" font-size="10.5" font-weight="700">THE PROJECT</text>
<text x="514" y="108" text-anchor="middle" fill="#64748b" font-size="10">nobody owns it;</text>
<text x="514" y="126" text-anchor="middle" fill="#64748b" font-size="10">it is consumed in turn</text>
<text x="514" y="152" text-anchor="middle" fill="#64748b" font-size="10">whoever needs it first</text>
<text x="514" y="170" text-anchor="middle" fill="#64748b" font-size="10">gets the use of it</text>
<rect x="34" y="196" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="218" fill="#64748b" font-size="10.5">Whichever you believe, the other side believes one of the other two &#8212; and neither of you wrote it down.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The third position is the one that operates in practice, because it is what happens when nobody has agreed the first two.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 226" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT THE PROGRAMME HAS TO DISCLOSE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">two contract families, two very different questions asked of the same bar chart</text>
<rect x="34" y="62" width="572" height="60" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="84" fill="#059669" font-size="10.5" font-weight="700">FIDIC 2017</text>
<text x="54" y="102" fill="#475569" font-size="10.5">show the float, if any, and the critical path or paths</text>
<text x="54" y="118" fill="#94a3b8" font-size="10">and then nothing &#8212; no rule about who may use it, or what happens when it is gone</text>
<rect x="34" y="132" width="572" height="76" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="154" fill="#059669" font-size="10.5" font-weight="700">NEC</text>
<text x="54" y="172" fill="#475569" font-size="10.5">show the float, and separately show the time risk allowances inside your durations</text>
<text x="54" y="190" fill="#475569" font-size="10.5">delay is measured against planned completion, so the tail end of the float stays yours</text>
<text x="54" y="204" fill="#94a3b8" font-size="10">the contingency is named, disclosed and protected rather than left to be argued</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">One family asks you to reveal your contingency. The other asks you to reveal it, and then declines to take it off you.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Everything turns on what was critical.</h2>

<p>Three weeks of this track have leaned on the same unexamined word. Week 2 put criticality in the middle of the causal chain and called it the link most claims assume. Week 3 made it gate one, ahead of the contract entirely. It is time to stop assuming it.</p>

<p>Here is why it carries so much: a delay to an activity with spare time costs the completion date nothing. Not less &#8212; nothing. The event was real, the cost was real, the crew stood there, and the claim for time is worth zero. Criticality is the switch between a claim and a bad week.</p>

<h2>Two kinds of spare time</h2>

<p><a href="week-13.html">Schedule Week 13</a> built the arithmetic. What changes here is what the arithmetic is for: in Track 1 float was a planning output, and in this track it is evidence.</p>

""" + FIG1 + """

<p>The distinction matters in an argument because the two numbers answer different questions. Free float is what an activity can absorb before it disturbs the next one. Total float is what the path can absorb before the completion date moves.</p>

<p>A claim for time lives entirely on total float. But free float is where a job quietly spends its resilience, and a contractor who has burned it on its own rework has no cushion left when the employer's delay arrives.</p>

<h2>What the contract says about float</h2>

<p>Almost nothing, and the size of that silence is worth measuring.</p>

<p>In the whole of the 2017 Red Book, the word float appears exactly once. It sits in the list of things the programme has to show: the activities, logically linked, with their early and late dates, the float if any, and the critical path or paths.</p>

<p>That is the entire treatment. The contract requires you to disclose your spare time. It does not say who may spend it, what happens when it runs out, or whether an employer delay that eats three weeks of float has caused anything at all.</p>

<p>Notice the plural, too. The contract contemplates critical <em>paths</em>, which is a more honest picture than the single red line most people carry in their heads.</p>

<h2>Three answers, and no clause</h2>

<p>Because the contract is silent, the question has been argued for decades, and three positions hold the field.</p>

""" + FIG2 + """

<p>The contractor's case is the strongest on its own terms: it built the programme, it sequenced the work to suit its own resources, and it carries the risk of a fixed completion date. On that reading the float is priced contingency, and it belongs to the party that priced it. The NEC family broadly accepts this.</p>

<p>The employer's case is simpler: it is buying a date, not a sequence, and any spare time sitting in front of that date is part of what it bought.</p>

<p>The third position &#8212; that float belongs to the project and is consumed by whoever reaches it first &#8212; is not really a principle. It is a description of what happens when nobody has settled the other two, which is most of the time.</p>

<h2>The other family asks a harder question</h2>

""" + FIG3 + """

<p>The NEC programme has to show float, and separately has to show <em>time risk allowances</em>: the padding built into durations for matters at the contractor's own risk. Most people meeting that requirement for the first time find it uncomfortable, because it asks you to write down the thing every planner keeps in their head.</p>

<p>In exchange the contractor gets something FIDIC does not offer. Delay from a compensation event is assessed against planned completion rather than against the contract completion date, so float at the tail of the programme stays with the contractor instead of being absorbed silently. The contingency is named, disclosed, and then protected.</p>

<h2>The path moves while you are looking away</h2>

<p>The deeper problem is that criticality isn't a property of an activity. It is a property of an activity <em>at a moment</em>, and it changes.</p>

<p>Take the forty-one days from <a href="contract-week-1.html">Contract Week 1</a> and suppose the piling path was driving on the day the rock was found, with the services path carrying thirty days of float behind it. For thirty days the rock delays completion day for day. On the thirty-first, the services path runs out of slack and becomes critical too.</p>

<p>From that point the job has two driving paths, and the last eleven days of the delay are being caused by both of them at once. Nobody did anything wrong on day thirty-one. The arithmetic changed, and with it the answer to who caused the delay.</p>

<p>There is a second version of the same trap, and it is more common. The critical path in the baseline and the critical path the job actually ran on are two different objects, and they are rarely the same by the end. Piling can drive the programme on paper and be overtaken in practice by a cladding package that slipped quietly for four months. An analysis built on the as-planned path is answering a question about the plan; an analysis built on the as-built path is answering one about the job. Both are legitimate methods, and they can produce different numbers from identical facts &#8212; which is the subject the middle of this track exists for.</p>

<p>This is why an analysis that identifies the critical path once, at the start, and then applies it to the whole job produces confident numbers that are wrong. It is also the mechanism behind the hardest argument in this track, which arrives in the phase on the hard problems.</p>

<h2>Your float disclosure is an admission</h2>

<p>One practical consequence, and it catches people.</p>

<p>The programme you submitted shows float. It was accepted, or it was not objected to within the period, which under <a href="contract-week-11.html">Contract Week 11</a> comes to much the same thing. That float is now a statement you made, in a contractual document, about how much spare time your sequence contained.</p>

<p>When you later claim that a two-week employer delay put you two weeks late, the first thing a competent reviewer does is open your own programme and look for the slack you disclosed. If it shows three weeks of total float on that path, your claim is arguing against your own submission.</p>

<h2>Practical insight</h2>

<p>Open your current accepted programme and write down two numbers: the total float on the path you are most worried about, and the number of separate paths within ten days of critical.</p>

<p>The second number is the one nobody has. If it is one, you have a straightforward job and an easy analysis ahead of you. If it is four, you do not really have a critical path &#8212; you have a critical band, and any delay of more than a few days will land in two places at once.</p>

<p>Then do it again next month and compare. What you're looking for isn't the float value; it's the rate at which it is disappearing, and who has been spending it. A path that lost twelve days of float in a month where nothing went visibly wrong is telling you something the progress report isn't.</p>

<p>Record the answer each month, in a document with a date on it. Float that was measured contemporaneously is evidence. Float reconstructed two years later is an argument, and it will be met with another one.</p>

<h2>Key takeaways</h2>

<p>&#10004; A delay to an activity with total float costs the completion date nothing, whatever it cost you.</p>

<p>&#10004; Free float and total float answer different questions; a claim for time runs on total float alone.</p>

<p>&#10004; FIDIC uses the word float once, in the list of things the programme must show, and never says who owns it.</p>

<p>&#10004; Three ownership positions compete &#8212; contractor, employer, project &#8212; and the third one wins by default when nobody agrees the first two.</p>

<p>&#10004; NEC asks for time risk allowances to be disclosed separately, and in exchange leaves terminal float with the contractor.</p>

<p>&#10004; Criticality belongs to a moment, not to an activity: paths become critical as their float runs out, without anybody doing anything.</p>

<p>&#10004; The float you disclosed is a statement you made, and it will be read back to you before your own analysis is.</p>

<h2>What&#39;s coming next</h2>

<p>That closes the first phase. You now know what a claim has to prove, what it means to say an event caused something, which delays are worth money, and what criticality actually is. Everything from here runs on evidence rather than principle, and the next phase starts where all of it starts: the as-planned programme, and whether the baseline you are about to analyse can survive being looked at closely.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 5 &#183; The as-planned programme &#183; coming soon</span>
                                    <h4>You cannot analyse what you cannot trust</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Not Every Delay Is Worth Money &#8212; The Project Control Hub</title>",
                  "<title>Everything Turns On What Was Critical &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Not Every Delay Is Worth Money | The Project Control Hub"',
                  'content="Everything Turns On What Was Critical | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-3.html", "claim-week-4.html")
    s = s.replace('<span>Week 3<span class="crumb-title"> &#183; Types of delay</span></span>',
                  '<span>Week 4<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 3",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 4", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Mar 22, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Mar 22, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="4"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week4.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 3", "claim-week-3.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-4.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 4 &#183; Criticality and float &#183; coming soon</span>\n'
            '                                    <h4>Everything turns on what was critical</h4>',
            '<span class="next-week-tag">Week 4 &#183; Criticality and float</span>\n'
            '                                    <h4>Everything turns on what was critical.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-4.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 4" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 4, title: "Criticality and float — what every claim actually argues about",\n'
           '          short: "Criticality and float", status: "upcoming" },')
    new = ('        { n: 4, title: "Criticality and float — what every claim actually argues about",\n'
           '          short: "Criticality and float", status: "live", page: "claim-week-4.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 4 live (%s)" % DATE)
    elif 'page: "claim-week-4.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 4 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-4.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-4.html</loc>\n"
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
