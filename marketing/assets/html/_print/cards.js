// Business card: render on-screen previews AND 300dpi print-ready JPEGs
// (3mm bleed) for both kicker variants. Front is shared across variants.
// Card trim 85x55mm + 3mm bleed = 91x61mm => ~1075x721px @ 300dpi.
import puppeteer from 'puppeteer-core';
import sharp from 'sharp';
import { readFileSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(__dirname, '..', 'business-card.html');
const outDir = join(__dirname, '..');
const baseUrl = pathToFileURL(htmlPath).href;
const baseHtml = readFileSync(htmlPath, 'utf8');

const variants = [
  { id: 'v1', role: 'KI-Berater für den Mittelstand', kicker: '<b>Step Into More.</b> The future is wide open.' },
  { id: 'v3', role: 'KI-Berater für den Mittelstand', kicker: '<b>Ihre KI,</b> gebaut auf Ihrem Wissen.' },
];

const DPI = 300, DSF = DPI / 96;

// Print overrides: grow card to bleed size, square corners, no shadow,
// keep safe margins by adding 3mm to insets, extend amber edge into bleed.
const printCss = `
  .stage{ padding:0 !important; gap:0 !important; background:#fff !important; }
  .lbl{ display:none !important; }
  .card{ width:91mm !important; height:61mm !important; border-radius:0 !important; box-shadow:none !important; }
  .front .edge{ height:5.4mm !important; }
  .back{ padding:10mm 11mm !important; }
  .back .mini-logo{ top:9mm !important; right:10mm !important; }
`;

function variantHtml(v) {
  return baseHtml
    .replace(/(<div class="role">)[^<]*(<\/div>)/, `$1${v.role}$2`)
    .replace(/(<div class="kicker">)[\s\S]*?(<\/div>)/, `$1${v.kicker}$2`);
}

const browser = await puppeteer.launch({
  executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  headless: 'new',
  args: ['--no-sandbox', '--force-color-profile=srgb'],
});

async function shoot(html, selector, { print }) {
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 560, deviceScaleFactor: print ? DSF : 3 });
  await page.goto(baseUrl, { waitUntil: 'domcontentloaded' });
  await page.setContent(html, { waitUntil: 'networkidle0' });
  if (print) await page.addStyleTag({ content: printCss });
  await page.evaluateHandle('document.fonts.ready');
  const buf = await (await page.$(selector)).screenshot({ type: 'png' });
  await page.close();
  return buf;
}

async function toJpg(buf, name) {
  const m = await sharp(buf).metadata();
  await sharp(buf).withMetadata({ density: DPI })
    .jpeg({ quality: 100, chromaSubsampling: '4:4:4' })
    .toFile(join(outDir, name));
  console.log(`${name}: ${m.width}x${m.height}px @ ${DPI}dpi`);
}

// Shared front (print)
await toJpg(await shoot(baseHtml, '.card.front', { print: true }), 'card-front.jpg');

for (const v of variants) {
  const html = variantHtml(v);
  // on-screen preview (rounded, for review)
  const pv = await shoot(html, '.card.back', { print: false });
  await sharp(pv).toFile(join(outDir, `card-back-${v.id}.png`));
  console.log(`card-back-${v.id}.png (preview)`);
  // print-ready
  await toJpg(await shoot(html, '.card.back', { print: true }), `card-back-${v.id}.jpg`);
}

await browser.close();
