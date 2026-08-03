#!/usr/bin/env python3
"""Publishes the 26 Reporting drafts.

Copying the files to the site root is not enough on its own, which is what
went wrong: the list on learn.html renders from curriculum.js, and every
Reporting week there is still `upcoming` with no page and no date. The module
therefore draws as inactive no matter what is sitting in the folder.

Publishing means four things happening together:

  1. curriculum.js  — status live, page, date for all 26
  2. the chain      — claim-week-28 -> reporting-week-1 -> ... -> learn.html
  3. sitemap.xml    — 26 entries
  4. cache          — curriculum.js?v bumped across every page

Dates continue the weekly cadence. Claims week 28 is 13 Sep 2028, so
Reporting week 1 is 20 Sep 2028 and week 26 is 14 Mar 2029.

Idempotent. Run twice and the second run reports 0 dosya.
"""
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "drafts"
FIRST = dt.date(2028, 9, 20)          # the week after claim-week-28
OLD_V, NEW_V = 124, 125


def week_titles():
    """Titles and short titles from curriculum.js, so nothing is retyped."""
    src = (ROOT / "curriculum.js").read_text(encoding="utf-8")
    i = src.index("const TRACK6 = {")
    j = src.index("get liveCount()", i)
    out = {}
    for m in re.finditer(r'\{[^{}]*?n:\s*(\d+),\s*title:\s*"((?:[^"\\]|\\.)*)"', src[i:j]):
        out[int(m.group(1))] = m.group(2).encode().decode("unicode_escape")
    return out


NEXT_BLOCK = '''                        <!-- NEXT ARTICLE NAV (after login) -->
                        <div class="next-article" id="nextArticle" style="display:none;">
                            <div class="next-article-label">{label}</div>
                            <a href="{href}" class="next-article-link">
                                <div>
                                    <span class="next-week-tag">{tag}</span>
                                    <h4>{title}</h4>
                                </div>
                                <i class='bx bx-right-arrow-alt'></i>
                            </a>
                        </div>
'''


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;")
             .replace("\u2014", "&#8212;").replace("\u2019", "&#8217;"))


def add_chain_links(titles):
    """Each article points at the next; week 26 hands back to learn.html."""
    n = 0
    for w in range(1, 27):
        f = DRAFTS / f"reporting-week-{w}.html"
        s = f.read_text(encoding="utf-8")
        if 'class="next-article"' in s:
            continue
        if w < 26:
            block = NEXT_BLOCK.format(
                label="Next week", href=f"reporting-week-{w + 1}.html",
                tag=f"Reporting &#183; Week {w + 1}", title=esc(titles[w + 1]))
        else:
            block = NEXT_BLOCK.format(
                label="Module 06 complete", href="learn.html",
                tag="Interfaces &#183; on the roadmap",
                title="When one contract stops being the shape of the job")
        # goes immediately before the paywall block, as on every published page
        anchor = "                        <!-- PAYWALL CTA -->"
        if anchor not in s:
            sys.exit(f"HATA: {f.name} icinde paywall bloku bulunamadi")
        s = s.replace(anchor, block + "\n" + anchor, 1)
        f.write_text(s, encoding="utf-8")
        n += 1
    return n


def publish_files():
    """Compare ignoring the cache version: the root copies get bumped after
    they are written, so a literal comparison would copy again every run."""
    strip = lambda t: re.sub(r"curriculum\.js\?v=\d+", "curriculum.js?v=", t)
    n = 0
    for w in range(1, 27):
        src = DRAFTS / f"reporting-week-{w}.html"
        dst = ROOT / f"reporting-week-{w}.html"
        if dst.exists() and strip(dst.read_text(encoding="utf-8")) == strip(src.read_text(encoding="utf-8")):
            continue
        shutil.copy2(src, dst)
        n += 1
    return n


def set_live():
    p = ROOT / "curriculum.js"
    s = p.read_text(encoding="utf-8")
    i = s.index("const TRACK6 = {")
    j = s.index("get liveCount()", i)
    block = s[i:j]
    if '"live"' in block:
        return 0
    out, w = block, 0
    for n in range(1, 27):
        date = (FIRST + dt.timedelta(weeks=n - 1)).strftime("%b %-d, %Y")
        # week 8 kept a stray page field from an earlier pass, so the tail is
        # matched loosely rather than assumed to end at the brace
        pat = re.compile(r'(\{[^{}]*?n:\s*%d,[^{}]*?)status:\s*"upcoming"(?:,\s*page:\s*"[^"]*")?(\s*\})' % n)
        new, k = pat.subn(
            r'\1status: "live", page: "reporting-week-%d.html", date: "%s"\2' % (n, date), out)
        if k != 1:
            sys.exit(f"HATA: TRACK6 hafta {n} icin tam bir eslesme yok ({k})")
        out, w = new, w + k
    s = s[:i] + out + s[j:]
    p.write_text(s, encoding="utf-8")
    return w


def link_from_claims():
    p = ROOT / "claim-week-28.html"
    s = p.read_text(encoding="utf-8")
    if "reporting-week-1.html" in s:
        return 0
    s = s.replace(
        '<div class="next-article-label">Module 05 complete</div>\n'
        '                            <a href="learn.html" class="next-article-link">\n'
        '                                <div>\n'
        '                                    <span class="next-week-tag">Track 6 &#183; The Assumptions That Stop Holding &#183; on the roadmap</span>\n'
        '                                    <h4>When one contract stops being the shape of the job</h4>',
        '<div class="next-article-label">Module 05 complete</div>\n'
        '                            <a href="reporting-week-1.html" class="next-article-link">\n'
        '                                <div>\n'
        '                                    <span class="next-week-tag">Reporting &#183; Week 1</span>\n'
        '                                    <h4>What project controls produces, and what it must be fed</h4>', 1)
    p.write_text(s, encoding="utf-8")
    return 1


def add_sitemap():
    p = ROOT / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    if "reporting-week-1.html" in s:
        return 0
    today = dt.date.today().isoformat()
    entries = "".join(
        f"  <url>\n    <loc>https://theprojectcontrolhub.com/reporting-week-{w}.html</loc>\n"
        f"    <lastmod>{today}</lastmod>\n  </url>\n" for w in range(1, 27))
    p.write_text(s.replace("</urlset>", entries + "</urlset>"), encoding="utf-8")
    return 26


def bump_cache():
    n = 0
    for f in sorted(ROOT.glob("*.html")):
        s = f.read_text(encoding="utf-8")
        t = s.replace(f"curriculum.js?v={OLD_V}", f"curriculum.js?v={NEW_V}")
        if t != s:
            f.write_text(t, encoding="utf-8")
            n += 1
    return n


def main():
    titles = week_titles()
    if len(titles) != 26:
        sys.exit(f"HATA: curriculum.js icinde 26 hafta bekleniyordu, {len(titles)} bulundu")
    steps = [("zincir baglantisi", add_chain_links(titles)),
             ("koke kopyalanan makale", publish_files()),
             ("curriculum.js live", set_live()),
             ("claim-week-28 -> reporting-week-1", link_from_claims()),
             ("sitemap girdisi", add_sitemap()),
             ("cache bump", bump_cache())]
    total = 0
    for name, n in steps:
        print(f"  {'+' if n else '='} {name}: {n}")
        total += n
    print(f"\n{total} degisiklik")


if __name__ == "__main__":
    main()
