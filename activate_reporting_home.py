#!/usr/bin/env python3
"""Turns the Reporting card on index.html from a roadmap card into a live one.

learn.html was fixed by curriculum.js alone, because the whole week list there
is generated. The home page is not: each track card carries its locked state
in the markup, and the week list needs a container and a wiring block. So the
card went on saying "on the roadmap" after the track went live, and the badge
read "Week 26 of 26" rather than "Complete", because the roadmap wiring never
expected a finished track.

Four things, matching how cards 01 to 05 are built:

  1. the three locked classes come off
  2. a module-posts container is added so the week list has somewhere to go
  3. renderHomeTrack6 / renderHomeTrack6Badge added to curriculum.js
  4. the card is wired in index.html the same way track 5 is

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RENDERS = '''function renderHomeTrack6()       { return homeCurriculumHTML(TRACK6); }
function renderHomeTrack6Badge()  { return badgeText(TRACK6); }
'''

WIRING = '''
            const t6 = document.getElementById('homeTrack6');
            if (t6 && typeof renderHomeTrack6 === 'function') {
                t6.innerHTML = renderHomeTrack6();
            }
            const t6Badge = document.getElementById('homeTrack6Badge');
            if (t6Badge && typeof renderHomeTrack6Badge === 'function') {
                t6Badge.innerHTML = renderHomeTrack6Badge();
            }
'''


def patch_curriculum():
    p = ROOT / "curriculum.js"
    s = p.read_text(encoding="utf-8")
    if "renderHomeTrack6" in s:
        print("  = curriculum.js: zaten uygulanmis")
        return 0
    anchor = "function renderTrack6Curriculum()"
    if anchor not in s:
        sys.exit("HATA: curriculum.js icinde TRACK6 render blogu bulunamadi")
    s = s.replace(anchor, RENDERS + anchor, 1)
    p.write_text(s, encoding="utf-8")
    print("  + curriculum.js: renderHomeTrack6 eklendi")
    return 1


def patch_index():
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    before = s

    if 'id="homeTrack6"' not in s:
        i = s.index("<!-- TRACK 6: THE ASSUMPTIONS THAT STOP HOLDING -->")
        j = s.index('<div class="module-track module-track-locked">', i)
        k = s.index('<span class="module-status locked-status" id="homeTrack6Badge">', j)
        end = s.index("</div>\n", s.index("</span>", k)) + len("</div>\n")
        card = s[j:end]

        card = card.replace('<div class="module-track module-track-locked">',
                            '<div class="module-track">', 1)
        card = card.replace('<span class="module-number locked">06</span>',
                            '<span class="module-number">06</span>', 1)
        card = card.replace(
            '<span class="module-status locked-status" id="homeTrack6Badge">'
            "<i class='bx bx-map-alt'></i> On the roadmap</span>",
            '<span class="module-status" id="homeTrack6Badge">'
            '<span class="dot-green"></span> Complete &#183; 26 weeks</span>', 1)
        # the week list container, as on every published card
        card = card.rstrip("\n")
        card += '\n                    <div class="module-posts" id="homeTrack6"></div>\n'
        s = s[:j] + card + s[end:]
        s = s.replace("<!-- TRACK 6: THE ASSUMPTIONS THAT STOP HOLDING -->",
                      "<!-- TRACK 6: REPORTING -->", 1)

    # the roadmap badge script no longer owns this card
    s = s.replace("[['homeTrack6Badge', typeof TRACK6 !== 'undefined' ? TRACK6 : null],\n"
                  "             ['homeTrack7Badge', typeof TRACK7 !== 'undefined' ? TRACK7 : null],",
                  "[['homeTrack7Badge', typeof TRACK7 !== 'undefined' ? TRACK7 : null],", 1)

    if "const t6 = document.getElementById('homeTrack6')" not in s:
        anchor = "            const t5Badge = document.getElementById('homeTrack5Badge');"
        i = s.index(anchor)
        j = s.index("            }\n", s.index("renderHomeTrack5Badge();", i)) + len("            }\n")
        s = s[:j] + WIRING + s[j:]

    if s != before:
        p.write_text(s, encoding="utf-8")
        print("  + index.html: 06 kilidi acildi ve baglandi")
        return 1
    print("  = index.html: degisiklik yok")
    return 0


def main():
    n = patch_curriculum() + patch_index()
    print(f"\n{n} dosya")


if __name__ == "__main__":
    main()
