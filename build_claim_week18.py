#!/usr/bin/env python3
"""claim-week-18.html — Track 5, hafta 18. Faz D kapanisi. Sablon: claim-week-17.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-17.html", "claim-week-18.html"
PREV_TITLE = "Slowing down on purpose."
TITLE = "Nobody instructed it. You did it anyway."
CRUMB = "Acceleration and mitigation"
DATE = "Jul 5, 2028"
WEEK_N = 18
DESC = ("Your extension of time has been refused, damages are running, and the only way to protect "
        "yourself is to spend money nobody has agreed to pay. Three different things wear the word "
        "acceleration, and the duty to mitigate is not one of them. Claims &amp; Delay Analysis Week 18.")
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
<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THREE THINGS, ONE WORD</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">they are paid for differently, and conflating them is how contractors work for free</text>
<rect x="34" y="60" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">MITIGATION &#8212; a duty you already have</text>
<text x="54" y="98" fill="#475569" font-size="10.5">reduce the effects of delay and keep idle labour and plant to a minimum</text>
<text x="54" y="108" fill="#94a3b8" font-size="9.5">it does not oblige you to spend money going faster</text>
<rect x="34" y="122" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="142" fill="#059669" font-size="10.5" font-weight="700">DIRECTED ACCELERATION &#8212; instructed, and priced</text>
<text x="54" y="160" fill="#475569" font-size="10.5">somebody asked for it, somebody agreed how it would be paid for</text>
<text x="54" y="170" fill="#94a3b8" font-size="9.5">the only comfortable version of this week</text>
<rect x="34" y="184" width="572" height="52" rx="8" fill="#94a3b8" opacity="0.14" stroke="#cbd5e1"/>
<text x="54" y="204" fill="#64748b" font-size="10.5" font-weight="700">CONSTRUCTIVE ACCELERATION &#8212; nobody instructed anything</text>
<text x="54" y="222" fill="#64748b" font-size="10.5">your time was refused or left undecided, so you paid to hit a date you should not have had to</text>
<text x="54" y="232" fill="#94a3b8" font-size="9.5">the version this week is actually about</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The first is owed by you. The second is owed to you. The third is an argument.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE DECISION NOBODY WANTS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">taken under time pressure, with the entitlement still unresolved</text>
<rect x="34" y="60" width="278" height="118" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">WAIT FOR THE DECISION</text>
<text x="54" y="104" fill="#64748b" font-size="10">costs you nothing today</text>
<text x="54" y="122" fill="#64748b" font-size="10">damages run if the answer</text>
<text x="54" y="140" fill="#64748b" font-size="10">comes back the wrong way</text>
<text x="54" y="164" fill="#64748b" font-size="10">and the date has passed by then</text>
<rect x="328" y="60" width="278" height="118" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">SPEED UP NOW</text>
<text x="348" y="104" fill="#64748b" font-size="10">costs are certain and immediate</text>
<text x="348" y="122" fill="#64748b" font-size="10">recovery is uncertain and late</text>
<text x="348" y="140" fill="#64748b" font-size="10">and if you succeed, the delay</text>
<text x="348" y="164" fill="#64748b" font-size="10">you were avoiding never shows</text>
<rect x="34" y="192" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="213" fill="#64748b" font-size="10.5">Either way it comes out of a net margin of $48,163. That is the whole of what is at stake.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The cruelty of the right-hand box: succeed, and you have destroyed the evidence of what you were avoiding.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 218" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">AGREE THE MECHANISM BEFORE YOU SPEND</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the recommendation is unromantic and it removes most of the argument</text>
<rect x="34" y="60" width="572" height="40" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="78" fill="#059669" font-size="10.5" font-weight="700">BEFORE ACCELERATING</text>
<text x="54" y="94" fill="#475569" font-size="10.5">agree how payment will work, even if entitlement itself is still in dispute</text>
<rect x="34" y="110" width="572" height="40" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="128" fill="#059669" font-size="10.5" font-weight="700">WHERE IT FOLLOWS AN EMPLOYER EVENT</text>
<text x="54" y="144" fill="#475569" font-size="10.5">agree the basis of payment too &#8212; rates, resources, and what counts as accelerated work</text>
<rect x="34" y="160" width="572" height="44" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="180" fill="#64748b" font-size="10.5">If they will not agree, write down what you are doing, why, and what it is costing &#8212;</text>
<text x="54" y="196" fill="#64748b" font-size="10.5">weekly, in a document you send. That record is the whole of the later claim.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Agreement is better. Contemporaneous unilateral records are the fallback. Silence is not an option that ends well.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Nobody instructed it. You did it anyway.</h2>

<p>Your extension of time application has been refused. Or it hasn't been refused &#8212; it has simply not been answered, and the completion date is eleven weeks away.</p>

<p>Delay damages start running on that date whatever anybody eventually decides. So you put on a second shift, bring in another gang, and pay for weekend working. You hit the date. Nobody instructed any of it, nobody agreed to pay for it, and the money has gone.</p>

<p>That is the situation this week is about, and it is one of the few in this track where the decision has to be made while the job is running rather than argued about afterwards.</p>

<h2>Three things wearing one word</h2>

""" + FIG1 + """

<p>Before anything else, separate them, because conflating them is a reliable way to work for nothing.</p>

<p><strong>Mitigation</strong> is a duty you already carry. A contractor is generally obliged to mitigate the loss arising from delayed or disrupted works, and in particular to do what is reasonably possible to keep non-productive labour and plant costs down. Many standard forms say so expressly.</p>

<p><strong>Directed acceleration</strong> is somebody asking you to go faster and agreeing what that will be worth. It is the only comfortable version of this subject and it is not the one that generates disputes.</p>

<p><strong>Constructive acceleration</strong> is the third case: nobody instructed anything, but your entitlement to time was refused or left hanging, so you spent money to reach a date you should not have been held to.</p>

<h2>What the duty to mitigate does not require</h2>

<p>This is the misunderstanding that costs contractors most, and it is worth stating flatly.</p>

<p>The duty to mitigate is about reducing the <em>effects</em> of delay &#8212; not standing crews down late, not leaving plant on hire doing nothing, not letting disruption cost more than it has to. It is a duty to be sensible with what you are already spending.</p>

<p>It is not a duty to accelerate. Nothing obliges a contractor to open its own wallet in the name of mitigation. It may well decide to &#8212; to claw back slippage that was its own fault, for example &#8212; but that is a choice it makes, not an obligation somebody can hold it to. Being told that you have a duty to mitigate, and that this duty means you must resource up at your own expense to protect somebody else's completion date, is an argument that gets made and it does not follow.</p>

<p>Keep the two apart in your own head and in your correspondence. Mitigating the cost effects of disruption and accelerating to reduce the delay effects are different acts with different price tags.</p>

<h2>The decision nobody wants</h2>

""" + FIG2 + """

<p>Now the actual dilemma, which is a commercial one taken under time pressure with the entitlement unresolved.</p>

<p>Wait for the decision, and you spend nothing today. If the answer eventually comes back against you, damages run from a date that has already passed and there is nothing left to do about it.</p>

<p>Speed up now, and the costs are certain, immediate and yours. Recovery is uncertain and arrives, if at all, years later.</p>

<p>Either way the money comes out of the same place. The net margin on this job is $48,163, and a fortnight of second-shift working on a project this size can account for a serious fraction of that. This is not a technical decision dressed as a commercial one. It is a commercial decision with a technical argument attached.</p>

<p>And there is a cruelty in the second box that deserves naming. If you accelerate successfully, the delay you were avoiding never happens &#8212; so the evidence of what it would have been no longer exists anywhere except in a model you build afterwards to prove it.</p>

<h2>Constructive acceleration</h2>

<p>The doctrine has been recognised in the United States for decades and is treated more cautiously elsewhere, which is itself worth knowing before relying on it.</p>

<p>The Protocol describes it as acceleration following the employer's failure to recognise that the contractor has met with employer delay entitling it to an extension &#8212; a failure that then obliges the contractor to speed up in order to finish by the completion date currently standing. It can arise from a refusal of a valid application, or simply from granting the extension too late to be of use.</p>

<p>Read that against the previous track and the shape becomes clear. <a href="contract-week-9.html">Contract Week 9</a> set out the machinery for assessing an extension of time, and <a href="contract-week-10.html">Contract Week 10</a> covered what happens when the periods in that machinery are missed. Constructive acceleration is what a contractor does when the machinery has failed to produce an answer in time, and the cost of that failure lands on the party that did not cause it.</p>

<h2>Proving it costs twice</h2>

<p>An awkward practical consequence, and it connects the whole of Phase C.</p>

<p>To recover the cost of acceleration you generally have to show what the delay would have been had you not accelerated. That is a hypothetical, so it needs one of the modelled techniques. But you also have to show what actually happened and what it cost, which needs the as-built.</p>

<p>Week 14 recorded the advice that where acceleration is in issue it is worth deliberately running both a modelled technique and one built purely on as-built data. Here is the reason: an acceleration claim genuinely needs both halves. One establishes the delay you avoided; the other establishes the resources you threw at it.</p>

<p>That is more expensive than an ordinary delay claim, and it is a further argument for settling the payment mechanism before spending the money rather than after.</p>

<h2>What to do instead</h2>

""" + FIG3 + """

<p>The guidance is unromantic and it works: before implementing acceleration, agree the payment entitlement mechanism. Where the acceleration follows an employer risk event, agree the basis of payment as well.</p>

<p>Note what that does not require. It does not require anybody to concede entitlement. Two parties who disagree entirely about whose fault the delay is can still agree, in an afternoon, how accelerated work will be recorded and valued if it turns out to be payable. Separating those two questions is the single most useful thing available here.</p>

<p>If the other side will not engage, the fallback is contemporaneous and unilateral: write down what you are doing, why you consider it necessary, and what it is costing &#8212; weekly, in something you send rather than something you file. That record is not as good as an agreement. It is the entire difference between a claim and a grievance.</p>

<h2>Practical insight</h2>

<p>Find any period on your job where you increased resources beyond the plan and ask one question about it: was that acceleration, or was that catching up on our own slippage?</p>

<p>Answer honestly, because the other side will. Extra resource applied to recover your own delay is not an acceleration claim, whatever it cost. Mixing the two into a single figure is the fastest way to have the whole amount rejected.</p>

<p>Then check what exists in writing from the time. An instruction? A minuted discussion? A letter saying you were proceeding under protest? If the answer is nothing, you are relying on reconstructing intent years later, and this is the one argument in the track where doing that reliably fails.</p>

<p>And if you are heading into that decision now &#8212; entitlement unresolved, date approaching &#8212; write the letter today. Not the claim. The letter that says what you are about to do, why, and that you regard the cost as recoverable.</p>

<h2>Key takeaways</h2>

<p>&#10004; Mitigation, directed acceleration and constructive acceleration are three different things with three different payment positions.</p>

<p>&#10004; The duty to mitigate means reducing the effects of delay, not spending your own money to go faster.</p>

<p>&#10004; The real decision is commercial: certain cost now against uncertain damages later, out of the same margin either way.</p>

<p>&#10004; Successful acceleration destroys the evidence of the delay it prevented, which then has to be modelled.</p>

<p>&#10004; Constructive acceleration follows a refused or late extension, and is recognised more readily in some jurisdictions than others.</p>

<p>&#10004; An acceleration claim needs both a modelled analysis and an as-built one, which makes it more expensive to prove than a delay claim.</p>

<p>&#10004; Agree the payment mechanism before spending, without conceding entitlement; failing that, record what you are doing weekly and send it.</p>

<h2>What&#39;s coming next</h2>

<p>That closes the hard arguments about time. The next phase is about the loss that does not touch the completion date at all &#8212; the job that finishes when it was always going to finish and still costs far more than it should have, because the work was done in the wrong order, in the wrong weather, with more people than the plan assumed. Disruption is the half of this subject that most claims handle worst.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 19 &#183; Disruption &#183; coming soon</span>
                                    <h4>On time, and losing money</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Slowing Down On Purpose &#8212; The Project Control Hub</title>",
                  "<title>Nobody Instructed It. You Did It Anyway &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Slowing Down On Purpose | The Project Control Hub"',
                  'content="Nobody Instructed It. You Did It Anyway | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-17.html", "claim-week-18.html")
    s = s.replace('<span>Week 17<span class="crumb-title"> &#183; Pacing</span></span>',
                  '<span>Week 18<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 17",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 18", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jun 28, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jun 28, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week18.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 17", "claim-week-17.html", PREV_TITLE):
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
    if 'href="claim-week-18.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 18 &#183; Acceleration and mitigation &#183; coming soon</span>\n'
            '                                    <h4>Nobody instructed it. You did it anyway</h4>',
            '<span class="next-week-tag">Week 18 &#183; Acceleration and mitigation</span>\n'
            '                                    <h4>Nobody instructed it. You did it anyway.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-18.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 18" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 18, title: "Acceleration and mitigation — directed, constructive and unpaid",\n'
           '          short: "Acceleration and mitigation", status: "upcoming" },')
    new = ('        { n: 18, title: "Acceleration and mitigation — directed, constructive and unpaid",\n'
           '          short: "Acceleration and mitigation", status: "live", page: "claim-week-18.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 18 live (%s)" % DATE)
    elif 'page: "claim-week-18.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 18 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-18.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-18.html</loc>\n"
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
