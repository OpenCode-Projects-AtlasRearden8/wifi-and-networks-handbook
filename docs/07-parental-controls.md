# Chapter 7 — Parental controls

A calm, honest chapter. Two ideas up front:

1. **Network-level parental controls are one tool of several, and not the strongest one.** They're easy to set up, easy to circumvent (any teen with a phone and data plan walks around them), and best treated as guardrails, not locks.
2. **The conversation matters more than the filter.** Machines enforce; they don't explain. Combine modest technical limits with an honest conversation and you get much further.

## Where parental controls live (pick one layer)

There are four layers, from weakest to strongest:

| Layer | Where | What it can do | Honest limitation |
| --- | --- | --- | --- |
| Router | Your router's admin page | Wi-Fi schedules, category block lists, per-device pause | Easily bypassed with mobile data; doesn't follow kids off your Wi-Fi |
| DNS | Router or a DNS provider ("family DNS") | Blocks whole categories (adult, gambling) domain-wide | Websites that rotate domains slip through; doesn't filter apps well |
| Device | The phone/tablet/console itself (Screen Time, Family Link, console parental settings) | App limits, content ratings, purchase locks | Needs per-device setup; the device is the one thing that actually reflects what the kid sees |
| App | Individual apps (YouTube Kids, in-app PINs) | Fine-grained, content-specific | App-by-app; can be missed |

The honest best answer for most families: **light network-level guardrails + real device-level limits on the phones**. The device settings are the ones that actually work while the kid is out of the house.

## At the router (network level)

Most recent routers have some parental controls. Common shapes:

- **Per-device pause / schedules.** Pause a specific device (e.g. "the Xbox") during dinner or after bedtime. This is the most useful single feature and a calm one: it targets the screen, not the child.
- **Category blocking.** Block "adult," "gambling," "social media" categories via the router's filtering list. Works through your network only, so a phone with mobile data bypasses it entirely.
- **SafeSearch enforcement** (some routers pass a flag to Google/Bing to force safe search on your network). Nice-to-have; not perfect.

Find these under names like **"Parental Controls," "Device access," "Access control," "Family,"** or **"Profiles"**.

**Practical tip:** schedule the pause around real life (dinner, bedtime), not around an abstract "screen time maximum." Real schedules are easier to explain ("Wi-Fi sleeps when we sleep") and less of a battle than constant supervision.

## At the DNS level (one quiet setting, whole-house effect)

A small step with real reach: change your router's **DNS** to a "family" DNS provider (most offer this for free for home use).

DNS is the phone book of the internet: it translates `example.com` into a number. Family DNS providers underline their phone book: certain domains resolve to a polite blank page.

- **What it blocks:** adult content sites, often gambling/hate/phishing, with categories you can toggle in a dashboard.
- **What it doesn't block:** YouTube/video apps (they serve contradictory domains), in-app content, messaging. It's a coarse filter.
- **Where to set it:** your router's admin page is one place (applies to every Wi-Fi device at once). Some phones can also set private DNS per-android-device — better for a phone that leaves your house.
- **The trade:** you'll get occasional false positives ("this blog is blocked?"), which you can usually whitelist in under a minute if the provider has a dashboard.

## On the kid's device (the layer that works)

This is where the honest work is. Every major platform has real parental settings built in, for free:

- **iPhone/iPad:** Screen Time (in Settings). App limits, content ratings, purchase approval, downtime schedules, and — genuinely valuable — "Ask to Buy" for purchases.
- **Android:** Google Family Link (a free app). App limits, screen-time budgets, bedtimes, content filters for Google services.
- **Windows/Mac:** built-in family features (Microsoft Family Safety / Apple's combined settings).
- **Consoles:** each platform (Nintendo, PlayStation, Xbox) has solid parental app companions. The console apps are often better than the router for gaming schedules, because they know what the console is playing.

Two genuinely useful settings in this layer:

1. **Purchase/approval locks.** $40 mystery charges are a common and avoidable heartbreak.
2. **Per-app time limits on the two or three apps that actually cause pain** (usually YouTube or a specific game). Limit the actual problem app rather than the whole device; you'll get less pushback.

## What to skip or don't bother with

- **Fine-grained activity monitoring, keyloggers, screenshot spying.** These tools exist. For most families they damage communication more than they improve safety, and a determined teenager will find the workaround anyway. If you feel you need this level of surveillance, the situation is bigger than network settings, and the right move is a conversation (and possibly a counselor), not a better filter.
- **Extra paid "parental control routers."** The built-in features of a decent modern router plus free controls on the devices cover 90% of cases.
- **Hidden blocking the kid doesn't know about.** If they find out (they will), it reads as dishonesty, and trust is the thing that actually protects them.

## A calm script, if helpful

One honest conversation covers more ground than any filter:

> "Phones and the internet are useful but designed to be hard to put down. No one blames you for that — it's built that way on purpose. So we're going to use the tools to help everyone, me included. Wi-Fi sleeps at 9:30. Your device has downtime too. If you need an exception, knock. And if you ever see something that upsets you, or someone online makes you feel weird or pressured, come tell me — you won't be in trouble. That's the rule that matters most."

The last sentence is the real parental control. Filters can't ask for help; a kid who knows they can come to you can.

## Quick setup order (30 minutes, once)

1. Set purchase locks and a simple, explained screen schedule on the kid's devices (the layer that works).
2. Set one router-level rule you'll enforce consistently (e.g. the game console pauses at bedtime).
3. Optional: switch DNS to a family provider for coarse category blocking.
4. Tell them what you set and why, briefly, with an offer to revisit as they mature.

That's genuinely most of it. Next: the chapter you'll open at 11pm when the Wi-Fi dies: [when the internet drops](08-when-the-internet-drops.md).
