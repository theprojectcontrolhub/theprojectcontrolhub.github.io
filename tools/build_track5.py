#!/usr/bin/env python3
"""Track 5 — Claims & Delay Analysis: curriculum kaydı ve bağlantıları.

Idempotent. İkinci çalıştırma no-op olmalı, hata değil (NOTES.md §5).
Sayfa üretmez; sadece curriculum.js + learn.html + index.html bağlar.
"""
import io, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CHANGED = []


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    # Aynı içerikse dosyaya dokunma: CHANGED yalnızca gerçek değişikliği saymalı,
    # yoksa ikinci çalıştırma cache sürümünü boşuna artırır.
    if os.path.exists(p) and read(p) == s:
        return
    io.open(p, "w", encoding="utf-8").write(s)
    CHANGED.append(p)


# --------------------------------------------------------------- hafta listesi
# (n, phase or None, title, short)
WEEKS = [
    (1, "Phase A — What a Claim Has to Prove",
     "Claims fundamentals — from preserved right to measured quantum", "Claims fundamentals"),
    (2, None, "Cause and effect — the chain a claim has to close", "Cause and effect"),
    (3, None, "Types of delay — excusable, compensable and the ones that pay nothing", "Types of delay"),
    (4, None, "Criticality and float — what every claim actually argues about", "Criticality and float"),

    (5, "Phase B — The Evidence the Analysis Runs On",
     "The as-planned programme — validating a baseline you did not build", "The as-planned programme"),
    (6, None, "The as-built programme — reconstructing what actually happened", "The as-built programme"),
    (7, None, "Programme updates — the contemporaneous record and the gaps in it", "Programme updates"),

    (8, "Phase C — Methods, by the Evidence They Need",
     "Choosing a method — what the SCL and AACE taxonomies are for", "Choosing a method"),
    (9, None, "Impacted as-planned — delay modelled into a plan that never happened", "Impacted as-planned"),
    (10, None, "Time impact analysis — fragnets, updates and prospective assessment", "Time impact analysis"),
    (11, None, "Windows analysis — contemporaneous periods and time slices", "Windows analysis"),
    (12, None, "As-planned versus as-built — the comparison and its limits", "As-planned versus as-built"),
    (13, None, "Collapsed as-built — subtraction, and the judgement hidden in it", "Collapsed as-built"),
    (14, None, "Why two analysts disagree — method choice as the real dispute", "Why two analysts disagree"),

    (15, "Phase D — The Hard Arguments",
     "Concurrency — two causes, one delay, and no agreed definition", "Concurrency"),
    (16, None, "Pacing — the delay that answers another delay", "Pacing"),
    (17, None, "Acceleration and mitigation — directed, constructive and unpaid", "Acceleration and mitigation"),

    (18, "Phase E — Disruption",
     "Disruption — the loss that never touches the critical path", "Disruption"),
    (19, None, "The measured mile — comparing the job to itself", "The measured mile"),
    (20, None, "Productivity loss — the methods used when no clean mile exists", "Productivity loss"),
    (21, None, "Global and total cost claims — why they fail", "Global and total cost claims"),

    (22, "Phase F — Quantum",
     "Prolongation — the cost of time on site", "Prolongation"),
    (23, None, "Head office overhead and finance — the formulae and their weaknesses",
     "Head office and finance"),
    (24, None, "Pricing and substantiation — from cost records to a number",
     "Pricing and substantiation"),

    (25, "Phase G — Presenting the Claim",
     "Assembling a claim — contents, executive summary and appendices", "Assembling a claim"),
    (26, None, "Defending a claim — reading one from the other side", "Defending a claim"),
    (27, None, "What five tracks were for — the claim that never happened",
     "What five tracks were for"),
]

# Track 4 Mar 1, 2028'de bitiyor; dizi haftalık devam ediyor (§10.1 kararı).
START = datetime.date(2028, 3, 1)


def week_date(n):
    d = START + datetime.timedelta(days=7 * n)
    return "%s %d, %d" % (d.strftime("%b"), d.day, d.year)


def track5_block():
    lines = ["const TRACK5 = {",
             '    title: "Claims & Delay Analysis",',
             "    totalWeeks: %d," % len(WEEKS),
             "    weeks: ["]
    for n, phase, title, short in WEEKS:
        if phase:
            lines.append("")
            lines.append("        // ---- %s ----" % phase.upper())
            head = '{ phase: "%s", n: %d,\n          ' % (phase, n)
        else:
            head = "{ n: %d, " % n
        row = ('        %stitle: "%s",\n'
               '          short: "%s", status: "upcoming" }' % (head, title, short))
        lines.append(row + ",")
    lines[-1] = lines[-1].rstrip(",")
    lines += [
        "    ],",
        '    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },',
        "    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },",
        "    get latestLiveWeek() {",
        '        const live = this.weeks.filter(w => w.status === "live");',
        "        return live.length ? live[live.length - 1] : null;",
        "    },",
        "    get phaseCount() { return this.weeks.filter(w => w.phase).length; },",
        "    getWeek(n) { return this.weeks.find(w => w.n === n); }",
        "};",
        "",
        "function renderTrack5Curriculum() { return learnCurriculumHTML(TRACK5); }",
        "function renderTrack5Sidebar(currentWeek) { return sidebarHTML(TRACK5, currentWeek); }",
        "function renderHomeTrack5()               { return homeCurriculumHTML(TRACK5); }",
        "function renderHomeTrack5Badge() {",
        "  return badgeText(TRACK5);",
        "}",
        "",
        "function renderTrack5Progress() {",
        "    return { text: `${TRACK5.liveCount} of ${TRACK5.totalWeeks} published`,"
        " percent: TRACK5.progressPercent };",
        "}",
    ]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------- 1. curriculum.js
def patch_curriculum():
    js = read("curriculum.js")
    if "const TRACK5" in js:
        print("  curriculum.js  TRACK5 zaten var")
    else:
        anchor = ("function renderTrack4Progress() {\n"
                  "    return { text: `${TRACK4.liveCount} of ${TRACK4.totalWeeks} published`,"
                  " percent: TRACK4.progressPercent };\n}\n")
        if anchor not in js:
            sys.exit("HATA: renderTrack4Progress bağlama noktası bulunamadı")
        js = js.replace(anchor, anchor + "\n\n"
                        "// ===================== TRACK 5 — CLAIMS & DELAY ANALYSIS =====================\n"
                        + track5_block(), 1)
        print("  curriculum.js  TRACK5 eklendi (%d hafta)" % len(WEEKS))

    # badgeText: hiç canlı hafta yokken "Week 0 of 27" yazıyordu.
    old = ("    var l = track.latestLiveWeek;\n"
           "    return '<span class=\"dot-green\"></span> In Progress &#183; Week '"
           " + (l ? l.n : 0) + ' of ' + track.totalWeeks;")
    new = ("    if (track.liveCount === 0) {\n"
           "        return \"<i class='bx bx-time'></i> Starting soon &#183; \""
           " + track.totalWeeks + ' weeks';\n"
           "    }\n"
           "    var l = track.latestLiveWeek;\n"
           "    return '<span class=\"dot-green\"></span> In Progress &#183; Week '"
           " + l.n + ' of ' + track.totalWeeks;")
    if old in js:
        js = js.replace(old, new, 1)
        print("  curriculum.js  badgeText() 0-canlı durumu eklendi")
    elif "track.liveCount === 0" in js:
        print("  curriculum.js  badgeText() zaten yamalı")
    else:
        sys.exit("HATA: badgeText gövdesi beklenen halde değil")

    # Rozet sınıfı: 0 canlıyken kilitli, sonra aktif.
    if "function badgeClass" not in js:
        js = js.replace("function renderHomeBadge() {",
                        "function badgeClass(track) {\n"
                        "  return (track && track.liveCount === 0) ? 'badge-locked' : 'badge-active';\n"
                        "}\n\n"
                        "function renderHomeBadge() {", 1)
        print("  curriculum.js  badgeClass() eklendi")
    write("curriculum.js", js)


# ------------------------------------------------------------------ 2. learn.html
LEARN_ROADMAP_CARD = """                    <!-- TRACK 5: CLAIMS -->
                    <div class="roadmap-card">
                        <span class="roadmap-marker"><i class='bx bx-file-find'></i></span>
                        <div class="roadmap-body">
                            <h3>Track 5 &#183; Claims &amp; Delay Analysis</h3>
                            <p>When things go wrong, who pays? Forensic delay analysis, extension of time, concurrency, disruption and productivity loss &#8212; turning a preserved entitlement into a number somebody actually pays.</p>
                        </div>
                        <span class="roadmap-badge"><i class='bx bx-time'></i> On the roadmap</span>
                    </div>

"""

LEARN_TRACK5 = """
<!-- ===== TRACK 5 — CLAIMS &amp; DELAY ANALYSIS ===== -->
                    <div class="track-header" id="track-5">
                        <div class="track-badge free"><i class='bx bx-file-find'></i> TRACK 5 &#183; FREE &#183; STARTING SOON</div>
                        <h2>Claims &amp; Delay Analysis</h2>
                        <p class="track-sub">The number. What the right you kept is actually worth.</p>
                        <p class="track-desc">Track 4 ended holding a preserved right, a programme that can be re-run, and the question it deliberately never answered: how much? This track is the answer &#8212; forensic delay methods and why two competent analysts reach different numbers, float and concurrency, disruption and the measured mile, and the quantum that turns an entitlement into an invoice. The method you can use is decided by the records you kept, not by the one you prefer.</p>
                        <div class="track-outcomes">
                            <h3>After this track you can</h3>
                            <ul>
                            <li>Choose a delay methodology from the records you actually have, and say why the other four would answer differently</li>
                            <li>Reconstruct an as-built programme and defend it as a finding rather than a record</li>
                            <li>Argue criticality, float and concurrency without conceding any of them by accident</li>
                            <li>Prove disruption from a measured mile, and know how much weaker every alternative is</li>
                            <li>Price prolongation, head office overhead and finance from the contract rather than from a formula you like</li>
                            <li>Read a claim the way the reviewer will, and fix what they would have found</li>
                            </ul>
                        </div>
                        <div class="track-note">
                            <i class='bx bx-lock-open-alt'></i>
                            <p><strong>The rock is worth $48,450 and the net margin on the job is $48,163.</strong> Four tracks have circled that pair without closing it &#8212; <a href="risk-week-5.html">Risk Week 5</a> priced the rock, <a href="contract-week-13.html">Contract Week 13</a> asked whether the contract even calls it a variation. Track 5 opens with the notice served on time, and the argument moved to what it is worth.</p>
                        </div>
                    </div>
                    <!-- MODULE 05: CLAIMS &amp; DELAY ANALYSIS -->
                    <div class="module-card">
                        <div class="module-card-header">
                            <div class="module-card-left">
                                <span class="module-num">05</span>
                                <div class="module-info">
                                    <h2>Claims &amp; Delay Analysis</h2>
                                    <p>Forensic delay analysis, disruption and quantum &#8212; the methods that turn a preserved entitlement into a number, and the reasons two analysts using two accepted methods disagree.</p>
                                </div>
                            </div>
                            <span class="module-badge badge-locked" id="t5ModuleBadge"><i class='bx bx-time'></i> Starting soon</span>
                        </div>
                        <div class="module-tools">
                            <span class="tool-tag-label">Topics:</span>
                            <span class="tool-tag">Delay Analysis</span>
                            <span class="tool-tag">Concurrency</span>
                            <span class="tool-tag">Float</span>
                            <span class="tool-tag">Windows</span>
                            <span class="tool-tag">Disruption</span>
                            <span class="tool-tag">Measured Mile</span>
                            <span class="tool-tag">Prolongation</span>
                            <span class="tool-tag">Quantum</span>
                        </div>
                        <div class="module-weeks" id="track5Weeks"></div>
                        <div class="module-progress">
                            <div class="progress-label">
                                <span id="t5ProgressText">0 of 27 published</span>
                                <span id="t5ProgressPct">0%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" id="t5ProgressFill" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>
"""

LEARN_JS = """
            const t5El = document.getElementById('track5Weeks');
            if (t5El && typeof renderTrack5Curriculum === 'function') {
                t5El.innerHTML = renderTrack5Curriculum();
                if (typeof renderTrack5Progress === 'function') {
                    const p5 = renderTrack5Progress();
                    const t5t = document.getElementById('t5ProgressText');
                    const t5p = document.getElementById('t5ProgressPct');
                    const t5f = document.getElementById('t5ProgressFill');
                    if (t5t) t5t.textContent = p5.text;
                    if (t5p) t5p.textContent = p5.percent + '%';
                    if (t5f) t5f.style.width = p5.percent + '%';
                }
            }
            const b5 = document.getElementById('t5ModuleBadge');
            if (b5 && typeof renderHomeTrack5Badge === 'function') {
                b5.innerHTML = renderHomeTrack5Badge();
                if (typeof badgeClass === 'function' && typeof TRACK5 !== 'undefined') {
                    b5.className = 'module-badge ' + badgeClass(TRACK5);
                }
            }
"""


def patch_learn():
    h = read("learn.html")
    if 'id="track5Weeks"' in h:
        print("  learn.html     Track 5 bloğu zaten var")
    else:
        if LEARN_ROADMAP_CARD not in h:
            sys.exit("HATA: learn.html Track 5 roadmap kartı bulunamadı")
        h = h.replace(LEARN_ROADMAP_CARD, "", 1)
        anchor = "\n                    <div class=\"roadmap-section\" id=\"roadmap\">"
        if anchor not in h:
            sys.exit("HATA: learn.html roadmap-section bulunamadı")
        h = h.replace(anchor, LEARN_TRACK5 + anchor, 1)
        h = h.replace("<h2>Tracks 5 and 6</h2>", "<h2>Track 6</h2>", 1)
        print("  learn.html     Track 5 bölümü eklendi, roadmap kartı kaldırıldı")

    if "const t5El" not in h:
        anchor = ("            const b4 = document.getElementById('t4ModuleBadge');\n"
                  "            if (b4 && typeof TRACK4 !== 'undefined' && typeof badgeText === 'function')"
                  " b4.innerHTML = badgeText(TRACK4);\n")
        if anchor not in h:
            sys.exit("HATA: learn.html t4ModuleBadge JS bağlama noktası bulunamadı")
        h = h.replace(anchor, anchor + LEARN_JS, 1)
        print("  learn.html     Track 5 JS bağlandı")
    write("learn.html", h)


# ------------------------------------------------------------------ 3. index.html
INDEX_LOCKED = """                <!-- TRACK 5: CLAIMS -->
                <div class="module-track module-track-locked">
                    <div class="module-track-header">
                        <div class="module-track-left">
                            <span class="module-number locked">05</span>
                            <div>
                                <h3 class="module-title">Claims &amp; Delay Analysis</h3>
                                <p class="module-desc">When things go wrong, who pays? Forensic delay analysis, extension of time, concurrency, disruption and productivity loss &#8212; turning a preserved entitlement into a number somebody actually pays.</p>
                            </div>
                        </div>
                        <span class="module-status locked-status"><i class='bx bx-map-alt'></i> On the roadmap</span>
                    </div>
                </div>
"""

INDEX_ACTIVE = """                <!-- TRACK 5: CLAIMS &amp; DELAY ANALYSIS -->
                <div class="module-track">
                    <div class="module-track-header">
                        <div class="module-track-left">
                            <span class="module-number">05</span>
                            <div>
                                <h3 class="module-title">Claims &amp; Delay Analysis</h3>
                                <p class="module-desc">What the right you kept is actually worth. Forensic delay methods and why they disagree, float and concurrency, disruption and the measured mile, and the quantum that turns an entitlement into an invoice.</p>
                            </div>
                        </div>
                        <span class="module-status" id="homeTrack5Badge"><i class='bx bx-time'></i> Starting soon</span>
                    </div>
                    <div class="module-posts" id="homeTrack5"></div>
                </div>
"""

INDEX_JS = """
            const t5 = document.getElementById('homeTrack5');
            if (t5 && typeof renderHomeTrack5 === 'function') {
                t5.innerHTML = renderHomeTrack5();
            }
            const t5Badge = document.getElementById('homeTrack5Badge');
            if (t5Badge && typeof renderHomeTrack5Badge === 'function') {
                t5Badge.innerHTML = renderHomeTrack5Badge();
            }
"""


def patch_index():
    h = read("index.html")
    if 'id="homeTrack5"' in h:
        print("  index.html     Track 5 kartı zaten aktif")
    else:
        if INDEX_LOCKED not in h:
            sys.exit("HATA: index.html kilitli Track 5 kartı bulunamadı")
        h = h.replace(INDEX_LOCKED, INDEX_ACTIVE, 1)
        print("  index.html     Track 5 kartı aktifleştirildi")

    if "const t5 = document.getElementById('homeTrack5')" not in h:
        anchor = ("                const t4Badge = document.getElementById('homeTrack4Badge');\n"
                  "                if (t4Badge && typeof renderHomeTrack4Badge === 'function') {\n"
                  "                    t4Badge.innerHTML = renderHomeTrack4Badge();\n"
                  "                }\n")
        if anchor not in h:
            sys.exit("HATA: index.html homeTrack4 JS bağlama noktası bulunamadı")
        h = h.replace(anchor, anchor + INDEX_JS, 1)
        print("  index.html     Track 5 JS bağlandı")
    write("index.html", h)


# ------------------------------------------------------------- 4. checker kaydı
def patch_checker():
    p = "tools/check_site.py"
    s = read(p)
    if "claim-week-" in s:
        print("  check_site.py  Claims zaten kayıtlı")
        return
    old = '          "Contract": ("contract-week-", 20)}'
    new = ('          "Contract": ("contract-week-", 20), "Claims": ("claim-week-", 27)}')
    if old not in s:
        sys.exit("HATA: check_site.py TRACKS sözlüğü beklenen halde değil")
    write(p, s.replace(old, new, 1))
    print("  check_site.py  Claims (claim-week-, 27) kaydedildi")


# --------------------------------------------------------------- 5. cache bump
def bump_cache(force=False):
    if not force:
        print("  cache          değişiklik yok, bump atlandı")
        return
    cur = re.search(r"curriculum\.js\?v=(\d+)", read("index.html"))
    if not cur:
        sys.exit("HATA: cache sürümü okunamadı")
    old = int(cur.group(1))
    target = old + 1
    n = 0
    for f in sorted(os.listdir(".")):
        if not f.endswith(".html"):
            continue
        s = read(f)
        t = s.replace("curriculum.js?v=%d" % old, "curriculum.js?v=%d" % target)
        if t != s:
            write(f, t)
            n += 1
    print("  cache          curriculum.js v%d -> v%d (%d sayfa)" % (old, target, n))


if __name__ == "__main__":
    print("\n  build_track5.py — %s" % ROOT)
    patch_curriculum()
    patch_learn()
    patch_index()
    patch_checker()
    # Yalnızca gerçekten bir şey değiştiyse sürüm artır; ikinci çalıştırma no-op.
    bump_cache(force=bool(CHANGED))
    print("  tamam, %d dosya yazıldı\n" % len(set(CHANGED)))
