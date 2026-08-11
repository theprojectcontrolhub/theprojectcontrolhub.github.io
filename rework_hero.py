#!/usr/bin/env python3
"""Reworks the first screen of index.html.

Four changes, in order of how much they matter to somebody who has been on
the page for five seconds:

  1. The paragraph under the headline described the author. A first-time
     reader is asking what the site is, not who wrote it. Now it answers
     that first and the credentials follow, which is also where they carry
     more weight.

  2. 143 lessons and six finished tracks are the strongest evidence the site
     has and they were in a small badge in the right-hand column. They move
     under the headline as three figures, read from curriculum.js.

  3. "Start from Week 1" was the primary action. Week 1 is the first of 143
     lessons, which is a lot to ask of somebody who does not yet know
     whether this is for them. Start Here is written for exactly that
     moment and was a small link further down the page.

  4. Module descriptions ran from two lines to five. Eight cards in a column
     made the unevenness obvious. Each is cut to its first sentence.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_P = """                <p class="hero-desc">
                    I'm a Planning & Project Controls Lead with years on large-scale construction and engineering projects — including nuclear. I write and teach for engineers who want to understand project controls the way it actually works on site, not just in textbooks.
                </p>"""

NEW_P = """                <p class="hero-desc">
                    A written curriculum in project controls, for engineers who want to understand the job the way it works on site rather than the way it is described in a textbook. Schedule, cost, risk, contract, claims and reporting — one lesson a week, in order, free.
                </p>
                <p class="hero-desc hero-desc-sub">
                    Written by a Planning &amp; Project Controls Lead with eight years on nuclear, mining, port and high-rise projects.
                </p>
                <div class="hero-stats" id="heroStats">
                    <span><b id="hsLessons">143</b> lessons</span>
                    <span><b id="hsTracks">6</b> tracks complete</span>
                    <span><b>Weekly</b> since 2026</span>
                </div>"""

OLD_BTN = """                    <a href="week-1.html" class="btn btn-primary-large"><i class='bx bx-play'></i> Start from Week 1</a>
                    <a href="about.html" class="btn btn-ghost-large"><i class='bx bx-user'></i> About Me</a>"""

NEW_BTN = """                    <a href="start-here.html" class="btn btn-primary-large"><i class='bx bx-compass'></i> Start here</a>
                    <a href="week-1.html" class="btn btn-ghost-large"><i class='bx bx-play'></i> Straight to Week 1</a>"""

CSS = """
        /* The credentials line sits under the description rather than in
           place of it: what the site is, then who wrote it. */
        .hero-desc-sub {
            font-size: 14.5px; opacity: 0.75; margin-top: -6px;
        }
        /* The evidence the site actually has, on the first screen instead of
           in a badge in the right-hand column. Read from curriculum.js. */
        .hero-stats {
            display: flex; flex-wrap: wrap; gap: 10px 26px;
            margin: 20px 0 6px; font-size: 14px; opacity: 0.85;
        }
        .hero-stats b { font-weight: 800; color: #34d399; margin-right: 4px; }
        @media (max-width: 640px) {
            .hero-stats { gap: 8px 18px; font-size: 13px; }
        }
"""

WIRING = """
            // Hero figures are read, not typed. Every other count on this
            // site that was typed has gone stale at least once.
            (function () {
                if (typeof allTracks !== 'function') return;
                var s = function (id, v) { var e = document.getElementById(id); if (e) e.textContent = v; };
                s('hsLessons', typeof liveLessonCount === 'function' ? liveLessonCount() : '');
                s('hsTracks', allTracks().filter(function (p) {
                    return p[0].liveCount > 0 && p[0].liveCount >= p[0].totalWeeks;
                }).length);
            })();
"""


def trim_descriptions(s):
    """First sentence only. Eight cards in a column need the same weight."""
    n = 0

    def cut(m):
        nonlocal n
        body = m.group(1)
        if "<" in body:
            return m.group(0)
        parts = re.split(r"(?<=[.!?])\s+", body.strip())
        if len(parts) < 2:
            return m.group(0)
        first = parts[0]
        # a one-clause opener on its own is too thin; keep two in that case
        if len(first.split()) < 9 and len(parts) > 2:
            first = first + " " + parts[1]
        n += 1
        return f'<p class="module-desc">{first}</p>'

    s = re.sub(r'<p class="module-desc">([^<]+)</p>', cut, s)
    return s, n


def main():
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    if 'id="heroStats"' in s:
        print("  = index.html: zaten uygulanmis\n\n0 dosya")
        return

    for old, new, label in ((OLD_P, NEW_P, "hero paragrafi"), (OLD_BTN, NEW_BTN, "hero butonlari")):
        if old not in s:
            sys.exit(f"HATA: {label} beklenen halde bulunamadi")
        s = s.replace(old, new, 1)

    if "    </style>" not in s:
        sys.exit("HATA: style blogu bulunamadi")
    s = s.replace("    </style>", CSS + "    </style>", 1)

    anchor = "            const liveBadge = document.getElementById('homeLiveBadge');"
    if anchor not in s:
        sys.exit("HATA: wiring noktasi bulunamadi")
    s = s.replace(anchor, WIRING + "\n" + anchor, 1)

    s, n = trim_descriptions(s)

    p.write_text(s, encoding="utf-8")
    print(f"  + hero paragrafi ve kunye ayrildi")
    print(f"  + ilk ekrana uc sayi eklendi (hesaplanan)")
    print(f"  + Start here birincil buton oldu")
    print(f"  + kisaltilan modul aciklamasi: {n}")
    print("\n1 dosya")


if __name__ == "__main__":
    main()
