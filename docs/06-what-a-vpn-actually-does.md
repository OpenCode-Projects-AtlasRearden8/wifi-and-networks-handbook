# Chapter 6 — What a VPN actually does (and when to skip it)

VPNs are sold with more confidence than they deserve. This chapter tells you exactly what one does, in one paragraph, then lists the honest cases for using one, and the noisy cases where you're paying for marketing.

## The one paragraph

A VPN is a private tunnel for your internet traffic. Instead of your traffic going straight from your house to a website, it goes **through a VPN server somewhere else first**, encrypted on the way.

That's it. Two consequences:

1. **To the website or app you're talking to, you look like you're at the VPN server's location**, not at your house.
2. **To your ISP (or the coffee-shop Wi-Fi you're on), your traffic is a sealed envelope** — they can see *that* you're using the internet and roughly *how much*, but not the contents.

That is the whole product. Encryption in transit; a relocated public IP address.

## What a VPN does NOT do

This list is where most VPN marketing quietly lies.

- **Does not make you anonymous.** Google, Facebook, and every website with a login still know exactly who you are, because you log in. A VPN changes your IP address, which is one of many identifiers.
- **Does not protect your device from viruses or phishing.** A VPN encrypts your pipe; it doesn't check what's inside it for malware.
- **Does not stop ad tracking.** Cookies, fingerprinting, and tracking pixels follow you regardless of your IP address.
- **Does not slow down scammers from calling your phone.** (Yes, some people believe this.)
- **Does not make your passwords safer.** Unrelated services, entirely.
- **Does not mean "no one can see what I do."** Your VPN provider sees what you do. You've moved the trust from your ISP to the VPN company. Sometimes that's a good trade (next section); just know a VPN is a shift in who you trust, not the removal of trust.

## The honest cases for a VPN

These are real, ranked by usefulness:

1. **Public/uncertain Wi-Fi.** Hotel, airport, café, hospital break room. You have no idea who runs the network, so treating the pipe as sealed is cheap peace of mind. This is the strongest use case.
2. **You want to look at another country's version of the internet.** Travel, or living apart from your home country's services. (This is the actual, real-life reason most people use VPNs for streaming, and it's a fair one.)
3. **You don't want your ISP selling your browsing history.** Legal in many places. This is principled, not paranoid.
4. **Accessing your own home network while away.** The *good* kind of VPN: connecting to your own router or a small device in your house remotely. You usually want your *own* home VPN — see the note below.
5. **Being cautious on a shared network.** For those times when you're on a work WiFi in a shared office with 60 other laptops.

## When you can politely skip a VPN

You don't need one if any of these are true:

- **At home, on your own Wi-Fi, just browsing.** Your home Wi-Fi with a WPA2/WPA3 password is already sealed. Your VPN does essentially nothing here except slow you down a bit.
- **All or nearly all your traffic is HTTPS.** Which means almost all traffic today: your bank, your email, every major site. The web is already end-to-end encrypted separately from the VPN; note the little padlock in the address bar.
- **You're chasing a feeling of anonymity.** You're not getting it, and a VPN app is not the way to look for it.
- **You see it bundled with software as a "protection" checkbox.** You might already have a working VPN through your antivirus or phone plan; use the bundled one (or skip it) rather than paying twice.

## Self-hosted home VPN: worth knowing about

There's a second, quieter kind of VPN. Some modern routers (and small devices like a Raspberry Pi) can run a VPN server *in your own house.*

What that means: you connect to your home VPN from the road, and you appear to be on your own home network. You can then reach your own file server, your printer, or just use your home connection as a private tunnel. This is a hobbyist's tool — genuinely useful, and something to consider later. It's mentioned here only so you know it exists; you do not need to set one up today.

## Picking a VPN if you need one

The market is loud. Filter it with three questions:

1. **Who owns it, and where is it?** Reputable VPNs are backed by known companies. The product is trust, so buy from people who've been around and published audits. Location matters less than reputation.
2. **Do they have a no-logs policy that has been audited** (not just claimed)? Look for third-party audit mentions in their documentation.
3. **How many simultaneous device connections?** Most plans cover 5–10. Just pick one that covers your house comfortably.

Skip "free" VPNs. If you're not paying with money, the product is your browsing data, which is the very thing you were trying to avoid sharing. A cheap reputable paid VPN is the honest option.

## The calm summary

> A VPN moves two things: your apparent location, and who can read your raw traffic. It doesn't hide your identity, block viruses, or stop ads. If you're at home on your own Wi-Fi, skip it. If you're on public Wi-Fi, want to appear somewhere else, or don't trust your ISP's business practices, a reputable paid VPN is a sensible, boring purchase.

Next: a fair, un-panicked approach to [parental controls](07-parental-controls.md).
