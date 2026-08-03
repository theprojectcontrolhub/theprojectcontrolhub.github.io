#!/usr/bin/env python3
"""claim-week-9.html — Track 5, hafta 9. Sablon: claim-week-8.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-8.html", "claim-week-9.html"
PREV_TITLE = "The evidence nobody thought to keep."
TITLE = "Pick the method your records support."
CRUMB = "Choosing a method"
DATE = "May 3, 2028"
DESC = ("Two industry documents classify the delay methods, and neither is law, neither has "
        "universal acceptance, and both agree that choosing between them is the most subjective "
        "step in the whole exercise. Claims &amp; Delay Analysis Week 9.")
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
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO DOCUMENTS, TWO PURPOSES</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">they overlap, they disagree in places, and neither one is binding on anybody</text>
<rect x="34" y="60" width="278" height="132" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE SCL PROTOCOL</text>
<text x="54" y="104" fill="#475569" font-size="10">first published 2002, since revised</text>
<text x="54" y="122" fill="#475569" font-size="10">broad: entitlement, records, disruption</text>
<text x="54" y="140" fill="#475569" font-size="10">pushes for assessment close to the event</text>
<text x="54" y="162" fill="#64748b" font-size="10">expressly not a statement of law</text>
<text x="54" y="180" fill="#64748b" font-size="10">cited in UK court and arbitral decisions</text>
<rect x="328" y="60" width="278" height="132" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="82" fill="#059669" font-size="10.5" font-weight="700">AACE RP 29R-03</text>
<text x="348" y="104" fill="#475569" font-size="10">issued 2007, forensic schedule analysis</text>
<text x="348" y="122" fill="#475569" font-size="10">narrower, and considerably more technical</text>
<text x="348" y="140" fill="#475569" font-size="10">built around terminology and method naming</text>
<text x="348" y="162" fill="#64748b" font-size="10">aim: reduce the subjectivity in the field</text>
<text x="348" y="180" fill="#64748b" font-size="10">adds forum and procedure as factors</text>
<text x="320" y="216" text-anchor="middle" fill="#94a3b8" font-size="10.5">Neither has universal acceptance among the people who use them for a living.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Guidance, not authority. Citing one does not win an argument; it tells the reader which conventions you are using.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 244" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT ACTUALLY DECIDES THE CHOICE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">roughly in the order they eliminate options</text>
<rect x="34" y="60" width="572" height="36" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="83" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">1 THE RECORDS</tspan> &#8212; what survives decides what can be run at all</text>
<rect x="34" y="104" width="572" height="36" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="127" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">2 WHEN YOU ARE ASKING</tspan> &#8212; during the works, or years afterwards</text>
<rect x="34" y="148" width="572" height="36" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="171" fill="#475569" font-size="10.5"><tspan fill="#059669" font-weight="700">3 THE CONTRACT</tspan> &#8212; whether it names a method or a procedure you must follow</text>
<rect x="34" y="192" width="572" height="36" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="215" fill="#64748b" font-size="10.5"><tspan font-weight="700">4 THE FORUM</tspan> &#8212; who decides, and what they are used to seeing</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The fourth is the one the American guidance adds and the one engineers forget. Proportionality sits over all of them.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 252" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT YOUR RECORDS LEAVE OPEN</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the honest version of method selection, and the reason this phase runs in this order</text>
<rect x="34" y="60" width="572" height="42" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="78" fill="#64748b" font-size="10.5" font-weight="700">BASELINE ONLY &#8212; no updates, thin site record</text>
<text x="54" y="95" fill="#64748b" font-size="10.5">you can model events into the plan, and that is very nearly all you can do</text>
<rect x="34" y="112" width="572" height="42" rx="8" fill="#059669" opacity="0.05" stroke="#a7f3d0"/>
<text x="54" y="130" fill="#059669" font-size="10.5" font-weight="700">BASELINE PLUS A CLEAN UPDATE SERIES</text>
<text x="54" y="147" fill="#475569" font-size="10.5">period-by-period analysis opens up, and with it the strongest contemporaneous story</text>
<rect x="34" y="164" width="572" height="42" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="182" fill="#059669" font-size="10.5" font-weight="700">A FULL AS-BUILT AS WELL</text>
<text x="54" y="199" fill="#475569" font-size="10.5">comparison and subtraction methods become available; you can choose rather than accept</text>
<rect x="34" y="216" width="572" height="30" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="236" fill="#64748b" font-size="10.5">Nobody in year three gets to move up this list. The rung was fixed while the job was running.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">This is the whole argument of the track in one picture, and the reason Phase B came before Phase C.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Pick the method your records support.</h2>

<p>Phase C is about techniques, and there are six or seven of them worth knowing. Before any of that, the question that decides most of the outcome: which one are you entitled to use?</p>

<p>Not <em>allowed</em> in a contractual sense. Able. Phase B spent four weeks on the baseline, the site record, the as-built and the update series precisely because those four things, and not your professional preference, determine which techniques will survive contact with somebody who wants them not to.</p>

<h2>Two documents, and what they are for</h2>

<p>The field has two reference works that most people cite and rather fewer have read carefully.</p>

""" + FIG1 + """

<p>The Society of Construction Law published its Delay and Disruption Protocol in 2002, and it has been revised since. It is the broader of the two: it covers entitlement, records, disruption and the practical conduct of claims, and its purpose is guidance on the recurring problems that arise when one party wants time or money from the other.</p>

<p>The American document, AACE's Recommended Practice for forensic schedule analysis, arrived in 2007. It is narrower and much more technical, built around naming things precisely &#8212; and its stated aim is to reduce the subjectivity in a field where two experts could describe the same exercise in incompatible language.</p>

<p>Two things about them are worth holding onto. The Protocol says of itself that it is not a statement of law. And neither document has achieved universal acceptance among the consultants and expert witnesses who work with them daily.</p>

<p>So citing one is not a trump card. What it does is tell your reader which conventions you have adopted, which is genuinely useful and much less than people usually claim for it.</p>

<h2>The finding that should be more famous</h2>

<p>Buried in the guidance on selection is an admission that reframes this whole phase.</p>

<p>Choosing the technique is the most subjective task in the exercise. And even where both parties agree on which technique to use, the way each side applies it can diverge so far that neither will accept the other's conclusion.</p>

<p>Read that twice, because it means the disagreement this phase closes on is not a failure of competence or good faith. It is structural. Agreement on the method is not agreement on the answer, and anybody who has watched two experts converge on time impact analysis and then produce numbers weeks apart already knows it.</p>

<p>The mechanism is easier to see with a period-based analysis. Two analysts agree to look at the job window by window. One chooses monthly windows because that matches the update cycle; the other chooses windows bounded by the delay events themselves, on the reasonable ground that a window straddling two events cannot separate them. Both choices are defensible and both are conventional. They will not produce the same number, because the answer to <em>what was driving</em> depends on where you draw the line.</p>

<p>No amount of shared vocabulary closes that gap. What closes it, partially, is each side saying plainly what it chose and why &#8212; which is the modest thing the taxonomies are actually good for.</p>

<h2>What actually decides it</h2>

""" + FIG2 + """

<p>Both documents set out selection factors, and unsurprisingly the lists resemble each other. The American one adds two the British one leaves out: the forum in which the dispute will be decided, and the legal and procedural requirements that come with it &#8212; drawn from US case law and from what American courts are accustomed to seeing.</p>

<p>Engineers tend to find that addition slightly distasteful, as though the right answer should not depend on the room. It does though. An analysis that a tribunal cannot follow is worth less than a simpler one it can, and a method a particular forum has repeatedly criticised starts every hearing at a disadvantage no amount of rigour recovers.</p>

<p>Proportionality sits over all four factors. A twelve-week dispute on a modest job does not justify a forensic exercise costing more than the claim, and reaching for one signals inexperience rather than thoroughness.</p>

<h2>Close to the event, or long afterwards</h2>

<p>Underneath the technical disagreements sits a genuine difference of philosophy, and it is worth naming because it explains why the guidance and the case law can seem to pull apart.</p>

<p>Judges see these disputes only after everything has happened, so the legal analysis is inevitably retrospective: what caused what, and which cause dominated. The Protocol deliberately pushes the other way. Its aim is to get parties assessing entitlement as close in time to the event as possible, and to discourage the wait-and-see approach where everybody keeps quiet until the end and then argues about thirty months at once.</p>

<p>Both positions are coherent. They simply answer different questions &#8212; one asks what should be decided now, the other what should be found later &#8212; and a great deal of unnecessary argument comes from people quoting one at somebody who is doing the other.</p>

<p>It is also the reason the method mandated by many contracts and the method eventually used in a dispute are frequently not the same technique, a point <a href="contract-week-9.html">Contract Week 9</a> approached from the entitlement side.</p>

<h2>Which rung you are standing on</h2>

<p>Strip away the guidance and the practical position is simpler and harsher.</p>

""" + FIG3 + """

<p>With a baseline and very little else, your options are essentially limited to modelling events into the plan and re-running it &#8212; which Week 5 showed is exactly the family that dies if the baseline is weak. That is an uncomfortable place to be, and a lot of claims are made from it.</p>

<p>Add a clean update series and period-by-period analysis becomes available, which is where the strongest contemporaneous arguments live.</p>

<p>Add a defensible as-built as well and you can compare, or subtract, or do both and see whether they agree. At that point you are choosing a method rather than accepting the only one left.</p>

<p>Nobody moves up this list retrospectively. Where you stand was fixed by what the project recorded while it was running, which is why this phase could not have come first.</p>

<h2>One more caution about the guidance</h2>

<p>Both documents are living things. The Protocol has been through revision, and specific recommendations in it have attracted sustained criticism &#8212; the treatment of time impact analysis in particular has been argued over by serious people for years.</p>

<p>The practical consequence is small and easy: say which edition you used, and date it. An analysis that cites a protocol without a version is quoting a moving target, and the first person to notice will use it to suggest the rest of your work was done with the same care.</p>

<h2>Practical insight</h2>

<p>Before reading another word about techniques, write down four answers for a live or recent dispute on your own job.</p>

<p>Do you have the accepted baseline in native format? Do you have an unbroken series of submitted updates covering the disputed period? Can you build an as-built for that period from records rather than memory? And where will this be decided &#8212; a negotiation, an adjudication, an arbitration?</p>

<p>The first three answers tell you which of the next five weeks apply to you. The fourth tells you how much of it the audience will tolerate.</p>

<p>If the honest answers are no, no and partly, that is worth knowing before spending three months building an analysis that a competent reviewer will take apart in an afternoon. It is also, if the job is still running, a list of things you can still change.</p>

<h2>Key takeaways</h2>

<p>&#10004; The two industry references are guidance rather than law, and neither has universal acceptance among practitioners.</p>

<p>&#10004; Citing a protocol tells the reader which conventions you adopted; it does not settle anything by itself.</p>

<p>&#10004; Selecting a technique is the most subjective step, and agreement on the technique does not produce agreement on the answer.</p>

<p>&#10004; Selection turns on records first, then timing, then the contract, then the forum in which it will be decided.</p>

<p>&#10004; The guidance pushes for assessment close to the event; the case law is inevitably retrospective, and the two answer different questions.</p>

<p>&#10004; What your records support decides which methods are open to you, and that was settled while the job was running.</p>

<p>&#10004; Always state the edition of any protocol you rely on, because the recommendations have changed and the criticism has not stopped.</p>

<h2>What&#39;s coming next</h2>

<p>The methods now arrive in order of how much evidence they need, starting with the one that needs almost none. Next week is impacted as-planned: delay events modelled into a programme that was never built, why it remains the most commonly submitted analysis in the industry, and why it is the first thing an experienced reviewer looks for a reason to reject.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 10 &#183; Impacted as-planned &#183; coming soon</span>
                                    <h4>A forecast made after the fact</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Evidence Nobody Thought To Keep &#8212; The Project Control Hub</title>",
                  "<title>Pick The Method Your Records Support &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Evidence Nobody Thought To Keep | The Project Control Hub"',
                  'content="Pick The Method Your Records Support | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-8.html", "claim-week-9.html")
    s = s.replace('<span>Week 8<span class="crumb-title"> &#183; Programme updates</span></span>',
                  '<span>Week 9<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 8",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 9", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Apr 26, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Apr 26, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="9"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week9.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 8", "claim-week-8.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-9.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 9 &#183; Choosing a method &#183; coming soon</span>\n'
            '                                    <h4>Pick the method your records support</h4>',
            '<span class="next-week-tag">Week 9 &#183; Choosing a method</span>\n'
            '                                    <h4>Pick the method your records support.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-9.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 9" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase C — Methods, by the Evidence They Need", n: 9,\n'
           '          title: "Choosing a method — what the SCL and AACE taxonomies are for",\n'
           '          short: "Choosing a method", status: "upcoming" },')
    new = ('        { phase: "Phase C — Methods, by the Evidence They Need", n: 9,\n'
           '          title: "Choosing a method — what the SCL and AACE taxonomies are for",\n'
           '          short: "Choosing a method", status: "live", page: "claim-week-9.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 9 live (%s)" % DATE)
    elif 'page: "claim-week-9.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 9 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-9.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-9.html</loc>\n"
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
