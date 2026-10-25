# Troubleshooting flowchart

Don't try to fix nine things at once. Start at the top; follow the arrows. Stop as soon as the internet works again. The calm order exists because most outages die young: steps 1–3 catch most of them.

Print this page if you like paper. It follows the same order as [chapter 8](08-when-the-internet-drops.md), just without the explanations.

---

## Start

**Is the internet slow, or is it *down*?**

- **Slow only** → go to **Branch A** below.
- **Down (or mostly down)** → go to **Step 1**.

---

## Step 1 — Is it really down?

Open **two different sites on two different devices** (e.g., phone + laptop).

- **Yes, both fail** → continue to **Step 2**.
- **Only one site fails** → that site is down, not you. Try again later.
- **Only one device fails** → toggle airplane mode on it, or forget-and-rejoin the Wi-Fi, or restart that device. Done.

## Step 2 — Look at the router's lights

- **No lights at all** → the router lost power. Check the plug, the outlet, the power strip's switch. This step fixes a genuinely surprising number of outages.
- **Wi-Fi light off** → someone or something turned Wi-Fi off (button on the router, or an admin-page setting). Re-enable it on the router (or its app).
- **Internet/WAN/globe light is off or red** → your house is probably fine; the pipe from the street is down. Continue to **Step 3**.
- **All lights look normal** → continue to **Step 3**.

## Step 3 — Restart, properly

1. Unplug **router** (and **modem**, if separate) from power.
2. Wait **60 full seconds**.
3. Plug in **modem first**; wait 2–3 minutes until its lights settle.
4. Then plug in the **router**; wait 2 minutes.
5. Test on a device.

- **Internet is back** → done (success). Log it in your [worksheet's incident table](network-map-worksheet.md).
- **Still down** → continue to **Step 4**.

## Step 4 — Rebuild the connection from your device

On the affected device:

- **Forget** your Wi-Fi network, then **rejoin** it with the password.
- Toggle **airplane mode** for ten seconds.
- Restart the device.
- Try **ethernet** on a live device if available: if cable works but Wi-Fi doesn't, your internet is fine and your Wi-Fi isn't → go to **Branch B** below.

- **Internet is back** → done (success).
- **Still down** → continue to **Step 5**.

## Step 5 — Ask the outside world

Use **your phone with mobile data on** (Wi-Fi off):

- Check your provider's app or status page for a published outage in your area.
- Check a crowd-sourced outage site for a spike matching your provider's name.

- **Outage on record** → no fixing required. Tell the household; tether your phone to a laptop if you need the internet; wait it out.
- **No outage on record** → continue to **Step 6**.

## Step 6 — Call the provider

Say, with calm confidence:

- "I've power-cycled the modem and router, sixty seconds each."
- "Power and Wi-Fi lights are normal; the **WAN/Internet light is off/dark/in error state**."
- "Two different devices on ethernet get no internet." *(if you tested that)*
- "Is there any known outage in my area?" *(one last low-effort check)*

Ask politely to skip repeated restart scripts ("I've done the standard steps; can we get to line diagnostics?"). Have your account number on hand.

- **Provider can see and fix it** → done. Log it in the worksheet.
- **Provider schedules a technician** → done for now. The technician will come; tell them what your map in the worksheet says about where everything is.

---

## Branch A — When it's slow but not down

1. **Two-speed test:** speed-test with your newest phone standing **one step from the router**; then repeat in the slow room.
   - **Both fast** → the internet and Wi-Fi are fine; the slow device is old → buy nothing; use it as-is or replace that device.
   - **Fast near, slow far** → placement/band problem → [chapter 3](03-router-placement-and-channels.md) placement & channels, and [chapter 4](04-24-vs-5-ghz.md) for the band.
   - **Slow near, slow far** → continue below.
2. **What's eating the connection?** Check the router's device list (admin page; [chapter 9](09-router-admin-page.md)) for things downloading (TVs updating, backups syncing).
3. **Channel congestion?** If you live in an apartment, run a Wi-Fi analyzer and pick a cleaner 2.4 GHz channel (1, 6, or 11 — [chapter 3](03-router-placement-and-channels.md)).
4. **Provider delivering?** Run speedtest over **ethernet, nothing else active, when the house is quiet.** Far below your plan's speed across multiple days calls for a provider conversation.

## Branch B — When the internet is fine but the Wi-Fi isn't

1. **One room only?** Placement or band. Test 5 GHz vs 2.4 GHz ([chapter 4](04-24-vs-5-ghz.md)).
2. **Whole house?** Router restart, then check router settings you recently changed (screenshots in chapter 9), then a firmware update ([chapter 9](09-router-admin-page.md)).
3. **An extender involved?** Move it toward the *middle* of the house, not the far edge.

---

## After any outage: 5-minute closeout

- Add one row to the incident log in the [network map worksheet](network-map-worksheet.md).
- Notice if a pattern is forming (same time of night, same fix) — patterns are evidence, and evidence turns support calls from arguments into confirmations.
