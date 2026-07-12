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
    { n: 17, title: "Model health — constraints, open ends, out-of-sequence logic", short: "Model health — constraints, OOS logic", status: "upcoming" },
    { n: 18, title: "EVM fundamentals — PMB, PV, EV, AC", short: "EVM fundamentals — PMB, PV, EV, AC", status: "upcoming" },
    { n: 19, title: "EVM analysis — SPI, CPI & variance interpretation", short: "EVM analysis — SPI, CPI, variance", status: "upcoming" },
    { n: 20, title: "Forecasting — EAC, ETC, TCPI & Earned Schedule", short: "Forecasting — EAC, ETC, Earned Schedule", status: "upcoming" },
    { n: 21, title: "Change control & protecting the baseline", short: "Change control & baseline protection", status: "upcoming" },
    { n: 22, title: "The control philosophy — telemetry & managing variances", short: "Control philosophy — telemetry", status: "upcoming" },
    { n: 23, title: "Project reviews & the Conformance Index", short: "Project reviews & Conformance Index", status: "upcoming" },

    // ---- PHASE E — CLOSEOUT & FORENSICS · DOMAIN 4 ----
    { phase: "Phase E — Closeout & Forensics", n: 24, title: "Forensic schedule analysis — delays, claims, evidence", short: "Forensic schedule analysis — claims", status: "upcoming" },
    { n: 25, title: "Closeout & continuous closeout — capturing the data", short: "Closeout & continuous closeout", status: "upcoming" },

    // ---- PHASE F — COMMUNICATION · DOMAIN 5 ----
    { phase: "Phase F — Communication", n: 26, title: "Reporting & the altitude concept — right data, right level", short: "Reporting & the altitude concept", status: "upcoming" },
    { n: 27, title: "Stakeholder management & schedule communication", short: "Stakeholder management & communication", status: "upcoming" },
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
function renderArticleSidebar(currentWeek) {
  const w = CURRICULUM;
  let rows = "";
  // Show first ~5 weeks + a summary row, or all if you prefer.
  const visible = w.weeks.slice(0, 5);
  visible.forEach(week => {
    const isActive = week.n === currentWeek;
    const isLive = week.status === "live";
    const isLatest = week === w.latestLiveWeek;
    const badge = isLatest && !isActive
      ? '<span class="sidebar-new" translate="no">New</span>' : "";

    if (isActive) {
      rows += `
        <a href="${week.page || '#'}" class="sidebar-series-item active">
          <span class="sidebar-week">Week ${week.n}</span>
          <span class="sidebar-item-title">${week.short}</span>
        </a>`;
    } else if (isLive) {
      rows += `
        <a href="${week.page}" class="sidebar-series-item">
          <span class="sidebar-week">Week ${week.n}</span>
          <span class="sidebar-item-title">${week.short}</span>${badge}
        </a>`;
    } else {
      // upcoming but shown as a gated/soon link if it has a target page,
      // otherwise a dead greyed row
      if (week.page) {
        rows += `
          <a href="${week.page}" class="sidebar-series-item" data-gated>
            <span class="sidebar-week">Week ${week.n}</span>
            <span class="sidebar-item-title">${week.short}</span>${badge}
          </a>`;
      } else {
        rows += `
          <div class="sidebar-series-item upcoming">
            <span class="sidebar-week">Week ${week.n}</span>
            <span class="sidebar-item-title">${week.short}</span>
          </div>`;
      }
    }
  });

  // summary row for the rest
  const remaining = w.weeks.length - visible.length;
  if (remaining > 0) {
    const firstRest = visible.length + 1;
    rows += `
      <div class="sidebar-series-item upcoming">
        <span class="sidebar-week">${firstRest}–${w.totalWeeks}</span>
        <span class="sidebar-item-title">Development · CPM · EVM · Forensics · Reporting</span>
      </div>`;
  }

  return `
    <div class="sidebar-card-header">
      <h4 translate="no">${w.moduleTitle} · ${w.totalWeeks} Weeks</h4>
    </div>${rows}`;
}

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
  const w = CURRICULUM;
  const live = w.weeks.filter(x => x.status === "live").slice(-3);
  let html = "";
  live.forEach(week => {
    const isLatest = week === w.latestLiveWeek;
    const badge = isLatest
      ? '<span class="home-new-pill" translate="no">New</span>' : '';
    html += `
      <a href="${week.page}" class="discussion-list-item module-post-item">
        <span class="category-text text-green">WEEK ${week.n} · SCHEDULE</span>
        <h4>${week.short}</h4>
        <div class="item-meta">
          ${week.date ? `<span class="home-date">${week.date}</span>` : ''}
          ${badge}
          <i class='bx bx-right-arrow-alt arrow-icon'></i>
        </div>
      </a>`;
  });
  return html;
}

// Home page — Module 01 curriculum card (compact, no phase dividers)
// Shows live weeks as links + first few upcoming, then a summary row.
function renderHomeCurriculum() {
  const w = CURRICULUM;
  let rows = "";
  const live = w.weeks.filter(x => x.status === "live");
  const upcoming = w.weeks.filter(x => x.status === "upcoming");

  // all live weeks
  live.forEach(week => {
    const isLatest = week === w.latestLiveWeek;
    const badge = isLatest ? '<span class="new-badge" translate="no">New</span>' : '';
    rows += `
      <a href="${week.page}" class="module-post-item">
        <span class="post-week">Week ${week.n}</span>
        <span class="post-title">${week.short}</span>
        ${week.date ? `<span class="post-date">${week.date}</span>` : ''}
        ${badge}
        <i class='bx bx-right-arrow-alt'></i>
      </a>`;
  });

  // next 2 upcoming (with a page target = gated links)
  const nextUp = upcoming.slice(0, 2);
  nextUp.forEach(week => {
    if (week.page) {
      const badge = week.new ? '<span class="new-badge" translate="no">New</span>' : '';
      rows += `
        <a href="${week.page}" class="module-post-item" data-gated>
          <span class="post-week">Week ${week.n}</span>
          <span class="post-title">${week.short}</span>
          ${badge}
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

  // summary row for the rest
  const shown = live.length + nextUp.length;
  const restStart = w.weeks[shown] ? w.weeks[shown].n : null;
  if (restStart) {
    rows += `
      <div class="module-post-item upcoming">
        <span class="post-week">Week ${restStart}\u2013${w.totalWeeks}</span>
        <span class="post-title">Development · CPM · EVM · Change Control · Forensics · Reporting</span>
        <span class="post-upcoming">Coming soon</span>
      </div>`;
  }
  return rows;
}

// Module badge text for home
function renderHomeBadge() {
  const latest = CURRICULUM.latestLiveWeek;
  return latest
    ? `<span class="dot-green"></span> In Progress · Week ${latest.n} of ${CURRICULUM.totalWeeks}`
    : '';
}
