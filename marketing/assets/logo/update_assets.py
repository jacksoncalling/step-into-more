#!/usr/bin/env python3
"""Replace every embedded logo (viewBox 0 0 210 200) in the website, business card
and flyer with the corrected, outlined master logo. Also wires favicons into the site.
Full logos (those that had <text>) get geometry + outlined wordmark; mark-only logos
get geometry only. SVG opening tags (height/aria/CSS) are preserved.
"""
import re
from pathlib import Path

MASTER = Path("../step-into-more-logo.svg").read_text(encoding="utf-8")
m = re.search(r"<svg[^>]*>(.*)</svg>", MASTER, re.S)
lines = [l.strip() for l in m.group(1).strip().splitlines()
         if l.strip() and not l.strip().startswith("<!--")]
geom = [l for l in lines if 'fill="none"' in l]          # arcs, node, triangles
text = [l for l in lines if 'fill="currentColor"' in l]   # outlined STEP/INTO/MORE

def block(elems, indent):
    pad = " " * indent
    return "\n" + "\n".join(pad + e for e in elems) + "\n" + " " * (indent - 2)

FULL = block(geom + text, 8)
MARK = block(geom, 8)

def swap_logos(html):
    def repl(mo):
        body = mo.group(0)
        open_tag = re.match(r"<svg[^>]*>", body).group(0)
        inner = FULL if "<text" in body else MARK
        return open_tag + inner + "</svg>"
    return re.sub(r'<svg[^>]*viewBox="0 0 210 200"[^>]*>.*?</svg>', repl, html, flags=re.S)

TARGETS = [
    "../../website/index.html",
    "../html/business-card.html",
    "../html/flyer-icm-wedge-de.html",
]
for t in TARGETS:
    p = Path(t)
    html = p.read_text(encoding="utf-8")
    n = len(re.findall(r'<svg[^>]*viewBox="0 0 210 200"', html))
    html = swap_logos(html)
    p.write_text(html, encoding="utf-8")
    print(f"{p.name}: swapped {n} logo(s)")

# --- favicons into the website <head> ---
site = Path("../../website/index.html")
html = site.read_text(encoding="utf-8")
if "rel=\"icon\"" not in html:
    links = (
        '  <link rel="icon" href="../assets/favicons/icon.svg" type="image/svg+xml">\n'
        '  <link rel="icon" href="../assets/favicons/favicon.ico" sizes="any">\n'
        '  <link rel="icon" href="../assets/favicons/favicon-32.png" type="image/png" sizes="32x32">\n'
        '  <link rel="icon" href="../assets/favicons/favicon-16.png" type="image/png" sizes="16x16">\n'
        '  <link rel="apple-touch-icon" href="../assets/favicons/apple-touch-icon-180.png">\n'
    )
    html = html.replace("</head>", links + "</head>", 1)
    site.write_text(html, encoding="utf-8")
    print("website: favicon links added")
else:
    print("website: favicon links already present")
