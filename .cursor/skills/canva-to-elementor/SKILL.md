# Canva / HTML → native Elementor

Use this skill whenever the user wants a WordPress page from a **Canva design** or an **approved HTML mockup**, imported as **native Elementor** widgets (containers, headings, text, buttons, images).

Do **not** restyle an old Elementor export. Rebuild from a page spec that matches the design.

## Pipeline (always)

```
Canva design  →  page spec JSON  →  HTML preview (approve)  →  Elementor import JSON
     or HTML  ↗
```

1. **Design** — Canva file and/or HTML mockup. Refine until the user signs off.
2. **Spec** — `design-bridge/examples/*.spec.json` shape. One object per section (`hero`, `split`, `spotlight`, `photo-header`, `chapter`, `stack`, `html`, `magazine-grid`).
3. **Generate** — `python3 design-bridge/generate.py path/to/page.spec.json --out path/to/out`
4. **Import** — WordPress → Templates → Import Templates → insert the JSON. Delete any previous template on the page first.

## Canva (when MCP is connected)

1. Resolve the design URL (`Canva:resolve-shortlink` or extract `D…` id).
2. `Canva:get-design` (title, page count), `Canva:get-design-thumbnail` (layout, color, overlay), `Canva:get-design-content` (copy).
3. Map each Canva page/frame to a **section type**:
   - Full-bleed photo + copy on one side → `hero` or `photo-header`
   - Two text columns → `split`
   - Photo left / copy right → `chapter`
   - Card mosaic / partner tiles → `html` (native widgets cannot match that mosaic cleanly)
   - Post listing → `magazine-grid` (Unlimited Elements widget in WP; spec only reserves the slot)
4. Write the spec using live `wp-content/uploads` URLs (do not re-upload media).
5. Generate HTML, let the user approve, then generate Elementor.

If Canva MCP status is `needsAuth`, tell the user to connect Canva in Cursor, then continue. Do not invent layout from memory.

## Native Elementor mapping

| Design | Elementor |
|---|---|
| Section background photo | Container `background_image` + overlay |
| Cinematic scrim | Container `custom_css` `selector::after { linear-gradient… }` |
| H1 / H2 | Heading widget |
| Body copy | Text editor, Montserrat 22px / 20px mobile |
| CTA | Button, pill, brand accent `#c44b6a` |
| Single photo | Image widget |
| Two columns | Nested containers, widths 50/50 or 46/54 |
| Partner covers / odd mosaic | HTML widget only |
| Blog/education cards | Magazine grid widget (dynamic posts) |

## Rules learned from What’s New

- Never start from the old purple-wave export if the HTML is a new layout.
- HTML widgets are allowed only for mosaics and third-party forms (ConvertKit).
- Images stay on existing Media Library URLs/IDs.
- After import, the user must **replace** the previous template, not stack it.

## Brand tokens

Read `design-bridge/tokens.lll.json` unless the user supplies another kit.
