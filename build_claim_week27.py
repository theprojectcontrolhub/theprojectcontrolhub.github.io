#!/usr/bin/env python3
"""claim-week-27.html — Track 5, hafta 27. Sablon: claim-week-26.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-26.html", "claim-week-27.html"
PREV_TITLE = "Write it for the person hunting holes."
TITLE = "Now sit across the table."
CRUMB = "Defending a claim"
DATE = "Sep 6, 2028"
WEEK_N = 27
DESC = ("You have to build a chain. They only have to break one link. What a competent response "
        "looks for and in what order, why rejecting everything is not defending, and why getting "
        "good at this is the fastest way to get good at claiming. Claims &amp; Delay Analysis Week 27.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE ORDER A REVIEW ACTUALLY RUNS IN</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">cheapest first &#8212; and most reviews never reach the bottom row</text>
<rect x="34" y="60" width="572" height="38" rx="8" fill="#059669" opacity="0.14" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">1 &#183; THE PERIODS</text>
<text x="54" y="93" fill="#475569" font-size="10.5">notice served in time, in form, to the right person? costs an afternoon, ends everything</text>
<rect x="34" y="106" width="572" height="38" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="124" fill="#059669" font-size="10.5" font-weight="700">2 &#183; WHAT IS MISSING</text>
<text x="54" y="139" fill="#475569" font-size="10.5">which events, periods and failures are not in the analysis? costs a day</text>
<rect x="34" y="152" width="572" height="38" rx="8" fill="#059669" opacity="0.07" stroke="#a7f3d0"/>
<text x="54" y="170" fill="#059669" font-size="10.5" font-weight="700">3 &#183; THE ASSUMPTIONS</text>
<text x="54" y="185" fill="#475569" font-size="10.5">the ones the chosen method needs and the document never states</text>
<rect x="34" y="198" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="216" fill="#64748b" font-size="10.5" font-weight="700">4 &#183; THE ARITHMETIC</text>
<text x="54" y="231" fill="#64748b" font-size="10.5">reconciliation, double counting, lines with no source &#8212; expensive, and rarely needed</text>
<text x="320" y="258" text-anchor="middle" fill="#94a3b8" font-size="10.5">Claims are almost never defeated on the numbers. They are defeated two rows above them.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Which is why a claimant who spends all the budget on the model and none on the notice has misallocated it.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE MOST PRODUCTIVE QUESTION</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">not is this wrong &#8212; what is not here</text>
<rect x="34" y="60" width="278" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="84" fill="#64748b" font-size="10.5">events left out of the model</text>
<rect x="328" y="60" width="278" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="84" fill="#64748b" font-size="10.5">months left out of the windows</text>
<rect x="34" y="106" width="278" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="130" fill="#64748b" font-size="10.5">their own delays, unmentioned</text>
<rect x="328" y="106" width="278" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="130" fill="#64748b" font-size="10.5">recovery periods, unmentioned</text>
<rect x="34" y="152" width="572" height="38" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="176" fill="#64748b" font-size="10.5">documents referred to in the narrative and absent from the appendices</text>
<rect x="34" y="198" width="572" height="30" rx="6" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="218" fill="#64748b" font-size="10.5">Every omission is a choice somebody made, and choices are easier to question than calculations.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The largest single source of divergence between two analyses is what went into them. Start there.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 262" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHERE EACH METHOD IS SOFTEST</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">identify the method, then go straight to its known weakness</text>
<rect x="34" y="60" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="83" fill="#64748b" font-size="10.5"><tspan font-weight="700">IMPACTED AS-PLANNED</tspan> &#8212; disprove any one of its three silent assumptions</text>
<rect x="34" y="102" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="125" fill="#64748b" font-size="10.5"><tspan font-weight="700">TIME IMPACT</tspan> &#8212; ask how each intermediate programme was built, and by whom</text>
<rect x="34" y="144" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="167" fill="#64748b" font-size="10.5"><tspan font-weight="700">WINDOWS</tspan> &#8212; the boundaries, and the rule used to pick the driving path</text>
<rect x="34" y="186" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="209" fill="#64748b" font-size="10.5"><tspan font-weight="700">AS-PLANNED v AS-BUILT</tspan> &#8212; variance is not cause; ask what caused each one</text>
<rect x="34" y="228" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="251" fill="#64748b" font-size="10.5"><tspan font-weight="700">COLLAPSED AS-BUILT</tspan> &#8212; where the arrows came from, and the order of removal</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">None of these is a trick. They are the weaknesses each method has always had, written down.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Now sit across the table.</h2>

<p>Twenty-six weeks have been written from one chair. Move to the other one and the whole subject changes shape, because the two jobs are not symmetrical.</p>

<p>A claimant has to build a chain: event, effect, criticality, entitlement, quantum, every link evidenced. A defender has to break one. Any one. That asymmetry is the single most important thing to understand about this side of the table, and it explains everything a good response does.</p>

<h2>Rejecting everything is not defending</h2>

<p>Before the technique, the failure mode, because it is at least as common as a weak claim.</p>

<p>Where the employer's team lacks the skills to assess these things properly, the risk runs in both directions: extensions that are inadequate, and extensions that are excessive. Neither is a defence. One buys a dispute and the other gives away money quietly.</p>

<p>The blanket rejection is the more visible version. A response that disputes every event, every day and every pound reads as a negotiating position rather than an assessment, and it costs the defender the one thing that matters most in front of a third party: the appearance of having actually looked.</p>

<p>A response that concedes eleven days and refuses thirty is far harder to argue with than one that refuses forty-one, for exactly the reason Week 12 gave the claimant for conceding first.</p>

<h2>The order a review runs in</h2>

""" + FIG1 + """

<p>Reviews run cheapest first, and most of them never reach the bottom row.</p>

<p>The periods come first because they cost an afternoon and can end everything. Was notice given, in time, in the form required, to the person named? <a href="contract-week-10.html">Contract Week 10</a> is the whole of that check, and a claim that fails it does not need a delay analysis at all.</p>

<p>Then the omissions, which cost a day. Then the assumptions the chosen method requires, which cost a week. The arithmetic comes last because it is expensive and rarely necessary &#8212; claims are almost never defeated on the numbers.</p>

<p>Which is worth carrying back across the table. A claimant who spends the entire budget on the model and none of it on the notice has misallocated it, because row one is where most claims actually die.</p>

<h2>What is not here</h2>

""" + FIG2 + """

<p>The most productive question in any review is not whether something is wrong. It is what is missing.</p>

<p>Week 15 identified the largest single source of divergence between two competent analyses: which events went into them. That works as an attack because omissions are choices, and choices are much easier to question than calculations.</p>

<p>So the list is short and always the same. Which events are not in the model. Which months are not in the windows. Whether the contractor's own delays appear anywhere. Whether any period of recovery is acknowledged. And whether every document the narrative relies on is actually in the appendices.</p>

<p>That last one is unglamorous and startlingly effective. A narrative referring to a letter that is not in the bundle is either an oversight or a document that does not say what the narrative claims, and the response is the same either way: ask for it.</p>

<h2>Go to the method's known weakness</h2>

""" + FIG3 + """

<p>Identify which technique was used and go directly to what it has always been bad at. There is nothing underhand in this; every weakness in that figure was set out in the weeks that described each method.</p>

<p>An impacted as-planned requires that the planned logic was right, the durations were right and the contractor followed the plan. Disproving any one of the three is usually a morning's work with the as-built.</p>

<p>A time impact analysis stands on its intermediate programmes. Ask how each was built, from what, and by whom. Where monthly updates existed, the answer is solid; where they were constructed by the analyst, every one carries judgements that should be listed and rarely are.</p>

<p>A windows analysis turns on where the boundaries fall and how the driving path was identified in each period. If the document does not state the rule, it does not have one.</p>

<p>An as-planned versus as-built comparison measures variance and says nothing about cause. Take the three largest variances and ask what the records say caused each.</p>

<p>And a collapsed as-built rests entirely on as-built logic that was inferred rather than recorded. Ask where the arrows came from, and whether the collapse was run in both orders.</p>

<h2>The defender's own exposure</h2>

<p>Three things a good response does that a reflexive one does not.</p>

<p>It states its own position on entitlement rather than only attacking. A response that never says what it does accept has not made an assessment, and a tribunal will notice.</p>

<p>It checks its own records before asking for theirs. The employer's file contains instructions, late information and access records, and if those support the claim it is better to know now than at a hearing.</p>

<p>And it prices the alternative. Rejecting a claim is not free: it buys the cost of the dispute, the management time, and the risk of a worse outcome later. A defence that has never compared the claimed sum to the cost of resisting it is not a commercial decision, it is a reflex.</p>

<h2>What the response should look like</h2>

<p>Mirror the claim's own structure, section for section. A response organised around its own preoccupations forces the reader to hold two different maps at once, and the reader will not bother.</p>

<p>For each head, state three things in this order: what is accepted, what is disputed, and why. Putting the acceptance first is not politeness &#8212; it establishes that the document is an assessment before it becomes an argument, and everything disputed afterwards is read in that light.</p>

<p>And answer with the same discipline you would demand. If the claim's figure is rejected, say what the correct figure is and where it comes from. A response that disputes a number without offering one has told the decision-maker nothing they can use, and decision-makers under time pressure tend to prefer the party that gave them something to work with.</p>

<h2>Why this makes you better at claiming</h2>

<p>The practical reason to learn this side is that it is the fastest available education in the other one.</p>

<p>Everything in this week is what will be done to your next submission. Reviewing two or three claims properly teaches more about how they fail than writing ten teaches about how they succeed, because the failures are visible from here and invisible from there.</p>

<p>It also changes what you keep on your own jobs. Nobody who has spent a fortnight asking a contractor for allocation sheets that do not exist goes back to their own project and leaves that column blank.</p>

<h2>Practical insight</h2>

<p>Take your own most recent claim &#8212; or the one you are drafting &#8212; and spend two hours attacking it as though somebody else wrote it.</p>

<p>Work the order in the figure. Check the notices first. Then list every event on the job during the claim period and mark which ones are in the analysis. Then find the assumptions your chosen method needs and see whether the document states them. Only then look at the numbers.</p>

<p>Write your findings down as a response document, in the tone the other side will use. Most people are surprised by how easy the first page is to write, and that first page is the one that will arrive.</p>

<p>Then fix what you found. The things you can fix are worth fixing; the things you cannot are worth knowing about before somebody else raises them, because a weakness you have already acknowledged is worth a fraction of the same weakness discovered.</p>

<h2>Key takeaways</h2>

<p>&#10004; The two roles are not symmetrical: a claim must build every link, a defence needs only to break one.</p>

<p>&#10004; A team without the skills to assess claims grants extensions that are either inadequate or excessive; both are failures.</p>

<p>&#10004; Blanket rejection reads as a position rather than an assessment and costs the appearance of having looked.</p>

<p>&#10004; Reviews run cheapest first: periods, then omissions, then assumptions, then arithmetic &#8212; and most stop early.</p>

<p>&#10004; The most productive question is what is missing, because omissions are choices and choices invite explanation.</p>

<p>&#10004; Every method has a documented weakness; identify the technique and go straight to it.</p>

<p>&#10004; A good defence states what it accepts, checks its own records first, and prices the cost of resisting.</p>

<p>&#10004; Mirror the claim's structure, lead each head with what is accepted, and offer your own figure rather than only rejecting theirs.</p>

<h2>What&#39;s coming next</h2>

<p>One week left, and it is not about claims. Five tracks have circled the same job, the same rock and the same two numbers three hundred dollars apart. Next week closes the loop: what the whole thing was for, and what happens to a project where none of this is ever needed.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 28 &#183; What five tracks were for &#183; coming soon</span>
                                    <h4>Net margin was $48,163</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Write It For The Person Hunting Holes &#8212; The Project Control Hub</title>",
                  "<title>Now Sit Across The Table &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Write It For The Person Hunting Holes | The Project Control Hub"',
                  'content="Now Sit Across The Table | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-26.html", "claim-week-27.html")
    s = s.replace('<span>Week 26<span class="crumb-title"> &#183; Assembling a claim</span></span>',
                  '<span>Week 27<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 26",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 27", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Aug 30, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Aug 30, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week27.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 26", "claim-week-26.html", PREV_TITLE):
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
    if 'href="claim-week-27.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 27 &#183; Defending a claim &#183; coming soon</span>\n'
            '                                    <h4>Now sit across the table</h4>',
            '<span class="next-week-tag">Week 27 &#183; Defending a claim</span>\n'
            '                                    <h4>Now sit across the table.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-27.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 27" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 27, title: "Defending a claim — reading one from the other side",\n'
           '          short: "Defending a claim", status: "upcoming" },')
    new = ('        { n: 27, title: "Defending a claim — reading one from the other side",\n'
           '          short: "Defending a claim", status: "live", page: "claim-week-27.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 27 live (%s)" % DATE)
    elif 'page: "claim-week-27.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 27 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-27.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-27.html</loc>\n"
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
