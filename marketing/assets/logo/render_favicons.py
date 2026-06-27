#!/usr/bin/env python3
"""Rasterize the mark-only logo (orbit + node + send icon) to favicon PNGs.
Pure Pillow (no native SVG renderer needed). Transparent background, ink color.
Small sizes use a heavier stroke so the line-art stays legible.
"""
import math
from PIL import Image, ImageDraw

INK = (22, 24, 29, 255)          # #16181d
CX, CY, R = 105.0, 100.0, 80.0   # orbit, in design units
# tight square viewBox around the mark, centered on the orbit
VX, VY, VSIDE = 17.0, 12.0, 176.0
SS = 8                            # supersampling factor

# arc angle ranges (deg, 0=3o'clock, clockwise+), matching the SVG gaps
ARC1 = (336.0, 145.7)   # right + bottom, up to the node
ARC2 = (153.1, 293.0)   # left + top, up to the plane opening
NODE = (36.5, 140.5, 5.2)
TRI_BIG = [(174.9, 31.3), (130.2, 45.9), (166.8, 55.7)]
TRI_SMALL = [(154.6, 52.4), (166.8, 55.7), (161.1, 72.8)]


def render(size, stroke):
    n = size * SS
    k = n / VSIDE
    img = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    sw = max(1, round(stroke * k))

    def P(x, y):
        return ((x - VX) * k, (y - VY) * k)

    # orbit bbox
    bb = [P(CX - R, CY - R), P(CX + R, CY + R)]
    bbox = [bb[0][0], bb[0][1], bb[1][0], bb[1][1]]
    d.arc(bbox, ARC1[0], ARC1[1], fill=INK, width=sw)
    d.arc(bbox, ARC2[0], ARC2[1], fill=INK, width=sw)

    # round-cap fakes at the four open arc ends
    for ang in (ARC1[0], ARC1[1], ARC2[0], ARC2[1]):
        ex = CX + R * math.cos(math.radians(ang))
        ey = CY + R * math.sin(math.radians(ang))
        px, py = P(ex, ey)
        rr = sw / 2
        d.ellipse([px - rr, py - rr, px + rr, py + rr], fill=INK)

    # node ring (drawn on top, like a bead on the string)
    nx, ny = P(NODE[0], NODE[1]); nr = NODE[2] * k
    d.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], outline=INK, width=sw)

    # send icon triangles (closed, rounded joins)
    for tri in (TRI_BIG, TRI_SMALL):
        pts = [P(x, y) for x, y in tri] + [P(*tri[0])]
        d.line(pts, fill=INK, width=sw, joint="curve")

    return img.resize((size, size), Image.LANCZOS)


# (filename, size, stroke in design units)
JOBS = [
    ("favicon-16.png", 16, 7.5),
    ("favicon-32.png", 32, 4.5),
    ("apple-touch-icon-180.png", 180, 2.6),
    ("icon-512.png", 512, 2.6),
]
for fn, sz, sw in JOBS:
    render(sz, sw).save("../favicons/" + fn)
    print("wrote ../favicons/" + fn, f"({sz}px, stroke {sw})")
