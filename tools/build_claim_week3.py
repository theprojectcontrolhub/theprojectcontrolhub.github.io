#!/usr/bin/env python3
"""claim-week-3.html — Track 5, hafta 3. Sablon: claim-week-2.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-2.html", "claim-week-3.html"
PREV_TITLE = "Blame is not causation."
TITLE = "Not every delay is worth money."
CRUMB = "Types of delay"
DATE = "Mar 22, 2028"
DESC = ("Three lost fortnights on the same job, three different answers. Excusable, compensable, "
        "or neither &#8212; and why the same rock is a claim under one FIDIC book and nothing at all "
        "under another. Claims &amp; Delay Analysis Week 3.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO QUESTIONS, THREE OUTCOMES</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">excusable decides the time; compensable decides the money</text>
<rect x="34" y="62" width="186" height="120" rx="10" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="127" y="88" text-anchor="middle" fill="#059669" font-size="10.5" font-weight="700">TIME AND MONEY</text>
<text x="127" y="112" text-anchor="middle" fill="#475569" font-size="10">excusable and</text>
<text x="127" y="128" text-anchor="middle" fill="#475569" font-size="10">compensable</text>
<text x="127" y="154" text-anchor="middle" fill="#64748b" font-size="10">the rock, a variation,</text>
<text x="127" y="170" text-anchor="middle" fill="#64748b" font-size="10">employer prevention</text>
<rect x="228" y="62" width="186" height="120" rx="10" fill="#059669" opacity="0.05" stroke="#a7f3d0"/>
<text x="321" y="88" text-anchor="middle" fill="#059669" font-size="10.5" font-weight="700">TIME ONLY</text>
<text x="321" y="112" text-anchor="middle" fill="#475569" font-size="10">excusable but not</text>
<text x="321" y="128" text-anchor="middle" fill="#475569" font-size="10">compensable</text>
<text x="321" y="154" text-anchor="middle" fill="#64748b" font-size="10">exceptionally adverse</text>
<text x="321" y="170" text-anchor="middle" fill="#64748b" font-size="10">climatic conditions</text>
<rect x="422" y="62" width="184" height="120" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="514" y="88" text-anchor="middle" fill="#64748b" font-size="10.5" font-weight="700">NEITHER</text>
<text x="514" y="112" text-anchor="middle" fill="#64748b" font-size="10">not excusable</text>
<text x="514" y="128" text-anchor="middle" fill="#64748b" font-size="10">at all</text>
<text x="514" y="154" text-anchor="middle" fill="#64748b" font-size="10">your subcontractor,</text>
<text x="514" y="170" text-anchor="middle" fill="#64748b" font-size="10">your rework, your rig</text>
<rect x="34" y="196" width="572" height="48" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="218" fill="#64748b" font-size="10.5">The middle column is the one that surprises people. The delay is real, the excuse is good,</text>
<text x="54" y="236" fill="#64748b" font-size="10.5">the completion date moves &#8212; and you carry every dollar of the extra time yourself.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Two independent questions. Answering the first one well tells you nothing about the second.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE FILTER, AND ITS ORDER</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">three gates, and the first one is not in the contract at all</text>
<rect x="34" y="60" width="572" height="48" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">1 &#183; WAS IT CRITICAL?</text>
<text x="54" y="100" fill="#475569" font-size="10.5">decided by the programme &#8212; a delay to an activity with float stops here, whatever caused it</text>
<rect x="34" y="118" width="572" height="48" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="140" fill="#059669" font-size="10.5" font-weight="700">2 &#183; WAS IT EXCUSABLE?</text>
<text x="54" y="158" fill="#475569" font-size="10.5">decided by the clause &#8212; if yes, the completion date moves and the damages stop</text>
<rect x="34" y="176" width="572" height="48" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="198" fill="#059669" font-size="10.5" font-weight="700">3 &#183; WAS IT COMPENSABLE?</text>
<text x="54" y="216" fill="#475569" font-size="10.5">decided by a different clause &#8212; and a great many excusable delays never reach this gate</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Most arguments start at gate two. The party that starts at gate one usually wins them.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 246" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE ROCK, THREE CONTRACTS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">same ground, same $48,450, and the classification changes with the cover of the book</text>
<rect x="34" y="60" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">RED &amp; YELLOW &#183; 4.12 UNFORESEEABLE PHYSICAL CONDITIONS</text>
<text x="54" y="100" fill="#475569" font-size="10.5">sub-surface conditions are named &#8212; entitlement to EOT and to Cost, subject to the claims clause</text>
<rect x="34" y="122" width="572" height="52" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="144" fill="#64748b" font-size="10.5" font-weight="700">SILVER &#183; NO SUCH SUB-CLAUSE</text>
<text x="54" y="162" fill="#64748b" font-size="10.5">4.10 and 4.11 push the other way &#8212; site data used, price deemed sufficient &#8212; and 4.12 is narrower</text>
<rect x="34" y="184" width="572" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="210" fill="#64748b" font-size="10.5">Nothing about the ground changed. The risk moved, and with it the whole of the claim.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Before asking what the rock is worth, find out which book the job was let under.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Not every delay is worth money.</h2>

<p>Take three fortnights on the same job. In the first, the rig sits idle because the ground is harder than anybody expected. In the second, it rains for eleven days out of fourteen and nothing can be poured. In the third, your piling subcontractor's crew doesn't turn up because he has put them on a better-paying job across town.</p>

<p>All three are real. All three cost the same to sit through. All three delay completion by a fortnight.</p>

<p>And they are worth completely different amounts, because the contract asks two separate questions about each of them and only one of those questions is about whose fault it was.</p>

<h2>Two questions, three outcomes</h2>

<p>The first question is whether the delay is <strong>excusable</strong> &#8212; does it move the completion date, so that delay damages stop running against you? The second is whether it is <strong>compensable</strong> &#8212; does anybody have to pay you for the extra time?</p>

<p>They're independent, and that is the whole of this week.</p>

""" + FIG1 + """

<p>The middle column is where the money quietly disappears. The delay is genuine, the entitlement is real, the completion date moves and the liquidated damages stop. And you fund every day of it out of your own margin.</p>

<h2>The rock: time and money, but not profit</h2>

<p>Under the 2017 Red Book, ground conditions have their own sub-clause. Physical conditions are defined to include sub-surface and hydrological conditions, and where they were Unforeseeable and the contractor has followed the notice procedure, the entitlement is to extension of time and to payment of Cost.</p>

<p>Read that last word carefully, because it is a defined term and the definition does the damage. Cost means expenditure reasonably incurred, including overheads &#8212; and it expressly does not include profit.</p>

<p>So a fully successful rock claim gets your $48,450 back and leaves you exactly where you started. The same work valued as a variation, at rates, would have carried your markup. The difference between those two routes is real money, and it is decided by which sub-clause the claim travels under &#8212; a point <a href="contract-week-13.html">Contract Week 13</a> spent a whole article on.</p>

<h2>The weather: time, and nothing else</h2>

<p>Exceptionally adverse climatic conditions appear in the extension of time clause. They are defined against the site data the employer provided and against published climatic data for the location, which is a harder test than it sounds &#8212; unusual is not the same as Unforeseeable.</p>

<p>Pass that test and you get the time. There is no route to the money, and the drafting makes sure of it: the ground conditions sub-clause defines physical conditions to exclude climatic conditions at the site and their effects. The clause that pays is closed to weather by its own definition.</p>

<p>Eleven wet days in fourteen, therefore, buys you a fortnight on the completion date and a fortnight of preliminaries at $7,100 a month out of your own pocket.</p>

<h2>The word both tests hang on</h2>

<p>Read the ground clause and the weather clause together and the same term is doing the work in both: <em>Unforeseeable</em>. It is defined, and the definition is narrower than the ordinary meaning.</p>

<p>What it asks is whether an experienced contractor could have seen the thing coming &#8212; and it fixes that judgement at the Base Date, which is itself defined and lands twenty-eight days before tenders were due.</p>

<p>Three things follow from that, and each one moves money.</p>

<p>The judgement is made as at tender time, not at the moment the rig hits the rock. What you learned during construction doesn't come into it. The standard is an experienced contractor rather than you specifically, so being new to the region is not an argument. And it is judged against what was available then, which on this job means the site investigation and the boreholes.</p>

<p><a href="risk-week-5.html">Risk Week 5</a> wrote the register entry that decides this before anybody knew it mattered: the southern ratio was measured, and nothing evidenced the northern half. That silence is the argument. If the tender documents gave an experienced contractor no basis for expecting the ground to change, the rock is Unforeseeable and the clause opens. If they gave enough to raise the question, it doesn't.</p>

<p>The classification of a delay three years into a job is therefore decided by a document assembled a month before anybody signed anything.</p>

<h2>Your own delay: neither, and worse</h2>

<p>The absent subcontractor is the easy one. It isn't excusable, so the completion date does not move and delay damages keep running. It isn't compensable, so nobody pays for the fortnight.</p>

<p>What is less obvious is what it does to the other two. A period of your own culpable delay sitting alongside an employer delay is the beginning of the hardest argument in this track, and it is why the third fortnight can quietly destroy the value of the first.</p>

<p>It also changes how the first fortnight reads. An employer looking at a job that is already late for the contractor's own reasons has an obvious answer to any claim that arrives afterwards, and the answer costs nothing to give: you'd have been late anyway. Refuting that takes a delay analysis. Avoiding the need to refute it takes a programme that shows, at the time, which delay was driving.</p>

<h2>Criticality comes first</h2>

<p>All of this assumes the delay reached the completion date at all. Week 2 pulled the word <em>caused</em> apart into four links, and the classification above only starts working at the far end of that chain.</p>

""" + FIG2 + """

<p>Gate one is not in the contract. It is in the programme, and it is answered by <a href="week-13.html">Schedule Week 13</a>'s arithmetic rather than by any clause. A fortnight lost on an activity carrying three weeks of float is worth nothing under every column of the grid above, and and no amount of good drafting rescues it.</p>

<h2>The same rock, in three books</h2>

<p>Here is the part that unsettles people who learned one contract form and assumed it was the subject.</p>

""" + FIG3 + """

<p>The Silver Book has no unforeseeable physical conditions sub-clause at all. What occupies that part of the contract instead pushes in the opposite direction: the contractor is taken to have used the data it was given, the accepted price is treated as covering everything the works require, and the only relief on offer is for difficulties of a narrower kind. The ground risk has been moved onto the contractor deliberately, because that is what the Silver Book is for.</p>

<p>Same rock. Same seventeen piles at $2,850. Under one book it is a claim for time and Cost; under another it is a number you absorb, and the net margin of $48,163 absorbs it. Nothing about the geology changed, and nothing about your costs did either.</p>

<p>Which is why the first question in any delay classification is not <em>what happened</em>. It is <em>which contract</em>.</p>

<h2>Practical insight</h2>

<p>Take the delay register or the extension of time log on your current job, and put three columns beside it: critical, excusable, compensable.</p>

<p>Fill them in with yes, no, or a question mark. Be honest about the question marks &#8212; they are the useful output. Most registers, done this way, produce a column of confident entries in the first field and a row of question marks in the third, which tells you exactly where the argument will be.</p>

<p>Then find the sub-clause number for every entry marked compensable. Not the category, the number. If you can't put a number against it, you have an expectation rather than an entitlement, and the difference will only surface at the point where it is too late to fix.</p>

<p>And do it once for the form you are actually on, not the form you learned. The rock proves the point: the same event, priced identically, is a claim in one book and a cost in another.</p>

<h2>Key takeaways</h2>

<p>&#10004; Excusable and compensable are two independent questions; a delay can move the completion date and still cost you everything.</p>

<p>&#10004; Time-only delays are where margin disappears quietly, because the entitlement looks like a win.</p>

<p>&#10004; Ground conditions under the Red and Yellow Books give time and Cost &#8212; and Cost is defined to exclude profit.</p>

<p>&#10004; A successful cost claim leaves you level, not ahead; the same work as a variation would have carried your markup.</p>

<p>&#10004; Exceptionally adverse weather buys time and no money, and the drafting closes the paying clause to it deliberately.</p>

<p>&#10004; Criticality is the first gate and it lives in the programme, not in the contract; a delay with float fails every column.</p>

<p>&#10004; The Silver Book has no unforeseeable physical conditions clause at all, so classification starts with which form you signed.</p>

<h2>What&#39;s coming next</h2>

<p>Gate one has now been assumed twice. Next week it stops being an assumption: what critical actually means once a job is running, why the critical path moves while you are looking away, and who owns the float that decides all of it &#8212; the question that turns friendly on paper and expensive in practice.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 4 &#183; Criticality and float &#183; coming soon</span>
                                    <h4>Everything turns on what was critical</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Blame Is Not Causation &#8212; The Project Control Hub</title>",
                  "<title>Not Every Delay Is Worth Money &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Blame Is Not Causation | The Project Control Hub"',
                  'content="Not Every Delay Is Worth Money | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-2.html", "claim-week-3.html")
    s = s.replace('<span>Week 2<span class="crumb-title"> &#183; Cause and effect</span></span>',
                  '<span>Week 3<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 2",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 3", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Mar 15, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Mar 15, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="3"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week3.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 2", "claim-week-2.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-3.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 3 &#183; Types of delay &#183; coming soon</span>\n'
            '                                    <h4>Not every delay is worth money</h4>',
            '<span class="next-week-tag">Week 3 &#183; Types of delay</span>\n'
            '                                    <h4>Not every delay is worth money.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-3.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 3" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 3, title: "Types of delay — excusable, compensable and the ones that pay nothing",\n'
           '          short: "Types of delay", status: "upcoming" },')
    new = ('        { n: 3, title: "Types of delay — excusable, compensable and the ones that pay nothing",\n'
           '          short: "Types of delay", status: "live", page: "claim-week-3.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 3 live (%s)" % DATE)
    elif 'page: "claim-week-3.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 3 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-3.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-3.html</loc>\n"
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
