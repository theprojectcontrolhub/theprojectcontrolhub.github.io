#!/usr/bin/env python3
"""Removes the roadmap block from learn.html.

It said the same thing three times on one page. The path figure at the top
already carries "the tools come last" as step four, and the Toolbox section
directly below repeats it in its own note. The only unique content in the
block was a Simulation card that nothing on the site commits to yet, so it
goes rather than sitting there as a promise.

The #roadmap anchor loses its last reference at the same time; no page links
to it and the jump nav chip was removed earlier. The roadmap-* CSS is left in
place, unused but harmless, in case a roadmap card is wanted again later.

Idempotent.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

START = '                    <div class="roadmap-section" id="roadmap">'
END = "                <!-- ===== SECTION: THE TOOLBOX ===== -->"


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if START not in s:
        print("  = learn.html: roadmap bolumu zaten yok\n\n0 dosya")
        return

    i = s.index(START)
    j = s.index(END, i)
    removed = j - i
    s = s[:i] + s[j:]

    # the anchor no longer exists, so drop it from the scroll-offset rule
    s = s.replace(
        "#track-1, #track-2, #track-3, #track-4, #track-5, #track-6, #lifecycle, #roadmap, #toolbox { scroll-margin-top: 132px; }",
        "#track-1, #track-2, #track-3, #track-4, #track-5, #track-6, #lifecycle, #toolbox { scroll-margin-top: 132px; }",
        1)

    p.write_text(s, encoding="utf-8")
    print(f"  - learn.html: roadmap bolumu kaldirildi ({removed} karakter)\n\n1 dosya")


if __name__ == "__main__":
    main()
