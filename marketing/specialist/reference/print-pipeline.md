# Reference: Print Pipeline (the tools)

How to turn an HTML asset into print-ready files the Aachen printer accepts. The toolchain lives in `marketing/assets/html/_print/` (Node, Puppeteer, sharp, qrcode).

## The printer's hard requirements
- Format: 300dpi JPG, TIF, or PDF. We deliver JPG (sRGB), because PDF/X and CMYK need pro tools we do not run.
- Bleed: 3mm all around. An embedded sRGB profile is accepted as the fallback for digital print.
- No transparency, no layers, no rotations. Rasterizing to an image satisfies all three and embeds fonts automatically.

## Dimensions (trim plus 3mm bleed, at 300dpi)
- A5 flyer: trim 148x210mm, with bleed 154x216mm = 1819x2550 px.
- Business card: trim 85x55mm, with bleed 91x61mm = 1075x722 px.
- Device scale factor for 300dpi from a 96dpi browser: 3.125.
- Keep text and key elements a safe margin (about 5mm) inside the trim. Full-bleed backgrounds run to the bleed edge. Corners square (no border-radius for print).

## Commands
- `cd marketing/assets/html/_print`
- `node gen-qr.js` embeds the official Lovable QR into the flyer HTML.
- `node render.js` renders flyer front and back to 300dpi JPEGs.
- `node cards.js` renders the business card front plus both back variants, preview PNGs and print JPEGs.
- After rendering, open the JPEG and confirm bleed, the QR, and that metadata reads 300dpi sRGB.

## Gotchas learned
- Chrome "Save as PDF" does not meet the spec (RGB, no bleed, not PDF/X). Always render.
- A large base64 QR can hang the live preview server; verify the rendered file instead of the preview.
- Re-embed the official QR with `gen-qr.js` rather than generating a fresh one, so the destination never drifts.
