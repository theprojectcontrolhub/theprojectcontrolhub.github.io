# The Project Control Hub

A written curriculum in project controls for construction and engineering
projects, in English. 199 lessons across eight tracks, complete and free to read
and free to read.

**Live site:** https://theprojectcontrolhub.com

| Track | Weeks |
| --- | --- |
| Schedule Management | 27 |
| Cost & Cash | 24 |
| Risk | 18 |
| Contract Management | 20 |
| Claims & Delay Analysis | 28 |
| Reporting | 26 |
| Interfaces | 17 |
| The Life of a Project | 39 |

Static site: HTML, CSS and a small number of JavaScript files (`curriculum.js`
for the lesson data, `auth.js` for Google sign-in). No build step is required to
serve it. The curriculum data lives in `curriculum.js`, which every page reads
at runtime, so week counts and badges are computed rather than written into
the pages.

Build scripts and working notes live under `tools/`, which `robots.txt` and
`.gitignore` both exclude from the published site. They are kept with the
source for reproducibility, not deployed.

## Dates

`curriculum.js` is the single source of truth for lesson publication dates.
Build scripts read it through `tools/lesson_dates.py`. Some older builders
still carry a literal date, but only as a fallback for a lesson that does not
yet exist in `curriculum.js`; for anything already published the date comes
from the file. Do not add a date that overrides it. Before v213 each script held a hardcoded `DATE_ISO`; when
the site's dates were corrected the scripts kept the old ones, so rebuilding
any article would have silently restored a publication date years in the
future. Do not reintroduce per-script dates.

## Checkers

    python3 tools/check_site.py            # links, metadata, chain, copyright
    python3 tools/check_status_strings.py  # stale strings, byline dates
    python3 tools/check_figures.py         # figure width and palette
    python3 tools/audit_track8.py          # Track 8 prose metrics and claims

`check_site.py --quick` skips the copyright scan, which needs the source
corpus. A quick pass is not a full pass.
