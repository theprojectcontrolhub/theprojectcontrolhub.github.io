#!/usr/bin/env python3
"""claim-week-14.html — Track 5, hafta 14. Sablon: claim-week-13.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-13.html", "claim-week-14.html"
PREV_TITLE = "Two bars, and what they leave out."
TITLE = "Take the delay out. See what remains."
CRUMB = "Collapsed as-built"
DATE = "Jun 7, 2028"
WEEK_N = 14
DESC = ("Build what happened, pull the delays back out, and read the date the job would have "
        "finished without them. The most intuitive method in the subject, and the one with the "
        "most judgement buried inside it. Claims &amp; Delay Analysis Week 14.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">SUBTRACTION, IN THREE STEPS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">no plan required anywhere in this &#8212; only what happened</text>
<text x="34" y="70" fill="#64748b" font-size="9.5" font-weight="700">AS BUILT</text>
<rect x="130" y="60" width="112" height="18" rx="3" fill="#059669" opacity="0.75"/>
<text x="186" y="73" text-anchor="middle" fill="#fff" font-size="9">Piling</text>
<rect x="242" y="60" width="58" height="18" rx="3" fill="#b91c1c" opacity="0.5"/>
<text x="271" y="73" text-anchor="middle" fill="#fff" font-size="8.5">rock</text>
<rect x="300" y="60" width="86" height="18" rx="3" fill="#059669" opacity="0.75"/>
<text x="343" y="73" text-anchor="middle" fill="#fff" font-size="9">Caps</text>
<rect x="386" y="60" width="46" height="18" rx="3" fill="#94a3b8" opacity="0.45"/>
<text x="409" y="73" text-anchor="middle" fill="#475569" font-size="8.5">rig</text>
<rect x="432" y="60" width="96" height="18" rx="3" fill="#059669" opacity="0.75"/>
<text x="480" y="73" text-anchor="middle" fill="#fff" font-size="9">Structure</text>
<line x1="528" y1="52" x2="528" y2="196" stroke="#b91c1c" stroke-width="1.5"/>
<text x="34" y="112" fill="#64748b" font-size="9.5" font-weight="700">COLLAPSE THE</text>
<text x="34" y="124" fill="#64748b" font-size="9.5" font-weight="700">EMPLOYER EVENT</text>
<rect x="130" y="102" width="112" height="18" rx="3" fill="#059669" opacity="0.75"/>
<rect x="242" y="102" width="86" height="18" rx="3" fill="#059669" opacity="0.75"/>
<rect x="328" y="102" width="46" height="18" rx="3" fill="#94a3b8" opacity="0.45"/>
<rect x="374" y="102" width="96" height="18" rx="3" fill="#059669" opacity="0.75"/>
<line x1="470" y1="94" x2="470" y2="196" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="34" y="158" fill="#64748b" font-size="9.5" font-weight="700">AND THE</text>
<text x="34" y="170" fill="#64748b" font-size="9.5" font-weight="700">CONTRACTOR&#39;S</text>
<rect x="130" y="148" width="112" height="18" rx="3" fill="#059669" opacity="0.75"/>
<rect x="242" y="148" width="86" height="18" rx="3" fill="#059669" opacity="0.75"/>
<rect x="328" y="148" width="96" height="18" rx="3" fill="#059669" opacity="0.75"/>
<line x1="424" y1="140" x2="424" y2="196" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="470" y="212" text-anchor="middle" fill="#059669" font-size="9.5">but-for the rock</text>
<text x="528" y="212" text-anchor="middle" fill="#b91c1c" font-size="9.5">actual</text>
<rect x="34" y="222" width="572" height="24" rx="6" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="238" fill="#64748b" font-size="10.5">The distance between the solid line and the first dashed one is the claim.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">But-for, made mechanical. Which is why it reads as obviously fair right up until you ask how the arrows were decided.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 224" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT YOU LEAVE OUT, YOU KEEP</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the residue rule, and why it points in one direction only</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">IDENTIFIED AND REMOVED</text>
<text x="54" y="97" fill="#475569" font-size="10.5">events you modelled, on either side, come out of the programme</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="134" fill="#64748b" font-size="10.5" font-weight="700">NOT IDENTIFIED</text>
<text x="54" y="151" fill="#64748b" font-size="10.5">stays in the collapsed programme, still pushing the date out</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.18" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#64748b" font-size="10.5" font-weight="700">AND IF IT CANNOT BE SHOWN TO BE THEIRS</text>
<text x="54" y="205" fill="#64748b" font-size="10.5">it is treated as yours &#8212; silence has a default, and the default is not neutral</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The method therefore rewards finding every event you can, including ones you would rather not discuss.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 238" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHERE IT FITS, AND WHERE IT DOESN&#39;T</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the literature is blunt: it is inapplicable more often than it is appropriate</text>
<rect x="34" y="60" width="278" height="108" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">SUITED TO</text>
<text x="54" y="104" fill="#475569" font-size="10">work that runs as a line</text>
<text x="54" y="122" fill="#475569" font-size="10">tunnels, roads, bridges</text>
<text x="54" y="140" fill="#475569" font-size="10">earthworks, pipelines</text>
<text x="54" y="158" fill="#64748b" font-size="10">as-built logic is nearly given</text>
<rect x="328" y="60" width="278" height="108" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">BADLY SUITED TO</text>
<text x="348" y="104" fill="#64748b" font-size="10">buildings with parallel trades</text>
<text x="348" y="122" fill="#64748b" font-size="10">fit-out, services, commissioning</text>
<text x="348" y="140" fill="#64748b" font-size="10">anything heavily resequenced</text>
<text x="348" y="158" fill="#64748b" font-size="10">as-built logic is invented</text>
<rect x="34" y="184" width="572" height="42" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="204" fill="#64748b" font-size="10.5">The test is simple: on this job, could two competent analysts independently draw the same</text>
<text x="54" y="220" fill="#64748b" font-size="10.5">as-built arrows? If not, the subtraction is being done on somebody&#39;s opinion.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Linear work makes the logic almost self-evident. Everything else makes it an argument dressed as a calculation.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Take the delay out. See what remains.</h2>

<p>Week 2 introduced the but-for test as the ordinary way of thinking about causation: remove the event, and ask whether the delay still happens. This method is that test turned into a procedure.</p>

<p>Build a programme of what actually happened. Identify the delay events inside it. Then pull them out, one at a time, and let the calculation tell you when the job would have finished without them. The distance between that date and the real one is the claim.</p>

""" + FIG1 + """

<p>It is the most immediately persuasive idea in the subject. Nothing hypothetical is inserted. Nothing is projected forward. You start from facts and remove things, which feels like the opposite of modelling.</p>

<p>That feeling is worth interrogating, because it is where the trouble lives.</p>

<h2>What it does not need</h2>

<p>Something unusual first, because it explains why this method survives at all.</p>

<p>It requires no baseline. Not a weak one &#8212; none. A job with no accepted programme, or one so defective that Week 5's checks fail it outright, can still be analysed this way. It also requires no update series.</p>

<p>Of everything in this phase, this is the only method that needs neither the plan nor the contemporaneous record of the plan. It needs one thing: an as-built good enough to carry logic. That makes it the technique of last resort which isn't, in itself, a bad answer.</p>

<h2>The residue rule</h2>

<p>Now the property that makes this method behave differently from every other one.</p>

""" + FIG2 + """

<p>You collapse the events you have identified. Anything you have not identified stays in the programme, still pushing the completion date out. And if a piece of the remaining delay cannot be shown to be the employer's, it is treated as the contractor's.</p>

<p>Read that as an incentive rather than a rule, because that is how it operates. The analyst is pushed to find and model every delay event that can be found &#8212; including the contractor's own, because leaving one out doesn't hide it. It simply sits in the residue, and the residue is presumed to belong to you.</p>

<p>That is an unusual and rather healthy pressure. Most methods reward selective attention. This one punishes it.</p>

<h2>The static logic problem</h2>

<p>Here is the technical objection, and it is the one that decides whether the analysis holds.</p>

<p>To collapse anything you first need as-built logic: an arrow saying this activity waited for that one. Week 7 established that those arrows are inferences rather than records. This method then does something the earlier ones don't &#8212; it makes them load-bearing, because the collapse propagates through them.</p>

<p>And the logic stays fixed. It is the same before the collapse and after it. But a job without the rock would not have been built in the same order; the contractor would have resequenced, taken different work first, moved the rig somewhere else. Remove a delay in reality and the critical path shifts. Remove it in this model and the critical path is held in place by arrows drawn from a job in which the delay did happen.</p>

<p>So the method answers what the recorded sequence would have produced without the event &#8212; not what the contractor would actually have done. Those are different questions, and on a job with any real resequencing they give different answers.</p>

<h2>The order you remove them in</h2>

<p>One more thing sits underneath the arithmetic, and it is easy to miss because the software never asks.</p>

<p>Done well, the collapse is iterative: you remove the employer's events and read a date, then remove the contractor's and read another, and the comparison between those runs is what separates the two parties' contributions. That is the method at its best, and it's the reason it can isolate one from the other at all.</p>

<p>But when both sets of events overlap the same stretch of programme, the sequence in which you strip them out changes what each one appears to have caused. Take the employer's out first and the contractor's delay is left holding the date. Take the contractor's out first and the employer's is. Neither run is wrong; they are answers to slightly different questions, and a report that shows only one of them has quietly chosen a side.</p>

<p>Show both. Where they differ is not a flaw in your analysis &#8212; it is the overlap itself, surfacing, and it is the subject the next phase opens with.</p>

<h2>Three things it cannot see</h2>

<p>Following from that, a short list worth having in mind before choosing it.</p>

<p>It cannot tell you what anybody intended at the time. There is no contemporaneous view in it at all; every judgement is made looking backwards from the end.</p>

<p>It cannot identify the contemporaneous critical path &#8212; which path was actually driving in March. That information lives in the updates, and this method does not use them.</p>

<p>And it cannot distinguish a contractor pacing its work &#8212; deliberately slowing because something else was holding the job anyway &#8212; from a contractor causing critical delay. Both look identical in an as-built, and the difference between them is worth a great deal of money.</p>

<h2>Where it belongs</h2>

""" + FIG3 + """

<p>The honest summary in the literature is that there are more situations where this technique doesn't apply than situations where it does. That is a strong statement about a method in common use, and it comes with a sensible qualification: it suits work that runs as a line.</p>

<p>On a tunnel, a road, a pipeline or a bulk earthworks job, the as-built logic is close to self-evident. You cannot line a section before you have driven it. The arrows are given by the work, not by the analyst, and the central weakness largely dissolves.</p>

<p>On a building with a dozen trades working in parallel, in a sequence that changed four times, the arrows are the analyst's opinion. The subtraction is then being performed on that opinion, with CPM arithmetic lending it a precision it hasn't earned.</p>

<p>The practical test is one question: on this job, would two competent analysts working independently draw the same as-built logic? If the answer is obviously yes, the method is available. If it is obviously no, everything downstream is contestable.</p>

<h2>Running two on purpose</h2>

<p>One piece of advice from the literature that applies well beyond this method.</p>

<p>Where acceleration or an early completion programme is in issue, it is worth deliberately running both a modelled technique and one built only on as-built data, and putting both in front of the tribunal. Not as hedging &#8212; as information. Two methods resting on different assumptions give a decision-maker a range and, more usefully, show where the assumptions are actually doing the work.</p>

<p>If both methods land close together, that convergence is the strongest thing in your report. If they diverge badly, you have learned something important about your own case before the other side explains it to you.</p>

<h2>Practical insight</h2>

<p>You can test whether this method is even open to you in half an hour, without building anything.</p>

<p>Take ten consecutive activities from a disputed period and, for each, write the reason it started when it did. Not the date &#8212; the reason. Waiting on the preceding activity. Waiting on a delivery. Waiting on access. Crew was elsewhere.</p>

<p>Now count how many of those reasons come from a document rather than from somebody's recollection. If most of them are documented, you have as-built logic and this method is genuinely available. If most are recollection, you can still produce the analysis &#8212; the software will not stop you &#8212; but what you will have produced is a collapse of your own assumptions, and it will be described that way by the person reading it.</p>

<h2>Key takeaways</h2>

<p>&#10004; The method makes the but-for test mechanical: build the as-built, remove the events, read the date that remains.</p>

<p>&#10004; It needs no baseline and no updates, making it the only technique here that survives having neither.</p>

<p>&#10004; Unidentified delay stays in the collapsed result and, if it cannot be shown to be the employer's, is treated as yours.</p>

<p>&#10004; That rule rewards finding every event, including your own, which is unusual among these methods.</p>

<p>&#10004; As-built logic is inferred, and this method makes those inferences load-bearing by collapsing through them.</p>

<p>&#10004; The logic stays static while a real job would have resequenced, so the answer describes the recorded sequence rather than the likely one.</p>

<p>&#10004; Where both parties' events overlap, the order of removal changes the result; run it both ways and show the difference.</p>

<p>&#10004; It suits linear work where the arrows are given by the job, and is contestable everywhere else.</p>

<h2>What&#39;s coming next</h2>

<p>Five methods, five sets of assumptions, five defensible answers. That is the phase, and it ends by facing what it has built: two competent analysts, the same records, and numbers weeks apart. Next week is why that happens, why it is not evidence of bad faith, and what a claim can do about it &#8212; which turns out to be more than most reports attempt.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 15 &#183; Why two analysts disagree &#183; coming soon</span>
                                    <h4>Same facts. Two answers. Both defensible</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Two Bars, And What They Leave Out &#8212; The Project Control Hub</title>",
                  "<title>Take The Delay Out. See What Remains &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Two Bars, And What They Leave Out | The Project Control Hub"',
                  'content="Take The Delay Out. See What Remains | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-13.html", "claim-week-14.html")
    s = s.replace('<span>Week 13<span class="crumb-title"> &#183; As-planned versus as-built</span></span>',
                  '<span>Week 14<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 13",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 14", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · May 31, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; May 31, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week14.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 13", "claim-week-13.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    body_only = page[page.index('<div class="content-preview"'):page.index("<!-- PAYWALL CTA -->")]
    fwd = sorted({m for m in re.findall(r"Week (\d+)", body_only) if int(m) > WEEK_N})
    if fwd:
        sys.exit("HATA: govdede numarali ileri atif: Week %s" % ", ".join(fwd))
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-14.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 14 &#183; Collapsed as-built &#183; coming soon</span>\n'
            '                                    <h4>Take the delay out. See what remains</h4>',
            '<span class="next-week-tag">Week 14 &#183; Collapsed as-built</span>\n'
            '                                    <h4>Take the delay out. See what remains.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-14.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 14" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 14, title: "Collapsed as-built — subtraction, and the judgement hidden in it",\n'
           '          short: "Collapsed as-built", status: "upcoming" },')
    new = ('        { n: 14, title: "Collapsed as-built — subtraction, and the judgement hidden in it",\n'
           '          short: "Collapsed as-built", status: "live", page: "claim-week-14.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 14 live (%s)" % DATE)
    elif 'page: "claim-week-14.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 14 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-14.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-14.html</loc>\n"
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
