#!/usr/bin/env python3
"""Build the Step Into More logo SVG with the wordmark outlined to vector paths.
Source font: Inter (SIL OFL), instanced to wght=500 (Medium), opsz=14 (text).
Geometry (orbit, node, send-icon triangles) traced from the original PNG.
"""
import re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = "Inter-var.ttf"
FONTSIZE = 26.0
TRACKING = 1.5      # extra space added after each glyph, in viewBox units
CX = 105.0
BASELINES = {"STEP": 85.5, "INTO": 113.2, "MORE": 140.7}

f = TTFont(FONT)
instantiateVariableFont(f, {"wght": 500, "opsz": 14}, inplace=True)
upem = f["head"].unitsPerEm
cmap = f.getBestCmap()
gs = f.getGlyphSet()
scale = FONTSIZE / upem

def word_paths(word, baseline):
    # measure total advance
    advs = [gs[cmap[ord(c)]].width for c in word]
    total = sum(a * scale for a in advs) + TRACKING * (len(word) - 1)
    penx = CX - total / 2
    ds = []
    for c, adv in zip(word, advs):
        gname = cmap[ord(c)]
        spen = SVGPathPen(gs)
        # font y-up -> svg y-down: (scale, 0, 0, -scale, penx, baseline)
        tpen = TransformPen(spen, (scale, 0, 0, -scale, penx, baseline))
        gs[gname].draw(tpen)
        d = spen.getCommands()
        if d:
            ds.append(d)
        penx += adv * scale + TRACKING
    return " ".join(ds)

def round_d(d):
    return re.sub(r"-?\d+\.\d+", lambda m: f"{float(m.group()):.2f}", d)

text_paths = []
for w in ("STEP", "INTO", "MORE"):
    text_paths.append(round_d(word_paths(w, BASELINES[w])))

GEOM = '''  <!-- open orbit, split so it meets the node like a bead on a string -->
  <path d="M178.1 67.5 A80 80 0 0 1 38.9 145.0" stroke="currentColor" stroke-width="2.3" fill="none" stroke-linecap="round"/>
  <path d="M33.7 136.2 A80 80 0 0 1 136.3 26.4" stroke="currentColor" stroke-width="2.3" fill="none" stroke-linecap="round"/>
  <!-- start node, sitting on the orbit -->
  <circle cx="36.5" cy="140.5" r="5.2" stroke="currentColor" stroke-width="2.3" fill="none"/>
  <!-- send icon: two triangles sharing the right edge as one straight line -->
  <path d="M174.9 31.3 L130.2 45.9 L166.8 55.7 Z" stroke="currentColor" stroke-width="2.3" fill="none" stroke-linejoin="round"/>
  <path d="M154.6 52.4 L166.8 55.7 L161.1 72.8 Z" stroke="currentColor" stroke-width="2.3" fill="none" stroke-linejoin="round"/>'''

text_block = "\n".join(f'  <path d="{d}" fill="currentColor"/>' for d in text_paths)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="210" height="200" viewBox="0 0 210 200" fill="none" role="img" aria-label="Step Into More">
{GEOM}
  <!-- wordmark: Inter Medium, outlined to paths (font-independent) -->
{text_block}
</svg>
'''
with open("../step-into-more-logo.svg", "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote ../step-into-more-logo.svg")

# --- preview HTML (regenerated from same source) ---
inner_full = GEOM + "\n" + text_block
inner_mark = GEOM.replace('stroke-width="2.3"', 'stroke-width="2.6"')

def tile(cls, cap, height, inner, color):
    return f'''    <div class="tile {cls}">
      <div class="logo" style="color:{color}"><svg viewBox="0 0 210 200" height="{height}" fill="none" xmlns="http://www.w3.org/2000/svg">
{inner}
      </svg></div>
      <div class="cap">{cap}</div>
    </div>'''

html = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Step Into More — Logo Preview</title>
<style>
  :root{{ --ink:#16181d; }}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{ font-family:system-ui,sans-serif; background:#f4f2ee; color:#16181d; padding:40px; }}
  h1{{ font-size:20px; font-weight:600; margin-bottom:4px; }}
  .sub{{ font-size:13px; color:#7a818c; margin-bottom:32px; max-width:660px; }}
  .grid{{ display:flex; flex-wrap:wrap; gap:28px; align-items:flex-start; }}
  .tile{{ background:#fff; border:1px solid #e7e0d2; border-radius:14px; padding:28px; display:flex; flex-direction:column; align-items:center; gap:14px; }}
  .tile.dark{{ background:var(--ink); }}
  .cap{{ font-size:11px; letter-spacing:1px; text-transform:uppercase; color:#9aa0a8; }}
  .tile.dark .cap{{ color:#6b7280; }}
  .logo svg{{ display:block; width:auto; }}
  code{{ background:#eceae4; padding:1px 5px; border-radius:4px; font-size:12px; }}
</style>
</head>
<body>
  <h1>Step Into More — Logo</h1>
  <div class="sub">Vektor (SVG) · jede Koordinate aus dem Original-PNG getracet · Wortmarke in Inter Medium, in Pfade umgewandelt (font-unabhängig) · färbt sich über <code>currentColor</code> für hell/dunkel.</div>
  <div class="grid">
{tile("", "Volllogo · hell", 180, inner_full, "var(--ink)")}
{tile("dark", "Volllogo · dunkel", 180, inner_full, "#fff")}
{tile("", "Klein (78px)", 78, inner_full, "var(--ink)")}
{tile("", "Nur Zeichen", 120, inner_mark, "var(--ink)")}
  </div>
</body>
</html>
'''
with open("../logo-preview.html", "w", encoding="utf-8") as fh:
    fh.write(html)
print("wrote ../logo-preview.html")
