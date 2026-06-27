// Embed the OFFICIAL Lovable QR (stepintomore-qr.png, points to
// https://www.stepintomore.co) into the flyer HTML as base64, replacing
// whatever QR payload is currently in the <img>.
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = join(__dirname, '..', 'flyer-icm-wedge-de.html');
const qrPath = join(__dirname, '..', 'stepintomore-qr.png'); // official Lovable QR

const base64 = readFileSync(qrPath).toString('base64');

let html = readFileSync(htmlPath, 'utf8');
html = html.replace(
  /(<img src="data:image\/png;base64,)[^"]*(" alt="QR)/,
  `$1${base64}$2`
);
writeFileSync(htmlPath, html);
console.log('Official Lovable QR embedded into flyer HTML (www.stepintomore.co)');
