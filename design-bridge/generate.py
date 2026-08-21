#!/usr/bin/env python3
"""Turn a page spec (JSON) into:
  - an HTML preview
  - an Elementor 0.4 native page template

The spec is the bridge. Canva and HTML inform the spec; Elementor is generated
from the spec, not from an old WordPress export.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
N = 0
PINK_DEFAULT = "#c44b6a"


def eid(label: str) -> str:
    global N
    N += 1
    return hashlib.md5(f"bridge-{label}-{N}".encode()).hexdigest()[:7]


def size(n, unit="px"):
    return {"unit": unit, "size": n, "sizes": []}


def gap(n):
    return {"size": n, "unit": "px", "column": str(n), "row": str(n), "isLinked": True}


def pad(t, r, b, l, unit="px", linked=False):
    return {
        "unit": unit,
        "top": str(t),
        "right": str(r),
        "bottom": str(b),
        "left": str(l),
        "isLinked": linked,
    }


def media(url: str, media_id: str = ""):
    return {"url": url, "id": media_id or "", "size": "", "alt": "", "source": "library"}


def node(el_type: str, settings: dict, elements=None, widget=None, title="", inner=None):
    if title:
        settings = {**settings, "_title": title}
    if inner is None:
        inner = bool(widget is None and elements)
    item = {
        "id": eid(el_type + (widget or "")),
        "elType": el_type,
        "isInner": inner,
        "settings": settings,
        "elements": elements or [],
    }
    if widget:
        item["widgetType"] = widget
        item["isInner"] = False
    return item


def heading(text, *, tag="h2", color="#2a1c22", size_px=32, weight="500", family="Montserrat", transform="", align="left"):
    s = {
        "title": text,
        "header_size": tag,
        "align": align,
        "title_color": color,
        "typography_typography": "custom",
        "typography_font_family": family,
        "typography_font_weight": weight,
        "typography_font_size": size(size_px),
        "ha_advanced_tooltip_content": "I am a tooltip",
        "ha_cmc_text": "Happy Addons",
    }
    if transform:
        s["typography_text_transform"] = transform
    return node("widget", s, widget="heading")


def text_editor(html, *, color="#2a1c22", size_px=22, mobile=20, family="Montserrat"):
    return node(
        "widget",
        {
            "editor": html if html.startswith("<") else f"<p>{html}</p>",
            "text_color": color,
            "typography_typography": "custom",
            "typography_font_family": family,
            "typography_font_size": size(size_px),
            "typography_font_size_mobile": size(mobile),
            "typography_font_weight": "300",
        },
        widget="text-editor",
    )


def button(label, url, *, accent="#c44b6a", align="left"):
    return node(
        "widget",
        {
            "text": label,
            "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
            "align": align,
            "background_color": accent,
            "button_text_color": "#FFFFFF",
            "button_background_hover_color": accent,
            "hover_color": "#FFFFFF",
            "border_radius": {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True},
            "typography_typography": "custom",
            "typography_font_family": "Montserrat",
            "typography_font_size": size(14),
            "typography_font_weight": "500",
            "typography_text_transform": "uppercase",
            "typography_letter_spacing": size(0.8),
            "__globals__": {
                "button_text_color": "",
                "background_color": "",
                "button_background_hover_color": "",
                "hover_color": "",
            },
            "ha_advanced_tooltip_content": "I am a tooltip",
            "ha_cmc_text": "Happy Addons",
        },
        widget="button",
    )


def image(url, *, css_class=""):
    s = {"image": media(url), "image_size": "full"}
    if css_class:
        s["_css_classes"] = css_class
    return node("widget", s, widget="image")


def html_widget(html):
    return node("widget", {"html": html}, widget="html")


def overlay_css(gradient: str) -> str:
    return (
        "\nselector::after {\n  content: \"\";\n  position: absolute;\n  inset: 0;\n  "
        f"background: {gradient};\n  z-index: 0;\n}}\n"
        "selector .e-con-inner { position: relative; z-index: 1; }\n"
    )


def tokens_of(spec):
    defaults = json.loads((ROOT / "tokens.lll.json").read_text())
    defaults.update(spec.get("tokens") or {})
    return defaults


def widgets_from_blocks(blocks, tokens, color=None):
    out = []
    ink = color or tokens["ink"]
    accent = tokens["accent"]
    sans = tokens["sans"]
    serif = tokens["serif"]
    body = tokens.get("bodySize", 22)
    mobile = tokens.get("bodySizeMobile", 20)
    for b in blocks or []:
        kind = b.get("type")
        if kind == "heading":
            out.append(
                heading(
                    b["text"],
                    tag=b.get("tag", "h2"),
                    color=b.get("color", ink),
                    size_px=b.get("size", 32),
                    family=serif if b.get("serif") else sans,
                    transform=b.get("transform", ""),
                    weight=str(b.get("weight", "500")),
                )
            )
        elif kind == "text":
            out.append(text_editor(b["html"] if "html" in b else b["text"], color=b.get("color", ink), size_px=body, mobile=mobile, family=sans))
        elif kind == "button":
            out.append(button(b["text"], b.get("url", "#"), accent=accent, align=b.get("align", "left")))
        elif kind == "image":
            out.append(image(b["url"]))
        elif kind == "html":
            out.append(html_widget(b["html"]))
    return out


def section_hero(sec, tokens):
    copy_width = sec.get("copyWidth", 540)
    gradient = sec.get(
        "overlayGradient",
        "linear-gradient(270deg, rgba(32,14,22,.86) 0%, rgba(32,14,22,.55) 38%, rgba(32,14,22,.08) 62%, transparent 78%)",
    )
    outer = {
        "layout": "full_width",
        "content_width": "full",
        "flex_align_items": "center",
        "flex_justify_content": sec.get("align", "flex-end"),
        "flex_gap": gap(0),
        "padding": pad(0, 0, 0, 0, linked=True),
        "background_background": "classic",
        "background_image": media(sec["background"]),
        "background_size": "cover",
        "background_position": sec.get("objectPosition", "18% center"),
        "background_repeat": "no-repeat",
        "min_height": size(sec.get("minHeight", 88), "vh"),
        "background_overlay_background": "classic",
        "background_overlay_color": sec.get("overlayColor", "rgba(32,14,22,0.6)"),
        "custom_css": overlay_css(gradient),
    }
    inner = node(
        "container",
        {
            "content_width": "boxed",
            "width": size(copy_width),
            "flex_direction": "column",
            "flex_gap": gap(16),
            "padding": pad(80, 40, 80, 20),
        },
        widgets_from_blocks(sec.get("blocks"), tokens, color="#ffffff"),
        title="Hero Copy",
    )
    return node("container", outer, [inner], title=sec.get("id", "Hero"), inner=False)


def section_split(sec, tokens):
    cols = []
    for col in sec.get("columns", []):
        cols.append(
            node(
                "container",
                {"content_width": "full", "width": size(50, "%"), "flex_direction": "column", "flex_gap": gap(12)},
                widgets_from_blocks(col.get("blocks"), tokens),
                title=col.get("title", "Column"),
            )
        )
    row = node(
        "container",
        {"content_width": "full", "flex_direction": "row", "flex_gap": gap(36), "flex_wrap": "wrap"},
        cols,
        title="Split Row",
    )
    card = node(
        "container",
        {
            "content_width": "boxed",
            "boxed_width": size(1180),
            "background_background": "classic",
            "background_color": sec.get("cardColor", "#fffaf6"),
            "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
            "padding": pad(40, 40, 40, 40),
            "margin": pad(-56, 0, 0, 0),
        },
        [row],
        title="Paper Card",
    )
    return node(
        "container",
        {
            "layout": "full_width",
            "content_width": "full",
            "background_background": "classic",
            "background_color": tokens["bg"],
            "padding": pad(0, 20, 40, 20),
        },
        [card],
        title=sec.get("id", "Intro"),
        inner=False,
    )


def section_spotlight(sec, tokens):
    left = node(
        "container",
        {"content_width": "full", "width": size(52, "%"), "flex_direction": "column", "flex_gap": gap(16)},
        widgets_from_blocks(sec.get("blocks"), tokens, color="#ffffff"),
        title="Spot Copy",
    )
    card_blocks = sec.get("card", {})
    card_kids = []
    if card_blocks.get("image"):
        card_kids.append(image(card_blocks["image"], css_class="spot-card-img"))
    card_kids.extend(widgets_from_blocks(card_blocks.get("blocks"), tokens))
    right = node(
        "container",
        {
            "content_width": "full",
            "width": size(40, "%"),
            "background_background": "classic",
            "background_color": "#ffffff",
            "border_radius": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": True},
            "overflow": "hidden",
        },
        card_kids,
        title="Spot Card",
    )
    row = node(
        "container",
        {
            "content_width": "boxed",
            "boxed_width": size(1180),
            "flex_direction": "row",
            "flex_align_items": "center",
            "flex_gap": gap(36),
            "padding": pad(56, 20, 56, 20),
        },
        [left, right],
    )
    return node(
        "container",
        {
            "layout": "full_width",
            "content_width": "full",
            "flex_align_items": "center",
            "background_background": "classic",
            "background_image": media(sec["background"]),
            "background_size": "cover",
            "min_height": size(sec.get("minHeight", 60), "vh"),
            "background_overlay_background": "classic",
            "background_overlay_color": sec.get("overlayColor", "rgba(32,14,22,0.65)"),
        },
        [row],
        title=sec.get("id", "Spotlight"),
        inner=False,
    )


def section_photo_header(sec, tokens):
    gradient = sec.get(
        "overlayGradient",
        "linear-gradient(270deg, rgba(18,8,14,.94) 0%, rgba(18,8,14,.78) 38%, rgba(18,8,14,.2) 68%, transparent 88%)",
    )
    inner = node(
        "container",
        {
            "content_width": "boxed",
            "width": size(sec.get("copyWidth", 620)),
            "flex_direction": "column",
            "flex_gap": gap(16),
            "padding": pad(64, 40, 48, 20),
        },
        widgets_from_blocks(sec.get("blocks"), tokens, color="#ffffff"),
        title="Copy",
    )
    return node(
        "container",
        {
            "layout": "full_width",
            "content_width": "full",
            "flex_justify_content": "flex-end",
            "flex_align_items": "center",
            "background_background": "classic",
            "background_image": media(sec["background"]),
            "background_size": "cover",
            "background_position": sec.get("objectPosition", "18% center"),
            "min_height": size(sec.get("minHeight", 55), "vh"),
            "background_overlay_background": "classic",
            "background_overlay_color": sec.get("overlayColor", "rgba(18,8,14,0.72)"),
            "custom_css": overlay_css(gradient),
        },
        [inner],
        title=sec.get("id", "Photo header"),
        inner=False,
    )


def section_chapter(sec, tokens):
    photo = node(
        "container",
        {
            "width": size(46, "%"),
            "content_width": "full",
            "background_background": "classic",
            "background_image": media(sec["background"]),
            "background_size": "cover",
            "min_height": size(sec.get("minHeight", 480)),
        },
        title="Photo",
    )
    copy = node(
        "container",
        {
            "width": size(54, "%"),
            "content_width": "full",
            "flex_direction": "column",
            "flex_justify_content": "center",
            "padding": pad(56, 48, 56, 48),
            "background_background": "classic",
            "background_color": sec.get("panelColor", "#2a1c22"),
        },
        widgets_from_blocks(sec.get("blocks"), tokens, color="#ffffff"),
        title="Copy",
    )
    return node(
        "container",
        {
            "layout": "full_width",
            "content_width": "full",
            "flex_direction": "row",
            "background_color": "#2a1c22",
            "min_height": size(sec.get("minHeight", 480)),
        },
        [photo, copy],
        title=sec.get("id", "Chapter"),
        inner=False,
    )


def section_stack(sec, tokens):
    inner = node(
        "container",
        {"content_width": "boxed", "boxed_width": size(1180), "flex_direction": "column", "flex_gap": gap(20), "padding": pad(40, 20, 40, 20)},
        widgets_from_blocks(sec.get("blocks"), tokens),
    )
    return node(
        "container",
        {
            "layout": "full_width",
            "content_width": "full",
            "background_background": "classic",
            "background_color": sec.get("backgroundColor", tokens["bg"]),
        },
        [inner],
        title=sec.get("id", "Section"),
        inner=False,
    )


def section_html(sec, tokens):
    inner = node(
        "container",
        {"content_width": "boxed", "boxed_width": size(1180), "padding": pad(28, 20, 28, 20), "flex_direction": "column", "flex_gap": gap(16)},
        widgets_from_blocks(sec.get("blocks"), tokens) + ([html_widget(sec["html"])] if sec.get("html") else []),
    )
    return node(
        "container",
        {"layout": "full_width", "content_width": "full", "background_color": tokens["bg"]},
        [inner],
        title=sec.get("id", "HTML"),
        inner=False,
    )


def section_grid(sec, tokens):
    note = heading("Post grid — insert Unlimited Elements magazine grid here in Elementor", tag="h3", size_px=18, color=tokens["ink"])
    hint = text_editor(
        "<p>Keep this container. In Elementor, add the same <strong>Post Magazine Grid</strong> widget used on the live What’s New page so posts stay dynamic.</p>",
        color=tokens["ink"],
        size_px=16,
        mobile=16,
    )
    inner = node("container", {"content_width": "boxed", "boxed_width": size(1180), "padding": pad(20, 20, 40, 20)}, [note, hint])
    return node("container", {"layout": "full_width", "background_color": tokens["bg"]}, [inner], title=sec.get("id", "Grid"), inner=False)


BUILDERS = {
    "hero": section_hero,
    "split": section_split,
    "spotlight": section_spotlight,
    "photo-header": section_photo_header,
    "chapter": section_chapter,
    "stack": section_stack,
    "html": section_html,
    "magazine-grid": section_grid,
    "wash": section_photo_header,
}


def to_elementor(spec: dict) -> dict:
    tokens = tokens_of(spec)
    content = []
    for sec in spec["sections"]:
        builder = BUILDERS.get(sec["type"], section_stack)
        content.append(builder(sec, tokens))
    return {
        "version": "0.4",
        "title": spec["title"],
        "type": "page",
        "page_settings": {"hide_title": "yes"},
        "content": content,
    }


def to_html(spec: dict) -> str:
    tokens = tokens_of(spec)
    parts = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>{spec['title']}</title>",
        f"<link href='https://fonts.googleapis.com/css2?family={tokens['sans'].replace(' ','+')}:wght@300;400;500;600&family={tokens['serif'].replace(' ','+')}:wght@400;700&display=swap' rel='stylesheet'>",
        f"<style>body{{margin:0;font-family:{tokens['sans']},sans-serif;background:{tokens['bg']};color:{tokens['ink']};font-size:{tokens['bodySize']}px;font-weight:300;line-height:1.65}}",
        f"@media(max-width:767px){{body,p{{font-size:{tokens['bodySizeMobile']}px}}}}",
        ".wrap{width:min(1180px,calc(100% - 40px));margin-inline:auto}",
        f"a.btn{{display:inline-flex;padding:12px 36px;border-radius:999px;background:{tokens['accent']};color:#fff;text-decoration:none;text-transform:uppercase;letter-spacing:.06em;font-size:14px;font-weight:500}}</style></head><body>",
    ]
    for sec in spec["sections"]:
        parts.append(f"<!-- {sec.get('id')} ({sec['type']}) -->")
        if sec["type"] == "html" and sec.get("html"):
            parts.append(f"<section class='wrap' style='padding:28px 0'>{sec['html']}</section>")
            continue
        bg = sec.get("background")
        style = "padding:48px 0"
        if bg:
            style = f"min-height:50vh;background:url('{bg}') center/cover;color:#fff;padding:64px 0"
        parts.append(f"<section id='{sec.get('id','')}' style=\"{style}\"><div class='wrap'>")
        for b in sec.get("blocks") or []:
            if b.get("type") == "heading":
                tag = b.get("tag", "h2")
                parts.append(f"<{tag}>{b['text']}</{tag}>")
            elif b.get("type") == "text":
                parts.append(f"<p>{b.get('html') or b.get('text')}</p>")
            elif b.get("type") == "button":
                parts.append(f"<p><a class='btn' href='{b.get('url','#')}'>{b['text']}</a></p>")
        for col in sec.get("columns") or []:
            for b in col.get("blocks") or []:
                if b.get("type") == "heading":
                    parts.append(f"<h2>{b['text']}</h2>")
                elif b.get("type") == "text":
                    parts.append(f"<p>{b.get('html') or b.get('text')}</p>")
        if sec["type"] == "magazine-grid":
            parts.append("<p><em>Magazine grid (dynamic in Elementor).</em></p>")
        parts.append("</div></section>")
    parts.append("</body></html>")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Generate HTML + Elementor JSON from a page spec")
    parser.add_argument("spec", type=Path)
    parser.add_argument("--out", type=Path, default=None, help="Output directory")
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text())
    out = args.out or args.spec.parent
    out.mkdir(parents=True, exist_ok=True)
    slug = args.spec.stem.replace(".spec", "")
    el_path = out / f"elementor-{slug}.json"
    html_path = out / f"{slug}-preview.html"
    el_path.write_text(json.dumps(to_elementor(spec), ensure_ascii=False, indent=2))
    html_path.write_text(to_html(spec))
    print(f"Wrote {el_path} ({el_path.stat().st_size} bytes)")
    print(f"Wrote {html_path} ({html_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
