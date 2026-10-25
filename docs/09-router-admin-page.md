# Chapter 9 — Reading your router admin page without fear

Every router runs a small website, private to you, that shows and controls everything about your network. People find it for the first time while trying to rename Wi-Fi and immediately leave. This chapter tours the rooms so nothing looks ominous.

## The front door: finding the admin page

You have three common options; try in order.

### Option 1 — The address printed on the router

Flip the router over. The sticker gives you a web address like `192.168.0.1` or `192.168.1.1`, or a wordy one like `http://myrouter.net`. Type that into any browser's address bar. This works in 90% of homes.

### Option 2 — Your device tells you where the router is

On your phone, with your Wi-Fi connected, look at the network's details:

- **Android:** Settings → Wi-Fi → tap your network → **Gateway** (or "Router") shows an address.
- **iPhone:** Settings → Wi-Fi → tap the (i) → **Router**.
- **Mac:** System Settings → Wi-Fi → Details → TCP/IP → **Router**.
- **Windows:** type `ipconfig` in a terminal; **Default Gateway** is your router's address.

Type that address into your browser.

### Option 3 — The router's own app

If your router brand has a phone app (many newer ones: Eero, TP-Link Tether, ASUS, Netgear, Google Home), the app logs you in with no address juggling at all. That's fine; the below tour still applies.

## The lock: signing in

You'll see a login page. Two cases:

1. **Your router made you set a password** (or the sticker has a unique admin password). Use it.
2. **Default credentials.** Older routers might still use `admin`/`admin` or `admin`/`password`. If yours does and you've never changed it, that's your first fix: change the admin password *right now.* A stranger who connects to your Wi-Fi can get in and quietly take over your home network with more steps — this is trivial to prevent.

> **The admin password is not your Wi-Fi password.** It's the login to the management page. Make it different, and make it a proper phrase you don't share with guests.

If you've lost the admin password: hold the small **reset** button pressed for about 10 seconds (usually a recessed pinhole). It puts the router back to factory settings, with the factory password from the sticker again. You'll then re-set your Wi-Fi name/password. Annoying, not fatal — and nothing you broke requires calling anyone.

## The tour: five rooms you'll actually use

Router pages differ in looks but all contain the same five rooms in slightly different furniture.

### Room 1 — Wireless / Wi-Fi settings

Here you can:

- Rename your network (**SSID**) and change **Wi-Fi password**.
- See and configure **2.4 GHz** and **5 GHz** separately ([chapter 4](04-24-vs-5-ghz.md)).
- Set the **channel** ([chapter 3](03-router-placement-and-channels.md)).
- Turn on the **guest network** ([chapter 5](05-passwords-and-guest-networks.md)).

Rules of safe use:

- Change one thing, click **Save/Apply**, and wait. Test before changing anything else. This is the single most important admin-page habit.
- Rename the network and both passwords in one visit if you must; but do it in that order and save between steps.

### Room 2 — Attached devices / Device list

The **device list** shows every device connected to your network — name, manufacturer, and the local address (IP). This is the most underused page in admin-land, and your [network map worksheet](network-map-worksheet.md) mirrors it.

Use it to:

- See if an unexpected device is connected (e.g., when your Wi-Fi speed is mysteriously congested).
- Identify your kid's console in the middle of the night for a pause.
- Learn names for your devices so your troubleshooting map stays accurate.

Names may look cryptic (`ESP_a7c3`, `DESKTOP-F4J2K1`); match them online-quarters ("the lamp that was set up three months ago") or just cross-check which devices are offline right now to help identify them.

### Room 3 — Parental controls / Access control

Discussed fully in [chapter 7](07-parental-controls.md). Usually a list where you pick a device, set a schedule or block categories. This is one of the pages you might visit multiple times a year.

### Room 4 — Status / System

Shows:

- Your **internet connection status** ("connected," IP address from provider, uptime).
- Your **firmware version** (the router's own operating system).
- Sometimes a **speed test** or **system log** (the log is for when you call support; don't try to read the whole thing).

### Room 5 — Firmware update / Software update

Two minutes a year that keep the router secure and fixed.

- Newer routers can auto-update in the background (great; leave it on if offered).
- Older ones need you to click **Check for updates** under a page called **Firmware/System/Tools**. Update the firmware when it's offered, ideally at a time when the family's Wi-Fi demand is low (an update can briefly restart Wi-Fi and it takes a few minutes).
- Write the date of the last update in your network map notes. If your router hasn't updated in years and can't, it's a candidate for replacement — old firmware is a security concern on any exposed-Internet device.

## What you should *never* touch

For the reader who's wandering the admin page out of calm curiosity (hello, welcome, it's fine), a list so you know to walk past it:

- **WAN settings / internet connection type / PPPoE credentials.** This is where you can break your whole internet if your provider gave you specific settings. Don't modify anything here.
- **DMZ / Port forwarding** (unless someone actually told you to forward a specific port; if you don't know, you don't need it).
- **Deep-advanced knobs** like QoS, IGMP, or multicast settings — safe to *look* at, safer to not alter. You can always search the term if you're truly curious.
- **Reset/factory reset** — unless you mean it and have your passwords ready to re-type.

> A trick: **screenshots before and after any change.** Then you always know how to get back if a change made things worse. (Only on desktop for now.)

## The three habits of a safe admin-page visit

1. **One change, apply, test.** Never a batch of changes.
2. **Screenshot before you change.** So you can always find your way back.
3. **Update firmware when offered.** Fewer bugs, fewer security holes, less slowness.

That's the last chapter. Now for the tools: the [network map](network-map-worksheet.md), the [flowchart](troubleshooting-flowchart.md), and the [glossary](glossary.md).
