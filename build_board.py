#!/usr/bin/env python3
"""Miss Affiliate — the whole business, wired.

Rebuilt 21 Aug 2026: the paid-entry lane is real now. She relaunched Meta on
20 Aug after ~3 weeks dark, and there are two separate funnels behind two
separate pixels.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P7 = f"{S}/Miss_Affiliate - Signup_Sunday - 2026-07-31/02_Pages"
P8 = f"{S}/Miss_Affiliate - Signup_Sunday - 2026-08-18/02_Pages"
NEW = f"{REPO}/media/shots_20260821"
ADS = f"{REPO}/media/ads_20260821"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · paid entry captured 21 August 2026",
    "TITLE": "Miss Affiliate — the whole business, wired",
    "BLURB": "Nurse to $157k/month, sold to women. She went dark on Meta at the end of July and "
             "<b>relaunched on 20 Aug with 18 ads</b> — all pointing at a brand-new "
             "<code>/signup</code> slug we had never seen. Two funnels run behind "
             "<b>two different pixels</b>: a live-class ladder with two paid steps before the "
             "seat is even confirmed, and a separate VSL&nbsp;&rarr;&nbsp;application lane "
             "with a hard $2,000 budget floor.",

    "SHOTS": {
        "ads": {
            "col": 1, "y": 120, "lane": "paid", "step": "Paid entry",
            "title": "7 creatives, 18 live ads",
            "url": "facebook.com/ads/library/?q=themissaffiliate.com&search_type=keyword_unordered&country=US&active_status=active",
            "img": f"{ADS}/_creative_sheet.png",
            "max_h": 700,
            "note": "All 18 launched <b>20 Aug 2026</b>, all UGC-style selfie video, all to "
                    "<code>/signup</code>. The media itself is <b>84 days old</b> — she is "
                    "re-running May creative, not shooting new.",
        },
        "optin": {
            "col": 2, "y": 120, "lane": "event", "step": "Entry — funnel A",
            "title": "The /signup opt-in — Wed 8pm ET",
            "url": "themissaffiliate.com/signup",
            "img": f"{NEW}/signup.png",
            "max_h": 1000,
            "note": "&ldquo;From 12-hour nursing shifts burnt out to $157k/month.&rdquo; "
                    "Phone and email <b>required</b>, name optional. "
                    "&ldquo;Limited to 250 total live spots.&rdquo; "
                    "Pixel <code>2548125322312559</code> + Cortana.",
        },
        "vip": {
            "col": 3, "y": 120, "lane": "back", "step": "Upsell 1",
            "title": "$27 VIP — &ldquo;spot isn't fully confirmed yet&rdquo;",
            "url": "themissaffiliate.com/almostdone",
            "img": f"{NEW}/almostdone.png",
            "max_h": 1000,
            "note": "30-day roadmap, product guide + 13 niches, top 20 hooks, and a 1-to-1 "
                    "coach call. &ldquo;Limited to 50 women total.&rdquo;",
        },
        "down": {
            "col": 4, "y": 120, "lane": "back", "step": "Upsell 2",
            "title": "$47 &rarr; $13 replay-access downsell",
            "url": "themissaffiliate.com/almostdone-416757-272179",
            "img": f"{P7}/P2_optin_P2_20260731T115714Z/20260731T115827Z__s1_after__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Declining the VIP does not end the sequence. A second paid offer for "
                    "<b>replay access</b> fires before she will confirm the seat.",
        },
        "replay": {
            "col": 5, "y": 120, "lane": "ever", "step": "Replay + booking",
            "title": "The full workshop replay — 1h 42m",
            "url": "themissaffiliate.com/replay",
            "img": f"{P8}/03_TY_registered_for_the_workshop/20260818T093447Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "The whole class now sits here, ungated, on Vidalytics — <b>6,177 seconds</b>. "
                    "A 1-hour <b>&ldquo;Miss Affiliate 1-1 Call&rdquo; booking calendar sits directly "
                    "under it</b>. The old YouTube decoy is still in the markup, unused.",
        },
        "vsl": {
            "col": 2, "y": 1360, "lane": "ever", "step": "Entry — funnel B",
            "title": "The /start VSL",
            "url": "themissaffiliate.com/start",
            "img": f"{P8}/02_VSL_start/20260818T093439Z__screenshot_fullpage.png",
            "max_h": 900,
            "note": "Watch video &rarr; apply. Different pixel "
                    "(<code>903499129224608</code>), <b>no Cortana</b>, and the footer says "
                    "<b>Los Angeles, CA</b> where funnel A says St. Petersburg, FL. "
                    "Different operator.",
        },
    },

    "DATA": {
        "adstat": {
            "col": 1, "y": 900, "lane": "paid", "step": "Spend footprint",
            "title": "What the Ad Library actually shows",
            "kv": [("Live ads", "18"), ("Unique creatives", "7"),
                   ("All launched", "20 Aug 2026"), ("Age at capture", "10 hrs"),
                   ("Under 100 impressions", "5 of 13 cards"),
                   ("Advertiser page", "1021090297763539"),
                   ("Ads before 20 Aug", "none in library"),
                   ("TikTok ads", "zero")],
            "note": "This is a <b>relaunch in testing</b>, not a scaled account. Nothing here "
                    "supports a $50k/day cold-traffic read on Meta.",
        },
        "gate": {
            "col": 3, "y": 1360, "lane": "ever", "step": "Qualification",
            "title": "The application gate — Typeform JAYokipv",
            "url": "themissaffiliate.com/application",
            "kv": [("Questions", "10"), ("Budget floor", "$2,000"),
                   ("Top band", "+$5,000"), ("Income bands", "3"),
                   ("Show commitment", "2 questions"),
                   ("Call length", "45–60 min, on a computer")],
            "note": "Q6 is the price anchor: <b>&ldquo;less than $2,000 (this is not the right "
                    "fit for me at this time)&rdquo;</b> — the DQ is written into the answer "
                    "itself. Q4 sorts student / stay-at-home mom / 9-5 / job-seeking / "
                    "entrepreneur / creator.",
        },
        "class": {
            "col": 6, "y": 120, "lane": "event", "step": "The class",
            "title": "103 minutes, genuinely live, no price",
            "kv": [("Runtime", "1h 42m 57s"), ("Words", "22,442"),
                   ("Slides", "281"), ("Teaching", "~31 min"),
                   ("Story + proof", "~23 min"),
                   ("Price stated", "never"),
                   ("Built in", "Gamma"),
                   ("Q&amp;A", "24 min, books on air")],
            "note": "Seven movements: frame, origin, opportunity, product selection, "
                    "content framework, the pitch, Q&amp;A. She reads chat names for the "
                    "full 103 minutes and <b>confirms bookings by name on air</b>. "
                    "Asked if it is pre-recorded she says it is her <b>first time</b> "
                    "running this format.",
        },
        "email": {
            "col": 2, "y": 900, "lane": "back", "step": "Follow-up",
            "title": "71 emails, zero written by a human",
            "kv": [("Messages", "71"), ("From her domain", "0"),
                   ("Sender", "webinarjam.net"), ("Distinct subjects", "8"),
                   ("Body", "~900 chars of platform furniture"),
                   ("20 Aug duplicate sends", "45"),
                   ("Real channel", "SMS 757-580-9956")],
            "note": "Her entire email programme is the <b>WebinarJam stock reminder "
                    "template</b>. Subject lines customised on one of two configs, body "
                    "never touched. No story, no proof, no objection handling. The work "
                    "happens over text.",
        },
        "prewb": {
            "col": 7, "y": 120, "lane": "ever", "step": "Objection library",
            "title": "21 videos, one per objection",
            "kv": [("Videos", "21"), ("Runtime", "25m 16s"),
                   ("Source", "4K Wistia"), ("Plus", "2m48s VSL"),
                   ("Longest", "algorithm / banned"),
                   ("Shortest", "age requirement, 9s")],
            "note": "Every video is titled with the objection it kills, and all of it sits on "
                    "the page every registrant lands on, before the training.",
        },
        "voice": {
            "col": 8, "y": 120, "lane": "ever", "step": "Technique",
            "title": "How the answers are built",
            "kv": [("Opener", "&ldquo;I want to be honest&rdquo;"),
                   ("Risk", "relocated onto hesitating"),
                   ("Income", "refuses to promise"),
                   ("90 days", "3 process wins"),
                   ("Structure", "concede, then reveal")],
            "note": "The honesty pledge buys permission to give a partly inconvenient answer, "
                    "which makes the convenient half land harder.",
        },
    },

    "EDGES": [
        ("ads", "optin"), ("optin", "vip"), ("vip", "down"), ("down", "replay"),
        ("replay", "class"), ("class", "prewb"), ("prewb", "voice"),
        ("optin", "email", "v"),
        ("vsl", "gate"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Funnel A — paid traffic into the weekly live class"},
        {"x": X[1], "y": 1300, "t": "Funnel B — separate pixel, separate operator, no ads found"},
        {"x": X[1], "y": 2400, "t": "Routing logic"},
        {"x": X[2], "y": 860, "t": "Follow-up"},
    ],

    "BRANCH": [
        {"id": "b_mismatch", "x": X[1] + 10, "y": 2460, "state": "no",
         "cond": "Three different class days, ad vs page vs event",
         "body": "Six of the seven running creatives say <b>&ldquo;this Sunday at 3pm "
                 "Eastern&rdquo;</b>. All 18 ads land on <code>/signup</code>, whose title "
                 "tag reads <b>&ldquo;Next Wed 8pm ET&rdquo;</b>. The class she actually ran "
                 "on 20 Aug was a <b>Thursday 8pm ET</b>, per her own WebinarJam mail. She is "
                 "paying to promise a day her funnel contradicts on arrival, twice.",
         "ev": "VERIFIED &middot; 7 creatives transcribed, both page titles, and the "
               "WebinarJam reminder body, 21 Aug"},
        {"id": "b_pixel", "x": X[2] + 10, "y": 2460, "state": "dq",
         "cond": "Two pixels → two operators",
         "body": "<code>/signup</code>, <code>/almostdone</code> and <code>/replay</code> all "
                 "carry pixel <b>2548125322312559</b> plus a Cortana hub. "
                 "<code>/start</code> and <code>/application</code> carry "
                 "<b>903499129224608</b> and no Cortana. Different pixel, different footer city. "
                 "The Ad Library shows <b>no ads at all</b> pointing at funnel B, so whatever "
                 "feeds it is not Meta.",
         "ev": "VERIFIED · pixels read off live HTML, domain-wide Ad Library query 21 Aug"},
        {"id": "b_decline", "x": X[3] + 10, "y": 2460, "state": "no",
         "cond": "Declines the $27 VIP → a second paid offer",
         "body": "The decline path is monetised. Saying no to VIP routes to a separate "
                 "replay-access offer, and only after declining <i>that</i> does the "
                 "confirmation page appear. Two chances to convert on the highest-intent "
                 "moment in the funnel.",
         "ev": "VERIFIED · walked both decline paths 31 Jul"},
        {"id": "b_free", "x": X[4] + 10, "y": 2460, "state": "dq",
         "cond": "The $13 replay is now free on /replay",
         "body": "She sells replay access for $13 inside the confirmation ladder, then serves "
                 "the <b>entire 1h42m class</b> unauthenticated on <code>/replay</code> to "
                 "anyone with the URL. The paid step is a friction tax on the honest, not a gate.",
         "ev": "VERIFIED · played 6,177s off the live page, no login, 21 Aug"},
        {"id": "b_email", "x": X[2] + 10, "y": 2760, "state": "dq",
         "cond": "The reminder sequence is untouched platform default",
         "body": "All 71 emails come from <code>webinarinfo@webinarjam.net</code>. Body is "
                 "~900 characters of class title, host name, room link and password. On "
                 "20 Aug it fired <b>45 times into one registration</b> in two bursts, "
                 "22 copies of one mail in three minutes. Her biggest class of the month, "
                 "18 fresh ads behind it, and the follow-up is stock template sent twenty "
                 "times over. <b>The one place we are clearly ahead.</b>",
         "ev": "VERIFIED &middot; 71 messages, 45 distinct message ids in the 20 Aug bursts"},
        {"id": "b_ugc", "x": X[6] + 10, "y": 2760, "state": "no",
         "cond": "She attacks the UGC model by name, unprompted",
         "body": "Asked in Q&amp;A how this compares to UGC, she says she started there at "
                 "18 or 19, then: <i>&ldquo;With UGC you're just paid for that one piece of "
                 "content and you never get paid on the sales it makes. The brand just takes "
                 "it from you.&rdquo;</i> One-off fee against residual. Same audience we "
                 "sell to, and we have no answer to it on file.",
         "ev": "VERIFIED &middot; transcript 01:34:04&ndash;01:35:00"},
        {"id": "b_apply", "x": X[4] + 10, "y": 2760, "state": "yes",
         "cond": "&ldquo;Please don't apply unless you're serious&rdquo;",
         "body": "The strongest move on the call. Applying becomes a favour to <i>her</i>, "
                 "and the scarcity is framed as respect for <b>other women waiting</b> rather "
                 "than her revenue. Raises perceived value and filters the list in one line, "
                 "and never sounds like selling. Paired with two separate questions that "
                 "extract a show-up promise in the prospect's own words before a call exists.",
         "ev": "VERIFIED &middot; close slides + Typeform Q8 and Q9"},
        {"id": "b_followers", "x": X[5] + 10, "y": 2460, "state": "dq",
         "cond": "&ldquo;I have no followers&rdquo; → pre-approved accounts",
         "body": "She concedes TikTok's real 5,000-follower rule plainly, then reveals a "
                 "&ldquo;cheat code&rdquo;: access to <b>pre-approved accounts</b> that already "
                 "clear it, &ldquo;ethically and safely&rdquo;. The concession is what makes the "
                 "reveal credible. <b>Flag:</b> account transfer sits against TikTok's terms. "
                 "Copy the persuasion structure, not the mechanic.",
         "ev": "VERIFIED · transcript of &ldquo;Do I need followers&rdquo;"},
        {"id": "b_risk", "x": X[6] + 10, "y": 2460, "state": "yes",
         "cond": "&ldquo;What's my risk?&rdquo; → risk is inaction",
         "body": "&ldquo;The real risk is not the program. The real risk is hesitating while "
                 "one of the biggest opportunities in social media history is happening right "
                 "in front of us.&rdquo; She never defends price. She moves the risk onto "
                 "standing still.",
         "ev": "VERIFIED · transcript, 99-second answer"},
        {"id": "b_90", "x": X[7] + 10, "y": 2460, "state": "yes",
         "cond": "&ldquo;How fast will I earn?&rdquo; → no number given",
         "body": "&ldquo;How much money will you make in 90 days? It's impossible to tell.&rdquo; "
                 "Then three process promises: confidence with the platform, first commissions "
                 "in 60&ndash;90 days, and a durable skill. Legally clean and more believable "
                 "than a figure.",
         "ev": "VERIFIED · transcript of the 90-day answer"},
    ],

    "LEGEND": [("paid", "Meta ads"), ("event", "Live training"),
               ("ever", "Evergreen assets"), ("back", "Paid upsell ladder")],
}

if __name__ == "__main__":
    build(CONFIG)
