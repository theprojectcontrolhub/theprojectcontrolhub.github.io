#!/usr/bin/env python3
"""Builds reporting-week-8.html from cost-week-11.html as template.

First article of Track 6. Week 8 rather than week 1 because the material
exists for it: the paint, the weighbridge and the timesheet allocation are
the three cases that make the whole track's argument, and the argument is
that site data is not dishonest, it is unmeasured.

No figures are invented. The three SVGs are structural — where a number is
born, what can corroborate it, and why the deadline decides the quality —
because the events behind this article happened on jobs that are not the
$1M case study and putting their quantities on the page would create numbers
nobody can reproduce (NOTES.md section 1, and the Track 4 audit).

File naming follows the site: reporting-week-8.html, not week-08. Every one
of the 117 published pages is unpadded and check_site.py reads week-(\\d+).

Idempotent.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "cost-week-11.html"
TARGET = ROOT / "reporting-week-8.html"

TITLE_H1 = "The site is not lying to you."
SHORT = "Construction: progress"
CRUMB = "Who measures, in what unit, on which day"
DATE = "Sep 20, 2028"
SHARE = "Ten litres of paint cannot cover twenty litres of wall. The site was not lying — it had no way to measure."

BODY = '''<h2 style="margin-top:0;">The site is not lying to you</h2>
                            <p>A painting gang reports the area it finished yesterday. The number goes into the daily report, into the weekly progress, into the monthly curve. Nobody checks it, because why would you.</p>
                            <p>Then somebody compares it against the paint that came out of the store.</p>
                            <p>The area reported would need roughly twice the paint that was issued. Not a rounding difference &#8212; twice. And the foreman who reported it is not a liar, has no reason to lie, and would be genuinely offended if you suggested it.</p>

                            <!-- LOCKED CONTENT -->
                            <div class="content-locked">
                                <p>He estimated. He stood at the end of a floor, looked down it, and said about two thirds. There is no other way for him to answer the question in the time he has. Nobody is going to tape-measure a painted wall at the end of a shift.</p>
                                <p>That is the whole subject of this week. The rawest input in project controls is not falsified. It is <em>unmeasured</em> &#8212; and unmeasured numbers drift in one direction.</p>

                                FIG1

                                <h2>Three ways the same thing happens</h2>
                                <p>Paint is the clearest case because the corroboration is so simple. Material out of the store against area claimed. The two should agree within a sensible loss allowance, and when they don't, one of them is a guess.</p>
                                <p>Earthworks is the same problem wearing a different coat. Volumes get reported by counting trucks. Twenty loads, so many cubic metres a load, done. But a load is not a fixed quantity, the trucks are not always full, and the conversion factor came from somebody's memory. The weighbridge tickets exist and they say something else.</p>
                                <p>Manhours are the version nobody sees, because the total is always right. HR has the attendance. What HR does not have is where the man stood. Timesheet allocation puts eight hours against an activity because that is what the foreman ticked, and a man who spent half his day helping another gang has just moved four hours of cost onto the wrong work. The total is correct. Every productivity figure built from it is not.</p>
                                <p>Three trades, three mechanisms, one shape. Somebody has to produce a number for work that is too spread out, too fast, or too mixed to measure by the time the report closes.</p>

                                <h2>Why the drift only goes one way</h2>
                                <p>Estimates under pressure are not random. They are optimistic, and consistently so.</p>
                                <p>Part of that is human &#8212; a man reporting his own gang's output is not a neutral observer. But most of it is structural. Nobody is punished for reporting eighty and delivering seventy-five. Everybody is asked why the number went backwards. So the estimate leans forward, week after week, and the gap between what the report says and what is on the wall grows quietly until something forces a reconciliation.</p>
                                <p>That something is usually the month end. Or worse, the handover, when the last ten percent turns out to be thirty.</p>

                                FIG2

                                <h2>The five records that can contradict a claim</h2>
                                <p>You cannot re-measure the site. What you can do is find the records that were created for another purpose and ask whether they agree.</p>
                                <p><strong>Delivery notes and weighbridge tickets.</strong> Material arrived, and someone signed for it. This is the strongest corroboration you have because it was produced by a third party with no interest in your progress figure.</p>
                                <p><strong>Store issues.</strong> Material left the warehouse and went somewhere. Paint, cable, welding consumables, formwork &#8212; consumption is a proxy for installed quantity, and a good one.</p>
                                <p><strong>Quantity survey measurements.</strong> Somebody measured for payment. It will be behind the site's claim and it will be more careful, because money depends on it.</p>
                                <p><strong>Attendance records.</strong> How many people were actually on site, which caps how much work can plausibly have been done.</p>
                                <p><strong>Inspection and test records.</strong> Work that has been signed off as complete by someone who had to look at it.</p>
                                <p>None of these measures progress. Every one of them constrains it. That is the difference, and it is the reason this list is worth more than a better reporting form.</p>

                                <h2>What the planner is actually for</h2>
                                <p>Here is the shift, and it is the argument this entire track is built on.</p>
                                <p>If you treat the site as your data source, your job is collection: chase the numbers, format them, publish. If you treat the site as <em>one</em> source among several that do not agree, your job changes completely. It becomes reconciliation &#8212; finding the number closest to the truth among records that contradict each other.</p>
                                <p>The second job is harder, slower, and the only one worth having. A planner who only collects is a formatting service. A planner who reconciles is the reason the monthly report can be defended in a room.</p>
                                <p>One rule makes it work: <strong>the planner does not correct the number alone.</strong> When the store says one thing and the site says another, that goes back to the engineer who reported it and to the department that holds the contradicting record, in the same email, and it stays open until they agree. Not because of politics. Because a figure the site did not agree to is a figure the site will not defend when it matters.</p>

                                FIG3

                                <h2>The deadline decides the quality</h2>
                                <p>One thing sets how much of your data is measured and how much is estimated, and it is not the form. It is the hour the report is due.</p>
                                <p>Ask for yesterday's report by seven the next morning and you have asked the site to report work that finished after they went home. They will estimate, because the alternative is a blank. Ask for it by the afternoon and the same foreman can walk the floor, check with the surveyor, and give you something he counted.</p>
                                <p>Both projects have a daily report. They do not have the same data in it.</p>

                                <h2>Practical insight</h2>
                                <p>Take last month's progress and pick the three activities with the largest reported quantities. For each, ask one question: <em>what record, produced by somebody outside the reporting chain, would agree with this?</em></p>
                                <p>Sometimes the answer arrives immediately &#8212; a weighbridge ticket, a delivery note, a signed inspection. That activity is measured, and you can defend it.</p>
                                <p>Sometimes there is no such record at all. That activity is an opinion with a percentage sign on it, and you have just found where your curve will correct.</p>
                                <p>Then do it once more, deliberately, on the activity closest to the critical path. That is the one where an optimistic estimate does the most damage, and it is almost always the one nobody has corroborated.</p>

                                <h2>Key takeaways</h2>
                                <p>&#10004; Site data is rarely falsified. It is unmeasured &#8212; estimated because the area is too large or the deadline too early to count.<br>
                                &#10004; Unmeasured numbers drift one way. Nobody is questioned for over-reporting; everybody is questioned when progress goes backwards.<br>
                                &#10004; Paint against store issues, volumes against weighbridge tickets, hours against where the man actually stood &#8212; three trades, one mechanism.<br>
                                &#10004; Manhour totals can be right while every productivity figure built on them is wrong, because allocation is what breaks.<br>
                                &#10004; Five records can contradict a claim: deliveries, store issues, QS measurement, attendance, inspection sign-off.<br>
                                &#10004; None of them measures progress. Each of them constrains it, and constraint is enough.<br>
                                &#10004; The planner reconciles rather than collects &#8212; and never corrects a number alone. It goes back to the reporter and the record holder together.<br>
                                &#10004; The report deadline decides how much of your data was counted and how much was guessed.</p>

                                <h2>What is coming next</h2>
                                <p>This week was about a number that already exists, and whether you can believe it.</p>
                                <p>Next comes the number that does not exist yet: the work the site says it is ready to start. Ready means six different things to six different people, and the gap between them is where a look-ahead stops being a plan and becomes a wish.</p>
                                <p>Next week: workfront and the six readiness tests &#8212; drawing, material, access, permit, labour, plant.</p>
                            </div>'''

FIG1 = '''<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
                                    <svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
  <text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" font-weight="700" letter-spacing="2">WHERE A REPORTED QUANTITY COMES FROM</text>

  <rect x="30" y="58" width="170" height="66" rx="10" fill="#fff" stroke="#cbd5e1"/>
  <text x="115" y="84" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">Measured</text>
  <text x="115" y="104" text-anchor="middle" fill="#64748b" font-size="11">Counted, weighed, surveyed</text>

  <rect x="235" y="58" width="170" height="66" rx="10" fill="#fff" stroke="#cbd5e1"/>
  <text x="320" y="84" text-anchor="middle" fill="#334155" font-size="13" font-weight="700">Derived</text>
  <text x="320" y="104" text-anchor="middle" fill="#64748b" font-size="11">Trucks &#215; a factor</text>

  <rect x="440" y="58" width="170" height="66" rx="10" fill="#fef2f2" stroke="#fca5a5"/>
  <text x="525" y="84" text-anchor="middle" fill="#b91c1c" font-size="13" font-weight="700">Estimated</text>
  <text x="525" y="104" text-anchor="middle" fill="#dc2626" font-size="11">&#8220;About two thirds&#8221;</text>

  <text x="115" y="152" text-anchor="middle" fill="#059669" font-size="11" font-weight="600">defensible</text>
  <text x="320" y="152" text-anchor="middle" fill="#64748b" font-size="11" font-weight="600">only as good as the factor</text>
  <text x="525" y="152" text-anchor="middle" fill="#b91c1c" font-size="11" font-weight="600">drifts optimistic</text>

  <line x1="30" y1="178" x2="610" y2="178" stroke="#e2e8f0" stroke-width="1"/>

  <text x="30" y="206" fill="#334155" font-size="12" font-weight="700">The report does not say which one it is.</text>
  <text x="30" y="230" fill="#64748b" font-size="11.5">Every field on a progress sheet looks identical once it has been typed. A quantity that was</text>
  <text x="30" y="248" fill="#64748b" font-size="11.5">weighed and a quantity that was glanced at arrive in the same column, in the same font,</text>
  <text x="30" y="266" fill="#64748b" font-size="11.5">and go into the same curve.</text>
                                    </svg>
                                    <figcaption style="text-align:center;font-size:13px;color:#64748b;margin-top:16px;line-height:1.5;"><strong style="color:#334155;">Figure 1 &#8212; Three origins, one column.</strong> The distinction that matters most is invisible on the form. Until you ask how a number was produced, you cannot tell whether you are reading a measurement or an opinion.</figcaption>
                                </figure>'''

FIG2 = '''<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
                                    <svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
  <text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" font-weight="700" letter-spacing="2">WHY THE ERROR IS NOT RANDOM</text>

  <line x1="70" y1="230" x2="600" y2="230" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="70" y1="70" x2="70" y2="230" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="70" y="252" text-anchor="middle" fill="#94a3b8" font-size="10.5">start</text>
  <text x="600" y="252" text-anchor="middle" fill="#94a3b8" font-size="10.5">handover</text>
  <text x="52" y="76" text-anchor="end" fill="#94a3b8" font-size="10.5">100%</text>

  <path d="M70 230 C 200 150, 330 100, 600 74" fill="none" stroke="#f87171" stroke-width="2.5"/>
  <path d="M70 230 C 240 200, 380 150, 600 74" fill="none" stroke="#10b981" stroke-width="2.5"/>

  <text x="330" y="112" fill="#dc2626" font-size="11.5" font-weight="700">reported</text>
  <text x="360" y="192" fill="#059669" font-size="11.5" font-weight="700">actual</text>

  <line x1="430" y1="120" x2="430" y2="171" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="440" y="150" fill="#64748b" font-size="11">the gap nobody is measuring</text>

  <text x="70" y="286" fill="#64748b" font-size="11.5">Over-reporting is never questioned. Progress going backwards always is. So the estimate leans forward every week.</text>
                                    </svg>
                                    <figcaption style="text-align:center;font-size:13px;color:#64748b;margin-top:16px;line-height:1.5;"><strong style="color:#334155;">Figure 2 &#8212; The drift has a direction.</strong> An unmeasured number is not wrong by a random amount in a random direction. The incentives on site push it one way, consistently, and the two curves only meet when something forces them to.</figcaption>
                                </figure>'''

FIG3 = '''<figure style="margin:36px 0;padding:24px;background:#f8fafc;border-radius:16px;border:1px solid #e2e8f0;">
                                    <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
  <text x="320" y="26" text-anchor="middle" fill="#10b981" font-size="11.5" font-weight="700" letter-spacing="2">FIVE RECORDS THAT CAN CONTRADICT A CLAIM</text>

  <rect x="220" y="52" width="200" height="46" rx="10" fill="#ecfdf5" stroke="#a7f3d0"/>
  <text x="320" y="80" text-anchor="middle" fill="#047857" font-size="13" font-weight="700">Reported quantity</text>

  <g stroke="#cbd5e1" stroke-width="1.5" fill="none">
    <path d="M320 98 L320 130"/>
    <path d="M110 158 L110 140 L530 140 L530 158"/>
    <path d="M215 158 L215 140"/>
    <path d="M320 158 L320 140"/>
    <path d="M425 158 L425 140"/>
  </g>

  <rect x="46" y="158" width="128" height="80" rx="9" fill="#fff" stroke="#cbd5e1"/>
  <text x="110" y="182" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="700">Deliveries</text>
  <text x="110" y="202" text-anchor="middle" fill="#64748b" font-size="10.5">weighbridge,</text>
  <text x="110" y="217" text-anchor="middle" fill="#64748b" font-size="10.5">delivery notes</text>

  <rect x="151" y="158" width="128" height="80" rx="9" fill="#fff" stroke="#cbd5e1" opacity="0"/>
  <rect x="158" y="158" width="114" height="80" rx="9" fill="#fff" stroke="#cbd5e1"/>
  <text x="215" y="182" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="700">Store</text>
  <text x="215" y="202" text-anchor="middle" fill="#64748b" font-size="10.5">what was</text>
  <text x="215" y="217" text-anchor="middle" fill="#64748b" font-size="10.5">issued out</text>

  <rect x="263" y="158" width="114" height="80" rx="9" fill="#fff" stroke="#cbd5e1"/>
  <text x="320" y="182" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="700">QS</text>
  <text x="320" y="202" text-anchor="middle" fill="#64748b" font-size="10.5">measured</text>
  <text x="320" y="217" text-anchor="middle" fill="#64748b" font-size="10.5">for payment</text>

  <rect x="368" y="158" width="114" height="80" rx="9" fill="#fff" stroke="#cbd5e1"/>
  <text x="425" y="182" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="700">Attendance</text>
  <text x="425" y="202" text-anchor="middle" fill="#64748b" font-size="10.5">who was</text>
  <text x="425" y="217" text-anchor="middle" fill="#64748b" font-size="10.5">on site</text>

  <rect x="473" y="158" width="114" height="80" rx="9" fill="#fff" stroke="#cbd5e1"/>
  <text x="530" y="182" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="700">Inspection</text>
  <text x="530" y="202" text-anchor="middle" fill="#64748b" font-size="10.5">signed off</text>
  <text x="530" y="217" text-anchor="middle" fill="#64748b" font-size="10.5">as complete</text>

  <text x="320" y="272" text-anchor="middle" fill="#334155" font-size="12" font-weight="700">Not one of them measures progress.</text>
  <text x="320" y="294" text-anchor="middle" fill="#64748b" font-size="11.5">Each was produced for another purpose, by someone with no interest in your curve. That is what makes them useful.</text>
                                    </svg>
                                    <figcaption style="text-align:center;font-size:13px;color:#64748b;margin-top:16px;line-height:1.5;"><strong style="color:#334155;">Figure 3 &#8212; Corroboration, not measurement.</strong> You will never re-measure the site. You can ask five records that already exist whether the claim is possible, and a claim that survives all five is one you can defend.</figcaption>
                                </figure>'''

TAGS = ["#ProgressReporting", "#SiteData", "#Reconciliation", "#ProjectControls"]


def main():
    if TARGET.exists():
        print("  = reporting-week-8.html: zaten var\n\n0 dosya")
        return
    if not TEMPLATE.exists():
        sys.exit("HATA: sablon bulunamadi")

    s = TEMPLATE.read_text(encoding="utf-8")

    body = BODY.replace("FIG1", FIG1).replace("FIG2", FIG2).replace("FIG3", FIG3)

    # ---- body ----------------------------------------------------------
    i = s.index('<h2 style="margin-top:0;">Every number in this track rests on one word</h2>')
    j = s.index("                            </div>\n                        </div>\n\n                        <!-- PAYWALL CTA -->")
    s = s[:i] + body + "\n" + s[j:]

    # ---- head and meta -------------------------------------------------
    s = re.sub(r"<title>.*?</title>",
               "<title>Construction progress data — why site numbers are estimates | The Project Control Hub</title>", s, count=1, flags=re.S)
    s = re.sub(r'(<meta name="description" content=")[^"]*(">)',
               r"\g<1>Site progress data is rarely falsified — it is unmeasured. How estimates drift, and the five records that can contradict a claim.\g<2>", s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', r"\g<1>The site is not lying to you\g<2>", s, count=1)
    s = re.sub(r'(<meta name="twitter:title" content=")[^"]*(">)', r"\g<1>The site is not lying to you\g<2>", s, count=1)
    s = re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*(">)',
               r"\g<1>Ten litres of paint cannot cover twenty litres of wall. The site was not lying — it had no way to measure.\g<2>", s)
    s = s.replace("cost-week-11.html", "reporting-week-8.html")
    s = s.replace("cost-week-12.html", "reporting-week-9.html")

    # ---- visible chrome ------------------------------------------------
    s = s.replace('<a href="learn.html">Cost &amp; Cash</a>', '<a href="learn.html">Reporting</a>', 1)
    s = s.replace("<span>Week 11<span class=\"crumb-title\"> &#183; Physical progress &#8212; the six methods</span></span>",
                  f"<span>Week 8<span class=\"crumb-title\"> &#183; {CRUMB}</span></span>", 1)
    s = s.replace("MODULE 02 · COST &amp; CASH · WEEK 11", "MODULE 06 · REPORTING · WEEK 8", 1)
    s = s.replace("Every number in this track rests on one word.", TITLE_H1)
    s = s.replace("Mar 10, 2027", DATE)
    s = s.replace("Cost &amp; Cash &#183; Week 12", "Reporting &#183; Week 9", 1)

    # share text
    old_share = "Progress%20is%20measured%2C%20counted%20or%20weighed.%20Estimated%2C%20it%20is%20a%20hope%20with%20a%20percentage%20sign."
    from urllib.parse import quote
    s = s.replace(old_share, quote(SHARE, safe=""))

    # sidebar
    s = s.replace('data-current-week="11" data-track="2"', 'data-current-week="8" data-track="6"', 1)
    s = s.replace("renderTrack2Sidebar", "renderTrack6Sidebar")

    # tags
    old_tags = re.search(r'<div class="article-tags">.*?</div>', s, re.S).group(0)
    new_tags = '<div class="article-tags">\n' + "\n".join(
        f'                                <span class="article-tag">{t}</span>' for t in TAGS) + "\n                            </div>"
    s = s.replace(old_tags, new_tags, 1)

    TARGET.write_text(s, encoding="utf-8")
    print("  + reporting-week-8.html yazildi\n\n1 dosya")


if __name__ == "__main__":
    main()
