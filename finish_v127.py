#!/usr/bin/env python3
"""v126 -> v127 finishing pass.

Assumes curriculum.js, learn.html and start-here.html are already in place
(add_start_here.py and add_track6_lifecycle.py). This handles the rest:

  1. index.html  — module 06 becomes Interfaces, module 07 is added,
                   both wired to curriculum.js, plus a Start Here link
  2. sitemap.xml — start-here.html
  3. cache       — curriculum.js?v=123 -> ?v=124 across every page

Idempotent: run twice, second run reports 0 dosya.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_V, NEW_V = 123, 124

# --------------------------------------------------------------------------

INDEX_CARDS = '''                <div class="module-track module-track-locked">
                    <div class="module-track-header">
                        <div class="module-track-left">
                            <span class="module-number locked">06</span>
                            <div>
                                <h3 class="module-title">Interfaces</h3>
                                <p class="module-desc">Five tracks taught the job as one contract with one chain of command. What happens when that stops being true &#8212; delivery models and who holds the scope, EPCM authority without a contract, the critical path through a purchase order, the work between two programmes, and the number with more than one owner.</p>
                            </div>
                        </div>
                        <span class="module-status locked-status" id="homeTrack6Badge"><i class='bx bx-map-alt'></i> On the roadmap</span>
                    </div>
                </div>

                <div class="module-track module-track-locked">
                    <div class="module-track-header">
                        <div class="module-track-left">
                            <span class="module-number locked">07</span>
                            <div>
                                <h3 class="module-title">The Life of a Project</h3>
                                <p class="module-desc">Everything above answers how. This answers when, why and with whom &#8212; one EPC job from the investment decision to the handover certificate, the order the work arrives in, what feeds what, and which record is born where.</p>
                            </div>
                        </div>
                        <span class="module-status locked-status" id="homeTrackLCBadge"><i class='bx bx-map-alt'></i> On the roadmap</span>
                    </div>
                </div>
'''

INDEX_WIRING = '''
            // Roadmap badges computed from curriculum.js, never typed
            [['homeTrack6Badge', typeof TRACK6 !== 'undefined' ? TRACK6 : null],
             ['homeTrackLCBadge', typeof LIFECYCLE !== 'undefined' ? LIFECYCLE : null]].forEach(function (p) {
                var el = document.getElementById(p[0]), t = p[1];
                if (!el || !t) return;
                el.innerHTML = t.liveCount === 0
                    ? "<i class='bx bx-map-alt'></i> On the roadmap \\u00b7 " + t.totalWeeks + " weeks"
                    : '<span class="dot-green"></span> Week ' + t.latestLiveWeek.n + ' of ' + t.totalWeeks;
            });
'''


def patch_index():
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    orig = s

    # a. replace the single module 06 roadmap card with two wired cards
    if 'id="homeTrack6Badge"' not in s:
        start = s.index('                <div class="module-track module-track-locked">\n'
                        '                    <div class="module-track-header">\n'
                        '                        <div class="module-track-left">\n'
                        '                            <span class="module-number locked">06</span>')
        end = s.index('                <div class="group-divider">', start)
        s = s[:start] + INDEX_CARDS + "\n" + s[end:]

    # b. wiring
    if "homeTrack6Badge'" not in s.split("</body>")[0].split("<script>")[-1]:
        anchor = "            const liveBadge = document.getElementById('homeLiveBadge');"
        if anchor in s and "Roadmap badges computed" not in s:
            s = s.replace(anchor, INDEX_WIRING + "\n" + anchor, 1)

    # c. Start Here link above the curriculum
    if "start-here.html" not in s:
        m = re.search(r'(<div class="group-divider">\s*<span class="group-label">)', s)
        if m:
            link = ('                <a href="start-here.html" class="home-start-here">'
                    "<i class='bx bx-compass'></i> New here? Start with the ten-minute orientation "
                    "<i class='bx bx-right-arrow-alt'></i></a>\n\n")
            s = s[:m.start()] + link + s[m.start():]
            css = """
        .home-start-here {
            display: inline-flex; align-items: center; gap: 9px;
            padding: 11px 18px; margin-bottom: 26px;
            background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 10px;
            font-size: 14px; font-weight: 600; color: #047857; text-decoration: none;
        }
        .home-start-here:hover { background: #d1fae5; }
    </style>"""
            s = s.replace("    </style>", css, 1)

    if s != orig:
        p.write_text(s, encoding="utf-8")
        print("  + index.html: 06/07 kartlari, wiring, Start Here linki")
        return 1
    print("  = index.html: degisiklik yok")
    return 0


def patch_sitemap():
    p = ROOT / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    if "start-here.html" in s:
        print("  = sitemap.xml: degisiklik yok")
        return 0
    entry = ("  <url>\n"
             "    <loc>https://theprojectcontrolhub.com/start-here.html</loc>\n"
             "    <lastmod>2026-07-31</lastmod>\n"
             "  </url>\n")
    s = s.replace("</urlset>", entry + "</urlset>")
    p.write_text(s, encoding="utf-8")
    print("  + sitemap.xml: start-here.html")
    return 1


def bump_cache():
    """Direct write. Not routed through any build helper — NOTES.md section 6."""
    n = 0
    for f in sorted(ROOT.glob("*.html")):
        s = f.read_text(encoding="utf-8")
        t = s.replace(f"curriculum.js?v={OLD_V}", f"curriculum.js?v={NEW_V}")
        if t != s:
            f.write_text(t, encoding="utf-8")
            n += 1
    print(f"  {'+' if n else '='} cache: v{OLD_V} -> v{NEW_V} ({n} sayfa)")
    return 1 if n else 0


def main():
    written = patch_index() + patch_sitemap() + bump_cache()
    print(f"\n{written} adim")


if __name__ == "__main__":
    main()
