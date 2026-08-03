#!/usr/bin/env python3
"""claim-week-5.html — Track 5, hafta 5. Sablon: claim-week-4.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-4.html", "claim-week-5.html"
PREV_TITLE = "Everything turns on what was critical."
TITLE = "The baseline is an intention, not a record."
CRUMB = "The as-planned programme"
DATE = "Apr 5, 2028"
DESC = ("Every delay method is built on the as-planned programme, and the as-planned programme is a "
        "model of how somebody wanted to build the job &#8212; drafted by a party with an interest, "
        "and usually inherited rather than written. Claims &amp; Delay Analysis Week 5.")
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
<svg viewBox="0 0 640 264" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FOUR QUESTIONS BEFORE YOU TRUST IT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">none of them is about whether the bars look tidy</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">IS ALL THE WORK IN IT?</text>
<text x="54" y="97" fill="#475569" font-size="10.5">scope missing from the baseline cannot be delayed, and cannot be claimed</text>
<rect x="34" y="112" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="132" fill="#059669" font-size="10.5" font-weight="700">DOES A CHAIN RUN FROM START TO FINISH?</text>
<text x="54" y="149" fill="#475569" font-size="10.5">if no continuous path exists, the programme has no critical path to argue about</text>
<rect x="34" y="164" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="184" fill="#059669" font-size="10.5" font-weight="700">DOES EVERY ACTIVITY HAVE A PREDECESSOR AND A SUCCESSOR?</text>
<text x="54" y="201" fill="#475569" font-size="10.5">an open-ended activity drives nothing, so delaying it proves nothing</text>
<rect x="34" y="216" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="236" fill="#059669" font-size="10.5" font-weight="700">WHAT IS HOLDING THE DATES &#8212; LOGIC, OR A CONSTRAINT?</text>
<text x="54" y="253" fill="#475569" font-size="10.5">a constrained date produces float and criticality that no sequence would produce</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A programme can fail all four of these and still print beautifully. That is why it survives to become evidence.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 236" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">HOW A CONSTRAINT CHANGES THE ANSWER</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same activities, the same durations, two different claims</text>
<text x="34" y="68" fill="#64748b" font-size="10" font-weight="700">DRIVEN BY LOGIC</text>
<rect x="34" y="76" width="150" height="22" rx="4" fill="#059669" opacity="0.8"/>
<text x="109" y="91" text-anchor="middle" fill="#fff" font-size="9.5">Piling</text>
<rect x="184" y="76" width="140" height="22" rx="4" fill="#059669" opacity="0.8"/>
<text x="254" y="91" text-anchor="middle" fill="#fff" font-size="9.5">Pile caps</text>
<rect x="324" y="76" width="120" height="22" rx="4" fill="#94a3b8" opacity="0.30"/>
<text x="384" y="91" text-anchor="middle" fill="#475569" font-size="9.5">float</text>
<text x="460" y="91" fill="#64748b" font-size="10">delay here eats float first</text>
<text x="34" y="130" fill="#64748b" font-size="10" font-weight="700">HELD BY A CONSTRAINED DATE</text>
<rect x="34" y="138" width="150" height="22" rx="4" fill="#059669" opacity="0.8"/>
<text x="109" y="153" text-anchor="middle" fill="#fff" font-size="9.5">Piling</text>
<rect x="184" y="138" width="140" height="22" rx="4" fill="#059669" opacity="0.8"/>
<text x="254" y="153" text-anchor="middle" fill="#fff" font-size="9.5">Pile caps</text>
<line x1="330" y1="130" x2="330" y2="168" stroke="#dc2626" stroke-width="2"/>
<text x="340" y="153" fill="#b91c1c" font-size="10" font-weight="600">must-finish-on</text>
<text x="460" y="153" fill="#64748b" font-size="10">no float exists to eat</text>
<rect x="34" y="180" width="572" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="206" fill="#64748b" font-size="10.5">One version says the delay was absorbed. The other says every day of it hit completion. Nothing on site differed.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Before arguing about what a delay did, find out whether the dates were being held by the sequence or by a setting.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 234" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT A WEAK BASELINE KILLS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the methods are not equally dependent on it, and that decides which ones remain open to you</text>
<rect x="34" y="60" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="78" fill="#64748b" font-size="10.5" font-weight="700">DIES OUTRIGHT</text>
<text x="54" y="95" fill="#64748b" font-size="10.5">anything that impacts events into the baseline and re-runs it &#8212; the model is the whole answer</text>
<rect x="34" y="110" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.08" stroke="#cbd5e1"/>
<text x="54" y="128" fill="#64748b" font-size="10.5" font-weight="700">WOUNDED</text>
<text x="54" y="145" fill="#64748b" font-size="10.5">anything using contemporaneous updates, since every update inherits the baseline&#39;s logic</text>
<rect x="34" y="160" width="572" height="42" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="178" fill="#059669" font-size="10.5" font-weight="700">SURVIVES</text>
<text x="54" y="195" fill="#475569" font-size="10.5">anything built from what actually happened &#8212; which is why the record matters more than the plan</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Your method is being chosen for you, right now, by a file somebody built before the job started.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The baseline is an intention, not a record.</h2>

<p>This is the sentence to carry through the rest of the track. The as-planned programme is a model of how one party wanted to build the job. It was produced before anything was built, by somebody with a commercial interest in how it looked, and it records nothing that happened. It is the least factual document in the entire claim.</p>

<p>And nearly every delay method starts by trusting it.</p>

<h2>Why this decides more than it should</h2>

<p>The methods in the middle of this track are not equally dependent on the baseline, and the difference is not a detail.</p>

""" + FIG3 + """

<p>A method that takes the baseline, inserts the delay events into it and re-runs the calculation is only as good as the model it re-runs. If the logic is wrong, the answer is wrong, and it is wrong with four decimal places of confidence.</p>

<p>That is the practical reason this phase comes before the phase on methods. By the time you choose a technique, the choice has largely been made for you by the quality of what you inherited.</p>

<h2>What you are actually inheriting</h2>

<p>On a real job you did not write this programme. The planner who did has gone to another project or another company. What you have is a PDF, possibly a printed copy in the contract documents, and if you're fortunate a native file that opens without warnings.</p>

<p>That is not a complaint, it is the normal condition. The question is what you do about it, and the answer is a short list of checks that has nothing to do with whether the bars look tidy.</p>

""" + FIG1 + """

<p><a href="week-17.html">Schedule Week 17</a> covered these as model health, which is what they are while a job is running. Here they are something else. A programme that fails them is not merely untidy &#8212; it cannot support a conclusion, and any conclusion drawn from it will be dismantled by the first person who opens the file.</p>

<h2>The fifth question, which nobody asks</h2>

<p>Those four checks test whether the model is coherent. They do not test whether it was ever going to work.</p>

<p>A baseline can pass every structural check and still be an aspiration. If it shows the forty-two piles finished inside a period that the rig on site could never have delivered, then the plan was already carrying delay on the day it was accepted &#8212; delay that belongs to whoever wrote it.</p>

<p>This matters because delay is measured as a departure from the plan. Measure against a programme that was never achievable and you get a number that includes the contractor's own optimism, dressed up as somebody else's fault. A reviewer who spots it does not argue about the rock at all. They argue about the durations, and they argue about them for free.</p>

<p>The test is not whether the plan was comfortable. It is whether the resources, the productivity and the access assumed in it were ones the job could actually have had. That question is far easier to answer in month two than in year three, and almost nobody asks it in month two.</p>

<p>One practical corollary: get the native file, not a printout. A PDF shows you the bars. It does not show you the logic, the constraints, the calendars or the float, which means it cannot answer a single one of the questions above.</p>

<h2>Constraints, and how they lie</h2>

<p>Of the four, the last is the one that changes numbers most quietly.</p>

""" + FIG2 + """

<p>A constrained date does not describe a sequence. It overrides one. Put a fixed date on an activity and the arithmetic underneath rearranges itself: float appears where none was earned, or disappears where it existed, and the critical path is no longer a statement about how the work has to be built.</p>

<p>The awkward part is that constraints are often placed for good reasons &#8212; a sectional date, an access restriction, a possession window. Nobody is being dishonest. But an analysis that runs a delay through a constrained model and reports the answer as though it came from the logic has reported something other than what it thinks.</p>

<h2>The programme was drafted by somebody with an interest</h2>

<p>Now the uncomfortable part, and the literature is blunt about it: there is a recognised set of programming practices designed to improve one party's position in a later argument. Not errors &#8212; choices.</p>

<p>Compressing the periods allowed for the employer's design or drawing reviews is one. An early completion programme, showing the works finishing well before the contractual date, is another; it manufactures a stretch of time that any employer delay will appear to consume. Sequences arranged so that everything runs through activities the other side controls is a third.</p>

<p>None of this needs to be treated as an accusation. It needs to be treated as a reason to look. The baseline is the other side's document as much as your own, and the person reviewing your claim will be reading it with exactly this list in mind.</p>

<h2>Which programme is the programme</h2>

<p>There is usually more than one, and the difference is contractual rather than technical.</p>

<p>There is the one submitted under the contract, which under <a href="contract-week-11.html">Contract Week 11</a> becomes the Programme once the review period passes without objection. And there is the one the team actually works to, which by month three has been resequenced twice and never went anywhere near the Engineer.</p>

<p>Analyse the second and you are describing the job. Analyse the first and you are describing your entitlement. They are different exercises, and the mistake is doing one while believing you are doing the other.</p>

<h2>If you have to rebuild it, do it in daylight</h2>

<p>Sometimes the baseline is unusable and there is no way forward except to correct or reconstruct it. That is permissible. What is not permissible is doing it quietly.</p>

<p>Every departure from what the contractor originally produced has to be visible: what was changed, why, and what it did to the answer. A reconstruction whose changes cannot be substantiated does not merely weaken that part of the analysis &#8212; it puts the whole conclusion in question, because the model has become the analyst's rather than the project's.</p>

<h2>Practical insight</h2>

<p>Open the accepted baseline on your current job and spend twenty minutes doing four things.</p>

<p>Count the activities with no successor. Count the constrained dates and write down what each one is for. Find the longest continuous chain from start to completion and check that it actually reaches both ends. Then compare the total scope in the programme against the bill or the activity schedule, at the level of major elements only.</p>

<p>You aren't looking for perfection and you won't find it. You're looking for the two or three findings that would change an answer, and for whether you would be comfortable if the other side found them first.</p>

<p>Write what you find in a dated note, now, while the job is running. If the baseline is weak, the most valuable thing you can do is know it in month four rather than in year three &#8212; because in month four you can still fix the record that a weak baseline will force you to rely on instead.</p>

<h2>Key takeaways</h2>

<p>&#10004; The as-planned programme records an intention, not a fact, and it was drafted by a party with an interest in how it looked.</p>

<p>&#10004; Methods that re-run the baseline die with it; methods built from what happened survive it, which is why the baseline quietly chooses your method.</p>

<p>&#10004; Four checks decide whether it can carry a conclusion: complete scope, a continuous chain, no open ends, and dates held by logic rather than by constraints.</p>

<p>&#10004; A constrained date overrides the sequence, creating or destroying float that no logic earned.</p>

<p>&#10004; A structurally sound baseline can still be unachievable, and delay measured against an unachievable plan silently includes your own optimism.</p>

<p>&#10004; Compressed review periods and early completion programmes are recognised tactics, and the reviewer of your claim knows them.</p>

<p>&#10004; The submitted programme and the working programme are different documents; one describes the job and the other describes your entitlement.</p>

<p>&#10004; Any correction to the baseline must be transparent, because unsubstantiated changes put the whole analysis in question rather than just that part.</p>

<h2>What&#39;s coming next</h2>

<p>If the plan is an intention, the facts have to come from somewhere else. Next week is the record the job produces every day without thinking about it &#8212; the daily reports, the allocation sheets, the diaries &#8212; what each one can actually prove, and why the document that looks most like evidence is usually the one that is not.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 6 &#183; The site record &#183; coming soon</span>
                                    <h4>A curve is not a record</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Everything Turns On What Was Critical &#8212; The Project Control Hub</title>",
                  "<title>The Baseline Is An Intention, Not A Record &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Everything Turns On What Was Critical | The Project Control Hub"',
                  'content="The Baseline Is An Intention, Not A Record | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-4.html", "claim-week-5.html")
    s = s.replace('<span>Week 4<span class="crumb-title"> &#183; Criticality and float</span></span>',
                  '<span>Week 5<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 4",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 5", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Mar 29, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Mar 29, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="5"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week5.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 4", "claim-week-4.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-5.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 5 &#183; The as-planned programme &#183; coming soon</span>\n'
            '                                    <h4>You cannot analyse what you cannot trust</h4>',
            '<span class="next-week-tag">Week 5 &#183; The as-planned programme</span>\n'
            '                                    <h4>The baseline is an intention, not a record.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-5.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 5" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase B — The Evidence the Analysis Runs On", n: 5,\n'
           '          title: "The as-planned programme — validating a baseline you did not build",\n'
           '          short: "The as-planned programme", status: "upcoming" },')
    new = ('        { phase: "Phase B — The Evidence the Analysis Runs On", n: 5,\n'
           '          title: "The as-planned programme — validating a baseline you did not build",\n'
           '          short: "The as-planned programme", status: "live", page: "claim-week-5.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 5 live (%s)" % DATE)
    elif 'page: "claim-week-5.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 5 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-5.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-5.html</loc>\n"
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
