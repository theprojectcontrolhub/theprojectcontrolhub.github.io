#!/usr/bin/env python3
"""Add Track 6 (Interfaces) and The Life of a Project to curriculum.js and
learn.html, and retire Track 0 from the page.

Track 0 stays in curriculum.js as a dormant object. It is removed from
learn.html because a 17-row "Coming soon" block above five complete tracks
is the most prominent unfinished thing on the site, and the decision was to
revisit it after the tracks are written, if it is needed at all.

Idempotent: run twice, second run reports 0 dosya.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ==========================================================================
# curriculum.js
# ==========================================================================

TRACK6_JS = '''

// ===================== TRACK 6 — INTERFACES =====================
// The printed handoff in claim-week-28 names four subjects: the scope sitting
// with somebody else, the critical path through a purchase order, the work
// where two programmes meet, and the number with more than one owner. All
// four appear below. Sources measured 2026-07-31: EPCM 171, interface 284,
// coordination 140, JV/consortium/alliance/partnering/IPD 249.
const TRACK6 = {
    title: "Interfaces",
    totalWeeks: 14,
    weeks: [
        { phase: "Who holds the scope", n: 1, title: "The shape every track has assumed \\u2014 one contract, one Engineer, one programme", short: "The shape every track assumed", status: "upcoming" },
        { n: 2, title: "How many contracts are there \\u2014 the axis nobody teaches", short: "How many contracts are there", status: "upcoming" },
        { n: 3, title: "EPCM \\u2014 instructing people you have no contract with", short: "Instructing without a contract", status: "upcoming" },
        { n: 4, title: "The Engineer, multiplied \\u2014 determination when every package has its own", short: "The Engineer, multiplied", status: "upcoming" },
        { n: 5, title: "Concurrency without a head contract \\u2014 the Special Provisions that do not exist", short: "Concurrency with no head contract", status: "upcoming" },
        { phase: "When the contractor is plural", n: 6, title: "Joint ventures and consortia \\u2014 one face, several sets of books", short: "Joint ventures and consortia", status: "upcoming" },
        { n: 7, title: "Alliancing, partnering and IPD \\u2014 contracts built to suppress claims", short: "Alliancing, partnering and IPD", status: "upcoming" },
        { phase: "The critical path leaves the site", n: 8, title: "Procurement on the critical path \\u2014 when the path runs through an order", short: "Procurement on the critical path", status: "upcoming" },
        { phase: "Where two programmes meet", n: 9, title: "The work in nobody\\u2019s scope \\u2014 the gap between two risk registers", short: "The work in nobody\\u2019s scope", status: "upcoming" },
        { n: 10, title: "Interface management as a function \\u2014 owning a boundary, not reporting one", short: "Interface management", status: "upcoming" },
        { n: 11, title: "Access, sequencing and the delay that belongs to no one", short: "The delay that belongs to no one", status: "upcoming" },
        { phase: "The number with more than one owner", n: 12, title: "Progress and valuation collide \\u2014 two methods, one monthly number", short: "Progress and valuation collide", status: "upcoming" },
        { n: 13, title: "The cost that arrives from somebody else\\u2019s books \\u2014 another ledger, another cut-off", short: "Somebody else\\u2019s books", status: "upcoming" },
        { n: 14, title: "Document control at organisational scale \\u2014 six firms, one transmittal", short: "Document control at scale", status: "upcoming" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() { const l = this.weeks.filter(w => w.status === "live"); return l.length ? l[l.length - 1] : null; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};

// ===================== THE LIFE OF A PROJECT =====================
// The integration layer. Tracks 1-5 teach the method; Interfaces shows how the
// method changes shape under a different contract; this shows the order the
// work actually arrives in, what feeds what, and which record is born where.
// Rule for every week: teach the occasion, hand the method to the track that
// owns it. Every week ends with "Records born here".
const LIFECYCLE = {
    title: "The Life of a Project",
    totalWeeks: 52,
    weeks: [
        { n: 1, title: "The journey of one drawing \\u2014 six hands, six changes, one as-built", short: "The journey of one drawing", status: "upcoming" },

        { phase: "Phase A \\u2014 Before the project exists", n: 2, title: "Why a project exists \\u2014 business need, investment decision, and who is already committed", short: "Why a project exists", status: "upcoming" },
        { n: 3, title: "Feasibility \\u2014 what gets studied, what gets assumed, and which assumption reaches you", short: "Feasibility", status: "upcoming" },
        { n: 4, title: "Delivery strategy \\u2014 how the owner decided to buy it", short: "Delivery strategy", status: "upcoming" },
        { n: 5, title: "Packaging and tender strategy \\u2014 why the job was split, and what each split costs", short: "Packaging and tender strategy", status: "upcoming" },
        { n: 6, title: "Tender to award \\u2014 ITB, clarification, evaluation, and the estimate you inherit", short: "Tender to award", status: "upcoming" },

        { phase: "Phase B \\u2014 Start-up", n: 7, title: "Day one \\u2014 the folder, the contract, and the dates you must know by Friday", short: "Day one", status: "upcoming" },
        { n: 8, title: "The kick-off \\u2014 what gets decided, and what gets deferred forever", short: "The kick-off", status: "upcoming" },
        { n: 9, title: "The project execution plan \\u2014 including the communication matrix nobody reads", short: "The project execution plan", status: "upcoming" },
        { n: 10, title: "Who is who \\u2014 client, PMC, EPC, vendors, and the authority behind each name", short: "Who is who", status: "upcoming" },
        { n: 11, title: "Coding philosophy \\u2014 the decisions that cannot be made later", short: "Coding philosophy", status: "upcoming" },
        { n: 12, title: "Setting up document control \\u2014 transmittals, revisions, registers", short: "Setting up document control", status: "upcoming" },

        { phase: "Phase C \\u2014 The control system", n: 13, title: "Building the baseline \\u2014 the two weeks, not the method", short: "Building the baseline", status: "upcoming" },
        { n: 14, title: "Rules of credit \\u2014 agreeing how progress will be claimed, before it is claimed", short: "Rules of credit", status: "upcoming" },
        { n: 15, title: "The calendar \\u2014 data date, cut-off, and three departments closing on three days", short: "The calendar", status: "upcoming" },
        { n: 16, title: "The reporting structure \\u2014 daily, weekly, monthly, executive", short: "The reporting structure", status: "upcoming" },
        { n: 17, title: "The meeting structure \\u2014 who chairs, who decides, and which ones move blame", short: "The meeting structure", status: "upcoming" },

        { phase: "Phase D \\u2014 Engineering", n: 18, title: "How engineering flows \\u2014 deliverable lists, disciplines, and the design freeze", short: "How engineering flows", status: "upcoming" },
        { n: 19, title: "Submittals, IFC and vendor documents \\u2014 the approval cycle as a programme input", short: "Submittals, IFC and approvals", status: "upcoming" },
        { n: 20, title: "Measuring engineering progress \\u2014 where percent complete is easiest to fake", short: "Measuring engineering progress", status: "upcoming" },

        { phase: "Phase E \\u2014 Procurement", n: 21, title: "The procurement cycle \\u2014 requisition to purchase order", short: "The procurement cycle", status: "upcoming" },
        { n: 22, title: "From approved vendor document to manufacturing release \\u2014 and the expediting between", short: "Vendor documents to release", status: "upcoming" },
        { n: 23, title: "Long lead \\u2014 ordering before the design is finished, and the cost of being wrong", short: "Long lead", status: "upcoming" },
        { n: 24, title: "Material management \\u2014 delivered, stored, issued, installed: four quantities", short: "Material management", status: "upcoming" },

        { phase: "Phase F \\u2014 Construction", n: 25, title: "Mobilisation \\u2014 the project inside the project", short: "Mobilisation", status: "upcoming" },
        { n: 26, title: "Site logistics and temporary works \\u2014 access, laydown, cranes, and a scaffold with its own lead time", short: "Site logistics and temporary works", status: "upcoming" },
        { n: 27, title: "Work packaging \\u2014 dividing scope into something a crew can be handed", short: "Work packaging", status: "upcoming" },
        { n: 28, title: "Constraints and readiness \\u2014 drawing, material, labour, permit, access", short: "Constraints and readiness", status: "upcoming" },
        { n: 29, title: "Look-ahead planning \\u2014 the six weeks that run the site", short: "Look-ahead planning", status: "upcoming" },
        { n: 30, title: "The week, day by day \\u2014 one workable rhythm, not the rhythm", short: "The week, day by day", status: "upcoming" },
        { n: 31, title: "Daily progress \\u2014 who measures, in what unit, on which day", short: "Daily progress", status: "upcoming" },
        { n: 32, title: "Productivity on site \\u2014 where the hours went", short: "Productivity on site", status: "upcoming" },
        { n: 33, title: "Equipment and resources \\u2014 availability, utilisation, crews, camp, shifts", short: "Equipment and resources", status: "upcoming" },
        { n: 34, title: "Quality as a subtraction \\u2014 NCRs, rework, and progress that reverses", short: "Quality as a subtraction", status: "upcoming" },
        { n: 35, title: "Safety as a stoppage \\u2014 permits, holds, stand-downs, and lost time as a delay event", short: "Safety as a stoppage", status: "upcoming" },

        { phase: "Phase G \\u2014 Commercial", n: 36, title: "The monthly valuation \\u2014 progress versus payment", short: "The monthly valuation", status: "upcoming" },
        { n: 37, title: "Change on the ground \\u2014 instruction to variation to claim, as it happens", short: "Change on the ground", status: "upcoming" },
        { n: 38, title: "Forecasting \\u2014 the number you will be judged on", short: "Forecasting", status: "upcoming" },
        { n: 39, title: "Trends and the change log \\u2014 catching cost before it becomes a variation", short: "Trends and the change log", status: "upcoming" },

        { phase: "Phase H \\u2014 Governance", n: 40, title: "Who approves what \\u2014 authority, delegation, and the escalation chain", short: "Who approves what", status: "upcoming" },
        { n: 41, title: "The change control board", short: "The change control board", status: "upcoming" },
        { n: 42, title: "Risk reviews that change something", short: "Risk reviews that change something", status: "upcoming" },
        { n: 43, title: "KPIs \\u2014 leading, lagging, and the ones that get gamed", short: "KPIs, leading and lagging", status: "upcoming" },
        { n: 44, title: "The register system \\u2014 which record feeds which, and which are actually read", short: "The register system", status: "upcoming" },

        { phase: "Phase I \\u2014 Finishing", n: 45, title: "Mechanical completion \\u2014 and the birth of the punch list", short: "Mechanical completion", status: "upcoming" },
        { n: 46, title: "Pre-commissioning and commissioning \\u2014 handing the schedule to another discipline", short: "Pre-commissioning and commissioning", status: "upcoming" },
        { n: 47, title: "Performance tests", short: "Performance tests", status: "upcoming" },
        { n: 48, title: "Closing the punch list and taking over", short: "Closing the punch list", status: "upcoming" },
        { n: 49, title: "Demobilisation \\u2014 the crane, the camp and the punch list want the same people", short: "Demobilisation", status: "upcoming" },
        { n: 50, title: "Closeout \\u2014 as-built, final account, archive", short: "Closeout", status: "upcoming" },

        { phase: "Capstone", n: 51, title: "Designing a project controls system from nothing", short: "Designing the system from nothing", status: "upcoming" },
        { n: 52, title: "The first 90 days \\u2014 a contract, a BoQ, a drawing set and an empty schedule", short: "The first 90 days", status: "upcoming" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() { const l = this.weeks.filter(w => w.status === "live"); return l.length ? l[l.length - 1] : null; },
    get phaseCount() { return this.weeks.filter(w => w.phase).length; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};

function renderTrack6Curriculum()  { return learnCurriculumHTML(TRACK6); }
function renderTrack6Sidebar(w)    { return sidebarHTML(TRACK6, w); }
function renderTrack6Progress()    { return { text: `${TRACK6.liveCount} of ${TRACK6.totalWeeks} published`, percent: TRACK6.progressPercent }; }

function renderLifecycleCurriculum() { return learnCurriculumHTML(LIFECYCLE); }
function renderLifecycleSidebar(w)   { return sidebarHTML(LIFECYCLE, w); }
function renderLifecycleProgress()   { return { text: `${LIFECYCLE.liveCount} of ${LIFECYCLE.totalWeeks} published`, percent: LIFECYCLE.progressPercent }; }
'''

# ==========================================================================
# learn.html — the two sections
# ==========================================================================

SECTIONS = '''                    <!-- ===== SECTION: THE INTEGRATION LAYER ===== -->
                    <div class="layer-intro">
                        <div class="track-badge roadmap"><i class='bx bx-layer'></i> THE INTEGRATION LAYER</div>
                        <h2>Two tracks follow, and neither repeats the five above</h2>
                        <p>Tracks 1&#8211;5 teach the methods. <strong>Interfaces</strong> shows how those methods change shape under a different contract and a different organisation. <strong>The Life of a Project</strong> shows the order the work actually arrives in, what feeds what, and which record is born where. Three layers, and each one needs the other two.</p>
                    </div>

<!-- ===== TRACK 6 — INTERFACES ===== -->
                    <div class="track-header" id="track-6">
                        <div class="track-badge free" id="t6TrackBadge"><i class='bx bx-git-branch'></i> TRACK 6 &#183; FREE</div>
                        <h2>Interfaces</h2>
                        <p class="track-sub">Where the work and the numbers change hands.</p>
                        <p class="track-desc">Five tracks taught one job: a single contract, a single chain of command, a single team on a single site. Every technique in all of them quietly assumes that shape. This track is what happens when it stops holding &#8212; when the scope sits with somebody else, when the critical path runs through a purchase order, when the work nobody planned appears where two programmes meet, and when the number has more than one owner. Nothing here replaces what came before. It marks the edges of it.</p>
                        <div class="track-outcomes">
                            <h3>After this track you can</h3>
                            <ul>
                            <li>Say how many contracts a project has, and why that decides more than the payment mechanism</li>
                            <li>Explain why an EPCM manager instructs people it has no contract with, and what that costs</li>
                            <li>Argue concurrency when there is no head contract holding the definition</li>
                            <li>Find the work sitting between two programmes before it becomes somebody&#39;s claim</li>
                            <li>Reconcile a progress-based number with a valuation-based one without producing two truths</li>
                            <li>Recognise which of the five tracks stops applying, and say precisely where</li>
                            </ul>
                        </div>
                        <div class="track-note">
                            <i class='bx bx-lock-open-alt'></i>
                            <p><strong>The handoff was printed five tracks ago.</strong> <a href="claim-week-28.html">Claims Week 28</a> closed by naming four things this track answers. It opens by naming the assumption all five tracks were built on, and then takes it apart one contract at a time.</p>
                        </div>
                    </div>

                    <!-- MODULE 06: INTERFACES -->
                    <div class="module-card">
                        <div class="module-card-header">
                            <div class="module-card-left">
                                <span class="module-num">06</span>
                                <div class="module-info">
                                    <h2>Interfaces</h2>
                                    <p>Delivery models and who holds the scope, EPCM authority without privity, joint ventures, the critical path through an order, the work between two programmes, and the number with two owners.</p>
                                </div>
                            </div>
                            <span class="module-badge badge-locked" id="t6ModuleBadge"><i class='bx bx-time'></i> Starting soon &#183; 14 weeks</span>
                        </div>
                        <div class="module-tools">
                            <span class="tool-tag-label">Topics:</span>
                            <span class="tool-tag">Delivery Models</span>
                            <span class="tool-tag">EPCM</span>
                            <span class="tool-tag">Joint Ventures</span>
                            <span class="tool-tag">Concurrency</span>
                            <span class="tool-tag">Interfaces</span>
                            <span class="tool-tag">Long Lead</span>
                            <span class="tool-tag">Document Control</span>
                        </div>
                        <div class="module-weeks" id="track6Weeks"></div>
                        <div class="module-progress">
                            <div class="progress-label">
                                <span id="t6ProgressText">0 of 14 published</span>
                                <span id="t6ProgressPct">0%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" id="t6ProgressFill" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

<!-- ===== THE LIFE OF A PROJECT ===== -->
                    <div class="track-header" id="lifecycle">
                        <div class="track-badge free" id="lcTrackBadge"><i class='bx bx-git-repo-forked'></i> THE LIFE OF A PROJECT &#183; FREE</div>
                        <h2>The Life of a Project</h2>
                        <p class="track-sub">From the investment decision to the handover certificate &#8212; and what project controls does at every step.</p>
                        <p class="track-desc">Everything above answers how. This answers when, why and with whom. It follows one EPC job in the order it actually arrives &#8212; the decision made before you were hired, the tender you inherit, the kick-off, the baseline nobody has time for, the six weeks that run the site, the month the curve stops behaving, the punch list, and the archive you hand to whoever starts on Monday. It teaches no new technique. It shows where the ones you have get used, and hands the method back to the track that owns it every time.</p>
                        <div class="track-outcomes">
                            <h3>After this you can</h3>
                            <ul>
                            <li>Say what happens on a project in what order, and what each stage needs from you</li>
                            <li>Name every input behind a monthly report, its owner, its unit and its cut-off</li>
                            <li>Run a constraint register and a look-ahead that a foreman will actually use</li>
                            <li>Know which record is born at which stage, and which of them anyone reads</li>
                            <li>Walk into a project on day one and say what you would set up first, and why</li>
                            <li>Place every technique in Tracks 1&#8211;5 against the moment in the week it is needed</li>
                            </ul>
                        </div>
                        <div class="track-note">
                            <i class='bx bx-bulb'></i>
                            <p><strong>Records born here.</strong> Every week ends the same way &#8212; naming the documents that come into existence at that stage, from the clarification log at tender to the lessons learned register at closeout. Learn the job and you learn the paperwork with it, in the order it appears rather than as a list.</p>
                        </div>
                    </div>

                    <!-- MODULE 07: THE LIFE OF A PROJECT -->
                    <div class="module-card">
                        <div class="module-card-header">
                            <div class="module-card-left">
                                <span class="module-num">07</span>
                                <div class="module-info">
                                    <h2>The Life of a Project</h2>
                                    <p>Nine phases from the investment decision to closeout, plus a two-week capstone. The integration layer: the order, the handovers, and the records.</p>
                                </div>
                            </div>
                            <span class="module-badge badge-locked" id="lcModuleBadge"><i class='bx bx-time'></i> On the roadmap &#183; 52 weeks</span>
                        </div>
                        <div class="module-tools">
                            <span class="tool-tag-label">Topics:</span>
                            <span class="tool-tag">Lifecycle</span>
                            <span class="tool-tag">Start-up</span>
                            <span class="tool-tag">Engineering</span>
                            <span class="tool-tag">Procurement</span>
                            <span class="tool-tag">Workfront</span>
                            <span class="tool-tag">Look-ahead</span>
                            <span class="tool-tag">Governance</span>
                            <span class="tool-tag">Commissioning</span>
                            <span class="tool-tag">Registers</span>
                        </div>
                        <div class="module-weeks" id="lifecycleWeeks"></div>
                        <div class="module-progress">
                            <div class="progress-label">
                                <span id="lcProgressText">0 of 52 published</span>
                                <span id="lcProgressPct">0%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" id="lcProgressFill" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

                    <div class="roadmap-section" id="roadmap">
                    <div class="roadmap-intro">
                        <div class="track-badge roadmap"><i class='bx bx-map-alt'></i> THE ROADMAP</div>
                        <h2>After the writing</h2>
                        <p>The text comes first. The tools come after it, because a tool you can drive but not reason about is worth nothing on a site.</p>
                    </div>

                    <div class="roadmap-card">
                        <span class="roadmap-marker"><i class='bx bx-joystick'></i></span>
                        <div class="roadmap-body">
                            <h3>The Simulation</h3>
                            <p>One EPC project, run end to end as a sequence of episodes with a real document pack. The same job as The Life of a Project, played rather than read.</p>
                        </div>
                        <span class="roadmap-badge"><i class='bx bx-time'></i> On the roadmap</span>
                    </div>
                </div>

'''

LAYER_CSS = '''
        .layer-intro {
            padding: 28px 0 4px;
            margin-top: 20px;
            border-top: 1px solid #e2e8f0;
        }
        .layer-intro h2 {
            margin: 14px 0 10px;
            font-size: 22px; font-weight: 800; color: #1e293b; letter-spacing: -0.01em;
        }
        .layer-intro p {
            margin: 0; max-width: 760px;
            font-size: 15px; color: #64748b; line-height: 1.7;
        }
        .layer-intro strong { color: #334155; font-weight: 700; }
        @media (max-width: 640px) {
            .layer-intro h2 { font-size: 19px; }
            .layer-intro p { font-size: 14px; }
        }
    </style>'''

WIRING = '''
            // Track 6 — Interfaces
            const t6El = document.getElementById('track6Weeks');
            if (t6El && typeof renderTrack6Curriculum === 'function') {
                t6El.innerHTML = renderTrack6Curriculum();
                const p6 = renderTrack6Progress();
                const s = function (id, v) { const e = document.getElementById(id); if (e) e.textContent = v; };
                s('t6ProgressText', p6.text); s('t6ProgressPct', p6.percent + '%');
                const f6 = document.getElementById('t6ProgressFill'); if (f6) f6.style.width = p6.percent + '%';
            }
            // The Life of a Project
            const lcEl = document.getElementById('lifecycleWeeks');
            if (lcEl && typeof renderLifecycleCurriculum === 'function') {
                lcEl.innerHTML = renderLifecycleCurriculum();
                const plc = renderLifecycleProgress();
                const s2 = function (id, v) { const e = document.getElementById(id); if (e) e.textContent = v; };
                s2('lcProgressText', plc.text); s2('lcProgressPct', plc.percent + '%');
                const flc = document.getElementById('lcProgressFill'); if (flc) flc.style.width = plc.percent + '%';
            }
            // Badges and header status words computed, never typed
            [['t6ModuleBadge', 't6TrackBadge', typeof TRACK6 !== 'undefined' ? TRACK6 : null, "<i class='bx bx-git-branch'></i> TRACK 6 \\u00b7 FREE"],
             ['lcModuleBadge', 'lcTrackBadge', typeof LIFECYCLE !== 'undefined' ? LIFECYCLE : null, "<i class='bx bx-git-repo-forked'></i> THE LIFE OF A PROJECT \\u00b7 FREE"]]
            .forEach(function (p) {
                const t = p[2]; if (!t) return;
                const mb = document.getElementById(p[0]);
                if (mb && typeof badgeText === 'function') {
                    mb.innerHTML = badgeText(t);
                    mb.className = 'module-badge ' + badgeClass(t);
                }
                const hb = document.getElementById(p[1]);
                if (hb) {
                    const word = t.liveCount >= t.totalWeeks ? ' \\u00b7 COMPLETE'
                               : t.liveCount === 0 ? ' \\u00b7 IN PREPARATION'
                               : ' \\u00b7 WEEK ' + t.latestLiveWeek.n;
                    hb.innerHTML = p[3] + word;
                }
            });
'''

JUMP_NAV = '''                <nav class="track-jump" aria-label="Jump to a section">
                    <a href="start-here.html" class="track-jump-link">Start Here</a>
                    <a href="#track-1" class="track-jump-link" data-jump="track-1">Schedule <span id="jn1">27</span></a>
                    <a href="#track-2" class="track-jump-link" data-jump="track-2">Cost &amp; Cash <span id="jn2">24</span></a>
                    <a href="#track-3" class="track-jump-link" data-jump="track-3">Risk <span id="jn3">18</span></a>
                    <a href="#track-4" class="track-jump-link" data-jump="track-4">Contract <span id="jn4">20</span></a>
                    <a href="#track-5" class="track-jump-link" data-jump="track-5">Claims <span id="jn5">28</span></a>
                    <a href="#track-6" class="track-jump-link" data-jump="track-6">Interfaces <span id="jn6">14</span></a>
                    <a href="#lifecycle" class="track-jump-link" data-jump="lifecycle">Life of a Project <span id="jnlc">52</span></a>
                    <a href="#roadmap" class="track-jump-link" data-jump="roadmap">Roadmap</a>
                    <a href="#toolbox" class="track-jump-link" data-jump="toolbox">Toolbox</a>
                </nav>'''

JUMP_WIRING = '''
            [['jn1', CURRICULUM],
             ['jn2', typeof TRACK2 !== 'undefined' ? TRACK2 : null],
             ['jn3', typeof TRACK3 !== 'undefined' ? TRACK3 : null],
             ['jn4', typeof TRACK4 !== 'undefined' ? TRACK4 : null],
             ['jn5', typeof TRACK5 !== 'undefined' ? TRACK5 : null],
             ['jn6', typeof TRACK6 !== 'undefined' ? TRACK6 : null],
             ['jnlc', typeof LIFECYCLE !== 'undefined' ? LIFECYCLE : null]].forEach(function (p) {
                var el = document.getElementById(p[0]);
                if (el && p[1]) el.textContent = p[1].totalWeeks;
            });
'''


def cut(src, start_marker, end_marker, label):
    """Remove the block between two markers, inclusive of start, exclusive of end."""
    if start_marker not in src:
        return src, False
    i = src.index(start_marker)
    j = src.index(end_marker, i)
    return src[:i] + src[j:], True


def main():
    written = 0

    # ---- curriculum.js -------------------------------------------------
    cj = ROOT / "curriculum.js"
    src = cj.read_text(encoding="utf-8")
    if "const TRACK6 =" in src:
        print("  = curriculum.js: zaten uygulanmis")
    else:
        anchor = "\n// ===================== TRACK 5 — CLAIMS & DELAY ANALYSIS ====================="
        if anchor not in src:
            sys.exit("HATA: curriculum.js icinde TRACK 5 basligi bulunamadi")
        src = src.replace(anchor, TRACK6_JS + anchor, 1)
        cj.write_text(src, encoding="utf-8")
        print("  + curriculum.js: TRACK6 + LIFECYCLE yazildi")
        written += 1

    # ---- learn.html ----------------------------------------------------
    lh = ROOT / "learn.html"
    s = lh.read_text(encoding="utf-8")
    before = s

    # a. retire Track 0 from the page
    s, did = cut(s, "                <!-- ===== SECTION: ORIENTATION ===== -->",
                 "                <!-- ===== TRACK 1 ===== -->", "Track 0 section")
    if did:
        print("  - learn.html: Track 0 bolumu kaldirildi")
    s, did = cut(s, "\n            // Track 0 — The Shape of the Job",
                 "\n            // Fill weeks", "Track 0 wiring")

    # b. replace the roadmap teaser with the two real sections
    if 'id="track-6"' not in s:
        i = s.index('                    <div class="roadmap-section" id="roadmap">')
        j = s.index("                <!-- ===== SECTION: THE TOOLBOX ===== -->")
        s = s[:i] + SECTIONS + s[j:]
        print("  + learn.html: Track 6 + The Life of a Project eklendi")

    # c. jump nav
    a = s.index('                <nav class="track-jump"')
    b = s.index("</nav>", a) + len("</nav>")
    s = s[:a] + JUMP_NAV + s[b:]

    # d. scroll offsets
    s = re.sub(r"#track-0, #track-1(.*?)\{ scroll-margin-top: 132px; \}",
               r"#track-1, #track-2, #track-3, #track-4, #track-5, #track-6, #lifecycle, #roadmap, #toolbox { scroll-margin-top: 132px; }",
               s, count=1)

    # e. css + wiring
    if ".layer-intro" not in s:
        s = s.replace("    </style>", LAYER_CSS, 1)
    if "// Track 6 \u2014 Interfaces" not in s:
        s = s.replace("            // Fill weeks", WIRING + "\n            // Fill weeks", 1)
    s = re.sub(r"\n            \[\['jn0'.*?\}\);\n", JUMP_WIRING, s, count=1, flags=re.S)

    # f. header meta
    s = re.sub(r"<i class='bx bx-layer'></i> \d+ tracks \+ a toolbox",
               "<i class='bx bx-layer'></i> 7 tracks + a toolbox", s)
    s = re.sub(r"Tracks 1&#8211;5 complete &#183; 117 lessons &#183; Track 0 in preparation",
               "Tracks 1&#8211;5 complete &#183; 117 lessons &#183; Interfaces next", s)

    if s != before:
        lh.write_text(s, encoding="utf-8")
        written += 1
    else:
        print("  = learn.html: degisiklik yok")

    # ---- start-here.html: Track 0 links ---------------------------------
    sh = ROOT / "start-here.html"
    if sh.exists():
        t = sh.read_text(encoding="utf-8")
        orig = t
        t = t.replace(
            '<p class="track-desc">Track 0 describes the shape of a construction job end to end, so the methods later have somewhere to sit. It is the natural place to start, but it is not a prerequisite. If you already work on a project you can go straight to Track 1 and come back when a term stops making sense.</p>',
            '<p class="track-desc">Track 1 is where to start. It is the foundation the other four stand on, and it assumes no software and no prior planning experience. If a term is unfamiliar, it gets defined the week it is first needed.</p>')
        t = t.replace('<li><a href="learn.html#track-0">Track 0 — The Shape of the Job</a>, if you want the map before the methods</li>\n                        ', '')
        t = t.replace('<li><a href="learn.html#track-1">Track 1 — Schedule Management</a>, if you are already on a project and want to begin</li>',
                      '<li><a href="learn.html#track-1">Track 1 — Schedule Management</a>, if you want to begin at the beginning</li>')
        if t != orig:
            sh.write_text(t, encoding="utf-8")
            print("  ~ start-here.html: Track 0 atiflari temizlendi")
            written += 1

    print(f"\n{written} dosya")


if __name__ == "__main__":
    main()
