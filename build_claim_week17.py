#!/usr/bin/env python3
"""claim-week-17.html — Track 5, hafta 17. Sablon: claim-week-16.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-16.html", "claim-week-17.html"
PREV_TITLE = "Both sides caused it. Now what?"
TITLE = "Slowing down on purpose."
CRUMB = "Pacing"
DATE = "Jun 28, 2028"
WEEK_N = 17
DESC = ("Why hurry up in order to wait? Pacing is the rational response to somebody else&#39;s delay, "
        "and in every programme ever drawn it looks exactly like default. Four things you have to "
        "show, three of which cannot be manufactured afterwards. Claims &amp; Delay Analysis Week 17.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">THE TWO STORIES BEHIND ONE BAR</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the programme records the slowdown; it cannot record the reason for it</text>
<text x="34" y="72" fill="#64748b" font-size="10" font-weight="700">WHAT EVERY PROGRAMME SHOWS</text>
<rect x="270" y="60" width="120" height="18" rx="3" fill="#94a3b8" opacity="0.35"/>
<text x="330" y="73" text-anchor="middle" fill="#475569" font-size="9">planned</text>
<rect x="270" y="82" width="210" height="18" rx="3" fill="#059669" opacity="0.70"/>
<text x="375" y="95" text-anchor="middle" fill="#fff" font-size="9">actual &#8212; took far longer</text>
<rect x="34" y="120" width="278" height="70" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="142" fill="#64748b" font-size="10.5" font-weight="700">STORY ONE &#183; DEFAULT</text>
<text x="54" y="162" fill="#64748b" font-size="10">the crew was short, the plant broke,</text>
<text x="54" y="180" fill="#64748b" font-size="10">nobody managed it &#8212; your delay</text>
<rect x="328" y="120" width="278" height="70" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="348" y="142" fill="#059669" font-size="10.5" font-weight="700">STORY TWO &#183; PACING</text>
<text x="348" y="162" fill="#475569" font-size="10">the job was held elsewhere anyway,</text>
<text x="348" y="180" fill="#475569" font-size="10">so you stopped paying to stand still</text>
<text x="320" y="222" text-anchor="middle" fill="#94a3b8" font-size="10.5">Identical bars. One is a breach, the other is competent management, and no method can tell them apart.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">This is the blind spot every technique in Phase C shares, and the reason it needs a week of its own.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 262" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FOUR THINGS THE ARGUMENT REQUIRES</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">and only the first can be reconstructed after the event</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.10" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">1 &#183; YOU KNEW ABOUT THE OTHER DELAY</text>
<text x="54" y="97" fill="#475569" font-size="10.5">provable from correspondence and minutes &#8212; the easy one</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="134" fill="#64748b" font-size="10.5" font-weight="700">2 &#183; YOU DECIDED TO PACE, AND THE DECISION IS RECORDED</text>
<text x="54" y="151" fill="#64748b" font-size="10.5">not a state of mind you remember having &#8212; a decision somebody wrote down</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#64748b" font-size="10.5" font-weight="700">3 &#183; YOU TOLD THEM</text>
<text x="54" y="205" fill="#64748b" font-size="10.5">notice that you would pace, so as not to add delay or disruption of your own</text>
<rect x="34" y="222" width="572" height="34" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="244" fill="#64748b" font-size="10.5"><tspan font-weight="700">4 &#183; YOU COULD HAVE RESUMED</tspan> &#8212; resources still available if the other delay had cleared</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Three of the four are contemporaneous acts. A claim invented at the end of the job can satisfy exactly one.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 214" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT IT COSTS TO KEEP THE ARGUMENT ALIVE</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">two documents, neither of which takes an hour</text>
<rect x="34" y="60" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">THE UPDATE FIELD</text>
<text x="54" y="98" fill="#475569" font-size="10.5">the line saying what an activity was waiting for &#8212; here it says: paced, against the access delay</text>
<rect x="34" y="122" width="572" height="52" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="142" fill="#059669" font-size="10.5" font-weight="700">THE LETTER</text>
<text x="54" y="160" fill="#475569" font-size="10.5">we are resequencing to match your delay, we can resume within a fortnight if it clears</text>
<text x="320" y="198" text-anchor="middle" fill="#94a3b8" font-size="10.5">Written in the month it happens, these two turn an unprovable state of mind into a record.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">And the letter does a second job: it puts the other side on notice that the delay is theirs.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Slowing down on purpose.</h2>

<p>The access to the north of the site has been blocked for six weeks and there is nothing you can do about it. Your steel gang could be working flat out on the section they can reach, finishing early, and then standing around for a month waiting for everybody else.</p>

<p>So you don't. You slow them down to match the pace of the job as it actually is, keep the crew smaller, and save the money you would have spent racing towards a queue.</p>

<p>That is a competent decision. It is what a good contracts manager does. And in every programme ever drawn, it is indistinguishable from failing to resource the work.</p>

""" + FIG1 + """

<h2>Why anybody does it</h2>

<p>The logic is straightforward once stated. If you become aware that a more critical delay is running elsewhere on the project, you can choose to pace your own progress against it &#8212; avoiding the cost of speeding up, or of working to normal output only to wait for the delayed work to catch up.</p>

<p>Hurrying in order to wait is expensive. Crews stand idle, plant sits on hire, and the completion date does not move an inch closer because something else is holding it.</p>

<p>The argument has limited support in both US and English case law, which is a careful way of saying it is recognised as real and is not a free pass.</p>

<h2>Both sides use it</h2>

<p>Worth knowing, because most people meet this argument from one direction only.</p>

<p>When an employer points to a contractor's concurrent culpable delays, the contractor frequently answers that it was pacing against employer delays that already existed. And when a designer is late returning information or approving shop drawings, the same argument comes back the other way: the works were already delayed, the response was just in time, and nothing further was caused.</p>

<p>Both versions are sometimes true. Both are also the most convenient thing each party could possibly say, which is precisely why the bar for proving them is where it is.</p>

<h2>Four things you have to show</h2>

""" + FIG2 + """

<p>A party relying on pacing needs to demonstrate four things: that it knew about the more critical excusable delay, that it made an express decision to pace, that it notified the other party it would do so without adding delay or disruption of its own, and that it could have reinstated normal output had the pre-existing delay been cleared.</p>

<p>Look at that list as a records problem rather than a legal one and its real difficulty appears immediately.</p>

<p>The first element is usually easy. Correspondence, minutes and the delay register will show you knew.</p>

<p>The second is where most attempts die. An express decision is not a state of mind you remember having. It is a decision somebody made and recorded &#8212; a note in a meeting, an instruction to the subcontractor, a line in the monthly report. Without it, what you are describing is your own slow progress with a favourable interpretation attached.</p>

<p>The third asks whether you told them. That is a contemporaneous act which either happened or didn't, and no amount of later reasoning creates it. <a href="contract-week-10.html">Contract Week 10</a> made the general point about notices; this is the same discipline applied to a decision rather than to an event.</p>

<p>The fourth asks whether you could have resumed. Keeping the resources available to restart is the thing that distinguishes pacing from having quietly demobilised, and it is provable from allocation records if anybody kept them.</p>

<h2>Three of the four cannot be manufactured</h2>

<p>That is the uncomfortable heart of this week.</p>

<p>Pacing is almost never asserted while a job is running. It is asserted at the end, in response to an employer's list of contractor delays, and by then three of the four elements are historical facts that either exist in the record or don't.</p>

<p>Which means the argument is usually decided long before anybody makes it. If nobody wrote the decision down and nobody sent the letter, the honest position is that you have your knowledge of the other delay and nothing else &#8212; and knowledge alone describes every contractor who was late while something else was also going wrong.</p>

<h2>Paced at your own peril</h2>

<p>The case law is not encouraging for the party that leaves it late.</p>

<p>The general rule where both parties have contributed to delay is that neither recovers, unless the delay and the expense attributable to each can be clearly apportioned. Courts have declined recovery where delays ran concurrently and the contractor could not establish its own delay separately from the other party's.</p>

<p>And a contractor pacing against an employer risk event has sometimes been held to do so at its own peril &#8212; the reasoning being that if it cannot show it would have finished on time but for the other party's delays, it was at least concurrently responsible, and it bears the consequences of the sequence it chose.</p>

<p>There is also a limit built into the argument that people forget. You can only pace against the delay that exists. Slow down by eight weeks while the access is blocked for six, and the last fortnight is yours no matter how good the first six weeks of reasoning were &#8212; and the whole argument now looks like a justification stretched to cover something it doesn't reach. Pacing is a matching exercise, and it stops being one the moment you overshoot.</p>

<p>Take Week 16's conclusion and apply it here. Concurrency generally moves a delay from compensable into time-only. A failed pacing argument does something worse: it leaves the delay looking like yours, which pushes it into the third column and takes the extension of time with it.</p>

<h2>What keeps it alive</h2>

""" + FIG3 + """

<p>The remedy costs almost nothing and has to happen at the time.</p>

<p>Week 7 proposed one extra field in the monthly update: what each activity was waiting for. That field is where pacing is recorded. Not <em>slow progress</em> &#8212; <em>paced against the access delay to the north</em>. Written that month, by the planner, in a document that gets issued.</p>

<p>Then the letter. Short, unremarkable, sent while it is happening: we are matching our sequence to the delayed access, we are not adding delay of our own, and we can return to normal output within a fortnight if it clears.</p>

<p>That letter does two jobs at once. It records the decision and the ability to resume, satisfying three of the four elements between them. And it puts the other side on notice that the delay is theirs, which is worth having entirely separately.</p>

<h2>Practical insight</h2>

<p>Go and look at the last three months on your job for any activity that visibly slowed down while something else was holding the works.</p>

<p>For each one, ask the person who ran it a single question: did we slow down because we chose to, or because we couldn't do better?</p>

<p>You will get clear answers, because they know. What almost never exists is any document containing that answer. The conversation takes ten minutes and the record it produces is the difference between an argument you can make and one you can only assert.</p>

<p>If the answer is that you chose to, write it down this week and send the letter. If the answer is that you couldn't do better, that is worth knowing too &#8212; because it means the pacing argument is not available to you, and building a claim on it later will fail in a way that damages everything around it.</p>

<h2>Key takeaways</h2>

<p>&#10004; Pacing is the rational choice to match your progress to a job already held up elsewhere, rather than hurrying in order to wait.</p>

<p>&#10004; In every programme it looks identical to default, which is the blind spot all the analysis methods share.</p>

<p>&#10004; Both sides use the argument &#8212; contractors against employer delays, designers against an already-late job.</p>

<p>&#10004; It requires knowledge of the other delay, a recorded decision to pace, notification, and the ability to have resumed.</p>

<p>&#10004; Three of those four are contemporaneous acts, so the argument is usually decided before anybody thinks to make it.</p>

<p>&#10004; Where both parties contributed and the delays cannot be clearly apportioned, neither may recover at all.</p>

<p>&#10004; One line in the monthly update and one short letter, written at the time, satisfy most of what the argument needs.</p>

<h2>What&#39;s coming next</h2>

<p>Pacing is the decision to go slower because the job allows it. The opposite decision is more expensive and considerably more contested: going faster than the plan, sometimes because you were instructed to and sometimes because refusing to would have cost more. Next week is acceleration and mitigation &#8212; including the version nobody instructed, nobody agreed, and somebody still has to pay for.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 18 &#183; Acceleration and mitigation &#183; coming soon</span>
                                    <h4>Nobody instructed it. You did it anyway</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Both Sides Caused It. Now What? &#8212; The Project Control Hub</title>",
                  "<title>Slowing Down On Purpose &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Both Sides Caused It. Now What? | The Project Control Hub"',
                  'content="Slowing Down On Purpose | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-16.html", "claim-week-17.html")
    s = s.replace('<span>Week 16<span class="crumb-title"> &#183; Concurrency</span></span>',
                  '<span>Week 17<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 16",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 17", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jun 21, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jun 21, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week17.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 16", "claim-week-16.html", PREV_TITLE):
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
    if 'href="claim-week-17.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 17 &#183; Pacing &#183; coming soon</span>\n'
            '                                    <h4>Slowing down on purpose</h4>',
            '<span class="next-week-tag">Week 17 &#183; Pacing</span>\n'
            '                                    <h4>Slowing down on purpose.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-17.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 17" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 17, title: "Pacing — the delay that answers another delay",\n'
           '          short: "Pacing", status: "upcoming" },')
    new = ('        { n: 17, title: "Pacing — the delay that answers another delay",\n'
           '          short: "Pacing", status: "live", page: "claim-week-17.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 17 live (%s)" % DATE)
    elif 'page: "claim-week-17.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 17 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-17.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-17.html</loc>\n"
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
