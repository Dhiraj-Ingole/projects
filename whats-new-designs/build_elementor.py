#!/usr/bin/env python3
"""Rebuild elementor-whats-new-d2.json from the HTML-matching layout.

The layout source is a native Elementor tree that mirrors whats-new-preview.html
(not a restyle of the old purple-wave page). This script copies that layout,
restores the original magazine-grid queries, ConvertKit form, pill buttons,
and larger partner logos.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LAYOUT = ROOT / "elementor-whats-new-d2-html-layout.json"
ORIG = ROOT / "elementor-whats-new-original.json"
CK = ROOT / "convertkit-form.html"
OUT = ROOT / "elementor-whats-new-d2.json"
PINK = "#C44B6A"


def walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in o.values():
            walk(v, fn)
    elif isinstance(o, list):
        for v in o:
            walk(v, fn)


def collect(tree, wt):
    acc = []
    walk(tree, lambda e: acc.append(e) if e.get("widgetType") == wt else None)
    return acc


def main() -> None:
    data = json.loads(LAYOUT.read_text())
    orig = json.loads(ORIG.read_text())
    ck = CK.read_text() if CK.exists() else ""

    orig_grids = collect(orig, "ucaddon_post_magazine_grid")
    new_grids = collect(data, "ucaddon_post_magazine_grid")
    keep = {
        "title_typography_font_family",
        "title_typography_font_size",
        "title_typography_font_weight",
        "title_typography_line_height",
        "title_typography_typography",
        "button_text",
        "grid_columns",
        "grid_gap",
        "item_min_height",
    }
    for dst, src in zip(new_grids, orig_grids):
        merged = copy.deepcopy(src["settings"])
        for k in keep:
            if k in dst["settings"]:
                merged[k] = dst["settings"][k]
        merged["title_typography_font_family"] = "Libre Baskerville"
        merged["title_typography_font_size"] = {"unit": "px", "size": 20, "sizes": []}
        extra = merged.get("custom_css") or ""
        hover = """
selector .ue-grid-item{transition:transform .4s cubic-bezier(.22,1,.36,1),box-shadow .4s ease;}
selector .ue-grid-item:hover{transform:translateY(-8px);box-shadow:0 18px 36px rgba(80,30,40,.16);}
selector .ue-grid-item img{transition:transform .6s ease;}
selector .ue-grid-item:hover img{transform:scale(1.06);}
"""
        if "ue-grid-item:hover" not in extra:
            merged["custom_css"] = extra + hover
        dst["settings"] = merged

    def style_btn(e):
        if e.get("widgetType") != "button":
            return
        s = e["settings"]
        s["background_color"] = PINK
        s["button_text_color"] = "#FFFFFF"
        s["button_background_hover_color"] = "#D45A78"
        s["hover_color"] = "#FFFFFF"
        s["border_radius"] = {
            "unit": "px",
            "top": "50",
            "right": "50",
            "bottom": "50",
            "left": "50",
            "isLinked": True,
        }
        s["typography_typography"] = "custom"
        s["typography_font_family"] = "Montserrat"
        s["typography_font_size"] = {"unit": "px", "size": 14, "sizes": []}
        s["typography_font_weight"] = "500"
        s["typography_text_transform"] = "uppercase"
        s["typography_letter_spacing"] = {"unit": "px", "size": 0.8, "sizes": []}
        g = s.get("__globals__") or {}
        for k in (
            "button_text_color",
            "background_color",
            "button_background_hover_color",
            "hover_color",
        ):
            g[k] = ""
        s["__globals__"] = g

    walk(data, style_btn)

    htmls = collect(data, "html")
    if htmls:
        htmls[0]["settings"]["html"] = (
            htmls[0]["settings"]["html"]
            .replace("height:56px", "height:64px")
            .replace("max-width:200px", "max-width:240px")
        )
    if len(htmls) > 1 and ck:
        htmls[1]["settings"]["html"] = f"""<div style="display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:center;background:#2a1c22;color:#fff;border-radius:28px;padding:28px;" class="lll-quote-grid">
<img src="https://learnlooklocate.com/wp-content/uploads/2024/08/Dr.-Yara-Robertson-.jpg" alt="Dr. Yara Robertson" style="width:200px;height:240px;object-fit:cover;border-radius:18px;">
<div>
<h2 style="font-family:Montserrat,sans-serif;font-size:28px;font-weight:500;margin:0 0 12px;color:#fff;">Stay in the Know. Stay Empowered.</h2>
<blockquote style="font-family:Libre Baskerville,Georgia,serif;font-size:22px;font-weight:500;font-style:italic;margin:0 0 12px;">“The best patient is an empowered patient.”</blockquote>
<p style="font-family:Montserrat,sans-serif;font-size:16px;margin:0 0 8px;">— Dr. Yara Robertson, Breast Surgical Oncologist &amp; Learn Look Locate Medical Advisor</p>
<p style="font-family:Montserrat,sans-serif;font-size:16px;margin:0 0 16px;">Sign up to receive the latest medically guided education, expert insights, and meaningful updates from Learn Look Locate — delivered with clarity and care.</p>
{ck}
</div>
</div>
<style>@media(max-width:900px){{.lll-quote-grid{{grid-template-columns:1fr !important;}}}}</style>"""

    ids = {}

    def map_ids(o):
        if isinstance(o, dict):
            url, iid = o.get("url"), o.get("id")
            if isinstance(url, str) and "/uploads/" in url and iid not in (None, ""):
                ids[url] = iid
                ids[url.split("/")[-1]] = iid
            for v in o.values():
                map_ids(v)
        elif isinstance(o, list):
            for v in o:
                map_ids(v)

    map_ids(orig)

    def attach(o):
        if isinstance(o, dict):
            if "url" in o and isinstance(o.get("url"), str) and "/uploads/" in o["url"] and not o.get("id"):
                o["id"] = ids.get(o["url"]) or ids.get(o["url"].split("/")[-1]) or ""
            for v in o.values():
                attach(v)
        elif isinstance(o, list):
            for v in o:
                attach(v)

    attach(data)
    data["title"] = "What's New — D2 Cinematic"
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
