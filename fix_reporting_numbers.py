#!/usr/bin/env python3
"""Repairs three defects left by the generator that built the Reporting pages.

All three come from the same mistake: the build script replaced strings it
had assumed the shape of, and never checked that the replacement happened.

  1. Breadcrumb   Every page except week 8 says "Week 8 - Who measures, in
                  what unit, on which day". The template's crumb is split by
                  a nested span, so the search string never existed.

  2. Module badge Same, for "MODULE 06 - REPORTING - WEEK 8". The separator
                  in the file is a literal middot; the script looked for the
                  HTML entity.

  3. Cross-links  The worst of the three. The generator rewrote every
                  occurrence of "reporting-week-8.html" to the page's own
                  filename, which turned nine references to Week 8 into links
                  pointing at the article the reader is already on, still
                  labelled "Week 8".

Crumbs are taken from curriculum.js so nothing is retyped.

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def crumbs():
    """short titles from TRACK6, used as the breadcrumb tail."""
    src = (ROOT / "curriculum.js").read_text(encoding="utf-8")
    i = src.index("const TRACK6 = {")
    j = src.index("get liveCount()", i)
    out = {}
    for m in re.finditer(r'n:\s*(\d+),\s*title:\s*"(?:[^"\\]|\\.)*",\s*short:\s*"((?:[^"\\]|\\.)*)"',
                         src[i:j]):
        out[int(m.group(1))] = m.group(2).encode().decode("unicode_escape")
    return out


def esc(t):
    return t.replace("&", "&amp;").replace("\u2014", "&#8212;").replace("\u2019", "&#8217;")


def main():
    short = crumbs()
    if len(short) != 26:
        sys.exit(f"HATA: 26 hafta bekleniyordu, {len(short)} bulundu")

    fixed = {"crumb": 0, "badge": 0, "link": 0}
    for n in range(1, 27):
        f = ROOT / f"reporting-week-{n}.html"
        s = f.read_text(encoding="utf-8")
        before = s

        # 1. breadcrumb
        want = f'<span>Week {n}<span class="crumb-title"> &#183; {esc(short[n])}</span>'
        s, k = re.subn(r'<span>Week \d+<span class="crumb-title"> &#183; [^<]*</span>', want, s, count=1)
        if k and want not in before:
            fixed["crumb"] += 1

        # 2. module badge
        wantb = f'MODULE 06 · REPORTING · WEEK {n}'
        s, k = re.subn(r'MODULE 06 · REPORTING · WEEK \d+', wantb, s, count=1)
        if k and wantb not in before:
            fixed["badge"] += 1

        # 3. a link whose text names a different week than its target
        def relink(m):
            if m.group(1) == m.group(2):
                return m.group(0)
            fixed["link"] += 1
            return f'<a href="reporting-week-{m.group(2)}.html">Week {m.group(2)}</a>'

        s = re.sub(r'<a href="reporting-week-(\d+)\.html">Week (\d+)</a>', relink, s)

        if s != before:
            f.write_text(s, encoding="utf-8")

    # the drafts are the source these were built from; keep them in step
    for n in range(1, 27):
        src = ROOT / f"reporting-week-{n}.html"
        dst = ROOT / "drafts" / f"reporting-week-{n}.html"
        if dst.exists():
            a = re.sub(r"curriculum\.js\?v=\d+", "curriculum.js?v=", src.read_text(encoding="utf-8"))
            b = re.sub(r"curriculum\.js\?v=\d+", "curriculum.js?v=", dst.read_text(encoding="utf-8"))
            if a != b:
                dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"  breadcrumb duzeltildi : {fixed['crumb']}")
    print(f"  rozet duzeltildi      : {fixed['badge']}")
    print(f"  atif linki duzeltildi : {fixed['link']}")
    print(f"\n{sum(fixed.values())} duzeltme")


if __name__ == "__main__":
    main()
