#!/usr/bin/env python3
"""Build the Miss Affiliate swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/MISS_AFFILIATE_Swipe")

objections = sorted(g for g in glob.glob(os.path.join(PKG, "Transcript/ma_*.md"))
                    if "workshop_replay" not in g)
workshop = sorted(glob.glob(os.path.join(PKG, "Transcript/ma_workshop_replay_transcript.md")))

CONFIG = {
    "SITE": "Miss Affiliate — TikTok Shop affiliate",
    "CREATOR": "Miss Affiliate",
    "ADS_KEY": "miss_affiliate",
    "FUNNEL_IDS": ["F117"],
    "CAPTURED": "21 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/MISS_AFFILIATE_Swipe",
    "BLURB": "A nurse-to-$157k/month TikTok Shop offer sold to women. She went dark on Meta at "
             "the end of July and relaunched on 20 Aug with 18 ads into a brand-new "
             "/signup slug. Two funnels run behind two different pixels, and the full "
             "1h42m class now sits ungated on /replay.",

    "PAGES": [
        ("index.html", "Overview"),
        ("slides.html", "Masterclass slides"),
        ("analysis.html", "Objection teardown"),
        ("transcripts.html", "Objection library"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Live Meta ads", "18"),
        ("Distinct creatives", "7"),
        ("All launched", "20 Aug 2026"),
        ("Replay runtime", "1h 42m 57s"),
        ("Application floor", "$2,000"),
        ("Objection videos", "21"),
        ("Library runtime", "25m 16s"),
        ("Capture quality", "4K"),
        ("Upsell", "$27 VIP"),
        ("Downsell", "Replay access"),
        ("Live cap", "250 spots"),
        ("Claim", "$157k/mo"),
        ("Cadence", "Wed 8pm ET"),
    ],

    "OFFER": [
        ("Product", "Miss Affiliate — TikTok Shop affiliate coaching"),
        ("Lead claim", "&ldquo;From working 12-hour nursing shifts burnt out to making "
                       "157k/month with TikTok Shop affiliate&rdquo;"),
        ("Qualifier", "Without a big following, prior experience, or sacrificing freedom"),
        ("Event", "Live training, Sundays 3:00 PM ET, capped at &ldquo;250 total live spots&rdquo;"),
        ("Post-optin", "$27 VIP upsell, then a second downsell for replay access"),
        ("Confirmation", "<b>SMS only</b> &mdash; texts from +1 757-580-9956, no email at all"),
        ("VIP contents", "30-day roadmap, product selection guide + 13 niches, top 20 hooks, "
                         "1-to-1 coach call"),
        ("VIP scarcity", "&ldquo;Limited to 50 women total&rdquo;"),
        ("Price", '<span class="tag warn">not yet observed</span> — behind the Sunday training'),
    ],

    "FINDINGS": [
        ("She relaunched Meta on 20 Aug &mdash; 18 ads, all in one day",
         "The 31 July read that she buys <b>zero</b> Meta traffic was true when taken and is now "
         "<b>wrong</b>. On 20 Aug she pushed <b>18 live ads / 7 distinct creatives</b> from page "
         "<code>1021090297763539</code>, every one pointing at a slug we had never seen: "
         "<code>/signup</code>. They were 10 hours old at capture and 5 of 13 cards were flagged "
         "under 100 impressions &mdash; a relaunch in testing, not a scaled account. The media is "
         "<b>84 days old</b>, so she is re-running May creative rather than shooting new. "
         "<b>gethookd still returned 0 for her a full day after the relaunch</b> &mdash; the "
         "third-party index lags Meta's own library, so a gethookd zero is unproven, not absence."),
        ("6 of the 7 live creatives sell the wrong class",
         "Six of the seven running videos say <b>&ldquo;this Sunday at 3pm Eastern&rdquo;</b>. All "
         "18 ads land on <code>/signup</code>, whose own title is <b>&ldquo;Countdown &mdash; Next "
         "Wed 8pm ET&rdquo;</b>. Only one creative says Wednesday. She is paying to promise a day "
         "her landing page contradicts on arrival."),
        ("Two pixels, two operators",
         "<code>/signup</code>, <code>/almostdone</code> and <code>/replay</code> carry pixel "
         "<code>2548125322312559</code> plus a Cortana hub, and a St. Petersburg, FL footer. "
         "<code>/start</code> and <code>/application</code> carry <code>903499129224608</code>, "
         "no Cortana, and a <b>Los Angeles, CA</b> footer. A domain-wide Ad Library query returns "
         "no ads at all pointing at the second funnel, so whatever feeds it is not Meta."),
        ("The $13 replay is now free to anyone with the URL",
         "She sells replay access for $13 inside the confirmation ladder, then serves the "
         "<b>entire 1h 42m class</b> unauthenticated on <code>/replay</code>, with a 1-hour "
         "&ldquo;Miss Affiliate 1-1 Call&rdquo; booking calendar directly beneath it."),
        ("The application carries a hard $2,000 budget floor",
         "Typeform <code>JAYokipv</code>, 10 questions. Q6 writes the DQ into the answer itself: "
         "<b>&ldquo;I have less than $2,000 (this is not the right fit for me at this time)&rdquo;</b>, "
         "against bands of $2,000&ndash;$5,000 and +$5,000. Two separate questions make her commit "
         "to showing up, on a computer, for 45&ndash;60 minutes."),
        ("She runs follow-up on SMS, not email",
         "Signed up twice on two different addresses and <b>no confirmation email ever arrived</b>. "
         "Her confirmation page says instead: <i>&ldquo;We just texted from +1 757-580-9956, reply "
         "YES to confirm.&rdquo;</i> Her whole follow-up runs by text. "
         "<b>This is the closest competitor comparison we have to AI-LNS.</b>"),
        ("Her join link is hidden in the calendar button",
         "The confirmation page never prints the join URL. It is buried inside the "
         "&ldquo;Add to Google Calendar&rdquo; link as an encoded parameter: "
         "<code>event.webinarjam.com/6mn333/go/live/0qgxxxa87i1s7s2</code>. Worth knowing because "
         "any capture that scrapes the visible page and stops there gets nothing."),
        ("21 objections, answered on camera, before the call",
         "Each video is titled with the objection it kills: do I need followers, what if I can't "
         "get approved, what's the risk, will this work if I have a job. She is answering the "
         "sales conversation before it happens, at 4K, on the page every registrant lands on."),
        ("Risk is reframed as inaction",
         "&ldquo;The real risk is not the program. The real risk is hesitating while one of the "
         "biggest opportunities in social media history is happening in front of us.&rdquo; She "
         "never defends the price — she moves the risk onto standing still."),
        ("She refuses to promise income",
         "The 90-day video says outright &ldquo;how much money will you make in 90 days? It's "
         "impossible to tell&rdquo; and substitutes three process wins: confidence, first "
         "commissions, and a durable skill. Legally clean and more believable than a number."),
        ("The honesty pledge is a verbal tic with a job",
         "Nearly every answer opens with &ldquo;I want to be so honest with you&rdquo; or "
         "&ldquo;I always want to be honest with you.&rdquo; It buys permission to then deliver "
         "a partially inconvenient answer, which makes the convenient part land harder."),
        ("Concede the hard fact, then reveal the workaround",
         "On followers she concedes TikTok's real 5,000-follower rule, then reveals a &ldquo;cheat "
         "code&rdquo; for pre-approved accounts. The concession is what makes the reveal credible."),
        ("Two-step upsell ladder",
         "Opt-in, then $27 VIP, then a separate downsell for replay access, then confirmation. "
         "She monetises the decline, not just the acceptance."),
    ],

    "FUNNEL": [
        ("Meta ads", "facebook.com/ads/library/?q=themissaffiliate.com",
         "<b>18 live ads, 7 creatives, all launched 20 Aug 2026.</b> Advertiser page "
         "<code>1021090297763539</code>. UGC-style selfie video, 26s&ndash;86s."),
        ("Opt-in (funnel A)", "themissaffiliate.com/signup",
         "New slug as of the relaunch. <b>Wed 8pm ET</b>. Phone and email required, name optional. "
         "Pixel <code>2548125322312559</code> + Cortana."),
        ("VIP upsell", "themissaffiliate.com/almostdone",
         "$27. &ldquo;Wait! Your Spot Isn't Fully Confirmed Yet…&rdquo; Limited to 50 women."),
        ("Replay downsell", "themissaffiliate.com/almostdone-416757-272179",
         "Declining the VIP offers replay access as a separate paid step, $47 struck to $13."),
        ("Replay + booking", "themissaffiliate.com/replay",
         "The <b>full 1h 42m 57s class</b> on Vidalytics, ungated, with a 1-hour discovery-call "
         "calendar underneath."),
        ("Pre-webinar page", "themissaffiliate.com/prewebinarpage-9774",
         "<b>The 21-video objection library</b> plus a 2m48s Vidalytics VSL."),
        ("VSL (funnel B)", "themissaffiliate.com/start",
         "Separate pixel <code>903499129224608</code>, no Cortana, Los Angeles footer. "
         "<b>No Meta ads point here.</b>"),
        ("Application (funnel B)", "themissaffiliate.com/application",
         "Typeform <code>JAYokipv</code>, 10 questions, hard <b>$2,000</b> budget floor."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The masterclass — full 1h 42m replay, 22,442 words", workshop),
        ("Objection library — 21 videos", objections),
    ],

    "SLIDE_PAGES": [
        ("The masterclass, slide by slide", "slides.html", "Screenshots", "wb_",
         "Every materially different frame from the full 1h 42m 57s workshop replay, "
         "pulled off the ungated <code>/replay</code> page on 21 Aug 2026."),
    ],

    "DECKS": [
        ("Miss Affiliate — TikTok Shop Masterclass (21 Aug 2026)", 281,
         "https://docs.google.com/presentation/d/1g3xqgfH4TX2-AP2RaXo9Xe3qpnfU5eHvzdxdZUa-mZA/edit"),
    ],

    "VIDEOS": [
        ("ma_workshop_replay_20260821.mp4", 6177, "770 MB",
         "<b>The full masterclass.</b> 1080p off the ungated /replay page, Vidalytics HLS. "
         "Duration matches the player's own reported 6177.04s."),
        ("7 &times; Meta ad creatives", 337, "20 MB",
         "Every distinct video running in the 20 Aug relaunch."),
        ("21 &times; Wistia objection videos", 1516, "1.5 GB",
         "The pre-webinar objection library. 4K source."),
        ("ma_vsl_vidalytics.mp4", 168, "24 MB",
         "Short pre-webinar VSL on the same page."),
    ],

    "ANALYSIS": """
<div class="note"><b>Why this one matters to us.</b> Her objection list maps almost one-to-one
onto the objections our setters hit in DMs. She has answered every one of them on camera and put
them where the prospect will actually watch them. We answer ours live, one prospect at a time,
in text.</div>

<h2 class="sec">Her objection map</h2>
<div class="tablewrap"><table>
<tr><th>Objection</th><th>Her move</th><th>Our nearest equivalent</th></tr>
<tr><td>Do I need followers?</td><td>Concedes the real 5,000 rule, then reveals pre-approved accounts</td><td>&ldquo;I have zero followers&rdquo;</td></tr>
<tr><td>Complete beginner?</td><td>Beginner reframed as an advantage on a young platform</td><td>&ldquo;I've never done UGC&rdquo;</td></tr>
<tr><td>What if I can't get approved?</td><td>Process answer with a fallback path</td><td>&ldquo;What if no brand picks me&rdquo;</td></tr>
<tr><td>What's the risk?</td><td>Risk relocated onto hesitating</td><td>&ldquo;What if it doesn't work for me&rdquo;</td></tr>
<tr><td>Realistic 90 days?</td><td>Refuses a number, promises three process wins</td><td>&ldquo;How fast will I make money&rdquo;</td></tr>
<tr><td>I have a job already</td><td>Time-boxed around shifts</td><td>&ldquo;I work full time&rdquo;</td></tr>
<tr><td>Show my face?</td><td>Faceless path exists</td><td>&ldquo;I'm shy on camera&rdquo;</td></tr>
<tr><td>Algorithm changes / banned</td><td>Longest answer in the set at 2m10s — platform-risk defence</td><td>&ldquo;What if the industry dies&rdquo;</td></tr>
<tr><td>Is it free?</td><td>Separates platform cost from program cost</td><td>&ldquo;Are there hidden costs&rdquo;</td></tr>
</table></div>

<h2 class="sec">The three patterns worth copying</h2>
<div class="grid g2">
<div class="card"><h3>Concede first, then reveal</h3><p>She never dodges the inconvenient fact.
She states it plainly, which earns the right to the workaround that follows. Our DM replies tend
to skip straight to the reassurance, which reads as dodging.</p></div>
<div class="card"><h3>Process promises, not income promises</h3><p>&ldquo;Impossible to tell&rdquo;
on money; specific and confident on confidence, first commission, and skill. Safer under scrutiny
and more credible to a sceptical buyer.</p></div>
<div class="card"><h3>Answer before you are asked</h3><p>Twenty-five minutes of objection handling
sitting on the page between opt-in and event. Every one of those is a conversation her closers
never have to have.</p></div>
<div class="card"><h3>Monetise the decline</h3><p>Declining the $27 VIP triggers a separate
replay-access offer rather than dropping straight to the confirmation page.</p></div>
</div>

<h2 class="sec">Flag</h2>
<p>The &ldquo;pre-approved accounts&rdquo; mechanic — buying or transferring TikTok accounts that
already clear the 5,000-follower threshold — sits against TikTok's own terms. Her script says
&ldquo;ethically and safely&rdquo; without saying how. Study the persuasion structure; do not
copy the mechanic.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
