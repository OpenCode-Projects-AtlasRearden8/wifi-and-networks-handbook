# Chapter 1 — How your home network actually works

Imagine water pipes for data. That's genuinely most of it. Let's name the pipes.

## The journey of your data, from request to cat video

When you open a website, data travels through a chain of friendly equipment:

1. **Your device** (phone, laptop, TV, whatever you're holding).
2. **Your router** — the director and dispatcher of your house.
3. **Your modem** — often built into the router these days; it talks to your ISP.
4. **Your provider (ISP)** — the cable/fiber/phone company that owns the road to the outside world.
5. **The internet** — the rest of every other road, and the site's server somewhere on it.

Each hop only knows how to pass the data along. Your router decides where the data goes *within your house*; your ISP decides where it goes *outside your house*.

## The pieces, one at a time

### Modem

The modem's whole job: convert your provider's signal into plain ethernet, and vice versa.

- If your provider is cable, the modem goes in the coax wall jack.
- If it's fiber, the modem is a small box that a fiber line goes into.
- If your provider gives you one box that does everything, it contains a modem **and** a router. People call it "the router," "the box," or "the internet one." All wrong; all fine.

### Router

The router has two jobs:

1. **Hold your local network together.** Every device in your house is a pupil and the router is the teacher taking attendance.
2. **Move traffic in and out** between your devices and the outside world.

It does this with addresses. Every device in your house has a **local address** (something like `192.168.1.42`), which is private — like an apartment number that only matters inside your building. The router hands out those numbers, remembers who has which, and forwards your requests out and the answers back in.

### Switch (usually invisible)

If your router has four yellow or white ports on the back, those are a built-in switch. It lets you plug devices in with ethernet cables instead of Wi-Fi. More ports = more of these. Plugging in a device is the single highest-quality improvement you can make for anything that sits still, like a TV or a desktop computer.

### Wi-Fi (the invisible part)

Wi-Fi is just a frequency band on which your router speaks. It's the same data, just carried by radio instead of cable. Radio has three big constraints:

1. It gets **weaker** as you get farther from the router.
2. **Walls diminish it**, and every interior wall is another diminishing.
3. It shares the air with **everyone else's** Wi-Fi, Bluetooth, and microwave (more on microwaves later — yes, really).

## What "speed" actually means

You have two separate speeds, and conflating them causes about half of all Wi-Fi confusion:

- **Internet speed** — the rated speed you pay your provider for. Tested by speed-test websites. This is the width of the pipe between your house and the world.
- **Wi-Fi link speed** — the negotiated speed between your device and your router. This is decided by distance, walls, congestion, and which band (2.4 or 5 GHz) you're on.

Your actual experience is roughly **the smaller of the two**. If your provider gives you 500 Mbps but your Wi-Fi link to a far bedroom is 60 Mbps, you experience 60 Mbps in that bedroom. Fixing slow Wi-Fi usually means fixing the link, not the subscription.

## Key terms (recap)

You now know more than you need, but hold onto these:

- **Modem**: talks to your provider.
- **Router**: directs your local house network.
- **Local address**: a device's apartment number inside your house.
- **Band**: which radio part of the Wi-Fi you're on (2.4 GHz or 5 GHz).
- **Link speed**: the actual speed between your device and your router.

On to the question that brought most people here: [why Wi-Fi is slow](02-why-wifi-is-slow.md).
