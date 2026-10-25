# Chapter 3 — Router placement and channels

Two completely different problems share this chapter because they get fixed with two completely different actions: **where you put the router** (a one-time physical fix) and **which channel it broadcasts on** (a five-minute setting).

## Placement: the physics one

Wi-Fi doesn't shine like a laser; it spreads like a lamp. Two rules follow from that:

1. **Center beats corner.** Your router sitting in a corner wastes signal in the direction of the corner (the wall outside your house) and shortchanges the far corner of your home. A router in the middle of the house lamp-lights everything.
2. **High beats low.** Wi-Fi travels nicely through open air and gets absorbed by furniture, floors, stacks of books, and people. A router on the floor behind a couch is like trying to light a room with a desk lamp under a blanket. Put it as close to ceiling-height as your cable allows — a high shelf is nearly perfect.

### Placement rules, in practical order

1. **Center of the house, at eye level or higher.** This alone can double your Wi-Fi speed.
2. **Free space around it.** At least a foot of open air on all sides. Wi-Fi doesn't penetrate mattresses or filing cabinets.
3. **Not inside a metal object.** TV stand, metal hamper, metal shelf, fridge. These block the signal completely.
4. **Not at ground level.** The floor absorbs a lot.
5. **Away from other electronics.** Speakers, TVs, big chargers, your television's cable box — these add their own quiet radio noise.
6. **Don't hide it.** You can hide a router from view with a wicker basket or an open shelf, as long as the basket isn't metal and the router has air.

### Things that are also placement problems but don't seem like it

- **Televisions sitting directly on top of a router.** Common, quietly terrible.
- **Aquariums.** Water absorbs Wi-Fi. Don't put the router on top of the fish tank.
- **Mirrors and big picture frames.** They quietly reflect Wi-Fi and effectively "bounce" it away from where you wanted it to go.

### Elevate vs. centralize

You sometimes can't have both. If you must pick one:

- Pick **central**. It roughly matters twice as much as height, all else equal.
- A router on a bookshelf in a central room is fine, even if it's not on the ceiling.
- If your house is shaped like an L, place the router near the inside corner of the L, and consider a cheap Wi-Fi extender in a far room later (or better, an ethernet cable run — but that's its own project).

## Channels: the "everyone else's router" fix

Wi-Fi is divided into **channels** — numbered slots, like lanes on a highway. Your router broadcasts on one.

On the 2.4 GHz band, there are only about three usable channels in most real homes: **1, 6, and 11**. (Yes, the numbers jump — the channels overlap, so only every fourth one is actually independent.) Most consumer routers default to **channel 6**, which means **most routers in your apartment building are shouting on the same lane**.

If your neighbors' routers share your channel, they each take turns speaking, and everyone gets slower.

### How to pick a better channel

You have two levels of effort here.

**Level 1 — let your router pick (and hope it's smart).**
Some modern routers have auto-channel selection that actually works. If your router is recent, setting the channel to "Auto" is the correct choice. Test it: if your speed is fine, you're done.

**Level 2 — pick it yourself with a phone app.**
This works when your router's auto mode is lazy (many older ones are).

1. Install a free Wi-Fi analyzer app (Android has several good ones; iOS has fewer because Apple restricts the scanning, but a few exist).
2. Open it, and look at the 2.4 GHz list. Count how many networks are on channels 1, 6, and 11.
3. Choose the channel that has the **fewest strong neighbors** (not the fewest total, the fewest *strong* ones — a channel two floors away barely matters).
4. In your router's admin page, set the 2.4 GHz band to that channel. See [chapter 9](09-router-admin-page.md) if the admin page makes you nervous.

**Do not** contort your network onto channel 8 or 13 "because it has fewer names." Channels in the middle overlap neighbors 1, 6, and 11, causing the same slowdown. Stick with 1, 6, and 11.

### 5 GHz channels are not much of a problem

On 5 GHz there are many more channels than neighbors, so channel picking rarely matters on that band. Use "Auto" there. It's fine.

## One more physical fix: ethernet cables

Seriously, this is the whole list of things ethernet is better at:

- Faster than Wi-Fi in almost every real house.
- Zero packet loss, near-zero latency.
- Stable for anything that doesn't move: TVs, desktops, game consoles, home offices, streaming devices.

If there's one device in your home that sits still and matters, run a cable to it. A 25-foot ethernet cable is under $15 and feels luxurious. Cable along a wall or under a rug is fine.

## When placement can't be fixed

Sometimes your modem outlet is pinned in a corner of an apartment and rewiring is not happening. What to do:

- **Move an extender halfway.** Place a Wi-Fi extender (or a cheap mesh node) somewhere in the *middle*, not at the edge. Placing it at the far edge is a very common mistake: the extender then relays a weak signal with a weak signal.
- **Consider powerline adapters.** These send network data over your electrical wiring. Quality varies house to house, but in many homes they're decent. Cheap, worth trying.
- **Run a long flat Ethernet cable under a rug.** Ugly but effective. You don't have to.

This chapter is done. Now the sister problem: [2.4 vs 5 GHz](04-24-vs-5-ghz.md).
