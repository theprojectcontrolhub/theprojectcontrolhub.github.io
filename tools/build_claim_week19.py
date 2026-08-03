#!/usr/bin/env python3
"""claim-week-19.html — Track 5, hafta 19. Faz E acilisi. Sablon: claim-week-18.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-18.html", "claim-week-19.html"
PREV_TITLE = "Nobody instructed it. You did it anyway."
TITLE = "On time, and losing money."
CRUMB = "Disruption"
DATE = "Jul 12, 2028"
WEEK_N = 19
DESC = ("The job finished on the contract date and the margin is gone. Disruption is the loss that "
        "never reaches the completion date, it always costs money, and concurrency does not defeat "
        "it the way it defeats a prolongation claim. Claims &amp; Delay Analysis Week 19.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TIME AND MONEY COME APART</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four jobs, and only one of them produces the claim everybody knows how to make</text>
<line x1="180" y1="58" x2="180" y2="212" stroke="#e2e8f0"/>
<line x1="60" y1="136" x2="606" y2="136" stroke="#e2e8f0"/>
<text x="120" y="100" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">FINISHED</text>
<text x="120" y="114" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">ON TIME</text>
<text x="120" y="178" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">FINISHED</text>
<text x="120" y="192" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">LATE</text>
<text x="300" y="72" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">WORKED AS PLANNED</text>
<text x="490" y="72" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">WORKED INEFFICIENTLY</text>
<rect x="200" y="84" width="188" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="294" y="103" text-anchor="middle" fill="#059669" font-size="10">nothing to claim</text>
<text x="294" y="119" text-anchor="middle" fill="#64748b" font-size="9.5">the job everybody planned</text>
<rect x="398" y="84" width="188" height="44" rx="8" fill="#b91c1c" opacity="0.10" stroke="#fca5a5"/>
<text x="492" y="103" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="600">disruption only</text>
<text x="492" y="119" text-anchor="middle" fill="#64748b" font-size="9.5">no extension, real money gone</text>
<rect x="200" y="144" width="188" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="294" y="163" text-anchor="middle" fill="#059669" font-size="10">delay only</text>
<text x="294" y="179" text-anchor="middle" fill="#64748b" font-size="9.5">the claim everyone knows</text>
<rect x="398" y="144" width="188" height="44" rx="8" fill="#b91c1c" opacity="0.10" stroke="#fca5a5"/>
<text x="492" y="163" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="600">both, and two claims</text>
<text x="492" y="179" text-anchor="middle" fill="#64748b" font-size="9.5">usually pursued as one</text>
<text x="320" y="238" text-anchor="middle" fill="#94a3b8" font-size="10.5">The top-right box is the one that gets missed entirely, and it can be the largest of the four.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Delay may cost nothing. Disruption, once established, always costs something. They are not two words for the same event.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">CONCURRENCY BITES DIFFERENTLY HERE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the argument that moves a prolongation claim does not simply cancel this one</text>
<rect x="34" y="60" width="278" height="112" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">A PROLONGATION CLAIM</text>
<text x="54" y="104" fill="#64748b" font-size="10">concurrent contractor delay</text>
<text x="54" y="122" fill="#64748b" font-size="10">moves it out of compensable</text>
<text x="54" y="146" fill="#64748b" font-size="10">time survives, money doesn&#39;t</text>
<rect x="328" y="60" width="278" height="112" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="82" fill="#059669" font-size="10.5" font-weight="700">A DISRUPTION CLAIM</text>
<text x="348" y="104" fill="#475569" font-size="10">once the loss of efficiency is</text>
<text x="348" y="122" fill="#475569" font-size="10">established, the financial</text>
<text x="348" y="140" fill="#475569" font-size="10">consequence is measurable</text>
<text x="348" y="162" fill="#64748b" font-size="10">even alongside your own faults</text>
<text x="320" y="204" text-anchor="middle" fill="#94a3b8" font-size="10.5">Which does not make it easy. It makes it a different argument, fought on quantum rather than on entitlement.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Worth knowing before conceding a disruption claim because a concurrency point has already cost you the prolongation.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 228" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHY THIS IS HARDER THAN DELAY</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">everything Phase C leaned on is missing here</text>
<rect x="34" y="60" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="78" fill="#64748b" font-size="10.5" font-weight="700">NO NETWORK TO CALCULATE IN</text>
<text x="54" y="95" fill="#64748b" font-size="10.5">there is no critical path for productivity; no software returns the answer</text>
<rect x="34" y="112" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="130" fill="#64748b" font-size="10.5" font-weight="700">NO SINGLE EVENT TO POINT AT</text>
<text x="54" y="147" fill="#64748b" font-size="10.5">the loss accumulates across hundreds of small interruptions nobody logged</text>
<rect x="34" y="164" width="572" height="42" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="182" fill="#059669" font-size="10.5" font-weight="700">SO THE PROOF COMES FROM HOURS</text>
<text x="54" y="199" fill="#475569" font-size="10.5">booked by trade, against an activity, in a location, on a date &#8212; and nothing else will do</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Demonstrating disruption is closer to an art than a science, and the art is entirely constrained by the timesheets.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">On time, and losing money.</h2>

<p>Picture the version of this job where everything works. The rock is found, the notice goes in on time, an extension is granted without argument, and the team pulls the programme back together. The building is handed over on the contract completion date.</p>

<p>Everybody congratulates each other. And the net margin of $48,163 is gone anyway, because for seven months the work was done in the wrong order, in half-finished areas, by crews who moved four times a week and never got a clean run at anything.</p>

<p>Nothing in the previous eighteen weeks finds that money. Every method in Phase C measures movement in a completion date, and the completion date never moved.</p>

<h2>What disruption actually is</h2>

<p>Disruption is what happens when the orderly flow of work breaks up: continuity lost, sequence scrambled, an operation turned into a series of interruptions. The Protocol frames it as disturbance or hindrance to the way a contractor would normally have worked, leaving the job less efficient than it would otherwise have been.</p>

<p>Delay can cause disruption and disruption can cause delay, and they frequently arise from the same events. They are still not the same thing, and the difference is not academic.</p>

""" + FIG1 + """

<p>Read that grid carefully, because it contains the whole argument for this phase. A delay may cost you nothing at all &#8212; it lands on an activity with float, the completion date holds, no damages run. Disruption is the reverse: once it is established, it always has a direct financial consequence, because inefficient work costs more to do.</p>

<p>The top-right box is the one that goes unclaimed. Finished on time, worked badly, money gone. No extension of time was ever due and none was ever applied for, so nothing in the project's paperwork records that anything happened.</p>

<h2>Three ways it stays invisible</h2>

<p>It helps to know the mechanisms, because each one produces a different-looking job.</p>

<p>The disruption lands on non-critical work. Activities with float are interrupted, resequenced, worked in fragments. The completion date is untouched, so no extension arises, and the only trace is that those activities consumed far more hours than they were priced at.</p>

<p>Or it lands on critical work and gets absorbed. More resources are applied, the date is protected, and the delay never materialises. Week 18 covered what that costs; the point here is that the cost is real even when the acceleration argument is unavailable.</p>

<p>Or everything simply takes longer than it should, everywhere, all year. Nobody can name a day when anything went wrong. The job finishes when it was always going to finish and the final account is a disaster.</p>

<h2>Concurrency does not settle it</h2>

""" + FIG2 + """

<p>Here is a point worth carrying out of this week even if nothing else sticks.</p>

<p>Week 16 established that concurrent contractor delay generally moves a prolongation claim out of the compensable column. Time survives; money doesn't. That rule is about the completion date, and it applies to costs that flow from the completion date moving.</p>

<p>Disruption behaves differently. Once loss of efficiency is established, it carries a direct and measurable financial consequence even where concurrent or co-contributory culpable factors are present. Your own failings do not simply cancel it the way they cancel prolongation.</p>

<p>That does not make it easy, and it is emphatically not a way round the concurrency problem. What it does is move the fight. On a prolongation claim, concurrency is fought on entitlement. On a disruption claim, the contractor's own contribution is fought on quantum &#8212; how much of the lost efficiency is attributable to which cause &#8212; which is a harder argument but a live one rather than a closed one.</p>

<h2>The same three questions, and a harder middle</h2>

<p>Week 2 set out the sequence: liability, causation, quantum. Disruption asks the same three and the second is where these claims die.</p>

<p>Entitlement is usually not the problem. Everyone accepts that late information, restricted access or a stream of variations disrupts work; the principle is not seriously contested.</p>

<p>Causation is the hurdle. You have to link a specific employer risk event to a specific loss of efficiency in specific work, and the loss is spread thinly across months. There is no moment where the disruption happened. There is a hundred mornings where a gang arrived and found something in the way.</p>

<p>And the Protocol's answer to that difficulty is a technique rather than an argument, which is next week's subject.</p>

<h2>Bundled, and lost</h2>

<p>One structural mistake accounts for a large share of disruption claims that fail, and it happens before any analysis starts.</p>

<p>The two claims get merged. A single submission asks for an extension of time and, in the same breath, for the additional cost of working inefficiently, with one narrative and one set of figures covering both. It feels efficient. It is how most claims arrive.</p>

<p>The trouble is that they are proved from different things. The delay half stands on a programme and a critical path. The disruption half stands on hours and outputs, and has no interest in the critical path at all. Bundled together, the disruption argument inherits every weakness of the delay argument &#8212; and a concurrency point that legitimately kills the prolongation takes the disruption claim down with it, even though, as above, it should not have.</p>

<p>Keep them separate. Two sections, two sets of evidence, two conclusions. The delay claim can fail entirely and the disruption claim still stand.</p>

<h2>Why this is harder than delay</h2>

""" + FIG3 + """

<p>It is worth being honest that demonstrating disruption sits closer to an art than a science &#8212; considerably more so than analysing delay.</p>

<p>Delay analysis has a network to calculate in. Whatever the disputes about method, there is a model, a critical path, and arithmetic that produces a number. Productivity has none of that. No software takes your programme and returns how much efficiency you lost.</p>

<p>Nor is there a single event to point at. The loss accumulates across hundreds of small interruptions, most of which nobody wrote down because individually none of them seemed worth a letter.</p>

<p>Which leaves one route. The proof is hours: booked by trade, against an activity, in a location, on a date. <a href="cost-week-10.html">Cost &amp; Cash Week 10</a> built the ledger those hours land in, and Week 6 argued the allocation sheet was the most valuable and worst-kept record on any site. This is the week that argument was for.</p>

<p>Without those records a disruption claim does not become harder. It becomes a different and much weaker kind of claim, which is where the rest of this phase goes.</p>

<h2>Practical insight</h2>

<p>Take one activity on your job that has clearly cost more than it was priced at, and try to answer a single question: how many hours went into it, and how many were in the estimate?</p>

<p>That comparison alone is not a disruption claim &#8212; it is the weakest form of the argument and the other side will say your estimate was wrong. But it tells you the size of the problem, and it takes an afternoon.</p>

<p>Then ask the harder question: can you split those hours into a period when the work ran normally and a period when it didn't? If you can, you have the beginnings of something considerably stronger.</p>

<p>And if the honest answer is that your records cannot separate the two, that is the finding. Fix it this month, on the activity with the most people on it, before the disrupted period you will eventually want to prove has already happened.</p>

<h2>Key takeaways</h2>

<p>&#10004; Disruption is interruption to the flow and sequence of work, leaving it less efficient than it would have been.</p>

<p>&#10004; A delay may cost nothing; disruption, once established, always carries a direct financial consequence.</p>

<p>&#10004; Work can be disrupted on a job that finishes exactly on time, and that loss is the one most often never claimed.</p>

<p>&#10004; It hides in three ways: on non-critical work, absorbed by extra resources, or spread thinly across the whole job.</p>

<p>&#10004; Concurrency does not defeat a disruption claim the way it defeats prolongation; it moves the fight from entitlement to quantum.</p>

<p>&#10004; Bundling the two claims into one submission lets the delay argument's weaknesses sink the disruption claim with it.</p>

<p>&#10004; Entitlement is rarely the problem &#8212; linking a specific event to a specific loss of efficiency is.</p>

<p>&#10004; There is no network and no software; the proof is hours booked by trade, against an activity, in a location, on a date.</p>

<h2>What&#39;s coming next</h2>

<p>If the loss cannot be calculated from a model, it has to be measured by comparison &#8212; and the strongest comparison available is not with an estimate, an industry study or another project. It is with your own crews, on your own site, during a period when nothing was in their way. Next week is the measured mile: how it is built, what makes a comparison period clean, and why it is the technique the guidance points to first.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 20 &#183; The measured mile &#183; coming soon</span>
                                    <h4>The best proof is your own site</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Nobody Instructed It. You Did It Anyway &#8212; The Project Control Hub</title>",
                  "<title>On Time, And Losing Money &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Nobody Instructed It. You Did It Anyway | The Project Control Hub"',
                  'content="On Time, And Losing Money | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-18.html", "claim-week-19.html")
    s = s.replace('<span>Week 18<span class="crumb-title"> &#183; Acceleration and mitigation</span></span>',
                  '<span>Week 19<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 18",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 19", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jul 5, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jul 5, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week19.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 18", "claim-week-18.html", PREV_TITLE):
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
    if 'href="claim-week-19.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 19 &#183; Disruption &#183; coming soon</span>\n'
            '                                    <h4>On time, and losing money</h4>',
            '<span class="next-week-tag">Week 19 &#183; Disruption</span>\n'
            '                                    <h4>On time, and losing money.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-19.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 19" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase E — Disruption", n: 19,\n'
           '          title: "Disruption — the loss that never touches the critical path",\n'
           '          short: "Disruption", status: "upcoming" },')
    new = ('        { phase: "Phase E — Disruption", n: 19,\n'
           '          title: "Disruption — the loss that never touches the critical path",\n'
           '          short: "Disruption", status: "live", page: "claim-week-19.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 19 live (%s)" % DATE)
    elif 'page: "claim-week-19.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 19 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-19.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-19.html</loc>\n"
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
