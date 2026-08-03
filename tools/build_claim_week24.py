#!/usr/bin/env python3
"""claim-week-24.html — Track 5, hafta 24. Sablon: claim-week-23.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-23.html", "claim-week-24.html"
PREV_TITLE = "Time has a daily rate."
TITLE = "The cost that is not on site."
CRUMB = "Head office and finance"
DATE = "Aug 16, 2028"
WEEK_N = 24
DESC = ("The office that carries this job has rent and salaries to pay whether the job runs late or "
        "not. Three formulae exist to put a number on it, the two that are recommended need data "
        "no project team holds, and the one everybody uses is the one that is criticised. "
        "Claims &amp; Delay Analysis Week 24.")
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
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO THINGS CALLED HEAD OFFICE OVERHEAD</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">one is a records problem, the other is the reason formulae exist at all</text>
<rect x="34" y="60" width="278" height="126" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">DEDICATED</text>
<text x="54" y="104" fill="#475569" font-size="10">people and effort assignable</text>
<text x="54" y="122" fill="#475569" font-size="10">to this job specifically</text>
<text x="54" y="146" fill="#64748b" font-size="10">a quantity surveyor&#39;s week</text>
<text x="54" y="164" fill="#64748b" font-size="10">spent on your variations</text>
<rect x="328" y="60" width="278" height="126" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">UNABSORBED</text>
<text x="348" y="104" fill="#64748b" font-size="10">rent, some salaries, the costs</text>
<text x="348" y="122" fill="#64748b" font-size="10">that run whatever you build</text>
<text x="348" y="146" fill="#64748b" font-size="10">no timesheet will ever</text>
<text x="348" y="164" fill="#64748b" font-size="10">allocate these to a project</text>
<text x="320" y="212" text-anchor="middle" fill="#94a3b8" font-size="10.5">Prove the left-hand column with records. The right-hand column is where the arguing happens.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Unless the contract shuts them out, unabsorbed overheads are generally recoverable as a foreseeable cost of prolongation.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 262" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THREE FORMULAE, THREE SOURCES OF PERCENTAGE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">they differ in one thing only: where the rate comes from</text>
<rect x="34" y="60" width="572" height="58" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="80" fill="#64748b" font-size="10.5" font-weight="700">HUDSON &#8212; your own tender allowance</text>
<text x="54" y="98" fill="#64748b" font-size="10.5">the overhead and profit percentage you priced, applied to the contract value per day</text>
<text x="54" y="112" fill="#94a3b8" font-size="10">criticised for circularity: it pays the margin you hoped for, not the cost you carried</text>
<rect x="34" y="126" width="572" height="58" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="146" fill="#059669" font-size="10.5" font-weight="700">EMDEN &#8212; your actual accounts</text>
<text x="54" y="164" fill="#475569" font-size="10.5">total overhead and profit against total company turnover, from audited figures</text>
<text x="54" y="178" fill="#94a3b8" font-size="10">recommended &#8212; and the data lives in finance, not on the project</text>
<rect x="34" y="192" width="572" height="58" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="212" fill="#059669" font-size="10.5" font-weight="700">EICHLEAY &#8212; allocate by billings, then per day</text>
<text x="54" y="230" fill="#475569" font-size="10.5">share of actual office overhead by billing ratio, divided by days, times days of delay</text>
<text x="54" y="244" fill="#94a3b8" font-size="10">the US standard, and in federal work effectively the only route</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Both recommended formulae need company-level figures. Which is why project teams reach for the third one.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 226" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THIRTY DAYS, TWO HEADS OF CLAIM</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">on this job, at a tender overhead and profit rate of 15%</text>
<rect x="34" y="60" width="278" height="72" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">PROLONGATION</text>
<text x="54" y="106" fill="#475569" font-size="14" font-weight="700">$6,997</text>
<text x="54" y="124" fill="#64748b" font-size="10">site costs, at the average rate</text>
<rect x="328" y="60" width="278" height="72" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">HEAD OFFICE, ON A FORMULA</text>
<text x="348" y="106" fill="#64748b" font-size="14" font-weight="700">$12,329</text>
<text x="348" y="124" fill="#64748b" font-size="10">15% of $1,000,000, spread over 365 days</text>
<rect x="34" y="146" width="572" height="66" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="168" fill="#64748b" font-size="10.5">The off-site figure is nearly twice the on-site one, which is why employers resist formulae</text>
<text x="54" y="186" fill="#64748b" font-size="10.5">and why the entitlement condition matters more than the arithmetic: you have to show</text>
<text x="54" y="204" fill="#64748b" font-size="10.5">the delay actually stopped you earning that overhead somewhere else.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Illustrative, on the criticised formula, using this job&#39;s own tender percentage. It is a starting figure, not an entitlement.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The cost that is not on site.</h2>

<p>Last week priced the site staying open. There is a second cost, in a building your employer has probably never visited, and it does not appear on any site record.</p>

<p>An office carries rent, salaries, insurance, accounting, IT and directors. None of it belongs to any one project, all of it has to be paid for out of the turnover the projects generate, and when a job runs late it occupies capacity that was supposed to be earning that contribution somewhere else by now.</p>

<p>That is the head office overhead claim. It is one of the largest heads of quantum in this track and one of the most reliably rejected, and the two facts aren't unrelated.</p>

<h2>Two things sharing a name</h2>

""" + FIG1 + """

<p>The guidance splits it usefully. Some head office cost is <em>dedicated</em> &#8212; effort that can be assigned to this job because somebody recorded it. The commercial manager who spent three weeks on your variation account is a real, provable cost, and it is proved the way everything else in Phase B was proved: with records.</p>

<p>The rest is <em>unabsorbed</em>. Rent and a proportion of salaries are incurred whether you build this job, another job, or nothing at all. No timesheet allocates them, because they are not caused by any project individually.</p>

<p>Unless the contract shuts them out, unabsorbed overheads are generally recoverable as a foreseeable consequence of prolongation. The difficulty is not entitlement in principle. It's arithmetic: nobody can say what portion of the rent this delay consumed, because the rent didn't change.</p>

<h2>The condition everybody skips</h2>

<p>Before any formula, there is a test that decides most of these claims and that most claims do not address at all.</p>

<p>You have to be able to demonstrate that, because of the employer's risk events, you were prevented from taking on other overhead-earning work.</p>

<p>Read that carefully. The claim is not that the delay was annoying, or that the office was busy. It is that the resources tied up on this job would otherwise have been on a different job, contributing to the same overhead. If the market was flat and there was no other work to take, there's no loss, however long the delay ran.</p>

<p>The US position adds an interesting variation. Where the delay was of uncertain duration and the contractor had to stand ready to resume, courts have accepted that it need not separately prove it could not have taken other work &#8212; standing ready is itself the constraint. Different route, same underlying idea: the loss is the capacity you could not redeploy.</p>

<h2>Three formulae</h2>

""" + FIG2 + """

<p>All three do the same thing: convert a percentage into a daily rate and multiply it by the delay. They differ in one respect only, which is where the percentage comes from.</p>

<p><strong>Hudson</strong> takes the overhead and profit percentage from your own tender. <strong>Emden</strong> takes your actual overhead and profit as a proportion of your actual company turnover, from the accounts. <strong>Eichleay</strong>, the American approach, allocates a share of the actual office overhead to the contract using the ratio of this job's billings to total billings over the period, converts that to a daily figure and multiplies by the days of delay.</p>

<p>The guidance recommends the second and third, and the reason is the objection to the first.</p>

<h2>Why Hudson is the one that gets attacked</h2>

<p>Hudson's circular. It pays you a percentage you chose, on a job where the argument is about whether you were paid enough.</p>

<p>Take this job. The tender carries overhead and profit of $124,051 on a controlled budget of $827,008 &#8212; exactly fifteen per cent. Apply that to the contract sum across the twelve-month programme and the head office rate is a little under $411 a day.</p>

""" + FIG3 + """

<p>Thirty days of delay is therefore $12,329 under Hudson, against $6,997 of site prolongation for the same thirty days. The off-site number is nearly double the on-site one.</p>

<p>An employer looking at that will make the obvious point: the fifteen per cent is the margin the contractor hoped to earn, not evidence of what its office actually cost. Emden answers that by going to the audited accounts. Eichleay answers it by using real overhead and a real billing ratio.</p>

<p>Which produces the practical problem nobody warns you about. Both recommended formulae need company-level financial data &#8212; total turnover, total overhead, total billings &#8212; and no project team has any of it. Getting it means asking the finance director to open the accounts for the purposes of a claim, and being prepared to have them examined. That's a conversation many contractors would rather not have, and it is precisely why the criticised formula keeps appearing in submissions.</p>

<h2>Precision, and how much of it is required</h2>

<p>Worth knowing, because it cuts against the instinct to abandon the claim as unprovable.</p>

<p>Courts have long accepted that damages do not become unassessable merely because they cannot be calculated exactly. Where a loss cannot be established with certainty, its assessment falls to the tribunal's judgement rather than disappearing.</p>

<p>That is what makes these formulae usable at all: they are recognised methods of approximating something real that cannot be measured directly. But the corollary is stated just as plainly in the guidance &#8212; where a formula produces a result that looks inaccurate or unsuitable, it has to be checked against something else rather than defended because the arithmetic was followed correctly.</p>

<h2>Finance, and the money you never had</h2>

<p>There is a further layer, and it is the one that ties this phase back to Track 2.</p>

<p>Delay does not only cost overhead. It costs the finance on the money you had tied up while it happened. <a href="cost-week-17.html">Cost &amp; Cash Week 17</a> measured the working capital gap on this job at $130,404 &#8212; funded from somewhere, at a price, for longer than intended.</p>

<p>Financing charges of that kind have been recognised as a head of loss in their own right in various jurisdictions, distinct from interest awarded on a debt after the event. The distinction matters: one is compensation for a cost you actually incurred during the works, the other is a consequence of not being paid afterwards. They are pleaded differently and they run for different periods.</p>

<p>Establish it the way you would establish anything else: what was borrowed or foregone, for how long, at what rate, and evidenced.</p>

<h2>Practical insight</h2>

<p>Two things, and the first takes ten minutes.</p>

<p>Find out what your company's actual overhead percentage is, from the accounts, and compare it to the percentage in your tenders. If the tender figure is higher, Hudson isn't your friend and you should know that before somebody else points it out. If it is lower, you have been under-recovering and the accounts version is worth the awkward conversation.</p>

<p>The second is the entitlement test. For any live prolongation claim, write down what your business would have done with those resources had the job finished on time. Name the project, or the tender you declined, or the bid team that could not be released. If you can name it, you have the strongest part of this claim. If you cannot, then whatever the formula produces, the claim has a hole in it at the point where the other side will start.</p>

<h2>Key takeaways</h2>

<p>&#10004; Head office overhead splits into dedicated cost, provable from records, and unabsorbed cost that no timesheet can allocate.</p>

<p>&#10004; Unabsorbed overheads are generally recoverable as a foreseeable consequence of prolongation unless the contract excludes them.</p>

<p>&#10004; The condition most claims skip is showing that the delay prevented you from taking on other overhead-earning work.</p>

<p>&#10004; The three formulae differ only in where the percentage comes from: your tender, your accounts, or your billings.</p>

<p>&#10004; Hudson uses your own tender allowance, which is why it is criticised and why it produces the friendliest number.</p>

<p>&#10004; The recommended formulae need company-level financial data that no project team holds, which is the real obstacle.</p>

<p>&#10004; Finance charges on working capital tied up during the delay are a separate head of loss from interest on a late payment.</p>

<h2>What&#39;s coming next</h2>

<p>Every head of claim in this phase ends the same way: with a number that somebody now has to believe. Next week is substantiation &#8212; how a figure gets from a cost ledger into a claim in a form a stranger can rebuild, what has to sit behind each line, and why the most common failure in quantum is not calculating the wrong amount but being unable to show where the right one came from.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 25 &#183; Pricing and substantiation &#183; coming soon</span>
                                    <h4>A number a stranger can rebuild</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Time Has A Daily Rate &#8212; The Project Control Hub</title>",
                  "<title>The Cost That Is Not On Site &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Time Has A Daily Rate | The Project Control Hub"',
                  'content="The Cost That Is Not On Site | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-23.html", "claim-week-24.html")
    s = s.replace('<span>Week 23<span class="crumb-title"> &#183; Prolongation</span></span>',
                  '<span>Week 24<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 23",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 24", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Aug 9, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Aug 9, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week24.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 23", "claim-week-23.html", PREV_TITLE):
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
    if 'href="claim-week-24.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 24 &#183; Head office overhead and finance &#183; coming soon</span>\n'
            '                                    <h4>The cost that is not on site</h4>',
            '<span class="next-week-tag">Week 24 &#183; Head office and finance</span>\n'
            '                                    <h4>The cost that is not on site.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-24.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 24" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 24, title: "Head office overhead and finance — the formulae and their weaknesses",\n'
           '          short: "Head office and finance", status: "upcoming" },')
    new = ('        { n: 24, title: "Head office overhead and finance — the formulae and their weaknesses",\n'
           '          short: "Head office and finance", status: "live", page: "claim-week-24.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 24 live (%s)" % DATE)
    elif 'page: "claim-week-24.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 24 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-24.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-24.html</loc>\n"
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
