#!/usr/bin/env python3
"""Build the Miss Affiliate swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/MISS_AFFILIATE_Swipe")

objections = sorted(glob.glob(os.path.join(PKG, "Transcript/ma_*.md")))

CONFIG = {
    "SITE": "Miss Affiliate — TikTok Shop affiliate",
    "CREATOR": "Miss Affiliate",
    "ADS_KEY": "miss_affiliate",
    "FUNNEL_IDS": ["F117"],
    "CAPTURED": "31 July 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/MISS_AFFILIATE_Swipe",
    "BLURB": "A nurse-to-$157k/month TikTok Shop offer sold to women off a weekly Sunday "
             "training. The asset worth studying is not the webinar — it is the "
             "21-video objection library sitting on the pre-webinar page.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Objection teardown"),
        ("transcripts.html", "Objection library"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Objection videos", "21"),
        ("Library runtime", "25m 16s"),
        ("Capture quality", "4K"),
        ("Upsell", "$27 VIP"),
        ("Downsell", "Replay access"),
        ("Live cap", "250 spots"),
        ("Claim", "$157k/mo"),
        ("Cadence", "Sundays 3pm ET"),
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
        ("She runs on SMS, not email &mdash; the only one of the seven",
         "Signed up twice on two different addresses and <b>no confirmation email ever arrived</b>. "
         "Her confirmation page says instead: <i>&ldquo;We just texted from +1 757-580-9956, reply "
         "YES to confirm.&rdquo;</i> Her whole follow-up runs by text. That lines up with her being "
         "the only competitor here buying <b>zero</b> Meta ads &mdash; she is TikTok-native and "
         "phone-first end to end. <b>This is the closest competitor comparison we have to AI-LNS.</b>"),
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
        ("Opt-in", "themissaffiliate.com/signup-sunday",
         "Full name optional; <b>phone and email required</b>. Countdown to the next Sunday."),
        ("VIP upsell", "themissaffiliate.com/almostdone-sunday",
         "$27. &ldquo;Wait! Your Spot Isn't Fully Confirmed Yet…&rdquo;"),
        ("Replay downsell", "themissaffiliate.com/almostdone-416757-272179",
         "Declining the VIP offers replay access as a separate paid step."),
        ("Pre-webinar page", "themissaffiliate.com/prewebinarpage-9774",
         "<b>The 21-video objection library</b> plus a 2m48s Vidalytics VSL."),
        ("Live training", "Sundays 3:00 PM ET", "Not yet captured — next session Sunday."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("Objection library — 21 videos", objections),
    ],

    "SLIDE_PAGES": [],

    "VIDEOS": [
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
