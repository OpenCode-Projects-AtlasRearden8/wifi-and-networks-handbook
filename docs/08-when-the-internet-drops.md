# Chapter 8 — Fixing the internet calmly when it drops

It's 9:47 pm. The video stops. Your heart does a small thing. This chapter exists so that the next time that happens, you follow steps instead of doing whatever your hands feel like doing.

The order below is deliberate. Do the steps **in order** and stop when the internet returns. Most outages die at step 2 or step 3.

## Step 0 — Breathe. Then check if it's really down

Open two different things on two different devices.

- A website on your phone **and** a different website on your laptop.
- If *both* fail, it's your network or your provider. Continue.
- If only one device / one site fails, it's that device or that site. Restart the app, then the device. You're done — no router was harmed.

*Why two devices and two sites:* single-site outages are common (the site, not you). Single-device failures are common (the device). Both are much more common than your whole network being down.

## Step 1 — Look at your router's lights

The lights on the router are its face. Squint, and read them:

| Light | Healthy | Not healthy |
| --- | --- | --- |
| **Power** | Solid on | Off, or blinking oddly |
| **Internet / Globe / WAN** | Solid, or blinking gently | **Off — usually means the provider signal is missing** |
| **Wi-Fi** | Solid or blinking with activity | Off (someone turned Wi-Fi off accidentally — router button or a pet) |

**Are there NO lights at all?** The router lost power. Check the plug, the outlet, the power strip's switch. Truly: about one in five "outages" are this.

**Is the Internet/WAN light off or red?** Your house is fine; the pipe from the street is down. Jump to **Step 5** (restart the modem) — but keep in mind this may genuinely be an outage on the provider side.

## Step 2 — Figure out whether Wi-Fi or internet is the problem

This matters: **Wi-Fi being down and internet being down are different problems with different fixes.**

- **Can you connect to your Wi-Fi but get no internet?** Your Wi-Fi link to the router is fine. The problem is between the router and the outside world → **Step 5**.
- **Does your device not even see your Wi-Fi name in the picker?** Your Wi-Fi itself is down → the router needs a restart → **Step 3**, or Wi-Fi got disabled → check the admin page (chapter 9).
- **Is it only one room?** Probably not an outage at all — it's placement/band (chapters [3](03-router-placement-and-channels.md) and [4](04-24-vs-5-ghz.md)). Restarting won't help.

## Step 3 — Restart the router (the classic, because it works)

Power cycling clears the router's memory of stale connections, half-rebooted devices, and confusion. It is a legitimate diagnostic step that professionals do first.

**Do it properly:**

1. Unplug the router (and modem, if separate) from power.
2. Wait a full **60 seconds**. (Yes, actually wait. A fast unplug-replug doesn't let the internal memory drain.)
3. Plug in the **modem first** (if separate), wait 2–3 minutes for its lights to settle.
4. Then plug in the **router**, wait 2 minutes.
5. Test on a device.

That resolves a large share of normal home outages all by itself.

## Step 4 — Reconnect the problem device

If the network is up but your *device* still misbehaves:

- **Forget the network and rejoin.** On the phone/laptop: Wi-Fi settings → your network → "Forget," then rejoin with the password. Clears corrupted saved-link data.
- **Toggle airplane mode** for 10 seconds. Cheap and weirdly effective on phones.
- **Restart the device.** Boring, works.
- **Try ethernet.** If the device has a port, plug in. If it works on cable and not on Wi-Fi, the problem is Wi-Fi (placement, band, antenna), not the internet.

## Step 5 — Restart the modem (if separate from the router)

If your provider signal itself (WAN light) is not solid:

1. Unplug the modem's power for 60 seconds.
2. Plug in. Wait. Its lights walk through a sequence; internet light should become solid/flicker-with-traffic.
3. Then restart the router behind it.

Some providers have long "handshake" waits (up to 5 minutes, occasionally with proprietary blink codes printed on the bottom of the modem — you can look them up if you care, but you don't have to).

## Step 6 — Ask the outside world

If two restarts haven't fixed it, learn whether it's just you:

- **Use your phone with mobile data** (Wi-Fi off). Look up your provider's status/coverage page or app; most ISPs publish a live outage map.
- Check a service like DownDetector for your provider's name for a spike.
- **Call/text the provider.** That's what phone plans are for on outage nights.

If the answer is "a crew is working on your street," then you're done actively fixing anything. Tell the household, open a book, and consider the evening reclaimed.

## Step 7 — Call the provider (when to bother, and what to say)

Call tech support only when:

- You've done a proper full restart (modem + router, 60-second wait).
- Lights on the console/power are healthy but the WAN light stays dark or red.
- An outage is *not* published in your area.

**Have this information ready; it transforms the call:**

- "I've power-cycled modem and router for 60 seconds each."
- "Power light is solid, Wi-Fi is on, **WAN/Internet light is off/dark/in error state**." (This specific phrasing reads to them as "not a beginner" and gets you a real technician faster.)
- "Devices on ethernet get no internet. I've tested two different devices." (If you've tested that.)
- Your account number and the modem's serial/MAC, if asked (usually printed on the bottom).

You can politely request escalation if the phone script goes nowhere. Repeating what you've already tried is not useful; say gently, "I've done the standard restart steps; can we skip to line diagnostics?" Almost every tier-1 phone agent will immediately do the polite equivalent of nodding.

## Step 8 — After it works again: 5 minutes that save hours

- Note the date and what fixed it. Two or three notes later, you *will* start seeing a pattern (e.g., "it died three times in two weeks around midnight").
- If the outage pattern is recurring, that's evidence to bring to your provider (and possibly the point at which you look at replacing the router/modem, especially if it's more than 5 years old).
- Update your [network map worksheet](network-map-worksheet.md) if anything changed.

## The one-paragraph fallback when you need the internet *now*

Phone → turn Wi-Fi off → you have mobile data → tether your laptop to your phone (Settings → Personal Hotspot / Mobile Hotspot) → continue your evening. Tethering is not the plan anyone wants long-term, but it makes an outage a minor event rather than a crisis. Check your plan's hotspot allowance once, so you know your budget.

That's the whole chapter. When you've calmed down afterward, take ten minutes to set up the [network map worksheet](network-map-worksheet.md) so the next outage is a lookup instead of an adventure. And once for courage, skim [the router admin page without fear](09-router-admin-page.md).
