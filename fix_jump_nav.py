#!/usr/bin/env python3
"""Jump nav: remove the Start Here chip and stop the row overflowing.

The container is 900px with 24px padding, so 852px of usable width. Nine
chips needed roughly 893px, which is why the last one was clipped. Three
changes bring it to about 800px and leave the horizontal scroll in place as
a fallback for narrow windows:

  - Start Here removed (it is a page, not a section on this page, and the
    card at the top of the list already points at it)
  - Roadmap removed (one card, and Toolbox sits right below it anyway)
  - "Life of a Project" shortened to "Lifecycle", matching the anchor id
  - tighter padding and gap, plus a fade at the right edge so that when it
    does scroll it reads as scrollable rather than cut off

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAV = '''                <nav class="track-jump" aria-label="Jump to a section">
                    <a href="#track-1" class="track-jump-link" data-jump="track-1">Schedule <span id="jn1">27</span></a>
                    <a href="#track-2" class="track-jump-link" data-jump="track-2">Cost &amp; Cash <span id="jn2">24</span></a>
                    <a href="#track-3" class="track-jump-link" data-jump="track-3">Risk <span id="jn3">18</span></a>
                    <a href="#track-4" class="track-jump-link" data-jump="track-4">Contract <span id="jn4">20</span></a>
                    <a href="#track-5" class="track-jump-link" data-jump="track-5">Claims <span id="jn5">28</span></a>
                    <a href="#track-6" class="track-jump-link" data-jump="track-6">Interfaces <span id="jn6">14</span></a>
                    <a href="#lifecycle" class="track-jump-link" data-jump="lifecycle">Lifecycle <span id="jnlc">52</span></a>
                    <a href="#toolbox" class="track-jump-link" data-jump="toolbox">Toolbox</a>
                </nav>'''

OLD_CSS = """        .track-jump {
            position: sticky; top: 72px; z-index: 400;
            display: flex; gap: 6px; align-items: center;
            padding: 12px 0; margin-bottom: 4px;
            background: var(--bg-light);
            overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch;
        }"""

NEW_CSS = """        .track-jump {
            position: sticky; top: 72px; z-index: 400;
            display: flex; gap: 5px; align-items: center;
            padding: 12px 0; margin-bottom: 4px;
            background: var(--bg-light);
            overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch;
            /* Fades the right edge only while there is more to scroll to, so a
               clipped chip reads as scrollable instead of broken. */
            -webkit-mask-image: linear-gradient(to right, #000 calc(100% - 28px), transparent);
            mask-image: linear-gradient(to right, #000 calc(100% - 28px), transparent);
        }
        @supports (animation-timeline: scroll(self inline)) {
            .track-jump {
                animation: jump-fade linear both;
                animation-timeline: scroll(self inline);
            }
            @keyframes jump-fade {
                to {
                    -webkit-mask-image: linear-gradient(to right, #000 100%, transparent);
                    mask-image: linear-gradient(to right, #000 100%, transparent);
                }
            }
        }"""

OLD_LINK = """        .track-jump-link {
            flex: 0 0 auto; padding: 7px 14px; border-radius: 20px;"""

NEW_LINK = """        .track-jump-link {
            flex: 0 0 auto; padding: 7px 12px; border-radius: 20px;"""


def main():
    p = ROOT / "learn.html"
    s = p.read_text(encoding="utf-8")
    orig = s

    if 'data-jump="lifecycle">Lifecycle' in s:
        print("  = learn.html: zaten uygulanmis")
        print("\n0 dosya")
        return

    a = s.index('                <nav class="track-jump"')
    b = s.index("</nav>", a) + len("</nav>")
    s = s[:a] + NAV + s[b:]

    for old, new, label in ((OLD_CSS, NEW_CSS, "track-jump"), (OLD_LINK, NEW_LINK, "track-jump-link")):
        if old not in s:
            sys.exit(f"HATA: {label} CSS blogu beklenen halde bulunamadi")
        s = s.replace(old, new, 1)

    # #roadmap no longer has a chip but still needs the anchor offset
    if s == orig:
        print("  = learn.html: degisiklik yok")
        print("\n0 dosya")
        return

    p.write_text(s, encoding="utf-8")
    print("  + learn.html: jump nav 8 chip, tasma giderildi")
    print("\n1 dosya")


if __name__ == "__main__":
    main()
