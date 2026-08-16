# Import the D2 What’s New page into Elementor

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
