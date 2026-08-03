#!/usr/bin/env python3
"""Puts data and reporting back into the path figure.

19 of the 52 lifecycle weeks and 5 of the 14 Interfaces weeks are about where
a number comes from, when it closes and what it produces. The figure did not
say so: reordering the module by project phase left the chain reading
"Tender, Start-up, Engineering", which describes a construction management
course rather than this one.

The lifecycle order is still the module's spine and its nine phases are listed
in the card below. The figure now carries the argument instead of the index.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_OUT_3 = ('                    <span class="path-out">Know when each method is needed, who feeds you the '
             'numbers, and which record it produces.</span>')
NEW_OUT_3 = ('                    <span class="path-out">Where every number in your report is born, who owns '
             'it, when it closes, and which record it leaves behind.</span>')

OLD_CHAIN_3 = '''                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Procurement</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>'''

NEW_CHAIN_3 = '''                        <span class="chain-box">Field data</span>
                        <span class="chain-box">Cost &amp; commitments</span>
                        <span class="chain-box">Rules of credit</span>
                        <span class="chain-box">Cut-off &amp; calendar</span>
                        <span class="chain-box">Daily, weekly, monthly</span>
                        <span class="chain-box">Registers &amp; KPIs</span>'''

OLD_BOX_2 = '<span class="chain-box">Shared numbers</span>'
NEW_BOX_2 = '<span class="chain-box">Numbers with two owners</span>'

# the lifecycle order has to stay visible somewhere in the figure, so it moves
# into the kicker where it costs one line instead of six boxes
OLD_KICKER_3 = '<span class="path-kicker"><b id="pfLC">52</b> weeks</span>'
NEW_KICKER_3 = '<span class="path-kicker"><b id="pfLC">52</b> weeks &#183; tender to handover</span>'


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")

    if "Rules of credit" in s and "chain-box" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return

    for old, new, label in ((OLD_CHAIN_3, NEW_CHAIN_3, "3. adim zinciri"),
                            (OLD_OUT_3, NEW_OUT_3, "3. adim aciklamasi"),
                            (OLD_KICKER_3, NEW_KICKER_3, "3. adim kicker"),
                            (OLD_BOX_2, NEW_BOX_2, "2. adim kutusu")):
        if old not in s:
            sys.exit(f"HATA: {label} beklenen halde bulunamadi")
        s = s.replace(old, new, 1)

    p.write_text(s, encoding="utf-8")
    print("  + learn.html: veri ve raporlama omurgasi figure tasindi\n\n1 dosya")


if __name__ == "__main__":
    main()
