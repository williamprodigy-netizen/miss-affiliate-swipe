#!/usr/bin/env python3
"""Miss Affiliate — the whole business, wired.

Run: python3 build_board.py  ->  board.html
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from boardbuild import build, X

REPO = os.path.dirname(os.path.abspath(__file__))
S = os.path.expanduser("~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS")
P = f"{S}/Miss_Affiliate - Signup_Sunday - 2026-07-31/02_Pages"

CONFIG = {
    "OUT": os.path.join(REPO, "board.html"),
    "KICK": "Competitor swipe · captured 31 July 2026",
    "TITLE": "Miss Affiliate — the whole business, wired",
    "BLURB": "Nurse to $157k/month, sold to women off a weekly Sunday training. Two paid steps "
             "sit between the opt-in and the confirmation page, and the pre-webinar page carries "
             "<b>21 objection videos in 4K</b> &mdash; the closest match in this swipe file to "
             "the objections our own setters hit in DMs.",

    "SHOTS": {
        "optin": {
            "col": 1, "y": 120, "lane": "event", "step": "Entry",
            "title": "Signup Sunday opt-in",
            "url": "themissaffiliate.com/signup-sunday",
            "img": f"{P}/01_Opt-in/20260731T103128Z__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "&ldquo;From 12-hour nursing shifts burnt out to $157k/month.&rdquo; "
                    "Full name optional, <b>phone and email required</b>. "
                    "&ldquo;Limited to 250 total live spots.&rdquo;",
        },
        "vip": {
            "col": 2, "y": 120, "lane": "back", "step": "Upsell 1",
            "title": "$27 VIP — &ldquo;spot isn't fully confirmed yet&rdquo;",
            "url": "themissaffiliate.com/almostdone-sunday",
            "img": f"{P}/P2_optin_P2_20260731T115714Z/20260731T115821Z__s1_before__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "30-day roadmap, product guide + 13 niches, top 20 hooks, and a 1-to-1 "
                    "coach call. &ldquo;Limited to 50 women total.&rdquo;",
        },
        "down": {
            "col": 3, "y": 120, "lane": "back", "step": "Upsell 2",
            "title": "Replay-access downsell",
            "url": "themissaffiliate.com/almostdone-416757-272179",
            "img": f"{P}/P2_optin_P2_20260731T115714Z/20260731T115827Z__s1_after__screenshot_fullpage.png",
            "max_h": 1000,
            "note": "Declining the VIP does not end the sequence. A second paid offer for "
                    "<b>replay access</b> fires before she will confirm the seat.",
        },
    },

    "DATA": {
        "prewb": {
            "col": 4, "y": 120, "lane": "ever", "step": "Pre-webinar",
            "title": "The objection library — 21 videos",
            "kv": [("Videos", "21"), ("Runtime", "25m 16s"),
                   ("Source", "4K Wistia"), ("Plus", "2m48s VSL"),
                   ("Longest", "algorithm / banned"),
                   ("Shortest", "age requirement, 9s")],
            "note": "Every video is titled with the objection it kills. All of it sits on the "
                    "page every registrant lands on, before the training.",
        },
        "voice": {
            "col": 5, "y": 120, "lane": "ever", "step": "Technique",
            "title": "How the answers are built",
            "kv": [("Opener", "&ldquo;I want to be honest&rdquo;"),
                   ("Risk", "relocated onto hesitating"),
                   ("Income", "refuses to promise"),
                   ("90 days", "3 process wins"),
                   ("Structure", "concede, then reveal")],
            "note": "The honesty pledge buys permission to give a partly inconvenient answer, "
                    "which makes the convenient half land harder.",
        },
        "event": {
            "col": 6, "y": 120, "lane": "event", "step": "The pitch",
            "title": "Sunday training — not yet captured",
            "kv": [("When", "Sundays 3:00 PM ET"),
                   ("Cap", "250 live spots"),
                   ("Price", "not yet observed"),
                   ("Registered", "yes")],
            "note": "Genuinely live, so it has to be attended. This is where the price is.",
        },
    },

    "EDGES": [
        ("optin", "vip"), ("vip", "down"), ("down", "prewb"),
        ("prewb", "voice"), ("voice", "event"),
    ],

    "LABELS": [
        {"x": X[1], "y": 60, "t": "Single mechanism — weekly live training"},
        {"x": X[1], "y": 1600, "t": "Routing logic"},
    ],

    "BRANCH": [
        {"id": "b_decline", "x": X[1] + 10, "y": 1660, "state": "no",
         "cond": "Declines the $27 VIP → a second paid offer",
         "body": "The decline path is monetised. Saying no to VIP routes to a separate "
                 "replay-access offer, and only after declining <i>that</i> does the "
                 "confirmation page appear. Two chances to convert on the highest-intent "
                 "moment in the funnel.",
         "ev": "VERIFIED · walked both decline paths 31 Jul"},
        {"id": "b_followers", "x": X[3] + 10, "y": 1660, "state": "dq",
         "cond": "&ldquo;I have no followers&rdquo; → pre-approved accounts",
         "body": "She concedes TikTok's real 5,000-follower rule plainly, then reveals a "
                 "&ldquo;cheat code&rdquo;: access to <b>pre-approved accounts</b> that already "
                 "clear it, &ldquo;ethically and safely&rdquo;. The concession is what makes the "
                 "reveal credible. <b>Flag:</b> account transfer sits against TikTok's terms. "
                 "Copy the persuasion structure, not the mechanic.",
         "ev": "VERIFIED · transcript of &ldquo;Do I need followers&rdquo;"},
        {"id": "b_risk", "x": X[5] + 10, "y": 1660, "state": "yes",
         "cond": "&ldquo;What's my risk?&rdquo; → risk is inaction",
         "body": "&ldquo;The real risk is not the program. The real risk is hesitating while "
                 "one of the biggest opportunities in social media history is happening right "
                 "in front of us.&rdquo; She never defends price. She moves the risk onto "
                 "standing still.",
         "ev": "VERIFIED · transcript, 99-second answer"},
        {"id": "b_90", "x": X[7] + 10, "y": 1660, "state": "yes",
         "cond": "&ldquo;How fast will I earn?&rdquo; → no number given",
         "body": "&ldquo;How much money will you make in 90 days? It's impossible to tell.&rdquo; "
                 "Then three process promises: confidence with the platform, first commissions "
                 "in 60&ndash;90 days, and a durable skill. Legally clean and more believable "
                 "than a figure.",
         "ev": "VERIFIED · transcript of the 90-day answer"},
    ],

    "LEGEND": [("event", "Live training"), ("ever", "Pre-webinar assets"),
               ("back", "Paid upsell ladder")],
}

if __name__ == "__main__":
    build(CONFIG)
