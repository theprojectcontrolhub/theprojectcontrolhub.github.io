#!/usr/bin/env python3
"""claim-week-16.html — Track 5, hafta 16. Faz D acilisi. Sablon: claim-week-15.html."""
import io, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC, DST = "claim-week-15.html", "claim-week-16.html"
PREV_TITLE = "Same facts. Two answers. Both defensible."
TITLE = "Both sides caused it. Now what?"
CRUMB = "Concurrency"
DATE = "Jun 21, 2028"
WEEK_N = 16
DESC = ("There is no agreed definition, the contract on this job hands the question to a document "
        "most projects never fill in, and the courts have given two different answers. What "
        "concurrency does to a claim, and why it usually costs the money rather than the time. "
        "Claims &amp; Delay Analysis Week 16.")
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
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO THINGS CALLED THE SAME WORD</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">and most arguments are between people who mean different ones</text>
<text x="34" y="70" fill="#64748b" font-size="10" font-weight="700">CONCURRENT EVENTS &#8212; they start together</text>
<rect x="230" y="60" width="130" height="16" rx="3" fill="#b91c1c" opacity="0.5"/>
<text x="295" y="72" text-anchor="middle" fill="#fff" font-size="9">employer event</text>
<rect x="230" y="80" width="130" height="16" rx="3" fill="#94a3b8" opacity="0.5"/>
<text x="295" y="92" text-anchor="middle" fill="#475569" font-size="9">contractor event</text>
<text x="380" y="82" fill="#94a3b8" font-size="9.5">rare on real jobs</text>
<text x="34" y="130" fill="#64748b" font-size="10" font-weight="700">CONCURRENT EFFECT &#8212; they overlap where it counts</text>
<rect x="150" y="120" width="150" height="16" rx="3" fill="#b91c1c" opacity="0.5"/>
<text x="225" y="132" text-anchor="middle" fill="#fff" font-size="9">employer event</text>
<rect x="260" y="140" width="150" height="16" rx="3" fill="#94a3b8" opacity="0.5"/>
<text x="335" y="152" text-anchor="middle" fill="#475569" font-size="9">contractor event</text>
<rect x="260" y="118" width="40" height="42" rx="3" fill="none" stroke="#0f172a" stroke-dasharray="3 2"/>
<text x="430" y="142" fill="#64748b" font-size="9.5">the overlap is the argument</text>
<rect x="34" y="180" width="572" height="58" rx="8" fill="#f1f5f9" stroke="#e2e8f0"/>
<text x="54" y="202" fill="#64748b" font-size="10.5">A useful working definition: a stretch of overrun driven by two or more effective causes of</text>
<text x="54" y="220" fill="#64748b" font-size="10.5">roughly equal weight. Note what it asks about &#8212; the overrun, not the events.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Simultaneous events are unusual. Overlapping effects are ordinary, which is why the second picture is the one that matters.</figcaption>
</figure>"""

FIG2 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 246" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">TWO ANSWERS, TWO JURISDICTIONS</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">the same eleven days, and the difference is where you are standing</text>
<rect x="34" y="60" width="278" height="140" rx="10" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="82" fill="#059669" font-size="10.5" font-weight="700">THE ENGLISH LINE</text>
<text x="54" y="104" fill="#475569" font-size="10">time is granted, money is not</text>
<text x="54" y="122" fill="#475569" font-size="10">the completion date moves,</text>
<text x="54" y="140" fill="#475569" font-size="10">the prolongation cost stays yours</text>
<text x="54" y="164" fill="#64748b" font-size="10">not an apportionment exercise &#8212;</text>
<text x="54" y="182" fill="#64748b" font-size="10">a judgement on the facts</text>
<rect x="328" y="60" width="278" height="140" rx="10" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="348" y="82" fill="#64748b" font-size="10.5" font-weight="700">THE SCOTTISH LINE</text>
<text x="348" y="104" fill="#64748b" font-size="10">the delay may be apportioned</text>
<text x="348" y="122" fill="#64748b" font-size="10">between the two causes on</text>
<text x="348" y="140" fill="#64748b" font-size="10">their relative significance</text>
<text x="348" y="164" fill="#64748b" font-size="10">a useful guide, but not</text>
<text x="348" y="182" fill="#64748b" font-size="10">binding south of the border</text>
<text x="320" y="228" text-anchor="middle" fill="#94a3b8" font-size="10.5">Before analysing anything, find out which line the tribunal you are heading for follows.</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">The technical work is identical either way. What it is worth is decided by law, not by the programme.</figcaption>
</figure>"""

FIG3 = """<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
<svg viewBox="0 0 640 226" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<text x="320" y="24" text-anchor="middle" fill="#64748b" font-size="11.5" font-weight="700" letter-spacing="2">WHICH METHODS CAN EVEN SEE IT</text>
<text x="320" y="42" text-anchor="middle" fill="#94a3b8" font-size="10.5">a hypothetical model cannot establish what genuinely ran alongside what</text>
<rect x="34" y="60" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="80" fill="#64748b" font-size="10.5" font-weight="700">THE MODELLED METHODS &#8212; approximate only</text>
<text x="54" y="97" fill="#64748b" font-size="10.5">run each party&#39;s events alone; the difference from the combined run hints at the overlap</text>
<rect x="34" y="114" width="572" height="44" rx="8" fill="#059669" opacity="0.08" stroke="#10b981"/>
<text x="54" y="134" fill="#059669" font-size="10.5" font-weight="700">THE AS-BUILT METHODS &#8212; the only route to the real thing</text>
<text x="54" y="151" fill="#475569" font-size="10.5">what was driving, in the period it was driving, from records rather than from a projection</text>
<rect x="34" y="168" width="572" height="44" rx="8" fill="#94a3b8" opacity="0.12" stroke="#cbd5e1"/>
<text x="54" y="188" fill="#64748b" font-size="10.5" font-weight="700">AND ONE BLIND SPOT THEY ALL SHARE</text>
<text x="54" y="205" fill="#64748b" font-size="10.5">a contractor deliberately slowing down looks exactly like a contractor causing delay</text>
</svg>
<figcaption style="margin-top:14px;font-size:12.5px;color:#64748b;line-height:1.5;">Approximate concurrency is a useful indicator and not a finding. Say which one you have produced.</figcaption>
</figure>"""

BODY = """<h2 style="margin-top:0;">Both sides caused it. Now what?</h2>

<p>Week 4 built the situation with nothing but arithmetic. The rock delays piling. The services path carries thirty days of float. On day thirty-one that float runs out, the services path becomes critical too, and from then on the job has two driving paths.</p>

<p>Nobody did anything on day thirty-one. No new event, no failure, no decision. The geometry changed, and from that moment the remaining eleven days are being caused by two things at once &#8212; one of which is the employer's risk and one of which is not.</p>

<p>This is the hardest question in the subject, and the honest place to start is that the industry has not settled it.</p>

<h2>Nobody agrees what the word means</h2>

<p>There is no universally accepted definition of concurrent delay. That is not a rhetorical opening; it is the actual state of the field, and it is the reason two experts can agree on every date and still be arguing.</p>

""" + FIG1 + """

<p>The definition most often cited describes a period of project overrun driven by two or more effective causes of delay carrying roughly equal weight. Notice what that puts at the centre: the <em>overrun</em>, not the events. Two things need not begin together to matter here. What matters is whether their effects were both operating during the stretch of time in dispute.</p>

<p>That distinction &#8212; concurrent events against concurrent effect &#8212; resolves a surprising share of arguments before they start. Genuinely simultaneous events are rare. Overlapping effects are ordinary, and on day thirty-one of the example above the events were months apart.</p>

<h2>What the contract says about it</h2>

<p>Here the job's own contract does something worth reading carefully.</p>

<p>The extension of time clause in the 2017 Red Book addresses concurrency in its final paragraph, and what it says is that where an employer-responsible delay runs concurrently with a contractor-responsible one, the contractor's entitlement is to be assessed according to the rules and procedures set out in the Special Provisions.</p>

<p>FIDIC's own guidance explains the drafting: there is no single standard set of rules that would suit every project, so the question is left to be answered project by project.</p>

<p>That is an entirely defensible piece of drafting and it has a practical consequence that catches people. The Special Provisions are a document a great many projects never populate. <a href="contract-week-20.html">Contract Week 20</a> made the general point about the blanks nobody sweeps; this is the most expensive blank in the book. The contract does not answer the concurrency question. It tells you where the answer should have been written, and on most jobs nobody wrote it.</p>

<h2>Which leaves the law</h2>

""" + FIG2 + """

<p>Two lines of authority answer the question differently, and the difference is worth real money.</p>

<p>The English position, running through a line of cases and reaffirmed more than once since, is that where completion is delayed concurrently by matters for which each party is responsible, the contractor gets its extension of time but cannot recover the loss caused by that delay. Time, not money. It is expressly not an apportionment exercise &#8212; the decision-maker is making a judgement on the facts about whether the employer's event did cause delay beyond the completion date, and then fixing a fair date.</p>

<p>The Scottish appellate position has been more willing to apportion the delay between the competing causes according to their relative significance. It is a useful guide and consistent with a common-sense approach to a genuinely hard problem. It is also not binding on the English courts, which have continued down the other road.</p>

<p>The practical instruction is unglamorous: before doing the analysis, find out which body of law your dispute will be decided under. The programme work is identical either way. What it is worth is not.</p>

<h2>Where that lands you</h2>

<p>Take the English answer back to Week 3's grid and the effect becomes concrete.</p>

<p>Concurrency does not usually destroy a claim. It moves it. A delay that would have been excusable and compensable becomes excusable but not compensable &#8212; the middle column, where the completion date shifts, the delay damages stop, and you fund the extra time yourself.</p>

<p>On the eleven contested days from Week 12, that is roughly $2,566 of preliminaries changing hands or not, on a job whose entire net margin is $48,163. The thirty clean days survive. The eleven move columns.</p>

<p>Which is why the windowed analysis mattered so much. A claim that asserts forty-one compensable days and meets a concurrency argument risks the whole figure. A claim that already separates thirty from eleven has pre-empted the argument and confined it to the part that was always going to be contested.</p>

<h2>The principle underneath</h2>

<p>There is an older idea sitting beneath all of this and it explains why contractors are not simply left holding everything.</p>

<p>Under English law a party cannot enforce an obligation against another party when it has itself prevented that party from performing. Applied here: an employer who has caused delay cannot straightforwardly insist on the original completion date and levy damages against it, because it contributed to the failure it is complaining about.</p>

<p>The point was established in a case from the 1970s where a fifty-eight week delay was caused by both sides &#8212; the contractor through its nominated piling subcontractor, and the employer through its own conduct. The consequences of getting the extension of time machinery wrong in that situation can be severe, which is a large part of why the machinery <a href="contract-week-9.html">Contract Week 9</a> described exists at all.</p>

<h2>What the methods can actually show</h2>

""" + FIG3 + """

<p>A last practical constraint, and it connects the whole of the previous phase.</p>

<p>The modelled methods cannot demonstrate true concurrency. They can produce an approximation &#8212; run the employer's events alone, compare against the combined model, and the difference indicates roughly where the overlap sits. That is a legitimate and useful output, and it is expressly an approximation.</p>

<p>Real concurrency, in the period it actually occurred, can only be established from as-built records and the methods built on them. If the concurrency argument is going to be central, that is a reason to have chosen a method from the second half of Phase C.</p>

<p>And every method shares one blind spot: a contractor deliberately slowing its work because something else is holding the job anyway looks identical, in any programme, to a contractor causing critical delay. That is next week.</p>

<h2>Practical insight</h2>

<p>Do one thing before you need it: open your contract and find out whether the concurrency question has been answered.</p>

<p>Look in the Special Provisions or the particular conditions for anything setting out how concurrent delay is to be assessed. On most jobs you will find nothing, and finding nothing is the useful result &#8212; because it tells you the question will be settled by the governing law rather than by agreement, and it tells you which law to go and check.</p>

<p>Then, for the largest live delay on the job, write down every other thing that was going wrong during the same weeks. Not the causes you want to rely on &#8212; all of them, including yours.</p>

<p>If that list is empty, your claim is stronger than you think and you should say so clearly. If it has three items on it, you now know what the other side's first response will be, and you have the option of dealing with it before they raise it rather than after.</p>

<h2>Key takeaways</h2>

<p>&#10004; There is no universally accepted definition of concurrent delay, which is why competent people argue about it in good faith.</p>

<p>&#10004; What matters is concurrent effect during the overrun, not events that happened to start on the same day.</p>

<p>&#10004; FIDIC 2017 sends the question to the Special Provisions, and most projects leave that document empty.</p>

<p>&#10004; The English line grants time but refuses the money; the Scottish line has been open to apportioning between causes.</p>

<p>&#10004; Concurrency usually moves a delay from compensable to excusable-only rather than destroying the claim outright.</p>

<p>&#10004; The prevention principle is why an employer that contributed to the delay cannot simply insist on the original date.</p>

<p>&#10004; Modelled methods show approximate concurrency only; establishing the real thing requires as-built records.</p>

<h2>What&#39;s coming next</h2>

<p>The blind spot every method shares deserves its own week. A contractor that slows down because the job is already held up by somebody else is behaving rationally and looks, in every programme ever drawn, exactly like a contractor in default. Next week is pacing: how to tell the two apart, why it is almost impossible to prove afterwards, and the one-line record that makes it provable at all.</p>
"""

NEXT_CARD = """<div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">Next in Claims &amp; Delay Analysis</div>
                            <a href="learn.html" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">Week 17 &#183; Pacing &#183; coming soon</span>
                                    <h4>Slowing down on purpose</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>"""


def words(x):
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", "", x, flags=re.S))
    return len(t.replace("&#8212;", " ").replace("&#10004;", " ").split())


def build():
    s = read(SRC)
    s = s.replace("<title>Same Facts. Two Answers. Both Defensible &#8212; The Project Control Hub</title>",
                  "<title>Both Sides Caused It. Now What? &#8212; The Project Control Hub</title>", 1)
    s = s.replace('content="Same Facts. Two Answers. Both Defensible | The Project Control Hub"',
                  'content="Both Sides Caused It. Now What? | The Project Control Hub"')
    for tag in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % tag,
                   '<meta %s content="%s">' % (tag, DESC_PLAIN), s, count=1)
    s = s.replace("claim-week-15.html", "claim-week-16.html")
    s = s.replace('<span>Week 15<span class="crumb-title"> &#183; Why two analysts disagree</span></span>',
                  '<span>Week 16<span class="crumb-title"> &#183; %s</span></span>' % CRUMB, 1)
    s = s.replace("MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 15",
                  "MODULE 05 · CLAIMS & DELAY ANALYSIS · WEEK 16", 1)
    s = s.replace('<h1 class="article-title">%s</h1>' % PREV_TITLE,
                  '<h1 class="article-title">%s</h1>' % TITLE, 1)
    s = s.replace("PMP® · Jun 14, 2028", "PMP® · " + DATE)
    s = s.replace("PMP&reg; &#183; Jun 14, 2028", "PMP&reg; &#183; " + DATE)

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
    print("\n  build_claim_week16.py — %s" % ROOT)
    page, n, mins = build()
    for probe in ("WEEK 15", "claim-week-15.html", PREV_TITLE):
        if probe in page:
            sys.exit("HATA: onceki hafta izi kaldi: %r" % probe)
    body_only = page[page.index('<div class="content-preview"'):page.index("<!-- PAYWALL CTA -->")]
    # Yalniz niteleyicisiz "Week N" bu track'e aittir; "Contract Week 20" capraz atiftir.
    qual = r"(?:Schedule|Cost\s*&(?:amp;)?\s*Cash|Risk|Contract|Claims)\s+"
    fwd = sorted({m.group(2) for m in re.finditer(r"(%s)?Week (\d+)" % qual, body_only)
                  if not m.group(1) and int(m.group(2)) > WEEK_N})
    if fwd:
        sys.exit("HATA: govdede numarali ileri atif: Week %s" % ", ".join(fwd))
    write(DST, page)
    print("  %-22s %d kelime, %d dk" % (DST, n, mins))

    prev = read(SRC)
    if 'href="claim-week-16.html"' not in prev:
        prev = prev.replace(
            '<span class="next-week-tag">Week 16 &#183; Concurrency &#183; coming soon</span>\n'
            '                                    <h4>Both sides caused it. Now what?</h4>',
            '<span class="next-week-tag">Week 16 &#183; Concurrency</span>\n'
            '                                    <h4>Both sides caused it. Now what?</h4>', 1)
        prev = prev.replace('<a href="learn.html" class="next-article-link">',
                            '<a href="claim-week-16.html" class="next-article-link">', 1)
        write(SRC, prev)
        print("  %-22s next-article -> hafta 16" % SRC)

    js = read("curriculum.js")
    old = ('        { phase: "Phase D — The Hard Arguments", n: 16,\n'
           '          title: "Concurrency — two causes, one delay, and no agreed definition",\n'
           '          short: "Concurrency", status: "upcoming" },')
    new = ('        { phase: "Phase D — The Hard Arguments", n: 16,\n'
           '          title: "Concurrency — two causes, one delay, and no agreed definition",\n'
           '          short: "Concurrency", status: "live", page: "claim-week-16.html",\n'
           '          date: "%s" },' % DATE)
    if old in js:
        write("curriculum.js", js.replace(old, new, 1))
        print("  curriculum.js          hafta 16 live (%s)" % DATE)
    elif 'page: "claim-week-16.html"' in js:
        print("  curriculum.js          zaten live")
    else:
        sys.exit("HATA: curriculum.js hafta 16 satiri beklenen halde degil")

    sm = read("sitemap.xml")
    if "claim-week-16.html" not in sm:
        write("sitemap.xml", sm.replace(
            "</urlset>",
            "  <url>\n    <loc>https://theprojectcontrolhub.com/claim-week-16.html</loc>\n"
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
