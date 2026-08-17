#!/usr/bin/env python3
"""Rebuild the What's New Elementor page from the original widget tree,
with D2 layout applied in native container/widget settings (not an HTML dump).
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIG = ROOT / "elementor-whats-new-original.json"
OUT = ROOT / "elementor-whats-new-d2.json"
README = ROOT / "ELEMENTOR-IMPORT.md"
PINK = "#C44B6A"
N = 0


def eid(label: str) -> str:
    global N
    N += 1
    return hashlib.md5(f"d2-native-{label}-{N}".encode()).hexdigest()[:7]


def size(n, unit="px"):
    return {"unit": unit, "size": n, "sizes": []}


def pad(t, r, b, l, unit="px"):
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


def walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in list(o.values()):
            walk(v, fn)
    elif isinstance(o, list):
        for v in o:
            walk(v, fn)


STYLE_BLOCK = r"""
<style id="lll-d2-native">
.lll-d2-page .elementor-button{
  border-radius:999px !important;
  padding:12px 36px !important;
  text-transform:uppercase !important;
  letter-spacing:.06em !important;
  font-family:Montserrat,sans-serif !important;
  font-weight:500 !important;
  font-size:14px !important;
  background-color:#C44B6A !important;
  color:#fff !important;
  box-shadow:none !important;
  transition:transform .3s ease,box-shadow .3s ease,filter .3s ease;
}
.lll-d2-page .elementor-button:hover{
  transform:translateY(-2px) scale(1.02);
  filter:brightness(1.08);
  box-shadow:0 10px 22px rgba(196,75,106,.32) !important;
}
.lll-partner-tile{
  overflow:hidden;
  transition:transform .4s cubic-bezier(.22,1,.36,1),box-shadow .4s ease;
}
.lll-partner-tile:hover{
  transform:translateY(-8px);
  box-shadow:0 20px 40px rgba(40,16,28,.22);
}
.lll-partner-logo img{
  height:64px !important;
  width:auto !important;
  max-width:240px !important;
  object-fit:contain !important;
  background:#fff !important;
  padding:10px 16px !important;
  border-radius:10px !important;
  box-shadow:0 6px 16px rgba(0,0,0,.12);
}
.lll-hero .elementor-background-overlay,
.lll-educate .elementor-background-overlay{
  background-color:transparent !important;
  background-image:linear-gradient(270deg,rgba(18,8,14,.94) 0%,rgba(18,8,14,.78) 38%,rgba(18,8,14,.2) 68%,transparent 88%) !important;
  opacity:1 !important;
}
@media (max-width:767px){
  .lll-hero .elementor-background-overlay,
  .lll-educate .elementor-background-overlay{
    background-image:linear-gradient(180deg,rgba(18,8,14,.15) 0%,rgba(18,8,14,.8) 40%,rgba(18,8,14,.95) 100%) !important;
  }
}
</style>
"""


def add_class(el, cls: str) -> None:
    s = el.setdefault("settings", {})
    cur = (s.get("_css_classes") or "").split()
    if cls not in cur:
        cur.append(cls)
    s["_css_classes"] = " ".join(cur).strip()


def hide(el) -> None:
    s = el.setdefault("settings", {})
    s["hide_desktop"] = "yes"
    s["hide_tablet"] = "yes"
    s["hide_mobile"] = "yes"


def right_overlay(sec, extra_class: str) -> None:
    s = sec["settings"]
    s["background_background"] = "classic"
    s["background_size"] = "cover"
    s["background_position"] = "18% center"
    s["background_color"] = "#1A0C12"
    s["background_overlay_background"] = "gradient"
    s["background_overlay_color"] = "#12080E00"
    s["background_overlay_color_stop"] = size(0, "%")
    s["background_overlay_color_b"] = "#12080EF2"
    s["background_overlay_color_b_stop"] = size(42, "%")
    s["background_overlay_gradient_angle"] = size(180, "deg")
    s["background_overlay_opacity"] = size(1)
    s["shape_divider_top"] = ""
    s["shape_divider_bottom"] = ""
    s["flex_justify_content"] = "flex-end"
    s["flex_align_items"] = "center"
    add_class(sec, extra_class)
    add_class(sec, "lll-d2-page")


def style_text(el) -> None:
    s = el["settings"]
    s["typography_typography"] = "custom"
    s["typography_font_family"] = "Montserrat"
    s["typography_font_size"] = size(22)
    s["typography_font_size_tablet"] = size(22)
    s["typography_font_size_mobile"] = size(20)
    s["typography_font_weight"] = "300"


def style_button(el) -> None:
    s = el["settings"]
    s["background_color"] = PINK
    s["button_text_color"] = "#FFFFFF"
    s["button_background_hover_color"] = "#D45A78"
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


def white_copy(el) -> None:
    s = el["settings"]
    wt = el.get("widgetType")
    if wt == "text-editor":
        s["text_color"] = "#FFFFFF"
    elif wt == "heading":
        s["title_color"] = "#FFFFFF"
        g = s.get("__globals__") or {}
        g["title_color"] = ""
        s["__globals__"] = g
    elif wt == "animated-headline":
        s["title_color"] = "#FFFFFF"
        s["hover_headline_color"] = PINK


def inject_styles(data) -> None:
    style_widget = {
        "id": eid("style"),
        "elType": "widget",
        "widgetType": "html",
        "isInner": False,
        "settings": {"html": STYLE_BLOCK},
        "elements": [],
    }
    hero = data["content"][1]
    hero["elements"].insert(0, style_widget)


def restyle_hero(sec) -> None:
    right_overlay(sec, "lll-hero")
    sec["settings"]["min_height"] = size(88, "vh")
    sec["settings"]["padding"] = pad(5, 5, 8, 5, "%")
    # Keep the existing 50/50 row but make the copy column right-aligned.
    if len(sec["elements"]) > 1:
        row = sec["elements"][1] if sec["elements"][0].get("widgetType") == "html" else sec["elements"][2]
        if row.get("elType") == "container":
            row["settings"]["flex_justify_content"] = "flex-end"
            cols = row.get("elements") or []
            if len(cols) >= 2:
                cols[0]["settings"]["width"] = size(38, "%")
                cols[1]["settings"]["width"] = size(54, "%")
                cols[1]["settings"]["flex_align_items"] = "flex-start"
    walk(sec, lambda e: white_copy(e) if e.get("elType") == "widget" else None)


def restyle_intro(sec) -> None:
    s = sec["settings"]
    s["background_image"] = {"url": "", "id": "", "size": "", "alt": "", "source": "library"}
    s["background_background"] = "classic"
    s["background_color"] = "#FFFAF6"
    s["background_overlay_color"] = "#FFFFFF00"
    s["shape_divider_bottom"] = ""
    s["margin"] = pad(-56, 0, 0, 0)
    s["padding"] = pad(40, 24, 40, 24)
    s["border_radius"] = {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True}
    s["z_index"] = 12
    add_class(sec, "lll-d2-page")


def restyle_spotlight(sec) -> None:
    """Copy on the left, slider card on the right."""
    add_class(sec, "lll-d2-page")
    kids = sec.get("elements") or []
    if len(kids) < 3:
        return
    intro, titles, slider = kids[0], kids[1], kids[2]
    rest = kids[3:]
    titles["settings"]["width"] = size(48, "%")
    slider["settings"]["width"] = size(52, "%")
    slider["settings"]["flex_align_items"] = "center"
    row = {
        "id": eid("spot-row"),
        "elType": "container",
        "isInner": True,
        "settings": {
            "content_width": "full",
            "flex_direction": "row",
            "flex_align_items": "center",
            "flex_gap": {"size": 28, "unit": "px", "column": "28", "row": "28", "isLinked": True},
            "padding": pad(24, 24, 24, 24),
            "background_background": "classic",
            "background_image": {
                "url": "https://learnlooklocate.com/wp-content/uploads/2025/09/spotlight-innovations-in-breast-cancer-care-progress-breakthroughs-learn-look-locate.jpg.png",
                "id": 47653,
                "size": "",
                "alt": "",
                "source": "library",
            },
            "background_size": "cover",
            "background_position": "center center",
            "background_overlay_background": "classic",
            "background_overlay_color": "#14080E99",
            "background_overlay_opacity": size(1),
            "border_radius": {"unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": True},
            "min_height": size(520),
        },
        "elements": [titles, slider],
    }
    walk(titles, lambda e: white_copy(e) if e.get("elType") == "widget" else None)
    # Hide the repeated SPOTLIGHT wordmark headings inside the slider stack.
    for child in slider.get("elements") or []:
        if child.get("widgetType") == "heading" and (child.get("settings") or {}).get("title") == "SPOTLIGHT":
            hide(child)
    sec["elements"] = [intro, row, *rest]


def restyle_partners(sec) -> None:
    s = sec["settings"]
    s["background_image"] = {"url": "", "id": "", "size": "", "alt": "", "source": "library"}
    s["background_color"] = "#F6EFE8"
    s["background_overlay_color"] = "#FFFFFF00"
    s["shape_divider_bottom"] = ""
    add_class(sec, "lll-d2-page")
    try:
        tiles = sec["elements"][0]["elements"][0]["elements"]
    except (IndexError, KeyError, TypeError):
        return
    wrap = sec["elements"][0]["elements"][0]
    wrap["settings"]["flex_wrap"] = "wrap"
    wrap["settings"]["flex_gap"] = {"size": 16, "unit": "px", "column": "16", "row": "16", "isLinked": True}
    for tile in tiles:
        ts = tile["settings"]
        add_class(tile, "lll-partner-tile")
        images = [e for e in tile.get("elements") or [] if e.get("widgetType") == "image"]
        headings = [e for e in tile.get("elements") or [] if e.get("widgetType") == "heading"]
        cover = (images[0]["settings"].get("image") or {}) if images else {}
        if cover.get("url"):
            ts["background_background"] = "classic"
            ts["background_image"] = cover
            ts["background_size"] = "cover"
            ts["background_position"] = "center center"
            ts["background_overlay_background"] = "gradient"
            ts["background_overlay_color"] = "#28101C14"
            ts["background_overlay_color_b"] = "#28101CE0"
            ts["background_overlay_gradient_angle"] = size(180, "deg")
            ts["background_overlay_opacity"] = size(1)
        ts["min_height"] = size(300)
        ts["width"] = size(32, "%")
        ts["flex_direction"] = "column"
        ts["flex_justify_content"] = "space-between"
        ts["flex_align_items"] = "flex-start"
        ts["padding"] = pad(18, 18, 18, 18)
        ts["border_radius"] = {"unit": "px", "top": "18", "right": "18", "bottom": "18", "left": "18", "isLinked": True}
        link = ts.get("ha_element_link") or {}
        if link.get("url"):
            link["url"] = link["url"].rstrip("/") + "/"
            ts["ha_element_link"] = link
        if images:
            hide(images[0])  # photo is now the container background
        if len(images) > 1:
            add_class(images[1], "lll-partner-logo")
            images[1]["settings"]["image_size"] = "custom"
            images[1]["settings"]["image_custom_dimension"] = {"width": "240", "height": "64"}
        if headings:
            h = headings[0]["settings"]
            h["align"] = "left"
            h["header_size"] = "h3"
            h["title_color"] = "#FFFFFF"
            h["typography_typography"] = "custom"
            h["typography_font_family"] = "Libre Baskerville"
            h["typography_font_size"] = size(20)
            h["typography_font_weight"] = "600"
            g = h.get("__globals__") or {}
            g["title_color"] = ""
            h["__globals__"] = g


def restyle_educate(sec) -> None:
    right_overlay(sec, "lll-educate")
    sec["settings"]["min_height"] = size(78, "vh")
    if len(sec["elements"]) > 1:
        row = sec["elements"][1]
        row["settings"]["flex_justify_content"] = "flex-end"
        cols = row.get("elements") or []
        if len(cols) >= 2:
            cols[0]["settings"]["width"] = size(36, "%")
            cols[1]["settings"]["width"] = size(58, "%")
    walk(sec, lambda e: white_copy(e) if e.get("elType") == "widget" else None)


def restyle_photo_chapter(sec, extra_class: str) -> None:
    s = sec["settings"]
    s["background_size"] = "cover"
    s["background_position"] = "center center"
    s["background_overlay_background"] = "classic"
    s["background_overlay_color"] = "#14080E66"
    s["background_overlay_opacity"] = size(1)
    s["shape_divider_top"] = ""
    s["shape_divider_bottom"] = ""
    add_class(sec, extra_class)
    add_class(sec, "lll-d2-page")
    walk(sec, lambda e: white_copy(e) if e.get("elType") == "widget" else None)


def style_grids(el) -> None:
    s = el["settings"]
    s["title_typography_font_family"] = "Libre Baskerville"
    s["title_typography_font_size"] = size(20)
    extra = s.get("custom_css") or ""
    hover = """
selector .ue-grid-item{transition:transform .4s cubic-bezier(.22,1,.36,1),box-shadow .4s ease;}
selector .ue-grid-item:hover{transform:translateY(-8px);box-shadow:0 18px 36px rgba(80,30,40,.16);}
selector .ue-grid-item img{transition:transform .6s ease;}
selector .ue-grid-item:hover img{transform:scale(1.06);}
"""
    if "ue-grid-item:hover" not in extra:
        s["custom_css"] = extra + hover


def main() -> None:
    data = copy.deepcopy(json.loads(ORIG.read_text()))
    data["title"] = "What's New — D2 Cinematic"
    data["page_settings"] = data.get("page_settings") or {}
    data["page_settings"]["hide_title"] = "yes"

    # Hide the old purple wave bar so the cinematic hero can read.
    hide(data["content"][0])

    def apply(el):
        if not isinstance(el, dict):
            return
        wt = el.get("widgetType")
        if wt == "text-editor":
            style_text(el)
        elif wt == "button":
            style_button(el)
        elif wt == "ucaddon_post_magazine_grid":
            style_grids(el)

    walk(data["content"], apply)

    restyle_hero(data["content"][1])
    inject_styles(data)
    restyle_intro(data["content"][2])
    restyle_spotlight(data["content"][3])
    restyle_partners(data["content"][4])
    restyle_educate(data["content"][5])
    restyle_photo_chapter(data["content"][8], "lll-discussions")
    restyle_photo_chapter(data["content"][10], "lll-survivors")
    restyle_photo_chapter(data["content"][12], "lll-blogs")
    add_class(data["content"][7], "lll-d2-page")

    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    README.write_text(
        """# Import What's New D2 into Elementor

File: `elementor-whats-new-d2.json`

This is the **original What’s New Elementor tree** (containers, headings, buttons, images, Unlimited Elements grids, Spotlight slider, ConvertKit) with the D2 layout applied **on those widgets**:

- Hero photo, copy on the right, dark overlay
- Cream intro panel
- Spotlight copy + slider side by side on the cinematic photo
- Partner tiles as photo covers with larger logos
- Education copy on the right with a stronger overlay
- Magazine grids still pull posts dynamically
- Pill buttons, Montserrat 22px / 20px mobile

## Import

1. Templates → Saved Templates → Import Templates
2. Upload `elementor-whats-new-d2.json`
3. **Replace** the previous import (do not leave the old template on the page)
4. Insert **What's New — D2 Cinematic** and publish

Images keep existing Media Library IDs. Do not re-upload.

If you still see the old purple wave layout, the old template is still on the page — remove those sections first, then insert this one.
"""
    )
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes) title={data['title']} sections={len(data['content'])}")


if __name__ == "__main__":
    main()
