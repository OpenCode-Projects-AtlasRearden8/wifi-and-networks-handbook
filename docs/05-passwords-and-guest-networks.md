# Chapter 5 — Passwords and guest networks

Home-network security has one legitimate goal: the people you live with (and their devices) can get on, and strangers at your door can't. Everything in this chapter serves that goal and stops there. You are not a bank.

## One strong Wi-Fi password, one time

Your Wi-Fi password is worth caring about, but only modestly: it's the front door key of your house, not the vault.

**What a good Wi-Fi password looks like:**

- Long (12+ characters). Length beats cleverness.
- Easy to say out loud to a guest, so letters and digits only if you can, and no sneaky uppercase-lookalike characters.
- Not shared with every account you own.

A **four-word phrase** like `tin-harbor-mango-1998` is secure, memorable, and easy to say to a houseguest while making a drink. That's the right shape.

**What you don't need to do:**

- Rotate it monthly. Nobody does, and it trains your household to write passwords on the fridge — which is the actual security problem.
- Use special characters `!@#$%`. They make it hell to type on a TV remote, which makes people keep the default password instead.
- Hide the SSID (turn off the broadcast of your network name). This is the one "security" setting that *makes your life worse* and adds zero real protection. Don't.

## Three passwords, three personalities

Modern routers often have up to three passwords. Know which is which:

| Password | What it's for | Who knows it |
| --- | --- | --- |
| **Admin password** | Signs into the router's admin page (the management panel) | Only you (one person) |
| **Wi-Fi password** | Signs a device onto your network | Everyone in your house |
| **Guest password** | Signs a guest's device onto the guest network | Anyone who visits |

Two rules:

1. **The admin password should not be the same as the Wi-Fi password.** A guest who learns your Wi-Fi password should not also gain access to your router's settings.
2. **Nobody outside your house needs the Wi-Fi password if you set up a guest network.** See the next section.

## Guest networks: a small kindness, well-made

Guest networks are extremely useful and almost nobody uses them. A guest network is a separate room in your house with one job: let visitors get online, and keep them out of your file cabinet.

### Why make one

- Guests can use Wi-Fi through your front door without you typing your main password on their phone in front of them (a small, real social discomfort).
- Guests can't see your file cabinet because guest networks are inbound-isolated: they can reach the internet, but not your computers, printers, or full network.
- Even your *own* visitors' devices, if they have a virus, can't wander around your home network.

### What to set up

Most routers made after about 2016 include a guest network option. It generally looks like:

- **Wireless settings → Guest network → Enable**
- Name: something obvious, like `FrankHouse-Guest`.
- Password: simple, memorable, maybe rotate when a long-term guest leaves. `guest-welcome-house` is fine.
- **Turn off "Allow guests to see my local network"** (sometimes phrased as access to "intranet" or "LAN"). This is the isolation switch. Turn it off if it's on.
- Choose 2.4 GHz if you want your guests' older devices to work reliably, or enable the guest network on both bands if you can.

### Practical guest etiquette

- **Long-term guests or housemates** should be given your main Wi-Fi password, not the guest one. A person living in your home isn't a guest.
- **Visitors at your door** should get the guest password. Print the guest password on a small card and keep it by the router or on the fridge. This looks hospitable; it is also secure.

## WPS: the button you should never press

WPS ("Wi-Fi Protected Setup") is supposed to be a friendly one-touch pairing. It's fine for a toaster. It's also a well-documented weak point in routers that support it, because the protocol has a math weakness that lets patient attackers guess the PIN.

- **Turn it OFF if your router admin page has a "WPS" toggle.** Nothing you use regularly depends on it.
- If you've never used the WPS button, you will not miss it.

## A note on router admin passwords

When you set up a new router, the first thing to change is its **admin password** (sometimes the router forces you to change it — good). If your router is still using the factory default admin password with a printed sticker on the bottom, fix that today. It takes one minute: see [chapter 9](09-router-admin-page.md) for how to sign in.

## What to skip (owing to your calm bonhomie)

You do not need:

- MAC filtering (an old, tedious, and easily bypassed "security" system).
- Per-device whitelisting.
- A complex password of symbols that no one in the house can type on a TV remote.
- "Security"-flavored apps that promise to "protect your Wi-Fi."

Your honest security picture, in one sentence: **strong main Wi-Fi password, different strong admin password, guest network for visitors, WPS off.** That's it. That's genuinely most of the useful work.

Now onto one of the most-misunderstood tools in all of home networking: [VPNs](06-what-a-vpn-actually-does.md).
