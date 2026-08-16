#!/usr/bin/env python3
"""Build an Elementor 0.4 page template from version-d2-refined.html."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D2 = ROOT / "version-d2-refined.html"
CK = Path("/tmp/ck-form.html")
OUT = ROOT / "elementor-whats-new-d2.json"
README = ROOT / "ELEMENTOR-IMPORT.md"

N = 0


def eid(label: str) -> str:
    global N
    N += 1
    return hashlib.md5(f"lll-d2-{label}-{N}".encode()).hexdigest()[:7]


def widget(wtype: str, settings: dict, title: str = "") -> dict:
    s = dict(settings)
    if title:
        s["_title"] = title
    return {
        "id": eid(wtype),
        "elType": "widget",
        "widgetType": wtype,
        "isInner": False,
        "settings": s,
        "elements": [],
    }


def container(settings: dict, children: list, inner: bool = False, title: str = "") -> dict:
    s = dict(settings)
    if title:
        s["_title"] = title
    return {
        "id": eid("container"),
        "elType": "container",
        "isInner": inner,
        "settings": s,
        "elements": children,
    }


def html_widget(html: str, title: str) -> dict:
    return widget(
        "html",
        {
            "html": html,
            "ha_advanced_tooltip_content": "I am a tooltip",
            "ha_cmc_text": "Happy Addons",
        },
        title,
    )


def prefix_selectors(selector_block: str, scope: str) -> str:
    parts = []
    for sel in selector_block.split(","):
        sel = sel.strip()
        if not sel:
            continue
        if sel.startswith("@") or sel.startswith(scope) or sel.startswith(":root"):
            parts.append(sel)
            continue
        if sel in ("html", "body"):
            parts.append(scope)
            continue
        if sel == "*" or sel.startswith("*::") or sel.startswith("*,"):
            parts.append(f"{scope},{scope} *")
            continue
        if sel.startswith("*"):
            parts.append(f"{scope} {sel}")
            continue
        parts.append(f"{scope} {sel}")
    return ",".join(parts)


def scope_css_chunk(css: str, scope: str, add_base: bool) -> str:
    css = re.sub(r"html\{scroll-behavior:smooth\}", "", css)
    css = css.replace(":root{", f":root,{scope}{{")
    out = []
    i = 0
    while i < len(css):
        if css.startswith("@media", i) or css.startswith("@supports", i):
            brace = css.find("{", i)
            at = css[i : brace + 1]
            depth = 1
            j = brace + 1
            while j < len(css) and depth:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                j += 1
            inner = css[brace + 1 : j - 1]
            out.append(at + scope_css_chunk(inner, scope, False) + "}")
            i = j
            continue
        nxt = css.find("{", i)
        if nxt < 0:
            out.append(css[i:])
            break
        selectors = css[i:nxt]
        depth = 1
        j = nxt + 1
        while j < len(css) and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        body = css[nxt:j]
        stripped = selectors.strip()
        if not stripped or stripped.startswith("@") or stripped.startswith("/*"):
            out.append(selectors + body)
        else:
            comment = ""
            if "*/" in selectors:
                cend = selectors.rfind("*/")
                comment = selectors[: cend + 2]
                selectors = selectors[cend + 2 :]
            out.append(comment + prefix_selectors(selectors, scope) + body)
        i = j
    extra = ""
    if add_base:
        extra = (
            f"{scope}{{margin:0;color:var(--ink);background:var(--bg);"
            f"font-family:var(--sans);line-height:1.65;font-size:22px;font-weight:300}}"
            f"{scope} img{{max-width:100%;height:auto;display:block}}"
            f"{scope} a{{color:inherit}}"
        )
    return extra + "".join(out)


def scope_css(css: str, scope: str = ".lll-whats-new") -> str:
    return scope_css_chunk(css, scope, True)


def extract_d2():
    html = D2.read_text()
    css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
    body = re.sub(r'<div class="design-switcher">.*?</div>', "", body, flags=re.S)
    body = re.sub(r"<footer class=\"wrap footer\">.*?</footer>", "", body, flags=re.S)
    ck = CK.read_text() if CK.exists() else ""
    if ck:
        body = re.sub(
            r'<form class="form" onsubmit="return false">.*?</form>',
            ck,
            body,
            count=1,
            flags=re.S,
        )
    sections = re.findall(r"<section\b.*?</section>", body, flags=re.S)
    return css, sections


SECTION_TITLES = [
    "Hero",
    "Intro",
    "Spotlight",
    "Partners",
    "Education header",
    "Education grid",
    "Newsletter",
    "Discussions header",
    "Discussions grid",
    "Survivors",
    "Blogs",
]


def boxed() -> dict:
    return {
        "content_width": "full",
        "flex_direction": "column",
        "flex_gap": {
            "size": 0,
            "unit": "px",
            "column": "0",
            "row": "0",
            "isLinked": True,
        },
        "padding": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "0",
            "left": "0",
            "isLinked": True,
        },
        "_css_classes": "lll-whats-new-section",
    }


def main() -> None:
    css, sections = extract_d2()
    scoped = scope_css(css)
    fonts = (
        "@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;500;600&display=swap');"
    )
    style_block = f'<style id="lll-whats-new-d2">{fonts}{scoped}</style>'

    content = [
        container(
            {**boxed(), "background_background": "classic", "background_color": "#F6EFE8"},
            [html_widget(style_block, "D2 styles + fonts")],
            title="D2 styles",
        )
    ]

    for i, section in enumerate(sections):
        title = SECTION_TITLES[i] if i < len(SECTION_TITLES) else f"Section {i+1}"
        wrapped = f'<div class="lll-whats-new">{section}</div>'
        content.append(
            container(
                boxed(),
                [html_widget(wrapped, title)],
                title=title,
            )
        )

    payload = {
        "content": content,
        "page_settings": {
            "hide_title": "yes",
            "ha_grid_zindex": "1000",
            "custom_css": scoped,
        },
        "version": "0.4",
        "title": "What's New — D2 Cinematic",
        "type": "page",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    README.write_text(
        """# Import the D2 What’s New page into Elementor

File: `elementor-whats-new-d2.json`

This is an Elementor **page template** (export format `0.4`), rebuilt from the approved D2 cinematic layout. Card and partner links go to the live article permalinks. Hover lift / image zoom is included. The ConvertKit newsletter form from the current What’s New page is embedded.

## How to import

1. In WordPress, open **Templates → Saved Templates** (or **Elementor → Saved Templates**).
2. Click **Import Templates**.
3. Upload `elementor-whats-new-d2.json`.
4. Open the **What’s New** page with Elementor (or create a new page).
5. Add a template / insert **What's New — D2 Cinematic**.
6. Publish. Hide the default page title if the theme still shows one.

Alternative: **Elementor → Tools → Import / Export** if your Elementor version lists JSON page exports there.

## After import

- Grids are HTML widgets so the D2 magazine layout and hover motion stay intact without Unlimited Elements.
- To swap a card, edit the HTML widget for that section and change the `href`, image, date, or title.
- The live ConvertKit form (`forms/8767355`) is in the newsletter section.
- Partner tiles, Spotlight, Education, Discussions, Survivors, and Blogs keep the same copy and photos as D2.

## Preview mockup

Local review file: `version-d2-refined.html`
"""
    )
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), {len(sections)} sections")


if __name__ == "__main__":
    main()
