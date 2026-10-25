# Glossary

Plain-English definitions for every piece of jargon in this handbook. If a chapter used a word you had to squint at, it's here. Words are ordered from "you need this" to "nice to have."

## The core cast

**Wi-Fi** — the radio link between your router and your devices. Same data as ethernet, just carried through the air.

**Router** — the director of your home network. It holds your devices together, hands out local addresses, and moves traffic in and out of your house.

**Modem** — the device that converts your provider's signal into plain ethernet, and back. Often built into the router; look for a "coax" or "fiber" cable plugged into it.

**Provider / ISP / Internet Service Provider** — the company that owns the cable coming into your house. You pay them monthly; when they say "we're all down," they're the reason.

**Ethernet / LAN cable** — the physical network cable. The yellow-RJ45-plug cousin of Wi-Fi. Faster and more stable than Wi-Fi in all real houses.

**Wi-Fi extender / repeater** — a small device that repeats your Wi-Fi signal further. Works well when placed *halfway* between the dead zone and the router, poorly when placed at the far edge of the house.

**Mesh system** — multiple router-pucks that work as one big seamless network. A neat approach in large or multi-floor homes.

## Addresses and identity

**Local address (IP address)** — every device on your network has one, like an apartment number inside one building. Usually starts with `192.168.` — your router hands these out.

**Gateway** — the address of your router. This is the number you type into a browser to reach the admin page (often `192.168.0.1` or `192.168.1.1`).

**MAC address** — a hardware serial number of a network card, permanent. (Not related to Apple computers; the name is a coincidence of naming history.) It appears in the router's device list.

**DNS** — the "phone book" of the internet. Turns `example.com` into the number the internet actually needs. Changing DNS to a "family provider" blocks coarse categories of sites; see [parental controls](07-parental-controls.md).

**SSID** — the name your Wi-Fi network broadcasts. What you see in the Wi-Fi picker. Renaming it changes nothing technically; it only changes what *you* and your neighbors see.

## Speed talk

**Bandwidth** — the width of the pipe: how much data can flow at once. Measured in **Mbps** (megabits per second). The number in your plan.

**Latency / ping** — how long one small packet takes to make the round trip. Measured in **ms** (milliseconds). Doesn't change "how much" data moves, but it determines how *snappy* a game, video call, or page load feels.

**Mbps** — megabits per second. Roughly: 25 Mbps is fine for one 4K stream; 100 Mbps is comfortable for a whole family; 1 Gbps (1000 Mbps) is wonderful and rarely needed in full.

**Throughput** — actual achieved speed once reality gets its cut (walls, distance, congestion). Your phone's speedtest result is your throughput.

**Packet / packet loss** — data travels in small numbered packets. "Packet loss" means some of them never arrive, which is what makes things stutter or hang. Usually caused by bad Wi-Fi signal or a failing cable, not by your provider.

## Wi-Fi specifics

**2.4 GHz / 5 GHz / 6 GHz** — the three radio "bands" your Wi-Fi can use. 2.4 GHz is slower but travels farther and powers cheaper, older devices. 5 GHz is faster and less crowded but dies sooner through walls. 6 GHz is newer and even faster, on newer hardware only.

**Channel** — a numbered slot within a band, like lanes on a highway. Knowing which channel your neighbors use helps you avoid them (see [placement and channels](03-router-placement-and-channels.md)).

**WPA2 / WPA3** — the security method guarding your Wi-Fi password. Any router made after ~2018 supports WPA2; newer ones support WPA3. Anything with WPA (no number) should be unplugged, sold for parts, or both.

**WPS** — a one-button pairing shortcut with known security flaws. Turn it off in your admin page.

**Band steering** — router behavior where both Wi-Fi bands share one network name, and the router steers devices onto the band it thinks fits them. Mostly good; occasionally wrong in ways that matter ([see how to override](04-24-vs-5-ghz.md)).

**Firmware** — the router's own operating system. Updates fix bugs and security holes; update when offered.

## Admin-page vocabulary

**Admin page / admin panel / management console** — the small private website your router runs, where all the settings live. See [chapter 9](09-router-admin-page.md).

**PORT / port forwarding** — a rule that says "if the internet sends traffic to my public address on port X, direct it inside my house to this specific device." Useful for a handful of advanced things; nothing a normal home needs by default.

**DMZ** — "demilitarized zone," an admin-page setting that removes *all* defenses for one device inside your network. It's a broad, blunt instrument; almost never what a home needs, and occasionally what a friend suggests in a panic. Avoid.

**VPN** — virtual private network. A private tunnel that moves your traffic through another server first; changes your public-looking location and hides your raw traffic from whatever Wi-Fi/ISP you're currently on (but not your own identity — see [chapter 6](06-what-a-vpn-actually-does.md)).

**Factory reset** — a button-hole on the router that un-does everything and returns it to as-new settings. Use this when you've lost the admin password or when a change left the router broken. Nothing about it is scary; you just re-enter your Wi-Fi settings afterward.

**Tethering / hotspot** — sharing your phone's mobile data with your laptop or other devices. The fallback during an outage (see [chapter 8](08-when-the-internet-drops.md)).

## Terms used but not needed

You may encounter these terms; knowing what they mean is enough to be at peace without adjusting anything:

- **QoS (Quality of Service)** — a way to prioritize some traffic over others (e.g., video calls over game downloads). Modern routers do a decent version automatically.
- **IPv6** — a newer, longer addressing scheme. Nothing you manage.
- **MU-MIMO / beamforming** — radio tricks on newer routers for better performance. You don't configure these.
- **Reboot** — "restart." Same thing. Calmer spelling.
- **Mbps vs MB/s** — Mbps is what ISPs measure and advertise (megabits). MB/s is what file downloads show (megabytes, 8× bigger). Your 100 Mbps plan downloading at "12 MB/s" is exactly correct, not a scam — just different units.
