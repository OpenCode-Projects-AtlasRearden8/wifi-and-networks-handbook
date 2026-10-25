# Chapter 2 — Why Wi-Fi is slow

Slow Wi-Fi is almost never one mysterious cause. It's usually one of a short list of boring causes, in roughly this order of likelihood.

## The honest list, most likely first

### 1. Distance and walls (by far the #1 cause)

Wi-Fi signals weaken with every meter and every wall. Distance is a contract you didn't sign but pay for anyway.

- Wi-Fi twice as far away can be much less than half as fast — signal strength drops fast.
- Each interior wall subtracts from your speed. Bathroom walls, kitchen backsplashes, and anything with metal (fridge, steel studs, mirror) subtract more.
- Wi-Fi bounces. Sometimes standing in a slightly different spot (even one step) measurably changes your speed. That's physics, not superstition.

**Fix:** move the router to a central, elevated spot; reduce the number of walls between it and wherever you actually use the internet. See [chapter 3](03-router-placement-and-channels.md).

### 2. You're on the wrong band

The 2.4 GHz band travels farther but is slower and much more crowded. The 5 GHz band is faster but travels less far. A device that "should" get 300 Mbps might be sitting on 2.4 GHz out of habit. See [chapter 4](04-24-vs-5-ghz.md).

### 3. Wi-Fi congestion (your neighbors' router)

In an apartment or a dense neighborhood, the air contains broadcasts from every Wi-Fi router within about 100 meters. All those uncles and students and printers are shouting in the same room.

The consequences:

- Your Wi-Fi has to wait its turn before it can talk. That's latency, not bandwidth, but it shows up the same way: things feel slow.
- Multiple routers sitting on the same channel will slow each other down — often each by half. See [channel picking in chapter 3](03-router-placement-and-channels.md).

**Fix:** pick a cleaner channel. Apartment dwellers: this is often worth a full 50% speed increase.

### 4. Devices on the network actually using the internet

Before you blame Wi-Fi, check what everyone else is doing:

- A TV downloading a game update in the background can eat an entire home connection.
- A backup service quietly syncing your photos.
- A guest watching 4K YouTube in another room.
- A smart plug or camera stuck in a retry loop and sending the same 1-second clip every few seconds.

**Fix:** ask the house, or check the list of connected devices on your router's admin page (see [chapter 9](09-router-admin-page.md)). This is where your [network map worksheet](network-map-worksheet.md) earns its keep.

### 5. Old Wi-Fi standards (your device, not your router)

Wi-Fi has versions. Your router might be modern, but if your laptop is a 2013 model, it's negotiating at an older, slower protocol.

- Everything supports the old bands, so old devices *work* — just not fast.
- One slow device in the house doesn't usually slow down the others on a modern router, but its own experience will be slow, and it can confuse you when you measure.

**Fix:** test speed using your newest phone. It has the best Wi-Fi radio in the house. If the newest phone is fast, your Wi-Fi is fine — the slow device is just old. That's a hardware limit, not a fixable network problem.

### 6. Your provider actually delivered less than promised

Real but less common than people think. Routers, cables, and wall jacks do go bad. Test with a **cable plugged directly into the router** with everything else quiet, at a time when the house is empty. See [chapter 8](08-when-the-internet-drops.md).

### 7. Your provider is throttling or shaping your connection

Rarer still, and mostly irrelevant on residential connections in ordinary use. If you consistently get less than what you pay for over cable, with no other devices active, call your provider — politely but insistently.

## What slow Wi-Fi usually *isn't*

To save you some time, these usually aren't the problem:

- **Your device "needing a restart."** Sometimes, but it's rarely the fix.
- **Interference from a microwave.** Real, and citable, but a 2020s router and a 2010s microwave rarely still fight. Skip this theory unless your Wi-Fi drops *only* while someone microwaves popcorn at lunch.
- **Your provider "capping" you.** Most residential plans aren't bandwidth-shaped in a way you'd feel on a daily basis.
- **Viruses or malware.** Possible. Very, very unlikely to be Wi-Fi-specific.

## A calm approach

1. Test speed with your newest phone, standing one step away from the router.
2. Then test in the room where it feels slow.
3. If the near-router speed is fine and the far-room speed is bad, the problem is placement, band, or walls — chapters [3](03-router-placement-and-channels.md) and [4](04-24-vs-5-ghz.md).
4. If even the near-router speed is bad, the problem is the router, the provider, or congestion — chapters [8](08-when-the-internet-drops.md) and [9](09-router-admin-page.md).

That one test — near and far, newest device — answers more than any other single measurement you can make.
