# Design bridge: Canva / HTML → native Elementor

This folder is the contract between a visual design and a WordPress page.

```
Canva  →  page.spec.json  →  HTML preview  →  approve  →  elementor-*.json  →  WP import
HTML   ↗
```

Canva is the artboard. The **spec** is the source of truth. Elementor is generated from the spec using native containers, headings, text, buttons, and images — the same approach that matched the What’s New HTML.

## Generate

```bash
python3 design-bridge/generate.py design-bridge/examples/hero-intro.spec.json --out /tmp/bridge-out
```

That writes:

- `elementor-hero-intro.json` — import in **Templates → Saved Templates**
- `hero-intro-preview.html` — browser check before import

## Spec section types

| `type` | Use |
|---|---|
| `hero` | Full-bleed photo, copy on the right |
| `split` | Cream paper, two text columns |
| `spotlight` | Photo band + featured card |
| `photo-header` | Photo band, copy on the right, stronger overlay |
| `chapter` | Photo pane + copy pane |
| `stack` | Simple boxed column |
| `html` | Partner mosaic, ConvertKit, anything native widgets cannot match |
| `magazine-grid` | Placeholder for Unlimited Elements post grid |

## Canva

Connect the **Canva** MCP in Cursor, then paste a design URL. The agent reads the design and fills a spec. This environment cannot call Canva until that MCP is authenticated.

## Import

1. Remove the previous Elementor template from the page.
2. Import the generated JSON.
3. Insert the template. Do not re-upload images that already live in Media Library.
