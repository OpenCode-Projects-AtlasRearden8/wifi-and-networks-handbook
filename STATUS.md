# STATUS.md — The Calm Home Network Handbook

Last updated: 2026-10-25

## What was built

A complete, local-first beginner manual on home networking, written in a calm, plain-English tone, plus a dependency-free build pipeline that turns it into a polished static HTML site.

### Content (Markdown in `docs/`)

- `index.md` — start-here page: audience, calm precepts, how to use the handbook.
- `01-how-your-network-works.md` — modem / router / switch / Wi-Fi in plain English; the difference between internet speed and Wi-Fi link speed.
- `02-why-wifi-is-slow.md` — honest ranked causes (distance/walls, wrong band, neighbor congestion, housemates' devices, old hardware, provider); what slow Wi-Fi usually is *not*; a two-test diagnosis.
- `03-router-placement-and-channels.md` — center/elevated placement rules, channel picking (1/6/11), ethernet advice, extender and powerline options.
- `04-24-vs-5-ghz.md` — band trade-offs table, which devices belong on which band, band steering, how to check/split bands, brief 6 GHz note.
- `05-passwords-and-guest-networks.md` — password shapes, the three passwords and their personalities, guest network setup, WPS off, what to skip.
- `06-what-a-vpn-actually-does.md` — one-paragraph definition, what VPNs don't do, honest cases, when to skip, self-hosted note, how to pick.
- `07-parental-controls.md` — four layers (router/DNS/device/app) with honest limitations, calm conversation script, 30-minute setup order.
- `08-when-the-internet-drops.md` — ordered calm outage procedure (check two devices/sets, read router lights, proper power-cycle, device reconnect, outage lookup, effective support call), incident-log advice, tethering fallback.
- `09-router-admin-page.md` — finding and signing into the admin page, a "tour" of the five rooms that matter, what never to touch, three safe habits.
- **Tools:** `network-map-worksheet.md` (printable census + numbers-you-should-know + incident log), `troubleshooting-flowchart.md` (branching decision flow for outages and slowness), `glossary.md` (all jargon translated).

### Build pipeline

- `build/build.py` — pure standard-library Python (3.10+). Converts the Markdown (headings, inline styles, fenced code, tables, nested/ordered/checkbox lists, blockquotes, fill-in-the-blank underscore fields) into per-page HTML with shared nav, footer, and stylesheet. Rewrites internal `.md` links to `.html`.
- `build/assets/style.css` — calm serif/sans stylesheet with warm palette, blockquote/table styling, printable worksheets, responsive layout.
- `--check` mode: builds, then verifies (a) every internal link resolves to a real file and (b) every generated page has well-formed, balanced HTML structure.
- `tests/test_build.py` — 30 pytest tests covering the converter unit-level (including escaping and edge cases), link rewriting/checking, HTML structure validation, the full build output, chapter inventory, and a no-secrets scan of `docs/`.

### Meta files

- `README.md` — overview, build/run instructions, credit to Asdale Dynamics, LLC.
- `LICENSE` — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `.gitignore` — ignores `site/` (reproducible output) and Python caches.

## How to run it

```bash
python3 build/build.py          # build static site into site/
python3 build/build.py --check  # build + link check + HTML structure check
python3 -m pytest tests/ -q     # run the 30-test suite
# then open site/index.html in any browser — fully static, no server needed
```

## Verification results

- `python3 build/build.py --check` → builds **13 pages** + stylesheet; **link check passed; HTML structure check passed.**
- `python3 -m pytest tests/ -q` → **30 passed, 0 failed.**
- Every generated page parsed with an HTML tag-balance validator: **no mismatches, no unclosed tags.**
- Internal-link scan: **no `.md` links remain in generated HTML** and no broken targets.
- No secrets/API keys/personal data in `docs/` or `build/` (scanned by a test that runs on every pytest run).
- Manual spot-checks of rendered output for tables, checkboxes, nested lists, fill-in blanks, and blockquotes all render correctly.

## Known gaps and intentional limits

- **Not a mesh/product-by-product guide** — concepts apply to any brand; brand-specific admin screens vary in naming/looks.
- **Wi-Fi analyzer apps are not included** — channel picking needs a third-party app on your phone (free ones exist; iOS is more limited than Android); no app is bundled.
- **PDF/EPUB output not provided** — the site's print stylesheet covers printing worksheets and the flowchart; a full PDF/EPUB export build is possible future work.
- **Footer link points to a live hub site** (`dylanasdale.github.io`): harmless offline (dead link if offline), and the site itself makes no network calls.
- **Search**: the site has no search box; it relies on nav, glossary, and chapter links.
- The troubleshooting flowchart is rendered as styled text/lists rather than a graphical diagram; it's deliberately printable and dependency-free.

## Housekeeping

- Repository: local only. Git initialized with a single plain commit; nothing pushed, no remotes, nothing published.
- The steady-state workflow for edits: change `docs/*.md`, run `python3 build/build.py --check`, run tests, done.
