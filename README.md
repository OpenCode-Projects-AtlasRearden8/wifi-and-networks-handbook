# The Calm Home Network Handbook

A plain-English manual that demystifies home networks — why Wi-Fi is slow, router placement and channels, 2.4 vs 5 GHz, passwords and guest networks, what a VPN actually does, parental controls, fixing outages calmly, and reading your router admin page without fear.

Written the way a friend would explain it: **clear, warm, step by step, never condescending.**

## What's inside

- **`docs/`** — the handbook in Markdown: nine chapters plus a [network map worksheet](docs/network-map-worksheet.md), a [troubleshooting flowchart](docs/troubleshooting-flowchart.md), and a [glossary](docs/glossary.md).
- **`build/build.py`** — a dependency-free Python build script that turns the Markdown into a polished static HTML site in `site/`.
- **`tests/`** — a pytest suite covering the Markdown converter, link checking, and HTML structure validation.
- **`site/`** — the generated site (run the build to create it; kept out of version control because it's reproducible output).

## Build and run it

Requirements: Python 3.10+ (standard library only; no packages to install).

```bash
# Build the static site into site/
python3 build/build.py

# Build, then verify every internal link resolves and every page is well-formed HTML
python3 build/build.py --check

# Run the test suite
python3 -m pytest tests/ -q

# Open the handbook in a browser (macOS/Linux)
python3 -c "import webbrowser; webbrowser.open('file://site/index.html')"
# or simply open site/index.html in any browser
```

No server needed. The site is fully static: open `site/index.html` from disk, put it on any static host you own, or carry the folder on a USB stick. It makes no network calls, has no analytics, and collects nothing.

## Who it's for

Anyone whose home network feels like a box of mystery — renters, parents, small households, people who've been nodding politely at "try the 5 GHz one." Start with `docs/index.md`.

## Credit

Created and published by **Asdale Dynamics, LLC** — plain-English beginner manuals, practical tools, and open-source templates. See the author hub at <https://dylanasdale.github.io>.

## License

MIT — see [LICENSE](LICENSE).
