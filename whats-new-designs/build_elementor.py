#!/usr/bin/env python3
"""Build an Elementor 0.4 page from the original What's New export.

Keeps native widgets (containers, headings, text, buttons, images,
Unlimited Elements magazine grids / spotlight slider, ConvertKit HTML)
and only restyles them to match the D2 HTML preview.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIG = Path("/home/ubuntu/.cursor/projects/workspace/uploads/elementor-74696-2026-08-16_d9d5.json")
if not ORIG.exists():
    ORIG = ROOT / "elementor-whats-new-original.json"
OUT = ROOT / "elementor-whats-new-d2.json"
README = ROOT / "ELEMENTOR-IMPORT.md"

PINK = "#C44B6A"
CUSTOM_CSS = r"""
selector .elementor-button {
  border-radius: 999px !important;
  padding: 12px 36px !important;
  text-transform: uppercase !important;
  letter-spacing: .06em !important;
  font-family: Montserrat, sans-serif !important;
  font-weight: 500 !important;
  font-size: 14px !important;
  background-color: #C44B6A !important;
  color: #fff !important;
  box-shadow: none !important;
  transition: transform .3s ease, box-shadow .3s ease, filter .3s ease;
}
selector .elementor-button:hover {
  transform: translateY(-2px) scale(1.02);
  filter: brightness(1.08);
  box-shadow: 0 10px 22px rgba(196,75,106,.32) !important;
  background-color: #C44B6A !important;
  color: #fff !important;
}
selector .lll-partner-tile {
  transition: transform .4s cubic-bezier(.22,1,.36,1), box-shadow .4s ease;
}
selector .lll-partner-tile:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(40,16,28,.22);
}
selector .lll-partner-cover img {
  width: 100% !important;
  height: 220px !important;
  object-fit: cover !important;
  border-radius: 12px;
}
selector .lll-partner-logo img {
  height: 64px !important;
  width: auto !important;
  max-width: 240px !important;
  object-fit: contain !important;
  background: #fff;
  padding: 10px 16px;
  border-radius: 10px;
  box-shadow: 0 6px 16px rgba(0,0,0,.12);
}
selector .lll-hero > .elementor-background-overlay,
selector .lll-educate > .elementor-background-overlay {
  background-image: linear-gradient(270deg, rgba(18,8,14,.94) 0%, rgba(18,8,14,.78) 36%, rgba(18,8,14,.28) 62%, transparent 86%) !important;
  background-color: transparent !important;
  opacity: 1 !important;
}
@media (max-width: 767px) {
  selector .lll-hero > .elementor-background-overlay,
  selector .lll-educate > .elementor-background-overlay {
    background-image: linear-gradient(180deg, rgba(18,8,14,.2) 0%, rgba(18,8,14,.78) 38%, rgba(18,8,14,.94) 100%) !important;
  }
}
"""


def size(n, unit="px"):
    return {"unit": unit, "size": n, "sizes": []}


def walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in o.values():
            walk(v, fn)
    elif isinstance(o, list):
        for v in o:
            walk(v, fn)


def style_text_editor(el):
    s = el["settings"]
    s["typography_typography"] = "custom"
    s["typography_font_family"] = "Montserrat"
    s["typography_font_size"] = size(22)
    s["typography_font_size_tablet"] = size(22)
    s["typography_font_size_mobile"] = size(20)
    s["typography_font_weight"] = "300"


def style_button(el):
    s = el["settings"]
    s["background_color"] = PINK
    s["button_text_color"] = "#FFFFFF"
    s["button_background_hover_color"] = PINK
    s["hover_color"] = "#FFFFFF"
    s["border_radius"] = {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True}
    s["typography_typography"] = "custom"
    s["typography_font_family"] = "Montserrat"
    s["typography_font_size"] = size(14)
    s["typography_font_weight"] = "500"
    s["typography_text_transform"] = "uppercase"
    s["typography_letter_spacing"] = size(0.8)
    g = s.get("__globals__") or {}
    for k in ("button_text_color", "background_color", "button_background_hover_color", "hover_color"):
        g[k] = ""
    s["__globals__"] = g


def style_hero(sec):
    s = sec["settings"]
    s["background_position"] = "18% center"
    s["background_size"] = "cover"
    s["flex_justify_content"] = "flex-end"
    s["flex_align_items"] = "center"
    cls = (s.get("_css_classes") or "").split()
    if "lll-hero" not in cls:
        cls.append("lll-hero")
    s["_css_classes"] = " ".join(cls).strip()
    inner = sec["elements"][1] if len(sec["elements"]) > 1 else None
    if inner and inner.get("elType") == "container":
        inner["settings"]["flex_justify_content"] = "flex-end"
        inner["settings"]["flex_align_items"] = "center"


def style_educate(sec):
    s = sec["settings"]
    s["background_position"] = "18% center"
    s["background_size"] = "cover"
    s["flex_justify_content"] = "flex-end"
    cls = (s.get("_css_classes") or "").split()
    if "lll-educate" not in cls:
        cls.append("lll-educate")
    s["_css_classes"] = " ".join(cls).strip()
    if len(sec["elements"]) > 1:
        row = sec["elements"][1]
        row["settings"]["flex_justify_content"] = "flex-end"


def style_partner_tiles(sec):
    try:
        tiles = sec["elements"][0]["elements"][0]["elements"]
    except (IndexError, KeyError, TypeError):
        return
    for tile in tiles:
        ts = tile["settings"]
        ts["_css_classes"] = ((ts.get("_css_classes") or "") + " lll-partner-tile").strip()
        ts["min_height"] = size(280)
        ts["border_radius"] = {"unit": "px", "top": "18", "right": "18", "bottom": "18", "left": "18", "isLinked": True}
        link = ts.get("ha_element_link") or {}
        url = (link.get("url") or "").rstrip("/") + "/"
        if url.startswith("http"):
            link["url"] = url
            ts["ha_element_link"] = link
        images = [e for e in tile.get("elements") or [] if e.get("widgetType") == "image"]
        headings = [e for e in tile.get("elements") or [] if e.get("widgetType") == "heading"]
        if images:
            cover = images[0]
            cover["settings"]["_css_classes"] = "lll-partner-cover"
            cover["settings"]["image_size"] = "full"
            cover["settings"]["image_border_radius"] = {
                "unit": "px",
                "top": "12",
                "right": "12",
                "bottom": "12",
                "left": "12",
                "isLinked": True,
            }
        if len(images) > 1:
            logo = images[1]
            logo["settings"]["_css_classes"] = "lll-partner-logo"
            logo["settings"]["image_size"] = "custom"
            logo["settings"]["image_custom_dimension"] = {"width": "240", "height": "64"}
        if headings:
            h = headings[0]["settings"]
            h["align"] = "left"
            h["header_size"] = "h3"
            h["title_color"] = "#2A1C22"
            h["typography_typography"] = "custom"
            h["typography_font_family"] = "Libre Baskerville"
            h["typography_font_size"] = size(20)
            h["typography_font_weight"] = "600"
            h["typography_line_height"] = {"unit": "em", "size": 1.3, "sizes": []}


def style_magazine_grid(el):
    s = el["settings"]
    s["title_typography_font_family"] = "Libre Baskerville"
    s["title_typography_font_size"] = size(20)
    s["title_typography_font_weight"] = 600
    extra = s.get("custom_css") or ""
    hover = """
selector .ue-grid-item {
  transition: transform .4s cubic-bezier(.22,1,.36,1), box-shadow .4s ease;
}
selector .ue-grid-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 18px 36px rgba(80,30,40,.16);
}
selector .ue-grid-item img {
  transition: transform .6s cubic-bezier(.22,1,.36,1);
}
selector .ue-grid-item:hover img {
  transform: scale(1.06);
}
"""
    if "ue-grid-item:hover" not in extra:
        s["custom_css"] = extra + hover


def main() -> None:
    data = copy.deepcopy(json.loads(ORIG.read_text()))
    data["title"] = "What's New — D2 Cinematic"
    data["page_settings"] = data.get("page_settings") or {}
    data["page_settings"]["hide_title"] = "yes"
    data["page_settings"]["custom_css"] = CUSTOM_CSS

    def apply(el):
        if not isinstance(el, dict) or el.get("elType") not in ("widget", "container"):
            return
        wt = el.get("widgetType")
        if wt == "text-editor":
            style_text_editor(el)
        elif wt == "button":
            style_button(el)
        elif wt == "ucaddon_post_magazine_grid":
            style_magazine_grid(el)

    walk(data["content"], apply)

    content = data["content"]
    if len(content) > 1:
        style_hero(content[1])
    if len(content) > 4:
        style_partner_tiles(content[4])
    if len(content) > 5:
        style_educate(content[5])

    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    README.write_text(
        """# Import the D2 What’s New page into Elementor

File: `elementor-whats-new-d2.json`

This file is built from the **original What’s New Elementor export**, not from a single HTML blob.

It keeps the same native structure:

- Containers (hero, educate, discussions, survivors, blog)
- Heading / animated headline widgets
- Text editor widgets
- Button widgets
- Image widgets (partner photos + logos)
- Unlimited Elements **post magazine grid** (Education, Discussions, Survivors, Blogs)
- Unlimited Elements **post slider** (Spotlight)
- ConvertKit form HTML widget (newsletter only)
- Decorative HTML (waves / lines) from the original page

D2 visual updates applied on those widgets:

- Montserrat body copy at 22px (20px on mobile)
- Pill buttons in the current pink, with hover
- Larger partner logos
- Stronger right-side overlay on Hero and Education
- Hover lift on partner tiles and magazine cards

## Images

Photos and logos keep the same Media Library URLs and attachment IDs as the live page. Do **not** re-upload images. If the importer asks “Import images?”, leave that off.

## How to import

1. **Templates → Saved Templates → Import Templates**
2. Upload `elementor-whats-new-d2.json`
3. Insert **What's New — D2 Cinematic** on the page
4. Publish

After import you can edit headings, buttons, and images in Elementor like the old page. Grids still pull posts dynamically.

## HTML preview

`whats-new-preview.html` is only for layout review in a browser. The import file is the Elementor version of that design.
"""
    )
    widgets = {}

    def count(el):
        if isinstance(el, dict) and el.get("elType") == "widget":
            widgets[el.get("widgetType")] = widgets.get(el.get("widgetType"), 0) + 1

    walk(data["content"], count)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
    print("widgets", widgets)


if __name__ == "__main__":
    main()
