#!/usr/bin/env python3
"""claim-week-10.html — Track 5, hafta 10. Sablon: claim-week-9.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-9.html", "claim-week-10.html"
PREV_TITLE = "Pick the method your records support."
TITLE = "A forecast made after the fact."
CRUMB = "Impacted as-planned"
DATE = "May 10, 2028"
DESC = ("Take the baseline, insert the delay events, re-run it, and read off the answer. It needs "
        "almost no evidence, which is why it is everywhere &#8212; and why an experienced reviewer "
        "starts by looking for the reason to reject it. Claims &amp; Delay Analysis Week 10.")
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
<svg viewBox="0 0 640 244" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE WHOLE METHOD, IN THREE STEPS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">no as-built, no updates, no site record &#8212; a baseline and a list of events</text>
<text x="34" y="70" fill="#64748b" font-size="10" font-weight="700">THE BASELINE</text>
<rect x="34" y="78" width="200" height="18" rx="4" fill="#059669" opacity="0.75"/>
<text x="134" y="91" text-anchor="middle" fill="#fff" font-size="9.5">Piling</text>
<rect x="234" y="78" width="150" height="18" rx="4" fill="#059669" opacity="0.75"/>
<text x="309" y="91" text-anchor="middle" fill="#fff" font-size="9.5">Pile caps</text>
<line x1="384" y1="70" x2="384" y2="104" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="392" y="91" fill="#64748b" font-size="9.5">planned completion</text>
<text x="34" y="128" fill="#64748b" font-size="10" font-weight="700">INSERT THE EVENT</text>
<rect x="34" y="136" width="120" height="18" rx="4" fill="#059669" opacity="0.75"/>
<rect x="154" y="136" width="70" height="18" rx="4" fill="#dc2626" opacity="0.55"/>
<text x="189" y="149" text-anchor="middle" fill="#fff" font-size="9">rock</text>
<rect x="224" y="136" width="80" height="18" rx="4" fill="#059669" opacity="0.75"/>
<rect x="304" y="136" width="150" height="18" rx="4" fill="#059669" opacity="0.75"/>
<text x="379" y="149" text-anchor="middle" fill="#fff" font-size="9.5">Pile caps</text>
<line x1="454" y1="128" x2="454" y2="162" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3 2"/>
<text x="462" y="149" fill="#b91c1c" font-size="9.5">new completion</text>
<rect x="34" y="180" width="572" height="50" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="200" fill="#059669" font-size="10.5" font-weight="700">READ OFF THE DIFFERENCE</text>
<text x="54" y="218" fill="#475569" font-size="10.5">the gap between the two dashed lines is the extension of time being claimed</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Simple, quick, and answering a question about a project that never existed.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHY IT IS EVERYWHERE, AND WHY IT FAILS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same property produces both columns</text>
<rect x="34" y="60" width="278" height="158" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">STRENGTHS</text>
<text x="54" y="106" fill="#475569" font-size="10">anyone in the room can follow it</text>
<text x="54" y="126" fill="#475569" font-size="10">fewest variables in the cause&#8211;effect chain</text>
<text x="54" y="146" fill="#475569" font-size="10">needs no as-built programme</text>
<text x="54" y="166" fill="#475569" font-size="10">needs no progressed programmes</text>
<text x="54" y="186" fill="#475569" font-size="10">can be run while the job is still going</text>
<text x="54" y="208" fill="#059669" font-size="10">cheap, fast, and available to everybody</text>
<rect x="328" y="60" width="278" height="158" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">WEAKNESSES</text>
<text x="348" y="106" fill="#64748b" font-size="10">ignores changes to logic and durations</text>
<text x="348" y="126" fill="#64748b" font-size="10">a theoretical answer to a hypothetical</text>
<text x="348" y="146" fill="#64748b" font-size="10">cannot identify true concurrent delay</text>
<text x="348" y="166" fill="#64748b" font-size="10">your own delays never appear at all</text>
<text x="348" y="186" fill="#64748b" font-size="10">can return more days than the job lost</text>
<text x="348" y="208" fill="#64748b" font-size="10">every weakness follows from the strengths</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">It needs no evidence of what happened. That is the selling point, and it is the whole objection.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 226" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHEN IT HOLDS UP</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the method is not disgraced &#8212; it is misapplied</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">EARLY, AND ON A CURRENT PLAN</text>
<text x="54" y="97" fill="#475569" font-size="10.5">one event, close to the baseline, before the plan has been overtaken by events</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#059669" opacity="0.06" stroke="#a7f3d0"/>
<text x="54" y="134" fill="#059669" font-size="10.5" font-weight="700">AS A NEGOTIATING INSTRUMENT</text>
<text x="54" y="151" fill="#475569" font-size="10.5">where both sides agree the building blocks, a shared simple model beats no model</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#64748b" font-size="10.5" font-weight="700">NOT: THIRTY MONTHS AND FORTY EVENTS, RECONSTRUCTED IN YEAR THREE</text>
<text x="54" y="205" fill="#64748b" font-size="10.5">which is, almost invariably, where it turns up</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The technique is fine. The trouble is that it is reached for precisely when it has stopped being appropriate.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">A forecast made after the fact.</h2>

<p>Of the four primary techniques, this is the one that needs the least, which is why it turns up more often than the other three combined.</p>

<p>The mechanics take a paragraph. Take the accepted baseline. Build a small network representing each delay event &#8212; a fragnet &#8212; and insert it into the logic at the point where it belongs. Re-run the calculation. The completion date moves, and the distance it moves is the extension of time you are claiming.</p>

""" + FIG1 + """

<p>That is the whole of it. No as-built. No update series. No site diaries. A baseline, a list of events, and an afternoon.</p>

<h2>The question it actually answers</h2>

<p>Here is where it gets uncomfortable, and it is worth stating precisely because the imprecision is where claims die.</p>

<p>An impacted as-planned analysis does not tell you what delayed the project. It tells you what <em>would</em> have delayed the project, if the plan had been followed exactly and nothing had gone wrong except the events you inserted.</p>

<p>That is a hypothetical question, and the answer is a forecast. It happens to be a forecast produced after the events it forecasts, which is an unusual thing for a document to be, and the strangeness is not cosmetic.</p>

<p>Every one of the objections below comes from that single property.</p>

<h2>Why it is everywhere, and why it fails</h2>

""" + FIG2 + """

<p>The strengths are real and shouldn't be sneered at. It is easy to understand, which matters more than engineers like to admit &#8212; Week 9 made the point that an analysis a tribunal can't follow is worth less than a simpler one it can. It carries the fewest variables between cause and effect. It can be run during the works. And it needs none of the evidence that Phase B spent four weeks describing.</p>

<p>The weaknesses are the same facts read from the other side.</p>

<p>Because it takes no account of what actually happened, it cannot see that the logic changed, that durations turned out different, or that the sequence was reorganised in month four. It cannot identify true concurrent delay, because your own delays are simply not in the model. And it will happily return an extension longer than the delay the job actually suffered, which is the point at which a reviewer stops reading and starts drafting a rejection.</p>

<h2>The delays that are not in the picture</h2>

<p>Take this job. Model the rock into the baseline, re-run, and out comes a number of days.</p>

<p>What the model does not contain is anything the contractor did. If the piling gang was already two weeks behind for its own reasons when the rock appeared, the impacted as-planned analysis is blind to it &#8212; not because it was concealed, but because the method has no place to put it. The baseline shows the plan, the fragnet shows the event, and everything else on the job is absent by construction.</p>

<p>So the answer arrives with the contractor's own delay silently removed. That is not fraud. It is the arithmetic doing exactly what it was asked to do, and the reason the other side's first question is always some version of <em>what else was going on that month?</em></p>

<h2>One at a time, or all at once</h2>

<p>There's a second-order choice inside the method that changes the number.</p>

<p>Events can be inserted one at a time, in chronological order, re-running the calculation after each; or all of them can be inserted together and the model run once. The first is more defensible and slower. The second is quicker and tends to produce a larger figure, because interactions between events get counted in ways nobody has examined.</p>

<p>Neither approach is illegitimate, and this is the same pattern Week 9 described with window lengths: a conventional choice inside an agreed method, made silently, moving the answer. Say which one you did.</p>

<h2>The paradox at the centre</h2>

<p>Now the awkward part, and it is worth sitting with.</p>

<p>The method needs a baseline that is contractually compliant and genuinely represents what the contractor intended before starting. If the baseline has the defects Week 5 catalogued &#8212; open ends, constrained dates, missing scope &#8212; you have to repair it before you can impact anything.</p>

<p>But repairing a model whose entire output is hypothetical adds a further layer of your own judgement to a result that was already theoretical. You are now presenting a forecast, made after the fact, from a plan you partly rebuilt.</p>

<p>Which produces the paradox: the method is least defensible exactly where it is most tempting. A weak baseline is precisely the situation in which a team has no update series and no usable as-built either &#8212; and impacted as-planned is the only method left standing.</p>

<h2>It points both ways</h2>

<p>One property that rarely gets mentioned: nothing about this method belongs to the contractor.</p>

<p>An employer can build the same model containing only the contractor's delays and produce the mirror image &#8212; a projection showing the works finishing late for reasons the employer had no part in, and therefore an argument that delay damages should run. Same technique, same assumptions, same weaknesses, pointed the other way.</p>

<p>Worth remembering before serving one. A method resting on <em>the plan was right and would have been followed</em> is available to whoever wants it, and the party with the better records is usually the party that would rather not be handed it.</p>

<p>It also explains a pattern worth recognising. Where both sides run an impacted as-planned, the two reports often agree on every date, every fragnet duration and every piece of arithmetic, and differ only in which events went into the model. <a href="risk-week-5.html">Risk Week 5</a> priced the rock at $48,450; whether the rock belongs in the model at all is not a technical question, and no amount of checking the calculation will answer it.</p>

<h2>Where it does hold up</h2>

""" + FIG3 + """

<p>None of this makes the technique disreputable. It makes it a tool with a narrow correct application, reached for far outside it.</p>

<p>Used early, on one event, against a plan that has not yet been overtaken, it is a sensible way to ask what an instruction is about to cost. That is essentially the contemporaneous use, and it is the door into next week.</p>

<p>It also has a role the literature is explicit about and practitioners rarely mention: as a negotiating instrument. Where both parties can agree the baseline, the events and the fragnets, a shared simple model that everybody understands will settle more disputes than a rigorous one that only one side can check. Agreement on a rough answer beats a correct answer nobody accepts.</p>

<h2>Practical insight</h2>

<p>If you have an impacted as-planned analysis in front of you &#8212; yours or theirs &#8212; ask four questions in this order.</p>

<p>Which baseline was used, and was it the accepted one or a repaired version? If repaired, is there a schedule of what was changed? Were the events inserted one at a time or together? And what was the contractor's own progress at the moment each event was inserted?</p>

<p>The fourth question is the one that decides the meeting. If the analysis cannot answer it &#8212; and by construction it usually can't &#8212; then what you are holding is a statement about a plan, offered as a statement about a project.</p>

<p>That may still be the best available answer. It is a different thing from being the right one, and the difference is worth saying out loud before somebody else says it for you.</p>

<h2>Key takeaways</h2>

<p>&#10004; Impacted as-planned inserts delay events into the baseline and reads the movement of the completion date as the claim.</p>

<p>&#10004; It needs no as-built, no updates and no site record, which is why it is the most commonly submitted analysis.</p>

<p>&#10004; It answers a hypothetical: what would have happened had the plan been followed and nothing else gone wrong.</p>

<p>&#10004; The contractor's own delays cannot appear in it, so it cannot identify true concurrency and can overstate the entitlement.</p>

<p>&#10004; Inserting events one at a time and inserting them together give different answers; state which you did.</p>

<p>&#10004; Repairing a defective baseline to run it adds your judgement to an already theoretical result, so the method is weakest where it is most tempting.</p>

<p>&#10004; The method is symmetrical: an employer can run it with only your delays in it, on the same assumptions, against you.</p>

<p>&#10004; It is legitimate early, on a current plan, and as a negotiating model both sides agree &#8212; not as a reconstruction of thirty months in year three.</p>

<h2>What&#39;s coming next</h2>

<p>Take the same additive idea and stop pretending the plan never changed. Next week is time impact analysis: the same fragnets inserted not into the original baseline but into the programme as it actually stood on the day the event happened &#8212; the method most contracts point at, the one the guidance argues about most, and the one that needs the update series you may not have.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 11 &#183; Time impact analysis &#183; coming soon</span>
                                    <h4>The method the contract asks for</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Pick The Method Your Records Support &#8212; The Project Control Hub</title>",
                  "<title>A Forecast Made After The Fact &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Pick The Method Your Records Support | The Project Control Hub"',
                  'content="A Forecast Made After The Fact | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-9.html", "claim-week-10.html")
    s = s.replace('<span>Week 9<span class="crumb-title"> &#183; Choosing a method</span></span>',
                  '<span>Week 10<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 9",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 10", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · May 3, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; May 3, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="10"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week10.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 9", "claim-week-9.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-10.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 10 &#183; Impacted as-planned &#183; coming soon</span>\n'
            '                                    <h4>A forecast made after the fact</h4>',
            '<span class="next-week-tag">Week 10 &#183; Impacted as-planned</span>\n'
            '                                    <h4>A forecast made after the fact.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-10.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 10" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 10, title: "Impacted as-planned — delay modelled into a plan that never happened",\n'
           '          short: "Impacted as-planned", status: "upcoming" },')
    new = ('        { n: 10, title: "Impacted as-planned — delay modelled into a plan that never happened",\n'
           '          short: "Impacted as-planned", status: "live", page: "claim-week-10.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 10 live (%s)" % DATE)
    elif 'page: "claim-week-10.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 10 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-10.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-10.html</loc>\n"
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
