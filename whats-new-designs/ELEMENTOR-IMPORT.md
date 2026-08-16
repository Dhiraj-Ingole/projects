# Import the D2 What’s New page into Elementor

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

Open this single HTML file before importing:

- `whats-new-preview.html`
- Local: `http://localhost:3000/whats-new-preview.html`

It is the same layout, links, and hover as the Elementor JSON.
