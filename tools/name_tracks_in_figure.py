#!/usr/bin/env python3
"""Names the tracks in the path figure and turns each step into a link.

The first step read "117 lessons · complete / The methods", which does not say
which methods. It now names all five tracks and links each one to its section,
so the figure doubles as navigation rather than being decoration above a nav
bar that repeats it.

Counts stay computed from curriculum.js. Track names are names, not statuses,
so they are written out.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_FIGURE_START = '            <ol class="path-figure" aria-label="How the curriculum builds">'
OLD_FIGURE_END = "            </ol>\n"

NEW_FIGURE = '''            <ol class="path-figure" aria-label="How the curriculum builds">
                <li class="path-step is-done">
                    <span class="path-dot"><i class='bx bx-check'></i></span>
                    <span class="path-kicker">Tracks 1&#8211;5 &#183; <b id="pfDone">117</b> lessons</span>
                    <strong class="path-title"><a href="#track-1">The methods</a></strong>
                    <span class="path-out">Build a programme, price it, keep the right when it slips, and prove the delay.</span>
                    <span class="path-tracks">
                        <a href="#track-1">Schedule</a><a href="#track-2">Cost &amp; Cash</a><a href="#track-3">Risk</a><a href="#track-4">Contract</a><a href="#track-5">Claims</a>
                    </span>
                </li>
                <li class="path-step is-next">
                    <span class="path-dot"></span>
                    <span class="path-kicker">Track 6 &#183; <b id="pfT6">14</b> weeks &#183; next</span>
                    <strong class="path-title"><a href="#track-6">Interfaces</a></strong>
                    <span class="path-out">Do all of that when the job has more than one contract and no single chain of command.</span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker"><b id="pfLC">52</b> weeks</span>
                    <strong class="path-title"><a href="#lifecycle">The life of a project</a></strong>
                    <span class="path-out">Know when each method is needed, who feeds you the numbers, and which record it produces.</span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker">After the writing</span>
                    <strong class="path-title"><a href="#toolbox">The tools</a></strong>
                    <span class="path-out">Excel, Primavera, Power BI &#8212; last, because a tool you cannot reason about is worth nothing.</span>
                </li>
            </ol>
'''

EXTRA_CSS = '''
        .path-title a { color: inherit; text-decoration: none; }
        .path-title a:hover { color: #059669; }
        .path-tracks { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 8px; }
        .path-tracks a {
            font-size: 10.5px; font-weight: 600; color: #475569;
            background: #fff; border: 1px solid #e2e8f0; border-radius: 5px;
            padding: 2px 6px; text-decoration: none; white-space: nowrap;
        }
        .path-tracks a:hover { border-color: #10b981; color: #059669; }
    </style>'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "path-tracks" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return
    if OLD_FIGURE_START not in s:
        sys.exit("HATA: path figure bulunamadi. once add_path_figure.py")

    i = s.index(OLD_FIGURE_START)
    j = s.index(OLD_FIGURE_END, i) + len(OLD_FIGURE_END)
    s = s[:i] + NEW_FIGURE + s[j:]

    s = s.replace("    </style>", EXTRA_CSS, 1)

    p.write_text(s, encoding="utf-8")
    print("  + learn.html: track adlari ve baglantilar eklendi\n\n1 dosya")


if __name__ == "__main__":
    main()
