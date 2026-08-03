#!/usr/bin/env python3
"""claim-week-23.html — Track 5, hafta 23. Faz F acilisi. Sablon: claim-week-22.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-22.html", "claim-week-23.html"
PREV_TITLE = "The claim that asks the tribunal to guess."
TITLE = "Time has a daily rate."
CRUMB = "Prolongation"
DATE = "Aug 9, 2028"
WEEK_N = 23
DESC = ("Preliminaries of $85,200 over twelve months is $7,100 a month, and multiplying that by "
        "forty-one days is the wrong answer. Prolongation is paid on what was actually being spent "
        "when the delay happened. Claims &amp; Delay Analysis Week 23.")
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
<svg viewBox="0 0 640 252" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE AVERAGE IS A LINE NOBODY SPENT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">$85,200 across twelve months, and not one of those months looked like the average</text>
<line x1="60" y1="180" x2="600" y2="180" stroke="#cbd5e1"/>
<line x1="60" y1="130" x2="600" y2="130" stroke="#059669" stroke-width="1.5" stroke-dasharray="5 3"/>
<text x="608" y="126" text-anchor="end" fill="#059669" font-size="9.5">$7,100 average</text>
<rect x="72" y="164" width="34" height="16" fill="#94a3b8" opacity="0.45"/>
<rect x="116" y="150" width="34" height="30" fill="#94a3b8" opacity="0.45"/>
<rect x="160" y="122" width="34" height="58" fill="#94a3b8" opacity="0.45"/>
<rect x="204" y="104" width="34" height="76" fill="#059669" opacity="0.55"/>
<rect x="248" y="96" width="34" height="84" fill="#059669" opacity="0.55"/>
<rect x="292" y="94" width="34" height="86" fill="#059669" opacity="0.55"/>
<rect x="336" y="100" width="34" height="80" fill="#059669" opacity="0.55"/>
<rect x="380" y="110" width="34" height="70" fill="#94a3b8" opacity="0.45"/>
<rect x="424" y="128" width="34" height="52" fill="#94a3b8" opacity="0.45"/>
<rect x="468" y="146" width="34" height="34" fill="#94a3b8" opacity="0.45"/>
<rect x="512" y="158" width="34" height="22" fill="#94a3b8" opacity="0.45"/>
<rect x="556" y="168" width="34" height="12" fill="#94a3b8" opacity="0.45"/>
<text x="72" y="196" fill="#94a3b8" font-size="9">mobilise</text>
<text x="280" y="196" fill="#64748b" font-size="9">full site &#183; crane, cabins, supervision</text>
<text x="520" y="196" fill="#94a3b8" font-size="9">wind down</text>
<rect x="34" y="210" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="231" fill="#64748b" font-size="10.5">A delay in month three and a delay in month eleven cost completely different amounts.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Illustrative shape, not measured values. The point is that the flat line is the one number the site never spent.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHICH PERIOD DO YOU PRICE?</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the answer is not the one most claims use</text>
<rect x="34" y="60" width="278" height="106" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE TAIL OF THE JOB</text>
<text x="54" y="104" fill="#64748b" font-size="10">the weeks added at the end</text>
<text x="54" y="122" fill="#64748b" font-size="10">crane gone, cabins reduced,</text>
<text x="54" y="140" fill="#64748b" font-size="10">half the staff demobilised</text>
<text x="54" y="158" fill="#64748b" font-size="10">easy to identify, and wrong</text>
<rect x="328" y="60" width="278" height="106" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="82" fill="#059669" font-size="10.5" font-weight="700">THE PERIOD THE DELAY FELL IN</text>
<text x="348" y="104" fill="#475569" font-size="10">the months the event actually</text>
<text x="348" y="122" fill="#475569" font-size="10">held the works up</text>
<text x="348" y="140" fill="#475569" font-size="10">priced from what the site was</text>
<text x="348" y="158" fill="#475569" font-size="10">genuinely costing then</text>
<rect x="34" y="180" width="572" height="44" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="200" fill="#64748b" font-size="10.5">This is why the windowed analysis mattered. Dated days can be priced. A lump of</text>
<text x="54" y="218" fill="#64748b" font-size="10.5">forty-one undated days can only be multiplied by an average.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The guidance keeps returning to the same phrase: at the time. It applies to the money as much as to the analysis.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 234" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT IS AND IS NOT IN THE CLAIM</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">only the part of the preliminaries that runs with the clock</text>
<rect x="34" y="60" width="278" height="118" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">TIME-RELATED &#183; IN</text>
<text x="54" y="104" fill="#475569" font-size="10">site staff and supervision</text>
<text x="54" y="122" fill="#475569" font-size="10">accommodation and welfare</text>
<text x="54" y="140" fill="#475569" font-size="10">plant standing on hire</text>
<text x="54" y="158" fill="#475569" font-size="10">security, insurances, utilities</text>
<rect x="328" y="60" width="278" height="118" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">NOT TIME-RELATED &#183; OUT</text>
<text x="348" y="104" fill="#64748b" font-size="10">mobilisation and setting up</text>
<text x="348" y="122" fill="#64748b" font-size="10">demobilisation and clearing</text>
<text x="348" y="140" fill="#64748b" font-size="10">anything priced per unit of work</text>
<text x="348" y="158" fill="#64748b" font-size="10">one-off items, however large</text>
<rect x="34" y="192" width="572" height="30" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="212" fill="#64748b" font-size="10.5">Claiming the whole preliminaries figure per week is the error a reviewer looks for first.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A longer job does not need a second setting-up. Splitting the preliminaries properly is most of the work.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Time has a daily rate.</h2>

<p>Here is the arithmetic everybody reaches for. Preliminaries on this job are $85,200. The programme runs twelve months. That is $7,100 a month, or about $233 a day. Forty-one days of delay, therefore, comes to roughly $9,563.</p>

<p>It is clean, it is checkable, and it is the wrong answer.</p>

<p>Not wildly wrong, and not dishonest. But it is an average standing in for a measurement, and the difference between those two is what this week is about &#8212; because it is also the difference between a number that survives scrutiny and one that gets negotiated.</p>

<h2>Nobody ever spent the average</h2>

""" + FIG1 + """

<p>Preliminaries are not a flat monthly charge. They are a curve. In the first month there is a compound, a small team and not much else. By the middle of the job there is a crane on hire, a full complement of site staff, three cabins, security, and a set of temporary works. By month eleven the crane has gone and half the staff are on the next project.</p>

<p>So a delay in month three and a delay in month eleven cost completely different amounts, and the flat line is the one figure the site never actually spent in any month of the job.</p>

<p>The $7,100 is a useful planning number and a good sanity check. It is not, on its own, a claim.</p>

<h2>The rule most claims get backwards</h2>

""" + FIG2 + """

<p>Now the rule, and it is the single most useful thing in this week.</p>

<p>The costs of a delay are assessed by reference to what was going on <em>at the time the delay event occurred</em> &#8212; not by reference to the extra weeks tacked onto the end of the job.</p>

<p>That is the opposite of how most prolongation claims are built. The instinctive approach is to identify the period between the original completion date and the actual one, price what the site cost during those weeks, and claim it. It is easy to identify and easy to evidence.</p>

<p>It is also, on most jobs, the cheapest period of the whole project. The crane is off hire, the cabins are coming down, and the site team is three people finishing snagging. Pricing your delay at the tail-end rate is frequently claiming considerably less than you are entitled to.</p>

<p>It can run the other way too. A delay that fell during a quiet spell, priced at a busy tail-end rate, overstates the claim and hands the other side an easy correction.</p>

<p>Either way, the guidance keeps returning to the same two words: <em>at the time</em>. Week 12 argued that a windowed analysis is worth more because it produces dated days. This is the week that pays off. Dated days can be priced against what the site was actually costing in those months. A lump of forty-one undated days can only be multiplied by an average.</p>

<h2>What you spent, not what you priced</h2>

<p>A second correction, and it catches experienced people.</p>

<p>Prolongation is recovered on cost actually incurred &#8212; time genuinely taken up, expense genuinely suffered. What the tender allowed for preliminaries is close to irrelevant to that calculation.</p>

<p>The reason is not moral, it is practical: bids are unbalanced. Preliminaries get loaded or thinned for commercial reasons that have nothing to do with what the site will cost, and a tender allowance is a bidding decision rather than a measurement.</p>

<p>Which cuts both ways and is worth being clear-eyed about. If you loaded your preliminaries at tender, the allowance flatters you and you will not be paid on it. If you thinned them to win the job, the allowance understates your actual spend &#8212; and you can recover the actual spend, because that is what the rule measures.</p>

<h2>Which parts of the preliminaries run with the clock</h2>

""" + FIG3 + """

<p>The third correction is the one a reviewer tests first, because it is the quickest to find.</p>

<p>Only the time-related part of the preliminaries belongs in a prolongation claim. Site staff, accommodation, welfare, standing plant, security, insurances and utilities all run with the clock: keep the site open another six weeks and they cost another six weeks.</p>

<p>Mobilisation does not. Neither does demobilisation, nor anything priced against a quantity of work rather than a duration. A longer job does not require a second setting-up.</p>

<p>Splitting the preliminaries into the part that runs with time and the part that does not is genuinely most of the work in a prolongation claim, and a claim that skips it &#8212; taking the whole $85,200, dividing by the programme, and multiplying by the delay &#8212; has made an error the other side does not even need an expert to find.</p>

<h2>The overlap that gets found</h2>

<p>One more thing to check before the claim goes out, because it is the first place a reviewer looks after the time-related split.</p>

<p>Site staff appear in a prolongation claim as a time-related cost. They also appear, frequently, in a disruption claim as supervision absorbed by managing change. Both entries can be perfectly honest and describe the same people in the same weeks, and together they charge for them twice.</p>

<p>The same trap catches standing plant claimed as prolongation and again as part of a variation, and site accommodation recovered under an extension and again inside an agreed change. Week 22 named double counting as the hazard of building a claim event by event; this is where it actually shows up.</p>

<p>Run one reconciliation before submitting: every time-related cost, listed once, with the single claim head it belongs to. Finding the overlap yourself costs an afternoon. Having it found for you costs the credibility of everything around it.</p>

<h2>And still no profit on it</h2>

<p>Week 3 established this and it belongs here too. Under the ground conditions clause the entitlement is to Cost, and Cost is defined to exclude profit.</p>

<p>So a fully successful prolongation claim restores what you spent keeping the site open and adds nothing. You financed the extra weeks, carried them on your own working capital &#8212; the $130,404 <a href="cost-week-17.html">Cost &amp; Cash Week 17</a> measured &#8212; and got the money back with no return on it.</p>

<p>That is the correct outcome under the clause and it is worth stating plainly, because a great many people are surprised by it at exactly the wrong moment.</p>

<h2>The version nobody uses</h2>

<p>There is a neat solution to all of the above and it is almost never adopted.</p>

<p>Agree a daily rate for delay at the outset, the same way the contract already fixes a daily rate for liquidated damages. Both parties know what a day is worth, the entire argument above disappears, and the assessment becomes arithmetic.</p>

<p>The reasons it is rare are not technical. Neither side wants to name the number early, and both prefer the optionality of arguing later. But on a job where the parties genuinely intend to settle things as they arise, it is available, and it removes more disputes than almost any other single clause.</p>

<h2>Practical insight</h2>

<p>Take your current job and build the curve rather than the average. Twelve rows, one per month, and in each one the time-related preliminaries actually incurred.</p>

<p>You will need to strip out mobilisation, demobilisation and anything quantity-driven, which is the exercise. Most cost systems will not do it for you, because preliminaries are usually coded as one lump.</p>

<p>What you end up with is a monthly rate table, and it does two things. It tells you what a week of delay is genuinely worth in any given month, which is a management number as much as a claims one. And when a delay does arrive, the claim is a lookup rather than an argument.</p>

<p>Do it once and maintain it monthly. It takes an hour to build and about ten minutes a month, and it converts the weakest part of most claims into the strongest.</p>

<h2>Key takeaways</h2>

<p>&#10004; An average monthly preliminaries figure is a planning number, not a claim; no month of the job costs the average.</p>

<p>&#10004; Prolongation is assessed on what the site was costing at the time the delay occurred, not during the extra weeks at the end.</p>

<p>&#10004; The tail of a job is usually its cheapest period, so pricing delay there often understates the entitlement.</p>

<p>&#10004; Recovery is on cost actually incurred; tender allowances are bidding decisions and carry little weight.</p>

<p>&#10004; Only time-related preliminaries qualify &#8212; mobilisation, demobilisation and quantity-driven items do not.</p>

<p>&#10004; Under a Cost entitlement there is no profit on any of it, so full recovery leaves you level rather than ahead.</p>

<p>&#10004; Site staff and standing plant are easily claimed twice, under prolongation and again under disruption or a variation; reconcile before submitting.</p>

<p>&#10004; A pre-agreed daily rate for delay removes the whole argument and is almost never put in the contract.</p>

<h2>What&#39;s coming next</h2>

<p>Site costs are only half of what a longer job consumes. The other half is happening in an office the delay never touched: the estimator, the accounts team, the directors' time, the borrowing that funded the overrun. Next week is head office overhead and finance &#8212; the formulae that exist to calculate it, why each of them is contested, and what a tribunal is really being asked to accept.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 24 &#183; Head office and finance &#183; coming soon</span>
                                    <h4>The cost that is not on site</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Claim That Asks The Tribunal To Guess &#8212; The Project Control Hub</title>",
                  "<title>Time Has A Daily Rate &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Claim That Asks The Tribunal To Guess | The Project Control Hub"',
                  'content="Time Has A Daily Rate | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-22.html", "claim-week-23.html")
    s = s.replace('<span>Week 22<span class="crumb-title"> &#183; Global and total cost claims</span></span>',
                  '<span>Week 23<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 22",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 23", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Aug 2, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Aug 2, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week23.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 22", "claim-week-22.html", PREV_TITLE):
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
    if 'href="claim-week-23.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 23 &#183; Prolongation &#183; coming soon</span>\n'
            '                                    <h4>Time has a daily rate</h4>',
            '<span class="next-week-tag">Week 23 &#183; Prolongation</span>\n'
            '                                    <h4>Time has a daily rate.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-23.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 23" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase F — Quantum", n: 23,\n'
           '          title: "Prolongation — the cost of time on site",\n'
           '          short: "Prolongation", status: "upcoming" },')
    new = ('        { phase: "Phase F — Quantum", n: 23,\n'
           '          title: "Prolongation — the cost of time on site",\n'
           '          short: "Prolongation", status: "live", page: "claim-week-23.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 23 live (%s)" % DATE)
    elif 'page: "claim-week-23.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 23 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-23.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-23.html</loc>\n"
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
