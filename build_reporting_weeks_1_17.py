#!/usr/bin/env python3
"""Builds reporting-week-1.html and reporting-week-17.html from week 8.

Week 8 is the template because it is the same track and the same layout, and
copying it keeps the three pages structurally identical rather than drifting
apart the way a cross-track template would.

Week 1 is the ownership argument: five departments, five answers, no owner.
Week 17 is the revision argument: the deadline decides the quality, and an
unmanaged correction turns one day into several versions of itself.

No figures anywhere. The events behind both articles happened on jobs that
are not the $1M case study, and quantities from them would be numbers nobody
can reproduce (NOTES.md section 1, and the Track 4 audit).

Written to drafts/ rather than the site root. Weeks 2 to 7 do not exist yet,
so none of these can join the chain without pointing readers at gaps.

Idempotent.
"""
import re
import sys
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "drafts"
TEMPLATE = DRAFTS / "reporting-week-8.html"


FIGW = ('<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;'
        'border:1px solid #e2e8f0;">\n                                    {svg}\n'
        '                                    <figcaption style="margin-top:16px;font-size:13px;'
        'color:#64748b;line-height:1.6;">{cap}</figcaption>\n                                </figure>')

def fig(svg, cap):
    return ('<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;'
            'border:1px solid #e2e8f0;">\n                                    ' + svg +
            '\n                                    <figcaption style="margin-top:16px;font-size:13px;'
            'color:#64748b;line-height:1.6;">' + cap + '</figcaption>\n                                </figure>')


SVG_OPEN = '<svg viewBox="0 0 640 {h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">'


def box(x, y, w, h, title, sub="", tone="plain"):
    fill, stroke, tc, sc = {
        "plain": ("#fff", "#cbd5e1", "#334155", "#64748b"),
        "good": ("#ecfdf5", "#a7f3d0", "#047857", "#059669"),
        "bad": ("#fef2f2", "#fca5a5", "#b91c1c", "#dc2626"),
    }[tone]
    cx = x + w / 2
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>'
    out += f'<text x="{cx}" y="{y + 26}" text-anchor="middle" fill="{tc}" font-size="13" font-weight="700">{title}</text>'
    if sub:
        out += f'<text x="{cx}" y="{y + 46}" text-anchor="middle" fill="{sc}" font-size="11">{sub}</text>'
    return out


def head(t):
    return f'<text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" font-weight="700" letter-spacing="2">{t}</text>'


FIGURES = {
    1: [
        ("Five answers, all true, and no owner.",
         fig(SVG_OPEN.format(h=210) + head("ONE WRONG NUMBER, FIVE DEPARTMENTS")
             + box(20, 58, 116, 66, "Site", "planning wrote it")
             + box(148, 58, 116, 66, "Planning", "site reported it")
             + box(276, 58, 116, 66, "Engineering", "not from us")
             + box(404, 58, 116, 66, "QS", "ours differs")
             + box(532, 58, 88, 66, "HR", "attendance only")
             + '<text x="320" y="162" text-anchor="middle" fill="#b91c1c" font-size="13" font-weight="700">Owner: none</text>'
             + '<text x="320" y="184" text-anchor="middle" fill="#64748b" font-size="11">Every answer is correct. The question still has no address.</text>'
             + "</svg>",
             "Figure 1 &#8212; The number nobody wrote. Each department answers accurately about its own scope, and the sum of five accurate answers is that the figure belongs to no one.")),
        ("Six sources, six owners, six different closing dates. The report has one date on it.",
         fig(SVG_OPEN.format(h=250) + head("WHAT ONE PROGRESS FIGURE IS MADE OF")
             + box(20, 52, 190, 58, "Quantities", "site &#183; daily")
             + box(225, 52, 190, 58, "Hours", "timesheets &#183; weekly")
             + box(430, 52, 190, 58, "Materials", "store &#183; on delivery")
             + box(20, 124, 190, 58, "Current revision", "document control")
             + box(225, 124, 190, 58, "Sign-off", "QA/QC &#183; on inspection")
             + box(430, 124, 190, 58, "Committed cost", "commercial &#183; own cut-off")
             + '<text x="320" y="216" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">One monthly figure. One date on the cover.</text>'
             + "</svg>",
             "Figure 2 &#8212; Six inputs, six owners, six cut-off dates. The report carries a single date, which is the first thing that stops being true about it.")),
        ("A figure that gets quietly fixed in a spreadsheet is a figure nobody will defend three months later.",
         fig(SVG_OPEN.format(h=190) + head("TWO DIFFERENT JOBS")
             + box(40, 54, 250, 84, "Owns the data", "writes the number", "bad")
             + box(350, 54, 250, 84, "Owns the reliability", "finds who wrote it, checks it, says so", "good")
             + '<text x="320" y="168" text-anchor="middle" fill="#64748b" font-size="11.5">The second one can be defended in a room. The first one cannot.</text>'
             + "</svg>",
             "Figure 3 &#8212; The distinction the track is built on. A planner who writes the number owns a guess; a planner who corroborates it owns something that survives a challenge.")),
    ],
    2: [
        ("The sheet was designed to answer the questions somebody had at the time, and it answers those perfectly.",
         fig(SVG_OPEN.format(h=200) + head("WORKING BACKWARDS FROM AN OUTPUT")
             + box(210, 46, 220, 52, "Productivity by area", "the request")
             + box(16, 122, 190, 56, "Hours", "against an activity")
             + box(222, 122, 190, 56, "Quantities", "against a bill item")
             + box(428, 122, 190, 56, "Area", "never collected", "bad")
             + "</svg>",
             "Figure 1 &#8212; Two of the three inputs exist and have all year. The output is still impossible, and no redesign of the report recovers the third.")),
        ("None of that is visible from inside the file.",
         fig(SVG_OPEN.format(h=210) + head("WHO ELSE IS READING THIS TABLE")
             + box(210, 50, 220, 54, "The data table")
             + box(16, 130, 140, 52, "Monthly report", "")
             + box(172, 130, 140, 52, "Dashboard", "")
             + box(328, 130, 140, 52, "Automated refresh", "")
             + box(484, 130, 134, 52, "Somebody else", "")
             + "</svg>",
             "Figure 2 &#8212; The person with the file open is one consumer among several. Inserting a column in the middle breaks the others silently, and the symptom appears somewhere else two weeks later.")),
        ("It is the one thing everything else depends on, and every change to it costs something somewhere you cannot see.",
         fig(SVG_OPEN.format(h=180) + head("TWO LAYERS, TWO SPEEDS")
             + box(40, 50, 250, 72, "Reports", "change often, cheaply", "good")
             + box(350, 50, 250, 72, "Data source", "changes rarely, expensively", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Most reporting problems come from repairing the fast layer and leaving the slow one alone.</text>'
             + "</svg>",
             "Figure 3 &#8212; Fixing the symptom in each report is how a project ends up making the same correction in six places and still getting it wrong in a seventh.")),
    ],
    13: [
        ("What was never confirmed is the thing that actually matters, which is whether the previous version stopped being used.",
         fig(SVG_OPEN.format(h=200) + head("ONE REVISION ISSUED, SEVERAL IN USE")
             + box(210, 46, 220, 52, "Rev C issued", "transmittal recorded", "good")
             + box(16, 122, 190, 56, "Technical office", "has Rev C", "good")
             + box(222, 122, 190, 56, "Site crew", "printed Rev B", "bad")
             + box(428, 122, 190, 56, "Subcontractor", "not sent yet", "bad")
             + "</svg>",
             "Figure 1 &#8212; The issue was recorded and the register is accurate. What the register cannot show is which drawing is in somebody&#8217;s hand on the wall.")),
        ("it has not succeeded merely because a transmittal was sent.",
         fig(SVG_OPEN.format(h=180) + head("TWO HALVES OF THE SAME PROCESS")
             + box(40, 50, 250, 72, "Issue the new revision", "tracked everywhere", "good")
             + box(350, 50, 250, 72, "Withdraw the old one", "tracked almost nowhere", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Success is one valid revision in use, not a transmittal in the register.</text>'
             + "</svg>",
             "Figure 2 &#8212; Every project can show you the first column. The second is the one that decides whether two revisions are live on the same site.")),
        ("Three columns instead of one.",
         fig(SVG_OPEN.format(h=180) + head("WHAT THE REGISTER HAS TO RECORD")
             + box(24, 52, 186, 66, "Issued", "the email left")
             + box(226, 52, 186, 66, "Acknowledged", "they confirm they have it", "good")
             + box(428, 52, 186, 66, "Withdrawn", "old copy taken out, by name", "good")
             + '<text x="320" y="148" text-anchor="middle" fill="#64748b" font-size="11.5">The first is administration. The other two are the process.</text>'
             + "</svg>",
             "Figure 3 &#8212; Most registers hold only the first event, which is why they can be complete and accurate while two revisions are in use.")),
    ],
    25: [
        ("there is no reason for them to give the same answer.",
         fig(SVG_OPEN.format(h=190) + head("TWO METHODS, TWO QUESTIONS")
             + box(40, 52, 250, 76, "Progress", "how much of the work exists")
             + box(350, 52, 250, 76, "Valuation", "how much is payable this month")
             + '<text x="320" y="158" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">Different questions. Both answers correct. Different numbers.</text>'
             + "</svg>",
             "Figure 1 &#8212; The disagreement is structural rather than accidental, which is why it recurs every month on every project and cannot be designed away.")),
        ("Usually the gap splits into three parts.",
         fig(SVG_OPEN.format(h=190) + head("SPLITTING THE DIFFERENCE")
             + box(24, 52, 186, 76, "Timing", "resolves itself next month")
             + box(226, 52, 186, 76, "Measurement", "needs a decision")
             + box(428, 52, 186, 76, "Error", "the part still wrong after", "bad")
             + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">Only the third one survives the meeting.</text>'
             + "</svg>",
             "Figure 2 &#8212; The proportions matter more than the precision. Mostly timing is a calendar problem; mostly measurement is a rules problem that needed settling at the start.")),
        ("It is to refuse to publish two numbers that have not been reconciled.",
         fig(SVG_OPEN.format(h=180) + head("BEFORE, NOT AFTER")
             + box(40, 50, 250, 72, "Reconcile, then publish", "twenty minutes and a list", "good")
             + box(350, 50, 250, 72, "Publish, then explain", "two documents that disagree", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">The second is not reconciliation. It is damage control with an audience.</text>'
             + "</svg>",
             "Figure 3 &#8212; The constraint is organisational rather than analytical: the two closing dates must leave room for a short meeting between them.")),
    ],
    3: [
        ("It is not a sensible way to plan construction",
         fig(SVG_OPEN.format(h=190) + head("TWO WAYS TO ORGANISE THE SAME LIST")
             + box(40, 50, 250, 76, "By discipline", "how engineering is staffed", "good")
             + box(350, 50, 250, 76, "By activity released", "what a planner needs", "bad")
             + '<text x="320" y="160" text-anchor="middle" fill="#64748b" font-size="11.5">The second view exists on almost no project.</text>'
             + "</svg>",
             "Figure 1 &#8212; Both are legitimate. Only one answers whether next month can start, and building it is planning work nobody else will do.")),
        ("None of them tells a planner anything",
         fig(SVG_OPEN.format(h=200) + head("WHAT NINETY PERCENT MEANS")
             + box(16, 52, 190, 60, "Calculations done", "engineer A")
             + box(222, 52, 190, 60, "Internally checked", "engineer B")
             + box(428, 52, 190, 60, "Draft exists", "engineer C")
             + '<text x="320" y="146" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Cannot go to site &#8594; releases nothing</text>'
             + '<text x="320" y="172" text-anchor="middle" fill="#64748b" font-size="11.5">All three defensible inside the discipline. None usable as a readiness input.</text>'
             + "</svg>",
             "Figure 2 &#8212; From the construction side, a drawing at ninety percent that has not been released is worth the same as one nobody has started.")),
        ("Considerable progress on paper, no production in the field.",
         fig(SVG_OPEN.format(h=180) + head("TWO PROGRAMMES, ONE PROJECT")
             + box(40, 50, 250, 72, "Engineering at 95%", "by discipline sequence", "good")
             + box(350, 50, 250, 72, "Nothing can start", "the needed revision is not out", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Both statements true at the same time.</text>'
             + "</svg>",
             "Figure 3 &#8212; Reporting engineering progress against the construction sequence closes the gap, and usually requires nothing new to be collected.")),
    ],
    4: [
        ("there is no independent record that contradicts it",
         fig(SVG_OPEN.format(h=180) + head("WHAT CAN BE CHECKED, AND WHAT CANNOT")
             + box(40, 50, 250, 72, "Concrete, cable, steel", "somebody can go and look", "good")
             + box(350, 50, 250, 72, "A document at 40%", "no wall to check", "bad")
             + "</svg>",
             "Figure 1 &#8212; The softest number on the project is also the earliest, which means the first months of reporting rest on it.")),
        ("The curve looks healthy for four months and flat for six.",
         fig(SVG_OPEN.format(h=180) + head("WEIGHTING BY COUNT OR BY EFFORT")
             + box(40, 50, 250, 72, "By count", "races, then stalls", "bad")
             + box(350, 50, 250, 72, "By expected hours", "moves with the work", "good")
             + "</svg>",
             "Figure 2 &#8212; A hundred small documents and ten large ones produce a curve that is encouraging early and inexplicable later.")),
        ("Transmittals show what was actually issued",
         fig(SVG_OPEN.format(h=180) + head("TWO CORROBORATING RECORDS")
             + box(40, 50, 250, 72, "Transmittals", "an event with a date", "good")
             + box(350, 50, 250, 72, "Hours booked", "effort against claim", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Neither is conclusive. A large divergence is worth a question.</text>'
             + "</svg>",
             "Figure 3 &#8212; Stages assigned before anything leaves the department become visible the moment the register is compared with what was actually transmitted.")),
    ],
    5: [
        ("a revised delivery date is a piece of information that has no defined route",
         fig(SVG_OPEN.format(h=190) + head("WHERE THE DATE LIVES")
             + box(24, 52, 186, 72, "Vendor call", "yesterday", "good")
             + box(226, 52, 186, 72, "Expediting report", "next update cycle")
             + box(428, 52, 186, 72, "Programme", "still the old date", "bad")
             + "</svg>",
             "Figure 1 &#8212; Each step is slower than the last. A planner who relies only on the report is always a cycle behind the person who took the call.")),
        ("An item on its fourth revision is a different risk from one on its first",
         fig(SVG_OPEN.format(h=180) + head("TWO FIELDS THAT CHANGE THE PICTURE")
             + box(40, 50, 250, 72, "Promised date", "what everyone quotes")
             + box(350, 50, 250, 72, "Times revised", "what nobody counts", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">One column turns a status list into a risk list.</text>'
             + "</svg>",
             "Figure 2 &#8212; The count costs nothing to keep and separates a date backed by a shipping document from one that is last week plus seven days.")),
        ("These are links in one chain.",
         fig(SVG_OPEN.format(h=190) + head("ONE CHAIN, THREE DEPARTMENTS")
             + box(16, 56, 146, 60, "Vendor docs", "engineering")
             + box(172, 56, 146, 60, "Manufacturing", "procurement")
             + box(328, 56, 146, 60, "Shipment", "procurement")
             + box(484, 56, 134, 60, "On site", "construction")
             + '<text x="320" y="152" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">A three-week approval appears two months later as a late delivery.</text>'
             + "</svg>",
             "Figure 3 &#8212; Each department watches its own segment, so the delay is visible only at the end, in a form that hides where it started.")),
    ],
    12: [
        ("Both records are accurate and there is usually no link between them.",
         fig(SVG_OPEN.format(h=180) + head("TWO SYSTEMS, NO FIELD IN COMMON")
             + box(40, 50, 250, 72, "HSE records", "permit, incident, stand-down", "good")
             + box(350, 50, 250, 72, "Schedule records", "an activity that slipped", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">The delay has a duration and no cause.</text>'
             + "</svg>",
             "Figure 1 &#8212; Neither record is wrong. The link between them is what has to be reconstructed from memory a year later.")),
        ("A stoppage discovered a week later has already consumed the float",
         fig(SVG_OPEN.format(h=190) + head("WHEN THE STOPPAGE REACHES YOU")
             + box(24, 52, 186, 72, "Daily meeting", "same day", "good")
             + box(226, 52, 186, 72, "Daily report", "next morning")
             + box(428, 52, 186, 72, "Variance analysis", "days later", "bad")
             + "</svg>",
             "Figure 2 &#8212; The third case is the common one, and by then the float that could have absorbed it has been spent elsewhere.")),
        ("A one-word cause field on the progress update",
         fig(SVG_OPEN.format(h=180) + head("THE CHEAPEST CONTEMPORANEOUS RECORD")
             + box(24, 50, 186, 68, "Delay, no cause", "unusable later", "bad")
             + box(226, 50, 186, 68, "Cause of variance", "one word, short list", "good")
             + box(428, 50, 186, 68, "Delay analysis", "built from records", "good")
             + "</svg>",
             "Figure 3 &#8212; Seconds per line on the progress update, and it is the difference between an analysis built from evidence and one built from recollection.")),
    ],
    18: [
        ("The only document in the room that could change next week is the one that gets the least attention.",
         fig(SVG_OPEN.format(h=180) + head("WHERE THE HOUR GOES")
             + box(40, 50, 250, 72, "Explaining last week", "most of the meeting", "bad")
             + box(350, 50, 250, 72, "Planning next week", "ten minutes left", "bad")
             + "</svg>",
             "Figure 1 &#8212; Each explanation is reasonable and takes four minutes. The document that could change something is reached when nobody is concentrating.")),
        ("the document has changed function and nobody has noticed",
         fig(SVG_OPEN.format(h=190) + head("THE TEST")
             + box(40, 52, 250, 72, "Mostly new items", "a plan", "good")
             + box(350, 52, 250, 72, "Mostly repeats", "an explanation list", "bad")
             + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">Count how many items were in last week&#39;s look-ahead as well.</text>'
             + "</svg>",
             "Figure 2 &#8212; The repeats are blocked work sitting in a planning document instead of in a constraint log where somebody would have to close it.")),
        ("A look-ahead written by planning is a proposal.",
         fig(SVG_OPEN.format(h=180) + head("WHO WROTE IT DECIDES WHAT IT IS")
             + box(40, 50, 250, 72, "Written by construction", "a commitment", "good")
             + box(350, 50, 250, 72, "Written by planning", "a proposal", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">The difference has nothing to do with the quality of the document.</text>'
             + "</svg>",
             "Figure 3 &#8212; When project controls writes it because the site sent too little, the plan for next week belongs to the person who will do none of it.")),
    ],
    19: [
        ("What takes the last days of the month is reaching a figure that more than one department will stand behind.",
         fig(SVG_OPEN.format(h=180) + head("WHERE THE MONTH-END TIME GOES")
             + box(24, 50, 186, 72, "Collection", "slow, predictable")
             + box(226, 50, 186, 72, "Reconciliation", "the real work", "bad")
             + box(428, 50, 186, 72, "Producing it", "an afternoon", "good")
             + "</svg>",
             "Figure 1 &#8212; The middle column is invisible from outside, which is why the monthly report is underestimated by everybody who does not produce one.")),
        ("the document is really five documents bound together",
         fig(SVG_OPEN.format(h=190) + head("SAME REPORT, DIFFERENT PAGES")
             + box(16, 52, 146, 68, "Management", "summary only")
             + box(172, 52, 146, 68, "Project manager", "indicators")
             + box(328, 52, 146, 68, "Department heads", "own section")
             + box(484, 52, 134, 68, "Client", "progress, risk")
             + '<text x="320" y="158" text-anchor="middle" fill="#64748b" font-size="11.5">The pages nobody reaches still have to be right.</text>'
             + "</svg>",
             "Figure 2 &#8212; The one month somebody does turn to page eleven is the month something has gone wrong.")),
        ("The narrative is what somebody reads two years later",
         fig(SVG_OPEN.format(h=180) + head("TWO LIVES OF ONE PARAGRAPH")
             + box(40, 50, 250, 72, "Vague", "&#8220;below plan due to factors&#8221;", "bad")
             + box(350, 50, 250, 72, "Specific", "cause, activities, response", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Same length. Useful now, and evidence later.</text>'
             + "</svg>",
             "Figure 3 &#8212; Specific sentences are harder to agree in the last two days of the month, which is exactly why they go missing.")),
    ],
    6: [
        ("Each figure is larger than the next, and the gaps between them can be months.",
         fig(SVG_OPEN.format(h=180) + head("ONE BILL ITEM, FOUR QUANTITIES")
             + box(16, 56, 146, 60, "Delivered", "on site")
             + box(172, 56, 146, 60, "In store", "accepted")
             + box(328, 56, 146, 60, "Issued", "gone to a crew")
             + box(484, 56, 134, 60, "Installed", "the only progress", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Each smaller than the last. Three of them are logistics.</text>'
             + "</svg>",
             "Figure 1 &#8212; All four are correct at the same moment. Reports that do not say which one they mean end up using different ones.")),
        ("It has left the store, so the store thinks it is used.",
         fig(SVG_OPEN.format(h=180) + head("THE QUANTITY NOBODY CAN SEE")
             + box(40, 50, 250, 72, "Store", "records it as issued")
             + box(350, 50, 250, 72, "Survey", "cannot see it on the wall")
             + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Issued and not installed is invisible to both.</text>'
             + "</svg>",
             "Figure 2 &#8212; It appears at reconciliation, when the project finds it has paid for more than exists.")),
        ("What you are looking for is not exactness.",
         fig(SVG_OPEN.format(h=170) + head("WHAT THE GAP TELLS YOU")
             + box(40, 48, 250, 66, "Installed &#8810; issued", "material sitting in the field", "bad")
             + box(350, 48, 250, 66, "Issued &#8810; delivered", "normal early, odd late")
             + "</svg>",
             "Figure 3 &#8212; Direction and size, once a month, for the handful of materials the job turns on. Per bill item is unmanageable and nobody does it.")),
    ],
    7: [
        ("They are answers to three different questions",
         fig(SVG_OPEN.format(h=190) + head("THREE SOURCES, THREE ANSWERS")
             + box(24, 52, 186, 72, "Bill", "what was priced")
             + box(226, 52, 186, 72, "Drawing", "what should exist")
             + box(428, 52, 186, 72, "Survey", "what does exist")
             + '<text x="320" y="158" text-anchor="middle" fill="#64748b" font-size="11.5">None of them is wrong. Only one belongs in a given document.</text>'
             + "</svg>",
             "Figure 1 &#8212; The three diverge as soon as the design moves, and they never converge again.")),
        ("the denominator stayed still while the numerator grew",
         fig(SVG_OPEN.format(h=180) + head("WHAT A VARIATION DOES")
             + box(40, 50, 250, 72, "Drawing quantity", "increases", "bad")
             + box(350, 50, 250, 72, "Bill quantity", "unchanged")
             + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">The percentage moves with nothing built.</text>'
             + "</svg>",
             "Figure 2 &#8212; It looks exactly like a data error, which is why it is worth recognising as the mechanism it is.")),
        ("Either you restate it or you note it.",
         fig(SVG_OPEN.format(h=170) + head("WHEN THE DENOMINATOR CHANGES")
             + box(40, 48, 250, 66, "Restate the series", "honest, visible", "good")
             + box(350, 48, 250, 66, "Say nothing", "continuous and false", "bad")
             + "</svg>",
             "Figure 3 &#8212; Doing neither produces a curve that looks smooth across a scope change, which is the version everybody finds hardest to explain later.")),
    ],
    10: [
        ("The total is correct. Both productivity figures are not.",
         fig(SVG_OPEN.format(h=190) + head("WHERE THE HOURS ACTUALLY WENT")
             + box(40, 50, 250, 72, "Attendance total", "reconciles to the gate", "good")
             + box(350, 50, 250, 72, "Hours per activity", "written from memory", "bad")
             + '<text x="320" y="160" text-anchor="middle" fill="#64748b" font-size="11.5">Productivity is built on the second one.</text>'
             + "</svg>",
             "Figure 1 &#8212; The reliability of the total is why the problem underneath survives so long unexamined.")),
        ("A crane that was available all month and used for a fifth of it",
         fig(SVG_OPEN.format(h=180) + head("PLANT: TWO DIFFERENT PROBLEMS")
             + box(40, 50, 250, 72, "Available, idle", "nothing to do")
             + box(350, 50, 250, 72, "Not available", "broken down", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">A record that shows only presence cannot tell them apart.</text>'
             + "</svg>",
             "Figure 2 &#8212; Availability is recorded well almost everywhere. Utilisation is the figure that would change a decision.")),
        ("Allocation error mostly cancels within an area",
         fig(SVG_OPEN.format(h=180) + head("THE LEVEL AT WHICH THE NUMBERS HOLD")
             + box(40, 50, 250, 72, "By area", "error largely cancels", "good")
             + box(350, 50, 250, 72, "By activity", "error does not", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Report the first. Resisting the second is a defensible position.</text>'
             + "</svg>",
             "Figure 3 &#8212; Aggregating before drawing conclusions costs nothing and is the difference between a usable figure and noise.")),
    ],
    11: [
        ("how does a percentage go down?",
         fig(SVG_OPEN.format(h=180) + head("THE ONLY INPUT THAT SUBTRACTS")
             + box(40, 50, 250, 72, "Quantities, hours, cost", "accumulate", "good")
             + box(350, 50, 250, 72, "Non-conformance", "takes work back", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Most reporting systems have no mechanism for the second.</text>'
             + "</svg>",
             "Figure 1 &#8212; When a percentage cannot go down, it does not. The activity keeps its figure and consumes its resources twice.")),
        ("Only the last category should move the percentage backwards",
         fig(SVG_OPEN.format(h=190) + head("NOT EVERY NCR REVERSES PROGRESS")
             + box(24, 52, 186, 72, "Documentation", "no effect")
             + box(226, 52, 186, 72, "Accepted as-is", "no effect")
             + box(428, 52, 186, 72, "Redo required", "reverses", "bad")
             + '<text x="320" y="160" text-anchor="middle" fill="#64748b" font-size="11.5">Somebody has to categorise each one, before the event rather than after.</text>'
             + "</svg>",
             "Figure 2 &#8212; Without the rule, the person updating the sheet leaves the number alone, and they are being sensible.")),
        ("the workable answer is a rework flag rather than a separate account",
         fig(SVG_OPEN.format(h=180) + head("WHERE REWORK HOURS LAND")
             + box(24, 50, 186, 72, "Original activity", "crew looks slow", "bad")
             + box(226, 50, 186, 72, "General code", "grows all year", "bad")
             + box(428, 50, 186, 72, "Same activity, flagged", "visible", "good")
             + "</svg>",
             "Figure 3 &#8212; The flag keeps the cost where the work happened and makes the second attempt countable, which is the only way anything is learned from it.")),
    ],
    20: [
        ("Each document is defensible and the three totals differ by a little.",
         fig(SVG_OPEN.format(h=190) + head("FOUR DOCUMENTS, FOUR DATES")
             + box(16, 52, 146, 68, "Client report", "prepared first")
             + box(172, 52, 146, 68, "Internal report", "two days later", "bad")
             + box(328, 52, 146, 68, "Dashboard", "refreshed again", "bad")
             + box(484, 52, 134, 68, "Foreman&#39;s list", "own source", "bad")
             + '<text x="320" y="158" text-anchor="middle" fill="#64748b" font-size="11.5">All defensible. None reconciling.</text>'
             + "</svg>",
             "Figure 1 &#8212; The cost is not the discrepancy. It is that the first person to find it now has reason to check everything else.")),
        ("The reports differ in level. They never differ in content.",
         fig(SVG_OPEN.format(h=200) + head("ONE CUT, FOUR VIEWS")
             + box(210, 46, 220, 52, "One data set", "one cut-off", "good")
             + box(16, 122, 146, 56, "Activity", "")
             + box(172, 122, 146, 56, "Discipline", "")
             + box(328, 122, 146, 56, "Trend", "")
             + box(484, 122, 134, 56, "Contract", "")
             + "</svg>",
             "Figure 2 &#8212; Exceptions are applied at the source. If an item is provisional, it is provisional in all four.")),
        ("The shape follows the decision each reader has to take",
         fig(SVG_OPEN.format(h=180) + head("NOT THE SAME DOCUMENT, SHORTENED")
             + box(40, 50, 250, 72, "Four shapes", "each follows a decision", "good")
             + box(350, 50, 250, 72, "One shape, trimmed", "detail deleted", "bad")
             + "</svg>",
             "Figure 3 &#8212; A construction manager needs a different cut, not a shorter one. Deleting rows produces a document nobody can act on.")),
    ],
    21: [
        ("Neither of them misread anything.",
         fig(SVG_OPEN.format(h=190) + head("SAME SCREEN, DIFFERENT CONCLUSIONS")
             + box(210, 46, 220, 52, "One dashboard", "accurate, current", "good")
             + box(40, 122, 250, 56, "&#8220;Recoverable&#8221;", "reads it through deliveries")
             + box(350, 122, 250, 56, "&#8220;Not recoverable&#8221;", "remembers the rework")
             + "</svg>",
             "Figure 1 &#8212; Both are reasoning correctly from the same display. The display carries the numbers and not what is behind them.")),
        ("it looks exactly like one that was counted",
         fig(SVG_OPEN.format(h=200) + head("WHAT A TILE CANNOT SHOW")
             + box(16, 52, 190, 60, "Two definitions", "shows one, says nothing", "bad")
             + box(222, 52, 190, 60, "Two cut-off dates", "different months, side by side", "bad")
             + box(428, 52, 190, 60, "Estimated figure", "looks like a measured one", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">Every one of these renders identically.</text>'
             + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">Readers fill the gap from whatever they happen to know that week.</text>'
             + "</svg>",
             "Figure 2 &#8212; The problems are all upstream, and none of them is visible at the point where the argument happens.")),
        ("it makes the disagreement look professional",
         fig(SVG_OPEN.format(h=180) + head("WHAT IT CAN AND CANNOT DO")
             + box(40, 50, 250, 72, "Organisation aligned", "makes it visible and useful", "good")
             + box(350, 50, 250, 72, "Organisation not aligned", "renders the disagreement well", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">A tool cannot produce an agreement that does not exist.</text>'
             + "</svg>",
             "Figure 3 &#8212; Projects buy dashboards expecting alignment. What arrives is a better rendering of a disagreement that was already there.")),
    ],
    22: [
        ("A project can have a perfectly healthy set of indicators in the month before everything stops.",
         fig(SVG_OPEN.format(h=180) + head("WHAT THE PACK MEASURES")
             + box(40, 50, 250, 72, "Progress, SPI, CPI", "a period that ended")
             + box(350, 50, 250, 72, "About next month", "usually nothing", "bad")
             + "</svg>",
             "Figure 1 &#8212; Accurate, necessary, and silent about what is coming. Management therefore responds a cycle late, every time.")),
        ("all of them are already being collected somewhere on your project for another purpose",
         fig(SVG_OPEN.format(h=190) + head("FOUR THAT LOOK FORWARD")
             + box(16, 52, 146, 68, "Constraints closed", "week 9")
             + box(172, 52, 146, 68, "Turnaround", "week 15")
             + box(328, 52, 146, 68, "Ready workfronts", "against need")
             + box(484, 52, 134, 68, "Drawing release", "vs sequence")
             + '<text x="320" y="158" text-anchor="middle" fill="#64748b" font-size="11.5">None is progress. All of them predict it.</text>'
             + "</svg>",
             "Figure 2 &#8212; Each of these is already recorded somewhere for a different reason, which makes the first version cheap to produce.")),
        ("It is a narrative, and it means the estimating",
         fig(SVG_OPEN.format(h=180) + head("THE FIGURE THAT ALWAYS LANDS JUST UNDER")
             + box(40, 50, 250, 72, "Measured", "moves unevenly", "good")
             + box(350, 50, 250, 72, "Managed", "one point below plan", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Indicators nobody is judged on stay honest longer.</text>'
             + "</svg>",
             "Figure 3 &#8212; Consistency of that kind is not a sign of control. It is a sign that the estimate is being tuned to the report.")),
    ],
    9: [
        ("They are what the word ready means when nobody has defined it.",
         fig(SVG_OPEN.format(h=230) + head("ONE ACTIVITY, SIX ANSWERS")
             + box(20, 54, 190, 58, "Engineering", "IFC not issued", "bad")
             + box(225, 54, 190, 58, "Store", "material not out", "bad")
             + box(430, 54, 190, 58, "Construction", "crane elsewhere", "bad")
             + box(20, 126, 190, 58, "Subcontractor", "gang elsewhere", "bad")
             + box(225, 126, 190, 58, "HSE", "no work permit", "bad")
             + box(430, 126, 190, 58, "QA/QC", "no inspection request", "bad")
             + '<text x="320" y="208" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">Site: &#8220;The area is ready.&#8221;</text>'
             + "</svg>",
             "Figure 1 &#8212; Every answer is correct within its own scope. None of the six can see the other five, which is why the activity was in the programme and still could not start.")),
        ("Six tests, derived from six complaints.",
         fig(SVG_OPEN.format(h=200) + head("THE SIX READINESS TESTS")
             + box(16, 56, 196, 56, "Drawing", "current revision, issued")
             + box(222, 56, 196, 56, "Material", "at the workface")
             + box(428, 56, 196, 56, "Plant", "available that day")
             + box(16, 124, 196, 56, "Labour", "trade and size allocated")
             + box(222, 124, 196, 56, "Permit", "activity, place, date")
             + box(428, 124, 196, 56, "Access", "predecessor signed off")
             + "</svg>",
             "Figure 2 &#8212; Not a framework borrowed from elsewhere. Each test is the negative of something that has already stopped work on the job you are on.")),
        ("Only one of them is a plan.",
         fig(SVG_OPEN.format(h=210) + head("THE ACTIVITY THAT NEVER LEAVES")
             + box(24, 56, 130, 56, "Week 1", "not ready", "bad")
             + box(172, 56, 130, 56, "Week 2", "not ready", "bad")
             + box(320, 56, 130, 56, "Week 3", "not ready", "bad")
             + box(468, 56, 148, 56, "Week 4", "still listed", "bad")
             + '<text x="320" y="146" text-anchor="middle" fill="#b91c1c" font-size="13" font-weight="700">Never removed. Never started. Always in the look-ahead.</text>'
             + '<text x="320" y="176" text-anchor="middle" fill="#64748b" font-size="11.5">What the site will build, and what the project wants built, stop being the same list.</text>'
             + "</svg>",
             "Figure 3 &#8212; Nothing dramatic happens in any single week. After a few of them the look-ahead has quietly changed from an instruction into an expectation.")),
    ],
    14: [
        ("asking it to is your problem rather than the storekeeper&#39;s.",
         fig(SVG_OPEN.format(h=210) + head("ONE NOTE, ONE CODE, SEVERAL DESTINATIONS")
             + box(210, 50, 220, 58, "Delivery note", "one project code")
             + box(16, 132, 190, 56, "Work item A", "some of it")
             + box(222, 132, 190, 56, "Work item B", "some of it")
             + box(428, 132, 190, 56, "Work item C", "the rest")
             + '<text x="320" y="122" text-anchor="middle" fill="#64748b" font-size="11.5">correct for logistics &#183; approximate for cost</text>'
             + "</svg>",
             "Figure 1 &#8212; The note proves goods arrived and were accepted, which is what it was built to do. Where the material went afterwards is a question it was never asked.")),
        ("They are the most certain of the three and the slowest, which is exactly the wrong combination for a monthly report.",
         fig(SVG_OPEN.format(h=190) + head("THREE COMMERCIAL RECORDS, THREE LAGS")
             + box(24, 54, 180, 76, "Commitment", "earliest &#183; least certain")
             + box(230, 54, 180, 76, "Accrual", "estimated by definition")
             + box(436, 54, 180, 76, "Invoice", "latest &#183; most certain", "good")
             + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">Certainty and timeliness move in opposite directions.</text>'
             + "</svg>",
             "Figure 2 &#8212; The record you can rely on most is the one that arrives too late to report, which is why accruals carry the weight and the argument.")),
        ("the most common way a cost report and a progress report come to disagree.",
         fig(SVG_OPEN.format(h=180) + head("TWO MONTH-ENDS")
             + box(40, 52, 250, 72, "Finance close", "financial calendar")
             + box(350, 52, 250, 72, "Progress close", "progress calendar")
             + '<text x="320" y="150" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">Work done in one. Cost landed in the other. Both records right.</text>'
             + "</svg>",
             "Figure 3 &#8212; Nothing is wrong on either side. Earned value calculated across the two dates is wrong anyway, which is what the reconciliation exists to catch.")),
    ],
    26: [
        ("not a report that was wrong, a report that was right and changed nothing.",
         fig(SVG_OPEN.format(h=200) + head("THE LINE THAT NEVER LEFT THE REPORT")
             + box(24, 54, 130, 56, "Week 1", "raised", "bad")
             + box(172, 54, 130, 56, "Week 2", "raised again", "bad")
             + box(320, 54, 130, 56, "Week 3", "raised again", "bad")
             + box(468, 54, 148, 56, "Week 4", "it happens", "bad")
             + '<text x="320" y="146" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">&#8220;Why did nobody see this coming?&#8221;</text>'
             + '<text x="320" y="174" text-anchor="middle" fill="#64748b" font-size="11.5">Repetition reads as diligence when writing and as background when reading.</text>'
             + "</svg>",
             "Figure 1 &#8212; The report was accurate every week. Accuracy was never the thing that was missing.")),
        ("A statement of fact does not create an obligation.",
         fig(SVG_OPEN.format(h=190) + head("TWO WAYS TO WRITE THE SAME ITEM")
             + box(30, 54, 265, 84, "A situation", "&#8220;The revision has not arrived.&#8221;", "bad")
             + box(345, 54, 265, 84, "A decision", "who, by when, and the consequence", "good")
             + '<text x="320" y="168" text-anchor="middle" fill="#64748b" font-size="11.5">One can be agreed with and left alone. The other cannot, quite as easily.</text>'
             + "</svg>",
             "Figure 2 &#8212; The rewrite is small and the difference is not in emphasis. A named person with a named consequence is harder to read past.")),
        ("to be the evidence a year from now",
         fig(SVG_OPEN.format(h=180) + head("ONE DOCUMENT, TWO TIMESCALES")
             + box(40, 52, 250, 72, "This week", "change a decision")
             + box(350, 52, 250, 72, "A year from now", "prove what was known", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">It often fails at the first while doing the second perfectly.</text>'
             + "</svg>",
             "Figure 3 &#8212; A warning nobody acted on is still the record that explains the delay afterwards, which is why it is written even on the weeks it changes nothing.")),
    ],
    15: [
        ("It is duration and permission, and it belongs in the programme rather than in a correspondence file.",
         fig(SVG_OPEN.format(h=190) + head("WHAT THE CLIENT SIDE ACTUALLY SUPPLIES")
             + box(24, 52, 186, 76, "Instruction", "changes what is built")
             + box(226, 52, 186, 76, "Approval", "decides when it can start")
             + box(428, 52, 186, 76, "Comment", "neither approved nor rejected", "bad")
             + '<text x="320" y="160" text-anchor="middle" fill="#64748b" font-size="11.5">None of the three is a number. All three move dates.</text>'
             + "</svg>",
             "Figure 1 &#8212; Every other source hands you a quantity. This one hands you permission and delay, which is why it belongs in the programme.")),
        ("Planning against the contractual figure produces a programme that assumes the fast case every time.",
         fig(SVG_OPEN.format(h=180) + head("TWO TURNAROUNDS")
             + box(40, 50, 250, 72, "What the contract allows", "a limit", "good")
             + box(350, 50, 250, 72, "What actually happens", "a distribution", "bad")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Plan against the second. There are hundreds of submittals.</text>'
             + "</svg>",
             "Figure 2 &#8212; The contractual period is a ceiling rather than a forecast, and a programme built on it is optimistic on every single submittal.")),
        ("Multiply it by a few requests a week",
         fig(SVG_OPEN.format(h=190) + head("THE REQUEST WITH NO RECORD")
             + box(40, 50, 250, 76, "Formal correspondence", "logged, assignable, countable", "good")
             + box(350, 50, 250, 76, "Direct message", "answered, then invisible", "bad")
             + '<text x="320" y="160" text-anchor="middle" fill="#64748b" font-size="11.5">Both take the same time. Only one appears in any plan.</text>'
             + "</svg>",
             "Figure 3 &#8212; Answering is not the problem. A request that leaves no trace cannot be prioritised, reassigned or explained a month later.")),
    ],
    16: [
        ("The report that combines them describes a month that nobody actually had.",
         fig(SVG_OPEN.format(h=190) + head("ONE MONTH, THREE CLOSING DATES")
             + box(24, 52, 186, 76, "Finance", "corporate calendar")
             + box(226, 52, 186, 76, "Project controls", "progress cut-off")
             + box(428, 52, 186, 76, "Measurement", "contract period")
             + '<text x="320" y="162" text-anchor="middle" fill="#b91c1c" font-size="12.5" font-weight="700">All three defensible. None of them the same month.</text>'
             + "</svg>",
             "Figure 1 &#8212; Nobody chose this. The three dates were inherited separately and have never been looked at on one page.")),
        ("The progress figure is simply describing a slightly different period from the one on the cover.",
         fig(SVG_OPEN.format(h=180) + head("TWO TERMS THAT ARE NOT THE SAME")
             + box(40, 50, 250, 72, "Data date", "a property of the schedule")
             + box(350, 50, 250, 72, "Cut-off", "a property of the process")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">They should coincide. When they do not, nothing looks wrong.</text>'
             + "</svg>",
             "Figure 2 &#8212; A schedule updated to one date and quantities collected to another produce a figure that is quietly about a different period.")),
        ("They need a list, made each month, of what crossed the boundary",
         fig(SVG_OPEN.format(h=190) + head("WHAT FALLS BETWEEN TWO DATES")
             + box(24, 52, 186, 68, "Work done after cut-off")
             + box(226, 52, 186, 68, "Material in the gap")
             + box(428, 52, 186, 68, "Late measurement")
             + '<text x="320" y="152" text-anchor="middle" fill="#334155" font-size="12.5" font-weight="700">One list, twenty minutes, most of the argument gone.</text>'
             + "</svg>",
             "Figure 3 &#8212; Without the list each side treats these items by its own logic, correctly, and the difference surfaces later as an apparent error.")),
    ],
    23: [
        ("The call is for solving. The email is the record of how it was solved.",
         fig(SVG_OPEN.format(h=180) + head("TWO CHANNELS, TWO JOBS")
             + box(40, 50, 250, 72, "The call", "resolves in four minutes", "good")
             + box(350, 50, 250, 72, "The email", "survives four months", "good")
             + '<text x="320" y="150" text-anchor="middle" fill="#64748b" font-size="11.5">Write first, then ring. The order is the whole habit.</text>'
             + "</svg>",
             "Figure 1 &#8212; Neither channel replaces the other. Reversing the order is what leaves a decision with no record of how it was reached.")),
        ("Five steps, and projects routinely execute the first three and abandon the last two.",
         fig(SVG_OPEN.format(h=180) + head("THE CHAIN")
             + box(16, 56, 116, 56, "Meeting", "", "good")
             + box(142, 56, 116, 56, "Minutes", "", "good")
             + box(268, 56, 116, 56, "Action", "", "good")
             + box(394, 56, 116, 56, "Follow-up", "skipped", "bad")
             + box(520, 56, 100, 56, "Closed", "unknown", "bad")
             + '<text x="320" y="148" text-anchor="middle" fill="#64748b" font-size="11.5">The fourth step is the one that decides whether the item comes back next week.</text>'
             + "</svg>",
             "Figure 2 &#8212; Most projects run the first three well. Without the fourth, nobody can distinguish an item that was closed from one that was never closed.")),
        ("An action with a stated cost is harder to leave alone than one without.",
         fig(SVG_OPEN.format(h=190) + head("WHAT AN ACTION NEEDS")
             + box(16, 52, 146, 68, "A person", "not a department")
             + box(172, 52, 146, 68, "A date", "makes follow-up possible")
             + box(328, 52, 146, 68, "Done looks like", "settles disputed closure")
             + box(484, 52, 134, 68, "If not done", "changes behaviour", "good")
             + "</svg>",
             "Figure 3 &#8212; Three fields carry the weight. The fourth is optional and does more than the other three together.")),
    ],
    24: [
        ("They are stages of the same thing, and the value is in the arrows rather than the lists.",
         fig(SVG_OPEN.format(h=220) + head("TWO CHAINS THROUGH EIGHT REGISTERS")
             + box(24, 50, 170, 54, "Assumption", "stops holding")
             + box(236, 50, 170, 54, "Risk", "occurs")
             + box(448, 50, 170, 54, "Change or delay", "", "bad")
             + box(24, 128, 170, 54, "Interface", "unresolved")
             + box(236, 128, 170, 54, "Constraint", "not closed")
             + box(448, 128, 170, 54, "Delay", "", "bad")
             + '<text x="320" y="204" text-anchor="middle" fill="#64748b" font-size="11.5">The earlier in a chain you catch it, the cheaper it is.</text>'
             + "</svg>",
             "Figure 1 &#8212; Read this way the registers stop being a filing convention and become a description of how a problem matures.")),
        ("It is that nothing connects them to a decision or an action, so the register can only add.",
         fig(SVG_OPEN.format(h=190) + head("SIX ACCUMULATE, TWO CLOSE")
             + box(40, 50, 250, 76, "Six registers", "record that it exists", "bad")
             + box(350, 50, 250, 76, "Decision &amp; action", "the only mechanisms", "good")
             + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">A register that only grows is one with nothing attached to it.</text>'
             + "</svg>",
             "Figure 2 &#8212; The other six can record that something stopped existing. They cannot cause it, which is why they fill up.")),
        ("State needs the arrows. Inventory does not.",
         fig(SVG_OPEN.format(h=190) + head("TWO KINDS OF REGISTER")
             + box(40, 50, 250, 76, "State", "open, unresolved, waiting", "good")
             + box(350, 50, 250, 76, "Inventory", "what exists and where")
             + '<text x="320" y="162" text-anchor="middle" fill="#64748b" font-size="11.5">Only one of them describes something that can get worse.</text>'
             + "</svg>",
             "Figure 3 &#8212; Submittal logs and material reports are inventories. Treating all fifteen lists as equally important is how the useful ones get lost.")),
    ],
    17: [
        ("Same document. One is an observation and the other is a recollection, and no amount of formatting will tell the two apart afterwards.",
         fig(SVG_OPEN.format(h=210) + head("THE SAME FORM, THREE DEADLINES")
             + box(20, 56, 186, 70, "Due 07:00", "before the site can check", "bad")
             + box(227, 56, 186, 70, "Due 14:00", "after a morning walk", "good")
             + box(434, 56, 186, 70, "Next day", "checked and measured", "good")
             + '<text x="113" y="152" text-anchor="middle" fill="#dc2626" font-size="11.5" font-weight="600">remembered</text>'
             + '<text x="320" y="152" text-anchor="middle" fill="#059669" font-size="11.5" font-weight="600">counted</text>'
             + '<text x="527" y="152" text-anchor="middle" fill="#059669" font-size="11.5" font-weight="600">counted</text>'
             + '<text x="320" y="184" text-anchor="middle" fill="#64748b" font-size="11.5">The form did not change. The data did.</text>'
             + "</svg>",
             "Figure 1 &#8212; The deadline is the variable. Nothing about the template decides whether a field holds a measurement or a memory; the hour it is due decides it.")),
        ("both of them believe they are looking at the daily report for the fourteenth.",
         fig(SVG_OPEN.format(h=200) + head("ONE DAY, THREE VERSIONS OF ITSELF")
             + box(30, 56, 170, 62, "Issued", "same filename")
             + box(235, 56, 170, 62, "Corrected", "same filename", "bad")
             + box(440, 56, 170, 62, "Corrected again", "same filename", "bad")
             + '<text x="320" y="146" text-anchor="middle" fill="#b91c1c" font-size="13" font-weight="700">No revision number. No note. No record that anything changed.</text>'
             + '<text x="320" y="174" text-anchor="middle" fill="#64748b" font-size="11.5">Three people, three files, one date, and each believes theirs is the report.</text>'
             + "</svg>",
             "Figure 2 &#8212; Where the versions come from. Every correction along that row was right. What was missing at each step was the record that a correction had happened.")),
        ("It costs nothing to count, it cannot be gamed by sending an emptier report earlier",
         fig(SVG_OPEN.format(h=190) + head("TWO WAYS TO JUDGE A DAILY REPORT")
             + box(40, 54, 250, 84, "Went out on time", "easy to measure, easy to hit", "bad")
             + box(350, 54, 250, 84, "Never revised after", "cannot be gamed by hurrying", "good")
             + '<text x="320" y="168" text-anchor="middle" fill="#64748b" font-size="11.5">Track both. Only one of them tells you about the data.</text>'
             + "</svg>",
             "Figure 3 &#8212; Timeliness is a proxy, and proxies become targets. Counting the reports that were never revised measures the thing timeliness was standing in for.")),
    ],
}


# --------------------------------------------------------------------------

W1 = dict(
    week=1,
    file="reporting-week-1.html",
    h1="Nobody owns this number.",
    title="Who owns a project number — data ownership in project controls",
    desc=("A wrong figure goes round five departments and comes back unclaimed. What project "
          "controls actually produces, what feeds it, and why the planner owns the reliability "
          "of a number rather than the number itself."),
    og="Nobody owns this number",
    share="A wrong number went round five departments and came back unclaimed. Every answer was true. That is the problem.",
    crumb="What project controls produces, and what it must be fed",
    short="What it produces, what it needs",
    body='''<h2 style="margin-top:0;">Nobody owns this number</h2>
                            <p>A quantity in the monthly report turns out to be wrong. Not catastrophically &#8212; wrong enough that somebody asks where it came from.</p>
                            <p>Site says planning wrote it. Planning says site reported it. Engineering says it did not come from them. The quantity surveyor says their measurement was always different. HR says they only keep attendance.</p>
                            <p>Five answers, all true, and no owner. The number went round the whole project and came back unclaimed.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>That is not a discipline problem and it is not a software problem. Every one of those five people did their job. What was missing was written down nowhere: which of them the number belonged to.</p>

                            <h2>What project controls actually produces</h2>
                            <p>Start from the output, because the inputs only make sense backwards from it.</p>
                            <p>A project controls function produces a small number of things. A schedule and its updates. A progress figure. A cost report and a forecast. A cash flow. A look-ahead. A set of registers. A monthly report, and the four or five slides somebody presents from it.</p>
                            <p>That is most of it. Everything else is an intermediate step on the way to one of those, and every one of them exists to answer a question somebody is going to act on. The schedule answers when. The forecast answers how much, in the end. The look-ahead answers what can start on Monday.</p>
                            <p>None of them are produced by project controls. All of them are assembled by project controls out of material that belongs to other people.</p>

                            <h2>Working backwards from a deliverable</h2>
                            <p>Take any one of those outputs and ask three questions about every field in it. What is this? Who produces it? In what unit, and on which day does it close?</p>
                            <p>Do that with a monthly progress figure and the answer is not one department. It is quantities from site, measured or estimated. Hours from the timesheets. Materials from the store and from delivery notes. Approved drawings from document control, because work cannot be claimed on a drawing that was superseded. Inspection sign-off from QA/QC. Committed cost from the commercial team, on their own cut-off date rather than yours.</p>
                            <p>Six sources, six owners, six different closing dates. The report has one date on it.</p>
                            <p>This is the whole reason the first half of this track is organised by department rather than by document. You cannot understand a monthly report by studying the monthly report. You understand it by knowing what each department can and cannot give you, and when.</p>

                            <h2>Why the ownership question is the one that matters</h2>
                            <p>Every input on that list has somebody whose job it is to know it. The site engineer knows what was built. The storekeeper knows what left the warehouse. Document control knows which revision is current. The quantity surveyor knows what was measured for payment.</p>
                            <p>Trouble starts when project controls fills a gap instead of naming it. The number is late, the report is due, so the planner estimates it. Once. Then it happens again, and after a few months the planner is not assembling the project's data, the planner is producing it.</p>
                            <p>At that point the question &#8220;whose number is this?&#8221; has no answer, and it has no answer precisely when you need one &#8212; when it turns out to be wrong.</p>

                            <h2>The planner owns the reliability, not the number</h2>
                            <p>Here is the distinction this entire track is built on, and it is worth stating plainly before any technique.</p>
                            <p>The planner does not own the data. The planner owns whether the data can be believed.</p>
                            <p>Those are different jobs and they need different behaviour. Owning the data means you write it. Owning its reliability means you find out who wrote it, check it against something produced independently, and refuse to publish a figure that nothing corroborates without saying so.</p>
                            <p>It also means you do not correct somebody else's number on your own. When two records disagree, the correction goes back to the person who reported it and the department that holds the contradicting record, together, and it stays open until they agree. A figure that gets quietly fixed in a spreadsheet is a figure nobody will defend three months later.</p>

                            <h2>The report is the last thing you build</h2>
                            <p>When a report comes out wrong, the first instinct is almost always to change the report. A column gets added to the spreadsheet. The dashboard is rebuilt. The chart is swapped for a better chart.</p>
                            <p>The report is rarely where the problem started. If a field was collected in three different ways by three different people, no amount of formatting reconciles them afterwards. If a field was never collected at all, it cannot appear in an output however the output is designed. The report can only be as accurate as the thing feeding it.</p>
                            <p>Which gives an order of work, and it runs the opposite way to how most people approach it. The data model is designed first. Then the data is collected. Then it is verified. The report is what comes out at the end.</p>
                            <p>In practice you will rarely design that model. Most planners inherit one &#8212; the coding structure was set before they arrived, the system was chosen by somebody else, and the input sheets already exist. The realistic version of this work is not designing from nothing. It is understanding what you have been given, then finding the fields a report needs that the input sheet never had.</p>
                            <p>Either way the principle holds: a mistake is not corrected in thirty reports. It is corrected once, in the place it is born.</p>
                            <p>It is worth saying plainly, because most writing on this subject assumes the opposite. The best project controls system is not the one designed from nothing. It is the one that can take a system somebody else built, with everything already running on it, and make what comes out of it reliable. That is the job almost everybody actually has.</p>

                            <h2>What this track is</h2>
                            <p>Five tracks taught what to do with a number once you have it. <a href="week-13.html">Schedule Week 13</a> works out float. <a href="cost-week-11.html">Cost &amp; Cash Week 11</a> turns quantities into percent complete. <a href="risk-week-8.html">Risk Week 8</a> puts a distribution around a duration. Every one assumes the number is already on your desk and is roughly true.</p>
                            <p>This track is about how it got there. The first half goes department by department: what each one can tell you, what it cannot, and when it closes. The second half is what you issue back.</p>
                            <p>The name is slightly misleading, and it is worth saying so at the start. Reporting here is not the writing of reports. It is the trade that makes a report possible, and the writing is the smallest part of it.</p>

                            <h2>Practical insight</h2>
                            <p>Open your last monthly report and pick any five numbers from it. Next to each one, write a name. Not a department &#8212; a person, the one who would have to answer if that figure were challenged in a meeting tomorrow.</p>
                            <p>You will get three kinds of answer. Some have an obvious owner and you can write the name without thinking. Some have an owner you are not certain of, which means the number has been arriving for months without anybody confirming it. And some, when you are honest, have your name against them.</p>
                            <p>That third group is your real exposure. Every one of those is a number you produced because somebody else did not, and every one of them will come back to you the first time it matters.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Project controls produces perhaps eight or nine things. Every one is assembled out of material owned by somebody else.</li>
                            <li>Work backwards from a deliverable: what is each field, who produces it, in what unit, and on which day does it close.</li>
                            <li>A single monthly progress figure draws on six departments with six different cut-off dates. The report carries one date.</li>
                            <li>The failure is not a wrong number. It is a number with no owner, discovered at the moment it is challenged.</li>
                            <li>Filling a gap once is help. Filling it every month makes the planner the producer of data they cannot verify.</li>
                            <li>The planner owns the reliability of a figure, not the figure itself.</li>
                            <li>Corrections go back to the reporter and the record holder together, never into a spreadsheet quietly.</li>
                            <li>A report can only be as accurate as what feeds it. Changing the report does not fix the collection.</li>
                            <li>Data model, then collection, then verification, then report. The report is the output, not the starting point.</li>
                            <li>Most planners inherit a model rather than design one. The real work is finding the field the input sheet never had.</li>
                            <li>The best system is not the one built from nothing. It is the one that makes an inherited system reliable.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Before any department, the method. If a report can only be as good as its inputs, the way to find the weak one is to start at the output and walk backwards.</p>
                            <p>Next week: working backwards from a deliverable &#8212; and why the shape of a data table is a contract rather than a spreadsheet.</p>''',
)

W17 = dict(
    week=17,
    file="reporting-week-17.html",
    h1="The deadline writes the report.",
    title="The daily report — deadlines, revisions and the version problem",
    desc=("The hour a daily report is due decides how much of it was counted and how much was "
          "guessed. Why silent corrections create several versions of one day, and what makes "
          "a report defensible."),
    og="The deadline writes the report",
    share="Ask for the report at seven and you asked the site to remember. Ask at two and they can count.",
    crumb="The shortest document with the most consequences",
    short="The daily report",
    body='''<h2 style="margin-top:0;">The deadline writes the report</h2>
                            <p>Three projects, three clients, one document. On the first, yesterday's daily report is due by two in the afternoon. On the second, by seven the next morning. On the third, some time during the following day.</p>
                            <p>The form is nearly identical on all three. The data in it is not remotely the same, and the reason has nothing to do with the form.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>Ask for a report by seven in the morning and you have asked the site to describe work that finished after the crew went home. Nobody walked the floor. Nobody checked with the surveyor. The foreman gave a number from memory, at the gate, on his way out, because the alternative was leaving the field blank.</p>
                            <p>Ask for the same report by the afternoon and that foreman has had a morning. He can look at what was actually poured, ask the storekeeper what went out, and give you something he counted.</p>
                            <p>Same document. One is an observation and the other is a recollection, and no amount of formatting will tell the two apart afterwards.</p>

                            <h2>The report before the report</h2>
                            <p>None of this arrives as a report. It arrives as messages.</p>
                            <p>Two hundred lines a day, from a dozen people, in whatever form was quickest for them. Some send a spreadsheet. Some send a photograph of a handwritten sheet. Some send a voice note that says they finished the area they were on today &#8212; not which area, not how much, not against which line of the bill.</p>
                            <p>The first job of the day is therefore not writing a report. It is translation: turning a dozen formats into one, and going back for the three quarters of it that cannot be used as sent. That is where the evening goes, and it is why the report is late even when everybody sent something on time.</p>
                            <p>A common template does not fix the deadline problem, but it removes the translation. When every discipline fills the same sheet, in your units, against your activity codes, the evening stops being spent on interpretation. It gets spent on checking &#8212; which is the job.</p>

                            <h2>Not this evening</h2>
                            <p>Some numbers genuinely are not known at the deadline. The concrete is still going in. The survey has not been done. Nobody is being difficult; the day simply has not finished producing its own data.</p>
                            <p>So the sentence arrives: we do not know that yet, can we correct it tomorrow?</p>
                            <p>Say yes and you have made a promise most projects then break, because tomorrow has its own report. Say no and you get a made-up number, which is worse. The honest answer is a third one: publish it as not yet reported, and hold the field open. A blank that everybody can see is a smaller problem than a figure that quietly turns out to be wrong.</p>

                            <h2>How one day becomes three versions of itself</h2>
                            <p>Here is the failure that costs the most and gets discussed the least.</p>
                            <p>A correction comes in two days later. The file is updated. The new file goes out with the same name, into the same folder, and takes the place of the old one. No revision number, no note saying what changed, no record that anything changed at all.</p>
                            <p>Do that for a few months and the project has several versions of the same day in circulation. Somebody is working from the file they downloaded in March, somebody else from the one that replaced it in April, and both of them believe they are looking at the daily report for the fourteenth.</p>
                            <p>Nobody is at fault at any single step. Every correction was right. What was missing was the record that a correction had happened.</p>
                            <p>Contract Week 1 was about a notice reaching the right address. This is the same problem one level down: a document that changes without announcing that it changed is a document nobody can rely on, however accurate its latest version is.</p>

                            <h2>The measure that actually matters</h2>
                            <p>Most projects judge a daily report on whether it went out on time. That is the wrong test, or at least an incomplete one.</p>
                            <p>The better test is how much it changes afterwards. A report published at seven that gets corrected three times is worth less than one published at two that stands. Timeliness is easy to measure and easy to hit, which is exactly why it becomes the target &#8212; and why the thing it is a proxy for gets lost.</p>
                            <p>So measure both. Track the proportion of a month's daily reports that were never revised after publication. It costs nothing to count, it cannot be gamed by sending an emptier report earlier, and it tells you something the delivery time never will.</p>

                            <h2>Why anyone reads it at all</h2>
                            <p>On most days, nobody does. The daily report goes into a folder and stays there, and it is tempting to conclude that the effort is wasted.</p>
                            <p>Then something happens. An extension of time claim needs to show which days were lost to weather. A dispute over a delivery needs the date material actually arrived. An incident investigation needs to know who was on site and what plant was running. A concrete result comes back low and somebody needs the pour date and the temperature.</p>
                            <p>All of that comes from the daily report, months or years later, and none of it can be reconstructed if the report was not kept. Claims Week 6 makes the contemporaneous record the strongest evidence there is. This is where that record is either made or not made, on an ordinary evening when nothing is at stake.</p>

                            <h2>Practical insight</h2>
                            <p>Find out two things about your own project this week, and neither takes long.</p>
                            <p>First, why the deadline is the hour it is. Ask. It is usually inherited from a meeting that no longer happens, or from a client representative who wanted it before their own morning call. If the reason has expired, moving it three hours can do more for your data than any change to the form.</p>
                            <p>Second, count how many of last month's daily reports were revised after they were issued, and whether the revision was recorded anywhere. If you cannot answer the second half, you already know what to fix first.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The deadline decides how much of a daily report was counted and how much was remembered.</li>
                            <li>A report due before the site can check its own work is a report of estimates, whatever the form asks for.</li>
                            <li>Site data arrives as messages in a dozen formats. A common template removes the translation, not the deadline.</li>
                            <li>&#8220;We will correct it tomorrow&#8221; is a promise projects break. Publish the field as not yet reported instead.</li>
                            <li>A correction that replaces a file without a revision record creates several versions of the same day.</li>
                            <li>Judge a report by how little it changes after publication, not only by whether it went out on time.</li>
                            <li>Nobody reads the daily report until a claim, an incident or a quality failure needs it &#8212; and then it cannot be reconstructed.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>The daily report says what happened. The weekly one has to say what happens next, which is a harder document to write and a much harder one to be wrong in.</p>
                            <p>Next week: the weekly report and the look-ahead &#8212; and the only part of either that anybody acts on.</p>''',
)

W9 = dict(
    week=9,
    file="reporting-week-9.html",
    h1="Ready means six different things.",
    title="Readiness in construction planning — why a look-ahead becomes a wish list",
    desc=("Six departments, six definitions of ready, and no shared one. How unready work rolls "
          "from look-ahead to look-ahead until the short-term plan stops describing what will "
          "actually be built."),
    og="Ready means six different things",
    share="Six departments, six definitions of ready, and none of them written down. That is how a look-ahead becomes a wish list.",
    crumb="Workfront, constraints and what ready actually means",
    body='''<h2 style="margin-top:0;">Ready means six different things</h2>
                            <p>A meeting, and one question: why has this not started?</p>
                            <p>The site says the area is ready. Planning says the programme allows it. Engineering says the drawing has not been issued for construction yet. QA/QC says no inspection request has been raised. Construction says the crane is in another zone today. The store says the material has not gone out. Somebody adds that the work permit was never obtained, and somebody else that the subcontractor put their gang somewhere else this morning.</p>
                            <p>Every one of those is true. I have heard all of them, on different jobs, in different countries, years apart. Put together in one meeting they look like a bad project. They are not. They are what the word ready means when nobody has defined it.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>The activity was in the programme. It was in the look-ahead. Everybody had agreed to it the previous Friday. And it could not start, because ready is an adjective and six people were using it about six different things.</p>

                            <h2>The six tests are already in the complaints</h2>
                            <p>You do not need a standard to work out what ready should mean on your job. The definition is sitting inside what people say when work fails to start.</p>
                            <p>Somebody said the drawing is not issued for construction. That is <strong>drawing readiness</strong>: a current revision exists, is approved, and has reached the people who will build from it.</p>
                            <p>Somebody said the material has not left the store. That is <strong>material readiness</strong>: the quantity is on site, released, and physically at the workface rather than in a laydown area two kilometres away.</p>
                            <p>Somebody said the crane is in another zone. That is <strong>plant readiness</strong>: the equipment the method needs is available on the day, not merely owned by the project.</p>
                            <p>Somebody said the gang went elsewhere. That is <strong>labour readiness</strong>: a crew of the right trade and size is actually allocated, which is a different question from whether the headcount exists.</p>
                            <p>Somebody said the permit was never obtained. That is <strong>permit readiness</strong>: the authorisations for that activity, in that location, on that day.</p>
                            <p>And the inspection request nobody raised is <strong>access and predecessor readiness</strong>: the preceding work has been signed off, and the area is handed over and physically reachable.</p>
                            <p>Six tests, derived from six complaints. Not a framework borrowed from somewhere else &#8212; a list of the things that have already stopped work on your own project.</p>

                            <h2>Why one owner is never enough</h2>
                            <p>The reason readiness is difficult has nothing to do with any single department being slow.</p>
                            <p>Each of the six belongs to a different person. Drawings to engineering. Material to procurement and the store. Plant to construction. Labour to the subcontractor. Permits to HSE or to the client. Access to whoever finished the work before.</p>
                            <p>None of them can see the other five. Engineering can be entirely confident the drawing went out, and be right, while the crane is somewhere else. Six people each doing their job correctly still produces an activity that cannot start, and no one of them is in a position to notice.</p>
                            <p>That gap is what a workfront view is for. It is not a planning technique. It is the one place where all six are looked at together, against a single piece of work, before somebody is sent to do it.</p>

                            <h2>The constraint that was closed in a meeting</h2>
                            <p>Constraints get recorded in whatever was to hand. A spreadsheet on one job. Meeting minutes on another. The workfront sheet itself. On more jobs than I would like, nowhere at all.</p>
                            <p>The recording is not really the problem. Closure is.</p>
                            <p>Somebody says it is sorted, and everybody moves on. Nobody writes down who sorted it, on what date, or on what evidence. The following week the same item comes up again, and the same conversation happens, and it is impossible to tell whether it was never closed or closed and then broken again by something else.</p>
                            <p>A constraint log that records only the constraint is half a log. What matters is the closure: who, when, and what proves it. Until that exists, a project cannot answer the only question that counts on a Thursday afternoon, which is what is genuinely clear to start on Monday.</p>

                            <h2>How a look-ahead turns into a wish list</h2>
                            <p>Here is the failure this whole week is about, and it happens quietly enough that most projects never name it.</p>
                            <p>An activity is not ready, so it does not start. It also does not get removed. It stays on the same dates, appears in the next look-ahead, and everybody assumes it will go this time. It does not. It appears again the week after. And again.</p>
                            <p>Nothing dramatic happens at any single step. But after two months the look-ahead has stopped describing what the site is going to build and started describing what the project would like the site to build. The two documents look identical. Only one of them is a plan.</p>
                            <p>Once that has happened the damage spreads. The foreman stops treating the look-ahead as instruction, because half of it did not happen last week either. Progress forecasts inherit the same optimism. And the reported percentage drifts for exactly the reason <a href="reporting-week-8.html">Week 8</a> described, except that here the cause is upstream of the measurement: work that was never going to start was counted as work that was about to.</p>

                            <h2>What a definition would actually cost</h2>
                            <p>I should be straight about this. I have not seen a written definition of ready that was genuinely used by everybody on a project. Checklists existed. Look-ahead meetings existed. Workfront sheets existed. A single set of criteria that engineering, the store, HSE and the subcontractor all applied the same way did not.</p>
                            <p>That is worth saying because it tells you where the difficulty sits. Writing the six tests takes an afternoon. Getting six departments to accept that an activity is not ready until all six are satisfied is a different matter, because it means an activity nobody objected to can still be refused, and that feels to each department like being blocked by somebody else's paperwork.</p>
                            <p>The argument that works is not a procedural one. It is that the alternative is sending a crew to a workface where they cannot work, which every one of those six people has watched happen and none of them enjoyed.</p>

                            <h2>Practical insight</h2>
                            <p>Take next week's look-ahead and go through it once with the six tests, before the meeting rather than in it.</p>
                            <p>For each activity, ask the six questions in order: drawing, material, plant, labour, permit, access. Do not ask whether it is ready. Ask each one separately, because the whole point is that the word hides which of the six is missing.</p>
                            <p>Then count. If more than a third of the list fails at least one test, you are not looking at a plan, and no amount of chasing on Monday morning will turn it into one. Take those activities out, tell the meeting why, and let the look-ahead be shorter and true.</p>
                            <p>The second part is harder than the first, and it is the part that changes the project.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Ready is an adjective, and six departments use it about six different things.</li>
                            <li>The six tests are already in the complaints: drawing, material, plant, labour, permit, access.</li>
                            <li>Each test has a different owner, and none of the six can see the other five.</li>
                            <li>A workfront view is not a planning technique. It is the one place all six are checked against one piece of work.</li>
                            <li>Recording a constraint is half the job. Closure needs who, when, and what proves it.</li>
                            <li>Unready work is rarely removed from the programme. It rolls into the next look-ahead, and the next.</li>
                            <li>After a few months the look-ahead describes what the project wants rather than what the site will build. The two documents look the same.</li>
                            <li>Writing the definition takes an afternoon. Getting six departments to be bound by it is the actual work.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Readiness decides whether work can start. The next question is what it costs while it runs, and that number comes from two places that rarely agree: the timesheet and the plant log.</p>
                            <p>Next week: hours and plant &#8212; allocation, availability, utilisation, and the difference between a man being present and a man being on your activity.</p>''',
)


W14 = dict(
    week=14,
    file="reporting-week-14.html",
    h1="The delivery note was never built for this.",
    title="Commercial data for planners — commitments, cut-off dates and cost allocation",
    desc=("A delivery note is correct for logistics and insufficient for cost allocation. Why the "
          "commercial ledger closes on a different date than progress, and what the planner can "
          "and cannot do about it."),
    og="The delivery note was never built for this",
    share="A delivery note is a correct document. It was just never designed to answer the question you are asking it.",
    crumb="Commitments, accruals and invoices on somebody else\u2019s cut-off",
    body='''<h2 style="margin-top:0;">The delivery note was never built for this</h2>
                            <p>Material arrives. Somebody signs for it. The note carries one project code, and into the cost ledger it goes, against one work item.</p>
                            <p>Then you look at where the material actually went. Shared consumables in particular &#8212; paint, fasteners, pipe, cable &#8212; rarely go to one place. The same consignment gets drawn down across several work items and several locations over the following days, and the single code on the note stops describing anything real.</p>
                            <p>This is not an error. The note is correct. It was produced to prove that goods arrived and were accepted, and it does that perfectly. It was never designed to allocate cost, and asking it to is your problem rather than the storekeeper&#39;s.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>That distinction runs through this whole week. Almost every record the commercial side gives you is accurate for its own purpose and approximate for yours.</p>

                            <h2>What the commercial side actually holds</h2>
                            <p>Three things reach you from that direction, and they behave differently.</p>
                            <p><strong>Commitments</strong> are money the project has promised: orders placed, subcontracts signed. They exist long before anything is spent, and they are the earliest warning you get that a package is going to cost more than the budget said.</p>
                            <p><strong>Accruals</strong> are work done but not yet invoiced. They are an estimate by definition, and they are the line where your progress figure and the ledger touch each other most directly.</p>
                            <p><strong>Invoices</strong> are what has actually been billed. They are the most certain of the three and the slowest, which is exactly the wrong combination for a monthly report.</p>
                            <p><a href="cost-week-10.html">Cost &amp; Cash Week 10</a> teaches what these are and how they behave inside one set of books. This week is about receiving them from somebody else, in their format, on their timetable.</p>

                            <h2>The code is where it breaks</h2>
                            <p>Every cost that arrives is tagged to something, and the tag came from the code of accounts the project set up before any of this started. <a href="cost-week-6.html">Cost &amp; Cash Week 6</a> is where that structure gets built, and it is worth reading again from this side.</p>
                            <p>The problem is not that the coding is wrong. It is that the commercial breakdown and the physical breakdown were designed to answer different questions. Commercial needs a structure that maps to the contract and to payment. Planning needs one that maps to where work happens. On a good project these two are reconciled at the start; on most, they are cousins rather than twins, and a cost that lands cleanly in one lands ambiguously in the other.</p>
                            <p>Shared material makes this visible faster than anything else, which is why it is worth watching. If you can explain where a consignment of cable went, you can usually explain the rest of the ledger.</p>

                            <h2>On somebody else&#39;s calendar</h2>
                            <p>None of it arrives when you want it. Finance closes on a financial calendar and you close on a progress one, so a delivery note that lands late or a measurement finished a few days after your cut-off is counted in a different month by each of you.</p>
                            <p>That is a calendar problem rather than a commercial one and it belongs later in the track, where all three of a project&#39;s closing dates can be looked at together. What matters here is narrower: the cost figures you receive were closed to a date that is not yours, and using them as though they were is the most common way a cost report and a progress report come to disagree.</p>

                            <h2>The cost that has not been billed yet</h2>
                            <p>Accruals deserve a moment on their own, because they are the line where the two sides of the project touch most directly and disagree most easily.</p>
                            <p>An accrual is an estimate of work done but not yet invoiced, and somebody has to make it. Where it is made from a progress percentage, it inherits everything <a href="reporting-week-8.html">Week 8</a> described: if the underlying quantity was estimated rather than measured, the accrual carries that optimism straight into the cost report, where it looks like a hard figure.</p>
                            <p>Which is a reason to know how your project&#39;s accruals are built. If the answer is that they come from your progress number, then your progress number is doing two jobs, and an error in it is now an error in two documents rather than one.</p>

                            <h2>Whose job it is to notice</h2>
                            <p>Finding this sort of thing is not the planner&#39;s responsibility, and the correction is not the planner&#39;s decision. But the planner is usually the one who spots it, for a structural reason: project controls is the only function that sits with the site record, the survey measurement, the store movement and the ledger open at the same time. Nobody else has cause to compare them.</p>
                            <p>So the pattern that works is the one from <a href="reporting-week-8.html">Week 8</a>, applied to a different pair of records. Write down which two disagree and by roughly how much. Send it to the commercial team and the store, with the site engineer copied, because they are the ones who know where the material went. Then let commercial decide, because the allocation is theirs to make.</p>
                            <p>Planning does not manage cost. Planning makes the inconsistency visible to the people who do.</p>

                            <h2>Practical insight</h2>
                            <p>Pick one shared material on your project &#8212; something that goes to several places, such as cable, fasteners or paint. Take last month&#39;s deliveries of it and ask two questions.</p>
                            <p>First: how many work items does the ledger think it went to? Usually one, sometimes two.</p>
                            <p>Second: how many does the site say it went to? Ask the engineer, not the system.</p>
                            <p>If those two answers are different, you have found something worth an email rather than an argument. And you have found it on the one material where it is easiest to demonstrate, which is why it is the one to start with.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A delivery note is correct for logistics and insufficient for cost allocation. It was built for a different question.</li>
                            <li>Shared consumables expose the gap first, because a single code cannot describe several destinations.</li>
                            <li>Commitments, accruals and invoices arrive with different certainty and different lag.</li>
                            <li>Commercial coding maps to the contract. Physical coding maps to where work happens. They are cousins, not twins.</li>
                            <li>Finance and progress close on different dates, and work done in one month can land as cost in the next.</li>
                            <li>Agree both cut-off dates, write them down, and reconcile the items that crossed the boundary before publishing.</li>
                            <li>Accruals built from a progress percentage inherit whatever was wrong with that percentage, into a second document.</li>
                            <li>The planner notices because the planner is the only one with all the records open. The allocation decision still belongs to commercial.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Everything so far has come from inside the project. The last source is outside it, and it does not send data at all.</p>
                            <p>Next week: the client and the consultant &#8212; instructions, approvals, comments, and why a turnaround time is a programme input rather than an administrative detail.</p>''',
)

W26 = dict(
    week=26,
    file="reporting-week-26.html",
    h1="Nobody acted on it.",
    title="Why project reports get ignored — writing for decisions rather than record",
    desc=("A warning sits in the report for weeks, then arrives anyway and nobody remembers being "
          "told. Why reports get ignored, and what putting the decisions on the first page does "
          "and does not fix."),
    og="Nobody acted on it",
    share="The warning was in the report for weeks. When it happened, the question was why nobody had said anything.",
    crumb="The most common failure in project controls",
    body='''<h2 style="margin-top:0;">Nobody acted on it</h2>
                            <p>The same line goes into the report week after week. The drawing revision has not arrived. The equipment has not shipped. The area is still under another subcontractor&#39;s control and access has not been given.</p>
                            <p>Every week it is read out. Every week somebody says it will be resolved shortly. The activity stays in the look-ahead, and the line stays in the report.</p>
                            <p>Then it happens. The delivery is late and it hits the critical path, or the revision arrives and part of what was already built has to be looked at again. And in the meeting afterwards, the question is why nobody saw this coming.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>It had been in the report for a month. That is the failure this week is about, and it is the most common one in the trade: not a report that was wrong, a report that was right and changed nothing.</p>

                            <h2>Why it is not a writing problem</h2>
                            <p>The temptation is to conclude that the warning was not clear enough, or not loud enough, and to write it in bold next time.</p>
                            <p>That rarely works, because the reason nothing happened usually has nothing to do with the sentence. It is that the report said a thing was going to be a problem without saying what anybody was supposed to do about it, who was supposed to do it, or what it would cost if they did not. A statement of fact does not create an obligation. Somebody reading it can agree with every word and still have nothing to act on.</p>
                            <p>And there is a second reason, less comfortable. A risk raised every week for a month stops sounding like a warning and starts sounding like background. The repetition that feels like diligence to the person writing it feels like noise to the person reading it.</p>

                            <h2>What a report is competing with</h2>
                            <p>The people who could act on that line are reading it alongside twenty other things, most of which are already on fire. A ten-page document arriving on a Monday does not get read in order. It gets skimmed for whatever the reader is currently worried about.</p>
                            <p>So the middle of page six is not a place where decisions happen, regardless of what is written there. That is not carelessness on the reader&#39;s part. It is what happens to any long document sent to somebody with a full day.</p>

                            <h2>Moving the decisions to the front</h2>
                            <p>What I found helped &#8212; not solved, helped &#8212; was to stop lengthening the report and start rearranging it.</p>
                            <p>The items that needed a decision went to the first page. Not the summary of progress, not the curve. Three questions, in plain language: what decision is needed this week, who has to take it, and what happens if it is not taken.</p>
                            <p>The effect was modest and real. Those items came up earlier in meetings and came up more often. It did not resolve every one of them, and plenty still sat there for weeks. What it changed was the chance of an important item being missed entirely, which is a smaller claim than solving the problem and a more honest one.</p>
                            <p>The mechanism is not mysterious. A named person with a named consequence is harder to leave alone than a paragraph describing a situation.</p>

                            <h2>The report that proves it later</h2>
                            <p>Here is the part that makes the whole thing worth doing even when nobody acts.</p>
                            <p>The line in the report did not change anything at the time. Months later it is the reason the delay can be explained, and it is the difference between a claim that is supported and one that is asserted. <a href="claim-week-6.html">Claims Week 6</a> sets out why the contemporaneous record carries the weight it does. This is where that record is either created or not, on an ordinary Monday when the warning is being ignored.</p>
                            <p>So the answer to a report nobody reads is not to stop writing it. It is to write it knowing it has two jobs on two timescales &#8212; to change a decision this week, and to be the evidence a year from now &#8212; and to accept that it will often fail at the first while doing the second perfectly.</p>

                            <h2>Where this leaves the trade</h2>
                            <p>Twenty-five weeks of this track have been about one thing: a number arrives from somebody, it means something specific, it closes on a particular day, and it can be checked against a record produced for another purpose.</p>
                            <p>None of that matters if the report built from it changes nothing. The last skill is the one that is hardest to teach and easiest to recognise &#8212; writing so that a person who is busy, sceptical and already behind can see what they are being asked to decide.</p>
                            <p>A planner who assembles accurate numbers that nobody acts on has done most of the job. The remaining part is not more data.</p>

                            <h2>Practical insight</h2>
                            <p>Open your last four weekly reports side by side and look for a line that appears in all four.</p>
                            <p>There will usually be one. When you find it, ask three questions of it. Does it say who has to act? Does it say by when? Does it say what happens if nobody does?</p>
                            <p>If the answer to all three is no, the item was never a request. It was a note, repeated four times, and the person you needed was reading it as background. Rewrite that one line as a decision with a name and a date, put it at the top of next week&#39;s report, and see whether anything different happens.</p>
                            <p>Sometimes nothing does. But you will have found out something useful either way, which is whether the problem was the message or the room.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The common failure is not a wrong report. It is a right one that changed nothing.</li>
                            <li>A statement of fact creates no obligation. A decision with an owner and a consequence does.</li>
                            <li>A warning repeated weekly stops reading as a warning and starts reading as background.</li>
                            <li>Long documents are skimmed for whatever the reader is already worried about. Page six is not where decisions happen.</li>
                            <li>Moving the decisions to the first page reduces the chance of an item being missed. It does not make people act.</li>
                            <li>An ignored warning still does the second job: it is the contemporaneous record that explains the delay later.</li>
                            <li>Accurate numbers that change no decision are most of the work and not the whole of it.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>This track assumed one thing throughout: that every record you chased belonged to the same project, under one contract, with one chain of command.</p>
                            <p>What follows is where that assumption stops holding &#8212; when the scope sits with another company, when the critical path runs through somebody else&#39;s purchase order, and when the number you are reconciling has two owners in two organisations who both produced it correctly.</p>''',
)


W2 = dict(
    week=2,
    file="reporting-week-2.html",
    h1="The column that was never collected.",
    title="Working backwards from a deliverable — data models for project reporting",
    desc=("A report needs a field the input sheet never had. How to work backwards from an output "
          "to its inputs, and why the shape of a data table is a contract rather than a spreadsheet."),
    og="The column that was never collected",
    share="A report cannot produce a field that was never collected. No amount of redesign fixes a column that does not exist.",
    crumb="Output, inputs, owners, units",
    body='''<h2 style="margin-top:0;">The column that was never collected</h2>
                            <p>Somebody asks for productivity by area. Reasonable question, and the data appears to exist &#8212; hours are recorded, quantities are recorded, both have been collected all year.</p>
                            <p>Then you look at the sheet. Hours are captured against an activity. Quantities are captured against a bill item. Neither of them records the area. The number cannot be produced, not because the report is badly designed, but because a column that was never collected cannot be recovered afterwards.</p>
                            <p>This is the ordinary failure, and it is worth being precise about why it happens. Nobody made a mistake. The sheet was designed to answer the questions somebody had at the time, and it answers those perfectly.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Start at the output</h2>
                            <p>The method is the same every time, and it runs backwards from the thing you have to produce.</p>
                            <p>Name the deliverable. List every field that appears in it. For each field, answer four questions: what exactly is it, who produces it, in what unit, and on which day does it close. Then go and look at whether the input sheet actually holds it.</p>
                            <p>Most of the time it does. The value of the exercise is the handful of fields where it does not, because those are the outputs you are currently producing by estimating, by asking somebody informally, or by not producing at all.</p>
                            <p>Do it once for the monthly report and you will find two or three. That is a normal result and a useful one.</p>

                            <h2>The same field, three units</h2>
                            <p>The second thing the exercise finds is subtler than a missing column, and harder to see: a field that exists but does not mean the same thing twice.</p>
                            <p>Pipework reported by one crew in metres and by another in joints. Concrete recorded as poured by the site and as delivered by the store. Hours entered by some supervisors as attended and by others as worked. Each entry is defensible. Aggregated, they produce a total that is not a quantity of anything.</p>
                            <p>This does not show up as an error, which is why it survives. Every row looks reasonable. It shows up as a productivity figure that moves for no reason, or a curve that behaves oddly in one area and not another.</p>
                            <p>So the unit is part of the field definition rather than a note beside it. If a column can be filled in two ways, it will be, and the correction is made once in the sheet rather than every month in the analysis.</p>

                            <h2>You will not be designing this from scratch</h2>
                            <p>Most planners arrive to a system that already exists. The coding structure was set before you got there. The input sheets are in use. Thirty reports are built on top of them, and people are used to filling them in.</p>
                            <p>So the realistic version of this work is not designing a model. It is understanding the one you inherited well enough to find its gaps, and adding what is missing without breaking what already works.</p>
                            <p>That second half is where the difficulty sits, and it has almost nothing to do with the data.</p>

                            <h2>A data table is an interface</h2>
                            <p>Here is the part that is easy to get wrong and expensive to get wrong.</p>
                            <p>Once a table has been in use for a while, the person opening the file is not its only user. Reports read it. A dashboard reads it. Somebody&#39;s automated refresh reads it. A colleague&#39;s calculation points at a particular column by position. None of that is visible from inside the file.</p>
                            <p>Which means the shape of the table has quietly become a contract. Insert a column in the middle and everything downstream that referenced positions is now reading the wrong thing, and it will not announce itself. It shows up two weeks later, in somebody else&#39;s output, as a number that looks slightly odd.</p>
                            <p>So the rule is not that tables cannot change. It is that they change in one direction. New fields are added at the end. Existing columns keep their position and their meaning. If a column has to be retired, it is emptied rather than deleted, at least until you know what was reading it.</p>
                            <p>This is not a spreadsheet rule and it does not depend on which software you use. It is what happens to any shared data source once more than one thing consumes it.</p>

                            <h2>When the field cannot be added</h2>
                            <p>Sometimes the answer is that it cannot be collected. The work is finished, or the crew has demobilised, or capturing it would take longer than the output is worth.</p>
                            <p>The honest response is to say so rather than to derive it. A figure assembled from a proxy, published without saying it was assembled from a proxy, is exactly the unmeasured number the rest of this track is about &#8212; except that this time you produced it yourself.</p>
                            <p>Report what you have, mark what you do not, and add the field going forward. Nobody is harmed by a gap they were told about. They are harmed by a number that looked like the others.</p>

                            <h2>What stays still and what moves</h2>
                            <p>There are two layers here and they change at different speeds.</p>
                            <p>Reports change constantly. A new manager wants a different summary. A client asks for another chart. The monthly gets restructured. All of that is normal and none of it is expensive.</p>
                            <p>The data source underneath should be close to stationary. It is the one thing everything else depends on, and every change to it costs something somewhere you cannot see.</p>
                            <p>Most reporting problems come from doing this backwards: leaving the collection alone because it is working, and repairing the symptom in each report as it appears. That is how a project ends up with the same correction made in six places and still wrong in a seventh.</p>

                            <h2>Practical insight</h2>
                            <p>Take the deliverable you are most often asked to produce off-cycle &#8212; the one somebody requests at short notice, that always takes longer than it should.</p>
                            <p>List its fields and check each against the input sheet. The reason it takes so long is almost always that one or two fields are not collected, and you have been assembling them by hand every time.</p>
                            <p>Then decide whether to add them. Not into the middle of the sheet: at the end, with a name, a unit, and somebody who owns filling it in. It will be empty for the first month, which feels like failure and is not. From the second month you stop doing that assembly by hand, permanently.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>A field that was never collected cannot be recovered by redesigning the report.</li>
                            <li>Work backwards: name the output, list its fields, and for each ask what, who, what unit, and which day it closes.</li>
                            <li>The useful result is the two or three fields the input sheet does not hold.</li>
                            <li>You will inherit a data model far more often than you will design one.</li>
                            <li>A table in use is an interface. Reports, dashboards and other people&#39;s calculations read it, and none of them are visible from inside the file.</li>
                            <li>Change tables in one direction: new fields at the end, existing columns keep their position.</li>
                            <li>Reports change often and cheaply. The source underneath should be close to stationary.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>From here the track goes department by department, in the order the data reaches you. The first is the one whose output looks least like data.</p>
                            <p>Next week: engineering &#8212; deliverable lists, issued-for-construction dates, and the drawing that arrives approved with comments.</p>''',
)

W13 = dict(
    week=13,
    file="reporting-week-13.html",
    h1="Two revisions on the same site.",
    title="Document control for planners — revision status as a reporting input",
    desc=("Publishing a new revision is the easy half. Why document control is finished only when "
          "the old drawing has left site, and what revision status has to do with a progress claim."),
    og="Two revisions on the same site",
    share="Document control is not issuing the new revision. It is getting the old one off site, and the second half is the hard one.",
    crumb="Revision status, distribution, and what is actually current",
    body='''<h2 style="margin-top:0;">Two revisions on the same site</h2>
                            <p>A walk round the works, and a question that sounds administrative: which revision are you working to?</p>
                            <p>The printouts come out, and they are not the same. Engineering issued a new revision some days ago. The technical office has it. The crew on the wall does not, because the copy in their hand was printed before it existed. Sometimes the office has it and the subcontractor has not been sent it. Sometimes everybody has it except the one gang that needed it.</p>
                            <p>Nobody in that chain did anything wrong. The revision was issued, and the issuing was recorded. What was never confirmed is the thing that actually matters, which is whether the previous version stopped being used.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>On most projects this gets found the same way &#8212; during a quality check, or on a site walk, when somebody happens to ask. It is not usually found by the system, because the system recorded the sending rather than the withdrawal.</p>

                            <h2>What happens when it is found</h2>
                            <p>The outcome varies more than people expect, and it is worth being honest about that rather than reaching for the worst case.</p>
                            <p>Often the work is early enough that it is simply stopped and restarted against the current drawing. Sometimes the change does not affect what was being built at all, and the work continues untouched. Occasionally it is expensive.</p>
                            <p>But the cost of any single instance is not really the point. The point is that on a large job you can never be entirely confident that everybody is looking at the same revision, and that uncertainty is permanent unless something is done about the withdrawal rather than the issue.</p>

                            <h2>The half of document control nobody measures</h2>
                            <p>Issuing a revision is straightforward. There is a transmittal, a date, a distribution list, and a record that it went out. Every project can show you that record.</p>
                            <p>Removing the previous revision from the places it is being used is the other half, and it is the half that is almost never tracked. The old drawing is on a wall in a site cabin, in a folder in a subcontractor&#39;s office, in somebody&#39;s truck. Sending the new one does not remove any of those.</p>
                            <p>So the useful definition is not the administrative one. Document control has succeeded when there is one valid revision in use and no other, and it has not succeeded merely because a transmittal was sent. If two revisions are live on the same site, the process is unfinished regardless of what the register says.</p>

                            <h2>The copy that left the system</h2>
                            <p>There is a structural reason this is hard, and it has nothing to do with anybody being careless.</p>
                            <p>A register controls a file. Work is done from paper. The moment a drawing is printed it leaves the system entirely: it goes into a folder, onto a wall, into a vehicle, and no revision control reaches it. Issuing a new file supersedes the old file. It does nothing at all to the sheet already pinned up in a cabin.</p>
                            <p>The subcontractor boundary makes it worse. You issue to their office and record that you did. What happens inside that office &#8212; who prints it, who gets a copy, whether the previous one comes down &#8212; is not visible to you, and the transmittal register will show the distribution as complete either way.</p>
                            <p>Which is why the check has to be physical. Not more fields in the register. Somebody walking over and looking at what is in a hand.</p>

                            <h2>Current on which date</h2>
                            <p>There is a timing question underneath this that matters for the report specifically.</p>
                            <p>A revision issued on the thirtieth does not make the work done on the twentieth correct or incorrect. What was built was built to whatever was current at the time, and judging it against a drawing that did not yet exist is unfair and useless.</p>
                            <p>So the useful question is never simply which revision is current. It is which revision was current when the work was done, and whether the change since then affects it. Answering that needs a dated record, which is the second reason the register has to hold more than one event.</p>

                            <h2>Why this is a reporting problem</h2>
                            <p>It would be easy to file this under quality and move on. It belongs here for a specific reason.</p>
                            <p>Progress claimed against a superseded drawing is not progress. The work may exist physically, and it may still have to be modified, so the percentage reported that month was describing something that had not been finished in the sense the report implied.</p>
                            <p>That makes revision status an input to your figures rather than a document management detail. It sits alongside the corroborating records from <a href="reporting-week-8.html">Week 8</a>: before accepting a quantity, it is fair to ask which drawing it was built to and whether that drawing is current.</p>
                            <p>It is also one of the six readiness tests from <a href="reporting-week-9.html">Week 9</a>. An activity is not ready if the current revision has not reached the people who will build from it, and reached means in their hands rather than in the register.</p>

                            <h2>What the register has to record</h2>
                            <p>Most transmittal registers record one event: sent. Two more are needed before the picture is complete.</p>
                            <p>Acknowledged, meaning the recipient confirmed they have it &#8212; not that the email left. And withdrawn, meaning the previous revision has been taken out of the places it was in use, with somebody&#39;s name against it.</p>
                            <p>Three columns instead of one. The first is administration. The other two are the process.</p>

                            <h2>Practical insight</h2>
                            <p>Pick three drawings that were revised in the last month and are being worked to right now. For each one, do not check the register. Go and look, or ask somebody who will go and look.</p>
                            <p>Ask two questions of whoever is holding the drawing. Which revision is this, and when did you get it. Then compare that against what the register says was issued.</p>
                            <p>If all three match, your distribution works and you have learned something worth knowing. If one does not, you have found the gap on the cheapest possible sample, and you have found it before somebody builds a fortnight of work to it.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Revision control usually runs on people telling each other, not on a system, however good the register looks.</li>
                            <li>The new revision reaching the office is not the same as it reaching the gang on the wall.</li>
                            <li>It is normally found on a site walk or a quality check, because the system recorded the sending rather than the withdrawal.</li>
                            <li>Outcomes vary: often the work is early enough to stop, sometimes the change is irrelevant, occasionally it is expensive.</li>
                            <li>Document control has succeeded when one revision is in use and no other. A transmittal is not the finish line.</li>
                            <li>Progress claimed against a superseded drawing is not progress, which makes revision status a reporting input.</li>
                            <li>A register needs three events, not one: issued, acknowledged, and the old copy withdrawn.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Every source so far has been inside the project. The next one keeps its own books, closes on its own date, and produces records that are correct for a purpose that is not yours.</p>
                            <p>Next week: commercial &#8212; commitments, accruals and invoices, and the delivery note that was never built to allocate cost.</p>''',
)

W25 = dict(
    week=25,
    file="reporting-week-25.html",
    h1="Both numbers were right.",
    title="Reconciling progress and valuation — when two project reports disagree",
    desc=("Project controls builds a progress figure. Commercial builds a valuation. They meet at "
          "month end and disagree, and both are correct. How the reconciliation works and who "
          "decides."),
    og="Both numbers were right",
    share="Progress said one thing, valuation said another, and neither was wrong. That is the month end nobody plans for.",
    crumb="Progress against valuation, reconciled before either goes out",
    body='''<h2 style="margin-top:0;">Both numbers were right</h2>
                            <p>Month end. Project controls has a progress figure, built from measured quantities against the rules of credit agreed at the start. Commercial has a valuation, built from what has been measured for payment under the contract.</p>
                            <p>They do not match. And the uncomfortable part is that neither of them is wrong.</p>
                            <p>They were produced by two legitimate methods answering two different questions. Progress asks how much of the work exists. Valuation asks how much of it the contract says is payable this month. Those are not the same question and there is no reason for them to give the same answer.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>What makes this difficult is not the gap. It is that both figures are about to leave the office, in different documents, to overlapping audiences, and somebody downstream is going to notice.</p>

                            <h2>Why they diverge</h2>
                            <p>The reasons are ordinary and they repeat.</p>
                            <p>Measurement rules differ. What counts as complete for progress is not always what counts as measurable for payment, and the second is usually stricter, because money depends on it.</p>
                            <p>Timing differs. The two close on different dates, which <a href="reporting-week-14.html">Week 14</a> covers from the commercial side. Work done near the boundary lands on one side in one document and the other side in the other.</p>
                            <p>Material at site is treated differently. Delivered material may carry value under the contract while representing no installed progress at all.</p>
                            <p>And the breakdown differs. The commercial structure maps to the contract; the physical one maps to where work happens. A figure that aggregates cleanly in one aggregates awkwardly in the other.</p>

                            <h2>Checking before arguing</h2>
                            <p>The mistake is to take the disagreement straight into a meeting. Almost every time, part of it dissolves against records that already exist.</p>
                            <p>The routine is the one from <a href="reporting-week-8.html">Week 8</a>, applied at month end rather than weekly. Site quantities against delivery notes and store issues. Against the quantity surveyor&#39;s measurement. Against attendance, which caps what could plausibly have been done. Against store movements for the material actually consumed.</p>
                            <p>Usually the gap splits into three parts. Some of it is a timing difference and will resolve itself next month. Some of it is a genuine measurement disagreement that needs a decision. And some of it is an error on one side, which is the part worth finding, because it is the only part that is still wrong after the meeting.</p>

                            <h2>The material nobody agrees about</h2>
                            <p>Of the four causes, material at site is the one that recurs most and argues hardest, so it is worth taking on its own.</p>
                            <p>Steel arrives and is stored. Under many contracts it carries value from the moment it is on site and accepted, so the valuation includes it. No progress has occurred: nothing is installed, nothing is measurable against a rule of credit, and the schedule has not moved.</p>
                            <p>Both positions are correct and they are not reconcilable by argument, because they are answering different questions. The only thing that resolves it is a decision taken once, early, about how delivered material is treated in each document &#8212; and then applied consistently rather than revisited every month when the gap reappears.</p>

                            <h2>Who decides</h2>
                            <p>Not the planner, and this matters more than it sounds.</p>
                            <p>When two records disagree, the item goes back to the person who reported it and to the department holding the contradicting record, in the same email, and it stays open until they agree. Project controls sets out what disagrees and by how much. It does not adjudicate.</p>
                            <p>There are two reasons for that. The obvious one is that the commercial position is a contractual matter and is not the planner&#39;s to settle. The less obvious one is that a figure quietly adjusted by project controls is a figure nobody else will stand behind. When it is challenged &#8212; by the client, by an auditor, by a claim two years later &#8212; the person who reported it will say it is not what they submitted, and they will be right.</p>
                            <p>The planner&#39;s authority here is not to decide the number. It is to refuse to publish two numbers that have not been reconciled.</p>

                            <h2>Before, not after</h2>
                            <p>All of this has to happen before either document goes out, which is an organisational constraint rather than an analytical one.</p>
                            <p>It means the two closing dates have to leave enough space between them for a short meeting, and that the meeting is about boundary items and differences rather than about the numbers in general. Twenty minutes, a list, and a decision on each line.</p>
                            <p>Do it afterwards and you are no longer reconciling. You are explaining why two published documents disagree, to people who now have a reason to distrust both.</p>

                            <h2>When there is no time to reconcile</h2>
                            <p>Sometimes the meeting does not happen. The dates were too close, somebody was away, the client moved the deadline.</p>
                            <p>The wrong response is to publish and hope nobody compares them. Somebody will, and usually it is the client, who receives both documents and has every reason to read them against each other. A difference discovered by the reader costs far more than the same difference declared by the writer, because the first raises a question about the numbers and the second only about the calendar.</p>
                            <p>So publish with the difference stated. One line: the two figures differ by this much, the cause is being confirmed, and the resolution follows next month. It is an uncomfortable sentence to write and it protects both documents.</p>

                            <h2>Practical insight</h2>
                            <p>Take last month&#39;s progress figure and last month&#39;s valuation and write the difference as one number. Most projects have never done this, because the two live in different documents owned by different people.</p>
                            <p>Then split it into the three parts: timing, measurement disagreement, and error. You will not manage it precisely and that is fine. The proportions are what matter.</p>
                            <p>If most of it is timing, you have a calendar problem and it is fixable by agreeing dates. If most of it is measurement, you have a rules problem and it needed settling at the start. If a meaningful share is error, you have found the thing that would otherwise have surfaced in an audit.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Progress and valuation answer different questions. Disagreement is the normal state, not a fault.</li>
                            <li>They diverge for four ordinary reasons: measurement rules, closing dates, material at site, and breakdown structure.</li>
                            <li>Check against records that already exist before taking the gap into a meeting. Much of it dissolves.</li>
                            <li>Split the difference into timing, disagreement and error. Only the third one stays wrong afterwards.</li>
                            <li>The planner sets out what disagrees and by how much. The planner does not adjudicate it.</li>
                            <li>A figure quietly adjusted by project controls is a figure the reporter will not defend when it is challenged.</li>
                            <li>Reconcile before publication. Afterwards it is not reconciliation, it is explaining two published documents that disagree.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Twenty-five weeks of inputs, outputs and the checks between them, and one question left that none of it answers.</p>
                            <p>Next week: the report nobody acts on &#8212; the most common failure in the trade, and what is worth changing when it happens.</p>''',
)


W15 = dict(
    week=15,
    file="reporting-week-15.html",
    h1="They do not send data. They send time.",
    title="Approvals as a programme input — client and consultant turnaround",
    desc=("The client and the consultant produce almost no data for a planner. What they produce "
          "is delay and permission, and turnaround time belongs in the programme rather than in "
          "a correspondence log."),
    og="They do not send data. They send time",
    share="The client is not a data source. The client is a duration, and it belongs in the programme like any other.",
    crumb="Instructions, approvals, comments",
    body='''<h2 style="margin-top:0;">They do not send data. They send time</h2>
                            <p>Every other source in this track hands you a number. The site gives quantities, the store gives issues, the commercial team gives cost. What the client and the consultant hand you is different in kind.</p>
                            <p>They give instructions, which change what has to be done. They give approvals, which decide when it can be done. And they give comments, which are the most ambiguous of the three, because a drawing returned with comments is neither approved nor rejected and somebody has to decide what to do with it this afternoon.</p>
                            <p>None of that is data in the sense the rest of the track means. It is duration and permission, and it belongs in the programme rather than in a correspondence file.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Turnaround is an activity</h2>
                            <p>A submittal goes out and something comes back. The gap between those two events is real, it is measurable, and on most projects it is not planned.</p>
                            <p>The contract usually states a period. What actually happens is a distribution: some responses come back in days, some take weeks, and a few sit. Planning against the contractual figure produces a programme that assumes the fast case every time.</p>
                            <p>The fix is unglamorous. Record the actual turnaround for a few months and plan against what you observe rather than what the contract permits. If your consultant averages three weeks and the contract says two, the programme that assumes two is wrong by a week on every submittal, and there are hundreds of them.</p>

                            <h2>Approved with comments</h2>
                            <p>This is the category that causes the most trouble, because it looks like a decision and is not.</p>
                            <p>The drawing comes back marked approved with comments. Sometimes the comments are editorial and work can start. Sometimes one of them changes a dimension, and starting means building something that will have to be revisited. The status field says the same thing in both cases.</p>
                            <p>So the status alone cannot be used as a readiness test. Somebody has to read the comments and decide, and that decision needs recording, because the alternative is that two people read the same drawing differently &#8212; which is where <a href="reporting-week-13.html">Week 13</a> starts.</p>

                            <h2>The request with no record</h2>
                            <p>There is a second thing that comes from the client side and it does not arrive through any of the formal channels.</p>
                            <p>A message asks where the daily report is, or whether the workfront is ready, or for the latest progress. It arrives directly, outside the reporting chain, often outside the project&#39;s own systems entirely.</p>
                            <p>Answering it is not the problem. The problem is that the request has no record. It cannot be prioritised against the other things you were doing, it cannot be assigned to somebody else, and in a month nobody can say who asked for it or why the work was done. Multiply it by a few requests a week and a meaningful share of the reporting effort on a project exists nowhere in any plan.</p>
                            <p>What works is not refusing to answer. It is answering and then logging it &#8212; a line in the same register that holds the formal correspondence, so that the volume becomes visible even when each individual request was trivial.</p>

                            <h2>The approval that was never asked for</h2>
                            <p>There is a quieter version of the same problem, and it costs more than the slow response.</p>
                            <p>A submittal that was never sent cannot be late. The activity sits in the programme with a start date, the drawing is ready, and nobody raised the inspection request or lodged the document because it was assumed somebody else had. Nothing appears in the turnaround log, because nothing entered it.</p>
                            <p>This is why a submittal register with only two columns is misleading. It measures the responses to things that were sent, which flatters the process by leaving out everything that never started. The useful register begins earlier: what has to be submitted, by when, to leave enough turnaround before the work needs it.</p>
                            <p>Read that way the register is a forward-looking document rather than a record. It tells you what to chase this week, which is a different job from telling you what happened last week.</p>

                            <h2>Instructions that are not instructions</h2>
                            <p>The last category is the one with contractual weight, and this track is not the place for it. <a href="contract-week-6.html">Contract Week 6</a> deals with what constitutes an instruction and what follows from one.</p>
                            <p>What matters here is narrower: the reporting consequence. An instruction changes scope, and scope changes have to reach your quantities and your baseline before the next report, or the report describes a project that no longer exists. That handover is often informal, and the planner finds out about a change from a site engineer rather than from the change register.</p>

                            <h2>Practical insight</h2>
                            <p>Take the last twenty submittals and write down two dates for each: sent, and returned.</p>
                            <p>Calculate the actual turnaround. Then compare it with the figure your programme assumes. Most projects find a gap, and most projects have never looked, because the assumption came from the contract at the start and nobody revisited it.</p>
                            <p>Then look at how many came back approved with comments rather than approved. If it is a large share, your readiness test for drawings is weaker than it appears, and the difference between the two statuses is being decided informally by whoever happens to open the file.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The client and the consultant supply duration and permission, not data.</li>
                            <li>Turnaround is measurable and usually unplanned. The contractual period is a limit, not a forecast.</li>
                            <li>Plan against observed turnaround, not the figure in the contract.</li>
                            <li>Approved with comments looks like a decision and is not. Somebody has to read the comments and record what they decided.</li>
                            <li>Informal requests carry no record, cannot be prioritised, and account for real effort that appears in no plan.</li>
                            <li>Answer them, then log them, so the volume becomes visible.</li>
                            <li>An instruction has to reach quantities and baseline before the next report, or the report describes a project that has changed.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>That is every source. From here the track turns round and looks at what you send back, starting with the thing that decides how much of it was measured.</p>
                            <p>Next week: the calendar &#8212; data date, cut-off, and why three departments closing on three different days is the most expensive unexamined decision on a project.</p>''',
)

W16 = dict(
    week=16,
    file="reporting-week-16.html",
    h1="Three departments, three month-ends.",
    title="Data date and cut-off — the reporting calendar in project controls",
    desc=("Cut-off dates are usually inherited rather than designed, and they decide how much of "
          "a report was measured. Why three departments closing on three days produces figures "
          "that cannot be compared."),
    og="Three departments, three month-ends",
    share="The cut-off date decides how much of your report was measured. On most projects nobody chose it.",
    crumb="Data date, cut-off, and the reporting week",
    body='''<h2 style="margin-top:0;">Three departments, three month-ends</h2>
                            <p>Ask three people on a project when the month closed and you can get three answers.</p>
                            <p>Finance closed on one date because the financial calendar says so. Project controls closed on another, because that is when the progress data was cut. The quantity surveyor measured across a period that matches neither, because measurement for payment follows the contract.</p>
                            <p>Each is defensible on its own terms. The report that combines them describes a month that nobody actually had.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>And almost nowhere was this decided. The dates were inherited, from a previous project or a previous manager or a client requirement that has since lapsed, and they have never been examined together.</p>

                            <h2>The cut-off decides the data</h2>
                            <p>The hour and the date are not administration. They determine what proportion of the report is a measurement and what proportion is a recollection, for the reason <a href="reporting-week-17.html">Week 17</a> describes at daily level and which applies at every frequency.</p>
                            <p>Close too early and you have asked people to report work that has not finished producing its own record. Close too late and the report arrives after the meeting it was meant to inform, which is a different kind of failure and just as complete.</p>
                            <p>Between those there is usually a defensible window, and the useful question is not what the deadline is but why it is where it is. Ask on most projects and the answer is that nobody knows.</p>

                            <h2>Data date is not cut-off</h2>
                            <p>Two terms get used interchangeably and they are not the same thing.</p>
                            <p>The data date is the moment the schedule is considered current: everything before it is actual, everything after is plan. It is a property of the schedule.</p>
                            <p>The cut-off is when data collection stops for a reporting period. It is a property of the process.</p>
                            <p>They should coincide and often do not, which produces the quiet error where a schedule updated to one date is reported against quantities collected to another. Nothing looks wrong. The progress figure is simply describing a slightly different period from the one on the cover.</p>

                            <h2>Why the dates are where they are</h2>
                            <p>It is worth asking, because the answer is usually recoverable and usually surprising.</p>
                            <p>A deadline set to feed a Monday morning meeting that no longer takes place. A client representative who wanted the report before their own call, and who left the project two years ago. A finance close inherited from a corporate calendar that has nothing to do with construction.</p>
                            <p>Some of these cannot move. Finance answers upwards and measurement answers to the contract. But the ones that belong to the project can move, and moving a collection deadline by three hours sometimes does more for data quality than a year of chasing people.</p>
                            <p>The precondition is knowing why the hour is the hour. If nobody on the project can answer that, it is not a constraint. It is a habit.</p>

                            <h2>What to write down</h2>
                            <p>The remedy is a calendar, and it is a page rather than a system.</p>
                            <p>For each reporting product, four things: when collection closes, who has to have submitted by then, when it is issued, and who receives it. Then the same for the month, including the finance close and the measurement period, so that the three dates sit on one sheet where their differences are visible.</p>
                            <p>Most of the value appears when it is first written. Three people discover they had assumed different dates, and that conversation is cheaper now than in the reconciliation meeting described in <a href="reporting-week-25.html">Week 25</a>.</p>

                            <h2>The boundary items</h2>
                            <p>Wherever two dates differ there is a set of items that fall between them: work done after your cut-off but before finance closed, material delivered in the gap, a measurement completed two days late.</p>
                            <p>These do not need a system. They need a list, made each month, of what crossed the boundary and which period it was counted in. Twenty minutes, and it removes almost all of the argument that would otherwise happen when the two documents disagree.</p>
                            <p>The alternative is that each side treats boundary items according to its own logic, both correctly, and the difference is discovered by somebody downstream who has no way of knowing it was a calendar effect rather than an error.</p>

                            <h2>Practical insight</h2>
                            <p>Write down three dates for last month: when your progress data closed, when finance closed, and the end of the measurement period.</p>
                            <p>If all three are the same, you are in a small minority and it is worth knowing. If they differ, work out by how many days, and then ask one question for each gap: what was going on during those days that would land on one side or the other?</p>
                            <p>You do not need to change the dates. Changing them is often impossible, because finance answers to a corporate calendar and measurement to the contract. What matters is knowing where the seams are, because every unexplained difference between two reports lives in one of them.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Three departments can close a month on three different dates, each for a good reason.</li>
                            <li>The dates are almost always inherited rather than chosen, and rarely examined together.</li>
                            <li>Cut-off decides how much of a report was measured and how much was remembered.</li>
                            <li>Data date is a property of the schedule; cut-off is a property of the process. They should coincide.</li>
                            <li>A reporting calendar is one page: collection closes, who submits, when issued, who receives.</li>
                            <li>Most of its value appears while writing it, when people discover they assumed different dates.</li>
                            <li>List the items that fall between two dates each month. It removes most of the argument later.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>With the calendar fixed, the outputs start. The first is the shortest document on the project and the one with the longest afterlife.</p>
                            <p>Next week: the daily report &#8212; what the deadline does to it, and how one day ends up with several versions of itself.</p>''',
)

W23 = dict(
    week=23,
    file="reporting-week-23.html",
    h1="The call solved it. The email proved it.",
    title="Minutes, actions and closure — making a project decision stick",
    desc=("Verbal agreements decay within days. How to run the meeting-to-closure chain so that "
          "a decision survives the week it was taken, including when the mistake was yours."),
    og="The call solved it. The email proved it",
    share="Two days later, two people remember the same call differently. Nobody misremembers a list they both read.",
    crumb="Meeting, minutes, action, follow-up, closed",
    body='''<h2 style="margin-top:0;">The call solved it. The email proved it</h2>
                            <p>A discrepancy turns up. Two records disagree, or a quantity looks wrong, or something that should have arrived has not.</p>
                            <p>The instinct is to pick up the phone, and the instinct is right &#8212; a call resolves in four minutes what an email thread takes three days to circle. But a habit is worth building around it, and it runs in the other order.</p>
                            <p>Write it down first. Which data disagrees, which departments are affected, which records do not match, as a short list. Copy the people who hold each record. Then ring the person and say you have sent something and ask whether they have a moment to go through it.</p>
                            <p>The call is for solving. The email is the record of how it was solved. And the same applies when the mistake turns out to be yours, which is the part that makes the habit credible rather than defensive.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Why verbal agreements decay</h2>
                            <p>Two days after a conversation, two people can recall it differently and both be sincere. A week later neither is sure. A month later, when it matters, there is nothing to consult.</p>
                            <p>This is not about distrust. It is that a conversation has no fixed form: each participant remembers the part that concerned them, in their own words, and the parts that did not concern them fade. Written text does not do that. Everybody reads the same sentence.</p>
                            <p>Which has a second benefit that is easy to miss. A written record de-personalises the disagreement. Two people arguing on a call are two people. Two people looking at the same list are two people looking at a list.</p>

                            <h2>The chain</h2>
                            <p>Meeting, minutes, action, follow-up, closed. Five steps, and projects routinely execute the first three and abandon the last two.</p>
                            <p>Minutes that record discussion are close to worthless. What earns the time is the action: a thing to be done, a person who is doing it, and a date. Anything in the minutes that is not one of those is background, and can be a sentence.</p>
                            <p>Follow-up means the item appears again next week whether or not anybody raises it. Closure means somebody says it is done, and what proves it.</p>
                            <p>The step that gets skipped is the fourth, and skipping it produces the pattern from <a href="reporting-week-9.html">Week 9</a>: an item resolved verbally in one meeting, raised again in the next, with nobody able to say whether it was ever closed or closed and reopened.</p>

                            <h2>The same list under pressure</h2>
                            <p>When a project is behind, a recovery action list appears. It is usually treated as a different kind of document &#8212; more urgent, more senior, more visible.</p>
                            <p>It is the same document. Same columns, same discipline, same failure mode if follow-up is dropped. The only difference is that the consequences of a lapsed action are now measured in weeks of programme rather than in inconvenience.</p>
                            <p>Which is an argument for running the ordinary version properly, because a project that cannot close routine actions in normal conditions will not suddenly be able to close urgent ones under pressure.</p>

                            <h2>Copy the record holder, not the hierarchy</h2>
                            <p>Who goes on the email decides whether it works, and the instinct to copy upwards is usually wrong.</p>
                            <p>The people who need to be on it are the ones holding the records that disagree: the engineer who reported the quantity, the department whose figure contradicts it. They can resolve it between them, and they are the ones who will have to stand behind whatever is agreed.</p>
                            <p>Copying a manager who holds neither record does something different. It converts a technical reconciliation into an escalation, which slows it down and makes the two people defensive rather than useful. Escalation is a tool, and it works because it is rare.</p>
                            <p>So the default distribution is narrow and complete: everybody who owns a piece of the disagreement, and nobody who does not.</p>

                            <h2>What an action needs</h2>
                            <p>Three fields carry almost all the weight, and a fourth is worth the space.</p>
                            <p>A person, not a department. Departments do not do things; people do, and an action assigned to engineering belongs to nobody.</p>
                            <p>A date, which is what makes follow-up possible at all.</p>
                            <p>A statement of what done looks like, because half of all disputed closures are two people with different pictures of completion.</p>
                            <p>And the consequence of not doing it, which is optional and changes behaviour more than the other three combined. An action with a stated cost is harder to leave alone than one without.</p>

                            <h2>Practical insight</h2>
                            <p>Take the last four sets of minutes from your weekly meeting and find every action in them. Then check each one: is there a named person, a date, and any record of closure?</p>
                            <p>Count how many are still open, how many are closed, and how many you cannot tell. That third number is the one that matters, because an action nobody can categorise was never really an action.</p>
                            <p>Then take the oldest open one and close it this week, properly, with a name against the closure. It is a small thing and it demonstrates the mechanism better than any explanation of it.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Write it down before you call. The call is for solving, the email is the record of how it was solved.</li>
                            <li>Apply the same rule when the mistake is yours. That is what makes it a habit rather than a defence.</li>
                            <li>Two days after a conversation, two people can recall it differently and both be sincere.</li>
                            <li>A written record de-personalises a disagreement: everybody reads the same sentence.</li>
                            <li>Minutes that record discussion are worth little. Actions with owners and dates are the output.</li>
                            <li>Follow-up is the step that gets skipped, and skipping it is why items reappear in every meeting.</li>
                            <li>A recovery action list is the same document under pressure, with the same failure mode.</li>
                            <li>An action needs a person, a date, and a picture of what done looks like. A stated consequence changes behaviour most.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Actions and decisions are two of the registers a project runs. There are half a dozen more, and most of them are taught as separate lists.</p>
                            <p>Next week: the register system &#8212; which record feeds which, and which of them anybody actually reads.</p>''',
)

W24 = dict(
    week=24,
    file="reporting-week-24.html",
    h1="Nothing closes by itself.",
    title="The register system — how project registers feed each other",
    desc=("Assumption, risk, change. Interface, constraint, delay. NCR and rework. Eight registers "
          "with a topology between them, and two that close all the rest."),
    og="Nothing closes by itself",
    share="Eight registers, and only two of them can close anything. Everything else just accumulates.",
    crumb="Which record feeds which, and which are read",
    body='''<h2 style="margin-top:0;">Nothing closes by itself</h2>
                            <p>A large project runs eight or so registers. Assumptions. Risks. Changes. Interfaces. Constraints. Non-conformances. Decisions. Actions.</p>
                            <p>They are usually taught as separate lists, each with its own owner and format, and that is how they end up being kept &#8212; separately, by different people, with no relationship between them.</p>
                            <p>They are not separate. They are stages of the same thing, and the value is in the arrows rather than the lists.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>The two chains</h2>
                            <p>Two paths run through those eight, and almost everything that goes wrong on a project travels one of them.</p>
                            <p>The first is about things you believed. An <strong>assumption</strong> that stops holding becomes a <strong>risk</strong>. A risk that occurs becomes a <strong>change</strong>, or a delay event, or both. Most change registers are full of items that began life as an assumption nobody revisited.</p>
                            <p>The second is about things you have to coordinate. An <strong>interface</strong> that is not resolved becomes a <strong>constraint</strong> on somebody&#39;s work. A constraint that is not closed becomes a delay, which is where <a href="reporting-week-9.html">Week 9</a> ends up.</p>
                            <p>Non-conformances sit slightly apart and feed both: an <strong>NCR</strong> produces rework, which reverses reported progress and often produces a change as well.</p>
                            <p>Read that way, the registers stop being a filing convention and start being a description of how a problem matures. The earlier in a chain you catch something, the cheaper it is, which is the entire argument for keeping the registers nobody thinks are urgent.</p>

                            <h2>The two that close things</h2>
                            <p>Six of the eight only accumulate. They record that something exists, and they can record that it stopped existing, but they cannot cause it.</p>
                            <p>Two are different. The <strong>decision</strong> register records that somebody with the authority chose, and the <strong>action</strong> register records that somebody with the responsibility is doing. Those are the only two mechanisms a project has for making an entry in any of the others go away.</p>
                            <p>Which explains a pattern most planners will recognise: a risk register that grows every month and never shrinks. It is not that the risks are unmanageable. It is that nothing connects them to a decision or an action, so the register can only add.</p>

                            <h2>State and inventory</h2>
                            <p>One distinction keeps this manageable, because a project has far more than eight lists.</p>
                            <p>Submittal registers, document registers, material status reports, procurement logs &#8212; these are inventories. They record what exists and where it is. They are useful and they do not need a topology, because nothing flows between them.</p>
                            <p>The eight above track state: something is open, unresolved, or waiting on somebody. State needs the arrows. Inventory does not.</p>
                            <p>Confusing the two produces the catalogue that this week is designed to avoid: fifteen registers presented as equally important, when only a handful of them describe anything that can get worse.</p>

                            <h2>The entry that belongs in two registers</h2>
                            <p>A common objection to the chains is that items refuse to stay in one list, and the objection is correct.</p>
                            <p>A late vendor document is an interface question, a constraint on the crew waiting for it, and a risk to the completion date. Recording it three times produces three entries that drift apart, each updated by somebody who cannot see the others. Recording it once means two of the three teams cannot find it.</p>
                            <p>The workable answer is to record it where it is being managed and reference it elsewhere. The constraint log holds it while somebody is chasing the document, because that is where the daily work happens. The risk register points at it rather than restating it.</p>
                            <p>Which means the registers need to be able to refer to each other at all &#8212; a single identifier that travels. That is a small design decision, taken at the start or not at all, and it is the difference between a set of registers and a system of them.</p>

                            <h2>Which ones get read</h2>
                            <p>Honestly, few of them. The action list gets read because it names people. The constraint log gets read on the days somebody cannot start. The risk register is read when it is reviewed and rarely between.</p>
                            <p>That is not an argument for keeping fewer. It is an argument for knowing which is which, because a register that is only read after the fact has a different job: it is evidence rather than management, and it should be kept to a standard that survives being read by somebody hostile a year later.</p>
                            <p>The ones that are read weekly should be short. The ones that are read afterwards should be complete. Trying to make every register do both is why most of them do neither.</p>

                            <h2>Practical insight</h2>
                            <p>Open your change register and take the last ten entries. For each one, work backwards: was there an assumption behind it, and was that assumption ever written down anywhere?</p>
                            <p>You will usually find that several of them were foreseeable &#8212; not certain, but visible as an assumption somebody was carrying. Those are the ones the chain would have caught.</p>
                            <p>Then do the reverse. Take your risk register and find the entries that have been open longest. For each, ask what decision would close it and who would have to take it. Any entry where you cannot name that person is not being managed, whatever the review meeting concluded.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Eight registers, and the value is in the relationships rather than the lists.</li>
                            <li>Assumption, then risk, then change: most change registers are full of assumptions nobody revisited.</li>
                            <li>Interface, then constraint, then delay: the second chain, and the one that stops work.</li>
                            <li>NCRs feed both, through rework that reverses progress and often produces a change.</li>
                            <li>Only decisions and actions can close anything. The other six accumulate.</li>
                            <li>A risk register that only grows is one with nothing connecting it to a decision.</li>
                            <li>Separate state registers from inventories. Only state needs a topology.</li>
                            <li>Weekly registers should be short. Registers read afterwards should be complete. Few can be both.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Everything so far assumes the records can be made to agree. Once a month they will not, and both sides will be right.</p>
                            <p>Next week: progress against valuation &#8212; two legitimate methods, one number, and who gets to decide.</p>''',
)


W6 = dict(
    week=6, file="reporting-week-6.html",
    h1="Four quantities, one bill item.",
    title="Material at site — delivered, stored, issued, installed",
    desc=("The same bill item has four different quantities at any moment, and only one of them is "
          "progress. Why material inflates a curve and what to reconcile it against."),
    og="Four quantities, one bill item",
    share="Delivered is not issued. Issued is not installed. Only one of the four is progress, and it is the smallest.",
    crumb="Delivered, stored, issued, installed",
    body='''<h2 style="margin-top:0;">Four quantities, one bill item</h2>
                            <p>Cable is on the schedule as a single line with a single quantity. On any given Tuesday that line has four different numbers attached to it, and they are all correct.</p>
                            <p>Some has been delivered to site. Some of that is in the store. Some has been issued to a crew. And some is actually installed. Each figure is larger than the next, and the gaps between them can be months.</p>
                            <p>The problem this creates is specific: if nobody says which of the four a report is using, different documents use different ones, and the project has a progress figure that moves when nothing has been built.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What the four quantities cost you</h2>
                            <p>Two failures, and both are common enough to expect.</p>
                            <p>The first is inflation. Where progress is measured by cost, delivered material carries value and the curve rises on the day the lorry arrives. Nothing has been built. The curve is not wrong &#8212; it is answering a question about value rather than about work &#8212; but everybody reading it believes it is about work.</p>
                            <p>The second is the reverse and it surfaces at the end. Material issued to a crew and not installed sits somewhere, and it is invisible. It has left the store, so the store thinks it is used. It is not on the wall, so the survey does not see it. The gap only appears at reconciliation, when the project discovers it has paid for more than exists.</p>

                            <h2>The reconciliation</h2>
                            <p>Delivered against issued against installed, once a month, per significant material. Not per bill item &#8212; that is unmanageable and nobody does it. The handful of materials that carry real value: cable, pipe, steel, formwork, whatever your job turns on.</p>
                            <p>What you are looking for is not exactness. It is the direction and size of the gap. Installed well below issued means material is sitting in the field, which is either wastage or a stock that nobody has counted. Issued well below delivered is normal early and unusual late.</p>
                            <p>This is also the corroboration route from <a href="reporting-week-8.html">Week 8</a>, used the other way round. There, store issues checked a claimed quantity. Here, the claimed quantity checks whether material has gone missing.</p>

                            <h2>What the gap is telling you</h2>
                            <p>A persistent difference between issued and installed has three explanations and they need different responses.</p>
                            <p>It might be wastage, in which case the figure is a cost problem and belongs with the commercial team rather than in a progress discussion. It might be uncounted stock in the field &#8212; material staged at a workface, still usable, simply not recorded anywhere. Or it might be a measurement lag, where the installation happened and the survey has not caught up.</p>
                            <p>Distinguishing them takes one walk. The point of tracking the gap is not the number but the question it forces somebody to answer, and on most projects nobody has been asked.</p>

                            <h2>Working with a register that already exists</h2>
                            <p>If you are setting this up, the decision is one line in the procedure: which of the four quantities is progress, stated once, and applied in every document. Everything after that is bookkeeping.</p>
                            <p>If you inherited it &#8212; which is the usual case &#8212; the decision was made implicitly and probably differently in different reports. The work is to find out what each document is actually using. Ask the cost report what its material figure represents, then ask the progress report. If the answers differ, you have found why the two never agree, and you have found it without changing anything.</p>

                            <h2>Practical insight</h2>
                            <p>Pick the single material your project spends the most on. Get four numbers for last month: delivered, in store, issued, installed.</p>
                            <p>Most projects can produce the first three quickly and struggle with the fourth, which is itself the finding. If installed cannot be stated, then the progress being reported for that material is derived from one of the other three, and everybody reading it thinks otherwise.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Delivered, in store, issued and installed are four different quantities for the same line, all correct.</li>
                            <li>Only installed is progress. The other three are logistics and value.</li>
                            <li>Cost-based measurement lifts the curve when material arrives, before anything is built.</li>
                            <li>Material issued and not installed is invisible: gone from the store, not on the wall.</li>
                            <li>Reconcile monthly, for the handful of materials that matter, looking for direction rather than precision.</li>
                            <li>Setting it up is one line in a procedure. Inheriting it means finding out what each document already assumes.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Material is not the only thing with several correct answers. The wall itself has three.</p>
                            <p>Next week: quantities from site &#8212; the bill, the drawing and the survey, and which of them belongs in a progress report.</p>''',
)

W7 = dict(
    week=7, file="reporting-week-7.html",
    h1="Three quantities for the same wall.",
    title="Quantity sources in project reporting — bill, drawing and survey",
    desc=("The bill, the drawing and the survey give three different quantities for the same work, "
          "and each is right for a different purpose. Which one belongs in a progress report."),
    og="Three quantities for the same wall",
    share="The bill, the drawing and the survey disagree about the same wall. All three are correct. Only one belongs in your report.",
    crumb="Bill, drawing, survey",
    body='''<h2 style="margin-top:0;">Three quantities for the same wall</h2>
                            <p>Ask three people how much of a wall exists and you get three answers.</p>
                            <p>The bill of quantities says one thing, priced at tender from a design that has since moved. The drawing says another, because it is the current revision and the design changed. The survey says a third, because that is what is physically there, including what was built slightly differently.</p>
                            <p>None of them is wrong. They are answers to three different questions: what was priced, what should exist, and what does exist.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Where the three quietly diverge</h2>
                            <p>The failure is not that the three differ. It is that different documents silently pick different ones.</p>
                            <p>Progress is usually reported against the bill, because that is what the baseline was built from. The site reports against the drawing, because that is what they are building. The quantity surveyor measures what exists, because payment depends on it. Three documents, three denominators, and a percentage that cannot be compared across them.</p>
                            <p>It gets worse with variations. A change increases the drawing quantity without touching the bill. Progress against the bill now rises when nothing has happened &#8212; the denominator stayed still while the numerator grew &#8212; or falls for the same reason inverted. This is the mechanism behind a curve that moves for no visible reason, and it is worth recognising because it looks exactly like a data error.</p>

                            <h2>Choosing the denominator</h2>
                            <p>The rule that works is simple and rarely written down: report progress against the current approved quantity, and re-baseline the denominator when it changes, not silently.</p>
                            <p>Which means every variation has a second consequence nobody enjoys. The scope changed, so the total changed, so last month&#39;s percentage was against a different total. Either you restate it or you note it. Doing neither produces a series that looks continuous and is not.</p>
                            <p><a href="cost-week-4.html">Cost &amp; Cash Week 4</a> covers how the bill relates to the schedule. What this week adds is that the relationship does not hold still, and the report has to say when it moved.</p>

                            <h2>Who owns the denominator</h2>
                            <p>There is an ownership question underneath this and it is usually unanswered, which is why the three sources drift.</p>
                            <p>The bill belongs to the commercial team. The drawing belongs to engineering. The measurement belongs to the quantity surveyor. The denominator used in the progress report belongs to nobody in particular, and so it is whatever the spreadsheet was built with, by somebody who has since left.</p>
                            <p>Naming an owner for it does more than it sounds. It means somebody is responsible for updating the total when scope changes, and for saying out loud that last month&#39;s percentage was against a different number. Without that, the update happens silently or not at all.</p>

                            <h2>If the orders are already placed</h2>
                            <p>If the project has not started, this is one decision recorded in the procedure. Progress is measured against a stated source, variations update it, and the update is visible in the report.</p>
                            <p>Inherited: take three documents from last month &#8212; the progress report, the payment application and the site&#39;s own tracker &#8212; and find one activity in all three. If the totals differ, you have found the seam. It is usually not worth changing the system for it. It is always worth knowing which document uses which, because that is the difference you will be asked to explain.</p>

                            <h2>Practical insight</h2>
                            <p>Take one activity that has been through a variation. Write down its quantity as the bill has it, as the current drawing has it, and as measured.</p>
                            <p>Then find the percentage your last report gave for it and work out which of the three was the denominator. On most projects it takes ten minutes and the answer surprises somebody.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Bill, drawing and survey answer three questions: what was priced, what should exist, what does exist.</li>
                            <li>The failure is not that they differ. It is that different documents pick different ones without saying so.</li>
                            <li>A variation moves the drawing quantity without moving the bill, and the percentage shifts with nothing built.</li>
                            <li>Report against a stated source and update it visibly when scope changes.</li>
                            <li>A restated denominator makes a series discontinuous. Say so rather than smoothing it.</li>
                            <li>Inherited systems rarely need changing here. They need somebody who knows which document uses which.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Quantities describe what was built. The other half of every productivity figure is what it took, and that number has a different problem.</p>
                            <p>Next week: hours and plant &#8212; why the total is right and the allocation is not.</p>''',
)

W10 = dict(
    week=10, file="reporting-week-10.html",
    h1="The total is right. The allocation is not.",
    title="Timesheet allocation and plant utilisation for planners",
    desc=("Attendance totals reconcile perfectly while every productivity figure built on them is "
          "wrong, because allocation is what breaks. What to check and what it costs to fix."),
    og="The total is right. The allocation is not",
    share="Headcount reconciles to the gate. Hours per activity do not, and that is the number productivity is built on.",
    crumb="Allocation, availability, utilisation",
    body='''<h2 style="margin-top:0;">The total is right. The allocation is not</h2>
                            <p>Attendance is one of the most reliable records on a project. People come through a gate, somebody counts them, and the monthly total reconciles.</p>
                            <p>Which is precisely why the problem underneath it goes unnoticed for so long.</p>
                            <p>Productivity is not built on the total. It is built on hours against an activity, and that allocation is made by a supervisor filling in a sheet at the end of a shift, from memory, for a gang that moved. A man who spent half the morning helping elsewhere has eight hours against one activity and none against the other. The total is correct. Both productivity figures are not.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What bad allocation actually breaks</h2>
                            <p>Two things, and the second is the expensive one.</p>
                            <p>Productivity per activity becomes noise. It moves week to week for reasons that have nothing to do with the work, and after a while nobody trusts it, which is the correct response to a number that behaves randomly.</p>
                            <p>Then it becomes evidence. Productivity figures end up in claims, in forecasts, in the argument about whether a disruption occurred. A figure that was never reliable at activity level is now carrying weight it cannot hold, and the other side only has to ask how the hours were allocated.</p>

                            <h2>Plant has the same shape</h2>
                            <p>Equipment records show availability &#8212; the machine was on site and working &#8212; far more reliably than they show what it was working on.</p>
                            <p>Utilisation is the useful figure and the harder one: hours running against hours available, and idle time separated from breakdown. A crane that was available all month and used for a fifth of it is a different problem from one that broke down, and both appear the same in a record that only shows presence.</p>

                            <h2>What can actually be improved</h2>
                            <p>Not much, and being honest about that is more useful than pretending otherwise.</p>
                            <p>Allocation will always be approximate, because the person recording it is running a crew rather than keeping records. What can change is the number of choices they have. A sheet with forty activities produces bad allocation. A sheet with the six that the gang could plausibly have worked on produces better allocation for no extra effort.</p>
                            <p>The other thing that helps is aggregating upward before drawing conclusions. Allocation error mostly cancels within an area and mostly does not cancel across a project, so productivity by area is usually usable while productivity by activity is usually not. Reporting the first and resisting the second is a defensible position.</p>

                            <h2>When the sheet cannot be changed</h2>
                            <p>Often the timesheet is not yours. It belongs to HR, or to a payroll system, or to a subcontractor who has used the same format for a decade.</p>
                            <p>In that case the useful move is not to fight for a new sheet. It is to collect the allocation separately, at a coarser level, from the supervisor who already knows it &#8212; a weekly split of a gang across two or three areas is enough to make productivity by area usable, and it takes a minute rather than a form.</p>
                            <p>What it costs is that two records now exist for the same hours, which means somebody has to reconcile the totals monthly. That is a real cost and it is smaller than the alternative, which is a productivity series nobody quotes.</p>

                            <h2>Deciding it, or finding out what was decided</h2>
                            <p>If the sheet is yours, keep the allocation list short and tie it to the area coding, so the choices on the sheet match the work in front of the person filling it in.</p>
                            <p>Inherited: do not start by redesigning the timesheet. Start by finding out at what level the figures hold together. Compare a month of allocated hours against attendance by area &#8212; if they agree at area level and disagree below it, you have found the level at which your productivity numbers are worth quoting, and you can stop quoting the ones below it.</p>

                            <h2>Practical insight</h2>
                            <p>Take one week and one area. Add the allocated hours for every activity in it, and compare that with the attendance for the same area and week.</p>
                            <p>They will not match exactly. What matters is by how much. A few percent is normal. A large gap means hours are being allocated to activities in one area from people who were somewhere else, and every productivity figure in that area is built on it.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Attendance totals are reliable. Allocation to activities is not, and productivity is built on the second.</li>
                            <li>Bad allocation produces productivity that moves for reasons unrelated to the work.</li>
                            <li>Those figures end up in claims and forecasts, carrying weight they cannot hold.</li>
                            <li>Plant records show availability well and utilisation badly. Idle and broken down are different problems.</li>
                            <li>Shorten the list of activities on the sheet. Fewer plausible choices produces better allocation for no extra effort.</li>
                            <li>Allocation error cancels within an area and not across a project. Report at the level where the numbers hold.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Everything so far adds. The next source subtracts, and it subtracts work that has already been reported as done.</p>
                            <p>Next week: quality &#8212; non-conformances, rework, and progress that goes backwards.</p>''',
)

W11 = dict(
    week=11, file="reporting-week-11.html",
    h1="Progress that goes backwards.",
    title="NCRs and rework in progress reporting — when work is undone",
    desc=("Quality is the only input that subtracts. Why most reporting systems have no mechanism "
          "for progress that reverses, and what happens to a curve that cannot go down."),
    og="Progress that goes backwards",
    share="Every other input adds. Quality is the only one that takes work back after it was reported as done.",
    crumb="NCRs, rework and reversed progress",
    body='''<h2 style="margin-top:0;">Progress that goes backwards</h2>
                            <p>Every source in this track so far adds something. Quantities accumulate, hours accumulate, cost accumulates. The curve goes up.</p>
                            <p>Quality is the exception. A non-conformance raised against work that was reported complete last month means that work is not complete, and in some cases it means it has to come out.</p>
                            <p>Which raises a question most reporting systems cannot answer: how does a percentage go down?</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What happens when a curve cannot fall</h2>
                            <p>In practice, it does not go down. That is the failure.</p>
                            <p>The progress figure for that activity stays where it was. The rework happens, consuming hours and material, and those are recorded against something &#8212; often the same activity, occasionally a general code. The activity now shows the same percentage as before while having consumed the resources twice.</p>
                            <p>Two consequences follow. Productivity for that activity is wrong, and it is wrong in the flattering direction, because the output stayed constant while the input grew and only the input was recorded. And the completion date is wrong, because the work everybody believes is finished is not.</p>
                            <p>It surfaces at handover, which is the worst possible time and the reason the last ten percent so often takes thirty.</p>

                            <h2>The mechanism that is missing</h2>
                            <p>What is needed is not complicated: a way for reported progress to be reduced, with a reason attached, and a rule about when it applies.</p>
                            <p>The rule matters more than the mechanism. Not every non-conformance reverses progress. Some are documentation issues. Some are accepted as-is. Some require a repair that is genuinely additional work rather than a redo. Only the last category should move the percentage backwards, and somebody has to decide which category each one is in.</p>
                            <p>Without that rule the choice falls to whoever is updating the sheet, and they will reasonably leave the number alone rather than explain a reversal to a meeting.</p>

                            <h2>Rework has to go somewhere</h2>
                            <p>The second half is where the hours land.</p>
                            <p>If rework is booked against the original activity, the activity looks unproductive and nobody can tell whether the crew was slow or the work was done twice. If it is booked to a general code, the activity looks fine and the general code becomes an unexplained lump that grows all year.</p>
                            <p>Neither is satisfactory, and the workable answer is a rework flag rather than a separate account: same activity, marked. It keeps the cost where the work happened and makes the second attempt visible, which is the only way anybody learns anything from it.</p>

                            <h2>The one that never closes</h2>
                            <p>The second failure is quieter than reversed progress and it accumulates in the same place.</p>
                            <p>A non-conformance is raised, a disposition is agreed, and the physical work is done. Nobody goes back and closes the record. Six months later the register holds a hundred open items, most of which were resolved long ago, and the ones that genuinely matter are indistinguishable from them.</p>
                            <p>By handover this becomes concrete: an open NCR against a system can block a completion certificate, and somebody has to go through them one by one under time pressure to work out which are real. That exercise is always more expensive than closing them as they went.</p>
                            <p>Which is the same closure problem as <a href="reporting-week-9.html">Week 9</a> and <a href="reporting-week-23.html">Week 23</a>, in a third register. Nothing closes by itself.</p>

                            <h2>On a project that is already running</h2>
                            <p>If you are setting this up, decide the categories of non-conformance, decide which reverses progress, and add a flag rather than a code.</p>
                            <p>Inherited: the odds are that nothing reverses and rework is invisible. The first useful step is not to fix it. It is to find out how large it is &#8212; take the NCRs from the last quarter, find the ones that required physical rework, and ask what happened to the reported percentage of each. If the answer is nothing in every case, you now know the direction of the error in your curve, which is worth more than a corrected number.</p>

                            <h2>Practical insight</h2>
                            <p>Take the last ten NCRs that required work to be redone. For each, look at the progress reported for that activity before and after.</p>
                            <p>If none of them moved, your curve has never gone down, and the difference between it and the site has been accumulating quietly. Then look at where the rework hours went. If you cannot find them, they are inside the original activity, making a crew look slower than it was.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Quality is the only input that subtracts, and most systems have no mechanism for it.</li>
                            <li>When progress cannot go down, the activity keeps its percentage while consuming resources twice.</li>
                            <li>Productivity is then wrong in the flattering direction: input grew, recorded output did not.</li>
                            <li>Not every non-conformance reverses progress. The categories have to be decided before the event.</li>
                            <li>Without a rule, the person updating the sheet leaves the number alone, and they are being sensible.</li>
                            <li>Flag rework against the original activity rather than hiding it in a general code.</li>
                            <li>On an inherited system, measure the size of the error before trying to correct it.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Two more sources and the inputs are complete. The next one produces no quantities at all &#8212; it produces stoppages.</p>
                            <p>Next week: permits, holds and stand-downs, and lost time as a delay event with a record behind it.</p>''',
)

W20 = dict(
    week=20, file="reporting-week-20.html",
    h1="One number, four altitudes.",
    title="Reporting to four audiences — the same number at different levels",
    desc=("A foreman, a construction manager, a project director and a client need the same figure "
          "at four levels of detail. How to do that without telling four different stories."),
    og="One number, four altitudes",
    share="Four readers, four levels of detail, one number. The failure is not simplification. It is four versions that no longer reconcile.",
    crumb="Four audiences, four altitudes",
    body='''<h2 style="margin-top:0;">One number, four altitudes</h2>
                            <p>The same progress figure has to reach four people who need entirely different amounts of it.</p>
                            <p>A foreman needs this week, this area, these activities. A construction manager needs the discipline totals and where they are diverging. A project director needs the trend and whether the date moved. A client needs the position against the contract.</p>
                            <p><a href="week-26.html">Schedule Week 26</a> established that as the altitude concept. What this week is about is what happens when the four are produced separately.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>How four documents drift apart</h2>
                            <p>They stop reconciling, and nobody notices until two of them are in the same room.</p>
                            <p>It happens through ordinary steps. The client report is prepared first and includes an item that was still being confirmed. The internal report is produced two days later without it. The dashboard was refreshed on a third date. Each document is defensible and the three totals differ by a little.</p>
                            <p>The cost of that is not the discrepancy. It is that the first person to spot it now has a reason to check everything else, and the credibility of all four documents drops together.</p>

                            <h2>Aggregation, not authorship</h2>
                            <p>The principle that prevents it is that the four documents are not written separately. They are aggregations of the same underlying figures at different levels, and the only thing that changes between them is how much is rolled up.</p>
                            <p>Which means the detail has to sum to the summary exactly, and any exception &#8212; something excluded, something provisional &#8212; is applied at the source rather than in one document. If an item is provisional, it is provisional in all four.</p>
                            <p>The practical version of this is a single cut, at a single moment, from which all four are produced. The reports differ in level. They never differ in content.</p>

                            <h2>What each altitude actually needs</h2>
                            <p>The mistake in the other direction is to produce the same document four times with different amounts of detail deleted.</p>
                            <p>The foreman&#39;s version needs what to do, not how the project is doing. The construction manager&#39;s needs comparison between areas, which is a different cut rather than a shorter one. The director&#39;s needs trend and exception: what changed and what is at risk. The client&#39;s needs position against obligations, which is a contractual frame the other three do not use.</p>
                            <p>So four documents, four shapes, one set of numbers. The shape follows the decision each reader has to take, and only the numbers are shared.</p>

                            <h2>The fifth document</h2>
                            <p>There is nearly always one more than the four, and it is the one that causes the discrepancy.</p>
                            <p>Somebody keeps their own tracker. A discipline lead maintains a spreadsheet because the official report does not show what they need. A client representative builds their own summary from the detail. None of these is unreasonable &#8212; each exists because the official set did not answer somebody&#39;s question.</p>
                            <p>They are worth finding rather than banning. A private tracker is a specification: it tells you exactly which view is missing from the four, written by the person who needed it. Adding that view is usually easy, and it removes the source of the next unexplained difference.</p>

                            <h2>Improving the sheet, or working round it</h2>
                            <p>If you are building it, work from one cut-off and one data set. Write down which report is produced from which and at what level, so that nobody adds a fifth from a different source.</p>
                            <p>Inherited: the four almost certainly come from different places. Rather than rebuilding, check whether they agree for one month. If they do, you have less of a problem than you feared. If they do not, the size of the difference tells you whether this is a timing artefact or two separate systems that have drifted.</p>

                            <h2>Practical insight</h2>
                            <p>Take last month&#39;s client report, internal report and dashboard, and find the same headline figure in all three.</p>
                            <p>If they match, note the date each was produced from &#8212; you may be lucky rather than systematic. If they do not, work out whether the difference is timing or content, because the fix for each is entirely different and only one of them is quick.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Four readers need the same figure at four levels: activity, discipline, trend, and contractual position.</li>
                            <li>Produced separately, the four drift apart through ordinary timing differences.</li>
                            <li>The damage is not the discrepancy. It is that all four lose credibility at once.</li>
                            <li>Reports are aggregations of one data set, not four separate documents.</li>
                            <li>Exceptions are applied at the source, so a provisional item is provisional everywhere.</li>
                            <li>Four shapes, one set of numbers. The shape follows the decision the reader has to take.</li>
                            <li>On an inherited setup, test whether they agree before rebuilding anything.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Whatever shape those four documents take, the same handful of figures ends up on the front of each. Every one of them describes a period that has already finished.</p>
                            <p>Next: the indicators themselves &#8212; the ones that report the past, the ones that predict the next month, and the one that always lands just under target.</p>''',
)

W22 = dict(
    week=22, file="reporting-week-22.html",
    h1="Every indicator is a rear-view mirror.",
    title="Leading and lagging indicators in project controls",
    desc=("SPI and CPI describe last month. Constraint closure and approval turnaround describe "
          "next month. Why most project KPI packs contain only the first kind."),
    og="Every indicator is a rear-view mirror",
    share="SPI tells you about last month. Constraint closure rate tells you about next month. Most KPI packs contain only the first.",
    crumb="Leading, lagging, and the ones that get gamed",
    body='''<h2 style="margin-top:0;">Every indicator is a rear-view mirror</h2>
                            <p>A typical monthly pack contains progress against plan, schedule performance, cost performance, and a variance or two.</p>
                            <p>Every one of those describes a period that has finished. They are accurate, they are necessary, and none of them tells anybody what is about to happen. A project can have a perfectly healthy set of indicators in the month before everything stops.</p>
                            <p>The methods behind them belong elsewhere &#8212; <a href="cost-week-9.html">Cost &amp; Cash Week 9</a> builds the performance indices. What this week is about is what a pack of them is missing.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Reacting one cycle late, every time</h2>
                            <p>Management reacts to the past, one reporting cycle late, every time.</p>
                            <p>The indicator turns in month four. By the time it is reported and discussed it is month five, and whatever caused it began in month three. The response is therefore always aimed at something that has already finished happening, which is why recovery plans so often address the previous problem.</p>

                            <h2>What a leading indicator looks like</h2>
                            <p>The distinguishing feature is that it measures the conditions for work rather than the work.</p>
                            <p>Constraint closure rate: how many of the things blocking next month&#39;s activities were cleared this month, from <a href="reporting-week-9.html">Week 9</a>. Approval turnaround: how long submittals are taking now, from <a href="reporting-week-15.html">Week 15</a>. Ready workfronts: how many are genuinely available against how many the look-ahead needs. Drawing release against the construction sequence rather than against the engineering plan.</p>
                            <p>None of these is progress. All of them predict it, and all of them are already being collected somewhere on your project for another purpose.</p>

                            <h2>The one that gets gamed</h2>
                            <p>An indicator that somebody is judged on becomes a target, and a target becomes a number that is managed rather than measured.</p>
                            <p>The recognisable symptom is a figure that always lands just under the threshold. Progress that is consistently one point below plan, month after month, is not a measurement of anything. It is a narrative, and it means the estimating discussed in <a href="reporting-week-8.html">Week 8</a> is being tuned to the reporting rather than to the wall.</p>
                            <p>Which is an argument for indicators nobody is judged on. Constraint closure works partly because it is not yet a performance metric anywhere.</p>

                            <h2>How many is too many</h2>
                            <p>Packs grow. Every question anybody has ever asked leaves an indicator behind, and removing one feels like admitting it was never useful.</p>
                            <p>The test is not whether an indicator is interesting. It is whether anybody has changed a decision because of it in the last six months. Most packs contain a handful that pass and a long tail that nobody has looked at since the month they were added.</p>
                            <p>The tail is not harmless. It buries the few that matter, and it makes the pack long enough that the reader skims, which returns us to the failure in <a href="reporting-week-26.html">Week 26</a>. A page with six indicators that are read beats a page with twenty that are not.</p>

                            <h2>Measuring the error before correcting it</h2>
                            <p>If the pack is yours to design, then for every lagging indicator in it, add one leading indicator that predicts it, and keep the pack small enough that both get read.</p>
                            <p>Inherited: do not propose replacing the pack. Add two leading indicators to the existing one and let them run for three months alongside. If they turn before the lagging ones do, the case makes itself. If they do not, you have learned something about your project rather than lost an argument.</p>

                            <h2>Practical insight</h2>
                            <p>List the indicators in your monthly pack and mark each one: does it describe a period that has ended, or conditions that exist now?</p>
                            <p>Most packs come out entirely in the first category. Then pick one thing you already collect that predicts next month &#8212; open constraints, submittals outstanding, workfronts ready &#8212; and put it on the same page. It costs one line and it is the only line on the page about the future.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Standard indices describe a period that has finished. They are necessary and they predict nothing.</li>
                            <li>Management therefore responds a cycle late, to something that has already stopped happening.</li>
                            <li>Leading indicators measure conditions for work: constraints closed, turnaround, ready workfronts, drawing release.</li>
                            <li>All of them are already collected somewhere for another purpose.</li>
                            <li>A figure that always lands just under target is a narrative, not a measurement.</li>
                            <li>Indicators nobody is judged on stay honest longer.</li>
                            <li>On an inherited pack, add two and run them alongside rather than proposing a replacement.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Indicators point at things. What records them, and what closes them, is the next question.</p>
                            <p>Next week: minutes, actions and closure &#8212; and why the fourth step is the one that gets skipped.</p>''',
)


W3 = dict(
    week=3, file="reporting-week-3.html",
    h1="Ninety percent of a drawing is zero on site.",
    title="Engineering deliverables and planning — released for construction",
    desc=("A deliverable register organised by discipline cannot tell a planner which activity a "
          "drawing releases. Why engineering percentage and site readiness are different questions."),
    og="Ninety percent of a drawing is zero on site",
    share="A drawing that is ninety percent complete and cannot go to site is worth nothing to a planner. Released or not released is the only status that plans.",
    crumb="Deliverables, IFC, and what engineering can tell you",
    body='''<h2 style="margin-top:0;">Ninety percent of a drawing is zero on site</h2>
                            <p>Engineering keeps a register. Most projects have one, usually called a deliverable register or a document register, and it lists every drawing and document with a status against it.</p>
                            <p>It is almost always organised by discipline. Civil in one block, mechanical in another, electrical in a third. That is a sensible way to manage an engineering department, because that is how the department is staffed.</p>
                            <p>It is not a sensible way to plan construction, and the mismatch is where the work of this week sits.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <p>The question a planner has is not whether a drawing has been issued. It is which activity a drawing releases. Those look similar and they are not, and on most projects the link between them has never been made by anybody.</p>

                            <h2>The mapping nobody owns</h2>
                            <p>Engineering knows which drawings exist and what state they are in. Construction knows what it wants to build next month. Nothing connects the two lists.</p>
                            <p>So the planner builds the mapping: this activity needs these drawings, at this status, by this date. It is unglamorous work, it takes a week, and it is the single most useful thing that can be done with an engineering register.</p>
                            <p>Once it exists, the engineering deliverable list stops being a document management artefact and becomes a look-ahead input. Without it, the honest answer to whether next month can start is that nobody knows.</p>

                            <h2>What ninety percent means</h2>
                            <p>Engineering reports progress as a percentage, and the percentage is not comparable between people.</p>
                            <p>One engineer counts the calculations as the work, so ninety percent means the analysis is done. Another counts internal checking, so ninety percent means it has been reviewed. A third means the draft exists and the drawing has not been checked by anybody.</p>
                            <p>All three are defensible from inside the discipline. None of them tells a planner anything, because a drawing at ninety percent that cannot go to site releases no activity at all. From the construction side it is worth exactly the same as one that has not been started.</p>

                            <h2>Released, or not released</h2>
                            <p>Which is why the status that matters is binary rather than proportional. Either the drawing is released for construction, at the current revision, in the hands of the people who will build from it &#8212; or it is not.</p>
                            <p>That does not mean engineering should stop measuring percentage. They need it to manage their own workload, and it is a reasonable measure of effort. It means the planner should not use it as a readiness input, because it was never designed to be one.</p>
                            <p>Two measures, two purposes. The failure is using the first for the second because it is the one that arrives in a report.</p>

                            <h2>Two programmes, one project</h2>
                            <p>The last piece is the one that produces the most surprise in meetings.</p>
                            <p>Engineering runs to its own programme, sequenced by discipline and by how the design develops. Construction runs to what it needs next. Those two sequences are related but not identical, and they can diverge for months without anybody noticing.</p>
                            <p>The result is familiar: engineering reports a high overall percentage, the client is pleased, and nothing can start on site because the particular revision the next activity needs has not been issued. Both statements are true at once. Considerable progress on paper, no production in the field.</p>
                            <p>Reporting engineering progress against the construction sequence rather than against the engineering programme is what closes that gap, and it usually requires nothing new to be collected.</p>

                            <h2>Practical insight</h2>
                            <p>Take the ten activities in your next two months with the earliest starts. For each, write down which drawings have to be released for it to begin.</p>
                            <p>Then check each of those against the engineering register. You are looking for one thing: activities where every drawing shows a high percentage and none of them is released.</p>
                            <p>That list is your engineering risk for the quarter, and it will not appear in any engineering report, because from inside the discipline everything on it is nearly finished.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Deliverable registers are organised by discipline because that is how engineering is staffed.</li>
                            <li>A planner needs the opposite view: which activity does this drawing release.</li>
                            <li>Nobody owns that mapping. Building it takes a week and turns the register into a look-ahead input.</li>
                            <li>Ninety percent means different things to different engineers, and all of them are defensible internally.</li>
                            <li>A drawing that cannot go to site releases nothing, whatever percentage it carries.</li>
                            <li>Use percentage for engineering workload and released status for readiness. They are different measures.</li>
                            <li>Engineering can be at ninety-five percent while nothing can start, and both statements are true.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>If percentage is the wrong measure for readiness, something has to replace it in the report.</p>
                            <p>Next week: measuring engineering progress &#8212; weighted deliverables, and the discipline where percent complete is easiest to fake.</p>''',
)

W4 = dict(
    week=4, file="reporting-week-4.html",
    h1="The easiest percentage to move.",
    title="Measuring engineering progress — weighted deliverables and their limits",
    desc=("Engineering progress is the softest number on a project because nothing physical "
          "constrains it. How weighting works, where it breaks, and what to corroborate it against."),
    og="The easiest percentage to move",
    share="Engineering progress has no wall to check it against. It is the softest number on the project and it arrives first.",
    crumb="Weighted deliverables and percent complete",
    body='''<h2 style="margin-top:0;">The easiest percentage to move</h2>
                            <p>Every other progress figure on a project can be checked against something physical. Concrete either exists or it does not. Cable is either pulled or it is not. Somebody can walk over and look.</p>
                            <p>Engineering has no wall. A document is forty percent complete because an engineer says so, and there is no independent record that contradicts it.</p>
                            <p>That makes it the softest number on the project, and it is also the earliest, which means it is the number the first several months of reporting rest on.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>How weighting works</h2>
                            <p>The standard approach is to weight each deliverable by expected effort and assign fixed percentages to defined stages: started, internally checked, issued for review, issued for construction.</p>
                            <p>The reason it works is not that the stages are accurate. It is that they remove the judgement. A drawing at the review stage scores the same regardless of who is reporting it, which makes the aggregate comparable even when each individual estimate is rough.</p>
                            <p>This is the same reasoning as rules of credit for construction, which <a href="cost-week-11.html">Cost &amp; Cash Week 11</a> covers. Fixed steps beat continuous judgement, not because the steps are right but because they are the same for everybody.</p>

                            <h2>Where it breaks</h2>
                            <p>Two failures, and both are visible if you look for them.</p>
                            <p>The first is weighting by count rather than by effort. A hundred small documents and ten large ones give a percentage that moves quickly at the start, when the easy items are being cleared, and then stalls. The curve looks healthy for four months and flat for six.</p>
                            <p>The second is revisions. A drawing issued for construction is at a hundred percent. It comes back with comments, or the design changes, and it has to be reworked. If the register has no way to move a deliverable backwards, the same problem from <a href="reporting-week-11.html">Week 11</a> appears here: effort is being consumed against something that already shows complete.</p>

                            <h2>What can corroborate it</h2>
                            <p>Since there is no physical check, the corroboration has to be procedural, and two records are usually available.</p>
                            <p>Transmittals show what was actually issued, and issuing is an event with a date rather than an opinion. A register claiming a large number of deliverables at issue stage should be matched by transmittals; if it is not, the stage is being assigned before the document leaves.</p>
                            <p>Hours booked to engineering give the other side. Effort expended against progress claimed is the engineering equivalent of the paint check in <a href="reporting-week-8.html">Week 8</a> &#8212; not conclusive, but a large divergence in either direction is worth a question.</p>

                            <h2>Changing the order rather than the length</h2>
                            <p>If the register is new, weight by expected hours, define four or five stages, and decide in advance what happens to a deliverable that is reissued.</p>
                            <p>Inherited: the weighting is probably by count, and changing it will restate the whole series, which nobody will thank you for mid-project. The workable move is to report the released count alongside the percentage. Two numbers, one of which cannot be softened, and the second gradually becomes the one people quote.</p>

                            <h2>Practical insight</h2>
                            <p>Take the engineering register and count two things for last month: how many deliverables moved a stage, and how many transmittals went out.</p>
                            <p>If the first is much larger than the second, progress is being recorded at stages that do not involve anything leaving the department. That is not dishonesty. It is what happens when the stages are defined internally and never checked against an external event.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Engineering progress has no physical record to check it against. It is the softest and earliest number on the project.</li>
                            <li>Weighted stages work because they remove judgement, not because the weights are accurate.</li>
                            <li>Weighting by document count instead of effort produces a curve that races then stalls.</li>
                            <li>A reissued drawing consumes effort against something already showing complete, unless the register can move backwards.</li>
                            <li>Transmittals corroborate the issue stages. Stages assigned before anything leaves are visible this way.</li>
                            <li>Hours booked against progress claimed is the engineering version of the same corroboration.</li>
                            <li>On an inherited register, report released count alongside percentage rather than restating the series.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Drawings release work. So do purchase orders, and the second chain is longer and less visible than the first.</p>
                            <p>Next week: procurement &#8212; order status, expediting, and the promise that keeps moving a week at a time.</p>''',
)

W5 = dict(
    week=5, file="reporting-week-5.html",
    h1="It arrives next week. It has arrived next week for two months.",
    title="Procurement status for planners — expediting and reliable dates",
    desc=("Order status lives with people rather than in the expediting report. Why the first "
          "promise is not the planning date, and what to do with a delivery that keeps moving."),
    og="It arrives next week. It has arrived next week for two months",
    share="The problem is not that the delivery slipped. It is that the programme still shows the date it slipped from.",
    crumb="Order status, expediting, vendor data",
    body='''<h2 style="margin-top:0;">It arrives next week. It has arrived next week for two months</h2>
                            <p>An activity in the look-ahead depends on a piece of equipment. Every week the question is asked, and every week the answer is that it arrives next week.</p>
                            <p>Nobody is lying. Each answer was the best information available on the day it was given, and the date genuinely was next week each time somebody said it.</p>
                            <p>The problem is not the slippage. It is that the programme still shows the date it slipped from, because a revised delivery date is a piece of information that has no defined route from procurement into the schedule.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>The list and the people</h2>
                            <p>Mature projects have an expediting report or a procurement status report. It is real, it is maintained, and it is usually behind.</p>
                            <p>The live information sits with people. Somebody in procurement had a call with the vendor yesterday and knows the shipment has not left. That knowledge reaches the report at the next update cycle, and reaches the planner when somebody thinks to mention it, which is why planners on well-run projects still spend a lot of time in procurement&#39;s office.</p>
                            <p>This is not a criticism of the report. Any status document describes a moment that has passed. What it means is that the report is the record and the conversation is the input, and a planner who relies only on the first is always a cycle late.</p>

                            <h2>The date that goes in the programme</h2>
                            <p>Which of the dates should a planner plan against? Not the original one, which is a commitment rather than a forecast. Not the latest verbal one either, if it has moved three times.</p>
                            <p>What matters is the last date somebody is willing to stand behind with a reason. A date backed by a shipping document, a manufacturing completion, a confirmed booking, is different in kind from one that is simply the previous date plus a week.</p>
                            <p>Two fields make this visible: the current promised date, and how many times it has moved. An item on its fourth revision is a different risk from one on its first, and the count costs nothing to keep.</p>

                            <h2>One chain, three departments</h2>
                            <p>The larger problem is that procurement is not one process but three, watched by three groups who each see their own part.</p>
                            <p>Engineering follows the vendor documents: the drawings and data the supplier has to produce and get approved before manufacturing can start. Procurement follows the order and the shipment. Construction cares only about the date the item is on site and ready to install.</p>
                            <p>These are links in one chain. An approval sitting for three weeks on the engineering side delays manufacturing, which delays shipment, which delays installation. But because each department tracks its own segment, the delay is usually visible only at the end, when it appears as a late delivery rather than as a late approval two months earlier.</p>
                            <p>Reconstructing that chain is planning work and nobody else will do it. It is also where the earliest warning on a plant project comes from, well before anything shows in a progress figure.</p>

                            <h2>Four documents that already exist</h2>
                            <p>If you are building the report, use one line per critical item, with the four dates that matter &#8212; vendor documents approved, manufacturing complete, on site, released to construction &#8212; and a revision count against the promised date.</p>
                            <p>Inherited: the report exists in some form. Rather than replacing it, add the revision count. It is one column, it requires no new source, and it converts a status list into a risk list within two months.</p>

                            <h2>Practical insight</h2>
                            <p>Take the ten items on the critical path with the longest lead times. For each, find the delivery date in the current programme and the date procurement is currently working to.</p>
                            <p>Count how many differ. On most projects it is more than half, and the reason is not carelessness &#8212; there is simply no defined moment at which a revised date becomes a programme change.</p>
                            <p>Making that moment explicit, even monthly, is worth more than any improvement to the report itself.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>The expediting report is the record. The live information is with people, and it arrives earlier.</li>
                            <li>The failure is not slippage. It is that no defined route exists from a revised date into the programme.</li>
                            <li>Plan against the last date somebody will stand behind with a reason, not the first commitment.</li>
                            <li>Count how many times a date has moved. A fourth revision is a different risk from a first.</li>
                            <li>Vendor documents, manufacturing and delivery are one chain watched by three departments.</li>
                            <li>A delayed approval appears months later as a late delivery, and the connection is rarely made.</li>
                            <li>Reconstructing that chain is the earliest warning available on a plant project.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>Material and drawings release work. One department can stop it entirely, and it does not report to project controls.</p>
                            <p>Next week: permits, safety holds and stand-downs &#8212; lost time as a delay event with a record behind it.</p>''',
)

W12 = dict(
    week=12, file="reporting-week-12.html",
    h1="The stoppage nobody recorded as a stoppage.",
    title="HSE data in project reporting — permits, holds and lost time",
    desc=("Safety records and the schedule are usually two disconnected systems. Why a stoppage "
          "reaches the planner late, and what it costs when the cause is never recorded."),
    og="The stoppage nobody recorded as a stoppage",
    share="The delay was recorded. The reason it happened was not, and by the time anybody asks, nobody remembers.",
    crumb="Permits, holds, stand-downs and lost time",
    body='''<h2 style="margin-top:0;">The stoppage nobody recorded as a stoppage</h2>
                            <p>Work stops. A permit was not obtained, or an incident triggered a stand-down, or an area was closed while something was investigated.</p>
                            <p>HSE records it, thoroughly, because that is what the function exists to do. The schedule records something else entirely: an activity that did not progress as expected.</p>
                            <p>Both records are accurate and there is usually no link between them. Months later, when somebody asks why that activity slipped, the answer exists in two systems and in neither.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>How it reaches you, and when</h2>
                            <p>Sometimes it comes up in the daily coordination meeting, which is the good case. Sometimes it appears in the daily report. And sometimes it emerges days later, during variance analysis, when somebody is working out why a figure came in low and a site engineer mentions that the area was shut for two days.</p>
                            <p>That last case is the common one, and the delay matters more than it sounds. A stoppage discovered on the day can be planned around. A stoppage discovered a week later has already consumed the float somebody would have used.</p>

                            <h2>Two systems that do not touch</h2>
                            <p>HSE keeps a permit register, an incident log and a record of stand-downs. Project controls keeps a schedule and a progress record. Neither has a field that points at the other.</p>
                            <p>So the schedule impact is calculated separately, by a planner, from a conversation, and it is recorded as a delay with a duration and no cause. It looks like every other slippage.</p>
                            <p>The consequence appears much later. When a delay analysis is done &#8212; for an extension of time, or a claim, or simply to explain a bad quarter &#8212; the events that caused it have to be reconstructed from memory. <a href="claim-week-6.html">Claims Week 6</a> explains why the contemporaneous record carries the weight it does. This is one of the places it is routinely not made.</p>

                            <h2>Not safety management</h2>
                            <p>It is worth being clear about what a planner is doing here, because it is easy to be resented for it.</p>
                            <p>The planner is not measuring safety performance, not auditing the permit system, and not commenting on whether a stand-down was justified. Those are HSE&#39;s and they are none of project controls&#39; business.</p>
                            <p>What the planner needs is narrower: a stoppage happened, it lasted this long, it affected these activities. That is a scheduling fact that happens to have originated in another function, and asking for it is not an intrusion into how that function does its job.</p>
                            <p>Framing it that way is usually the difference between getting the information and not.</p>

                            <h2>The permit as a readiness test</h2>
                            <p>There is a forward-looking use as well as a backward one.</p>
                            <p>Permits are one of the six readiness tests from <a href="reporting-week-9.html">Week 9</a>, and unlike the other five they are frequently the last one checked. A crew arrives at a workface with drawings, material, plant and access, and cannot start because the permit was applied for that morning.</p>
                            <p>Permit lead time is knowable. It is a number HSE can give you, it does not change much, and adding it to the look-ahead check costs nothing.</p>

                            <h2>Practical insight</h2>
                            <p>Take last month&#39;s activities that lost time and, for each, write the cause in one word. Weather, materials, drawings, access, permit, incident, other.</p>
                            <p>You will not be able to do it for all of them, and the ones you cannot are the point. Those are the delays that have already lost their explanation, and next month there will be more.</p>
                            <p>Then add a single field to the progress update: cause of variance, from a short list. It takes seconds per line, and it is the difference between a delay analysis built from records and one built from recollection.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>HSE records the event and the schedule records the delay. Nothing links them.</li>
                            <li>Stoppages often reach the planner days late, during variance analysis rather than on the day.</li>
                            <li>A stoppage found late has already consumed the float that could have absorbed it.</li>
                            <li>Delays recorded without a cause cannot be reconstructed when a delay analysis needs them.</li>
                            <li>The planner is not auditing safety. The requirement is narrow: it happened, it lasted, it affected these activities.</li>
                            <li>Permits are the readiness test checked last and the one most often missing on the day.</li>
                            <li>A one-word cause field on the progress update is the cheapest contemporaneous record on a project.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>That completes the sources. Everything from here is what you send back, starting with the date that decides how much of it was measured.</p>
                            <p>Next week: document control &#8212; revision status, and the reason half the site can be building to something superseded.</p>''',
)

W18 = dict(
    week=18, file="reporting-week-18.html",
    h1="The meeting about next week is about last week.",
    title="The weekly report and the look-ahead — who prepares it and what it becomes",
    desc=("Most weekly meetings spend their time explaining what did not happen. Why the "
          "look-ahead turns into an explanation list, and why the person who prepares it matters."),
    og="The meeting about next week is about last week",
    share="The look-ahead is a document about next week, prepared for a meeting that spends its time on last week.",
    crumb="What happened, and the only part anyone acts on",
    body='''<h2 style="margin-top:0;">The meeting about next week is about last week</h2>
                            <p>The weekly meeting has two documents. A report, which says what happened. A look-ahead, which says what happens next.</p>
                            <p>In practice most of the hour goes on the first, and not even on the first &#8212; on explaining why parts of it did not happen. Each explanation is reasonable and each one takes four minutes, and by the time the look-ahead is reached there are ten minutes left and everybody has stopped concentrating.</p>
                            <p>The only document in the room that could change next week is the one that gets the least attention.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>How the look-ahead becomes an explanation list</h2>
                            <p><a href="reporting-week-9.html">Week 9</a> followed this from the workface: work that is not ready does not start, does not get removed, and rolls forward. What that looks like from inside the meeting is different, and worse.</p>
                            <p>An item everybody remembers from last week is no longer planned. It is explained. The conversation about it changes register entirely &#8212; from what has to happen for this to start, which is useful, to why it did not, which is not &#8212; and it does so without anybody deciding to change the subject.</p>
                            <p>The tell is easy to spot. Count how many items in this week&#39;s look-ahead were in last week&#39;s. If it is most of them, the document has changed function and nobody has noticed.</p>

                            <h2>Who prepares it</h2>
                            <p>In principle construction prepares the look-ahead, because they are the ones who will do the work and they know what is possible. Project controls consolidates it, checks it against the schedule and the constraints, and challenges what does not hold.</p>
                            <p>In practice project controls often writes it, because the site did not send enough to consolidate. And the moment that happens the ownership problem from <a href="reporting-week-1.html">Week 1</a> reappears in a new place: the plan for next week now belongs to the person who will not be doing any of it.</p>
                            <p>That is worse than it sounds. A look-ahead written by planning is a proposal. One written by construction is a commitment. Only the second is worth taking into a meeting, and the difference has nothing to do with the quality of the document.</p>

                            <h2>What the weekly report is for</h2>
                            <p>The report has a narrower job than most of them do.</p>
                            <p>It records the week for people who were not there, and it feeds the monthly. It is not the place to analyse the project, because the data is a week old and too thin to support conclusions. A weekly report that tries to be a small monthly report is long, late and read by nobody.</p>
                            <p>What earns its space is the exception: what changed, what is now at risk, and what decision is needed. The rest can be a table.</p>

                            <h2>Turning the meeting round</h2>
                            <p>The structural fix is to reverse the order, and it is more effective than it deserves to be.</p>
                            <p>Take the look-ahead first, while there is time and attention. Deal with next week&#39;s constraints while somebody can still act on them, because a constraint discussed on Friday can be cleared by Monday and one discussed at the end of the hour cannot.</p>
                            <p>Then handle last week, briefly, and only for items that change something. An activity that did not start and now has a route is a two-line update. An activity that did not start and still has no route is next week&#39;s problem, which means it belongs in the first half of the meeting rather than the second.</p>

                            <h2>Practical insight</h2>
                            <p>Take the last four look-aheads and mark every activity that appeared in more than one. Then mark the ones that appeared in all four.</p>
                            <p>That second group is not a plan. It is a list of blocked work, and it has been sitting in a planning document rather than in a constraint log where somebody would have had to close it.</p>
                            <p>Move them. The look-ahead gets shorter and more honest, and the constraints become visible to the person who can clear them.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Most weekly meetings spend their time explaining last week rather than planning next week.</li>
                            <li>An activity that does not start and does not leave the list turns the look-ahead into an explanation list.</li>
                            <li>Count how many items repeat from last week. If it is most of them, the document has changed function.</li>
                            <li>Construction should prepare the look-ahead; project controls should consolidate and challenge it.</li>
                            <li>A look-ahead written by planning is a proposal. One written by construction is a commitment.</li>
                            <li>The weekly report records the week and feeds the monthly. It is not the place for analysis.</li>
                            <li>Take the look-ahead first in the meeting, while there is still time to clear a constraint.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>The weekly feeds the monthly, and the monthly is the document the project is judged by.</p>
                            <p>Next week: the monthly report &#8212; and why writing it is the easy part.</p>''',
)

W19 = dict(
    week=19, file="reporting-week-19.html",
    h1="Writing it is the easy part.",
    title="The monthly report — agreeing one number across departments",
    desc=("Producing a monthly report is mostly not writing. It is reaching one figure that four "
          "departments will stand behind, and that work happens in the last days of the month."),
    og="Writing it is the easy part",
    share="Making the chart takes an hour. Getting four departments to agree what the number is takes the last week of the month.",
    crumb="Curve, variance, narrative, summary",
    body='''<h2 style="margin-top:0;">Writing it is the easy part</h2>
                            <p>Ask what takes the time in a monthly report and most people will say the report. The curve, the tables, the narrative, the slides.</p>
                            <p>Those take an afternoon. What takes the last days of the month is reaching a figure that more than one department will stand behind.</p>
                            <p>That is the real work, and it is invisible from outside, which is why the monthly report is chronically underestimated by everybody who does not produce one.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>Where the time actually goes</h2>
                            <p>Collection is slow but predictable. The unpredictable part is what happens when the collected records do not agree, which is most months.</p>
                            <p>The site quantity does not match the surveyed one. The cost report closed on a different date. A late delivery note changes the material position. Each of these needs a conversation with the department that owns the record, and the conversations cannot be parallelised because the answer to one changes the next.</p>
                            <p>This is the routine from <a href="reporting-week-8.html">Week 8</a> and the reconciliation from <a href="reporting-week-25.html">Week 25</a>, compressed into three or four days. Which is the argument for spreading it: the more of it that happens weekly, the less of it lands at month end.</p>

                            <h2>Everybody gets it, nobody reads all of it</h2>
                            <p>The monthly goes to a wide distribution and each reader opens it at a different page.</p>
                            <p>Senior management reads the summary and stops. The project manager reads the indicators. Department heads read their own section and glance at the rest. The client reads progress, milestones, risks and anything about delay, in that order.</p>
                            <p>Which means the document is really five documents bound together, and the parts most people never reach still have to be right &#8212; because the one month somebody does turn to page eleven is the month something has gone wrong.</p>
                            <p>It also means the summary is not a summary. It is the report, for most of its readers, and it deserves the time that implies. <a href="reporting-week-20.html">Week 20</a> deals with how to do that without producing five different stories.</p>

                            <h2>The narrative is the part that ages</h2>
                            <p>Charts are read in the month they are issued. The narrative is what somebody reads two years later, trying to establish what was known and when.</p>
                            <p>That gives it a second job, and it changes how it should be written. A sentence saying progress was below plan due to various factors is useless in both roles. A sentence naming the cause, the affected activities and what was done about it is useful now and evidence later.</p>
                            <p>It costs nothing extra. It is the same length. The difference is specificity, and the reason it is usually missing is that specific sentences are harder to agree in the last two days of the month, which brings us back to where the time goes.</p>

                            <h2>Adding rather than replacing</h2>
                            <p>If you are setting the process up, fix the cut-off and agree the reconciliation before the report rather than during it, and keep the summary to one page that can be read alone.</p>
                            <p>Inherited: the report is probably too long and nobody will let you shorten it. The realistic move is to change the front rather than the whole. Make the first page carry the decisions, the exceptions and the changed dates, and let the rest stay as it is. Length is a habit and it is hard to break. Order is a choice and it can be changed next month.</p>

                            <h2>Practical insight</h2>
                            <p>Time yourself for one cycle. Record hours spent on collection, on reconciliation, and on producing the document.</p>
                            <p>Most planners are surprised by the proportion, and the number is useful for two arguments: it justifies the resource, and it shows exactly which of the three would benefit from being moved earlier in the month.</p>
                            <p>Almost always it is the middle one, and almost always it can be spread into the weekly cycle at no extra cost.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Producing the document is an afternoon. Agreeing the number takes the last days of the month.</li>
                            <li>Reconciliation cannot be parallelised, because each answer changes the next question.</li>
                            <li>The more reconciliation happens weekly, the less of it lands at month end.</li>
                            <li>Everybody receives the same report and each reader opens it at a different page.</li>
                            <li>For most readers the summary is the report, not a summary of it.</li>
                            <li>The narrative is what gets read years later. Specific sentences are useful now and evidence afterwards.</li>
                            <li>On an inherited report, change the order rather than the length. Length is a habit; order is a choice.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>One document, several readers, several levels of detail &#8212; and the risk of telling each of them something slightly different.</p>
                            <p>Next week: four audiences, four altitudes, and one set of numbers.</p>''',
)


W21 = dict(
    week=21, file="reporting-week-21.html",
    h1="One screen, two conclusions.",
    title="Why dashboards do not align an organisation",
    desc=("Two managers leave the same dashboard review having reached different conclusions. The "
          "cause is not the dashboard. It is that nothing behind it was defined in common."),
    og="One screen, two conclusions",
    share="A dashboard cannot align an organisation. If the organisation is already aligned it makes that visible. If it is not, it makes the disagreement look professional.",
    crumb="What a dashboard cannot say",
    body='''<h2 style="margin-top:0;">One screen, two conclusions</h2>
                            <p>A review meeting. One dashboard on the wall, and everybody in the room is looking at it.</p>
                            <p>An hour later two experienced people leave having reached different conclusions about the same project. Not slightly different &#8212; one thinks the position is recoverable and one does not.</p>
                            <p>Neither of them misread anything. The screen was accurate, the figures were current, and nobody was being difficult.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                            <h2>What a dashboard actually is</h2>
                            <p>Everything in this track ends up on that screen.</p>
                            <p>Quantities from the site. Hours from the timesheets. Cost from a ledger that closed on its own date. Drawing status from document control. Deliveries from the store. Approvals from the client. Twenty-five weeks of records, from seven or eight departments, reduced to a page of tiles.</p>
                            <p>That reduction is the point of it and it is also the problem. A dashboard shows the output of a data model. It does not show the model, and it certainly does not show where the model is weak.</p>

                            <h2>Why two readers diverge</h2>
                            <p>The divergence has causes and they are all upstream.</p>
                            <p>If two departments calculate the same indicator differently, the tile shows one of the two versions and does not say which. If cost closed on the fifteenth and progress on the twentieth, the two tiles beside each other describe different months. If a quantity was estimated rather than measured, it looks exactly like one that was counted. If nobody owns a figure, nobody can be asked what it means.</p>
                            <p>Each reader then fills the gaps from what they know. One has been in procurement all week and reads the screen through the deliveries. Another remembers a conversation about rework. Both are reasoning correctly from the same display and arriving somewhere different, because the display carries the numbers and not what is behind them.</p>
                            <p>That is the failure this week is about, and it is not a design failure.</p>

                            <h2>Changing the screen changes nothing</h2>
                            <p>The instinct when this happens is to improve the dashboard. Add a chart. Change the thresholds. Show a different indicator. Somebody suggests a different tool.</p>
                            <p>None of it works, for a reason that is obvious once stated: the disagreement was never about presentation. Two people who do not share a definition of complete will not come to share one because the tile turned a different colour.</p>
                            <p>Which is why the response to a dashboard argument belongs at the input. Which indicator, calculated how, from which record, closed on which date, owned by whom. Answer those and the screen stops being contentious, usually without anybody touching it.</p>

                            <h2>What it can and cannot do</h2>
                            <p>A dashboard cannot align an organisation. If the organisation is already aligned &#8212; shared definitions, agreed cut-offs, owned figures &#8212; it makes that alignment visible and useful. If it is not, it makes the disagreement look professional.</p>
                            <p>That is worth stating because the opposite is widely believed. Projects buy tools expecting them to produce agreement, and what arrives is a better rendering of a disagreement that was already there.</p>
                            <p>There is one thing a dashboard does that nothing else does, and it is not the thing it is bought for. It puts every department&#39;s output on one page at one moment, which means inconsistencies that were survivable while they lived in separate documents suddenly sit next to each other. A project that has never reconciled anything finds out on the day the dashboard goes live.</p>

                            <h2>The version that works</h2>
                            <p>A dashboard is defensible when three things are true of every tile on it, and they are all upstream of the tool.</p>
                            <p>The indicator has one definition, written down, used by everybody who produces or consumes it. The data behind it closed on a date the reader can find. And somebody owns it, meaning there is a person who can be asked what it means and who will answer the same way next month.</p>
                            <p>Tiles that fail any of the three should not be there. A page of six figures that meet all three is worth more than twenty that do not, and it is a shorter argument than any redesign.</p>

                            <h2>Where this leaves the track</h2>
                            <p>Twenty weeks of this have been about single records: what a quantity means, when a ledger closes, which revision is current, who owns a number.</p>
                            <p>The screen is where all of it becomes visible at once, to people who were not involved in producing any of it. Which makes it the honest test of whether the work was done &#8212; not of whether the dashboard is any good.</p>

                            <h2>Practical insight</h2>
                            <p>Take your dashboard and pick three tiles. For each one, answer three questions without looking anything up.</p>
                            <p>What exactly does this measure, in one sentence that a second department would agree with? What date is the underlying data closed to? Who would you go to if it were challenged?</p>
                            <p>Any tile where you cannot answer all three is a tile two readers can legitimately interpret differently. On most projects that is more than half the page, and it explains the meeting.</p>
                            <p>Then do it once more, with somebody from another department, on the same three tiles. Where their sentence differs from yours, you have found the reason two people can leave the same review disagreeing.</p>

                            <h2>Key takeaways</h2>
                            <ul class="takeaways">
                            <li>Two people can read the same dashboard correctly and reach different conclusions.</li>
                            <li>A dashboard shows the output of a data model. It does not show the model, or where it is weak.</li>
                            <li>Different definitions, different cut-offs, estimated figures and unowned numbers all look identical on a tile.</li>
                            <li>Readers fill the gaps from what they happen to know, which is why they diverge.</li>
                            <li>Improving the display cannot resolve a disagreement that was never about the display.</li>
                            <li>A dashboard cannot align an organisation. Aligned, it makes that visible; unaligned, it makes the disagreement look professional.</li>
                            <li>It does put every department on one page at one moment, which is where a project finds out it has never reconciled anything.</li>
                            <li>A tile is defensible when it has one written definition, a findable cut-off date, and an owner who will answer the same way next month.</li>
                            </ul>

                            <h2>What is coming next</h2>
                            <p>If a tile has to have one definition and one owner, the next question is which tiles are worth the page at all.</p>
                            <p>Next week: leading and lagging indicators &#8212; the ones that describe last month, the ones that describe the next, and the one that always lands just under target.</p>''',
)


# --------------------------------------------------------------------------
# The data dictionary.
#
# One shape for every week: Record / Produced by / Required quality / Verified
# against / Feeds. The columns are fixed because these tables are the common
# data model the later modules will sit on, and a dictionary whose shape
# changes per entry is not a dictionary.
#
# Required quality answers one question and only one: can project controls use
# this as it arrives, without doing anything to it first? Where the answer is
# no, the entry names what is missing rather than describing the record. That
# column is the usability definition, and it is the part that does not exist
# anywhere else.

COLS = ["Record", "Produced by", "Required quality", "Verified against", "Feeds"]

ROWS = {
 1: [("Installed quantities", "Site engineer", "Against an activity and an area, in the unit of the bill", "Store issues, survey", "Progress, schedule update"),
     ("Manhours", "Supervisor", "Allocated to activities, not just totalled", "Attendance", "Productivity, earned hours"),
     ("Plant hours", "Equipment department", "Running hours separated from present hours", "Operator log", "Utilisation, method decisions"),
     ("Material issued", "Store", "Issued quantity, not delivered quantity", "Delivery notes", "Progress corroboration"),
     ("Drawing revision", "Document control", "Current status, and who holds it", "Site spot check", "Readiness, progress claim"),
     ("Inspection sign-off", "QA/QC", "Tied to the activity, not just the system", "Inspection record", "Completion, handover"),
     ("Commitments and accruals", "Commercial", "Coded to the same breakdown you report on", "Invoices", "Cost report, forecast")],
 2: [("Installed quantity", "Site engineer", "One unit per field, defined once and not per person", "Survey", "Progress"),
     ("Area or system", "Site engineer", "A coded value, not free text", "Area coding", "Productivity by area"),
     ("Activity reference", "Site engineer", "A schedule ID that exists", "Schedule", "Progress, earned value"),
     ("Hours", "Supervisor", "Allocated against the same activity list", "Attendance", "Productivity"),
     ("Drawing revision built to", "Site engineer", "Recorded at the time, not reconstructed", "Transmittal register", "Progress validity")],
 3: [("Deliverable list", "Engineering", "Mapped to the activity each drawing releases", "Construction sequence", "Look-ahead, constraints"),
     ("Released status", "Document control", "Binary, and reflecting what the crew holds", "Site spot check", "Readiness test"),
     ("Required-by date", "Project controls", "Derived from activity starts, not from engineering", "Schedule", "Engineering priorities")],
 4: [("Deliverable weighting", "Engineering", "By expected hours, not by document count", "Historic effort", "Engineering progress"),
     ("Stage reached", "Discipline lead", "Defined stages applied the same way by everybody", "Transmittal record", "Progress, earned value"),
     ("Hours booked to engineering", "Timesheets", "Split by discipline", "Progress claimed", "Productivity, forecast"),
     ("Released count", "Document control", "A count, which cannot be softened", "Transmittals", "The figure people end up quoting")],
 5: [("Vendor documents approved", "Engineering", "Dated, with the approval status", "Transmittal record", "Manufacturing release"),
     ("Manufacturing complete", "Procurement", "Confirmed by the vendor, not assumed", "Vendor confirmation", "Shipment forecast"),
     ("On site", "Logistics", "Date of arrival and acceptance", "Delivery note", "Readiness test"),
     ("Promised date", "Procurement", "Backed by a document or a booking, not last week plus seven", "Shipping record", "Programme"),
     ("Times revised", "Project controls", "A count kept from the first promise", "The date history", "Risk register, forecast")],
 6: [("Delivered", "Logistics", "Quantity accepted, in the bill unit", "Delivery note", "Cost report"),
     ("In store", "Storekeeper", "Current holding, not cumulative receipts", "Stock count", "Materials status"),
     ("Issued", "Storekeeper", "Against an activity or area, not just a date", "Store record", "Progress corroboration"),
     ("Installed", "Site engineer or survey", "Physically in place, not staged at the workface", "Survey", "Progress, schedule")],
 7: [("Bill quantity", "Estimating", "Frozen, with variations tracked separately", "Contract", "Baseline, payment"),
     ("Drawing quantity", "Engineering", "From the current revision, dated", "Revision register", "Site, procurement"),
     ("Measured quantity", "Quantity surveyor", "Measured under the contract rules", "Site measurement", "Valuation"),
     ("Denominator in use", "Project controls", "Stated, and restated visibly when scope moves", "Change register", "Every progress percentage")],
 8: [("Claimed quantity", "Site engineer", "Measured, or flagged as estimated", "Delivery notes, store issues", "Progress"),
     ("Measured quantity", "Quantity surveyor", "Independent of the progress claim", "Site measurement", "Valuation, corroboration"),
     ("Attendance", "HR", "By area and day", "Gate record", "Plausibility of the claim"),
     ("Inspection record", "QA/QC", "Linked to the activity claimed", "Inspection request", "Completion evidence"),
     ("Rules of credit", "Project controls", "Agreed before work starts, not after", "Baseline", "How a quantity becomes a percentage")],
 9: [("Constraint", "Whoever is blocked", "Named against one of the six tests", "The workfront", "Look-ahead"),
     ("Owner", "Project controls", "A person who can clear it, not a department", "Organisation", "Follow-up"),
     ("Closure", "The owner", "Who, when, and the evidence", "The evidence itself", "Ready work list"),
     ("Ready work list", "Project controls", "Only items passing all six tests", "Constraint log", "Look-ahead, weekly meeting")],
 10: [("Attendance", "HR or security", "By area and day", "Gate record", "Headcount, cost"),
      ("Hours allocated", "Supervisor", "From a short list of plausible activities", "Attendance by area", "Productivity"),
      ("Plant availability", "Equipment department", "On site and serviceable", "Equipment log", "Resourcing"),
      ("Plant utilisation", "Site", "Running hours, with idle separated from breakdown", "Operator record", "Method decisions")],
 11: [("NCR", "QA/QC", "Linked to the activity, not only to the system", "Inspection record", "Quality, progress"),
      ("Category", "QA/QC lead", "Decided before the event: does it reverse progress", "The disposition", "Progress adjustment"),
      ("Rework hours and quantities", "Site engineer", "Flagged against the original activity", "Timesheet", "Productivity, cost"),
      ("Progress adjustment", "Project controls", "Applied with a reason, not silently", "The NCR", "Report, schedule")],
 12: [("Permit status", "HSE", "Current, per activity and location", "Permit register", "Readiness test"),
      ("Permit lead time", "HSE", "A historic average, not a target", "Permit history", "Look-ahead check"),
      ("Stoppage", "HSE or site", "Duration and area, on the day", "Daily report", "Progress variance"),
      ("Cause of variance", "Project controls", "One word from a fixed list, on every delayed line", "The stoppage record", "Delay analysis, claims")],
 13: [("Transmittal", "Document control", "Dated, with the distribution list", "The register", "Revision status"),
      ("Acknowledgement", "Recipient", "Confirmed by them, not by the sending system", "The reply", "Distribution completeness"),
      ("Withdrawal", "Named person on site", "Old copy out of use, with a name against it", "Site spot check", "Single valid revision"),
      ("Revision in use", "Spot check", "What the crew is holding today", "Physical check", "Readiness, progress validity")],
 14: [("Commitments", "Commercial", "Coded to the breakdown you report on", "Purchase orders", "Forecast"),
      ("Accruals", "Commercial", "Stated basis: from progress, or independently estimated", "Progress figure", "Cost report"),
      ("Invoices", "Commercial", "Dated to the work period, not the payment date", "Delivery and measurement", "Actual cost"),
      ("Cost cut-off date", "Commercial", "Written down, and known to you before the month closes", "Finance calendar", "Reconciliation")],
 15: [("Submittal sent", "Project or engineering", "Dated at issue", "Transmittal", "Turnaround measurement"),
      ("Submittal returned", "Client or consultant", "Dated at receipt, with status", "Correspondence", "Turnaround, readiness"),
      ("Comment decision", "Engineering", "Who read the comments and what they concluded", "The marked drawing", "Whether work can start"),
      ("Actual turnaround", "Project controls", "Observed, not the contractual period", "The two dates", "Programme durations"),
      ("Informal request", "Project controls", "Logged after answering, even when trivial", "The message", "Workload visibility")],
 16: [("Reporting calendar", "Project controls", "One page holding all three closing dates", "Finance and contract dates", "Every report"),
      ("Data date", "Project controls", "Coinciding with the collection cut-off", "The schedule", "Schedule update"),
      ("Collection cut-off", "Project controls", "Late enough that the site can count, early enough to be read", "The meeting it feeds", "Report content"),
      ("Boundary item list", "Both sides", "Made monthly, before publication", "The two cut-offs", "Reconciliation")],
 17: [("Daily report", "Site engineers, consolidated", "Fields either filled or marked not yet reported", "Store, survey, attendance", "Weekly report, records"),
      ("Revision number", "Project controls", "Incremented, never a new file with the same name", "The issue log", "Which version is current"),
      ("What changed and why", "Whoever corrected it", "The field, the old value, and the reason", "The original issue", "Audit trail, delay analysis"),
      ("Not-yet-reported list", "Site engineers", "Explicit blanks rather than invented figures", "Next day&#39;s data", "Follow-up")],
 18: [("Look-ahead", "Construction", "Only work passing the six readiness tests", "Constraint log", "Next week&#39;s work"),
      ("Constraint items", "Project controls", "Moved out of the look-ahead into the log", "The six tests", "Constraint closure"),
      ("Weekly report", "Project controls", "Exception and change, not analysis", "The week&#39;s records", "Monthly report"),
      ("Actions", "The meeting", "Owner, date, and what done looks like", "Follow-up", "Closure")],
 19: [("Collected data", "All departments", "Complete by the cut-off, in agreed units", "Reporting calendar", "Reconciliation"),
      ("Agreed figure", "Project controls with owners", "Signed off by the record holders, not adjusted alone", "Corroborating records", "Every document that month"),
      ("Narrative", "Project controls", "Cause, activities affected, and response &#8212; not &#8220;various factors&#8221;", "The variance causes", "Now, and delay analysis later"),
      ("Summary page", "Project controls", "Readable alone, because for most readers it is the report", "The detail", "Management decisions")],
 20: [("The extraction", "Project controls", "One cut, one moment, one data set", "The cut-off", "All four reports"),
      ("Look-ahead view", "Construction", "Activity and area level", "The extraction", "What to start"),
      ("Internal report", "Project controls", "Discipline level, same numbers", "The extraction", "Where to move resources"),
      ("Executive summary", "Project controls", "Trend and exception, same numbers", "The extraction", "Whether to intervene"),
      ("Client report", "Project controls", "Contract position, same numbers", "The extraction", "Entitlement, payment")],
 22: [("Progress against plan", "Project controls", "Usable as is &#8212; and describes a finished period", "The baseline", "Performance review"),
      ("Schedule and cost indices", "Project controls", "Usable as is &#8212; and describes a finished period", "Cost report", "Performance review"),
      ("Constraint closure rate", "Project controls", "Count of closures with evidence, not verbal", "Constraint log", "Whether next month starts"),
      ("Approval turnaround", "Project controls", "Observed, rolling, not contractual", "Submittal log", "Engineering and procurement dates"),
      ("Ready workfronts", "Construction", "Passing all six tests, against what the look-ahead needs", "Workfront register", "Achievable look-ahead")],
 23: [("Written statement of the disagreement", "Project controls", "Sent before the call, not after it", "The records that differ", "The conversation"),
      ("Minutes", "The chair", "Decisions and actions, not discussion", "The meeting", "Action log"),
      ("Action", "The meeting", "A person, a date, and what done looks like", "Follow-up", "Closure"),
      ("Closure", "The owner", "Who closed it, when, and on what evidence", "The evidence", "Whether it reappears next week")],
 24: [("Assumption register", "Project controls", "Written down while it is still an assumption", "Reality", "Risk register"),
      ("Risk register", "Risk owner", "Each entry linked to a decision that would close it", "Assumptions, events", "Change, decisions"),
      ("Interface register", "Project controls", "One identifier that travels between registers", "The other registers", "Constraint log"),
      ("Constraint log", "Project controls", "Closure with evidence", "The workfront", "Look-ahead"),
      ("Decision register", "Whoever has authority", "The decision, dated, and what it closed", "The register it closed", "All six others"),
      ("Action register", "The meeting", "Owner and date", "Follow-up", "All six others")],
 25: [("Progress figure", "Project controls", "Built on rules of credit agreed at the start", "Corroborating records", "Report, schedule"),
      ("Valuation", "Commercial", "Measured under the contract rules", "Site measurement", "Payment application"),
      ("Difference", "Both, jointly", "Split into timing, measurement and error", "Both records", "The reconciliation"),
      ("Agreed treatment", "Commercial", "Decided by the record holders, not by project controls", "The decision", "Both documents")],
 26: [("Decision needed", "Project controls", "A request, not a description of a situation", "The underlying data", "The meeting"),
      ("Owner", "Project controls", "A person who can take it", "Organisation", "Follow-up"),
      ("By when", "Project controls", "A date the consequence is measured against", "The programme", "Escalation"),
      ("If not taken", "Project controls", "The cost of doing nothing, stated", "Schedule and cost impact", "Whether anybody acts"),
      ("The report itself", "Project controls", "Specific enough to be read as evidence later", "The records behind it", "Delay analysis, claims")],
}

# --------------------------------------------------------------------------
# System design and Records born here.
#
# One table per week, placed before Practical insight, and one line naming the
# records that come into existence at that stage. Deliberately not a six-column
# specification: the reader-facing version carries the owner and nothing else,
# because a table with six columns reads as a form to be filled rather than a
# question to be answered. The fuller version — source, validation method,
# update frequency, consumer — is a working document for building the system,
# not article content.
#
# There is no "feeds next" line. Which record feeds which is week 24's subject,
# and on most weeks the honest answer would be "the archive".

TSTYLE = ('style="width:100%;border-collapse:collapse;margin:18px 0;font-size:13.5px;">')
TH = ('style="text-align:left;padding:9px 12px;background:#f1f5f9;color:#334155;'
      'font-weight:700;border-bottom:1px solid #e2e8f0;"')
TD = 'style="padding:9px 12px;border-bottom:1px solid #f1f5f9;color:#475569;"'


def table(cols, rows):
    h = "".join(f"<th {TH}>{c}</th>" for c in cols)
    b = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table {TSTYLE}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def sysdesign(intro, tbl, note):
    return ("<h2>System design</h2>\n                            <p>" + intro + "</p>\n"
            "                            " + tbl + "\n"
            "                            <p>" + note + "</p>")


def records(items):
    return ('<p style="margin-top:22px;padding:14px 18px;background:#f8fafc;border-left:3px solid #10b981;'
            'border-radius:0 8px 8px 0;font-size:13.5px;color:#475569;">'
            '<strong style="color:#334155;">Records born here.</strong> ' + items + "</p>")


DESIGN = {
    1: (sysdesign(
        "One column, not four. The question that has no answer when a figure is challenged is who owns it, and a table that also records who checks it and who approves it turns a single missing name into three arguments.",
        table(["Input", "Produced by", "Owner"], [
            ["Installed quantities", "Site engineer", "Area manager"],
            ["Manhours", "Timesheets and supervisor", "Construction manager"],
            ["Plant hours", "Equipment department", "Equipment manager"],
            ["Material issued", "Store", "Store manager"],
            ["Current drawing revision", "Engineering", "Lead engineer"],
            ["Inspection sign-off", "QA/QC", "QA/QC lead"],
            ["Permits and holds", "HSE", "HSE lead"],
            ["Commitments and accruals", "Commercial", "Commercial manager"],
        ]),
        "Fill it once, agree it in a meeting, and put it in the project execution plan. The value is not the table. It is that the argument about who owns a number happens now, in an hour, rather than in six months when the number is already in a report somebody is challenging."),
        records("Data ownership register &#183; the input list behind each deliverable.")),
    8: (sysdesign(
        "Corroboration is a checking routine, not a form. For each claimed quantity, name the record that was produced by somebody with no interest in your progress figure.",
        table(["Claimed", "Corroborating record", "Held by"], [
            ["Installed quantity", "Delivery note or weighbridge ticket", "Store or logistics"],
            ["Installed quantity", "Store issue", "Store"],
            ["Measured quantity", "Payment measurement", "Quantity surveyor"],
            ["Work volume", "Attendance record", "HR"],
            ["Completed work", "Inspection and test record", "QA/QC"],
        ]),
        "None of these measures progress. Each of them constrains it, and a claim that survives all five is one you can defend without re-measuring anything."),
        records("Progress claim sheet &#183; corroboration note &#183; the query email when two records disagree.")),
    3: (sysdesign(
        "The register engineering keeps and the view a planner needs are different cuts of the same list. This is the second one.",
        table(["Data", "Produced by", "Verified against", "Feeds"], [
            ["Deliverable list", "Engineering", "The construction sequence", "Look-ahead &#183; constraint log"],
            ["Released status", "Document control", "What the crew is holding", "Readiness test &#183; progress claim"],
            ["Required-by date", "Project controls", "Activity start dates", "Engineering priorities"],
        ]),
        "The third row is the one that does not exist on most projects. Without a required-by date, engineering has no way to know which of two drawings matters more this month."),
        records("Drawing-to-activity map &#183; required-by list &#183; the engineering risk list for the quarter.")),
    4: (sysdesign(
        "Weighted stages, and two records that can contradict them. Neither corroboration is conclusive; both are free.",
        table(["Data", "Produced by", "Verified against", "Feeds"], [
            ["Deliverable weighting", "Engineering", "Expected hours, not count", "Engineering progress"],
            ["Stage reached", "Discipline lead", "Transmittal record", "Progress &#183; earned value"],
            ["Hours booked", "Timesheets", "Progress claimed", "Productivity &#183; forecast"],
            ["Released count", "Document control", "&#8212;", "The number that cannot be softened"],
        ]),
        "The last row is the antidote to the first three. Report it alongside the percentage and it gradually becomes the figure people quote."),
        records("Weighted deliverable register &#183; transmittal log &#183; released count series.")),
    5: (sysdesign(
        "One line per critical item, four dates, and a count. The count is the field that turns a status report into a risk report.",
        table(["Data", "Produced by", "Verified against", "Feeds"], [
            ["Vendor documents approved", "Engineering", "Transmittal record", "Manufacturing release"],
            ["Manufacturing complete", "Procurement", "Vendor confirmation", "Shipment"],
            ["On site", "Logistics", "Delivery note", "Readiness test"],
            ["Promised date", "Procurement", "Shipping document or booking", "Programme"],
            ["Times revised", "Project controls", "&#8212;", "Risk register &#183; forecast"],
        ]),
        "Rows one to three are the chain three departments watch separately. Putting them on one line is what makes a late approval visible before it becomes a late delivery."),
        records("Expediting report with revision count &#183; long lead register &#183; the chain view per critical item.")),
    12: (sysdesign(
        "Nothing here asks HSE to change how it works. It asks for one fact in a form the schedule can use.",
        table(["Data", "Produced by", "Verified against", "Feeds"], [
            ["Permit status", "HSE", "Permit register", "Readiness test"],
            ["Permit lead time", "HSE", "Historic average", "Look-ahead check"],
            ["Stoppage: duration and area", "HSE or site", "Daily report", "Progress variance"],
            ["Cause of variance", "Project controls", "The stoppage record", "Delay analysis &#183; claims"],
        ]),
        "The last row is a single field on the progress update, filled from a short list. It is the cheapest contemporaneous record a project can keep and the one most often missing."),
        records("Permit register &#183; stoppage log with durations &#183; cause-of-variance field on every progress line.")),
    18: (sysdesign(
        "Two documents with two different jobs, and the ownership question decides whether either works.",
        table(["Document", "Produced by", "Verified against", "Feeds"], [
            ["Look-ahead", "Construction", "Constraints and schedule", "Next week&#39;s work"],
            ["Constraint items", "Project controls", "The six readiness tests", "Constraint log, not the look-ahead"],
            ["Weekly report", "Project controls", "The week&#39;s records", "Monthly report"],
            ["Actions", "The meeting", "Owner and date", "Follow-up"],
        ]),
        "The second row is the correction. Blocked items belong in a constraint log where somebody has to close them, not in a plan where they can sit for months looking like work."),
        records("Look-ahead &#183; weekly report &#183; action list &#183; the constraint entries moved out of the look-ahead.")),
    19: (sysdesign(
        "The report is the last step. What decides whether it can be produced is when the reconciliation happens.",
        table(["Step", "Produced by", "Verified against", "Feeds"], [
            ["Collection", "All departments", "The reporting calendar", "Reconciliation"],
            ["Reconciliation", "Project controls with owners", "Corroborating records", "The agreed figure"],
            ["Agreed figure", "Jointly", "&#8212;", "Every document that month"],
            ["Narrative", "Project controls", "The variance causes", "Now, and a delay analysis later"],
        ]),
        "Move as much of row two into the weekly cycle as will go. Whatever is left is what the last days of the month are for, and it cannot be compressed by working faster."),
        records("Monthly report &#183; the agreed figure and who agreed it &#183; the narrative, which is read twice and years apart.")),
    6: (sysdesign(
        "Three questions per row: where the number is born, who produces it, and which process consumes it. Without the third column a register is a list; with it, it is a system.",
        table(["Quantity", "Born where", "Produced by", "Consumed by"], [
            ["Delivered", "Gate or laydown", "Logistics", "Commercial &#183; cost report"],
            ["In store", "Warehouse", "Storekeeper", "Materials status"],
            ["Issued", "Store counter", "Storekeeper", "Progress corroboration"],
            ["Installed", "Workface", "Site engineer or survey", "Progress report &#183; schedule update"],
        ]),
        "Only the last row is progress. If your report cannot state which of the four it used, the answer is decided by whoever built the spreadsheet."),
        records("Materials reconciliation &#183; store issue log &#183; installed quantity record.")),
    7: (sysdesign(
        "The three sources and what each is entitled to answer. The column that matters is the last one, because that is where the disagreements surface.",
        table(["Source", "Born where", "Produced by", "Consumed by"], [
            ["Bill quantity", "Tender", "Estimating", "Baseline &#183; payment"],
            ["Drawing quantity", "Current revision", "Engineering", "Site &#183; procurement"],
            ["Measured quantity", "The wall", "Quantity surveyor", "Valuation"],
        ]),
        "From scratch, the denominator is stated once in the procedure. Inherited, the useful step is to find out which of the three each existing document already uses."),
        records("Quantity source statement &#183; the re-baselined denominator after each variation.")),
    10: (sysdesign(
        "Nothing here needs new collection. What it needs is a shorter list of choices at the point of entry, and a level at which the output is quoted.",
        table(["Data", "Born where", "Produced by", "Consumed by"], [
            ["Attendance", "Gate", "HR or security", "Headcount &#183; cost"],
            ["Hours allocated", "Timesheet, end of shift", "Supervisor", "Productivity &#183; earned hours"],
            ["Plant availability", "Equipment log", "Equipment department", "Utilisation"],
            ["Plant utilisation", "Operator record", "Site", "Method and resourcing decisions"],
        ]),
        "Keep the allocation list tied to the area coding, so the choices on the sheet match the work in front of the person filling it in. Then quote productivity at the level where allocated hours reconcile with attendance."),
        records("Timesheet &#183; allocation sheet &#183; plant log with idle time separated from breakdown.")),
    11: (sysdesign(
        "Two decisions, taken before the first non-conformance rather than during it: which categories reverse progress, and where rework hours land.",
        table(["Field", "Born where", "Produced by", "Consumed by"], [
            ["NCR", "Inspection", "QA/QC", "Quality &#183; progress"],
            ["Category", "NCR review", "QA/QC lead", "Decides whether progress reverses"],
            ["Rework flag", "Timesheet and quantity", "Site engineer", "Productivity &#183; cost"],
            ["Progress adjustment", "Progress update", "Project controls", "Report &#183; schedule"],
        ]),
        "The category is the field that does the work. Without it the choice falls to whoever is updating the sheet, and they will leave the number alone."),
        records("NCR register &#183; rework-flagged hours and quantities &#183; the progress adjustment record.")),
    20: (sysdesign(
        "One cut, four views. What matters is not the format of each document but that all four are produced from the same extraction at the same moment.",
        table(["Report", "Level", "Produced from", "Reader decides"], [
            ["Look-ahead", "Activity, area", "The single cut", "What to start"],
            ["Weekly internal", "Discipline", "The single cut", "Where to move resources"],
            ["Monthly executive", "Trend, exception", "The single cut", "Whether to intervene"],
            ["Client report", "Contract position", "The single cut", "Entitlement and payment"],
        ]),
        "The third column is the same in every row on purpose. If any report is produced from a different extraction or a different date, the four stop reconciling and nobody finds out until two of them meet."),
        records("The extraction itself, dated &#183; the four views &#183; the exception list applied at source.")),
    21: (sysdesign(
        "Nothing here is about the tool. These are the three things that have to be true of a figure before it is worth putting on a screen at all.",
        table(COLS, [
            ["Indicator definition", "Project controls with the owner", "One sentence a second department would agree with", "The producing department", "Every tile using that figure"],
            ["Cut-off date behind the tile", "Project controls", "Findable by the reader, not implied", "The reporting calendar", "Whether two tiles are comparable"],
            ["Figure owner", "Named person", "Someone who will answer the same way next month", "The data ownership register", "Any challenge to the tile"],
            ["Measured or estimated", "Producing department", "Marked, because the tile cannot show the difference", "Corroborating records", "How much weight a reader gives it"],
        ]),
        "A tile failing any of the four is one that two readers can legitimately interpret differently. Removing it is a shorter argument than redesigning the page."),
        records("Indicator definition list &#183; the dashboard specification &#183; the tiles removed, and why.")),
    22: (sysdesign(
        "For every indicator that describes a finished period, one that describes conditions now. All four of the second kind are already being collected for another purpose.",
        table(["Indicator", "Kind", "Born where", "Predicts"], [
            ["Progress against plan", "Lagging", "Progress update", "&#8212;"],
            ["Schedule and cost indices", "Lagging", "Cost report", "&#8212;"],
            ["Constraint closure rate", "Leading", "Constraint log", "Whether next month starts"],
            ["Approval turnaround", "Leading", "Submittal log", "Engineering and procurement dates"],
            ["Ready workfronts", "Leading", "Workfront register", "Achievable look-ahead"],
        ]),
        "Add two and run them alongside the existing pack for three months rather than proposing a replacement. If they turn before the lagging ones do, the case makes itself."),
        records("KPI page with both kinds marked &#183; the leading indicator series, kept from the start.")),
    9: (sysdesign(
        "A constraint log that records only the constraint is half a log. The columns that matter are the closing ones, because an item nobody can prove was closed will be raised again next week.",
        table(["Constraint", "Test", "Owner", "Raised", "Closed by, when, evidence"], [
            ["IFC not issued", "Drawing", "Lead engineer", "date", "who &#183; date &#183; transmittal"],
            ["Material not at workface", "Material", "Store manager", "date", "who &#183; date &#183; store issue"],
            ["Crane in another zone", "Plant", "Construction", "date", "who &#183; date &#183; allocation"],
            ["Gang allocated elsewhere", "Labour", "Subcontractor", "date", "who &#183; date &#183; confirmation"],
            ["Permit not obtained", "Permit", "HSE lead", "date", "who &#183; date &#183; permit number"],
            ["Predecessor not signed off", "Access", "QA/QC", "date", "who &#183; date &#183; inspection record"],
        ]),
        "The last column is the one most logs are missing. Without it, closure happens verbally in a meeting and cannot be distinguished from an item that was never closed at all."),
        records("Workfront register &#183; constraint log &#183; ready work list.")),
    2: (sysdesign(
        "A field specification, not a spreadsheet. Four questions per field, and the discipline is that new fields go at the end of the table rather than into the middle of it.",
        table(["Field", "Produced by", "Unit", "Closes"], [
            ["Installed quantity", "Site engineer", "m&#179;, m&#178;, t, m, no.", "Daily, at cut-off"],
            ["Area or system", "Site engineer", "coded value", "With the quantity"],
            ["Activity reference", "Site engineer", "schedule ID", "With the quantity"],
            ["Hours", "Supervisor", "man-hours", "Weekly"],
            ["Material issued", "Store", "as delivered", "On issue"],
            ["Drawing revision built to", "Site engineer", "revision code", "With the quantity"],
        ]),
        "Column order is fixed once the table is in use. Anything added later goes on the right, keeps its own owner, and does not move what is already there."),
        records("Field specification &#183; the input sheet itself &#183; the list of fields a report needs and the sheet does not hold.")),
    13: (sysdesign(
        "Most distribution registers record one event. The other two are what tell you whether a single revision is actually in use.",
        table(["Event", "Recorded by", "What it proves"], [
            ["Issued", "Document control", "The transmittal left, with a date"],
            ["Acknowledged", "Recipient", "They have it &#8212; not that the email was sent"],
            ["Withdrawn", "Named person on site", "The previous copy is out of use"],
            ["In use on site", "Spot check", "What the crew is actually holding today"],
        ]),
        "The fourth row is not a system field and cannot be. It is a walk, done occasionally on a small sample, and it is the only thing that verifies the other three."),
        records("Transmittal register &#183; revision status list &#183; withdrawal record for superseded copies.")),
    25: (sysdesign(
        "One table, filled in before either document is published, and only the lines that disagree go in it.",
        table(["Item", "Progress says", "Valuation says", "Cause", "Agreed treatment"], [
            ["Line by line", "quantity", "measured quantity", "timing / measurement / error", "who decided, and when"],
        ]),
        "Cause is the column that does the work. Timing resolves next month, measurement needs a rules decision, and error is the only category that is still wrong after the meeting ends."),
        records("Month-end reconciliation sheet &#183; boundary item list &#183; the query email holding both parties.")),
    15: (sysdesign(
        "A submittal log that records only what was sent cannot tell you what to plan against. Two dates and one status field turn it into an input.",
        table(["Field", "What it gives you"], [
            ["Sent", "Start of the turnaround"],
            ["Returned", "End of it &#8212; the actual duration, not the contractual one"],
            ["Status", "Approved, approved with comments, or rejected"],
            ["Comment decision", "Who read the comments and what they concluded"],
        ]),
        "The fourth row is the one that is usually missing, and it is the one that decides whether work can start on a drawing returned with comments."),
        records("Submittal log with actual turnaround &#183; comment decision record &#183; log of informal requests.")),
    16: (sysdesign(
        "One page, not a system. Written once, it settles the assumptions three departments were each making separately.",
        table(["Product", "Collection closes", "Who submits", "Issued", "To whom"], [
            ["Daily report", "hour", "site engineers", "hour", "construction, client"],
            ["Weekly report", "day and hour", "all disciplines", "day", "project team"],
            ["Monthly report", "date", "all departments", "date", "management, client"],
            ["Finance close", "date", "commercial", "&#8212;", "&#8212;"],
            ["Measurement period", "contract dates", "quantity surveyor", "&#8212;", "&#8212;"],
        ]),
        "The last two rows are not yours and cannot be changed. Putting them on the same page as the first three is the point: the gaps become visible, and the boundary items become a list rather than an argument."),
        records("Reporting calendar &#183; boundary item list &#183; the agreed data date for each update.")),
    23: (sysdesign(
        "An action log with three columns is a wish list. These are the fields that make follow-up possible at all.",
        table(["Field", "Why"], [
            ["Action", "One thing, stated as a task rather than a topic"],
            ["Owner", "A person. Departments do not do things"],
            ["Raised", "When the clock started"],
            ["Due", "What follow-up is measured against"],
            ["Done looks like", "Settles half of all disputed closures"],
            ["Closed by, when", "The step that distinguishes closed from forgotten"],
        ]),
        "Column order fixed, new fields to the right. This log will be read by somebody a year from now who was not in the room."),
        records("Minutes &#183; action log &#183; decision log &#183; recovery action list when the project is behind.")),
    24: (sysdesign(
        "Not fifteen registers. Eight that track state, with the relationships between them written down where they can be seen.",
        table(["Register", "Fed by", "Closed by"], [
            ["Assumption", "&#8212;", "Decision, or it becomes a risk"],
            ["Risk", "Assumption that stopped holding", "Decision and action"],
            ["Interface", "&#8212;", "Decision, or it becomes a constraint"],
            ["Constraint", "Unresolved interface", "Action, with evidence"],
            ["NCR", "&#8212;", "Rework, which feeds change"],
            ["Change", "Risk, NCR, instruction", "Contractual process"],
            ["Decision", "Any of the above", "Itself"],
            ["Action", "Any of the above", "Itself, with a name and a date"],
        ]),
        "The last two columns are the ones most register templates omit, and they are the reason six of these lists grow without ever shrinking."),
        records("The eight state registers &#183; the map above &#183; the review that walks the arrows rather than the rows.")),
    14: (sysdesign(
        "The reconciliation is not about the numbers. It is about the items that crossed the boundary between two closing dates, and it takes twenty minutes if both dates are written down beforehand.",
        table(["Field", "Set by", "Why it matters"], [
            ["Finance close date", "Commercial", "When cost stops being counted"],
            ["Progress close date", "Project controls", "When work stops being counted"],
            ["Boundary list", "Both, jointly", "Deliveries, measurements and invoices landing between the two"],
            ["Treatment agreed", "Commercial", "Which month each boundary item belongs to"],
        ]),
        "Two dates and one short list. Earned value calculated across two unreconciled month-ends is wrong even when both sides are individually correct."),
        records("Cut-off calendar &#183; boundary item list &#183; monthly reconciliation note.")),
    17: (sysdesign(
        "The daily report itself needs no design. What is almost always missing is the record that it changed.",
        table(["Field", "What goes in it"], [
            ["Revision", "1, 2, 3 &#8212; not a new file with the same name"],
            ["Date issued", "When this version went out"],
            ["Changed by", "The person, not the department"],
            ["What changed", "The field and the old value"],
            ["Why", "Late measurement, correction, or new information"],
        ]),
        "Five columns, filled in under a minute, and it removes the failure entirely: nobody can end up holding a different version of the same day without knowing it."),
        records("Daily report &#183; revision log &#183; the not-yet-reported list for fields the day could not close.")),
    26: (sysdesign(
        "The first page of a report is the only page that reliably gets read. What goes on it decides whether the document changes anything.",
        table(["Column", "What it forces"], [
            ["Decision needed", "A request rather than a description"],
            ["Owner", "A person, not a department"],
            ["By when", "A date the consequence is measured against"],
            ["If not taken", "The cost of doing nothing, stated"],
        ]),
        "Four columns and rarely more than three rows. It does not make people act. It reduces the chance that something important is read as background and left alone."),
        records("Decision page &#183; action list with owners and dates &#183; the report itself, as the contemporaneous record.")),
}


# --------------------------------------------------------------------------


def build(spec):
    src = TEMPLATE.read_text(encoding="utf-8")
    out = DRAFTS / spec["file"]

    # body
    i = src.index('<h2 style="margin-top:0;">')
    j = src.index("<h3>Enjoyed this lesson?")
    # the body ends at the last </p> before the closing divs
    tail_start = src.rindex("</p>", i, j) + len("</p>")
    src = src[:i] + spec["body"] + src[tail_start:]

    # metadata
    src = re.sub(r"<title>.*?</title>", f"<title>{spec['title']} | The Project Control Hub</title>", src, 1, re.S)
    src = re.sub(r'(<meta name="description" content=")[^"]*(")', r"\g<1>" + spec["desc"] + r"\g<2>", src, 1)
    src = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r"\g<1>" + spec["desc"] + r"\g<2>", src, 1)
    src = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', r"\g<1>" + spec["desc"] + r"\g<2>", src, 1)
    src = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r"\g<1>" + spec["og"] + r"\g<2>", src, 1)
    src = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', r"\g<1>" + spec["og"] + r"\g<2>", src, 1)
    # share text must be unique per page — check_site compares all 120
    # Share text lives URL-encoded inside the three share links, and
    # check_site compares the decoded text across all pages.
    W8_SHARE = ("Ten litres of paint cannot cover twenty litres of wall. "
                "The site was not lying \u2014 it had no way to measure.")
    for enc in (quote(W8_SHARE, safe=""), quote(W8_SHARE, safe="").replace("%20", "+")):
        src = src.replace(enc, quote(spec["share"], safe=""))
    src = src.replace(W8_SHARE, spec["share"])
    src = re.sub(r'<h1 class="article-title">.*?</h1>', f'<h1 class="article-title">{spec["h1"]}</h1>', src, 1, re.S)
    src = src.replace("reporting-week-8.html", spec["file"])
    src = src.replace('data-current-week="8"', f'data-current-week="{spec["week"]}"')
    src = src.replace("Week 8 &#183; Who measures, in what unit, on which day",
                      f"Week {spec['week']} &#183; {spec['crumb']}")
    src = src.replace("MODULE 06 &#183; REPORTING &#183; WEEK 8",
                      f"MODULE 06 &#183; REPORTING &#183; WEEK {spec['week']}")
    src = re.sub(r"Reporting &#183; Week 8", f"Reporting &#183; Week {spec['week']}", src)

    for anchor, figure in FIGURES[spec["week"]]:
        if anchor not in src:
            sys.exit(f"HATA: figur capasi bulunamadi: {anchor[:50]}")
        src = src.replace(anchor, anchor + "</p>\n\n                                " + figure + "\n\n                                <p>", 1)

    # System design goes before Practical insight; the records line closes the takeaways
    d = DESIGN.get(spec["week"])
    if d:
        design, rec = d
        rows = ROWS.get(spec["week"])
        if rows:
            old = re.search(r"<table .*?</table>", design, re.S)
            if old:
                design = design.replace(old.group(0), table(COLS, [list(r) for r in rows]), 1)
        src = src.replace("<h2>Practical insight</h2>", design + "\n\n                            <h2>Practical insight</h2>", 1)
        src = src.replace("</ul>\n\n                            <h2>What is coming next</h2>",
                          "</ul>\n                            " + rec + "\n\n                            <h2>What is coming next</h2>", 1)

    # Contractions: verb negatives only, the rule Tracks 2 and 3 were aligned on.
    # "is not" and "are not" stay, which is what keeps week 8 at 6 rather than 15.
    a = src.index('<h2 style="margin-top:0;">'); b = src.index("Enjoyed this")
    body = src[a:b]
    # Contraction density is tuned per week rather than applied blindly: the
    # published tracks sit between 5 and 9 per thousand, and a body full of
    # "cannot" lands well above that while one full of "is not" lands below.
    rules = [(r"\bdoes not\b", "doesn't"), (r"\bdo not\b", "don't"),
             (r"\bwill not\b", "won't"), (r"\bdid not\b", "didn't"),
             (r"\bcould not\b", "couldn't")]
    if spec["week"] not in (2, 18, 21):
        rules.append((r"\bcannot\b", "can't"))
    if spec["week"] in (14, 7, 22, 4, 5):
        rules += [(r"\bis not\b", "isn't"), (r"\bare not\b", "aren't")]
    for pat, rep in rules:
        body = re.sub(pat, rep, body)
    src = src[:a] + body + src[b:]

    if out.exists() and out.read_text(encoding="utf-8") == src:
        print(f"  = {spec['file']}: degisiklik yok")
        return 0
    out.write_text(src, encoding="utf-8")
    print(f"  + {spec['file']}: yazildi")
    return 1


def main():
    if not TEMPLATE.exists():
        sys.exit("HATA: sablon bulunamadi: drafts/reporting-week-8.html")
    n = sum(build(w) for w in (W1, W2, W3, W4, W5, W6, W7, W9, W10, W11, W12, W13, W14, W15, W16, W17, W18, W19, W20, W21, W22, W23, W24, W25, W26))
    print(f"\n{n} dosya")


if __name__ == "__main__":
    main()
