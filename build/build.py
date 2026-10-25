#!/usr/bin/env python3
"""Build the Calm Home Network Handbook as a static HTML site.

Reads Markdown files from docs/, converts them to HTML (no external
dependencies), and writes a self-contained static site to site/.

Usage:
    python3 build/build.py            # build the site
    python3 build/build.py --check    # build, then verify links resolve
    python3 build/build.py --clean    # remove the site/ directory and exit

Every page gets the same calm stylesheet, a top nav, a breadcrumb of where
you are, and a footer crediting Asdale Dynamics, LLC.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = ROOT / "build" / "assets"

SITE_TITLE = "The Calm Home Network Handbook"

CHAPTER_TITLES = {
    "index.md": "Start here",
    "01-how-your-network-works.md": "1. How your network works",
    "02-why-wifi-is-slow.md": "2. Why Wi-Fi is slow",
    "03-router-placement-and-channels.md": "3. Placement & channels",
    "04-24-vs-5-ghz.md": "4. 2.4 vs 5 GHz",
    "05-passwords-and-guest-networks.md": "5. Passwords & guests",
    "06-what-a-vpn-actually-does.md": "6. What a VPN does",
    "07-parental-controls.md": "7. Parental controls",
    "08-when-the-internet-drops.md": "8. When it drops",
    "09-router-admin-page.md": "9. Router admin page",
    "network-map-worksheet.md": "Network map worksheet",
    "troubleshooting-flowchart.md": "Flowchart",
    "glossary.md": "Glossary",
}


# --------------------------------------------------------------------------
# Minimal Markdown -> HTML
# --------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Render inline markdown (code, bold, italic, links)."""
    placeholders: list[str] = []

    def stash(html_fragment: str) -> str:
        placeholders.append(html_fragment)
        return f"\x00{len(placeholders) - 1}\x00"

    # Protect fenced inline code first so its contents aren't re-processed.
    def code_sub(match: re.Match) -> str:
        return stash(f"<code>{html.escape(match.group(2))}</code>")

    text = re.sub(r"(`+)(.+?)\1", code_sub, text)

    # Images: ![alt](src)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)\)",
        lambda m: stash(
            f'<img src="{html.escape(m.group(2), quote=True)}" '
            f'alt="{html.escape(m.group(1), quote=True)}">'
        ),
        text,
    )
    # Links: [text](target)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}">'
            f"{m.group(1)}</a>"
        ),
        text,
    )

    # Now escape everything that remains so raw &, <, > are safe.
    text = html.escape(text, quote=False)

    # Runs of underscores are fill-in-the-blank fields, not emphasis.
    text = re.sub(
        r"_{2,}",
        lambda m: stash('<span class="blank-fill" aria-label="fill in here"></span>'),
        text,
    )

    # Bold / italic before plain emphasis so "***" resolves sensibly.
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"<em>\1</em>", text)

    # Restore stashed fragments.
    for i, fragment in enumerate(placeholders):
        text = text.replace(f"\x00{i}\x00", fragment)
    return text


def _extract_title(md_text: str) -> tuple[str, str]:
    lines = md_text.splitlines()
    if lines and lines[0].startswith("# "):
        return lines[0][2:].strip(), "\n".join(lines[1:])
    return "", md_text


def markdown_to_html(md_text: str) -> str:
    """Convert the subset of Markdown used by this handbook to HTML."""
    title, body = _extract_title(md_text)
    md_text = body

    out: list[str] = []
    if title:
        out.append(f"<h1>{_inline(title)}</h1>")

    lines = md_text.split("\n")
    i = 0
    n = len(lines)

    def close_list(tag: str) -> None:
        if out and out[-1] != f"</{tag}>":
            out.append(f"</{tag}>")

    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Fenced code block
        if line.strip().startswith("```"):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # closing fence
            out.append(
                "<pre><code>"
                + html.escape("\n".join(code_lines))
                + "</code></pre>"
            )
            continue

        # Horizontal rule
        if re.fullmatch(r"(---+|\*\*\*+|___+)\s*", line):
            out.append("<hr>")
            i += 1
            continue

        # Headings
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            out.append(
                f"<h{level}>{_inline(heading.group(2).strip())}</h{level}>"
            )
            i += 1
            continue

        # Blockquote (collect consecutive > lines)
        if line.lstrip().startswith(">"):
            quote_lines = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{markdown_to_html_inner(quote_lines)}</blockquote>")
            continue

        # Table
        if "|" in line and i + 1 < n and re.fullmatch(r"\s*\|[\s:|-]+\|\s*", lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                cells += [""] * (len(header) - len(cells))
                rows.append(cells)
                i += 1
            table = ["<table>", "<thead>", "<tr>"]
            for cell in header:
                table.append(f"<th>{_inline(cell)}</th>")
            table += ["</tr>", "</thead>", "<tbody>"]
            for row in rows:
                table.append("<tr>")
                for cell in row:
                    table.append(f"<td>{_inline(cell)}</td>")
                table.append("</tr>")
            table += ["</tbody>", "</table>"]
            out.append("".join(table))
            continue

        # Lists (unordered / ordered / checkbox), nested by indentation.
        list_match = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if list_match:
            tag = "ol" if re.match(r"\d+\.", list_match.group(2)) else "ul"
            items, i = collect_list_items(lines, i)
            out.append(render_list_block(items, tag=tag))
            continue

        # Paragraph
        para_lines = []
        while i < n and lines[i].strip() and not re.match(
            r"^(#{1,6}\s|```|\s*[-*+]\s|\s*\d+\.\s|\s*>|\s*\||---+\s*\*?\s*$)", lines[i]
        ):
            para_lines.append(lines[i].strip())
            i += 1
        out.append(f"<p>{'<br>'.join(_inline(pl) for pl in para_lines)}</p>")

    return "\n".join(part for part in out if part)


def markdown_to_html_inner(lines: list[str]) -> str:
    """Render a pre-filtered block of lines (used for blockquotes)."""
    return markdown_to_html("\n".join(lines))


# --------------------------------------------------------------------------
# Site assembly
# --------------------------------------------------------------------------

def render_list_item(raw: str) -> str:
    """Render one list item's text, recognizing checkbox syntax - [ ] / - [x]."""
    check = re.match(r"^\[([ xX])\]\s*(.*)$", raw)
    if check:
        checked = " checked" if check.group(1).lower() == "x" else ""
        return (f'<span class="check-item">'
                f'<input type="checkbox" disabled{checked}>'
                f"{_inline(check.group(2))}</span>")
    return _inline(raw)


def collect_list_items(
    lines: list[str], start: int, base_indent: int = 0
) -> tuple[list[tuple[int, str]], int]:
    """Collect (indent_depth, text) tuples for a list starting at lines[start].

    A marker line at the same indent as the first continues the list as a
    sibling; deeper indents become nested items; an indented non-marker line
    is treated as a continuation of the previous item's text. The list ends
    at a non-indented non-marker line, or at a blank line followed by such.
    """
    marker = re.compile(r"^(\s*)([-*+]|\d+\.)\s+(.*)$")
    n = len(lines)
    first = marker.match(lines[start])
    assert first is not None
    base = len(first.group(1)) or base_indent
    items: list[tuple[int, str]] = [(0, first.group(3))]
    i = start + 1
    while i < n:
        # Skip blank lines only if the list continues after them.
        if not lines[i].strip():
            j = i
            while j < n and not lines[j].strip():
                j += 1
            if j >= n:
                break
            m = marker.match(lines[j])
            continues = m is not None and len(m.group(1)) >= base
            if not continues:
                break
            i = j
            continue
        m = marker.match(lines[i])
        indent = len(lines[i]) - len(lines[i].lstrip())
        if m is not None:
            if indent < base:
                break  # outer level: belongs to an enclosing list
            depth = (indent - base) // 2
            items.append((depth, m.group(3)))
            i += 1
            continue
        if indent >= base + 2 or lines[i].startswith("\t"):
            # Indented continuation of the previous item.
            depth, text = items[-1]
            items[-1] = (depth, text + " " + lines[i].strip())
            i += 1
            continue
        break  # non-indented, non-marker: the list is over
    return items, i


def render_list_block(items: list[tuple[int, str]], tag: str = "ul") -> str:
    """Render (depth, text) items as a properly nested HTML list."""
    parts: list[str] = []
    level = items[0][0] if items else 0
    idx = 0
    while idx < len(items):
        depth, text = items[idx]
        if depth > level:
            # Should not happen at top call; children handled below.
            idx += 1
            continue
        parts.append("<li>" + render_list_item(text))
        children: list[tuple[int, str]] = []
        while idx + 1 < len(items) and items[idx + 1][0] > depth:
            idx += 1
            children.append((items[idx][0] - depth - 1, items[idx][1]))
        if children:
            parts.append(render_list_block(children, tag=tag))
        parts.append("</li>")
        idx += 1
    return "<" + tag + ">" + "".join(parts) + "</" + tag + ">"


def render_list_item(raw: str) -> str:
    """Render one list item's text, recognizing checkbox syntax - [ ] / - [x]."""
    check = re.match(r"^\[([ xX])\]\s*(.*)$", raw)
    if check:
        checked = " checked" if check.group(1).lower() == "x" else ""
        return (f'<span class="check-item">'
                f'<input type="checkbox" disabled{checked}>'
                f"{_inline(check.group(2))}</span>")
    return _inline(raw)


def slug_for(md_path: Path) -> str:
    return md_path.stem + ".html"


def relative_links(html_text: str) -> str:
    """Rewrite internal .md hrefs to .html (leaving http(s) links untouched)."""
    def repl(match: re.Match) -> str:
        target = match.group(1)
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            return match.group(0)
        return match.group(0).replace(f"{target}.md", f"{target}.html")

    return re.sub(r'href="([^"]+)\.md"', repl, html_text)


def page_shell(title: str, content_html: str, pages: dict[Path, str]) -> str:
    nav_items = []
    for path, label in pages.items():
        href = slug_for(path)
        nav_items.append(f'<a href="{href}">{html.escape(label)}</a>')
    nav = "".join(f'<li>{item}</li>' for item in nav_items)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A plain-English manual explaining home networks calmly: slow Wi-Fi, router placement, 2.4 vs 5 GHz, passwords, guest networks, VPNs, parental controls, and outages.">
<title>{html.escape(title)} — {SITE_TITLE}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html">{SITE_TITLE}</a>
  <p class="tagline">Plain English, step by step, never condescending.</p>
</header>
<nav class="site-nav"><ul>{nav}</ul></nav>
<main class="content">
{content_html}
</main>
<footer class="site-footer">
  <p>The Calm Home Network Handbook — built local-first by Asdale Dynamics, LLC.</p>
  <p>MIT licensed. No tracking, no analytics, no network calls: this site is static and yours to keep.</p>
</footer>
</body>
</html>
"""


def build_site(clean: bool = False) -> list[Path]:
    written: list[Path] = []

    if clean and SITE.exists():
        shutil.rmtree(SITE)
    if not DOCS.exists():
        raise SystemExit(f"docs/ directory not found at {DOCS}")

    md_files = sorted(
        p for p in DOCS.glob("*.md")
        if p.name.lower() != "readme.md"
    )
    if not md_files:
        raise SystemExit("No markdown files found in docs/")

    # Order pages for the nav: index first, chapters in order, specials last.
    def nav_key(path: Path):
        if path.name == "index.md":
            return (0, "")
        titles = list(CHAPTER_TITLES.keys())
        if path.name in titles:
            return (1, titles.index(path.name))
        return (2, path.name)

    md_files.sort(key=nav_key)
    pages = {p: CHAPTER_TITLES.get(p.name, p.stem.replace("-", " ").title())
             for p in md_files}

    SITE.mkdir(exist_ok=True)
    assets_dir = SITE / "assets"
    assets_dir.mkdir(exist_ok=True)

    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    (assets_dir / "style.css").write_text(css, encoding="utf-8")
    written.append(assets_dir / "style.css")

    for md in md_files:
        md_text = md.read_text(encoding="utf-8")
        title, body = _extract_title(md_text)
        if not title:
            title = pages[md]
        content_html = relative_links(markdown_to_html(body))
        href = slug_for(md)
        full = page_shell(title, content_html, pages)
        out = SITE / href
        out.write_text(full, encoding="utf-8")
        written.append(out)

    return written


def check_site(written: list[Path]) -> list[str]:
    """Verify every internal link on every built page resolves to a real file."""
    errors: list[str] = []
    for page in written:
        if page.suffix != ".html":
            continue
        text = page.read_text(encoding="utf-8")
        for match in re.finditer(r'href="([^"]+)"', text):
            target = match.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            if target.startswith("#"):
                continue
            resolved = (page.parent / Path(target)).resolve()
            if not resolved.exists():
                errors.append(f"{page.name}: broken link -> {target}")
    return errors


def check_html_structure(written: list[Path]) -> list[str]:
    """Verify every built page has well-formed, balanced tag nesting."""
    from html.parser import HTMLParser

    void_tags = {"meta", "link", "input", "hr", "br", "img"}

    class _Validator(HTMLParser):
        def __init__(self) -> None:
            super().__init__(convert_charrefs=True)
            self.stack: list[str] = []
            self.errors: list[str] = []

        def handle_starttag(self, tag: str, attrs) -> None:
            if tag not in void_tags:
                self.stack.append(tag)

        def handle_endtag(self, tag: str) -> None:
            if not self.stack:
                self.errors.append(f"</{tag}> without an open tag")
                return
            if self.stack[-1] == tag:
                self.stack.pop()
                return
            if tag in self.stack:
                self.errors.append(
                    f"</{tag}> closes past <{self.stack[-1]}>"
                )
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                self.stack.pop()
            else:
                self.errors.append(f"</{tag}> never opened")

    errors: list[str] = []
    for page in written:
        if page.suffix != ".html":
            continue
        validator = _Validator()
        validator.feed(page.read_text(encoding="utf-8"))
        validator.close()
        if validator.errors:
            errors.append(f"{page.name}: {validator.errors[:3]}")
        if validator.stack:
            errors.append(f"{page.name}: unclosed tags {validator.stack}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="build, then verify all internal links resolve")
    parser.add_argument("--clean", action="store_true",
                        help="remove site/ before building")
    args = parser.parse_args(argv)

    if args.clean and not args.check:
        if SITE.exists():
            shutil.rmtree(SITE)
        print("site/ removed.")
        return 0

    written = build_site(clean=args.clean)
    print(f"Built {len(written)-1} pages into site/ (plus stylesheet):")
    for path in written:
        print(f"  {path.relative_to(ROOT)}")

    if args.check:
        problems = check_site(written)
        if problems:
            print("\nLink check FAILED:")
            for problem in problems:
                print(f"  {problem}")
            return 1
        print("\nLink check passed: every internal link resolves.")

        structural = check_html_structure(written)
        if structural:
            print("\nHTML structure check FAILED:")
            for problem in structural:
                print(f"  {problem}")
            return 1
        print("HTML structure check passed: all pages well-formed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
