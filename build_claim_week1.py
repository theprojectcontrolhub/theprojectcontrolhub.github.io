#!/usr/bin/env python3
"""claim-week-1.html — Track 5 birinci hafta.

Şablon: contract-week-20.html (§7.1). Idempotent: ikinci çalıştırma no-op.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC = "contract-week-20.html"
DST = "claim-week-1.html"
DATE = "Mar 8, 2028"
CHANGED = []


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    # Sürüm damgası her koşuda değişebilir; karşılaştırmada onu nötrle,
    # yoksa yeniden üretilen sayfa hep "değişti" görünür ve cache boşuna artar.
    def norm(x):
        return re.sub(r"\?v=\d+", "?v=N", x)
    if os.path.exists(p) and norm(read(p)) == norm(s):
        return
    io.open(p, "w", encoding="utf-8").write(s)
    CHANGED.append(p)


TITLE = "The notice held. Now price it."
CRUMB = "Claims fundamentals"
DESC = ("The rock is worth $48,450 and the net margin on the job is $48,163. This time the notice "
        "was served in time, so the entitlement survives &#8212; and the argument moves to the "
        "question four tracks have never answered. Claims &amp; Delay Analysis Week 1.")
DESC_PLAIN = DESC.replace("&amp;", "&")

FIG1 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 268" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE TWO HALVES OF A CLAIM</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">they are answered from different places, and they fail independently</text>
<rect x="34" y="60" width="278" height="180" rx="10" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="84" fill="#64748b" font-size="10.5" font-weight="700">ENTITLEMENT &#183; TRACK 4</text>
<text x="54" y="108" fill="#475569" font-size="10.5">Does the contract give a right here?</text>
<text x="54" y="128" fill="#475569" font-size="10.5">Was it kept alive?</text>
<text x="54" y="156" fill="#64748b" font-size="10.5" font-weight="600">Answered from documents</text>
<text x="54" y="176" fill="#64748b" font-size="10.5">the clause, the notice, the file</text>
<text x="54" y="208" fill="#64748b" font-size="10.5" font-weight="600">Fails on:</text>
<text x="54" y="226" fill="#64748b" font-size="10.5">a period missed, a record never kept</text>
<rect x="328" y="60" width="278" height="180" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="84" fill="#059669" font-size="10.5" font-weight="700">QUANTUM &#183; TRACK 5</text>
<text x="348" y="108" fill="#475569" font-size="10.5">How much time?</text>
<text x="348" y="128" fill="#475569" font-size="10.5">How much money?</text>
<text x="348" y="156" fill="#059669" font-size="10.5" font-weight="600">Answered from a comparison</text>
<text x="348" y="176" fill="#475569" font-size="10.5">this job against a job that never ran</text>
<text x="348" y="208" fill="#059669" font-size="10.5" font-weight="600">Fails on:</text>
<text x="348" y="226" fill="#475569" font-size="10.5">a method the records cannot support</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">An engineer who has never lost a claim on entitlement can still lose the whole of it on the right-hand box.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE CHAIN, AND WHERE IT BREAKS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four links, each with its own evidence &#8212; the claim is only as good as the weakest</text>
<rect x="26" y="66" width="132" height="58" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="92" y="90" text-anchor="middle" fill="#64748b" font-size="11" font-weight="700">CAUSE</text>
<text x="92" y="110" text-anchor="middle" fill="#64748b" font-size="10">the event</text>
<rect x="182" y="66" width="132" height="58" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="248" y="90" text-anchor="middle" fill="#64748b" font-size="11" font-weight="700">EFFECT</text>
<text x="248" y="110" text-anchor="middle" fill="#64748b" font-size="10">what it moved</text>
<rect x="338" y="66" width="132" height="58" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="404" y="90" text-anchor="middle" fill="#64748b" font-size="11" font-weight="700">ENTITLEMENT</text>
<text x="404" y="110" text-anchor="middle" fill="#64748b" font-size="10">the clause that pays</text>
<rect x="494" y="66" width="120" height="58" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="554" y="90" text-anchor="middle" fill="#059669" font-size="11" font-weight="700">QUANTUM</text>
<text x="554" y="110" text-anchor="middle" fill="#059669" font-size="10">the number</text>
<text x="170" y="100" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="326" y="100" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="482" y="100" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="92" y="152" text-anchor="middle" fill="#94a3b8" font-size="9.5">site records</text>
<text x="248" y="152" text-anchor="middle" fill="#94a3b8" font-size="9.5">the programme</text>
<text x="404" y="152" text-anchor="middle" fill="#94a3b8" font-size="9.5">the contract</text>
<text x="554" y="152" text-anchor="middle" fill="#94a3b8" font-size="9.5">cost ledger</text>
<rect x="26" y="176" width="588" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="46" y="202" fill="#64748b" font-size="10.5">Track 4 closed the first three links. This track is the fourth &#8212; and the fourth is where most claims are actually lost.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Each link is proved from a different place, which is why one strong link rescues nothing.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 252" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE EVENT, TWO CLAIMS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same rock, priced twice, by two different tests</text>
<rect x="34" y="62" width="572" height="56" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="84" fill="#059669" font-size="10.5" font-weight="700">MONEY &#183; THE WORK ITSELF</text>
<text x="54" y="104" fill="#475569" font-size="10.5">17 of 42 piles at $2,850 &#8212; $48,450, and the register says the northern half is unevidenced</text>
<rect x="34" y="128" width="572" height="56" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="150" fill="#059669" font-size="10.5" font-weight="700">TIME &#183; THE SITE STAYING OPEN</text>
<text x="54" y="170" fill="#475569" font-size="10.5">preliminaries run at $7,100 a month, so the delay is priced by its length, not by its cause</text>
<rect x="34" y="194" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="220" fill="#64748b" font-size="10.5">Net margin on the job: $48,163. Either claim alone is larger than what the job was built to earn.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Two claims, two tests, two sets of evidence. Winning one proves nothing about the other.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The notice held. Now price it.</h2>

<p>Four tracks have circled the same rock. <a href="risk-week-5.html">Risk Week 5</a> priced it at $48,450 &#8212; seventeen of forty-two piles at $2,850 each &#8212; and said plainly that the figure was conditional, because nothing evidenced what the northern half of the site was made of. <a href="risk-week-14.html">Risk Week 14</a> asked whose risk it was. <a href="contract-week-13.html">Contract Week 13</a> asked whether the contract even calls it a variation. And <a href="contract-week-1.html">Contract Week 1</a> opened on an email that was never a notice, and on a commercial manager who found out forty-one days after the event.</p>

<p>This track changes one fact and leaves everything else alone. The notice was served: inside the period, in the form the contract requires, to the person named in the Contract Data. Everything <a href="contract-week-10.html">Contract Week 10</a> warned about was avoided. The right survived.</p>

<p>That's not the end of the argument. It is the start of a different one, and a harder one.</p>

<h2>What the last track handed over</h2>

<p>Three things, and the whole of this track runs on all three.</p>

<p><strong>A preserved right.</strong> The notice is in, the records exist, and nobody can argue your entitlement away on a technicality.</p>

<p><strong>A programme that can be re-run.</strong> Track 1 built it. <a href="contract-week-11.html">Contract Week 11</a> made it a contractual document, with a deemed no-objection at twenty-one days on the initial submission and fourteen on a revision. An unobjected programme is the Programme, and that matters more here than it did there: every method in this track needs a plan it is allowed to call the plan.</p>

<p><strong>A question.</strong> <a href="contract-week-9.html">Contract Week 9</a> sets out the test for an extension of time and stops, deliberately, before measuring anything. <a href="contract-week-8.html">Contract Week 8</a> builds entitlement before a claim exists. Neither one says how much.</p>

<h2>Two questions, and only one of them is answered</h2>

<p>Every claim has two halves, and they fail independently of each other.</p>

<p>The first is entitlement. Does the contract give you a right in these circumstances, and did you do what was needed to keep it alive? It is a question about documents, and you answer it by reading a clause and a file. That is the whole of the previous track.</p>

<p>The second is quantum. How much time, and how much money? It is not a question about documents at all. It is a question about a project that never happened.</p>

""" + FIG1 + """

<p>The asymmetry is worth sitting with. An engineer who has never lost a claim on entitlement can still lose the entire value of one on quantum, and that's the more common way to lose.</p>

<h2>The comparison nobody can observe</h2>

<p>Here is the difficulty in one sentence. To say what the rock cost, you have to say what would have happened without it &#8212; and that job was never built.</p>

<p>Entitlement has a document to point at. Quantum has only a comparison, and one side of the comparison doesn't exist. Every method in this track is an attempt to construct that missing side from something: a baseline programme, a set of updates, an as-built record, a stretch of undisrupted work on the same site. The methods differ in what they borrow and what they assume, and that is precisely why two competent analysts reach two different numbers from one set of facts.</p>

<p>So the question that governs this track is not which method is best. It is which method your records will carry.</p>

<h2>What a claim actually has to prove</h2>

<p>Four links, and each is proved from somewhere different.</p>

""" + FIG2 + """

<p>Cause is an event, evidenced from site records. Effect is movement in the programme, evidenced from the programme itself. Entitlement is the clause that turns that movement into a right, and Track 4 covered it. Quantum is the number, and it is evidenced from the cost ledger that <a href="cost-week-10.html">Cost &amp; Cash Week 10</a> built.</p>

<p>A claim is only as strong as its weakest link, which is why a beautifully argued clause rescues nothing when your as-built record is a set of monthly photographs.</p>

<h2>Time and money are two claims, not one</h2>

<p>The rock generates both, and they're assessed by different tests.</p>

<p>The money claim is for the work itself: the piles that had to be redrilled, priced from what was actually spent. The time claim is for the site staying open longer, and it is priced by length rather than by cause. Preliminaries on this job run at $7,100 a month &#8212; $85,200 spread across a twelve-month programme &#8212; and that clock runs whether the delay came from rock, rain or a late drawing.</p>

""" + FIG3 + """

<p>They can also come apart completely. You can finish on the original completion date and still have lost a great deal of money, because you built it in a worse sequence with more people than the plan assumed. There's no extension of time in that story at all. That is disruption, and it has its own half of this track.</p>

<h2>Forty-one days, and the shape of the problem</h2>

<p>Contract Week 1 established that the commercial manager found out forty-one days after the event. Read as a delay rather than as a governance failure, that number shows you the shape of everything this track has to do.</p>

<p>Forty-one days of what? Of the rock delaying the piling, if piling was driving the completion date at the time. Of nothing at all, if the piling had float and something else was driving. Of some part of the forty-one, if the driving path changed halfway through &#8212; which, on a real job, it usually does.</p>

<p>Those three answers are not opinions. They are what three different analytical methods return, and each is defensible on the same facts.</p>

<h2>Why the margin is the whole argument</h2>

<p>Net margin on this job is $48,163, from <a href="cost-week-22.html">Cost &amp; Cash Week 22</a>. The conditional value of the rock is $48,450. The two numbers sit within three hundred dollars of each other, and that coincidence is the reason this track exists.</p>

<p>A claim that recovers in full leaves the job at roughly the margin it was priced to earn. A claim that recovers half of it turns a profitable job into a break-even one. A claim that fails on quantum having succeeded on entitlement leaves you holding a proven right worth nothing.</p>

<p>None of that is decided by how good your engineering was. It is decided by whether the records you kept eighteen months earlier can support a method that produces a number a reviewer can't take apart.</p>

<h2>Practical insight</h2>

<p>Take the last claim your organisation submitted, and find the sentence where it stops arguing about entitlement and starts arguing about amount.</p>

<p>That sentence is usually easy to find, because the register changes. The entitlement half cites clauses and dates. The quantum half starts citing rates, hours and comparisons. Mark it.</p>

<p>Now read only what comes after it, and ask one question of every number: what is this being compared with, and where did that comparison come from? If the answer is a baseline programme, check that it was the accepted one. If it is a rate, check that the rate is in the contract rather than in your estimate. If you can't find the comparison at all, you've found the reason the claim was negotiated down.</p>

<p>Do this before you need it. On the job you are running now, the records that will decide your next quantum argument are being created this week, by people who have no idea that's what they're doing.</p>

<h2>Key takeaways</h2>

<p>&#10004; Entitlement and quantum are separate halves of a claim, and a right that survives every time bar can still be worth nothing.</p>

<p>&#10004; Entitlement is answered from documents; quantum is answered from a comparison with a project that never ran.</p>

<p>&#10004; Every delay method is a way of constructing that missing comparison, which is why competent analysts disagree on the same facts.</p>

<p>&#10004; The method is chosen by the records you kept, not by the answer you prefer.</p>

<p>&#10004; A claim proves four links &#8212; cause, effect, entitlement, quantum &#8212; and each is evidenced from a different place.</p>

<p>&#10004; Time and money are two claims: the work costs what it costs, and the delay costs $7,100 a month regardless of what caused it.</p>

<p>&#10004; The rock is worth $48,450 against a net margin of $48,163, so the quantum argument is the whole commercial outcome of the job.</p>

<h2>What&#39;s coming next</h2>

<p>Before any of the methods, the chain has to close. Next week is cause and effect: what it means to say that an event caused a delay, why a list of things that went wrong is not a causal argument, and why the link most claims skip is the one between the two.</p>
"""

TAGS = ("""                            <div class="article-tags">
                            <span class="article-tag">#Claims</span>
                            <span class="article-tag">#DelayAnalysis</span>
                            <span class="article-tag">#Quantum</span>
                            <span class="article-tag">#ProjectControls</span>
                        </div>""")

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 2 &#183; Cause and effect &#183; coming soon</span>
                                    <h4>The chain a claim has to close</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(html_):
    t = re.sub(r"<[^>]+>", " ", html_)
    t = t.replace("&#8212;", " ").replace("&#10004;", " ").replace("&#39;", "'").replace("&amp;", "&")
    return len(t.split())


def build_page():
    s = read(SRC)

    # --- head / meta
    s = s.replace("<title>A Calendar of Obligations &#8212; The Project Control Hub</title>",
                  "<title>The Notice Held. Now Price It. &#8212; The Project Control Hub</title>", 1)
    s = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s">' % DESC_PLAIN, s, count=1)
    s = s.replace('href="https://theprojectcontrolhub.com/contract-week-20.html"',
                  'href="https://theprojectcontrolhub.com/claim-week-1.html"', 1)
    s = s.replace('content="A Calendar of Obligations | The Project Control Hub"',
                  'content="The Notice Held. Now Price It. | The Project Control Hub"')
    s = re.sub(r'<meta property="og:description" content="[^"]*">',
               '<meta property="og:description" content="%s">' % DESC_PLAIN, s, count=1)
    s = re.sub(r'<meta name="twitter:description" content="[^"]*">',
               '<meta name="twitter:description" content="%s">' % DESC_PLAIN, s, count=1)
    s = s.replace('content="https://theprojectcontrolhub.com/contract-week-20.html"',
                  'content="https://theprojectcontrolhub.com/claim-week-1.html"', 1)

    # --- breadcrumb
    s = s.replace('<a href="learn.html">Contract Management</a>',
                  '<a href="learn.html">Claims &amp; Delay Analysis</a>', 1)
    s = s.replace('<span>Week 20<span class="crumb-title"> &#183; A calendar of obligations</span></span>',
                  '<span>Week 1<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)

    # --- eyebrow (§7.2: önceki track adı sayfada kalmamalı)
    s = s.replace("MODULE 04 · CONTRACT MANAGEMENT · WEEK 20",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 1", 1)
    s = s.replace('<h1 class="article-title">Every clock in this contract is somebody&#39;s Tuesday.</h1>',
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP&reg; &#183; Mar 1, 2028", "PMP&reg; &#183; " + DATE)
    s = s.replace("PMP® · Mar 1, 2028", "PMP® · " + DATE)

    # --- gövde
    i = s.index('<div class="content-preview"', s.index("article-title"))
    i = s.index(">", i) + 1
    j = s.index("<!-- PAYWALL CTA -->")
    j = s.rindex("</div>", i, j)
    old_body = s[i:j]
    # okuma süresi: 225 wpm + figür başına 15 sn
    n = words(BODY)
    mins = max(1, round(n / 225 + 3 * 0.25))
    s = s[:i] + "\n" + BODY + "\n" + s[j:]
    s = re.sub(r"<i class='bx bx-time-five'></i> \d+ min read",
               "<i class='bx bx-time-five'></i> %d min read" % mins, s, count=1)

    # --- kuyruk
    s = re.sub(r'<div class="article-tags">.*?</div>', TAGS.strip(), s, count=1, flags=re.S)
    # MEVCUT KARTI KORU (bkz. diger build script'leri, 2026-07-27)
    card = NEXT_CARD
    if os.path.exists(DST):
        m = re.search(r'<div class="next-article" id="nextArticle".*?\n                        </div>',
                      read(DST), re.S)
        if m and 'href="learn.html"' not in m.group(0):
            card = m.group(0)
    s = re.sub(r'<div class="next-article" id="nextArticle".*?\n                        </div>\n',
               card + '\n', s, count=1, flags=re.S)
    s = s.replace("renderTrack4Sidebar", "renderTrack5Sidebar")
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="1"', s)

    # Paylaşım çubukları şablonun URL'sini ve başlığını taşıyor (§7.2).
    from urllib.parse import quote
    s = s.replace("contract-week-20.html", "claim-week-1.html")
    s = s.replace(quote("Every clock in this contract is somebody's Tuesday.", safe=""),
                  quote(TITLE, safe=""))
    s = s.replace("Every%20clock%20in%20this%20contract%20is%20somebody%27s%20Tuesday.",
                  quote(TITLE, safe=""))

    return s, n, mins


def main():
    print("\n  build_claim_week1.py — %s" % ROOT)
    page, n, mins = build_page()

    leftovers = [p for p in ("CONTRACT MANAGEMENT", "renderTrack4Sidebar", "contract-week-20.html")
                 if p in page]
    if leftovers:
        sys.exit("HATA: onceki track izi kaldi: %s" % leftovers)

    write(DST, page)
    print("  %-22s %d kelime, %d dk okuma" % (DST, n, mins))

    # önceki haftanın next-article kartı (§7.4)
    prev = read(SRC)
    if 'href="claim-week-1.html"' not in prev:
        prev = prev.replace(
            '<div class="next-article-label">Module 04 complete</div>\n'
            '                            <a href="learn.html" class="next-article-link">\n'
            '                                <div>\n'
            '                                    <span class="next-week-tag">Track 5 &#183; Claims &amp;'
            ' Delay Analysis &#183; coming soon</span>\n'
            '                                    <h4>What the entitlement is actually worth</h4>',
            '<div class="next-article-label">Module 04 complete</div>\n'
            '                            <a href="claim-week-1.html" class="next-article-link">\n'
            '                                <div>\n'
            '                                    <span class="next-week-tag">Track 5 &#183; Claims &amp;'
            ' Delay Analysis &#183; Week 1</span>\n'
            '                                    <h4>The notice held. Now price it.</h4>', 1)
        write(SRC, prev)
        print("  %-22s next-article karti claim-week-1'e baglandi" % SRC)

    # curriculum.js: 1. hafta live
    js = read("curriculum.js")
    old = ('        { phase: "Phase A — What a Claim Has to Prove", n: 1,\n'
           '          title: "Claims fundamentals — from preserved right to measured quantum",\n'
           '          short: "Claims fundamentals", status: "upcoming" },')
    new = ('        { phase: "Phase A — What a Claim Has to Prove", n: 1,\n'
           '          title: "Claims fundamentals — from preserved right to measured quantum",\n'
           '          short: "Claims fundamentals", status: "live", page: "claim-week-1.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 1 live (%s)" % DATE)
    elif 'page: "claim-week-1.html"' in js:
        print("  curriculum.js          hafta 1 zaten live")
    else:
        sys.exit("HATA: curriculum.js 1. hafta satiri beklenen halde degil")

    # sitemap
    sm = read("sitemap.xml")
    if "claim-week-1.html" not in sm:
        entry = ("  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-1.html</loc>\n"
                 "    <lastmod>2026-07-27</lastmod>\n  </url>\n")
        sm = sm.replace("</urlset>", entry + "</urlset>", 1)
        write("sitemap.xml", sm)
        print("  sitemap.xml            claim-week-1 eklendi")

    # cache bump — sadece gercekten degisiklik olduysa
    if CHANGED:
        cur = re.search(r"curriculum\.js\?v=(\d+)", read("index.html"))
        old_v, new_v = int(cur.group(1)), int(cur.group(1)) + 1
        cnt = 0
        for f in sorted(os.listdir(".")):
            if f.endswith(".html"):
                a = read(f)
                b = a.replace("curriculum.js?v=%d" % old_v, "curriculum.js?v=%d" % new_v)
                if a != b:
                    io.open(f, "w", encoding="utf-8").write(b)   # surum damgasi:
                    CHANGED.append(f)                            # normalize eden write() atlar
                    cnt += 1
        print("  cache                  v%d -> v%d (%d sayfa)" % (old_v, new_v, cnt))
    else:
        print("  cache                  degisiklik yok, bump atlandi")

    print("  tamam, %d dosya\n" % len(set(CHANGED)))


if __name__ == "__main__":
    main()
