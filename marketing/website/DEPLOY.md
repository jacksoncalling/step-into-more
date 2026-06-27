# Step Into More — Website (deploy bundle)

Self-contained static site. Drop this whole folder into any static host.

## Contents
```
website/
├── index.html        ← the site (bilingual DE/EN, inline SVG logo)
└── favicons/         ← all icons, referenced as favicons/… (relative)
```
The only external dependency is the Google Fonts (Inter) `@import`, which loads from
Google's CDN at runtime. Everything else — logo, copy, favicons, the DE/EN toggle — is
inside this folder.

## Deploy options

**Vercel / Netlify / Cloudflare Pages (static — recommended, unchanged):**
- Drag this `website/` folder into the dashboard, or point the project at it.
- Set the output/root directory to this folder. No build command needed.
- Serves `index.html` exactly as authored.

**Lovable:**
- Lovable rebuilds as React, so paste `index.html` and tell it explicitly:
  > "Use this HTML as a single static page exactly as provided. Do not redesign or
  > restructure it. Keep the inline SVG logo and the DE/EN language toggle (the
  > JavaScript and `data-i18n` attributes) untouched. Just publish it."
- Then verify: (1) logo = open circle + paper-plane, (2) the DE/EN slider flips the language.

## Domains (running Lovable + Vercel under one brand)
One hostname points to one host. To use both, split by subdomain:
- `stepintomore.co` (+ `www`) → wherever the marketing site lives
- `app.stepintomore.co`, `terroir.stepintomore.co`, … → Vercel apps (add a CNAME per subdomain)

## Notes
- Default language: **German**; a visitor's toggle choice is remembered (localStorage).
- To regenerate favicons or the logo, see `../assets/logo/` (build scripts).
- This folder is a copy-for-deploy; the favicons' source of truth is `../assets/favicons/`.
