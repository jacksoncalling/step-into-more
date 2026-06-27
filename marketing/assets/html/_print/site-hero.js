// Screenshot the index.html hero to verify the i18n object parses and the
// new recognition-arc hero renders (default DE).
import puppeteer from 'puppeteer-core';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(__dirname, '..', '..', '..', 'website', 'index.html');

const browser = await puppeteer.launch({
  executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  headless: 'new',
  args: ['--no-sandbox', '--force-color-profile=srgb'],
});
const page = await browser.newPage();
const errors = [];
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', e => errors.push('PAGEERROR: ' + e.message));
await page.setViewport({ width: 1100, height: 760, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle0' });
await page.evaluateHandle('document.fonts.ready');
// what the hero actually shows after setLang() runs
const heroText = await page.evaluate(() => ({
  eyebrow: document.querySelector('.hero .eyebrow')?.textContent,
  h1: document.querySelector('.hero h1')?.textContent,
}));
await page.screenshot({ path: join(__dirname, '..', '..', '..', 'website', 'site-hero-check.png'), type: 'png' });
await browser.close();
console.log('JS errors:', errors.length ? errors : 'none');
console.log('hero eyebrow:', heroText.eyebrow);
console.log('hero h1:', heroText.h1);
