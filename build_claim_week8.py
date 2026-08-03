#!/usr/bin/env python3
"""claim-week-8.html — Track 5, hafta 8. Sablon: claim-week-7.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-7.html", "claim-week-8.html"
PREV_TITLE = "The as-built is a finding, not a record."
TITLE = "The evidence nobody thought to keep."
CRUMB = "Programme updates"
DATE = "Apr 26, 2028"
DESC = ("An update is the only document that records what the job believed while it still had to "
        "guess. It is also the one most often overwritten, re-baselined or kept as a PDF. "
        "Claims &amp; Delay Analysis Week 8.")
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
<svg viewBox="0 0 640 254" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHAT ONLY AN UPDATE CAN TELL YOU</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the driving path in each month &#8212; a fact that stops existing the moment the month ends</text>
<line x1="60" y1="150" x2="590" y2="150" stroke="#cbd5e1" stroke-width="1.5"/>
<circle cx="110" cy="150" r="5" fill="#059669"/><text x="110" y="172" text-anchor="middle" fill="#64748b" font-size="10">March</text>
<circle cx="250" cy="150" r="5" fill="#059669"/><text x="250" y="172" text-anchor="middle" fill="#64748b" font-size="10">April</text>
<circle cx="390" cy="150" r="5" fill="#059669"/><text x="390" y="172" text-anchor="middle" fill="#64748b" font-size="10">May</text>
<circle cx="530" cy="150" r="5" fill="#059669"/><text x="530" y="172" text-anchor="middle" fill="#64748b" font-size="10">June</text>
<text x="110" y="94" text-anchor="middle" fill="#475569" font-size="10">piling</text>
<text x="110" y="110" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">driving</text>
<text x="250" y="94" text-anchor="middle" fill="#475569" font-size="10">piling</text>
<text x="250" y="110" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">driving</text>
<text x="390" y="94" text-anchor="middle" fill="#475569" font-size="10">cladding</text>
<text x="390" y="110" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">driving</text>
<text x="530" y="94" text-anchor="middle" fill="#475569" font-size="10">commissioning</text>
<text x="530" y="110" text-anchor="middle" fill="#059669" font-size="9.5" font-weight="600">driving</text>
<rect x="34" y="192" width="278" height="48" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="212" fill="#059669" font-size="10.5" font-weight="700">FROM THE UPDATES</text>
<text x="54" y="230" fill="#475569" font-size="10.5">four answers, one per month, recorded live</text>
<rect x="328" y="192" width="278" height="48" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="212" fill="#64748b" font-size="10.5" font-weight="700">FROM THE AS-BUILT ALONE</text>
<text x="348" y="230" fill="#64748b" font-size="10.5">one answer, inferred, applied to all four</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Which path was driving in March is a question about March. Only a document written in March answers it without an argument.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 224" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">AN UPDATE IS NOT JUST A RECORD</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">under FIDIC, each accepted revision becomes the Programme &#8212; with consequences attached</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="80" fill="#059669" font-size="10.5" font-weight="700">IT IS DUE WHEN PROGRESS DIVERGES, NOT ON THE LAST FRIDAY OF THE MONTH</text>
<text x="54" y="97" fill="#475569" font-size="10.5">the trigger is the picture going out of date &#8212; a condition on site, not a day in the diary</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="134" fill="#059669" font-size="10.5" font-weight="700">SILENCE MAKES IT THE PROGRAMME</text>
<text x="54" y="151" fill="#475569" font-size="10.5">no notice within the review period and it is the accepted document, whatever it contains</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="188" fill="#059669" font-size="10.5" font-weight="700">THE OTHER SIDE IS ENTITLED TO RELY ON IT</text>
<text x="54" y="205" fill="#475569" font-size="10.5">the employer&#39;s people may plan their own work around the dates you published</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">A monthly chore in the planner&#39;s calendar is, in the contract, a series of statements you are bound by.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">FOUR WAYS THE SERIES IS DESTROYED</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">none of them looks like damage at the time; all of them are permanent</text>
<rect x="34" y="60" width="278" height="76" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="82" fill="#64748b" font-size="10.5" font-weight="700">RE-BASELINING</text>
<text x="54" y="102" fill="#64748b" font-size="10">a clean new baseline is issued and</text>
<text x="54" y="118" fill="#64748b" font-size="10">the history it replaced is gone</text>
<rect x="328" y="60" width="278" height="76" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">RETROSPECTIVE EDITS</text>
<text x="348" y="102" fill="#64748b" font-size="10">last month&#39;s actual dates corrected</text>
<text x="348" y="118" fill="#64748b" font-size="10">in this month&#39;s file, silently</text>
<rect x="34" y="146" width="278" height="76" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="168" fill="#64748b" font-size="10.5" font-weight="700">MISSING MONTHS</text>
<text x="54" y="188" fill="#64748b" font-size="10">the quiet period nobody updated</text>
<text x="54" y="204" fill="#64748b" font-size="10">is the period you need most</text>
<rect x="328" y="146" width="278" height="76" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="168" fill="#64748b" font-size="10.5" font-weight="700">PDF ONLY</text>
<text x="348" y="188" fill="#64748b" font-size="10">the picture survives, the logic,</text>
<text x="348" y="204" fill="#64748b" font-size="10">float and calendars do not</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Keep the native file of every submitted revision, unaltered, in a folder nobody tidies. That is the whole instruction.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">The evidence nobody thought to keep.</h2>

<p>Of everything a project produces, the programme update is the strangest document. It is treated as an administrative chore, produced by one person under time pressure at month end, circulated to people who look at the bar chart and nothing else, and then filed.</p>

<p>It is also the only document on the job that records what the project <em>believed</em> at a moment when it still had to guess.</p>

<p>Everything else in Phase B looks backwards. The baseline is an intention written before anything happened. The as-built is a reconstruction assembled once everything had. The update sits in the middle, made by people who knew what had gone wrong so far and did not yet know how it would end. That is what makes it worth more than either.</p>

<h2>What only an update can tell you</h2>

""" + FIG1 + """

<p>Week 4 established that criticality belongs to a moment. Week 7 established that as-built logic is inferred rather than recorded. Put those together and there is one question neither the baseline nor the as-built can answer: <em>which path was driving in March?</em></p>

<p>The March update answers it directly, because somebody calculated it in March. Without that file, the answer has to be reconstructed from an as-built whose logic is already an inference &#8212; an inference on top of an inference, and both of them made by a party with an interest in the outcome.</p>

<p>This is not a marginal improvement in evidence. It is the difference between a fact and an argument, repeated for every month of the job.</p>

<h2>What the contract actually asks for</h2>

<p>Most teams update monthly out of habit. That is a reasonable habit, but it isn't what the contract says, and the difference matters in the months when things move.</p>

""" + FIG2 + """

<p>Under the 2017 Red Book the trigger for a revised programme is not a date in the calendar. It is a condition. A revision falls due once the existing programme no longer gives an accurate picture of where the works have got to, or has drifted out of line with what the contractor is obliged to be doing. Something significant goes wrong in the second week of the month, and the obligation arrives with it rather than waiting for month end.</p>

<p>Then the mechanism <a href="contract-week-11.html">Contract Week 11</a> set out takes over. If the Engineer says nothing within the review period, no-objection is deemed and the revision becomes the Programme.</p>

<p>And there is a consequence that gets almost no attention: the employer's people are entitled to rely on the Programme in planning their own activities. Your update is not merely a record of what you thought. It is a statement the other side may act on, and later point to.</p>

<p>One more detail, easy to overlook and expensive later: the contract requires an electronic copy, not only paper. That obligation is the reason the native files should exist &#8212; and the reason it is worth asking, in month two, whether anybody is actually keeping them.</p>

<h2>Four ways the series is destroyed</h2>

<p>An update series is fragile in ways that don't look like damage while they are happening.</p>

""" + FIG3 + """

<p><strong>Re-baselining</strong> is the most damaging and the most defensible-sounding. The programme has drifted so far that it is useless for managing the work, so a new baseline is issued and everyone moves on. Operationally that is often the right call. Evidentially it draws a line: the history before it has been replaced by a document that shows the new plan as though it were always the plan.</p>

<p><strong>Retrospective editing</strong> is quieter. Last month's actual start was wrong, so it gets corrected in this month's file. Nobody records that it was changed. Two years later the update series contains no contradictions at all, which is itself a slightly suspicious property for thirty months of construction.</p>

<p><strong>Missing months</strong> follow a cruel pattern. Updates get skipped in the periods when everybody is too busy &#8212; which are the disrupted periods, which are the periods a claim will turn on.</p>

<p><strong>PDF-only retention</strong> is the most common of the four. The picture survives and everything that makes it analysable does not: no logic, no float values, no calendars, no way to re-run anything.</p>

<h2>The setting that changes last month&#39;s answer</h2>

<p>There is a fifth failure, more technical than the four above and harder to spot, because it lives in a dialog box rather than in a decision.</p>

<p>Work on site rarely follows the logic exactly. Something starts before its predecessor finished, and the software has to be told what to do about it. Depending on the setting chosen, it will either honour the original logic and push the remaining work out, or accept what happened and let the work proceed. The two produce different forecast completion dates from identical progress.</p>

<p>Neither setting is wrong. What causes damage is changing it partway through a job, because the update series then contains two kinds of month and nothing records which is which. An analysis run across that boundary is comparing answers produced by different rules and reporting the difference as delay.</p>

<p>The instruction is the same as everywhere else in this phase: pick a convention, write it down, apply it every month, and note it if it ever changes. None of this is difficult while a job is running. All of it is impossible afterwards.</p>

<h2>What the gaps do to your options</h2>

<p>Phase C opens next week with a choice of methods, and this is the point at which that choice narrows.</p>

<p>Methods that analyse the job period by period run directly on the update series. No updates, no periods; the technique simply isn't available. Methods that model an event into the programme as it stood at the time need the file as it stood at the time, for the same reason.</p>

<p>What remains, if the series has holes, are the methods built from the as-built alone &#8212; and those carry every inference Week 7 described. The update series is therefore not a nice-to-have record. It is the thing that decides how good an answer you are allowed to give.</p>

<h2>The one that was never issued</h2>

<p>A final case, and it comes up more than it should.</p>

<p>Sometimes a revision was prepared, was never submitted, and sits on a server. It shows the job as the planner saw it, honestly, and it may be the best contemporaneous evidence available.</p>

<p>It is also not the Programme. It went through no review, attracted no deemed acceptance, and the other side never had the chance to object to it or rely on it. It can support a narrative. It cannot carry the contractual weight of a submitted revision, and presenting it as though it can is the kind of error that costs credibility on everything else in the file.</p>

<h2>Practical insight</h2>

<p>Go and find every programme file your job has issued, and list them by date with two columns: was it submitted, and do we still have the native file.</p>

<p>Most teams doing this discover three things within an hour. There are months with no revision at all. There is at least one point where the baseline changed and nobody wrote down why. And a proportion of what survives is PDF only, usually the older ones, usually from the period that matters.</p>

<p>Then fix the going-forward half, which is cheap: one folder, one file per submitted revision, native format, never edited after issue, named by status date. Nobody tidies it and nobody works in it.</p>

<p>The backward half is harder, and worth an afternoon anyway. Native files that still exist on a laptop or in an email attachment can be recovered now. In two years the laptop is gone and the mailbox has been archived by somebody applying a retention policy that has never heard of your claim.</p>

<h2>Key takeaways</h2>

<p>&#10004; The update is the only document recording what the project believed while the outcome was still unknown.</p>

<p>&#10004; Which path was driving in a given month is answerable from that month's update and, without it, only by inference.</p>

<p>&#10004; FIDIC ties revisions to a condition rather than a calendar: the picture going out of date is itself what makes one due.</p>

<p>&#10004; Each accepted revision becomes the Programme, and the employer's people are entitled to plan around the dates in it.</p>

<p>&#10004; The contract asks for an electronic copy, which is the contractual basis for keeping native files rather than printouts.</p>

<p>&#10004; Re-baselining, silent retrospective edits, skipped months and PDF-only retention each destroy the series in a way that cannot be repaired later.</p>

<p>&#10004; A revision that was prepared but never submitted is evidence of what you thought, not a contractual document, and it must not be presented as one.</p>

<h2>What&#39;s coming next</h2>

<p>Phase B ends here, and with it the evidence. You have a baseline and know what it is worth, a record of what happened, an as-built built from it, and a series of updates with whatever holes it has. Next week the track turns to methods &#8212; and opens with the question that decides everything that follows: not which technique is best, but which ones your records have left open to you.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 9 &#183; Choosing a method &#183; coming soon</span>
                                    <h4>Pick the method your records support</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>The As-Built Is A Finding, Not A Record &#8212; The Project Control Hub</title>",
                  "<title>The Evidence Nobody Thought To Keep &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="The As-Built Is A Finding, Not A Record | The Project Control Hub"',
                  'content="The Evidence Nobody Thought To Keep | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-7.html", "claim-week-8.html")
    s = s.replace('<span>Week 7<span class="crumb-title"> &#183; The as-built programme</span></span>',
                  '<span>Week 8<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 7",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 8", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Apr 19, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Apr 19, 2028", "PMP&reg; &#183; " + DATE)

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
    s = re.sub(r'data-current-week="\d+"', 'data-current-week="8"', s)
    s = s.replace(quote(PREV_TITLE, safe=""), quote(TITLE, safe=""))
    return s, n, mins


def main():
    print("\n  build_claim_week8.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 7", "claim-week-7.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-8.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 8 &#183; Programme updates &#183; coming soon</span>\n'
            '                                    <h4>The evidence nobody thought to keep</h4>',
            '<span class="next-week-tag">Week 8 &#183; Programme updates</span>\n'
            '                                    <h4>The evidence nobody thought to keep.</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-8.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 8" % SRC)

    js = read("curriculum.js")
    old = ('        { n: 8, title: "Programme updates — the contemporaneous record and the gaps in it",\n'
           '          short: "Programme updates", status: "upcoming" },')
    new = ('        { n: 8, title: "Programme updates — the contemporaneous record and the gaps in it",\n'
           '          short: "Programme updates", status: "live", page: "claim-week-8.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 8 live (%s)" % DATE)
    elif 'page: "claim-week-8.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 8 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-8.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-8.html</loc>\n"
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
