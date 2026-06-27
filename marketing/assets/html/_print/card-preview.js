// Quick on-screen preview of the business card (both sides side by side).
import puppeteer from 'puppeteer-core';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(__dirname, '..', 'business-card.html');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: 'new',
  args: ['--no-sandbox', '--force-color-profile=srgb'],
});
const page = await browser.newPage();
await page.setViewport({ width: 900, height: 520, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle0' });
await page.evaluateHandle('document.fonts.ready');
const el = await page.$('.stage');
await el.screenshot({ path: join(__dirname, '..', 'card-preview.png'), type: 'png' });
await browser.close();
console.log('card-preview.png written');
