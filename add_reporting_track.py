#!/usr/bin/env python3
"""Reporting becomes Track 6. Interfaces moves to Track 7. The lifecycle
module drops from 52 weeks to 36.

Sixteen lifecycle weeks were about where a number comes from and what you
issue, which is the whole of Reporting. Keeping them in both places would
teach the same material twice, so they move and the module keeps only the
weeks about doing the work:

  moved  14 rules of credit        -> Reporting 08
         15 the calendar           -> Reporting 16
         16 reporting structure    -> Reporting 17-19
         19 submittals and IFC     -> Reporting 03
         20 engineering progress   -> Reporting 04
         22 vendor documents       -> Reporting 05
         24 material management    -> Reporting 06
         31 daily progress         -> Reporting 08
         32 productivity           -> Reporting 10
         33 equipment and resources-> Reporting 10
         34 quality as subtraction -> Reporting 11
         35 safety as a stoppage   -> Reporting 12
         36 monthly valuation      -> Reporting 19, 25
         39 trends and change log  -> Reporting 24
         43 KPIs                   -> Reporting 22
         44 the register system    -> Reporting 24

Separating rule: Reporting owns the exchange, the lifecycle module owns doing
the work. Week 28 keeps constraint removal and loses the six readiness tests
to Reporting 09 for the same reason.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ==========================================================================
# curriculum.js
# ==========================================================================

NEW_JS = '''
// ===================== TRACK 6 — REPORTING =====================
// The trade around the methods. Phase A follows every input back to the
// department that produces it; Phase B follows every document forward to the
// person meant to act on it. Every week ends with the same four lines:
// what arrives, from whom and in what unit, what you issue, who uses it.
// Source position measured 2026-07-31: this is the thinnest-sourced track on
// the site. monthly report 0, data date 0, interface register 0, action item
// 0, constraint log 0, work permit 0, dashboard 2, reconciliation 2. Write it
// as industry practice, give units and flows, give no figures.
const TRACK6 = {
    title: "Reporting",
    totalWeeks: 26,
    weeks: [
        { phase: "Phase A \\u2014 What feeds you", n: 1, title: "What project controls produces, and what it must be fed", short: "What it produces, what it needs", status: "upcoming" },
        { n: 2, title: "Working backwards from a deliverable \\u2014 output, inputs, owners, units", short: "Working backwards", status: "upcoming" },
        { n: 3, title: "Engineering feeds you \\u2014 deliverables, IFC, and approved with comments", short: "Engineering feeds you", status: "upcoming" },
        { n: 4, title: "Engineering progress \\u2014 where percent complete is easiest to fake", short: "Engineering progress", status: "upcoming" },
        { n: 5, title: "Procurement feeds you \\u2014 PO status, expediting, shipping, vendor data", short: "Procurement feeds you", status: "upcoming" },
        { n: 6, title: "Material at site \\u2014 delivered, stored, issued, installed", short: "Material at site", status: "upcoming" },
        { n: 7, title: "Construction: quantities \\u2014 three numbers for the same wall", short: "Construction: quantities", status: "upcoming" },
        { n: 8, title: "Construction: progress \\u2014 who measures, in what unit, on which day", short: "Construction: progress", status: "upcoming" },
        { n: 9, title: "Workfront and the six readiness tests \\u2014 drawing, material, access, permit, labour, plant", short: "Workfront and readiness", status: "upcoming" },
        { n: 10, title: "Construction: hours and plant \\u2014 allocation, availability, utilisation, idle time", short: "Hours and plant", status: "upcoming" },
        { n: 11, title: "QA/QC feeds you \\u2014 NCRs, inspection requests, and progress that reverses", short: "QA/QC feeds you", status: "upcoming" },
        { n: 12, title: "HSE feeds you \\u2014 permits, holds, stand-downs and lost time as delay events", short: "HSE feeds you", status: "upcoming" },
        { n: 13, title: "Document control feeds you \\u2014 revision status, and why half the site builds to Rev B", short: "Document control feeds you", status: "upcoming" },
        { n: 14, title: "Commercial feeds you \\u2014 commitments, accruals and invoices on somebody else\\u2019s cut-off", short: "Commercial feeds you", status: "upcoming" },
        { n: 15, title: "The client feeds you \\u2014 instructions, approvals, comments: time rather than data", short: "The client feeds you", status: "upcoming" },

        { phase: "Phase B \\u2014 What you issue", n: 16, title: "The calendar \\u2014 data date, cut-off, and three departments closing on three days", short: "The calendar", status: "upcoming" },
        { n: 17, title: "The daily report \\u2014 the shortest document with the most consequences", short: "The daily report", status: "upcoming" },
        { n: 18, title: "The weekly report and the look-ahead \\u2014 and the only part anyone acts on", short: "Weekly report and look-ahead", status: "upcoming" },
        { n: 19, title: "The monthly report \\u2014 curve, variance, narrative, and the summary read first", short: "The monthly report", status: "upcoming" },
        { n: 20, title: "Four audiences, four altitudes \\u2014 one number told four ways, not four stories", short: "Four audiences, four altitudes", status: "upcoming" },
        { n: 21, title: "Dashboards \\u2014 who reads what, and what a dashboard cannot say", short: "Dashboards", status: "upcoming" },
        { n: 22, title: "KPIs, leading and lagging \\u2014 last month against next month", short: "KPIs, leading and lagging", status: "upcoming" },
        { n: 23, title: "Minutes, actions and closure \\u2014 and the recovery action list under pressure", short: "Minutes, actions and closure", status: "upcoming" },
        { n: 24, title: "The register system \\u2014 assumption, risk, change; interface, constraint, delay", short: "The register system", status: "upcoming" },
        { n: 25, title: "When two reports disagree \\u2014 progress against valuation, reconciled first", short: "When two reports disagree", status: "upcoming" },
        { n: 26, title: "The report nobody acts on \\u2014 the most common failure, and what to change", short: "The report nobody acts on", status: "upcoming" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() { const l = this.weeks.filter(w => w.status === "live"); return l.length ? l[l.length - 1] : null; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};

// ===================== TRACK 7 — INTERFACES =====================
// The printed handoff in claim-week-28 names four subjects: the scope sitting
// with somebody else, the critical path through a purchase order, the work
// where two programmes meet, and the number with more than one owner.
const TRACK7 = {
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
// The order the work arrives in. Everything about where a number comes from
// moved to Reporting; what is left is the job itself. Rule for every week:
// teach the occasion, hand the method to the track that owns it. Every week
// ends with "Records born here".
const LIFECYCLE = {
    title: "The Life of a Project",
    totalWeeks: 36,
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
        { n: 13, title: "Building the baseline \\u2014 the two weeks, not the method", short: "Building the baseline", status: "upcoming" },
        { n: 14, title: "The meeting structure \\u2014 who chairs, who decides, and which ones move blame", short: "The meeting structure", status: "upcoming" },

        { phase: "Phase C \\u2014 Engineering and procurement", n: 15, title: "How engineering flows \\u2014 deliverable lists, disciplines, and the design freeze", short: "How engineering flows", status: "upcoming" },
        { n: 16, title: "The procurement cycle \\u2014 requisition to purchase order", short: "The procurement cycle", status: "upcoming" },
        { n: 17, title: "Long lead \\u2014 ordering before the design is finished, and the cost of being wrong", short: "Long lead", status: "upcoming" },

        { phase: "Phase D \\u2014 Construction", n: 18, title: "Mobilisation \\u2014 the project inside the project", short: "Mobilisation", status: "upcoming" },
        { n: 19, title: "Site logistics and temporary works \\u2014 access, laydown, cranes, and a scaffold with its own lead time", short: "Site logistics and temporary works", status: "upcoming" },
        { n: 20, title: "Work packaging \\u2014 dividing scope into something a crew can be handed", short: "Work packaging", status: "upcoming" },
        { n: 21, title: "Clearing the workfront \\u2014 constraint removal, and who removes each kind", short: "Clearing the workfront", status: "upcoming" },
        { n: 22, title: "Look-ahead planning \\u2014 the six weeks that run the site", short: "Look-ahead planning", status: "upcoming" },
        { n: 23, title: "The week, day by day \\u2014 one workable rhythm, not the rhythm", short: "The week, day by day", status: "upcoming" },

        { phase: "Phase E \\u2014 Commercial", n: 24, title: "Change on the ground \\u2014 instruction to variation to claim, as it happens", short: "Change on the ground", status: "upcoming" },
        { n: 25, title: "Forecasting \\u2014 the number you will be judged on", short: "Forecasting", status: "upcoming" },

        { phase: "Phase F \\u2014 Governance", n: 26, title: "Who approves what \\u2014 authority, delegation, and the escalation chain", short: "Who approves what", status: "upcoming" },
        { n: 27, title: "The change control board", short: "The change control board", status: "upcoming" },
        { n: 28, title: "Risk reviews that change something", short: "Risk reviews that change something", status: "upcoming" },

        { phase: "Phase G \\u2014 Finishing", n: 29, title: "Mechanical completion \\u2014 and the birth of the punch list", short: "Mechanical completion", status: "upcoming" },
        { n: 30, title: "Pre-commissioning and commissioning \\u2014 handing the schedule to another discipline", short: "Pre-commissioning and commissioning", status: "upcoming" },
        { n: 31, title: "Performance tests", short: "Performance tests", status: "upcoming" },
        { n: 32, title: "Closing the punch list and taking over", short: "Closing the punch list", status: "upcoming" },
        { n: 33, title: "Demobilisation \\u2014 the crane, the camp and the punch list want the same people", short: "Demobilisation", status: "upcoming" },
        { n: 34, title: "Closeout \\u2014 as-built, final account, archive", short: "Closeout", status: "upcoming" },

        { phase: "Capstone", n: 35, title: "Designing a project controls system from nothing", short: "Designing the system from nothing", status: "upcoming" },
        { n: 36, title: "The first 90 days \\u2014 a contract, a BoQ, a drawing set and an empty schedule", short: "The first 90 days", status: "upcoming" }
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

function renderTrack7Curriculum()  { return learnCurriculumHTML(TRACK7); }
function renderTrack7Sidebar(w)    { return sidebarHTML(TRACK7, w); }
function renderTrack7Progress()    { return { text: `${TRACK7.liveCount} of ${TRACK7.totalWeeks} published`, percent: TRACK7.progressPercent }; }

function renderLifecycleCurriculum() { return learnCurriculumHTML(LIFECYCLE); }
function renderLifecycleSidebar(w)   { return sidebarHTML(LIFECYCLE, w); }
function renderLifecycleProgress()   { return { text: `${LIFECYCLE.liveCount} of ${LIFECYCLE.totalWeeks} published`, percent: LIFECYCLE.progressPercent }; }
'''

# ==========================================================================
# learn.html sections
# ==========================================================================

SECTIONS = '''<!-- ===== TRACK 6 — REPORTING ===== -->
                    <div class="track-header" id="track-6">
                        <div class="track-badge free" id="t6TrackBadge"><i class='bx bx-line-chart'></i> TRACK 6 &#183; FREE</div>
                        <h2>Reporting</h2>
                        <p class="track-sub">Everything that arrives, everything you issue, and what to do when two of them disagree.</p>
                        <p class="track-desc">Five tracks taught what to do with a number once you have it. None of them said where it came from, who owns it, when it closes, or who reads it afterwards. This track follows every input project controls consumes back to the department that produces it, then follows every document you issue forward to the person who is supposed to act on it. It teaches no new technique. It is the trade around them.</p>
                        <div class="track-outcomes">
                            <h3>After this track you can</h3>
                            <ul>
                            <li>Name every input behind a monthly report, its owner, its unit and its cut-off date</li>
                            <li>Work backwards from any deliverable to the data it needs and who holds it</li>
                            <li>Say what &quot;ready&quot; means in six specific tests, and refuse the word until they are met</li>
                            <li>Tell whether the drawing the site is building to is the current revision</li>
                            <li>Write a daily, weekly and monthly report that four different readers can each act on</li>
                            <li>Reconcile a progress number with a valuation number before either one leaves the office</li>
                            </ul>
                        </div>
                        <div class="track-note">
                            <i class='bx bx-bulb'></i>
                            <p><strong>Every week ends the same way.</strong> What arrives &#8212; from whom, in what unit, on which day. What you issue. Who uses it. And the records born there. Learn the trade and you learn the paperwork with it, in the order it actually reaches your desk.</p>
                        </div>
                    </div>

                    <!-- MODULE 06: REPORTING -->
                    <div class="module-card">
                        <div class="module-card-header">
                            <div class="module-card-left">
                                <span class="module-num">06</span>
                                <div class="module-info">
                                    <h2>Reporting</h2>
                                    <p>Fifteen weeks on what each department feeds you and in what unit, then eleven on what you issue back &#8212; daily to executive, dashboards, KPIs, registers, and the report nobody acts on.</p>
                                </div>
                            </div>
                            <span class="module-badge badge-locked" id="t6ModuleBadge"><i class='bx bx-time'></i> Starting soon &#183; 26 weeks</span>
                        </div>
                        <div class="module-tools">
                            <span class="tool-tag-label">Topics:</span>
                            <span class="tool-tag">Data Sources</span>
                            <span class="tool-tag">Readiness</span>
                            <span class="tool-tag">Revision Status</span>
                            <span class="tool-tag">Cut-off</span>
                            <span class="tool-tag">Daily / Weekly / Monthly</span>
                            <span class="tool-tag">Dashboards</span>
                            <span class="tool-tag">KPIs</span>
                            <span class="tool-tag">Registers</span>
                        </div>
                        <div class="module-weeks" id="track6Weeks"></div>
                        <div class="module-progress">
                            <div class="progress-label">
                                <span id="t6ProgressText">0 of 26 published</span>
                                <span id="t6ProgressPct">0%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" id="t6ProgressFill" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

<!-- ===== TRACK 7 — INTERFACES ===== -->
                    <div class="track-header" id="track-7">
                        <div class="track-badge free" id="t7TrackBadge"><i class='bx bx-git-branch'></i> TRACK 7 &#183; FREE</div>
                        <h2>Interfaces</h2>
                        <p class="track-sub">Where the work and the numbers change hands.</p>
                        <p class="track-desc">Six tracks taught one job: a single contract, a single chain of command, a single team on a single site. Every technique in all of them quietly assumes that shape. This track is what happens when it stops holding &#8212; when the scope sits with somebody else, when the critical path runs through a purchase order, when the work nobody planned appears where two programmes meet, and when the number has more than one owner.</p>
                        <div class="track-outcomes">
                            <h3>After this track you can</h3>
                            <ul>
                            <li>Say how many contracts a project has, and why that decides more than the payment mechanism</li>
                            <li>Explain why an EPCM manager instructs people it has no contract with, and what that costs</li>
                            <li>Argue concurrency when there is no head contract holding the definition</li>
                            <li>Find the work sitting between two programmes before it becomes somebody&#39;s claim</li>
                            <li>Reconcile a number that two organisations both produce and neither owns</li>
                            <li>Recognise which of the earlier tracks stops applying, and say precisely where</li>
                            </ul>
                        </div>
                        <div class="track-note">
                            <i class='bx bx-lock-open-alt'></i>
                            <p><strong>The handoff was printed five tracks ago.</strong> <a href="claim-week-28.html">Claims Week 28</a> closed by naming four things this track answers. It opens by naming the assumption every track before it was built on, and then takes it apart one contract at a time.</p>
                        </div>
                    </div>

                    <!-- MODULE 07: INTERFACES -->
                    <div class="module-card">
                        <div class="module-card-header">
                            <div class="module-card-left">
                                <span class="module-num">07</span>
                                <div class="module-info">
                                    <h2>Interfaces</h2>
                                    <p>Delivery models and who holds the scope, EPCM authority without privity, joint ventures, the critical path through an order, the work between two programmes, and the number with two owners.</p>
                                </div>
                            </div>
                            <span class="module-badge badge-locked" id="t7ModuleBadge"><i class='bx bx-time'></i> On the roadmap &#183; 14 weeks</span>
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
                        <div class="module-weeks" id="track7Weeks"></div>
                        <div class="module-progress">
                            <div class="progress-label">
                                <span id="t7ProgressText">0 of 14 published</span>
                                <span id="t7ProgressPct">0%</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" id="t7ProgressFill" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>

'''

WIRING = '''
            // Tracks 6 and 7, and the lifecycle module
            [['track6Weeks', 'renderTrack6Curriculum', 'renderTrack6Progress', 't6ProgressText', 't6ProgressPct', 't6ProgressFill'],
             ['track7Weeks', 'renderTrack7Curriculum', 'renderTrack7Progress', 't7ProgressText', 't7ProgressPct', 't7ProgressFill'],
             ['lifecycleWeeks', 'renderLifecycleCurriculum', 'renderLifecycleProgress', 'lcProgressText', 'lcProgressPct', 'lcProgressFill']]
            .forEach(function (c) {
                var el = document.getElementById(c[0]);
                if (!el || typeof window[c[1]] !== 'function') return;
                el.innerHTML = window[c[1]]();
                var p = window[c[2]]();
                var t = document.getElementById(c[3]); if (t) t.textContent = p.text;
                var q = document.getElementById(c[4]); if (q) q.textContent = p.percent + '%';
                var f = document.getElementById(c[5]); if (f) f.style.width = p.percent + '%';
            });
            [['t6ModuleBadge', 't6TrackBadge', typeof TRACK6 !== 'undefined' ? TRACK6 : null, "<i class='bx bx-line-chart'></i> TRACK 6 \\u00b7 FREE"],
             ['t7ModuleBadge', 't7TrackBadge', typeof TRACK7 !== 'undefined' ? TRACK7 : null, "<i class='bx bx-git-branch'></i> TRACK 7 \\u00b7 FREE"],
             ['lcModuleBadge', 'lcTrackBadge', typeof LIFECYCLE !== 'undefined' ? LIFECYCLE : null, "<i class='bx bx-git-repo-forked'></i> THE LIFE OF A PROJECT \\u00b7 FREE"]]
            .forEach(function (p) {
                var t = p[2]; if (!t) return;
                var mb = document.getElementById(p[0]);
                if (mb && typeof badgeText === 'function') {
                    mb.innerHTML = badgeText(t);
                    mb.className = 'module-badge ' + badgeClass(t);
                }
                var hb = document.getElementById(p[1]);
                if (hb) {
                    hb.innerHTML = p[3] + (t.liveCount >= t.totalWeeks ? ' \\u00b7 COMPLETE'
                                 : t.liveCount === 0 ? ' \\u00b7 IN PREPARATION'
                                 : ' \\u00b7 WEEK ' + t.latestLiveWeek.n);
                }
            });
'''

JUMP_NAV = '''                <nav class="track-jump" aria-label="Jump to a section">
                    <a href="#track-1" class="track-jump-link" data-jump="track-1">Schedule <span id="jn1">27</span></a>
                    <a href="#track-2" class="track-jump-link" data-jump="track-2">Cost <span id="jn2">24</span></a>
                    <a href="#track-3" class="track-jump-link" data-jump="track-3">Risk <span id="jn3">18</span></a>
                    <a href="#track-4" class="track-jump-link" data-jump="track-4">Contract <span id="jn4">20</span></a>
                    <a href="#track-5" class="track-jump-link" data-jump="track-5">Claims <span id="jn5">28</span></a>
                    <a href="#track-6" class="track-jump-link" data-jump="track-6">Reporting <span id="jn6">26</span></a>
                    <a href="#track-7" class="track-jump-link" data-jump="track-7">Interfaces <span id="jn7">14</span></a>
                    <a href="#lifecycle" class="track-jump-link" data-jump="lifecycle">Lifecycle <span id="jnlc">36</span></a>
                </nav>'''

JUMP_WIRING = '''
            [['jn1', CURRICULUM], ['jn2', typeof TRACK2 !== 'undefined' ? TRACK2 : null],
             ['jn3', typeof TRACK3 !== 'undefined' ? TRACK3 : null],
             ['jn4', typeof TRACK4 !== 'undefined' ? TRACK4 : null],
             ['jn5', typeof TRACK5 !== 'undefined' ? TRACK5 : null],
             ['jn6', typeof TRACK6 !== 'undefined' ? TRACK6 : null],
             ['jn7', typeof TRACK7 !== 'undefined' ? TRACK7 : null],
             ['jnlc', typeof LIFECYCLE !== 'undefined' ? LIFECYCLE : null]].forEach(function (p) {
                var el = document.getElementById(p[0]);
                if (el && p[1]) el.textContent = p[1].totalWeeks;
            });
'''

FIGURE = '''            <ol class="path-figure is-five" aria-label="How the curriculum builds">
                <li class="path-step is-done">
                    <span class="path-dot"><i class='bx bx-check'></i></span>
                    <span class="path-kicker">Tracks 1&#8211;5 &#183; <b id="pfDone">117</b> lessons</span>
                    <strong class="path-title"><a href="#track-1">The methods</a></strong>
                    <span class="path-out">Build a programme, price it, keep the right when it slips, prove the delay.</span>
                    <span class="path-chain">
                        <a class="chain-box" href="#track-1">Schedule <b id="cb1">27</b></a>
                        <a class="chain-box" href="#track-2">Cost &amp; Cash <b id="cb2">24</b></a>
                        <a class="chain-box" href="#track-3">Risk <b id="cb3">18</b></a>
                        <a class="chain-box" href="#track-4">Contract <b id="cb4">20</b></a>
                        <a class="chain-box" href="#track-5">Claims <b id="cb5">28</b></a>
                    </span>
                </li>
                <li class="path-step is-next">
                    <span class="path-dot"></span>
                    <span class="path-kicker">Track 6 &#183; <b id="pfT6">26</b> weeks &#183; next</span>
                    <strong class="path-title"><a href="#track-6">Reporting</a></strong>
                    <span class="path-out">Where every number is born, who owns it, when it closes, and who acts on it.</span>
                    <span class="path-chain">
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Procurement</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">QA/QC &amp; HSE</span>
                        <span class="chain-box">Document control</span>
                        <span class="chain-box">Reports &amp; registers</span>
                    </span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker">Track 7 &#183; <b id="pfT7">14</b> weeks</span>
                    <strong class="path-title"><a href="#track-7">Interfaces</a></strong>
                    <span class="path-out">All of it when the job has more than one contract and no single chain of command.</span>
                    <span class="path-chain">
                        <span class="chain-box">Delivery models</span>
                        <span class="chain-box">EPCM</span>
                        <span class="chain-box">Joint ventures</span>
                        <span class="chain-box">Numbers with two owners</span>
                    </span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker"><b id="pfLC">36</b> weeks</span>
                    <strong class="path-title"><a href="#lifecycle">The life of a project</a></strong>
                    <span class="path-out">The order the work arrives in, from the investment decision to the archive.</span>
                    <span class="path-chain">
                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>
                    </span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker">After the writing</span>
                    <strong class="path-title"><a href="#toolbox">The tools</a></strong>
                    <span class="path-out">Last, because a tool you cannot reason about is worth nothing on a site.</span>
                    <span class="path-chain">
                        <span class="chain-box">Excel</span>
                        <span class="chain-box">Primavera P6</span>
                        <span class="chain-box">Power BI</span>
                        <span class="chain-box">Power Platform</span>
                        <span class="chain-box">ERP</span>
                        <span class="chain-box">AI</span>
                    </span>
                </li>
            </ol>
'''

FIVE_CSS = '''
        .path-figure.is-five { grid-template-columns: repeat(5, 1fr); gap: 0 14px; }
        .path-figure.is-five::before { left: 10%; right: 10%;
            background: linear-gradient(to right, #10b981 0 20%, #cbd5e1 20%); }
        .path-figure.is-five .path-title { font-size: 14px; }
        .path-figure.is-five .path-out { font-size: 12px; }
        .path-figure.is-five .chain-box { font-size: 11px; padding: 5px 8px; }
        @media (max-width: 720px) {
            .path-figure.is-five { grid-template-columns: 1fr; }
            .path-figure.is-five::before { left: 9px; right: auto;
                background: linear-gradient(to bottom, #10b981 0 20%, #cbd5e1 20%); }
        }
    </style>'''

PF_WIRING_OLD = re.compile(r"\n            // Path figure counts.*?\}\)\(\);\n", re.S)
PF_WIRING_NEW = '''
            // Path figure counts — read, never typed
            (function () {
                var live = [CURRICULUM, typeof TRACK2 !== 'undefined' ? TRACK2 : null,
                            typeof TRACK3 !== 'undefined' ? TRACK3 : null,
                            typeof TRACK4 !== 'undefined' ? TRACK4 : null,
                            typeof TRACK5 !== 'undefined' ? TRACK5 : null]
                           .filter(Boolean).reduce(function (a, t) { return a + t.liveCount; }, 0);
                var set = function (id, v) { var e = document.getElementById(id); if (e) e.textContent = v; };
                set('pfDone', live);
                if (typeof TRACK6 !== 'undefined') set('pfT6', TRACK6.totalWeeks);
                if (typeof TRACK7 !== 'undefined') set('pfT7', TRACK7.totalWeeks);
                if (typeof LIFECYCLE !== 'undefined') set('pfLC', LIFECYCLE.totalWeeks);
            })();
'''


def main():
    # ---- curriculum.js -------------------------------------------------
    cj = ROOT / "curriculum.js"
    src = cj.read_text(encoding="utf-8")
    if "const TRACK7 =" in src:
        print("  = curriculum.js: zaten uygulanmis")
    else:
        i = src.index("\n// ===================== TRACK 6 — INTERFACES =====================")
        j = src.index("\n// ===================== TRACK 5 — CLAIMS & DELAY ANALYSIS =====================", i)
        src = src[:i] + NEW_JS + src[j:]
        cj.write_text(src, encoding="utf-8")
        print("  + curriculum.js: TRACK6 Reporting, TRACK7 Interfaces, LIFECYCLE 36")

    # ---- learn.html ----------------------------------------------------
    lh = ROOT / "learn.html"
    s = lh.read_text(encoding="utf-8")
    before = s
    done = 'id="track-7"' in s

    if not done:
        i = s.index("<!-- ===== TRACK 6 — INTERFACES ===== -->")
        j = s.index("<!-- ===== THE LIFE OF A PROJECT ===== -->")
        s = s[:i] + SECTIONS + "                " + s[j:]
        s = s.replace('<span class="module-num">07</span>\n', '<span class="module-num">08</span>\n', 1) \
            if s.count('<span class="module-num">07</span>') > 1 else s

    if done:
        print("  = learn.html: zaten uygulanmis")
        check_index()
        return

    # lifecycle module number 07 -> 08
    s = re.sub(r'(<!-- MODULE 07: THE LIFE OF A PROJECT -->.*?<span class="module-num">)07(</span>)',
               r"\g<1>08\g<2>", s, flags=re.S)
    s = s.replace("<!-- MODULE 07: THE LIFE OF A PROJECT -->", "<!-- MODULE 08: THE LIFE OF A PROJECT -->")

    # jump nav
    a = s.index('                <nav class="track-jump"')
    b = s.index("</nav>", a) + len("</nav>")
    s = s[:a] + JUMP_NAV + s[b:]
    s = re.sub(r"\n            \[\['jn1'.*?\}\);\n", JUMP_WIRING, s, count=1, flags=re.S)

    # figure
    fi = s.index('            <ol class="path-figure')
    fj = s.index("            </ol>\n", fi) + len("            </ol>\n")
    s = s[:fi] + FIGURE + s[fj:]
    if ".path-figure.is-five" not in s:
        s = s.replace("    </style>", FIVE_CSS, 1)
    s = PF_WIRING_OLD.sub(PF_WIRING_NEW, s, count=1)

    # main wiring block
    wi = s.index("\n            // Track 6 — Interfaces")
    wj = s.index("\n            // Fill weeks", wi)
    s = s[:wi] + WIRING + s[wj:]

    # anchors + counts
    s = s.replace("#track-1, #track-2, #track-3, #track-4, #track-5, #track-6, #lifecycle, #toolbox { scroll-margin-top: 132px; }",
                  "#track-1, #track-2, #track-3, #track-4, #track-5, #track-6, #track-7, #lifecycle, #toolbox { scroll-margin-top: 132px; }")
    s = re.sub(r"<i class='bx bx-layer'></i> \d+ tracks \+ a toolbox",
               "<i class='bx bx-layer'></i> 8 tracks + a toolbox", s)
    s = s.replace("&#183; Interfaces next", "&#183; Reporting next")
    s = s.replace("<strong>Interfaces</strong> shows how those methods change shape under a different contract and a different organisation.",
                  "<strong>Reporting</strong> follows every number back to the person who produces it and forward to the person who acts on it. <strong>Interfaces</strong> shows how all of it changes shape under more than one contract.")

    if s != before:
        lh.write_text(s, encoding="utf-8")
        print("  + learn.html: Track 6 Reporting, Track 7 Interfaces, figur 5 adim")
    else:
        print("  = learn.html: degisiklik yok")

    check_index()


def check_index():
    ix = ROOT / "index.html"
    t = ix.read_text(encoding="utf-8")
    o = t
    if 'id="homeTrack7Badge"' in t:
        print("  = index.html: zaten uygulanmis")
        return
    t = t.replace('<h3 class="module-title">Interfaces</h3>',
                  '<h3 class="module-title">Reporting</h3>', 1)
    t = t.replace('<p class="module-desc">Five tracks taught the job as one contract with one chain of command. What happens when that stops being true &#8212; delivery models and who holds the scope, EPCM authority without a contract, the critical path through a purchase order, the work between two programmes, and the number with more than one owner.</p>',
                  '<p class="module-desc">Five tracks taught what to do with a number once you have it. This one follows every input back to the department that produces it, in what unit and on whose cut-off date &#8212; then follows every report you issue forward to the person who is supposed to act on it.</p>', 1)
    if 'id="homeTrack7Badge"' not in t:
        marker = '                        <span class="module-status locked-status" id="homeTrackLCBadge">'
        card7 = '''                <div class="module-track module-track-locked">
                    <div class="module-track-header">
                        <div class="module-track-left">
                            <span class="module-number locked">07</span>
                            <div>
                                <h3 class="module-title">Interfaces</h3>
                                <p class="module-desc">Six tracks taught the job as one contract with one chain of command. What happens when that stops being true &#8212; delivery models, EPCM authority without a contract, the critical path through a purchase order, and the number with more than one owner.</p>
                            </div>
                        </div>
                        <span class="module-status locked-status" id="homeTrack7Badge"><i class='bx bx-map-alt'></i> On the roadmap</span>
                    </div>
                </div>

'''
        k = t.index('                <div class="module-track module-track-locked">\n                    <div class="module-track-header">\n                        <div class="module-track-left">\n                            <span class="module-number locked">07</span>')
        t = t[:k] + card7 + t[k:]
        t = t.replace('<span class="module-number locked">07</span>\n                            <div>\n                                <h3 class="module-title">The Life of a Project</h3>',
                      '<span class="module-number locked">08</span>\n                            <div>\n                                <h3 class="module-title">The Life of a Project</h3>', 1)
        t = t.replace("[['homeTrack6Badge', typeof TRACK6 !== 'undefined' ? TRACK6 : null],",
                      "[['homeTrack6Badge', typeof TRACK6 !== 'undefined' ? TRACK6 : null],\n             ['homeTrack7Badge', typeof TRACK7 !== 'undefined' ? TRACK7 : null],", 1)
    if t != o:
        ix.write_text(t, encoding="utf-8")
        print("  + index.html: 06 Reporting, 07 Interfaces, 08 Life of a Project")
    else:
        print("  = index.html: degisiklik yok")


if __name__ == "__main__":
    main()
