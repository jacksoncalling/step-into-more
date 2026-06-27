// Render each .page of the flyer to a 300dpi print-ready JPEG with 3mm bleed.
// A5 trim 148x210mm + 3mm bleed = 154x216mm => 1819x2551px @ 300dpi.
import puppeteer from 'puppeteer-core';
import sharp from 'sharp';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(__dirname, '..', 'flyer-icm-wedge-de.html');
const outDir = join(__dirname, '..');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const DPI = 300;
const DSF = DPI / 96; // 3.125

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: 'new',
  args: ['--no-sandbox', '--force-color-profile=srgb'],
});
const page = await browser.newPage();
await page.setViewport({ width: 640, height: 1000, deviceScaleFactor: DSF });
await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle0' });
await page.evaluateHandle('document.fonts.ready');

const targets = [
  { sel: '.page.front', out: 'flyer-front.jpg' },
  { sel: '.page.back', out: 'flyer-back.jpg' },
];

for (const t of targets) {
  const el = await page.$(t.sel);
  const pngBuf = await el.screenshot({ type: 'png' });
  const meta = await sharp(pngBuf).metadata();
  await sharp(pngBuf)
    .withMetadata({ density: DPI })
    .jpeg({ quality: 100, chromaSubsampling: '4:4:4' })
    .toFile(join(outDir, t.out));
  console.log(`${t.out}: ${meta.width}x${meta.height}px @ ${DPI}dpi`);
}

await browser.close();
console.log('done');
