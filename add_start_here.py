#!/usr/bin/env python3
"""Build start-here.html and link it from learn.html.

Start Here is NOT a track. It is one page, five sections, no week numbers,
no "coming soon" rows, and nothing that promises a next article
(NOTES.md section 9, the open item left deliberately unacted on).

Shell (head, nav, footer) is cloned from learn.html so the two pages cannot
drift apart. Week counts are read from curriculum.js at runtime rather than
typed, so the page cannot go stale the way the jump nav did.

Idempotent: run twice, second run reports 0 dosya.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TITLE = "Start Here — The Project Control Hub"
DESC = ("What project controls is, who this curriculum is for, the five career paths it opens, "
        "and how to work through it. Written by a planning lead with 8+ years on nuclear, mining, "
        "port and high-rise projects.")

# --------------------------------------------------------------------------
# The page body
# --------------------------------------------------------------------------

BODY = '''    <!-- START HERE PAGE -->
    <div class="learn-page">
        <div class="learn-container">

            <div class="learn-header">
                <div class="learn-header-badge">
                    <i class='bx bx-compass'></i> START HERE
                </div>
                <h1>New Here? Read This First.</h1>
                <p>Five short answers before you start. What project controls is, whether this is written for you, where it can take you, and how to work through it. Seven minutes, and then you will know which track to open.</p>
                <div class="learn-header-meta">
                    <span class="learn-meta-item"><i class='bx bx-time-five'></i> 7 min read</span>
                    <span class="learn-meta-item"><i class='bx bx-book-open'></i> No prior knowledge assumed</span>
                    <span class="learn-meta-item"><i class='bx bx-lock-open'></i> Free, and it stays free</span>
                </div>
            </div>

            <nav class="track-jump" aria-label="Jump to a section">
                <a href="#what" class="track-jump-link" data-jump="what">What it is</a>
                <a href="#who" class="track-jump-link" data-jump="who">Is this for you</a>
                <a href="#paths" class="track-jump-link" data-jump="paths">Five paths</a>
                <a href="#ladder" class="track-jump-link" data-jump="ladder">The ladder</a>
                <a href="#how" class="track-jump-link" data-jump="how">How to use it</a>
            </nav>

            <div class="modules-list">

                <!-- 1 -->
                <div class="track-header" id="what">
                    <div class="track-badge free"><i class='bx bx-help-circle'></i> ONE</div>
                    <h2>What Project Controls Actually Is</h2>
                    <p class="track-sub">It is not scheduling. Scheduling is one of its instruments.</p>
                    <p class="track-desc">A construction project is a large machine with almost no windows. Thousands of things happen every week across engineering, procurement and site, and no one person can see them. Project controls is the instrumentation. It measures what the project is doing, compares that against what the project promised, works out where it is heading, and puts a number in front of the people who can still change the outcome.</p>
                    <p class="track-desc">The word "control" misleads people. Project controls does not control the project. It cannot pour concrete faster, and it cannot make a vendor deliver on time. What it does is take away the excuse of not knowing. When a project finishes late, it very rarely surprised anyone at the end. It told somebody in month three, quietly, in a number nobody acted on.</p>
                    <p class="track-desc">That work splits into a handful of disciplines that share one model of the project. Planning owns the time. Cost control owns the money and the cash. Risk owns what has not happened yet. Contract and claims own entitlement, which is the right to more time or more money when something outside your control changed the job. Reporting connects all of them to the people who decide. On a small job one person does all of it. On a megaproject each is a department, and knowing where the boundaries fall is half of working effectively.</p>
                    <div class="track-note">
                        <i class='bx bx-bulb'></i>
                        <p><strong>The misconception worth killing early.</strong> Most people arrive believing project controls means Primavera P6. P6 is a calculator. It answers the question you type into it, and it has no opinion about whether the question was any good. Every serious mistake in this field is made before the software opens.</p>
                    </div>
                </div>

                <!-- 2 -->
                <div class="track-header" id="who">
                    <div class="track-badge free"><i class='bx bx-user-check'></i> TWO</div>
                    <h2>Is This Written for You?</h2>
                    <p class="track-sub">Probably, if you are already near a construction project.</p>
                    <p class="track-desc">This curriculum assumes you understand what a construction project is and roughly how one is built. It does not assume you have ever opened scheduling software, run a report, or read a contract clause. Everything technical is built from the ground up.</p>
                    <div class="track-outcomes">
                        <h3>It is written for</h3>
                        <ul>
                        <li>Civil, mechanical and electrical engineers moving toward planning or controls</li>
                        <li>Site engineers who produce the progress data and want to know where it goes</li>
                        <li>Quantity surveyors and cost engineers who work next to a schedule they did not build</li>
                        <li>Planners already in the role who learned the software but never the reasoning</li>
                        <li>Fresh graduates with an engineering degree and no field experience yet</li>
                        <li>Project managers who inherited a monthly report they cannot interrogate</li>
                        </ul>
                    </div>
                    <p class="track-desc">It is not written for someone who needs to produce a Primavera file by Friday. That is a legitimate need and there are faster answers to it elsewhere. What is here is slower and more durable: the reasoning underneath the file. The tools come later, after the reasoning, because a tool you can drive but not reason about is worth nothing on a site.</p>
                    <p class="track-desc">One more thing worth saying plainly. This is written from eight years on nuclear, mining, port and high-rise projects, and it reflects how those projects actually behave rather than how a textbook says they should. Where the two disagree, the field wins and the disagreement gets explained.</p>
                </div>

                <!-- 3 -->
                <div class="track-header" id="paths">
                    <div class="track-badge free"><i class='bx bx-git-branch'></i> THREE</div>
                    <h2>The Five Paths This Opens</h2>
                    <p class="track-sub">Project controls is not one job. It is five, and they pay attention to different things.</p>
                    <p class="track-desc">Most people drift into one of these without choosing it. Knowing they exist early lets you choose. Each has a track here, and each track is a complete curriculum on its own.</p>
                </div>

                <div class="module-card">
                    <div class="module-card-header">
                        <div class="module-card-left">
                            <span class="module-num"><i class='bx bx-calendar'></i></span>
                            <div class="module-info">
                                <h2>Planning &amp; Scheduling</h2>
                                <p>You own time. You build the schedule, keep it honest as the job changes, and tell everyone what the current date really is. The most common entry point, and the one closest to the site.</p>
                            </div>
                        </div>
                        <span class="module-badge badge-active"><span class="dot-green"></span> Track 1 &#183; <span id="p1Weeks">27</span> weeks</span>
                    </div>
                </div>

                <div class="module-card">
                    <div class="module-card-header">
                        <div class="module-card-left">
                            <span class="module-num"><i class='bx bx-dollar-circle'></i></span>
                            <div class="module-info">
                                <h2>Cost &amp; Cash</h2>
                                <p>You own money. Budgets, commitments, earned value and the cash the project needs next month. Closer to the commercial team, and the path that leads most directly toward project management.</p>
                            </div>
                        </div>
                        <span class="module-badge badge-active"><span class="dot-green"></span> Track 2 &#183; <span id="p2Weeks">24</span> weeks</span>
                    </div>
                </div>

                <div class="module-card">
                    <div class="module-card-header">
                        <div class="module-card-left">
                            <span class="module-num"><i class='bx bx-error'></i></span>
                            <div class="module-info">
                                <h2>Risk</h2>
                                <p>You own what has not happened yet. Registers, quantification, contingency and the Monte Carlo run behind a completion date. The most analytical of the five, and the smallest job market.</p>
                            </div>
                        </div>
                        <span class="module-badge badge-active"><span class="dot-green"></span> Track 3 &#183; <span id="p3Weeks">18</span> weeks</span>
                    </div>
                </div>

                <div class="module-card">
                    <div class="module-card-header">
                        <div class="module-card-left">
                            <span class="module-num"><i class='bx bx-file'></i></span>
                            <div class="module-info">
                                <h2>Contract &amp; Claims</h2>
                                <p>You own entitlement. Notices, variations, extensions of time, and proving a delay was not yours. Two tracks, because reading the contract and proving the delay are different skills.</p>
                            </div>
                        </div>
                        <span class="module-badge badge-active"><span class="dot-green"></span> Tracks 4&#8211;5 &#183; <span id="p45Weeks">48</span> weeks</span>
                    </div>
                </div>

                <div class="module-card module-card-locked">
                    <div class="module-card-header">
                        <div class="module-card-left">
                            <span class="module-num"><i class='bx bx-chip'></i></span>
                            <div class="module-info">
                                <h2>Digital &amp; Project Controls Systems</h2>
                                <p>You own the machine the other four run on. Excel, Primavera, Power BI, field data capture and the interfaces to the cost system. It comes last here on purpose, because a tool without the reasoning is worth nothing.</p>
                            </div>
                        </div>
                        <span class="module-badge badge-locked"><i class='bx bx-time'></i> In preparation</span>
                    </div>
                </div>

                <!-- 4 -->
                <div class="track-header" id="ladder">
                    <div class="track-badge free"><i class='bx bx-trending-up'></i> FOUR</div>
                    <h2>Where the Job Goes</h2>
                    <p class="track-sub">The usual shape of a project controls career, and why almost nobody follows it exactly.</p>
                    <p class="track-desc">A common route runs graduate engineer, site engineer, planning engineer, senior planner, project controls lead, project controls manager. Some people then move into project management, some stay technical and go deeper, and some move to the client side where the same skills are used to check other people's numbers instead of producing them.</p>
                    <p class="track-desc">Two things are worth knowing about that list. The first is that the step from site engineer to planning engineer is the one most people underestimate. It is not a promotion, it is a change of trade. You stop being responsible for work getting done and start being responsible for what the project believes about itself, and the second job needs a different kind of thinking than the first.</p>
                    <p class="track-desc">The second is that the ladder is not what actually moves people. What moves people is the size and type of project they have been on, and whether they can defend a number in a room that does not want to hear it. That skill is not taught by title. It is the thing this curriculum is trying to build.</p>
                </div>

                <!-- 5 -->
                <div class="track-header" id="how">
                    <div class="track-badge free"><i class='bx bx-map'></i> FIVE</div>
                    <h2>How to Work Through This</h2>
                    <p class="track-sub">There is a reading order, and there is permission to ignore it.</p>
                    <p class="track-desc">Track 0 describes the shape of a construction job end to end, so the methods later have somewhere to sit. It is the natural place to start, but it is not a prerequisite. If you already work on a project you can go straight to Track 1 and come back when a term stops making sense.</p>
                    <p class="track-desc">Track 1 is the foundation everything else stands on. Cost, risk, contract and claims all assume it. After Track 1 the order is genuinely yours, because those four are independent of each other and each says so where it depends on something you have not read yet.</p>
                    <p class="track-desc">Every lesson is a single article of roughly seven minutes, published one week at a time, each one building on the last. There is nothing to install and no exercise you have to complete before the next one opens. The fundamentals are free and stay free. The digital phase, when it arrives, is where the tools are taught, and it comes last because it depends on everything before it.</p>
                    <div class="track-note">
                        <i class='bx bx-lock-open-alt'></i>
                        <p><strong>What you are looking at.</strong> <span id="shCounts">Five tracks complete, 117 lessons published</span>, one lesson a week, and a toolbox after the theory. Written by one planning lead, from the field, and corrected wherever the field disagreed with the book.</p>
                    </div>
                    <div class="track-outcomes">
                        <h3>Start with</h3>
                        <ul>
                        <li><a href="learn.html#track-0">Track 0 — The Shape of the Job</a>, if you want the map before the methods</li>
                        <li><a href="learn.html#track-1">Track 1 — Schedule Management</a>, if you are already on a project and want to begin</li>
                        <li><a href="learn.html">The full curriculum</a>, if you would rather see everything first</li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    </div>

'''

SCRIPT = '''    <script src="curriculum.js?v=123"></script>
    <script>
        // Counts come from curriculum.js so this page cannot go stale.
        (function () {
            if (typeof CURRICULUM === 'undefined') return;
            var set = function (id, val) {
                var el = document.getElementById(id);
                if (el) el.textContent = val;
            };
            set('p1Weeks', CURRICULUM.totalWeeks);
            if (typeof TRACK2 !== 'undefined') set('p2Weeks', TRACK2.totalWeeks);
            if (typeof TRACK3 !== 'undefined') set('p3Weeks', TRACK3.totalWeeks);
            if (typeof TRACK4 !== 'undefined' && typeof TRACK5 !== 'undefined') {
                set('p45Weeks', TRACK4.totalWeeks + TRACK5.totalWeeks);
            }
            var tracks = [CURRICULUM, TRACK2, TRACK3, TRACK4, TRACK5].filter(Boolean);
            var done = tracks.filter(function (t) { return t.liveCount >= t.totalWeeks; }).length;
            var lessons = tracks.reduce(function (a, t) { return a + t.liveCount; }, 0);
            set('shCounts', done + ' tracks complete, ' + lessons + ' lessons published');
        })();
    </script>
'''

# --------------------------------------------------------------------------
# learn.html — the card that points at it, plus two stale strings
# --------------------------------------------------------------------------

LEARN_CARD = '''                <!-- ===== START HERE ===== -->
                <a href="start-here.html" class="start-here-card">
                    <span class="sh-icon"><i class='bx bx-compass'></i></span>
                    <span class="sh-body">
                        <strong>New here? Read this first.</strong>
                        <span>What project controls is, whether this is for you, and the five paths it opens. Seven minutes, no prior knowledge.</span>
                    </span>
                    <i class='bx bx-right-arrow-alt sh-arrow'></i>
                </a>

'''

LEARN_CSS = '''
        .start-here-card {
            display: flex; align-items: center; gap: 16px;
            padding: 20px 24px; margin-bottom: 32px;
            background: #fff; border: 1px solid #e2e8f0; border-radius: 14px;
            text-decoration: none; transition: border-color .15s, transform .15s;
        }
        .start-here-card:hover { border-color: #10b981; transform: translateY(-1px); }
        .sh-icon {
            width: 42px; height: 42px; flex-shrink: 0;
            display: flex; align-items: center; justify-content: center;
            background: #ecfdf5; border-radius: 10px;
        }
        .sh-icon i { font-size: 22px; color: #059669; }
        .sh-body { display: flex; flex-direction: column; gap: 3px; }
        .sh-body strong { font-size: 15px; font-weight: 700; color: #1e293b; }
        .sh-body span { font-size: 13.5px; color: #64748b; line-height: 1.55; }
        .sh-arrow { margin-left: auto; font-size: 20px; color: #cbd5e1; flex-shrink: 0; }
        .start-here-card:hover .sh-arrow { color: #10b981; }
        @media (max-width: 640px) {
            .start-here-card { padding: 16px 18px; gap: 13px; }
            .sh-arrow { display: none; }
        }
    </style>'''

JUMP_NAV = '''                <nav class="track-jump" aria-label="Jump to a section">
                    <a href="start-here.html" class="track-jump-link">Start Here</a>
                    <a href="#track-0" class="track-jump-link" data-jump="track-0">Shape of the Job <span id="jn0">17</span></a>
                    <a href="#track-1" class="track-jump-link" data-jump="track-1">Schedule <span id="jn1">27</span></a>
                    <a href="#track-2" class="track-jump-link" data-jump="track-2">Cost &amp; Cash <span id="jn2">24</span></a>
                    <a href="#track-3" class="track-jump-link" data-jump="track-3">Risk <span id="jn3">18</span></a>
                    <a href="#track-4" class="track-jump-link" data-jump="track-4">Contract <span id="jn4">20</span></a>
                    <a href="#track-5" class="track-jump-link" data-jump="track-5">Claims <span id="jn5">28</span></a>
                    <a href="#roadmap" class="track-jump-link" data-jump="roadmap">Roadmap</a>
                    <a href="#toolbox" class="track-jump-link" data-jump="toolbox">Toolbox</a>
                </nav>'''

JUMP_WIRING = '''
            // Jump-nav counts computed, never typed — the old markup said
            // Contract 1/20 long after Contract finished, and omitted Claims.
            [['jn0', typeof TRACK0 !== 'undefined' ? TRACK0 : null],
             ['jn1', CURRICULUM],
             ['jn2', typeof TRACK2 !== 'undefined' ? TRACK2 : null],
             ['jn3', typeof TRACK3 !== 'undefined' ? TRACK3 : null],
             ['jn4', typeof TRACK4 !== 'undefined' ? TRACK4 : null],
             ['jn5', typeof TRACK5 !== 'undefined' ? TRACK5 : null]].forEach(function (p) {
                var el = document.getElementById(p[0]);
                if (el && p[1]) el.textContent = p[1].totalWeeks;
            });
'''


def build_start_here():
    learn = (ROOT / "learn.html").read_text(encoding="utf-8")

    head_end = learn.index("    <!-- LEARN PAGE -->")
    tail_start = learn.index("    <!-- MOBILE NAV -->")
    tail_end = learn.index('    <script src="curriculum.js')

    head = learn[:head_end]
    tail = learn[tail_start:tail_end]

    # meta
    head = head.replace("<title>Learn — The Project Control Hub</title>", f"<title>{TITLE}</title>")
    head = re.sub(r'(<meta name="description" content=")[^"]*(">)', r"\g<1>" + DESC + r"\g<2>", head)
    head = head.replace("https://theprojectcontrolhub.com/learn.html",
                        "https://theprojectcontrolhub.com/start-here.html")
    head = head.replace('<meta property="og:title" content="Curriculum — The Project Control Hub">',
                        '<meta property="og:title" content="Start Here — The Project Control Hub">')
    head = head.replace('<meta name="twitter:title" content="Curriculum — The Project Control Hub">',
                        '<meta name="twitter:title" content="Start Here — The Project Control Hub">')
    head = re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*(">)',
                  r"\g<1>" + DESC + r"\g<2>", head)

    # nav highlight: Learn should not look active on this page
    head = head.replace('<a href="learn.html" class="nav-link active">', '<a href="learn.html" class="nav-link">')

    page = head + BODY + tail + SCRIPT + "</body>\n</html>\n"
    return page


def patch_learn():
    p = ROOT / "learn.html"
    src = p.read_text(encoding="utf-8")
    if "start-here-card" in src:
        print("  = learn.html Start Here: zaten uygulanmis, atlandi")
        return 0
    old_nav_start = src.index('                <nav class="track-jump"')
    old_nav_end = src.index("</nav>", old_nav_start) + len("</nav>")
    src = src[:old_nav_start] + JUMP_NAV + src[old_nav_end:]

    src = src.replace("    </style>", LEARN_CSS, 1)
    src = src.replace("                <!-- ===== SECTION: ORIENTATION ===== -->",
                      LEARN_CARD + "                <!-- ===== SECTION: ORIENTATION ===== -->", 1)
    src = src.replace("            // Track 0 — The Shape of the Job",
                      JUMP_WIRING + "\n            // Track 0 — The Shape of the Job", 1)
    p.write_text(src, encoding="utf-8")
    print("  + learn.html Start Here: yazildi")
    return 1


def main():
    written = 0
    # learn.html first: start-here.html clones its head, so patching learn
    # afterwards would make the clone differ on the next run.
    written += patch_learn()
    out = ROOT / "start-here.html"
    page = build_start_here()
    if out.exists() and out.read_text(encoding="utf-8") == page:
        print("  = start-here.html: degisiklik yok")
    else:
        out.write_text(page, encoding="utf-8")
        print("  + start-here.html: yazildi")
        written += 1
    print(f"\n{written} dosya")
    if written:
        print("Not: sitemap.xml ve ana sayfa linki elle eklenmeli.")


if __name__ == "__main__":
    main()
