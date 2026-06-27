# Favicons — Step Into More

Mark-only logo (orbit + node + send icon), rendered from `step-into-more-logo.svg`.
Regenerate with `../logo/render_favicons.py` (PNG/ICO) and `icon.svg` (hand-kept, dark-mode aware).

## Files
| File | Size | Use |
|------|------|-----|
| `icon.svg` | vector | **Primary** modern favicon — crisp at every size, auto-switches to white on dark browser tabs |
| `favicon.ico` | 16/32/48 | Legacy fallback (older browsers, bookmarks) |
| `favicon-16.png` / `favicon-32.png` | 16/32 | Explicit PNG tab icons (heavier stroke for legibility) |
| `apple-touch-icon-180.png` | 180 | iOS / iPadOS home-screen icon |
| `icon-512.png` | 512 | PWA / Android manifest icon, social previews |

All PNGs are ink (`#16181d`) on a transparent background.

## Paste into your site `<head>`
```html
<link rel="icon" href="/favicons/icon.svg" type="image/svg+xml">
<link rel="icon" href="/favicons/favicon.ico" sizes="any">
<link rel="icon" href="/favicons/favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="/favicons/favicon-16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="/favicons/apple-touch-icon-180.png">
```

## Note on the 16px size
This is a detailed line-mark, so at 16px the send icon and node largely collapse into a
ring. The `icon.svg` keeps it sharp on browsers that support SVG favicons (all modern ones).
If a legible 16px raster matters, the cleanest option is a simplified small mark
(e.g. the send icon alone) — ask and I'll generate it.
