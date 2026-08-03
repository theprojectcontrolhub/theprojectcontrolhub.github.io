#!/usr/bin/env python3
"""Adds a four-step path figure between the header and the jump nav.

The page currently states the shape of the curriculum in prose and then drops
the reader straight into a 27-week list. This puts the argument on one line of
sight: what you learn, in what order, and what you can do after each stage.

All counts are read from curriculum.js at runtime. Nothing here is typed.

Idempotent.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIGURE = '''
            <ol class="path-figure" aria-label="How the curriculum builds">
                <li class="path-step is-done">
                    <span class="path-dot"><i class='bx bx-check'></i></span>
                    <span class="path-kicker"><b id="pfDone">117</b> lessons &#183; complete</span>
                    <strong class="path-title">The methods</strong>
                    <span class="path-out">Build a programme, price it, keep the right when it slips, and prove the delay.</span>
                </li>
                <li class="path-step is-next">
                    <span class="path-dot"></span>
                    <span class="path-kicker"><b id="pfT6">14</b> weeks &#183; next</span>
                    <strong class="path-title">Interfaces</strong>
                    <span class="path-out">Do all of that when the job has more than one contract and no single chain of command.</span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker"><b id="pfLC">52</b> weeks</span>
                    <strong class="path-title">The life of a project</strong>
                    <span class="path-out">Know when each method is needed, who feeds you the numbers, and which record it produces.</span>
                </li>
                <li class="path-step">
                    <span class="path-dot"></span>
                    <span class="path-kicker">after the writing</span>
                    <strong class="path-title">The tools</strong>
                    <span class="path-out">Excel, Primavera, Power BI &#8212; last, because a tool you cannot reason about is worth nothing.</span>
                </li>
            </ol>
'''

CSS = '''
        /* ===== PATH FIGURE =====
           Four stages, left to right, above the jump nav. Counts come from
           curriculum.js so the figure cannot drift from the lists below it. */
        .path-figure {
            list-style: none; margin: 22px 0 6px; padding: 0;
            display: grid; grid-template-columns: repeat(4, 1fr); gap: 0 18px;
            position: relative;
        }
        .path-figure::before {
            content: ''; position: absolute; top: 9px;
            left: 12.5%; right: 12.5%; height: 2px;
            background: linear-gradient(to right, #10b981 0 25%, #cbd5e1 25%);
            border-radius: 2px;
        }
        .path-step { position: relative; display: flex; flex-direction: column; }
        .path-dot {
            width: 20px; height: 20px; border-radius: 50%;
            background: #fff; border: 2px solid #cbd5e1;
            display: flex; align-items: center; justify-content: center;
            margin-bottom: 12px; position: relative; z-index: 1;
        }
        .path-step.is-done .path-dot { background: #10b981; border-color: #10b981; }
        .path-step.is-done .path-dot i { font-size: 13px; color: #fff; }
        .path-step.is-next .path-dot { border-color: #10b981; box-shadow: 0 0 0 4px rgba(16,185,129,0.12); }
        .path-kicker {
            font-size: 10.5px; font-weight: 700; letter-spacing: 0.07em;
            text-transform: uppercase; color: #94a3b8; margin-bottom: 4px;
        }
        .path-step.is-done .path-kicker, .path-step.is-next .path-kicker { color: #059669; }
        .path-kicker b { font-weight: 800; }
        .path-title {
            font-size: 15px; font-weight: 700; color: #1e293b;
            line-height: 1.3; margin-bottom: 5px;
        }
        .path-out { font-size: 12.5px; line-height: 1.5; color: #64748b; }
        @media (max-width: 720px) {
            .path-figure {
                grid-template-columns: 1fr; gap: 16px 0;
                margin: 18px 0 4px; padding-left: 30px;
            }
            .path-figure::before {
                top: 6px; bottom: 10px; left: 9px; right: auto;
                width: 2px; height: auto;
                background: linear-gradient(to bottom, #10b981 0 25%, #cbd5e1 25%);
            }
            .path-step { display: block; }
            .path-dot { position: absolute; left: -30px; top: 0; margin: 0; }
            .path-title { display: block; margin-top: 1px; }
            .path-out { display: block; margin-top: 3px; }
        }
    </style>'''

WIRING = '''
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
                if (typeof LIFECYCLE !== 'undefined') set('pfLC', LIFECYCLE.totalWeeks);
            })();
'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "path-figure" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return

    anchor = '                <nav class="track-jump"'
    if anchor not in s:
        sys.exit("HATA: track-jump bulunamadi")
    s = s.replace(anchor, FIGURE + "\n" + anchor, 1)

    if "    </style>" not in s:
        sys.exit("HATA: style blogu bulunamadi")
    s = s.replace("    </style>", CSS, 1)

    wire_anchor = "            // Fill weeks"
    if wire_anchor not in s:
        sys.exit("HATA: wiring noktasi bulunamadi")
    s = s.replace(wire_anchor, WIRING + "\n" + wire_anchor, 1)

    p.write_text(s, encoding="utf-8")
    print("  + learn.html: path figure eklendi\n\n1 dosya")


if __name__ == "__main__":
    main()
