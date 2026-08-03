#!/usr/bin/env python3
"""Gives every step in the path figure a sub-list.

Only the first step had one, which made the other three look unfinished. Each
step now shows what is inside it: the five tracks, the four arguments of
Interfaces, the arc of the lifecycle module, and the tools themselves.

The first step's items link to their sections because those are real
destinations on this page. The rest are contents rather than destinations, so
they are plain. The step titles stay linked in all four.

The lifecycle module has nine phases; the figure shows the arc rather than the
list, because a figure is for shape and the full list sits in the module card
below it.

Idempotent.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ANCHOR_2 = ('                    <span class="path-out">Do all of that when the job has more than one '
            'contract and no single chain of command.</span>\n')
SUB_2 = '''                    <span class="path-tracks is-plain">
                        <span>Delivery models</span><span>EPCM</span><span>Joint ventures</span><span>Shared numbers</span>
                    </span>
'''

ANCHOR_3 = ('                    <span class="path-out">Know when each method is needed, who feeds you the '
            'numbers, and which record it produces.</span>\n')
SUB_3 = '''                    <span class="path-tracks is-plain">
                        <span>Tender</span><span>Start-up</span><span>Engineering</span><span>Procurement</span><span>Construction</span><span>Handover</span>
                    </span>
'''

ANCHOR_4 = ('                    <span class="path-out">Excel, Primavera, Power BI &#8212; last, because a tool '
            'you cannot reason about is worth nothing.</span>\n')
SUB_4 = '''                    <span class="path-tracks is-plain">
                        <span>Excel</span><span>Primavera P6</span><span>Power BI</span><span>Power Platform</span><span>ERP</span><span>AI</span>
                    </span>
'''

CSS = '''
        .path-tracks.is-plain span {
            font-size: 10.5px; font-weight: 600; color: #64748b;
            background: #fff; border: 1px solid #e2e8f0; border-radius: 5px;
            padding: 2px 6px; white-space: nowrap;
        }
    </style>'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "is-plain" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return

    for anchor, sub, n in ((ANCHOR_2, SUB_2, 2), (ANCHOR_3, SUB_3, 3), (ANCHOR_4, SUB_4, 4)):
        if anchor not in s:
            sys.exit(f"HATA: {n}. adimin path-out satiri bulunamadi")
        s = s.replace(anchor, anchor + sub, 1)

    s = s.replace("    </style>", CSS, 1)
    p.write_text(s, encoding="utf-8")
    print("  + learn.html: 2., 3. ve 4. adimlara alt liste eklendi\n\n1 dosya")


if __name__ == "__main__":
    main()
