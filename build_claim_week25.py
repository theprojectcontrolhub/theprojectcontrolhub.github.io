#!/usr/bin/env python3
"""claim-week-25.html — Track 5, hafta 25. Faz F kapanisi. Sablon: claim-week-24.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-24.html", "claim-week-25.html"
PREV_TITLE = "The cost that is not on site."
TITLE = "A number a stranger can rebuild."
CRUMB = "Pricing and substantiation"
DATE = "Aug 23, 2028"
WEEK_N = 25
DESC = ("The contract already defines what a claim is, in four parts, and the fourth is the money. "
        "How a figure travels from the cost ledger into a submission somebody else can verify "
        "&#8212; and why the coding decided it years ago. Claims &amp; Delay Analysis Week 25.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT THE CONTRACT SAYS A CLAIM IS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four components &#8212; and this track has been building them in order</text>
<rect x="34" y="60" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">A · WHAT HAPPENED</text>
<text x="54" y="94" fill="#475569" font-size="10.5">a detailed description of the event or circumstance behind the claim</text>
<rect x="34" y="108" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="126" fill="#059669" font-size="10.5" font-weight="700">B · WHY IT ENTITLES YOU</text>
<text x="54" y="142" fill="#475569" font-size="10.5">the contractual, and any other legal, basis relied on</text>
<rect x="34" y="156" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="174" fill="#059669" font-size="10.5" font-weight="700">C · THE RECORDS</text>
<text x="54" y="190" fill="#475569" font-size="10.5">every contemporary record the claim actually relies on</text>
<rect x="34" y="204" width="572" height="34" rx="8" fill="#059669" opacity="0.12" stroke="#10b981"/>
<text x="54" y="226" fill="#059669" font-size="10.5"><tspan font-weight="700">D · THE NUMBER</tspan> &#8212; detailed supporting particulars of the time and money claimed</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A is Phase B. B is the previous track. C is Weeks 6 to 8. D is this phase. The contract wrote the syllabus.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE COST CODE SETS THE CEILING</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">you cannot prove a figure finer than the code it was booked to</text>
<rect x="34" y="60" width="278" height="100" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">ONE CODE: PILING</text>
<text x="54" y="104" fill="#64748b" font-size="10">every hour, every pile, one bucket</text>
<text x="54" y="124" fill="#64748b" font-size="10">the northern rock and the southern</text>
<text x="54" y="142" fill="#64748b" font-size="10">clean run are the same number</text>
<rect x="328" y="60" width="278" height="100" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="82" fill="#059669" font-size="10.5" font-weight="700">CODED BY LOCATION</text>
<text x="348" y="104" fill="#475569" font-size="10">north and south booked separately</text>
<text x="348" y="124" fill="#475569" font-size="10">the comparison exists in the</text>
<text x="348" y="142" fill="#475569" font-size="10">ledger without anybody building it</text>
<rect x="34" y="174" width="572" height="44" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="194" fill="#64748b" font-size="10.5">The budget ties back to the estimate; the ledger compares against the budget. Whatever</text>
<text x="54" y="212" fill="#64748b" font-size="10.5">resolution that chain was set up with, three years ago, is the resolution you get.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The same lesson as the as-built level of detail, arriving from the accounting side of the job.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 234" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">ONE LINE, ALL THE WAY DOWN</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the test: a stranger with your files reaches your number without asking you anything</text>
<rect x="34" y="60" width="572" height="30" rx="6" fill="#059669" opacity="0.14" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">CLAIM TOTAL</text>
<rect x="70" y="96" width="536" height="30" rx="6" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="90" y="116" fill="#475569" font-size="10.5">head of claim &#8212; prolongation, thirty days</text>
<rect x="106" y="132" width="500" height="30" rx="6" fill="#059669" opacity="0.07" stroke="#a7f3d0"/>
<text x="126" y="152" fill="#475569" font-size="10.5">item &#8212; site supervision, March and April</text>
<rect x="142" y="168" width="464" height="30" rx="6" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="162" y="188" fill="#64748b" font-size="10.5">source &#8212; payroll ledger, cost code, dated, unamended</text>
<text x="320" y="222" text-anchor="middle" fill="#94a3b8" font-size="10.5">Any line that stops before the bottom row is the line the whole claim will be judged on.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Not most lines. Every line. The reviewer will find the one that doesn&#39;t reach the ledger.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">A number a stranger can rebuild.</h2>

<p>Six weeks of methods and two weeks of quantum produce a figure. Somebody now has to believe it, and the most common failure at this stage is not arriving at the wrong amount. It is being unable to show where the right one came from.</p>

<p>The test is simple to state and unforgiving to apply. Hand your files to somebody who was never on the job, with no access to you, and see whether they arrive at your number. If they cannot, you do not have a claim. You have an assertion with a spreadsheet attached.</p>

<h2>The contract already wrote the syllabus</h2>

<p>It's worth noticing that the contract doesn't leave this to taste. The 2017 Red Book defines what a fully detailed claim is, and it has four components.</p>

""" + FIG1 + """

<p>A description of the event. A statement of the contractual or other legal basis relied on. All the contemporary records the claim rests on. And detailed supporting particulars of the time and money being claimed.</p>

<p>Look at what this track has been doing. Phase B built the first. The previous track built the second. Weeks 6 through 8 built the third. This phase is the fourth. The structure was in the contract the whole time, which is a slightly humbling thing to notice at week twenty-five.</p>

<h2>Contemporary records, defined</h2>

<p>The contract also defines the term, and the definition is narrower than casual usage.</p>

<p>Contemporary records are those prepared or generated at the time of the event, or immediately afterwards. Not reconstructed, not compiled later from other documents &#8212; made then. The claiming party is obliged to keep whatever records are necessary to substantiate its claim, which places the burden squarely where Week 6 said it would land.</p>

<p>Two further details are worth knowing because they are frequently missed. The Engineer may monitor those records as they are kept, and may instruct that additional ones be kept. And doing either implies nothing at all &#8212; not acceptance of liability, and not acceptance that the records are accurate or complete.</p>

<p>So an Engineer who has watched you keep records for two years has conceded precisely nothing, and a contractor who's taken comfort from the absence of objection has misread the clause.</p>

<h2>Pricing before, or pricing after</h2>

<p>There are two moments at which changed work can be priced, and they behave differently.</p>

<p>Forward pricing agrees the number before the work is done. It's far better for everybody and the pace of construction routinely prevents it &#8212; the work has to proceed before anybody can agree what it is worth.</p>

<p>Which leaves post pricing, and the standard mechanism is to record what was actually spent: hours, materials and plant, captured as they happen. That works cleanly where the changed work can be segregated from the rest &#8212; a discrete instruction, a separate area, a gang that can be booked to its own code.</p>

<p>It stops working the moment the change can't be separated. Increase a pipe diameter and the consequence runs through multiple areas and several trades, none of which can be booked distinctly. At that point directly capturing the cost is not possible, and you are back in the disruption phase with all its difficulty. The distinction is worth recognising early, because it determines whether you are pricing a variation or building an argument.</p>

<h2>The code you set up decides what you can prove</h2>

""" + FIG2 + """

<p>Here is the structural point of this week, and it has appeared before in a different costume.</p>

<p>The budget ties back to the estimate. The cost system compares actual against budget. Whatever level of detail that chain was built at &#8212; before the job started, by somebody who was not thinking about claims &#8212; is the finest resolution available to you now.</p>

<p>On this job the illustration is exact. If piling was coded as one line, the seventeen northern piles through rock and the twenty-five clean southern ones are inside the same total, and the measured mile Week 20 identified cannot be extracted no matter how obvious it is that it exists. Code the same work by location and the comparison sits in the ledger without anybody constructing it.</p>

<p>Week 7 made this argument about the as-built programme: a coarse baseline caps the precision of everything downstream. This is the same constraint arriving through the accounting system, and it is decided at the same moment &#8212; the beginning.</p>

<h2>The burden, and the certificate</h2>

<p>Two things about substantiation that people underrate.</p>

<p>The burden sits with the party making the claim. Not with the Engineer to disprove it, not with the employer to investigate it. Yours.</p>

<p>And under some standard forms you are not merely submitting a figure &#8212; you are certifying it. You are signing to say the claim is honestly made, that nothing behind it has been left out or overstated, and that the sum asked for is genuinely the sum you are owed. That is a different kind of document to sign. It also means that a padded head of claim is not a negotiating position; it is a statement you have certified, and its discovery contaminates the rest.</p>

<h2>What a rebuildable number looks like</h2>

""" + FIG3 + """

<p>Every figure should descend through the same four levels: the claim total, the head it belongs to, the item within that head, and the source document behind the item.</p>

<p>The failures are always the same. A total that does not reconcile to the sum of its parts. An item that appears only in the claim and in no ledger anywhere. Hours with no timesheets. A rate with no derivation. An allocation percentage that nobody can explain the basis of.</p>

<p>None of those is fatal on its own. Their effect is cumulative and it is not about the money: each one shifts the reader from checking your figures to wondering how the document was put together, and that is a much worse conversation to be having.</p>

<h2>Before it goes out</h2>

<p>Two reconciliations, and neither takes long.</p>

<p>The first is arithmetic: every total ties to its components, every component ties to a source, and the sum of the heads equals the number on the front page. It sounds trivial. It fails more often than any other check.</p>

<p>The second is the overlap Week 23 described. Every time-related cost appears once, under one head. Site staff cannot be in prolongation and in disruption. Standing plant cannot be in prolongation and in a variation. Finding that yourself costs an afternoon; having it found for you costs the credibility of everything else in the file.</p>

<h2>Practical insight</h2>

<p>Take one head of claim from any live submission and try to walk a single line all the way down to a source document. Pick the largest one.</p>

<p>Most people doing this for the first time get two levels down and find the trail ends in a spreadsheet somebody built for the claim, which draws on another spreadsheet, which draws on a figure whose origin nobody present can now explain.</p>

<p>That is worth knowing before the other side finds it. Sometimes the underlying document exists and simply was not referenced; that is an hour's work. Sometimes it doesn't exist, and the honest response is to reduce the claim to what can be evidenced rather than to defend what cannot.</p>

<p>And on a live job, the useful version of this exercise is upstream. Look at your cost coding and ask what you would be able to prove from it if this job went wrong. The answer, for most projects, is a good deal less than the team assumes &#8212; and it is one of the few things in this track that can still be fixed by editing a list.</p>

<h2>Key takeaways</h2>

<p>&#10004; The test of a claim is whether a stranger with your files reaches your number without asking you anything.</p>

<p>&#10004; The contract defines a fully detailed claim in four parts: the event, the basis, the contemporary records, and the particulars of the amount.</p>

<p>&#10004; Contemporary records are those made at the time or immediately after, and the obligation to keep them is yours.</p>

<p>&#10004; An Engineer monitoring or instructing records concedes nothing about liability or about their accuracy.</p>

<p>&#10004; Post pricing from actual records works where the change can be segregated, and fails where its effects spread across trades.</p>

<p>&#10004; Your cost coding fixes the finest resolution you will ever be able to prove, and it was decided before the job began.</p>

<p>&#10004; The burden of substantiation is on the claiming party, and under some forms the figure is certified rather than merely submitted.</p>

<h2>What&#39;s coming next</h2>

<p>That closes the money. Everything from here is presentation &#8212; not decoration, but the difference between a correct claim that persuades and a correct claim that does not. Next week is assembling the document: what goes in it, what order, how long it should be, and why the section most people write last is the only one a decision-maker is certain to read.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 26 &#183; Assembling a claim &#183; coming soon</span>
                                    <h4>Write it for the person hunting holes</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Cost That Is Not On Site &#8212; The Project Control Hub</title>",
                  "<title>A Number A Stranger Can Rebuild &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Cost That Is Not On Site | The Project Control Hub"',
                  'content="A Number A Stranger Can Rebuild | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-24.html", "claim-week-25.html")
    s = s.replace('<span>Week 24<span class="crumb-title"> &#183; Head office and finance</span></span>',
                  '<span>Week 25<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 24",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 25", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Aug 16, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Aug 16, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week25.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 24", "claim-week-24.html", PREV_TITLE):
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
    if 'href="claim-week-25.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 25 &#183; Pricing and substantiation &#183; coming soon</span>\n'
            '                                    <h4>A number a stranger can rebuild</h4>',
            '<span class="next-week-tag">Week 25 &#183; Pricing and substantiation</span>\n'
            '                                    <h4>A number a stranger can rebuild.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-25.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 25" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 25, title: "Pricing and substantiation — from cost records to a number",\n'
           '          short: "Pricing and substantiation", status: "upcoming" },')
    new = ('        { n: 25, title: "Pricing and substantiation — from cost records to a number",\n'
           '          short: "Pricing and substantiation", status: "live", page: "claim-week-25.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 25 live (%s)" % DATE)
    elif 'page: "claim-week-25.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 25 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-25.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-25.html</loc>\n"
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
