#!/usr/bin/env python3
"""Track 5'e 'The site record' haftasi eklenir (yeni 6), 6-27 bir kayar, toplam 28.

Idempotent. Hafta 1 canli oldugu icin ona dokunulmaz.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CHANGED = []

NEW_WEEK = ('        { n: 6, title: "The site record — daily reports, allocation sheets and what each '
            'one proves",\n'
            '          short: "The site record", status: "upcoming" },\n')


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    if os.path.exists(p) and re.sub(r"\?v=\d+", "?v=N", read(p)) == re.sub(r"\?v=\d+", "?v=N", s):
        return
    io.open(p, "w", encoding="utf-8").write(s)
    CHANGED.append(p)


def patch_curriculum():
    js = read("curriculum.js")
    i = js.index("const TRACK5")
    j = js.index("\n    ],", i)
    head, block, tail = js[:i], js[i:j], js[j:]

    if "The site record" in block:
        print("  curriculum.js   hafta zaten ekli")
        return

    if "totalWeeks: 27," not in block:
        sys.exit("HATA: TRACK5 totalWeeks beklenen halde degil (27)")

    # 1) n >= 6 olan her haftayi bir ileri kaydir (buyukten kucuge, cakisma olmasin)
    for n in range(27, 5, -1):
        pat = r"\bn: %d,(?=\s|\n)" % n
        if len(re.findall(pat, block)) != 1:
            sys.exit("HATA: n: %d tek kez gecmiyor" % n)
        block = re.sub(pat, "n: %d," % (n + 1), block)

    # 2) yeni haftayi Faz B icine, as-planned'dan hemen sonra koy
    anchor = ('          short: "The as-planned programme", status: "upcoming" },\n')
    if anchor not in block:
        sys.exit("HATA: as-planned satiri bulunamadi")
    block = block.replace(anchor, anchor + NEW_WEEK, 1)

    # 3) toplam
    block = block.replace("totalWeeks: 27,", "totalWeeks: 28,", 1)

    write("curriculum.js", head + block + tail)
    print("  curriculum.js   yeni hafta 6 eklendi, 6-27 kaydi, toplam 28")


def patch_others():
    # checker kaydi
    p = "tools/check_site.py"
    s = read(p)
    if '"Claims": ("claim-week-", 27)' in s:
        write(p, s.replace('"Claims": ("claim-week-", 27)', '"Claims": ("claim-week-", 28)', 1))
        print("  check_site.py   Claims 27 -> 28")
    else:
        print("  check_site.py   zaten 28")

    # learn.html statik yedek metin (JS zaten uzerine yaziyor ama tutarli olsun)
    p = "learn.html"
    s = read(p)
    if '<span id="t5ProgressText">0 of 27 published</span>' in s:
        write(p, s.replace('<span id="t5ProgressText">0 of 27 published</span>',
                           '<span id="t5ProgressText">1 of 28 published</span>', 1))
        print("  learn.html      ilerleme yedegi 1 of 28")
    else:
        print("  learn.html      zaten guncel")


def bump():
    if not CHANGED:
        print("  cache           degisiklik yok")
        return
    v = int(re.search(r"curriculum\.js\?v=(\d+)", read("index.html")).group(1))
    n = 0
    for f in sorted(os.listdir(".")):
        if f.endswith(".html"):
            a = read(f)
            b = a.replace("curriculum.js?v=%d" % v, "curriculum.js?v=%d" % (v + 1))
            if a != b:
                io.open(f, "w", encoding="utf-8").write(b)   # surum damgasi:
                CHANGED.append(f)                            # normalize eden write() atlar
                n += 1
    print("  cache           v%d -> v%d (%d sayfa)" % (v, v + 1, n))


if __name__ == "__main__":
    print("\n  add_site_record_week.py — %s" % ROOT)
    patch_curriculum()
    patch_others()
    bump()
    print("  tamam, %d dosya\n" % len(set(CHANGED)))
