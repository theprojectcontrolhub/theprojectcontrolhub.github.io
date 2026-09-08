# The Project Control Hub

A written curriculum in project controls for construction and engineering
projects, in English. 199 lessons across eight tracks, complete and free to read.

**Live site:** https://theprojectcontrolhub.com

| Track | Topics |
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
at runtime, so topic counts and badges are computed rather than written into
the pages.

Build scripts and working notes live under `tools/`, which `robots.txt` and
`.gitignore` both exclude from the published site. They are kept with the
source for reproducibility, not deployed.

## No publication dates

The site carries no per-lesson dates. The ones it used to show were a planned
release schedule, not real publication dates, and presenting them as
`datePublished` misrepresented the corpus — 199 lessons written over two
months were dated across four years. Bylines, JSON-LD and `curriculum.js`
now carry none, and `tools/lesson_dates.py` has been removed. Order comes
from the curriculum, not from a calendar.

## Topics, not weeks

Lessons are numbered `Topic N` rather than `Week N`. Nothing is published
weekly, so the old label described a cadence that never ran. Filenames keep
their `week-N.html` slugs deliberately: renaming them would break every
inbound link and every canonical URL for no reader benefit.


## Checkers

    python3 tools/check_site.py            # links, metadata, chain, copyright
    python3 tools/check_status_strings.py  # stale strings, byline dates
    python3 tools/check_figures.py         # figure width and palette
    python3 tools/audit_track8.py          # Track 8 prose metrics and claims

`check_site.py --quick` skips the copyright scan, which needs the source
corpus. A quick pass is not a full pass.

## What "latest" used to mean

The home page once showed the three most recently published lessons, sorted
by date, with a "New" badge on the first. With dates gone every entry sorted
equal, so the panel showed an arbitrary three and badged one of them new. A
fixed, complete curriculum has no newest item: the panel now offers a
starting point instead, and the badge is gone.

## Naming

The data model uses `topics`, `totalTopics`, `latestLiveTopic` and `getTopic`.
It used to say `weeks`, which stopped describing anything once the site
dropped its weekly framing. Renaming it meant changing `curriculum.js` and the
inline scripts in the pages together, since several read the model directly.

Filenames are the deliberate exception: `week-N.html` stays, because renaming
would break every inbound link and canonical URL for no reader benefit.

Nine one-shot scripts under `tools/` still target the old model. They are
marked HISTORICAL at the top and must not be re-run — the change each one made
is already in the site, and they would fail against the current data.

## Checkers are part of the model

`check_site.py` verifies that every lesson's breadcrumb, badge and
`data-current-week` agree with its filename. Those checks looked for "Week N"
and, after the rename, matched nothing — so they reported a clean result while
testing nothing. `check_status_strings.py` had the same problem: it parsed
`totalWeeks` and read every track as empty.

Both now target the current model. When terminology changes, change the
checkers in the same pass, and confirm they still fail on a deliberate error.

## Runtime links

`curriculum.js` supplies the `page:` value for every lesson, and the browser
builds the learn list, the home cards and each article sidebar from it. A wrong
value there is invisible to a static scan: the HTML files are all present and
all internally consistent, and only the navigation built at load time is dead.

That happened once. Renaming the internal model from `weeks` to `topics` also
rewrote the slugs — `week-1.html` became `topic-1.html` — and all 199 runtime
links pointed at files that do not exist. `check_site.py` matched live entries
by expected prefix, found none, reported `Schedule 0/27`, and passed.

Two checks now cover it. `check_site.py` verifies that every `page:` value
exists on disk whatever it is named, and fails a track whose live list comes
back empty. `node tools/check_runtime_links.js` renders the curriculum and
resolves every link it produces. Run both before any release.

## tools/legacy

Twelve scripts live under `tools/legacy/`. Each generated part of the site
against the pre-Topic model: `weeks`/`totalWeeks`, "Week N" labels, dated
curriculum entries from a fixed 2028 start. Running one now would rewrite
`curriculum.js` back to a model the site no longer uses and reintroduce
publication dates, so they are out of `tools/` where a glob cannot reach them.
They are kept as the record of how each track was first produced.

`tools/` itself contains only scripts that work against the current model.
