#!/usr/bin/env python3
"""Turns the flat sub-lists in the path figure into connected milestone chains.

Small flat pills read as tags. Boxes joined by a connector read as a route,
which is what the figure is actually claiming: this, then this, then this.
The completed column is filled green, the next one is outlined green, the rest
are neutral, so the state of the whole curriculum is legible before a word is
read.

Week counts on the first column come from curriculum.js.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHAINS = {
    1: '''                    <span class="path-chain">
                        <a class="chain-box" href="#track-1">Schedule <b id="cb1">27</b></a>
                        <a class="chain-box" href="#track-2">Cost &amp; Cash <b id="cb2">24</b></a>
                        <a class="chain-box" href="#track-3">Risk <b id="cb3">18</b></a>
                        <a class="chain-box" href="#track-4">Contract <b id="cb4">20</b></a>
                        <a class="chain-box" href="#track-5">Claims <b id="cb5">28</b></a>
                    </span>
''',
    2: '''                    <span class="path-chain">
                        <span class="chain-box">Delivery models</span>
                        <span class="chain-box">EPCM</span>
                        <span class="chain-box">Joint ventures</span>
                        <span class="chain-box">Shared numbers</span>
                    </span>
''',
    3: '''                    <span class="path-chain">
                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Procurement</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>
                    </span>
''',
    4: '''                    <span class="path-chain">
                        <span class="chain-box">Excel</span>
                        <span class="chain-box">Primavera P6</span>
                        <span class="chain-box">Power BI</span>
                        <span class="chain-box">Power Platform</span>
                        <span class="chain-box">ERP</span>
                        <span class="chain-box">AI</span>
                    </span>
''',
}

CSS = '''
        /* Milestone chain under each step. Boxes joined by a connector, so the
           column reads as a route rather than as a row of tags. */
        .path-chain { display: flex; flex-direction: column; gap: 8px; margin-top: 12px; }
        .chain-box {
            position: relative; display: block;
            padding: 6px 10px; border-radius: 7px;
            background: #fff; border: 1px solid #e2e8f0;
            font-size: 11.5px; font-weight: 600; color: #475569;
            text-decoration: none; line-height: 1.35;
        }
        .chain-box b { float: right; font-weight: 700; color: #94a3b8; }
        .chain-box:not(:last-child)::after {
            content: ''; position: absolute; left: 15px; bottom: -9px;
            width: 2px; height: 9px; background: #e2e8f0;
        }
        a.chain-box:hover { border-color: #10b981; color: #059669; }
        a.chain-box:hover b { color: #10b981; }

        .path-step.is-done .chain-box {
            background: #ecfdf5; border-color: #a7f3d0; color: #047857;
        }
        .path-step.is-done .chain-box b { color: #10b981; }
        .path-step.is-done .chain-box:not(:last-child)::after { background: #a7f3d0; }
        .path-step.is-next .chain-box { border-color: #cbd5e1; }

        @media (max-width: 720px) {
            .path-chain { flex-flow: row wrap; gap: 6px; margin-top: 10px; }
            .chain-box { padding: 4px 9px; }
            .chain-box b { float: none; margin-left: 5px; }
            .chain-box:not(:last-child)::after {
                left: auto; right: -6px; bottom: auto; top: 50%;
                width: 6px; height: 2px; transform: translateY(-50%);
            }
        }
    </style>'''

WIRING = '''
            // Chain box week counts — read from curriculum.js
            [['cb1', CURRICULUM],
             ['cb2', typeof TRACK2 !== 'undefined' ? TRACK2 : null],
             ['cb3', typeof TRACK3 !== 'undefined' ? TRACK3 : null],
             ['cb4', typeof TRACK4 !== 'undefined' ? TRACK4 : null],
             ['cb5', typeof TRACK5 !== 'undefined' ? TRACK5 : null]].forEach(function (p) {
                var e = document.getElementById(p[0]);
                if (e && p[1]) e.textContent = p[1].totalWeeks;
            });
'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "path-chain" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return
    if "path-tracks" not in s:
        sys.exit("HATA: mevcut alt listeler bulunamadi")

    i = s.index('<ol class="path-figure"')
    j = s.index("</ol>", i)
    head, fig, tail = s[:i], s[i:j], s[j:]

    steps = re.findall(r'<li class="path-step.*?</li>\n', fig, re.S)
    if len(steps) != 4:
        sys.exit(f"HATA: 4 adim bekleniyordu, {len(steps)} bulundu")

    for n, step in enumerate(steps, 1):
        new = re.sub(r'                    <span class="path-tracks.*?</span>\n', "", step, flags=re.S)
        new = new.replace("                </li>\n", CHAINS[n] + "                </li>\n")
        fig = fig.replace(step, new, 1)

    s = head + fig + tail
    s = s.replace("    </style>", CSS, 1)
    s = s.replace("            // Fill weeks", WIRING + "\n            // Fill weeks", 1)

    p.write_text(s, encoding="utf-8")
    print("  + learn.html: alt listeler milestone zincirine cevrildi\n\n1 dosya")


if __name__ == "__main__":
    main()
