#!/usr/bin/env python3
"""claim-week-26.html — Track 5, hafta 26. Faz G acilisi. Sablon: claim-week-25.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-25.html", "claim-week-26.html"
PREV_TITLE = "A number a stranger can rebuild."
TITLE = "Write it for the person hunting holes."
CRUMB = "Assembling a claim"
DATE = "Aug 30, 2028"
WEEK_N = 26
DESC = ("Three people will read your claim and only one of them wants it to succeed. What goes in "
        "the body, what goes in the appendices, why the summary is written last and read first, "
        "and why thickness is not an argument. Claims &amp; Delay Analysis Week 26.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THREE READERS, THREE DIFFERENT DOCUMENTS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">and one submission that has to serve all of them</text>
<rect x="34" y="60" width="186" height="126" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE DECIDER</text>
<text x="54" y="104" fill="#475569" font-size="10">reads the summary,</text>
<text x="54" y="122" fill="#475569" font-size="10">skims the conclusions</text>
<text x="54" y="146" fill="#64748b" font-size="10">wants to know what</text>
<text x="54" y="164" fill="#64748b" font-size="10">happened and how much</text>
<rect x="228" y="60" width="186" height="126" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="248" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE REVIEWER</text>
<text x="248" y="104" fill="#64748b" font-size="10">reads all of it, once,</text>
<text x="248" y="122" fill="#64748b" font-size="10">looking for the weak link</text>
<text x="248" y="146" fill="#64748b" font-size="10">needs to find only</text>
<text x="248" y="164" fill="#64748b" font-size="10">one thing that fails</text>
<rect x="422" y="60" width="184" height="126" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="442" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE LAWYER</text>
<text x="442" y="104" fill="#64748b" font-size="10">reads the entitlement</text>
<text x="442" y="122" fill="#64748b" font-size="10">section and the clauses</text>
<text x="442" y="146" fill="#64748b" font-size="10">wants the legal basis</text>
<text x="442" y="164" fill="#64748b" font-size="10">stated, not implied</text>
<text x="320" y="216" text-anchor="middle" fill="#94a3b8" font-size="10.5">Write the summary for the first, the appendices for the second, and the entitlement section for the third.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Only one of these three is hoping the claim works, and it is not the one with the most time to spend on it.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 232" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">BODY OR APPENDIX</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">one rule, and it settles almost every argument about what goes where</text>
<rect x="34" y="60" width="278" height="110" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE BODY IS THE ARGUMENT</text>
<text x="54" y="104" fill="#475569" font-size="10">what happened, why it is theirs,</text>
<text x="54" y="122" fill="#475569" font-size="10">what it did, what it cost</text>
<text x="54" y="146" fill="#64748b" font-size="10">readable end to end in an evening</text>
<rect x="328" y="60" width="278" height="110" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE APPENDIX IS THE PROOF</text>
<text x="348" y="104" fill="#64748b" font-size="10">records, calculations, programmes,</text>
<text x="348" y="122" fill="#64748b" font-size="10">ledgers, correspondence</text>
<text x="348" y="146" fill="#64748b" font-size="10">nobody reads it end to end, ever</text>
<rect x="34" y="182" width="572" height="34" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="203" fill="#64748b" font-size="10.5">Every assertion in the left-hand box carries a reference into the right-hand one. No exceptions.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Evidence in the body makes it unreadable. Argument in the appendix means nobody will ever find it.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT THE REVIEWER LOOKS FOR FIRST</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">answer these five from your contents page and the review starts well</text>
<rect x="34" y="60" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#475569" font-size="10.5">1 &#183; which method, and does the document say why that one?</text>
<rect x="34" y="96" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="116" fill="#475569" font-size="10.5">2 &#183; which events are in the analysis, and which are not?</text>
<rect x="34" y="132" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="152" fill="#475569" font-size="10.5">3 &#183; where did the as-built logic come from?</text>
<rect x="34" y="168" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="188" fill="#475569" font-size="10.5">4 &#183; was the baseline used as issued, and is every adjustment listed?</text>
<rect x="34" y="204" width="572" height="30" rx="6" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="224" fill="#475569" font-size="10.5">5 &#183; does the modelled completion date resemble the date the job finished?</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A document that answers these in its first ten pages has removed the reviewer&#39;s easiest five attacks.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Write it for the person hunting holes.</h2>

<p>Everything up to here has been about being right. This week is about being believed, and they aren't the same problem. A correct claim badly assembled loses to an adequate claim well assembled more often than anybody in this industry likes to admit.</p>

<p>Start from the audience, because it is not one person.</p>

""" + FIG1 + """

<p>Somebody has to decide, and they will read the summary and possibly the conclusions. Somebody has to review it, and they will read all of it once, looking for the weakest link &#8212; and they need to find only one. And somebody will read the entitlement section for the legal basis and nothing else.</p>

<p>One document, three jobs. The mistake is writing it for the reviewer alone, which produces something forensically complete that the decision-maker never finishes.</p>

<p><a href="week-24.html">Schedule Week 24</a> put the reader in that room two years later, surrounded by lawyers, holding documents assembled by people who had no idea they were writing evidence. This is the week those documents get written on purpose.</p>

<h2>The contract gave you the structure</h2>

<p>Week 25 found the four components of a fully detailed claim sitting in the contract: what happened, why it entitles you, the contemporary records, and the particulars of the amount.</p>

<p>That's the spine of the document, and following it has an underrated advantage. A reviewer working through your claim is checking it against those four things whether you organised around them or not. A submission that presents them in that order is being read on its own terms rather than being taken apart and reassembled by somebody who is not on your side.</p>

<p>Under it sit the analysis and the quantum, in the order this track built them: what happened, what was driving, how much time, how much money.</p>

<h2>The summary is written last and read first</h2>

<p>The executive summary is the only part of the document you can be reasonably certain will be read in full, and it's routinely written in an hour on the last afternoon.</p>

<p>It has four jobs and they map to the four components. What happened, in a paragraph a layperson understands. Why it is the other party's responsibility, with the clause named. What the analysis concluded, including the method and why it was chosen. And the money, split by head, tying exactly to the number on the front page.</p>

<p>It has one prohibition: it can't promise anything the body doesn't deliver. A summary asserting sixty days when the analysis supports forty-five is not an overview, it is the first thing the reviewer will quote back &#8212; and the discrepancy will be read as intent rather than as carelessness.</p>

<p>Write it after the analysis is finished. Writing it first produces a document that argues towards a number decided before anybody looked.</p>

<h2>Show it, do not only say it</h2>

""" + FIG2 + """

<p>Delay claims are difficult to present for reasons that have nothing to do with the merits. They carry specialist vocabulary, and they depend on a mass of different documents &#8212; contracts, minutes, drawings, change orders, notices, correspondence. A submission that relies on hundreds of documents without presenting the relevant ones clearly produces confusion rather than persuasion, and confusion is not neutral. It defaults against the party with the burden, which is you.</p>

<p>The literature is unambiguous about the remedy: use graphics. Studies reported in this field suggest that people retain a small fraction of material delivered purely in words, and several times as much when it is supported visually. Demonstrative exhibits are now routine in every form of dispute resolution for exactly that reason.</p>

<p>For a delay claim that means the as-built against the as-planned, the windows with their driving paths marked, the events on a timeline against the movement of the completion date. Not decoration &#8212; the argument, drawn.</p>

<p>The same source makes a related point about people rather than paper. Expert evidence that is technically impeccable can be close to incomprehensible if it has not been honed for the audience. The same is true of a written claim, and the test is the same: can a competent person outside the industry follow the chain from event to money without help?</p>

<h2>Body or appendix</h2>

<p>One rule settles most arguments about what goes where. The body is the argument. The appendices are the proof.</p>

<p>The body should be readable end to end in an evening by somebody who was not there. The appendices will never be read end to end by anybody, and that is fine &#8212; their purpose is to be checkable, not readable.</p>

<p>Between them runs the discipline that makes the whole thing work: every assertion in the body carries a reference into the appendices. Not most. Every one. A statement in the body with no reference behind it is the exact thing Week 25 described &#8212; a line that stops before it reaches a source, and the one the reviewer will build their response around.</p>

<h2>Thickness is not an argument</h2>

<p>Week 7 recorded an uncomfortable observation from the literature: an elaborate analysis carries no more credibility than a careful one, and what it really does is impose an enormous burden on the party trying to answer it.</p>

<p>That effect is real, and it is worth being honest about the fact that some claims are built to exploit it. It's also a strategy with a short life. A tribunal that suspects it is being buried rather than persuaded starts reading with a different attitude, and the document has then made an enemy of the only person whose opinion counts.</p>

<p>Proportionality applies here as much as it did to choosing a method. The right length is the length that makes the argument checkable, and no more.</p>

<h2>Answer the five questions on the contents page</h2>

""" + FIG3 + """

<p>Week 15 set out the five questions a reviewer asks first. They are the fastest route into any delay report, and every experienced reviewer uses some version of them.</p>

<p>So answer them early and explicitly. A section that states the method and why it was chosen, a schedule listing every event considered, a note on the source of the as-built logic, a table of every baseline adjustment made, and a comparison of the modelled outcome against what actually happened.</p>

<p>Doing this feels like handing the other side a map, and that's precisely what it is. The five easiest attacks on a delay claim are attacks on things the claim never explained. Explaining them first doesn't weaken the document. It forces the argument onto the merits, which is where you wanted it.</p>

<h2>Practical insight</h2>

<p>Take a claim you have written or received and read only the executive summary and the contents page. Then write down what you now know.</p>

<p>Do you know what happened, which clause is relied on, which method was used and why, and how the money splits? If the answer to any of those is no, the document has failed before the reader reached page ten &#8212; and on most claims the answer is no to at least two.</p>

<p>Then pick three assertions at random from the body and follow their references. If a reference is missing, or points to a bundle rather than a document, or points to a document that does not say what the body says it says, you have found the shape of the response you are going to receive.</p>

<p>Both exercises take an hour, and both are considerably cheaper done by you than by them.</p>

<h2>Key takeaways</h2>

<p>&#10004; Being right and being believed are different problems, and the second is decided by assembly.</p>

<p>&#10004; Three people read a claim &#8212; a decider, a reviewer and a lawyer &#8212; and only one of them wants it to work.</p>

<p>&#10004; The contract's four components make the natural spine, and organising around them means being read on your own terms.</p>

<p>&#10004; The executive summary is written last, read first, and must not promise anything the body does not deliver.</p>

<p>&#10004; Complex material presented only in words is largely lost; the argument should be drawn as well as written.</p>

<p>&#10004; The body is the argument and the appendices are the proof, with every assertion referenced into them.</p>

<p>&#10004; Volume is not persuasion, and a tribunal that feels buried rather than helped reads everything differently.</p>

<h2>What&#39;s coming next</h2>

<p>The whole of this week has been written from one side of the table. Next week moves to the other and reads a claim as the person receiving it &#8212; what a competent response actually looks for, in what order, and why becoming good at defending claims is the fastest way anybody ever gets better at making them.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 27 &#183; Defending a claim &#183; coming soon</span>
                                    <h4>Now sit across the table</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>A Number A Stranger Can Rebuild &#8212; The Project Control Hub</title>",
                  "<title>Write It For The Person Hunting Holes &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="A Number A Stranger Can Rebuild | The Project Control Hub"',
                  'content="Write It For The Person Hunting Holes | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-25.html", "claim-week-26.html")
    s = s.replace('<span>Week 25<span class="crumb-title"> &#183; Pricing and substantiation</span></span>',
                  '<span>Week 26<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 25",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 26", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Aug 23, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Aug 23, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week26.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 25", "claim-week-25.html", PREV_TITLE):
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
    if 'href="claim-week-26.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 26 &#183; Assembling a claim &#183; coming soon</span>\n'
            '                                    <h4>Write it for the person hunting holes</h4>',
            '<span class="next-week-tag">Week 26 &#183; Assembling a claim</span>\n'
            '                                    <h4>Write it for the person hunting holes.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-26.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 26" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase G — Presenting the Claim", n: 26,\n'
           '          title: "Assembling a claim — contents, executive summary and appendices",\n'
           '          short: "Assembling a claim", status: "upcoming" },')
    new = ('        { phase: "Phase G — Presenting the Claim", n: 26,\n'
           '          title: "Assembling a claim — contents, executive summary and appendices",\n'
           '          short: "Assembling a claim", status: "live", page: "claim-week-26.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 26 live (%s)" % DATE)
    elif 'page: "claim-week-26.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 26 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-26.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-26.html</loc>\n"
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
