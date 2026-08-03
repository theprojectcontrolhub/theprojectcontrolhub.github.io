#!/usr/bin/env python3
"""Two chains in the path figure did not match their tracks.

Interfaces showed four boxes and none of them was an interface, even though
weeks 9 to 11 are the phase the track is named after. "Numbers with two
owners" goes, replaced by the two concrete cases behind it, which say the
same thing without needing to be decoded.

The lifecycle chain skipped procurement, which is a phase of its own in the
module (weeks 16 and 17) and the phase where an EPC programme is usually
lost.

Idempotent.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_7 = '''                        <span class="chain-box">Delivery models</span>
                        <span class="chain-box">EPCM</span>
                        <span class="chain-box">Joint ventures</span>
                        <span class="chain-box">Numbers with two owners</span>'''

NEW_7 = '''                        <span class="chain-box">Delivery models</span>
                        <span class="chain-box">EPCM</span>
                        <span class="chain-box">Joint ventures</span>
                        <span class="chain-box">Work in nobody&#39;s scope</span>
                        <span class="chain-box">Shared progress</span>
                        <span class="chain-box">Shared cost</span>'''

OLD_LC = '''                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>'''

NEW_LC = '''                        <span class="chain-box">Tender</span>
                        <span class="chain-box">Start-up</span>
                        <span class="chain-box">Engineering</span>
                        <span class="chain-box">Procurement</span>
                        <span class="chain-box">Construction</span>
                        <span class="chain-box">Handover</span>'''


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")
    if "Shared progress" in s:
        print("  = learn.html: zaten uygulanmis\n\n0 dosya")
        return
    for old, new, label in ((OLD_7, NEW_7, "Interfaces zinciri"), (OLD_LC, NEW_LC, "Lifecycle zinciri")):
        if old not in s:
            sys.exit(f"HATA: {label} beklenen halde bulunamadi")
        s = s.replace(old, new, 1)
    p.write_text(s, encoding="utf-8")
    print("  + learn.html: iki zincir duzeltildi\n\n1 dosya")


if __name__ == "__main__":
    main()
