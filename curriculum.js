// ============================================================
// THE PROJECT CONTROL HUB — Central Curriculum
// ------------------------------------------------------------
// This is the SINGLE SOURCE OF TRUTH for the whole series.
// To publish a new week: find its entry below, change
// "status" from "upcoming" to "live", set the "date", and
// (optionally) mark it "new: true". That's it — every page
// (home, learn, and each article sidebar) updates itself.
//
// To add a brand-new topic: add an object to the array.
// To fix a title/typo: change it here, once.
// ============================================================

const CURRICULUM = {
  moduleTitle: "Schedule Management",
  totalWeeks: 27,

  // status: "live" = published & clickable | "upcoming" = greyed out
  // page:   the html file for that week (only needed when live)
  // new:    true shows a green "New" badge (use for the latest one)
  weeks: [
    // ---- PHASE A — FOUNDATIONS ----
    { phase: "Phase A — Foundations", n: 1, title: "Why projects fail — and why the answer is never the tools", short: "Why projects fail — and why the answer is never the tools", status: "live", page: "week-1.html", date: "Jun 20, 2026" },
    { n: 2, title: "The foundations of construction project controls", short: "The foundations of construction project controls", status: "live", page: "week-2.html", date: "Jun 27, 2026" },
    { n: 3, title: "That Gantt chart on the wall? It's not your schedule.", short: "That Gantt chart? It's not your schedule.", status: "live", page: "week-3.html", date: "Jul 8, 2026" },

    // ---- PHASE B — SCHEDULE STRATEGY · DOMAIN 1 ----
    { phase: "Phase B — Schedule Strategy", n: 4, title: "Strategy before software — scheduling approach & governance", short: "Strategy before software", status: "live", page: "week-4.html", date: "Jul 15, 2026" },
    { n: 5, title: "Life cycles: Critical Path, Critical Chain & Rolling Wave", short: "Life cycles: CPM, Critical Chain, Rolling Wave", status: "live", page: "week-5.html", date: "Jul 22, 2026" },
    { n: 6, title: "From charter to schedule — building the project strategy", short: "From charter to schedule", status: "live", page: "week-6.html", date: "Jul 29, 2026" },

    // ---- PHASE C — SCHEDULE DEVELOPMENT · DOMAIN 2 ----
    { phase: "Phase C — Schedule Development", n: 7, title: "The 9-step schedule development process", short: "The 9-step development process", status: "live", page: "week-7.html", date: "Aug 5, 2026" },
    { n: 8, title: "Scheduling components I — activity types, calendars, data", short: "Components I — activities, calendars", status: "live", page: "week-8.html", date: "Aug 12, 2026" },
    { n: 9, title: "Scheduling components II — scope & schedule performance", short: "Components II — scope & performance", status: "live", page: "week-9.html", date: "Aug 19, 2026" },
    { n: 10, title: "WBS & baseline development — structure that survives", short: "WBS & baseline development", status: "live", page: "week-10.html", date: "Aug 26, 2026" },
    { n: 11, title: "Activities & networks — PDM, relationships, leads & lags", short: "Activities & networks — PDM, logic", status: "live", page: "week-11.html", date: "Sep 2, 2026" },
    { n: 12, title: "Estimating — duration & budget techniques", short: "Estimating — duration & budget", status: "live", page: "week-12.html", date: "Sep 9, 2026" },
    { n: 13, title: "CPM math — forward pass, backward pass, float", short: "CPM math — forward/backward pass, float", status: "live", page: "week-13.html", date: "Sep 16, 2026" },
    { n: 14, title: "Resource loading, leveling & schedule compression", short: "Resource loading, leveling & compression", status: "live", page: "week-14.html", date: "Sep 23, 2026" },
    { n: 15, title: "Schedule risk analysis — Monte Carlo & contingency", short: "Schedule risk analysis — Monte Carlo", status: "live", page: "week-15.html", date: "Sep 30, 2026" },

    // ---- PHASE D — MONITORING & CONTROL · DOMAIN 3 ----
    { phase: "Phase D — Monitoring & Control", n: 16, title: "Schedule maintenance — actuals & the update cycle", short: "Maintenance — actuals & update cycle", status: "live", page: "week-16.html", date: "Oct 7, 2026" },
    { n: 17, title: "Model health — constraints, open ends, out-of-sequence logic", short: "Model health — constraints, OOS logic", status: "live", page: "week-17.html", date: "Oct 14, 2026" },
    { n: 18, title: "EVM fundamentals — PMB, PV, EV, AC", short: "EVM fundamentals — PMB, PV, EV, AC", status: "live", page: "week-18.html", date: "Oct 21, 2026" },
    { n: 19, title: "EVM analysis — SPI, CPI & variance interpretation", short: "EVM analysis — SPI, CPI, variance", status: "live", page: "week-19.html", date: "Oct 28, 2026" },
    { n: 20, title: "Forecasting — EAC, ETC, TCPI & Earned Schedule", short: "Forecasting — EAC, ETC, Earned Schedule", status: "live", page: "week-20.html", date: "Nov 4, 2026" },
    { n: 21, title: "Change control & protecting the baseline", short: "Change control & baseline protection", status: "live", page: "week-21.html", date: "Nov 11, 2026" },
    { n: 22, title: "The control philosophy — telemetry & managing variances", short: "Control philosophy — telemetry", status: "live", page: "week-22.html", date: "Nov 18, 2026" },
    { n: 23, title: "Project reviews & the Conformance Index", short: "Project reviews & Conformance Index", status: "live", page: "week-23.html", date: "Nov 25, 2026" },

    // ---- PHASE E — CLOSEOUT & FORENSICS · DOMAIN 4 ----
    { phase: "Phase E — Closeout & Forensics", n: 24, title: "Forensic schedule analysis — delays, claims, evidence", short: "Forensic schedule analysis — claims", status: "live", page: "week-24.html", date: "Dec 2, 2026" },
    { n: 25, title: "Closeout & continuous closeout — capturing the data", short: "Closeout & continuous closeout", status: "live", page: "week-25.html", date: "Dec 9, 2026" },

    // ---- PHASE F — COMMUNICATION · DOMAIN 5 ----
    { phase: "Phase F — Communication", n: 26, title: "Reporting & the altitude concept — right data, right level", short: "Reporting & the altitude concept", status: "live", page: "week-26.html", date: "Dec 16, 2026" },
    { n: 27, title: "Stakeholder management & schedule communication", short: "Stakeholder management & communication", status: "live", page: "week-27.html", date: "Dec 23, 2026" },
  ],

  // ---- Derived helpers ----
  get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
  get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
  get latestLiveWeek() {
    const live = this.weeks.filter(w => w.status === "live");
    return live.length ? live[live.length - 1] : null;
  },
  getWeek(n) { return this.weeks.find(w => w.n === n); }
};

// ============================================================
// RENDERERS — build HTML from the data above
// ============================================================

// Sidebar for article pages. currentWeek = the week number of THIS page.
function sidebarHTML(track, currentWeek) {
  // Tüm track'i göster. Eskiden slice(0,5) + sabit bir özet satırı vardı;
  // üç track de tamamlandığı için o satır hem yanlış hem gereksizdi, ve
  // 13. haftadaki okur yan panelde kendini bulamıyordu.
  const label = track.moduleTitle || track.title;
  const rows = track.weeks.map(function (week) {
    const isActive = week.n === currentWeek;
    const isLive = week.status === "live";
    const badge = (week === track.latestLiveWeek && !isActive)
      ? '<span class="sidebar-new" translate="no">New</span>' : "";
    const inner = `<span class="sidebar-week">Week ${week.n}</span>`
                + `<span class="sidebar-item-title">${week.short}</span>`;
    if (isActive) {
      return `<a href="${week.page || '#'}" class="sidebar-series-item active" aria-current="page">${inner}</a>`;
    }
    if (isLive) {
      return `<a href="${week.page}" class="sidebar-series-item">${inner}${badge}</a>`;
    }
    if (week.page) {
      return `<a href="${week.page}" class="sidebar-series-item" data-gated>${inner}${badge}</a>`;
    }
    return `<div class="sidebar-series-item upcoming">${inner}</div>`;
  }).join("");

  return `
    <div class="sidebar-card-header">
      <h4 translate="no">${label} &#183; ${track.totalWeeks} Weeks</h4>
    </div>
    <div class="sidebar-scroll">${rows}</div>`;
}

function renderArticleSidebar(currentWeek) { return sidebarHTML(CURRICULUM, currentWeek); }
function renderTrack2Sidebar(currentWeek)  { return sidebarHTML(TRACK2, currentWeek); }
function renderTrack3Sidebar(currentWeek)  { return sidebarHTML(TRACK3, currentWeek); }

// Full curriculum for learn.html (with phase dividers + progress)
function renderLearnCurriculum() {
  const w = CURRICULUM;
  let rows = "";
  w.weeks.forEach((week, idx) => {
    if (week.phase) {
      // compute the week range covered by this phase
      let end = week.n;
      for (let j = idx + 1; j < w.weeks.length; j++) {
        if (w.weeks[j].phase) break;
        end = w.weeks[j].n;
      }
      const range = week.n === end ? `Week ${week.n}` : `Weeks ${week.n}\u2013${end}`;
      rows += `
        <div class="phase-divider">
          <span class="phase-label" translate="no">${week.phase.toUpperCase()}</span>
          <span class="phase-weeks-tag">${range}</span>
        </div>`;
    }
    const isLive = week.status === "live";
    if (isLive || week.page) {
      const isLatest = week === w.latestLiveWeek;
      const dateOrNew = isLatest
        ? '<span class="week-new" translate="no">New</span>'
        : (week.date ? `<span class="week-date">${week.date}</span>` : '');
      const gated = isLive ? "" : " data-gated";
      rows += `
        <a href="${week.page}" class="week-item"${gated}>
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          ${dateOrNew}
          <i class='bx bx-right-arrow-alt week-arrow'></i>
        </a>`;
    } else {
      rows += `
        <div class="week-item upcoming">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          <span class="week-upcoming-label">Coming soon</span>
        </div>`;
    }
  });
  return rows;
}

// Progress bar values for learn.html
function renderLearnProgress() {
  const w = CURRICULUM;
  return {
    text: `${w.liveCount} of ${w.totalWeeks} published`,
    percent: w.progressPercent
  };
}

// Home page compact list (hero panel: latest 3 live)
function renderHomeLatest() {
  // Sitedeki EN YENİ üç ders — hangi track'ten gelirse gelsin.
  // Önceden yalnızca Track 1'e bakıyordu; üç track de bitince ana sayfa
  // on ay bayat içeriğe "New" rozeti takıyordu.
  const all = [];
  [[CURRICULUM, "SCHEDULE"], [TRACK2, "COST & CASH"], [TRACK3, "RISK"]].forEach(function (pair) {
    pair[0].weeks.filter(function (x) { return x.status === "live" && x.page; })
      .forEach(function (w) { all.push({ w: w, track: pair[1], t: Date.parse(w.date || "") || 0 }); });
  });
  all.sort(function (a, b) { return b.t - a.t; });
  const top = all.slice(0, 3);
  let html = "";
  top.forEach(function (item, i) {
    const w = item.w;
    const badge = i === 0 ? '<span class="home-new-pill" translate="no">New</span>' : '';
    html += `
      <a href="${w.page}" class="discussion-list-item module-post-item">
        <span class="category-text text-green">WEEK ${w.n} &#183; ${item.track}</span>
        <h4>${w.short}</h4>
        <div class="item-meta">
          ${w.date ? `<span class="home-date">${w.date}</span>` : ''}
          ${badge}
          <i class='bx bx-right-arrow-alt arrow-icon'></i>
        </div>
      </a>`;
  });
  return html;
}

// Home page — Module 01 curriculum card (compact, no phase dividers)
// Shows live weeks as links + first few upcoming, then a summary row.
var HOME_PREVIEW = 5;

function homeCurriculumHTML(track) {
  // Ana sayfa müfredatı iştah açar, listelemez. Eskiden bütün canlı haftaları
  // basıyordu; üç track tamamlanınca 69 satır oldu ve sayfa bitmez hale geldi.
  // Tam liste zaten learn.html'de ve bölümün başında "Full Curriculum" butonu var.
  const live = track.weeks.filter(function (x) { return x.status === "live"; });
  const upcoming = track.weeks.filter(function (x) { return x.status === "upcoming"; });
  let rows = "";

  live.slice(0, HOME_PREVIEW).forEach(function (week) {
    const badge = (week === track.latestLiveWeek) ? '<span class="new-badge" translate="no">New</span>' : '';
    rows += `
      <a href="${week.page}" class="module-post-item">
        <span class="post-week">Week ${week.n}</span>
        <span class="post-title">${week.short}</span>
        ${week.date ? `<span class="post-date">${week.date}</span>` : ''}
        ${badge}
        <i class='bx bx-right-arrow-alt'></i>
      </a>`;
  });

  // Henüz yayınlanmamış ilk iki hafta (varsa) — bunlar gerçekten kilitli
  upcoming.slice(0, 2).forEach(function (week) {
    if (week.page) {
      rows += `
        <a href="${week.page}" class="module-post-item" data-gated>
          <span class="post-week">Week ${week.n}</span>
          <span class="post-title">${week.short}</span>
          <i class='bx bx-right-arrow-alt'></i>
        </a>`;
    } else {
      rows += `
        <div class="module-post-item upcoming">
          <span class="post-week">Week ${week.n}</span>
          <span class="post-title">${week.short}</span>
          <span class="post-upcoming">Coming soon</span>
        </div>`;
    }
  });

  const rest = live.slice(HOME_PREVIEW);
  if (rest.length > 0) {
    let restRows = "";
    rest.forEach(function (week) {
      const badge = (week === track.latestLiveWeek) ? '<span class="new-badge" translate="no">New</span>' : '';
      restRows += `
        <a href="${week.page}" class="module-post-item">
          <span class="post-week">Week ${week.n}</span>
          <span class="post-title">${week.short}</span>
          ${week.date ? `<span class="post-date">${week.date}</span>` : ''}
          ${badge}
          <i class='bx bx-right-arrow-alt'></i>
        </a>`;
    });
    rows += `<div class="module-post-rest" hidden>${restRows}</div>
      <button type="button" class="module-post-item module-post-more" aria-expanded="false"
              data-more="Show all ${track.totalWeeks} weeks" data-less="Show fewer" data-count="+${rest.length}">
        <span class="post-week">+${rest.length}</span>
        <span class="post-title">Show all ${track.totalWeeks} weeks</span>
        <i class='bx bx-chevron-down more-chevron'></i>
      </button>`;
  }
  return rows;
}

function renderHomeCurriculum() { return homeCurriculumHTML(CURRICULUM); }
function renderHomeTrack2()     { return homeCurriculumHTML(TRACK2); }
function renderHomeTrack3()     { return homeCurriculumHTML(TRACK3); }

// Module badge text for home
function badgeText(track) {
    if (!track) return '';
    if (track.liveCount >= track.totalWeeks) {
        return '<span class="dot-green"></span> Complete &#183; ' + track.totalWeeks + ' weeks';
    }
    if (track.liveCount === 0) {
        return "<i class='bx bx-time'></i> Starting soon &#183; " + track.totalWeeks + ' weeks';
    }
    var l = track.latestLiveWeek;
    return '<span class="dot-green"></span> In Progress &#183; Week ' + l.n + ' of ' + track.totalWeeks;
}

function badgeClass(track) {
  return (track && track.liveCount === 0) ? 'badge-locked' : 'badge-active';
}

function renderHomeBadge() {
  return badgeText(CURRICULUM);
}


// ============================================================
// TRACK 2 — COST & CASH
// ------------------------------------------------------------
// Separate object on purpose: CURRICULUM above is the single
// source of truth for Track 1 and is read by all 27 article
// pages. Do not merge them — extend here instead.
// ============================================================

const TRACK2 = {
  title: "Cost & Cash",
  totalWeeks: 24,

  // Titles are written in the same register as Track 1: the topic and its
  // components. The punchy version of each is the article's own headline.
  // status: "live" = published & clickable | "upcoming" = greyed out
  weeks: [
    // ---- PHASE A — FOUNDATIONS & ESTIMATING ----
    { phase: "Phase A — Foundations & Estimating", n: 1, title: "Why cost control fails — and why \u201cactual cost\u201d is the hardest number", short: "Why cost control fails", status: "live", page: "cost-week-1.html", date: "Dec 30, 2026" },
    { n: 2, title: "Unit rates — labour, plant, material & waste", short: "Unit rates — how a price is built", status: "live", page: "cost-week-2.html", date: "Jan 6, 2027" },
    { n: 3, title: "Estimate classes & the costs not on the drawing — accuracy, indirects & escalation", short: "Estimate classes, indirects & escalation", status: "live", page: "cost-week-3.html", date: "Jan 13, 2027" },
    { n: 4, title: "The BoQ and the schedule — mapping bill items to activities", short: "Mapping the BoQ to the schedule", status: "live", page: "cost-week-4.html", date: "Jan 20, 2027" },
    { n: 5, title: "Contingency & management reserve — sizing, ownership & drawdown", short: "Contingency & management reserve", status: "live", page: "cost-week-5.html", date: "Jan 27, 2027" },

    // ---- PHASE B — FROM ESTIMATE TO BUDGET ----
    { phase: "Phase B — From Estimate to Budget", n: 6, title: "From estimate to budget — the cost breakdown structure & the code of accounts", short: "The CBS & the code of accounts", status: "live", page: "cost-week-6.html", date: "Feb 3, 2027" },
    { n: 7, title: "Control accounts & work packages — where scope, cost and ownership meet", short: "Control accounts & work packages", status: "live", page: "cost-week-7.html", date: "Feb 10, 2027" },
    { n: 8, title: "The time-phased baseline — building planned value from unit rates", short: "The time-phased baseline", status: "live", page: "cost-week-8.html", date: "Feb 17, 2027" },
    { n: 9, title: "The schedule of values — valuation, front-loading & interim payment", short: "The schedule of values", status: "live", page: "cost-week-9.html", date: "Feb 24, 2027" },

    // ---- PHASE C — MEASUREMENT & CHANGE ----
    { phase: "Phase C — Measurement & Change", n: 10, title: "Cost accounting for planners — commitment, accrual & expenditure", short: "Commitment, accrual & expenditure", status: "live", page: "cost-week-10.html", date: "Mar 3, 2027" },
    { n: 11, title: "Physical progress measurement — the six methods", short: "Physical progress — the six methods", status: "live", page: "cost-week-11.html", date: "Mar 10, 2027" },
    { n: 12, title: "Subcontractor cost control — packages, valuations & variations", short: "Subcontractor cost control", status: "live", page: "cost-week-12.html", date: "Mar 17, 2027" },
    { n: 13, title: "Change & variation pricing — bill rates, star rates, dayworks & disruption", short: "Pricing a change", status: "live", page: "cost-week-13.html", date: "Mar 24, 2027" },
    { n: 14, title: "Single data capture — one entry, cost and schedule", short: "Single data capture", status: "live", page: "cost-week-14.html", date: "Mar 31, 2027" },
    { n: 15, title: "Productivity control — factors, indices & earned hours", short: "Productivity & earned hours", status: "live", page: "cost-week-15.html", date: "Apr 7, 2027" },

    // ---- PHASE D — CASH ----
    { phase: "Phase D — Cash", n: 16, title: "Cash flow fundamentals — the income and requirements curves", short: "Cash flow fundamentals", status: "live", page: "cost-week-16.html", date: "Apr 14, 2027" },
    { n: 17, title: "The interim payment cycle — valuation, retention & the working capital gap", short: "Interim payment & retention", status: "live", page: "cost-week-17.html", date: "Apr 21, 2027" },
    { n: 18, title: "Overtrading — why growth destroys profitable contractors", short: "Overtrading — when growth kills", status: "live", page: "cost-week-18.html", date: "Apr 28, 2027" },
    { n: 19, title: "Cash management — the levers a project actually has", short: "Cash management strategies", status: "live", page: "cost-week-19.html", date: "May 5, 2027" },

    // ---- PHASE E — THE COMPANY ----
    { phase: "Phase E — The Company", n: 20, title: "Direct, indirect & site overheads — the true cost of being there", short: "Direct, indirect & site overheads", status: "live", page: "cost-week-20.html", date: "May 12, 2027" },
    { n: 21, title: "The levers — value engineering & the time-cost trade-off", short: "Value engineering & time-cost trade-off", status: "live", page: "cost-week-21.html", date: "May 19, 2027" },
    { n: 22, title: "Contribution & margin — what the project returns to the business", short: "Contribution & margin", status: "live", page: "cost-week-22.html", date: "May 26, 2027" },
    { n: 23, title: "Contract cost accounting — revenue recognition & the expected loss rule", short: "Revenue recognition & expected loss", status: "live", page: "cost-week-23.html", date: "Jun 2, 2027" },
    { n: 24, title: "The commercial planner — speaking the language of money", short: "The commercial planner", status: "live", page: "cost-week-24.html", date: "Jun 9, 2027" },
  ],


  get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
  get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
  get latestLiveWeek() {
    const live = this.weeks.filter(w => w.status === "live");
    return live.length ? live[live.length - 1] : null;
  },
  get phaseCount() { return this.weeks.filter(w => w.phase).length; },
  getWeek(n) { return this.weeks.find(w => w.n === n); }
};

// Renderer: Track 2 curriculum for learn.html
// NOTE: must use the SAME classes as renderLearnCurriculum above,
// or the rows render as unstyled plain text.
function renderTrack2Curriculum() {
  const t = TRACK2;
  let rows = "";
  t.weeks.forEach((week, idx) => {
    if (week.phase) {
      let end = week.n;
      for (let j = idx + 1; j < t.weeks.length; j++) {
        if (t.weeks[j].phase) break;
        end = t.weeks[j].n;
      }
      const range = week.n === end ? `Week ${week.n}` : `Weeks ${week.n}\u2013${end}`;
      rows += `
        <div class="phase-divider">
          <span class="phase-label" translate="no">${week.phase.toUpperCase()}</span>
          <span class="phase-weeks-tag">${range}</span>
        </div>`;
    }
    if (week.status === "live" && week.page) {
      const isLatest = week === t.latestLiveWeek;
      const dateOrNew = isLatest
        ? '<span class="week-new" translate="no">New</span>'
        : (week.date ? `<span class="week-date">${week.date}</span>` : '');
      rows += `
        <a href="${week.page}" class="week-item">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          ${dateOrNew}
          <i class='bx bx-right-arrow-alt week-arrow'></i>
        </a>`;
    } else {
      rows += `
        <div class="week-item upcoming">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          <span class="week-upcoming-label">Coming soon</span>
        </div>`;
    }
  });
  return rows;
}

// Progress bar values for the Track 2 card on learn.html
function renderTrack2Progress() {
  const t = TRACK2;
  return {
    text: `${t.liveCount} of ${t.totalWeeks} published`,
    percent: t.progressPercent
  };
}

// Renderer: Track 2 post list for the home page module card.
// Mirrors renderHomeCurriculum so the rows pick up the same styling.

// Module badge text for the Track 2 card on home
function renderHomeTrack2Badge() {
  return badgeText(TRACK2);
}

// Sidebar for Track 2 article pages. Mirrors renderArticleSidebar.


// ============================================================
// TRACK 3 — RISK
// The same $1,000,000 project, third lens. Track 1 measured time,
// Track 2 measured money, Track 3 measures what has not happened yet.
// Opens on the five-line risk register from Cost & Cash Week 5 —
// the one nobody ever audited.
// ============================================================
const TRACK3 = {
  title: "Risk",
  totalWeeks: 18,

  // Same register as Tracks 1 and 2: the topic and its components.
  // The punchy version of each is the article's own headline.
  weeks: [
    // ---- PHASE A — IDENTIFICATION & THE REGISTER ----
    { phase: "Phase A — Identification & the Register", n: 1, title: "Risk fundamentals — the register behind the contingency", short: "The register behind the contingency", status: "live", page: "risk-week-1.html", date: "Jun 16, 2027" },
    { n: 2, title: "Risk identification — where risks actually hide on a construction project", short: "Where risks actually hide", status: "live", page: "risk-week-2.html", date: "Jun 23, 2027" },
    { n: 3, title: "The risk breakdown structure — a WBS for what can go wrong", short: "The risk breakdown structure", status: "live", page: "risk-week-3.html", date: "Jun 30, 2027" },
    { n: 4, title: "Writing a risk properly — cause, event, effect", short: "Cause, event, effect", status: "live", page: "risk-week-4.html", date: "Jul 7, 2027" },

    // ---- PHASE B — QUALITATIVE ANALYSIS ----
    { phase: "Phase B — Qualitative Analysis", n: 5, title: "Qualitative analysis — anchoring probability and impact scales", short: "Anchoring the scales", status: "live", page: "risk-week-5.html", date: "Jul 14, 2027" },
    { n: 6, title: "The limits of the probability-impact matrix", short: "The limits of the heat map", status: "live", page: "risk-week-6.html", date: "Jul 21, 2027" },
    { n: 7, title: "Bias, the planning fallacy & reference class forecasting", short: "Bias & reference class forecasting", status: "live", page: "risk-week-7.html", date: "Jul 28, 2027" },

    // ---- PHASE C — QUANTITATIVE ANALYSIS ----
    { phase: "Phase C — Quantitative Analysis", n: 8, title: "Two kinds of uncertainty — aleatory and epistemic", short: "Aleatory & epistemic uncertainty", status: "live", page: "risk-week-8.html", date: "Aug 4, 2027" },
    { n: 9, title: "The shape of an estimate — three-point ranges & distributions", short: "Three-point ranges & distributions", status: "live", page: "risk-week-9.html", date: "Aug 11, 2027" },
    { n: 10, title: "Correlation & common cause effects — why bad days cluster", short: "Correlation & common cause effects", status: "live", page: "risk-week-10.html", date: "Aug 18, 2027" },
    { n: 11, title: "Cost risk analysis — pointing the machine at money", short: "Cost risk analysis", status: "live", page: "risk-week-11.html", date: "Aug 25, 2027" },
    { n: 12, title: "Risk appetite & confidence levels — P50, P80 and who decides", short: "Risk appetite & confidence levels", status: "live", page: "risk-week-12.html", date: "Sep 1, 2027" },

    // ---- PHASE D — RISK OWNERSHIP & THE CONTRACT ----
    { phase: "Phase D — Risk Ownership & the Contract", n: 13, title: "Response strategies — priced, owned, and the decision tree", short: "Response strategies & decision trees", status: "live", page: "risk-week-13.html", date: "Sep 8, 2027" },
    { n: 14, title: "Contractual risk allocation — FIDIC and the ground risk", short: "FIDIC & the ground risk", status: "live", page: "risk-week-14.html", date: "Sep 15, 2027" },
    { n: 15, title: "Time, money, or neither — extension of time, exceptional events, insurance & bonds", short: "Transferring risk — insurance & bonds", status: "live", page: "risk-week-15.html", date: "Sep 22, 2027" },

    // ---- PHASE E — LIVING WITH RISK ----
    { phase: "Phase E — Living with Risk", n: 16, title: "The living register — triggers, reviews & Bayesian revision", short: "The living register", status: "live", page: "risk-week-16.html", date: "Sep 29, 2027" },
    { n: 17, title: "Opportunity — the half nobody manages", short: "Opportunity management", status: "live", page: "risk-week-17.html", date: "Oct 6, 2027" },
    { n: 18, title: "The risk-literate planner — acting before the number moves", short: "Acting before the number moves", status: "live", page: "risk-week-18.html", date: "Oct 13, 2027" }
  ],

  get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
  get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
  get latestLiveWeek() {
    const live = this.weeks.filter(w => w.status === "live");
    return live.length ? live[live.length - 1] : null;
  },
  get phaseCount() { return this.weeks.filter(w => w.phase).length; },
  getWeek(n) { return this.weeks.find(w => w.n === n); }
};


// ============================================================
//  TRACK 4 — CONTRACT MANAGEMENT
//  Split out of the old "Claims & Delay Analysis" on 2026-07-20:
//  Risk Week 18 sets up contract administration, not forensic delay.
//  Track 4 preserves an entitlement; Track 5 values one.
// ============================================================
const TRACK4 = {
    title: "Contract Management",
    totalWeeks: 20,
    weeks: [
        // ---- PHASE A — THE CONTRACT AS A SYSTEM ----
        { phase: "Phase A — The Contract as a System", n: 1, title: "Contract management fundamentals — the notice behind the entitlement", short: "The notice behind the entitlement", status: "live", page: "contract-week-1.html", date: "Oct 20, 2027" },
        { n: 2, title: "Reading a contract — structure, priority of documents and definitions", short: "Reading a contract", status: "live", page: "contract-week-2.html", date: "Oct 27, 2027" },
        { n: 3, title: "The Engineer — authority, impartiality and determination", short: "The Engineer", status: "live", page: "contract-week-3.html", date: "Nov 3, 2027" },
        { n: 4, title: "Contract types — lump sum, remeasurement, cost-plus and target cost", short: "Contract types", status: "live", page: "contract-week-4.html", date: "Nov 10, 2027" },

        // ---- PHASE B — OBLIGATIONS & INSTRUCTIONS ----
        { phase: "Phase B — Obligations & Instructions", n: 5, title: "Employer and contractor obligations — what each side actually promised", short: "What each side promised", status: "live", page: "contract-week-5.html", date: "Nov 17, 2027" },
        { n: 6, title: "Instructions — and the ones that are not instructions", short: "Instructions", status: "live", page: "contract-week-6.html", date: "Nov 24, 2027" },
        { n: 7, title: "Variations — the right to be paid for a change", short: "Variations", status: "live", page: "contract-week-7.html", date: "Dec 1, 2027" },
        { n: 8, title: "Building entitlement — before a claim exists", short: "Building entitlement", status: "live", page: "contract-week-8.html", date: "Dec 8, 2027" },

        // ---- PHASE C — TIME ----
        { phase: "Phase C — Time", n: 9, title: "Extension of time — the contractual mechanism", short: "Extension of time", status: "live", page: "contract-week-9.html", date: "Dec 15, 2027" },
        { n: 10, title: "Notices and time bars — periods, forms and recipients", short: "Notices and time bars", status: "live", page: "contract-week-10.html", date: "Dec 22, 2027" },
        { n: 11, title: "Programme obligations — the contract's view of your schedule", short: "Programme obligations", status: "live", page: "contract-week-11.html", date: "Dec 29, 2027" },

        // ---- PHASE D — MONEY ----
        { phase: "Phase D — Money", n: 12, title: "Payment mechanisms — application, certificate and the money", short: "Payment mechanisms", status: "live", page: "contract-week-12.html", date: "Jan 5, 2028" },
        { n: 13, title: "When the contract says it isn't a variation", short: "When it isn't a variation", status: "live", page: "contract-week-13.html", date: "Jan 12, 2028" },
        { n: 14, title: "Currency, escalation and price adjustment", short: "Currency and escalation", status: "live", page: "contract-week-14.html", date: "Jan 19, 2028" },
        { n: 15, title: "Retention, bonds, guarantees and insurance", short: "Retention and securities", status: "live", page: "contract-week-15.html", date: "Jan 26, 2028" },

        // ---- PHASE E — RISK, DISPUTES & OTHER REGIMES ----
        { phase: "Phase E — Risk, Disputes & Other Regimes", n: 16, title: "Risk allocation across the three books — Red, Yellow and Silver", short: "Across the three books", status: "live", page: "contract-week-16.html", date: "Feb 2, 2028" },
        { n: 17, title: "Suspension and termination — the contractual exits", short: "Suspension and termination", status: "live", page: "contract-week-17.html", date: "Feb 9, 2028" },
        { n: 18, title: "Dispute avoidance — the DAAB and the notice of dissatisfaction", short: "Dispute avoidance", status: "live", page: "contract-week-18.html", date: "Feb 16, 2028" },
        { n: 19, title: "NEC4 — early warning, compensation events and proactive contract management", short: "NEC4", status: "live", page: "contract-week-19.html", date: "Feb 23, 2028" },
        { n: 20, title: "The contract administrator's year — a calendar of obligations", short: "A calendar of obligations", status: "live", page: "contract-week-20.html", date: "Mar 1, 2028" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() {
        const live = this.weeks.filter(w => w.status === "live");
        return live.length ? live[live.length - 1] : null;
    },
    get phaseCount() { return this.weeks.filter(w => w.phase).length; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};


// Learn-page curriculum rows. Same classes as renderLearnCurriculum, otherwise
// the rows render as unstyled text. Shared so a new track needs a wrapper, not a copy.
function learnCurriculumHTML(t) {
  let rows = "";
  t.weeks.forEach((week, idx) => {
    if (week.phase) {
      let end = week.n;
      for (let j = idx + 1; j < t.weeks.length; j++) {
        if (t.weeks[j].phase) break;
        end = t.weeks[j].n;
      }
      const range = week.n === end ? `Week ${week.n}` : `Weeks ${week.n}\u2013${end}`;
      rows += `
        <div class="phase-divider">
          <span class="phase-label" translate="no">${week.phase.toUpperCase()}</span>
          <span class="phase-weeks-tag">${range}</span>
        </div>`;
    }
    if (week.status === "live" && week.page) {
      const isLatest = week === t.latestLiveWeek;
      const dateOrNew = isLatest
        ? '<span class="week-new" translate="no">New</span>'
        : (week.date ? `<span class="week-date">${week.date}</span>` : '');
      rows += `
        <a href="${week.page}" class="week-item">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          ${dateOrNew}
          <i class='bx bx-right-arrow-alt week-arrow'></i>
        </a>`;
    } else {
      rows += `
        <div class="week-item upcoming">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          <span class="week-upcoming-label">Coming soon</span>
        </div>`;
    }
  });
  return rows;
}

function renderTrack4Curriculum() { return learnCurriculumHTML(TRACK4); }

function renderTrack4Sidebar(currentWeek) { return sidebarHTML(TRACK4, currentWeek); }
function renderHomeTrack4()               { return homeCurriculumHTML(TRACK4); }
function renderHomeTrack4Badge() {
  return badgeText(TRACK4);
}

function renderTrack4Progress() {
    return { text: `${TRACK4.liveCount} of ${TRACK4.totalWeeks} published`, percent: TRACK4.progressPercent };
}



// ===================== TRACK 0 — THE SHAPE OF THE JOB =====================
// Read before Track 1, written after Track 5. Orientation, not method:
// it describes the job rather than teaching a technique. Every week must
// answer "what happens, who does it, what is it called" and hand the
// method itself to one of the five tracks that follow.
const TRACK0 = {
    title: "The Shape of the Job",
    totalWeeks: 17,
    weeks: [
        // ---- PHASE A — THE JOB BEFORE IT IS A JOB ----
        { phase: "Phase A \u2014 The Job Before It Is a Job", n: 1, title: "The documents that arrive before the work \u2014 charter, contract, scope, BoQ, drawings", short: "The documents that arrive first", status: "upcoming" },
        { n: 2, title: "Tender to award \u2014 the estimate you inherited and the schedule you did not write", short: "Tender to award", status: "upcoming" },
        { n: 3, title: "The contract as an organisation chart \u2014 who can instruct whom", short: "Who can instruct whom", status: "upcoming" },

        // ---- PHASE B — BUILDING THE MACHINE ----
        { phase: "Phase B \u2014 Building the Machine", n: 4, title: "The departments \u2014 what each one produces and what each needs from you", short: "The departments", status: "upcoming" },
        { n: 5, title: "Where project controls sits \u2014 planning, cost, commercial and the monthly argument", short: "Where project controls sits", status: "upcoming" },
        { n: 6, title: "Coding before dating \u2014 WBS, OBS, cost codes, areas and systems", short: "Coding before dating", status: "upcoming" },
        { n: 7, title: "Mobilisation \u2014 the project inside the project", short: "Mobilisation", status: "upcoming" },

        // ---- PHASE C — THE RHYTHM ----
        { phase: "Phase C \u2014 The Rhythm", n: 8, title: "The project heartbeat \u2014 daily, weekly, monthly and the cut-off dates", short: "The project heartbeat", status: "upcoming" },
        { n: 9, title: "Nobody gives you data \u2014 measurement, surveys and the sources you chase", short: "Nobody gives you data", status: "upcoming" },
        { n: 10, title: "The meetings are the machine \u2014 who chairs, who decides, what you are there to do", short: "The meetings are the machine", status: "upcoming" },
        { n: 11, title: "Four reports, four audiences \u2014 and what happens when you mix them up", short: "Four reports, four audiences", status: "upcoming" },

        // ---- PHASE D — WHERE IT GOES WRONG ----
        { phase: "Phase D \u2014 Where It Goes Wrong", n: 12, title: "Construction is decided upstream \u2014 engineering, vendor data and expediting", short: "Decided upstream", status: "upcoming" },
        { n: 13, title: "The vocabulary of change \u2014 instruction, variation, notice, claim", short: "The vocabulary of change", status: "upcoming" },
        { n: 14, title: "Trouble travels in documents \u2014 NCRs, site instructions and recovery plans", short: "Trouble travels in documents", status: "upcoming" },

        // ---- PHASE E — FINISHING ----
        { phase: "Phase E \u2014 Finishing", n: 15, title: "Construction complete is not complete \u2014 punch lists, handover, defects liability", short: "Complete is not complete", status: "upcoming" },
        { n: 16, title: "The job outlives the project \u2014 as-built, final account, archive, lessons learned", short: "The job outlives the project", status: "upcoming" },
        { n: 17, title: "What you now know you do not know \u2014 a map of the five tracks ahead", short: "A map of the tracks ahead", status: "upcoming" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() {
        const live = this.weeks.filter(w => w.status === "live");
        return live.length ? live[live.length - 1] : null;
    },
    get phaseCount() { return this.weeks.filter(w => w.phase).length; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};

function renderTrack0Curriculum() { return learnCurriculumHTML(TRACK0); }
function renderTrack0Sidebar(currentWeek) { return sidebarHTML(TRACK0, currentWeek); }
function renderHomeTrack0()               { return homeCurriculumHTML(TRACK0); }
function renderHomeTrack0Badge()          { return badgeText(TRACK0); }
function renderTrack0Progress() {
    return { text: `${TRACK0.liveCount} of ${TRACK0.totalWeeks} published`, percent: TRACK0.progressPercent };
}


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
        { phase: "Phase A \u2014 What feeds you", n: 1, title: "What project controls produces, and what it must be fed", short: "What it produces, what it needs", status: "upcoming" },
        { n: 2, title: "Working backwards from a deliverable \u2014 output, inputs, owners, units", short: "Working backwards", status: "upcoming" },
        { n: 3, title: "Engineering feeds you \u2014 deliverables, IFC, and approved with comments", short: "Engineering feeds you", status: "upcoming" },
        { n: 4, title: "Engineering progress \u2014 where percent complete is easiest to fake", short: "Engineering progress", status: "upcoming" },
        { n: 5, title: "Procurement feeds you \u2014 PO status, expediting, shipping, vendor data", short: "Procurement feeds you", status: "upcoming" },
        { n: 6, title: "Material at site \u2014 delivered, stored, issued, installed", short: "Material at site", status: "upcoming" },
        { n: 7, title: "Construction: quantities \u2014 three numbers for the same wall", short: "Construction: quantities", status: "upcoming" },
        { n: 8, title: "Construction: progress \u2014 who measures, in what unit, on which day", short: "Construction: progress", status: "upcoming", page: "reporting-week-8.html" },
        { n: 9, title: "Ready means six different things \u2014 drawing, material, access, permit, labour, plant", short: "Ready means six different things", status: "upcoming" },
        { n: 10, title: "Construction: hours and plant \u2014 allocation, availability, utilisation, idle time", short: "Hours and plant", status: "upcoming" },
        { n: 11, title: "QA/QC feeds you \u2014 NCRs, inspection requests, and progress that reverses", short: "QA/QC feeds you", status: "upcoming" },
        { n: 12, title: "HSE feeds you \u2014 permits, holds, stand-downs and lost time as delay events", short: "HSE feeds you", status: "upcoming" },
        { n: 13, title: "Document control feeds you \u2014 revision status, and why half the site builds to Rev B", short: "Document control feeds you", status: "upcoming" },
        { n: 14, title: "Commercial feeds you \u2014 commitments, accruals and invoices on somebody else\u2019s cut-off", short: "Commercial feeds you", status: "upcoming" },
        { n: 15, title: "The client feeds you \u2014 instructions, approvals, comments: time rather than data", short: "The client feeds you", status: "upcoming" },

        { phase: "Phase B \u2014 What you issue", n: 16, title: "The calendar \u2014 data date, cut-off, and three departments closing on three days", short: "The calendar", status: "upcoming" },
        { n: 17, title: "The daily report \u2014 the shortest document with the most consequences", short: "The daily report", status: "upcoming" },
        { n: 18, title: "The weekly report and the look-ahead \u2014 and the only part anyone acts on", short: "Weekly report and look-ahead", status: "upcoming" },
        { n: 19, title: "The monthly report \u2014 curve, variance, narrative, and the summary read first", short: "The monthly report", status: "upcoming" },
        { n: 20, title: "Four audiences, four altitudes \u2014 one number told four ways, not four stories", short: "Four audiences, four altitudes", status: "upcoming" },
        { n: 21, title: "Dashboards \u2014 who reads what, and what a dashboard cannot say", short: "Dashboards", status: "upcoming" },
        { n: 22, title: "KPIs, leading and lagging \u2014 last month against next month", short: "KPIs, leading and lagging", status: "upcoming" },
        { n: 23, title: "Minutes, actions and closure \u2014 and the recovery action list under pressure", short: "Minutes, actions and closure", status: "upcoming" },
        { n: 24, title: "The register system \u2014 assumption, risk, change; interface, constraint, delay", short: "The register system", status: "upcoming" },
        { n: 25, title: "When two reports disagree \u2014 progress against valuation, reconciled first", short: "When two reports disagree", status: "upcoming" },
        { n: 26, title: "The report nobody acts on \u2014 the most common failure, and what to change", short: "The report nobody acts on", status: "upcoming" }
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
        { phase: "Who holds the scope", n: 1, title: "The shape every track has assumed \u2014 one contract, one Engineer, one programme", short: "The shape every track assumed", status: "upcoming" },
        { n: 2, title: "How many contracts are there \u2014 the axis nobody teaches", short: "How many contracts are there", status: "upcoming" },
        { n: 3, title: "EPCM \u2014 instructing people you have no contract with", short: "Instructing without a contract", status: "upcoming" },
        { n: 4, title: "The Engineer, multiplied \u2014 determination when every package has its own", short: "The Engineer, multiplied", status: "upcoming" },
        { n: 5, title: "Concurrency without a head contract \u2014 the Special Provisions that do not exist", short: "Concurrency with no head contract", status: "upcoming" },
        { phase: "When the contractor is plural", n: 6, title: "Joint ventures and consortia \u2014 one face, several sets of books", short: "Joint ventures and consortia", status: "upcoming" },
        { n: 7, title: "Alliancing, partnering and IPD \u2014 contracts built to suppress claims", short: "Alliancing, partnering and IPD", status: "upcoming" },
        { phase: "The critical path leaves the site", n: 8, title: "Procurement on the critical path \u2014 when the path runs through an order", short: "Procurement on the critical path", status: "upcoming" },
        { phase: "Where two programmes meet", n: 9, title: "The work in nobody\u2019s scope \u2014 the gap between two risk registers", short: "The work in nobody\u2019s scope", status: "upcoming" },
        { n: 10, title: "Interface management as a function \u2014 owning a boundary, not reporting one", short: "Interface management", status: "upcoming" },
        { n: 11, title: "Access, sequencing and the delay that belongs to no one", short: "The delay that belongs to no one", status: "upcoming" },
        { phase: "The number with more than one owner", n: 12, title: "Progress and valuation collide \u2014 two methods, one monthly number", short: "Progress and valuation collide", status: "upcoming" },
        { n: 13, title: "The cost that arrives from somebody else\u2019s books \u2014 another ledger, another cut-off", short: "Somebody else\u2019s books", status: "upcoming" },
        { n: 14, title: "Document control at organisational scale \u2014 six firms, one transmittal", short: "Document control at scale", status: "upcoming" }
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
        { n: 1, title: "The journey of one drawing \u2014 six hands, six changes, one as-built", short: "The journey of one drawing", status: "upcoming" },

        { phase: "Phase A \u2014 Before the project exists", n: 2, title: "Why a project exists \u2014 business need, investment decision, and who is already committed", short: "Why a project exists", status: "upcoming" },
        { n: 3, title: "Feasibility \u2014 what gets studied, what gets assumed, and which assumption reaches you", short: "Feasibility", status: "upcoming" },
        { n: 4, title: "Delivery strategy \u2014 how the owner decided to buy it", short: "Delivery strategy", status: "upcoming" },
        { n: 5, title: "Packaging and tender strategy \u2014 why the job was split, and what each split costs", short: "Packaging and tender strategy", status: "upcoming" },
        { n: 6, title: "Tender to award \u2014 ITB, clarification, evaluation, and the estimate you inherit", short: "Tender to award", status: "upcoming" },

        { phase: "Phase B \u2014 Start-up", n: 7, title: "Day one \u2014 the folder, the contract, and the dates you must know by Friday", short: "Day one", status: "upcoming" },
        { n: 8, title: "The kick-off \u2014 what gets decided, and what gets deferred forever", short: "The kick-off", status: "upcoming" },
        { n: 9, title: "The project execution plan \u2014 including the communication matrix nobody reads", short: "The project execution plan", status: "upcoming" },
        { n: 10, title: "Who is who \u2014 client, PMC, EPC, vendors, and the authority behind each name", short: "Who is who", status: "upcoming" },
        { n: 11, title: "Coding philosophy \u2014 the decisions that cannot be made later", short: "Coding philosophy", status: "upcoming" },
        { n: 12, title: "Setting up document control \u2014 transmittals, revisions, registers", short: "Setting up document control", status: "upcoming" },
        { n: 13, title: "Building the baseline \u2014 the two weeks, not the method", short: "Building the baseline", status: "upcoming" },
        { n: 14, title: "The meeting structure \u2014 who chairs, who decides, and which ones move blame", short: "The meeting structure", status: "upcoming" },

        { phase: "Phase C \u2014 Engineering and procurement", n: 15, title: "How engineering flows \u2014 deliverable lists, disciplines, and the design freeze", short: "How engineering flows", status: "upcoming" },
        { n: 16, title: "The procurement cycle \u2014 requisition to purchase order", short: "The procurement cycle", status: "upcoming" },
        { n: 17, title: "Long lead \u2014 ordering before the design is finished, and the cost of being wrong", short: "Long lead", status: "upcoming" },

        { phase: "Phase D \u2014 Construction", n: 18, title: "Mobilisation \u2014 the project inside the project", short: "Mobilisation", status: "upcoming" },
        { n: 19, title: "Site logistics and temporary works \u2014 access, laydown, cranes, and a scaffold with its own lead time", short: "Site logistics and temporary works", status: "upcoming" },
        { n: 20, title: "Work packaging \u2014 dividing scope into something a crew can be handed", short: "Work packaging", status: "upcoming" },
        { n: 21, title: "Clearing the workfront \u2014 constraint removal, and who removes each kind", short: "Clearing the workfront", status: "upcoming" },
        { n: 22, title: "Look-ahead planning \u2014 the six weeks that run the site", short: "Look-ahead planning", status: "upcoming" },
        { n: 23, title: "The week, day by day \u2014 one workable rhythm, not the rhythm", short: "The week, day by day", status: "upcoming" },

        { phase: "Phase E \u2014 Commercial", n: 24, title: "Change on the ground \u2014 instruction to variation to claim, as it happens", short: "Change on the ground", status: "upcoming" },
        { n: 25, title: "Forecasting \u2014 the number you will be judged on", short: "Forecasting", status: "upcoming" },

        { phase: "Phase F \u2014 Governance", n: 26, title: "Who approves what \u2014 authority, delegation, and the escalation chain", short: "Who approves what", status: "upcoming" },
        { n: 27, title: "The change control board", short: "The change control board", status: "upcoming" },
        { n: 28, title: "Risk reviews that change something", short: "Risk reviews that change something", status: "upcoming" },

        { phase: "Phase G \u2014 Finishing", n: 29, title: "Mechanical completion \u2014 and the birth of the punch list", short: "Mechanical completion", status: "upcoming" },
        { n: 30, title: "Pre-commissioning and commissioning \u2014 handing the schedule to another discipline", short: "Pre-commissioning and commissioning", status: "upcoming" },
        { n: 31, title: "Performance tests", short: "Performance tests", status: "upcoming" },
        { n: 32, title: "Closing the punch list and taking over", short: "Closing the punch list", status: "upcoming" },
        { n: 33, title: "Demobilisation \u2014 the crane, the camp and the punch list want the same people", short: "Demobilisation", status: "upcoming" },
        { n: 34, title: "Closeout \u2014 as-built, final account, archive", short: "Closeout", status: "upcoming" },

        { phase: "Capstone", n: 35, title: "Designing a project controls system from nothing", short: "Designing the system from nothing", status: "upcoming" },
        { n: 36, title: "The first 90 days \u2014 a contract, a BoQ, a drawing set and an empty schedule", short: "The first 90 days", status: "upcoming" }
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

// ===================== TRACK 5 — CLAIMS & DELAY ANALYSIS =====================
const TRACK5 = {
    title: "Claims & Delay Analysis",
    totalWeeks: 28,
    weeks: [

        // ---- PHASE A — WHAT A CLAIM HAS TO PROVE ----
        { phase: "Phase A — What a Claim Has to Prove", n: 1,
          title: "Claims fundamentals — from preserved right to measured quantum",
          short: "Claims fundamentals", status: "live", page: "claim-week-1.html",
          date: "Mar 8, 2028" },
        { n: 2, title: "Cause and effect — the chain a claim has to close",
          short: "Cause and effect", status: "live", page: "claim-week-2.html",
          date: "Mar 15, 2028" },
        { n: 3, title: "Types of delay — excusable, compensable and the ones that pay nothing",
          short: "Types of delay", status: "live", page: "claim-week-3.html",
          date: "Mar 22, 2028" },
        { n: 4, title: "Criticality and float — what every claim actually argues about",
          short: "Criticality and float", status: "live", page: "claim-week-4.html",
          date: "Mar 29, 2028" },

        // ---- PHASE B — THE EVIDENCE THE ANALYSIS RUNS ON ----
        { phase: "Phase B — The Evidence the Analysis Runs On", n: 5,
          title: "The as-planned programme — validating a baseline you did not build",
          short: "The as-planned programme", status: "live", page: "claim-week-5.html",
          date: "Apr 5, 2028" },
        { n: 6, title: "The site record — daily reports, allocation sheets and what each one proves",
          short: "The site record", status: "live", page: "claim-week-6.html",
          date: "Apr 12, 2028" },
        { n: 7, title: "The as-built programme — reconstructing what actually happened",
          short: "The as-built programme", status: "live", page: "claim-week-7.html",
          date: "Apr 19, 2028" },
        { n: 8, title: "Programme updates — the contemporaneous record and the gaps in it",
          short: "Programme updates", status: "live", page: "claim-week-8.html",
          date: "Apr 26, 2028" },

        // ---- PHASE C — METHODS, BY THE EVIDENCE THEY NEED ----
        { phase: "Phase C — Methods, by the Evidence They Need", n: 9,
          title: "Choosing a method — what the SCL and AACE taxonomies are for",
          short: "Choosing a method", status: "live", page: "claim-week-9.html",
          date: "May 3, 2028" },
        { n: 10, title: "Impacted as-planned — delay modelled into a plan that never happened",
          short: "Impacted as-planned", status: "live", page: "claim-week-10.html",
          date: "May 10, 2028" },
        { n: 11, title: "Time impact analysis — fragnets, updates and prospective assessment",
          short: "Time impact analysis", status: "live", page: "claim-week-11.html",
          date: "May 17, 2028" },
        { n: 12, title: "Windows analysis — contemporaneous periods and time slices",
          short: "Windows analysis", status: "live", page: "claim-week-12.html",
          date: "May 24, 2028" },
        { n: 13, title: "As-planned versus as-built — the comparison and its limits",
          short: "As-planned versus as-built", status: "live", page: "claim-week-13.html",
          date: "May 31, 2028" },
        { n: 14, title: "Collapsed as-built — subtraction, and the judgement hidden in it",
          short: "Collapsed as-built", status: "live", page: "claim-week-14.html",
          date: "Jun 7, 2028" },
        { n: 15, title: "Why two analysts disagree — method choice as the real dispute",
          short: "Why two analysts disagree", status: "live", page: "claim-week-15.html",
          date: "Jun 14, 2028" },

        // ---- PHASE D — THE HARD ARGUMENTS ----
        { phase: "Phase D — The Hard Arguments", n: 16,
          title: "Concurrency — two causes, one delay, and no agreed definition",
          short: "Concurrency", status: "live", page: "claim-week-16.html",
          date: "Jun 21, 2028" },
        { n: 17, title: "Pacing — the delay that answers another delay",
          short: "Pacing", status: "live", page: "claim-week-17.html",
          date: "Jun 28, 2028" },
        { n: 18, title: "Acceleration and mitigation — directed, constructive and unpaid",
          short: "Acceleration and mitigation", status: "live", page: "claim-week-18.html",
          date: "Jul 5, 2028" },

        // ---- PHASE E — DISRUPTION ----
        { phase: "Phase E — Disruption", n: 19,
          title: "Disruption — the loss that never touches the critical path",
          short: "Disruption", status: "live", page: "claim-week-19.html",
          date: "Jul 12, 2028" },
        { n: 20, title: "The measured mile — comparing the job to itself",
          short: "The measured mile", status: "live", page: "claim-week-20.html",
          date: "Jul 19, 2028" },
        { n: 21, title: "Productivity loss — the methods used when no clean mile exists",
          short: "Productivity loss", status: "live", page: "claim-week-21.html",
          date: "Jul 26, 2028" },
        { n: 22, title: "Global and total cost claims — why they fail",
          short: "Global and total cost claims", status: "live", page: "claim-week-22.html",
          date: "Aug 2, 2028" },

        // ---- PHASE F — QUANTUM ----
        { phase: "Phase F — Quantum", n: 23,
          title: "Prolongation — the cost of time on site",
          short: "Prolongation", status: "live", page: "claim-week-23.html",
          date: "Aug 9, 2028" },
        { n: 24, title: "Head office overhead and finance — the formulae and their weaknesses",
          short: "Head office and finance", status: "live", page: "claim-week-24.html",
          date: "Aug 16, 2028" },
        { n: 25, title: "Pricing and substantiation — from cost records to a number",
          short: "Pricing and substantiation", status: "live", page: "claim-week-25.html",
          date: "Aug 23, 2028" },

        // ---- PHASE G — PRESENTING THE CLAIM ----
        { phase: "Phase G — Presenting the Claim", n: 26,
          title: "Assembling a claim — contents, executive summary and appendices",
          short: "Assembling a claim", status: "live", page: "claim-week-26.html",
          date: "Aug 30, 2028" },
        { n: 27, title: "Defending a claim — reading one from the other side",
          short: "Defending a claim", status: "live", page: "claim-week-27.html",
          date: "Sep 6, 2028" },
        { n: 28, title: "What five tracks were for — the claim that never happened",
          short: "What five tracks were for", status: "live", page: "claim-week-28.html",
          date: "Sep 13, 2028" }
    ],
    get liveCount() { return this.weeks.filter(w => w.status === "live").length; },
    get progressPercent() { return Math.round((this.liveCount / this.totalWeeks) * 100); },
    get latestLiveWeek() {
        const live = this.weeks.filter(w => w.status === "live");
        return live.length ? live[live.length - 1] : null;
    },
    get phaseCount() { return this.weeks.filter(w => w.phase).length; },
    getWeek(n) { return this.weeks.find(w => w.n === n); }
};

function renderTrack5Curriculum() { return learnCurriculumHTML(TRACK5); }
function renderTrack5Sidebar(currentWeek) { return sidebarHTML(TRACK5, currentWeek); }
function renderHomeTrack5()               { return homeCurriculumHTML(TRACK5); }
function renderHomeTrack5Badge() {
  return badgeText(TRACK5);
}

function renderTrack5Progress() {
    return { text: `${TRACK5.liveCount} of ${TRACK5.totalWeeks} published`, percent: TRACK5.progressPercent };
}

// Renderer: Track 3 curriculum for learn.html
// NOTE: must use the SAME classes as renderLearnCurriculum above,
// or the rows render as unstyled plain text.
function renderTrack3Curriculum() {
  const t = TRACK3;
  let rows = "";
  t.weeks.forEach((week, idx) => {
    if (week.phase) {
      let end = week.n;
      for (let j = idx + 1; j < t.weeks.length; j++) {
        if (t.weeks[j].phase) break;
        end = t.weeks[j].n;
      }
      const range = week.n === end ? `Week ${week.n}` : `Weeks ${week.n}\u2013${end}`;
      rows += `
        <div class="phase-divider">
          <span class="phase-label" translate="no">${week.phase.toUpperCase()}</span>
          <span class="phase-weeks-tag">${range}</span>
        </div>`;
    }
    if (week.status === "live" && week.page) {
      const isLatest = week === t.latestLiveWeek;
      const dateOrNew = isLatest
        ? '<span class="week-new" translate="no">New</span>'
        : (week.date ? `<span class="week-date">${week.date}</span>` : '');
      rows += `
        <a href="${week.page}" class="week-item">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          ${dateOrNew}
          <i class='bx bx-right-arrow-alt week-arrow'></i>
        </a>`;
    } else {
      rows += `
        <div class="week-item upcoming">
          <span class="week-num">Week ${week.n}</span>
          <span class="week-title">${week.title}</span>
          <span class="week-upcoming-label">Coming soon</span>
        </div>`;
    }
  });
  return rows;
}

// Progress bar values for the Track 3 card on learn.html
function renderTrack3Progress() {
  const t = TRACK3;
  return {
    text: `${t.liveCount} of ${t.totalWeeks} published`,
    percent: t.progressPercent
  };
}

// Sidebar for Track 3 article pages. Mirrors renderTrack2Sidebar.

// Renderer: Track 3 post list for the home page module card.

// Module badge text for the Track 3 card on home
function renderHomeTrack3Badge() {
  return badgeText(TRACK3);
}


/* Yan panel artık tüm track'i gösteriyor (27/24/18 satır). Okur 13. haftadaysa
   listenin başında değil, kendi haftasında açılmalı. Bu blok curriculum.js'in
   sonunda duruyor ama DOMContentLoaded'i dinlediği için sayfanın kendi render
   çağrısından SONRA çalışır; 69 makaleyi düzenlemeye gerek kalmıyor. */
(function () {
  function centreActiveWeek() {
    var boxes = document.querySelectorAll('.sidebar-scroll');
    for (var i = 0; i < boxes.length; i++) {
      var box = boxes[i];
      var active = box.querySelector('.sidebar-series-item.active');
      if (!active) continue;
      var target = active.offsetTop - box.offsetTop
                 - (box.clientHeight / 2) + (active.offsetHeight / 2);
      box.scrollTop = target > 0 ? target : 0;
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', centreActiveWeek);
  } else {
    centreActiveWeek();
  }
})();


/* Ana sayfa müfredat kartlarını yerinde açar. Olay delegasyonu kullanıyor:
   düğmeler render'dan sonra DOM'a giriyor, doğrudan bağlamak yarış koşulu olurdu. */
document.addEventListener('click', function (e) {
  var btn = e.target.closest && e.target.closest('.module-post-more');
  if (!btn) return;
  var rest = btn.previousElementSibling;
  if (!rest || !rest.classList.contains('module-post-rest')) return;
  var isOpen = btn.getAttribute('aria-expanded') === 'true';
  rest.hidden = isOpen;
  btn.setAttribute('aria-expanded', String(!isOpen));
  btn.querySelector('.post-title').textContent =
    isOpen ? btn.getAttribute('data-more') : btn.getAttribute('data-less');
  btn.querySelector('.post-week').textContent =
    isOpen ? btn.getAttribute('data-count') : '';
});
