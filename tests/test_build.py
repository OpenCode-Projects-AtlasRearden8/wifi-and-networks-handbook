"""Tests for the Calm Home Network Handbook build.

Run with:  python3 -m pytest tests/ -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT / "build"))
import build as builder  # noqa: E402


# --------------------------------------------------------------------------
# Markdown converter
# --------------------------------------------------------------------------

def test_heading_levels():
    html_text = builder.markdown_to_html("# Big\n\n## Small\n\n### Tiny")
    assert "<h1>Big</h1>" in html_text
    assert "<h2>Small</h2>" in html_text
    assert "<h3>Tiny</h3>" in html_text


def test_title_line_replaced_by_h1():
    html_text = builder.markdown_to_html("# My Title\n\nBody text.")
    assert html_text.count("<h1>") == 1
    assert "My Title" in html_text
    assert "<p>Body text.</p>" in html_text


def test_paragraph_and_hard_break():
    html_text = builder.markdown_to_html("line one\nline two")
    assert "<p>line one<br>line two</p>" in html_text


def test_inline_formatting():
    html_text = builder.markdown_to_html("a **bold** and *thin* and `code` thing")
    assert "<strong>bold</strong>" in html_text
    assert "<em>thin</em>" in html_text
    assert "<code>code</code>" in html_text


def test_emphasis_does_not_swallow_underscores_in_words():
    html_text = builder.markdown_to_html("snake_case_name stays")
    assert "snake_case_name" in html_text
    assert "<em>" not in html_text


def test_raw_html_is_escaped():
    html_text = builder.markdown_to_html("evil <script>alert(1)</script> bit")
    assert "<script>" not in html_text
    assert "&lt;script&gt;" in html_text


def test_links_render_and_survive_escaping():
    html_text = builder.markdown_to_html("see [the guide](guide.md) now")
    assert '<a href="guide.md">the guide</a>' in html_text


def test_unordered_list():
    html_text = builder.markdown_to_html("- one\n- two\n- three")
    assert "<ul>" in html_text and "</ul>" in html_text
    assert html_text.count("<li>") == 3


def test_ordered_list():
    html_text = builder.markdown_to_html("1. one\n2. two")
    assert "<ol>" in html_text and "</ol>" in html_text


def test_nested_list():
    html_text = builder.markdown_to_html("- outer\n  - inner\n- outer2")
    assert html_text.count("<ul>") == 2
    assert "<li>inner</li>" in html_text


def test_checkbox_list_item():
    html_text = builder.markdown_to_html("- [ ] unchecked\n- [x] checked")
    assert 'type="checkbox" disabled>' in html_text
    assert 'disabled checked>' in html_text


def test_table():
    md = "| a | b |\n| --- | --- |\n| 1 | 2 |"
    html_text = builder.markdown_to_html(md)
    assert "<table>" in html_text
    assert "<th>a</th>" in html_text
    assert "<td>2</td>" in html_text


def test_table_cells_carry_inline_links():
    md = "| a | b |\n| --- | --- |\n| [x](y.md) | z |"
    html_text = builder.markdown_to_html(md)
    assert 'href="y.md"' in html_text


def test_blockquote():
    html_text = builder.markdown_to_html("> a calm quote\n> continues")
    assert "<blockquote>" in html_text
    assert "calm quote" in html_text


def test_fenced_code_block_is_escaped():
    md = "```\n<script>&ok\n```"
    html_text = builder.markdown_to_html(md)
    assert "&lt;script&gt;&amp;ok" in html_text
    assert "<script>" not in html_text


def test_horizontal_rule():
    assert "<hr>" in builder.markdown_to_html("above\n\n---\n\nbelow")


def test_ampersand_escaped_outside_links():
    html_text = builder.markdown_to_html("rock & roll place")
    assert "&amp;" in html_text


# --------------------------------------------------------------------------
# Link rewriting and checking
# --------------------------------------------------------------------------

def test_relative_links_rewrites_md_hrefs_only():
    source = (
        '<a href="glossary.md">g</a>'
        '<a href="site.html">s</a>'
        '<a href="https://example.com/x.md">t</a>'
        '<a href="#anchor">a</a>'
    )
    result = builder.relative_links(source)
    assert 'href="glossary.html"' in result
    assert 'href="site.html"' in result           # untouched
    assert 'href="https://example.com/x.md"' in result  # external stays
    assert 'href="#anchor"' in result


def test_check_site_reports_broken_links(tmp_path):
    good = tmp_path / "good.html"
    good.write_text('<a href="missing.html">oops</a>', encoding="utf-8")
    errors = builder.check_site([good])
    assert errors and "missing.html" in errors[0]


def test_check_site_passes_when_links_resolve(tmp_path):
    good = tmp_path / "good.html"
    good.write_text(
        '<a href="other.html">ok</a> '
        '<a href="https://example.com">ext</a> '
        '<a href="assets/style.css">css</a>',
        encoding="utf-8",
    )
    other = tmp_path / "other.html"
    other.write_text("hello", encoding="utf-8")
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "style.css").write_text("body{}", encoding="utf-8")
    assert builder.check_site([good, other]) == []


# --------------------------------------------------------------------------
# Full build against the real docs
# --------------------------------------------------------------------------

@pytest.fixture(scope="module")
def built_site(tmp_path_factory):
    site_dir = tmp_path_factory.mktemp("sitecheck")
    original_site = builder.SITE
    builder.SITE = site_dir
    try:
        written = builder.build_site()
    finally:
        builder.SITE = original_site
    return written


def test_build_writes_expected_pages(built_site):
    names = {p.name for p in built_site if p.suffix == ".html"}
    assert "index.html" in names
    assert "glossary.html" in names
    assert "troubleshooting-flowchart.html" in names
    assert "network-map-worksheet.html" in names
    assert "09-router-admin-page.html" in names
    assert len(names) == 13


def test_build_includes_stylesheet(built_site):
    css_pages = [p for p in built_site if p.suffix == ".css"]
    assert len(css_pages) == 1
    assert css_pages[0].read_text(encoding="utf-8").strip()


def test_built_docs_pass_link_check(built_site):
    assert builder.check_site(built_site) == []


def test_built_docs_have_wellformed_html(built_site):
    assert builder.check_html_structure(built_site) == []


def test_check_html_structure_flags_mislabeled_nesting(tmp_path):
    bad = tmp_path / "bad.html"
    bad.write_text("<main><p><strong>x</em></p></main>", encoding="utf-8")
    errors = builder.check_html_structure([bad])
    assert errors and "bad.html" in errors[0]


def test_every_built_page_has_nav_and_footer(built_site):
    for page in built_site:
        if page.suffix != ".html":
            continue
        text = page.read_text(encoding="utf-8")
        assert "The Calm Home Network Handbook" in text
        assert "Asdale Dynamics, LLC" in text
        assert text.strip().endswith("</html>")


def test_built_pages_link_to_html_not_md(built_site):
    for page in built_site:
        if page.suffix != ".html":
            continue
        for href in simple_hrefs(page):
            if href.endswith(".md"):
                pytest.fail(f"{page.name} still links to a .md file: {href}")


def simple_hrefs(page: Path) -> list[str]:
    import re
    return re.findall(r'href="([^"]+\.md)"', page.read_text(encoding="utf-8"))


def test_site_title_is_on_every_page(built_site):
    for page in built_site:
        if page.suffix == ".html":
            assert "The Calm Home Network Handbook" in page.read_text(
                encoding="utf-8"
            )


def test_chapter_titles_map_defined():
    expected = [
        "index.md", "01-how-your-network-works.md", "02-why-wifi-is-slow.md",
        "03-router-placement-and-channels.md", "04-24-vs-5-ghz.md",
        "05-passwords-and-guest-networks.md", "06-what-a-vpn-actually-does.md",
        "07-parental-controls.md", "08-when-the-internet-drops.md",
        "09-router-admin-page.md", "network-map-worksheet.md",
        "troubleshooting-flowchart.md", "glossary.md",
    ]
    for name in expected:
        assert (ROOT / "docs" / name).exists(), f"missing doc: {name}"
        assert name in builder.CHAPTER_TITLES


def test_no_secrets_in_docs():
    secret_markers = [
        "api_key", "API_KEY", "sk-", "password = ", "BEGIN PRIVATE KEY",
        "ghp_", "AKIA",
    ]
    for md in (ROOT / "docs").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for marker in secret_markers:
            assert marker not in text, f"{md.name} contains marker {marker}"
