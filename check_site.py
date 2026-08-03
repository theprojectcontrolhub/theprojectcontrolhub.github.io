#!/usr/bin/env python3
"""
check_site.py — one command that runs every audit this project relies on.

    python3 tools/check_site.py            # all checks
    python3 tools/check_site.py --quick    # skip the copyright n-gram scan (slow)

Run it after ANY content change. It exists because on 2026-07-19 a set of
figures was carried in from a conversation summary rather than from the
published article, and six articles were built on top of the wrong numbers
before anyone noticed. Prose reminders do not catch that. This does.
"""
import re, os, sys, json, glob, html, collections, subprocess
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CANON = json.load(open("tools/canon.json", encoding="utf-8"))
QUICK = "--quick" in sys.argv

TRACKS = {"Schedule": ("week-", 27), "Cost & Cash": ("cost-week-", 24), "Risk": ("risk-week-", 18),
          "Contract": ("contract-week-", 20), "Claims": ("claim-week-", 28),
          "Reporting": ("reporting-week-", 26), "Interfaces": ("interfaces-week-", 14)}
# Yayında olan sayfalar. Track 4 parça parça çıkacağı için diskte var olanla
# sınırlanır; "live ama dosya yok" durumunu check_curriculum ayrıca yakalar.
PAGES = [f for f in (f"{p}{i}.html" for p, n in TRACKS.values() for i in range(1, n + 1))
         if os.path.exists(f)]

STOPWORDS = set("""about above across after again against already always another because before
being below between both cannot could during either enough every first found still their there these
things think those through under until using where which while whole would""".split())

fails, warns = [], []
def bad(section, msg):  fails.append(f"{section}: {msg}")
def warn(section, msg): warns.append(f"{section}: {msg}")

def read(f):
    return open(f, encoding="utf-8").read()

def body(f, strip_svg=True):
    s = read(f)
    i = s.find('class="article-body"')
    if i < 0:
        return ""
    seg = s[i:s.find("share-bar-bottom", i)]
    if strip_svg:
        seg = re.sub(r"<svg.*?</svg>", "", seg, flags=re.S)
    return seg

def prose(f, strip_svg=True):
    return re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", " ", body(f, strip_svg))))


# ---------------------------------------------------------------- 1. links
def check_links():
    present = set(os.listdir("."))
    n = 0
    for f in sorted(glob.glob("*.html")):
        for h in re.findall(r'(?:href|src)="([^"]+)"', read(f)):
            if h.startswith(("http", "mailto:", "tel:", "#", "data:", "javascript:")):
                continue
            t = h.split("#")[0].split("?")[0]
            if t and t not in present:
                bad("links", f"{f} -> {h}")
                n += 1
    return f"{len(glob.glob('*.html'))} sayfa tarandı, {n} kırık"


# ------------------------------------------------------------- 2. tag balance
def check_tags():
    n = 0
    for f in glob.glob("*.html"):
        s = read(f)
        for t in ["div", "section", "figure", "svg", "p", "g", "text", "a", "em", "strong"]:
            o = len(re.findall(r"<" + t + r"\b(?![^>]*/>)", s))
            c = len(re.findall(r"</" + t + ">", s))
            if o != c:
                bad("tags", f"{f} <{t}> {o} açık / {c} kapalı")
                n += 1
    return "dengeli" if not n else f"{n} dengesizlik"


# ---------------------------------------------------------------- 3. chain
def check_chain():
    def nxt(f):
        s = read(f)
        i = s.find('class="next-article"')
        m = re.findall(r'href="([^"]+\.html)"', s[i:i + 900])
        return m[0] if m else None
    seen, cur = [], "week-1.html"
    for _ in range(200):
        seen.append(cur)
        if cur == "learn.html":
            break
        cur = nxt(cur)
        if cur is None or cur in seen:
            bad("chain", f"zincir {seen[-1]} sonrası koptu")
            break
    missing = [p for p in PAGES if p not in seen]
    if missing:
        bad("chain", f"zincirde olmayan makale: {missing[:5]}")
    if seen[-1] != "learn.html":
        bad("chain", f"learn.html ile bitmiyor ({seen[-1]})")
    return f"{len(seen)} adım, son {seen[-1]}"


# ----------------------------------------------------------------- 4. meta
def check_meta():
    for key, pat in [("title", r"<title>(.*?)</title>"),
                     ("description", r'name="description" content="([^"]*)"')]:
        c = collections.Counter(re.search(pat, read(f), re.S).group(1) for f in PAGES)
        for v, n in c.items():
            if n > 1:
                bad("meta", f"{key} {n} sayfada aynı: {v[:60]}")
    share = collections.Counter()
    for f in PAGES:
        s = read(f)
        tw = re.search(r'twitter\.com/intent/tweet\?url=([^&"]+)&text=([^"]+)', s)
        li = re.search(r'share-offsite/\?url=([^"]+)', s)
        wa = re.search(r'wa\.me/\?text=([^"]+)', s)
        if not (tw and li and wa):
            bad("meta", f"{f} paylaşım linki eksik")
            continue
        share[unquote(tw.group(2))] += 1
        if not unquote(tw.group(1)).endswith(f): bad("meta", f"{f} twitter url yanlış")
        if not unquote(li.group(1)).endswith(f): bad("meta", f"{f} linkedin url yanlış")
        if f not in unquote(wa.group(1)):        bad("meta", f"{f} whatsapp url yanlış")
    for v, n in share.items():
        if n > 1:
            bad("meta", f"paylaşım metni {n} sayfada aynı: {v[:50]}")
    return f"{len(PAGES)} makale, başlık/açıklama/paylaşım benzersiz"


# -------------------------------------------------------------- 5. sitemap
def check_sitemap():
    locs = re.findall(r"<loc>([^<]+)</loc>", read("sitemap.xml"))
    dup = [u for u, n in collections.Counter(locs).items() if n > 1]
    if dup:
        bad("sitemap", f"tekrar eden URL: {dup}")
    for p in PAGES:
        if not any(u.endswith("/" + p) for u in locs):
            bad("sitemap", f"eksik: {p}")
    return f"{len(locs)} URL"


# ---------------------------------------------------------------- 6. cache
def check_cache():
    v = set()
    for f in glob.glob("*.html"):
        v |= set(re.findall(r"curriculum\.js\?v=(\d+)", read(f)))
    if len(v) > 1:
        bad("cache", f"karışık sürüm: {sorted(v)}")
    return f"v{sorted(v)[0]}" if v else "sürüm yok"


# ----------------------------------------------------------- 7. curriculum
def check_curriculum():
    js = read("curriculum.js")
    out = []
    for name, (pre, total) in TRACKS.items():
        live = re.findall(r'status:\s*"live",\s*page:\s*"(' + re.escape(pre) + r'\d+\.html)"', js)
        for p in live:
            if not os.path.exists(p):
                bad("curriculum", f"live ama dosya yok: {p}")
        out.append(f"{name} {len(live)}/{total}")
    if "function badgeText" not in js:
        bad("curriculum", "badgeText() yok — rozetler bayatlayabilir")
    return " · ".join(out)


# ----------------------------------------------------------------- 8. canon
def check_canon():
    for expr, expect in CANON["identities"].items():
        if expr.startswith("_"):
            continue
        got = eval(expr, {"__builtins__": {}})
        if got != expect:
            bad("canon", f"aritmetik bozuk: {expr} = {got}, beklenen {expect}")
    allprose = {f: prose(f, strip_svg=False) for f in PAGES}
    for value, why in CANON["forbidden_values"].items():
        if value.startswith("_"):
            continue
        hit = [f for f, t in allprose.items() if value in t]
        if hit:
            bad("canon", f"YASAKLI DEĞER '{value}' geri geldi ({why}) → {hit}")
    reg = CANON["risk_register"]
    if sum(reg["risks"].values()) != reg["total_14_risks"]:
        bad("canon", "canon.json kendi içinde tutarsız: 14 risk toplamı")
    return f"{len(CANON['identities'])-1} aritmetik, {len(CANON['forbidden_values'])-1} yasaklı değer"


# ------------------------------------------------------------------ 9. xref
def check_xref():
    QUAL = r"(?:Schedule|Cost\s*&(?:amp;)?\s*Cash|Risk|Contract(?:\s*Management)?|Claims|Reporting|Interfaces|Track\s*[1-7])"
    cross = 0
    for f in PAGES:
        own_pre = ("cost-week-" if f.startswith("cost-") else
               "risk-week-" if f.startswith("risk-") else
               "contract-week-" if f.startswith("contract-") else
               "claim-week-" if f.startswith("claim-") else
               "reporting-week-" if f.startswith("reporting-") else
               "interfaces-week-" if f.startswith("interfaces-") else "week-")
        n = int(re.search(r"week-(\d+)", f).group(1))
        t = prose(f)
        for m in re.finditer(r"((?:" + QUAL + r")\s+)?Weeks?\s+(\d+)(\s+of\s+(?:Schedule|Cost))?", t):
            if m.group(1) or m.group(3):
                cross += 1
                continue
            w = int(m.group(2))
            if w >= n:
                # Kendi track'inde ileri atıf meşru olabilir ("Week 23 explains...").
                # Mutlak eşik ayırt etmiyor; ayırt eden şey, aynı numaralı makaleyi
                # üç track'te karşılaştırmak. Kendi track'i açık ara kaybediyorsa şüpheli.
                ctx = t[max(0, m.start() - 150):m.end() + 130].lower()
                kw = {x for x in re.findall(r"[a-z][a-z'-]{5,}", ctx) if x not in STOPWORDS}
                if len(kw) < 5:
                    continue
                score = {}
                for pre in ("week-", "cost-week-", "risk-week-", "contract-week-",
                            "claim-week-", "reporting-week-", "interfaces-week-"):
                    cand = f"{pre}{w}.html"
                    if os.path.exists(cand):
                        tgt = prose(cand).lower()
                        score[cand] = sum(1 for k in kw if k in tgt) / len(kw)
                own = f"{own_pre}{w}.html"
                if own not in score:
                    warn("xref", f"{f} 'Week {w}' — bu track'te öyle bir hafta yok")
                    continue
                best = max(score, key=score.get)
                if best != own and score[best] - score[own] >= 0.15:
                    warn("xref", f"{f} çıplak 'Week {w}' → {best} ({score[best]:.2f}) "
                                 f"{own}'dan ({score[own]:.2f}) daha iyi eşleşiyor")
        # her track-aşırı atıf linkli olmalı
        b = body(f, strip_svg=True)
        for m in re.finditer(QUAL + r"\s+Weeks?\s+\d+", re.sub("<[^>]+>", " ", b)):
            pass
    unlinked = []
    for f in PAGES:
        b = body(f)
        plain = html.unescape(re.sub("<[^>]+>", " ", b))
        for m in re.finditer(r"(?:Schedule|Cost\s*&\s*Cash)\s+Week\s+\d+", plain):
            frag = m.group(0).replace("&", "&amp;")
            if f'>{frag}<' not in b and frag not in re.sub(r"<a [^>]*>|</a>", "", b):
                pass
        if re.search(r"(?<!>)(?:Schedule|Cost\s*&amp;\s*Cash)\s+Week\s+\d+(?!</a>)", b):
            if not re.search(r'<a href="[^"]+">(?:Schedule|Cost\s*&amp;\s*Cash)\s+Week', b):
                unlinked.append(f)
    if unlinked:
        warn("xref", f"linklenmemiş track-aşırı atıf olabilir: {unlinked}")
    return f"{cross} track-aşırı atıf"


# ----------------------------------------------------------------- 10. voice
def _sections(f):
    seg = body(f)
    parts = re.split(r"<h2[^>]*>(.*?)</h2>", seg)
    out = {}
    for k in range(1, len(parts), 2):
        head = re.sub("<[^>]+>", "", parts[k]).strip().lower()
        txt = re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", " ", parts[k + 1])))
        if "practical insight" in head:
            key = "practical"
        elif "key takeaway" in head:
            key = "takeaways"
        else:
            key = "body"
        out[key] = out.get(key, "") + " " + txt
    return out


def check_voice():
    V = re.compile(r"\b[A-Za-z]+(?:'|\u2019)(?:t|re|ve|ll|m)\b"
                   r"|\b(?:it|that|there|what|here|he|she|who|let|nothing|somebody|nobody|one)(?:'|\u2019)s\b", re.I)
    YOU = re.compile(r"\byou\b|\byour\b|\byou(?:'|\u2019)(?:re|ve|ll|d)\b", re.I)
    out = []
    agg = {}
    for name, (pre, total) in TRACKS.items():
        w = c = 0
        sec = {}
        for i in range(1, total + 1):
            f = f"{pre}{i}.html"
            if not os.path.exists(f):
                continue
            t = prose(f)
            w += len(t.split()); c += len(V.findall(t))
            for k, v in _sections(f).items():
                sec[k] = sec.get(k, "") + " " + v
        agg[name] = {k: (1000 * len(YOU.findall(v)) / len(v.split()) if v.split() else 0)
                     for k, v in sec.items()}
        d = 1000 * c / w if w else 0
        out.append(f"{name} {d:.0f}")
        if w == 0:
            continue          # henuz yayinlanmamis track: olcecek prose yok
        if d < 3:
            warn("voice", f"{name} kısaltma yoğunluğu {d:.1f}/1000 — diğer track'lerden kopuk")
    # "Practical insight" her track'te okura hitap etmeli. Gövde farkı kasıtlı
    # (bkz. NOTES.md §4): Risk vakayı anlatır, Schedule okura anlatır.
    base = agg.get("Schedule", {}).get("practical", 0)
    for name, a in agg.items():
        if not a:
            continue          # henuz yayinlanmamis track
        if base and a.get("practical", 0) < base * 0.5:
            warn("voice", f"{name} 'Practical insight' ikinci şahıs yoğunluğu "
                          f"{a.get('practical', 0):.0f}/1000 — Schedule {base:.0f}, okura hitap zayıflamış")
    detail = " | ".join(f"{n[:4]} gövde {a.get('body',0):.0f} prat {a.get('practical',0):.0f}"
                        for n, a in agg.items())
    return "kısaltma " + " · ".join(out) + " /1000 · you: " + detail


# ------------------------------------------------------------ 11. copyright
def check_copyright():
    # Kaynaklar bir arşivden çıkarılmış olabilir: uploads/ salt-okunur olduğu için
    # PDF'ler oraya konulamaz. SOURCE_DIR ile ek bir kaynak ağacı verilebilir.
    roots = ["/mnt/user-data/uploads"]
    env = os.environ.get("SOURCE_DIR")
    if env:
        roots.append(env)
    srcs = []
    for r in roots:
        for ext in ("pdf", "pptx", "docx"):
            srcs += glob.glob(os.path.join(r, "**", "*." + ext), recursive=True)
    if not srcs:
        bad("telif", "kaynak dosya yok — tam tarama çalışmadı. Bu bir GEÇTİ değil. "
                     "Kaynakları uploads/ içine koy ya da SOURCE_DIR=<dizin> ver.")
        return "TARANMADI"
    def nm(t):
        return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", t.lower())).strip()
    pool = set()
    read = 0
    for p in srcs:
        try:
            if p.lower().endswith(".pdf"):
                t = subprocess.run(["pdftotext", "-q", p, "-"], capture_output=True,
                                   text=True, timeout=240).stdout
            else:
                t = subprocess.run(["extract-text", p], capture_output=True,
                                   text=True, timeout=240).stdout
        except Exception:
            continue
        if len(t.strip()) < 200:      # taranmış / metin katmanı yok
            continue
        read += 1
        ws = nm(t).split()
        pool |= {tuple(ws[i:i + 10]) for i in range(len(ws) - 9)}
    if read < len(srcs):
        warns.append(f"telif: {len(srcs) - read} kaynak metin katmanı olmadan atlandı (OCR gerekir)")
    hits = []
    for f in PAGES:
        ws = nm(prose(f)).split()
        for i in range(len(ws) - 9):
            if tuple(ws[i:i + 10]) in pool:
                hits.append((f, " ".join(ws[i:i + 10])))
    for f, g in hits:
        bad("copyright", f"{f}: 10 kelimelik örtüşme “{g}”")
    long_q = []
    for f in PAGES:
        for m in re.finditer(r"&#8220;(.*?)&#8221;", body(f), re.S):
            q = html.unescape(re.sub("<[^>]+>", "", m.group(1)))
            if len(q.split()) >= 15 and nm(q)[:60] in "":
                long_q.append((f, q[:60]))
    return f"{read} kaynak, 10-gram örtüşme {len(hits)}"


CHECKS = [("linkler", check_links), ("etiketler", check_tags), ("zincir", check_chain),
          ("meta", check_meta), ("sitemap", check_sitemap), ("cache", check_cache),
          ("müfredat", check_curriculum), ("KANON", check_canon), ("atıflar", check_xref),
          ("ses", check_voice)]
if not QUICK:
    CHECKS.append(("telif", check_copyright))

print(f"\n  check_site.py — {ROOT}\n  " + "-" * 62)
for name, fn in CHECKS:
    try:
        note = fn()
    except Exception as e:
        bad(name, f"kontrol çöktü: {e}")
        note = "HATA"
    print(f"  {name:<12} {note}")
print("  " + "-" * 62)
for w in warns:
    print(f"  uyarı   {w}")
for f_ in fails:
    print(f"  HATA    {f_}")
print(f"\n  {'GEÇTİ' if not fails else str(len(fails)) + ' HATA'}"
      f"{', ' + str(len(warns)) + ' uyarı' if warns else ''}\n")
sys.exit(1 if fails else 0)
