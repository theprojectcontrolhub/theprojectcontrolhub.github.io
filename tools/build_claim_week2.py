#!/usr/bin/env python3
"""claim-week-2.html — Track 5, hafta 2. Sablon: claim-week-1.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-1.html", "claim-week-2.html"
PREV_TITLE = "The notice held. Now price it."
TITLE = "Blame is not causation."
CRUMB = "Cause and effect"
DATE = "Mar 15, 2028"
DESC = ("Everybody agrees the rock was there and the job finished late. Neither fact is disputed, "
        "and together they prove nothing &#8212; the sentence between them is the one most rejected "
        "claims never wrote. Claims &amp; Delay Analysis Week 2.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE TWO-LIST CLAIM</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">both columns true, both columns evidenced, and no sentence joining them</text>
<rect x="34" y="60" width="242" height="150" rx="10" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="54" y="84" fill="#64748b" font-size="10.5" font-weight="700">WHAT WENT WRONG</text>
<text x="54" y="108" fill="#475569" font-size="10.5">the rock</text>
<text x="54" y="128" fill="#475569" font-size="10.5">the late drawing</text>
<text x="54" y="148" fill="#475569" font-size="10.5">the restricted access</text>
<text x="54" y="168" fill="#475569" font-size="10.5">the wet October</text>
<text x="54" y="194" fill="#94a3b8" font-size="10">evidenced from site records</text>
<rect x="364" y="60" width="242" height="150" rx="10" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1"/>
<text x="384" y="84" fill="#64748b" font-size="10.5" font-weight="700">WHAT IT COST</text>
<text x="384" y="108" fill="#475569" font-size="10.5">forty-one days of site costs</text>
<text x="384" y="128" fill="#475569" font-size="10.5">supervision that stayed on</text>
<text x="384" y="148" fill="#475569" font-size="10.5">plant hire still running</text>
<text x="384" y="168" fill="#475569" font-size="10.5">the piles, redrilled</text>
<text x="384" y="194" fill="#94a3b8" font-size="10">evidenced from the cost ledger</text>
<rect x="288" y="112" width="64" height="46" rx="8" fill="#fff" stroke="#cbd5e1" stroke-dasharray="4 3"/>
<text x="320" y="140" text-anchor="middle" fill="#94a3b8" font-size="20">?</text>
<text x="320" y="236" text-anchor="middle" fill="#64748b" font-size="10.5">The claim is the missing box. Everything either side of it is just bookkeeping.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A reviewer reads both columns, agrees with both, and rejects the claim. Nothing in it was untrue.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 250" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THREE QUESTIONS, IN ORDER</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">each has its own evidence and its own way of failing</text>
<rect x="34" y="60" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">1 &#183; LIABILITY &#8212; is this event somebody else&#39;s risk under the contract?</text>
<text x="54" y="100" fill="#475569" font-size="10.5">proved from the clause &#183; fails when the risk was always yours</text>
<rect x="34" y="120" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="142" fill="#059669" font-size="10.5" font-weight="700">2 &#183; CAUSATION &#8212; was the event actually operative, not merely present?</text>
<text x="54" y="160" fill="#475569" font-size="10.5">proved from the programme &#183; fails silently, because nobody asks</text>
<rect x="34" y="180" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="202" fill="#059669" font-size="10.5" font-weight="700">3 &#183; QUANTUM &#8212; how much time, and how much money?</text>
<text x="54" y="220" fill="#475569" font-size="10.5">proved from the ledger &#183; fails when the records cannot carry the method</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">One and three arrive with documents attached. Two arrives with an assertion, which is why it is the one that gets tested.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 244" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">INSIDE THE WORD &#8216;CAUSED&#8217;</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">four links, and most claims evidence only the two at the ends</text>
<rect x="26" y="62" width="136" height="56" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="94" y="86" text-anchor="middle" fill="#059669" font-size="10.5" font-weight="700">THE EVENT</text>
<text x="94" y="105" text-anchor="middle" fill="#475569" font-size="10">rock, at this chainage</text>
<rect x="180" y="62" width="136" height="56" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1" stroke-dasharray="4 3"/>
<text x="248" y="86" text-anchor="middle" fill="#64748b" font-size="10.5" font-weight="700">THE ACTIVITY</text>
<text x="248" y="105" text-anchor="middle" fill="#94a3b8" font-size="10">which one, by how long</text>
<rect x="334" y="62" width="136" height="56" rx="8" fill="#94a3b8" opacity="0.10" stroke="#cbd5e1" stroke-dasharray="4 3"/>
<text x="402" y="86" text-anchor="middle" fill="#64748b" font-size="10.5" font-weight="700">THE PATH</text>
<text x="402" y="105" text-anchor="middle" fill="#94a3b8" font-size="10">was it driving at the time</text>
<rect x="488" y="62" width="126" height="56" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="551" y="86" text-anchor="middle" fill="#059669" font-size="10.5" font-weight="700">COMPLETION</text>
<text x="551" y="105" text-anchor="middle" fill="#475569" font-size="10">the date moved</text>
<text x="171" y="96" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="325" y="96" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="479" y="96" text-anchor="middle" fill="#cbd5e1" font-size="15">&#8594;</text>
<text x="94" y="140" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">EVIDENCED</text>
<text x="248" y="140" text-anchor="middle" fill="#94a3b8" font-size="9.5" font-weight="600">ASSUMED</text>
<text x="402" y="140" text-anchor="middle" fill="#94a3b8" font-size="9.5" font-weight="600">ASSUMED</text>
<text x="551" y="140" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">EVIDENCED</text>
<rect x="26" y="164" width="588" height="56" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="46" y="188" fill="#64748b" font-size="10.5">An event that delays an activity carrying float moves the second box and stops there.</text>
<text x="46" y="208" fill="#64748b" font-size="10.5">The claim still reads &#8216;caused&#8217;, and the two dashed boxes are where it is taken apart.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The ends are the easy links. Criticality lives in the middle, and criticality is the argument.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Blame is not causation.</h2>

<p>Everybody agrees the rock was there. <a href="risk-week-5.html">Risk Week 5</a> put seventeen piles at $2,850 each against it and wrote down, in the register, that nothing evidenced what the northern half of the site was made of. Everybody also agrees the job finished late.</p>

<p>Both facts are on the record. Neither is disputed. And together they prove nothing whatsoever.</p>

<p>That gap is where most rejected claims fail. An event happened, a loss followed, and the document between them says <em>therefore</em> without ever saying <em>how</em>.</p>

<h2>The two-list claim</h2>

<p>Open a weak claim and you find two columns. On the left, everything that went wrong: the rock, the late drawing, the restricted access, the wet October. On the right, everything that hurt: the forty-one days, the supervision team that stayed on, the plant hire that kept running.</p>

<p>Both columns are true. Both are evidenced. Neither column is an argument, and nothing in the document says which item on the left produced which item on the right.</p>

""" + FIG1 + """

<p>What makes this failure hard to see from the inside is that everything in it is honest, including yours. Nobody exaggerated. The reviewer agrees with every line and rejects the whole, and the author never understands why.</p>

<h2>Three questions, and they have an order</h2>

<p>A causal argument answers three questions in sequence, and each fails differently.</p>

<p>First, <strong>liability</strong>: does the contract put this event on somebody else? That is the whole subject of <a href="contract-week-9.html">Contract Week 9</a>, and it is answered by reading a clause.</p>

<p>Second, <strong>causation</strong>: was the event actually operative? Not present on site &#8212; operative. Rock in the ground that nobody was drilling through that month caused nothing at all.</p>

<p>Third, <strong>quantum</strong>: how much time, and how much money? Week 1 set that out as this track's subject.</p>

""" + FIG2 + """

<p>The middle question is the one that goes missing, and the reason is structural rather than careless. Liability arrives with a clause attached. Quantum arrives with your invoices attached. Causation arrives with nothing attached except the analyst's sentence, so it is the link a reviewer reaches for first.</p>

<h2>But for, and where it stops working</h2>

<p>The standard test is a subtraction. Take the event out, and ask whether the delay still happens. If it does, the event didn't cause it &#8212; however expensive it was, and however clearly it was the other side's fault.</p>

<p>The test is clean when one thing goes wrong at a time. Real jobs rarely oblige. Take out the rock and the piling still slips, because the reinforcement drawing was late too. Take out the drawing and the piling still slips, because of the rock. Subtract either one and the delay survives, so on a strict reading neither caused it, and the contractor recovers nothing for a delay that plainly happened.</p>

<p>That result is obviously wrong, and the answer to it is the concurrency week later in this track. What matters here is knowing why the simple test breaks, because a claim that leans on but-for without noticing the second cause is a claim already written against itself.</p>

<h2>When several causes are operative</h2>

<p>Where more than one cause contributes, the courts have not concluded that nobody pays. One line of authority asks whether an event the employer is responsible for can fairly be described as the <strong>dominant</strong> cause of the loss. If it can, liability is established even though other things played a part.</p>

<p>Two things follow, and both matter more than the label. Dominance is a judgement rather than a calculation, so it is argued rather than computed. And the English courts have leaned towards common sense, treating the method of analysis as secondary to whether the account of events holds together.</p>

<p>Which is worth saying plainly, because it cuts against how the subject is usually taught: no software output settles causation. Your programme is evidence in the argument, not a verdict on it.</p>

<h2>The link most claims skip</h2>

<p>Zoom in on the word <em>caused</em> and it turns out to contain four links, not one.</p>

""" + FIG3 + """

<p>The event is easy to evidence, because somebody on your site wrote it down. The moved completion date is easy to evidence, because it is a matter of record. The two links in the middle are where the work is, and they are the two most claims assert rather than prove.</p>

<p>An event that delays an activity carrying float delays that activity and nothing else. The completion date does not move, no matter how disruptive the event was on the day. <a href="week-13.html">Schedule Week 13</a> built the arithmetic that decides this, and you now need it as evidence rather than as planning.</p>

<h2>Written at the time, or written afterwards</h2>

<p>There is a difference between a causal account recorded the week it happened and one assembled eighteen months later by somebody who already knows the answer.</p>

<p>The contemporaneous version has a quality the retrospective one cannot manufacture: at the time, nobody knew which way it would go. A site diary that records the rig standing idle, the reason given that morning, and the instruction to move to another location is worth more than a paragraph written by an expert who has seen the completion date and is reasoning backwards towards it.</p>

<p>This is not a point about honesty. It is a point about what a reviewer can test.</p>

<h2>Forty-one days, and three answers</h2>

<p><a href="contract-week-1.html">Contract Week 1</a> established that the commercial manager found out forty-one days after the event. Put the three questions to that number and you can see how much work is still undone.</p>

<p>Liability is arguable and was argued across the whole of the previous track. Quantum has a rate attached: preliminaries run at $7,100 a month. Causation has nothing attached at all &#8212; nobody has yet shown which activity moved, whether it was driving the completion date at the time, or whether it stayed driving for all forty-one of those days.</p>

<p>Two of the three questions have been circled for four tracks. The third hasn't been asked once.</p>

<h2>Practical insight</h2>

<p>Take the last claim or variation you submitted and find its causal sentence &#8212; the one that connects the event to the loss.</p>

<p>Most of the time you will find that it does not exist as a sentence. What exists is a heading, a narrative of the event, then a heading, then a valuation. The connection lives in the white space between two sections, and you supplied it in your head as you read.</p>

<p>If you can find it, test it with three questions. Which activity moved, and by how many days? Was that activity driving the completion date at the time, or did it have float? Did it stay driving for the whole period claimed, or did the driving path change halfway through?</p>

<p>If you can't answer all three from documents that already exist, you have found the work, and you have found it early enough to matter. Those answers are cheap to record this month and expensive to reconstruct next year.</p>

<h2>Key takeaways</h2>

<p>&#10004; An agreed event and an agreed loss prove nothing on their own; the sentence connecting them is the claim.</p>

<p>&#10004; A causal argument answers liability, causation and quantum in that order, and the middle one is the one that goes missing.</p>

<p>&#10004; Causation fails silently because it is the only link that arrives without documents attached.</p>

<p>&#10004; The but-for test is clean with one cause and breaks with two, which is why it cannot be the whole of the argument.</p>

<p>&#10004; Where several causes operate, an event can still be the dominant cause and establish liability &#8212; but dominance is argued, not computed.</p>

<p>&#10004; No delay software settles causation; your programme is evidence in the argument rather than a verdict on it.</p>

<p>&#10004; The word <em>caused</em> contains four links, and the two in the middle &#8212; which activity, and was it driving &#8212; are the two most claims assert instead of proving.</p>

<h2>What&#39;s coming next</h2>

<p>Causation tells you that an event moved the completion date. It doesn't tell you whether anybody has to pay for it. Next week is the classification that decides that: delays that are excusable and compensable, delays that buy time but no money, and delays that are simply yours &#8212; and why the same fortnight of lost work can land in any of the three depending on a single clause.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 3 &#183; Types of delay &#183; coming soon</span>
                                    <h4>Not every delay is worth money</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The Notice Held. Now Price It. &#8212; The Project Control Hub</title>",
                  "<title>Blame Is Not Causation &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The Notice Held. Now Price It. | The Project Control Hub"',
                  'content="Blame Is Not Causation | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-1.html", "claim-week-2.html")
    s = s.replace('<span>Week 1<span class="crumb-title"> &#183; From right to quantum</span></span>',
                  '<span>Week 2<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 1",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 2", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Mar 8, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Mar 8, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="2"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week2.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 1", "claim-week-1.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    # hafta 1'in next-article karti
    prev = read(SRC)
    if 'href="claim-week-2.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 2 &#183; Cause and effect &#183; coming soon</span>\n'
            '                                    <h4>The chain a claim has to close</h4>',
            '<span class="next-week-tag">Week 2 &#183; Cause and effect</span>\n'
            '                                    <h4>Blame is not causation.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-2.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 2" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 2, title: "Cause and effect — the chain a claim has to close",\n'
           '          short: "Cause and effect", status: "upcoming" },')
    new = ('        { n: 2, title: "Cause and effect — the chain a claim has to close",\n'
           '          short: "Cause and effect", status: "live", page: "claim-week-2.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 2 live (%s)" % DATE)
    elif 'page: "claim-week-2.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 2 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-2.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-2.html</loc>\n"
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
