#!/usr/bin/env python3
"""Rebuilds the path figure around a question per stage.

Adopted from the infographic version: a question rather than a noun, a
one-line answer under it, numbered milestones, and the size moved to a footer
badge so the top of each column stays clear.

Not adopted, deliberately: five separate hues (colour here carries state, not
category), five filled milestones (only tracks 1-5 exist and the figure must
not say otherwise), an icon per row, and the marketing strip.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIGURE = '''            <ol class="path-figure is-five" aria-label="How the curriculum builds">
                <li class="path-step is-done">
                    <span class="path-dot"><i class='bx bx-check'></i></span>
                    <span class="path-q">How?</span>
                    <span class="path-sub">Learn the disciplines</span>
                    <strong class="path-title"><a href="#track-1">The methods</a></strong>
                    <span class="path-out">Build a programme, price it, keep the right when it slips, prove the delay.</span>
                    <span class="path-chain">
                        <a class="chain-box" href="#track-1">Schedule <b id="cb1">27</b></a>
                        <a class="chain-box" href="#track-2">Cost &amp; Cash <b id="cb2">24</b></a>
                        <a class="chain-box" href="#track-3">Risk <b id="cb3">18</b></a>
                        <a class="chain-box" href="#track-4">Contract <b id="cb4">20</b></a>
                        <a class="chain-box" href="#track-5">Claims <b id="cb5">28</b></a>
                    </span>
                    <span class="path-foot"><i class='bx bx-book-open'></i> Tracks 1&#8211;5 &#183; <b id="pfDone">117</b> lessons</span>
                </li>
                <li class="path-step is-next">
                    <span class="path-dot">2</span>
                    <span class="path-q">Where from?</span>
                    <span class="path-sub">Understand the information</span>
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
                    <span class="path-foot"><i class='bx bx-calendar'></i> Track 6 &#183; <b id="pfT6">26</b> weeks &#183; next</span>
                </li>
                <li class="path-step">
                    <span class="path-dot">3</span>
                    <span class="path-q">Who?</span>
                    <span class="path-sub">Coordinate the organisations</span>
                    <strong class="path-title"><a href="#track-7">Interfaces</a></strong>
                    <span class="path-out">All of it when the job has more than one contract and no single chain of command.</span>
                    <span class="path-chain">
                        <span class="chain-box">Delivery models</span>
                        <span class="chain-box">EPCM</span>
                        <span class="chain-box">Joint ventures</span>
                        <span class="chain-box">Work in nobody&#39;s scope</span>
                        <span class="chain-box">Shared progress</span>
                        <span class="chain-box">Shared cost</span>
                    </span>
                    <span class="path-foot"><i class='bx bx-calendar'></i> Track 7 &#183; <b id="pfT7">14</b> weeks</span>
                </li>
                <li class="path-step">
                    <span class="path-dot">4</span>
                    <span class="path-q">When?</span>
                    <span class="path-sub">Follow the project through</span>
                    <strong class="path-title"><a href="#lifecycle">The life of a project</a></strong>
                    <span class="path-out">The order the work arrives in, from the investment decision to the archive.</span>
                    <span class="path-chain">
                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Procurement</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>
                    </span>
                    <span class="path-foot"><i class='bx bx-calendar'></i> <b id="pfLC">36</b> weeks</span>
                </li>
                <li class="path-step">
                    <span class="path-dot">5</span>
                    <span class="path-q">With what?</span>
                    <span class="path-sub">Use the tools that support it</span>
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
                    <span class="path-foot"><i class='bx bx-infinite'></i> After the writing</span>
                </li>
            </ol>
'''

CSS = '''
        .path-dot {
            font-size: 11px; font-weight: 800; color: #94a3b8;
            line-height: 1;
        }
        .path-step.is-done .path-dot, .path-step.is-next .path-dot { color: #fff; }
        .path-step.is-next .path-dot { background: #10b981; border-color: #10b981; }
        .path-q {
            display: block; font-size: 13px; font-weight: 800;
            color: #cbd5e1; letter-spacing: -0.01em; margin-bottom: 2px;
        }
        .path-step.is-done .path-q, .path-step.is-next .path-q { color: #10b981; }
        .path-sub {
            display: block; font-size: 11px; font-weight: 600;
            color: #94a3b8; margin-bottom: 7px; line-height: 1.35;
        }
        .path-foot {
            display: flex; align-items: center; gap: 6px;
            margin-top: 10px; padding-top: 9px;
            border-top: 1px solid #e2e8f0;
            font-size: 10.5px; font-weight: 600; color: #94a3b8;
        }
        .path-foot i { font-size: 13px; }
        .path-foot b { font-weight: 800; }
        .path-step.is-done .path-foot, .path-step.is-next .path-foot { color: #059669; }
        .path-step.is-done .path-foot { border-top-color: #a7f3d0; }
        @media (max-width: 720px) {
            .path-foot { margin-top: 8px; padding-top: 7px; }
        }
    </style>'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "path-q" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return

    i = s.index('            <ol class="path-figure')
    j = s.index("            </ol>\n", i) + len("            </ol>\n")
    s = s[:i] + FIGURE + s[j:]

    # the old stage label rule is superseded
    s = re.sub(r"\n *\.path-stage \{.*?\n *\}\n( *\.path-step\.is-done \.path-stage[^\n]*\n)?", "\n", s, flags=re.S)

    s = s.replace("    </style>", CSS, 1)
    p.write_text(s, encoding="utf-8")
    print("  + learn.html: figur sorulara gore yeniden kuruldu\n\n1 dosya")


if __name__ == "__main__":
    main()
