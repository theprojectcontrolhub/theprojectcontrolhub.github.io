#!/usr/bin/env python3
"""Repairs the breadcrumb on the 27 Claims articles.

Every Claims page from week 2 to week 28 says "Week 1" in its breadcrumb
while the module badge and data-current-week are correct. The same defect was
found in Reporting and fixed there; this is the older instance of it, and it
has been live since the track was published.

Both were caused the same way: a build script replaced a string it assumed
was contiguous, the crumb is split by a nested span, and nothing verified the
replacement happened. check_stale now catches it.

Short titles come from curriculum.js.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def shorts():
    src = (ROOT / "curriculum.js").read_text(encoding="utf-8")
    i = src.index("const TRACK5 = {")
    j = src.index("get liveCount()", i)
    out = {}
    for m in re.finditer(r'n:\s*(\d+),\s*title:\s*"(?:[^"\\]|\\.)*",\s*short:\s*"((?:[^"\\]|\\.)*)"',
                         src[i:j]):
        out[int(m.group(1))] = m.group(2).encode().decode("unicode_escape")
    return out


def esc(t):
    return t.replace("&", "&amp;").replace("\u2014", "&#8212;").replace("\u2019", "&#8217;")


def main():
    short = shorts()
    if len(short) != 28:
        sys.exit(f"HATA: 28 hafta bekleniyordu, {len(short)} bulundu")
    n = 0
    for w in range(1, 29):
        f = ROOT / f"claim-week-{w}.html"
        if not f.exists():
            continue
        s = f.read_text(encoding="utf-8")
        want = f'<span>Week {w}<span class="crumb-title"> &#183; {esc(short[w])}</span>'
        new, k = re.subn(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>',
                         want, s, count=1)
        if k and want not in s:
            f.write_text(new, encoding="utf-8")
            n += 1
    print(f"  duzeltilen kirinti: {n}\n\n{n} dosya")


if __name__ == "__main__":
    main()
