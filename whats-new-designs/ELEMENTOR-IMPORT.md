# Import the D2 What’s New page into Elementor

File: `elementor-whats-new-d2.json`

This is an Elementor **page template** (export format `0.4`), rebuilt from the finalized HTML preview. Card and partner links go to the live article permalinks. Hover, Montserrat body type, pill buttons, larger partner logos, and the stronger Education overlay are included. The ConvertKit newsletter form from the current What’s New page is embedded.

## Images — do not re-upload

Every photo and logo already uses a `learnlooklocate.com/wp-content/uploads/...` URL from the live Media Library. The template does **not** bundle image files. After import, Elementor loads those existing files. You do not need to import a media zip or upload the images again.

If the importer asks “Import images?”, you can leave that off. These are HTML widgets pointing at URLs already on the site, not new attachments.

## How to import

1. In WordPress, open **Templates → Saved Templates** (or **Elementor → Saved Templates**).
2. Click **Import Templates**.
3. Upload `elementor-whats-new-d2.json`.
4. Open the **What’s New** page with Elementor (or create a new page).
5. Insert **What's New — D2 Cinematic**.
6. Publish. Hide the default page title if the theme still shows one.

## After import

- Grids are HTML widgets so the D2 magazine layout and hover motion stay intact without Unlimited Elements.
- To swap a card, edit the HTML widget for that section and change the `href`, image, date, or title.
- The live ConvertKit form (`forms/8767355`) is in the newsletter section.

## Preview HTML

`whats-new-preview.html` — same layout as this import.
