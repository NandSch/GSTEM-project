// Generates assets/satellite.svg - a procedural, aerial-imagery style ground
// texture (fields, forest, river, roads, town) used as the base of the 3D map.
// Run: node scripts/gen-satellite.js
const fs = require('fs');
const path = require('path');

const W = 1800;
const H = 1800;

// deterministic PRNG so the texture is stable between runs
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const rnd = mulberry32(20240929);
const r = (min, max) => min + rnd() * (max - min);
const pick = (arr) => arr[Math.floor(rnd() * arr.length)];
const n = (v) => Math.round(v * 100) / 100;

const FIELD_COLORS = [
  '#7d9c57', '#8aa85f', '#6e8c4b', '#9fae6a', '#b3a878',
  '#a89a63', '#57713d', '#c2b98a', '#4f6a38', '#94a866',
  '#87a05b', '#6b8750', '#b9b184',
];
const FOREST = ['#33502d', '#2c4527', '#3b5a33', '#28401f'];

const out = [];
out.push(`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`);

out.push(`<defs>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.5 0.5 0.5 0 0"/>
  </filter>
  <filter id="softblur" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="14"/>
  </filter>
  <filter id="treeblur" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="1.6"/>
  </filter>
  <filter id="roofnoise" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="turbulence" baseFrequency="0.9" numOctaves="2" seed="11" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0.35 0.35 0.35 0 0"/>
  </filter>
</defs>`);

// base terrain
out.push(`<rect width="${W}" height="${H}" fill="#5f7a43"/>`);
out.push(`<rect width="${W}" height="${H}" fill="#6b8549" filter="url(#softblur)" opacity="0.6"/>`);

// ---- rotated patchwork of fields -------------------------------------------
const tilt = -13;
out.push(`<g transform="rotate(${tilt} 900 900)" stroke="#495c33" stroke-width="2.5">`);
for (let y = -260; y < H + 260; y += 232) {
  for (let x = -260; x < W + 260; x += 232) {
    const w = 232 * r(0.92, 1.06);
    const h = 232 * r(0.92, 1.06);
    const cx = x + 116 + r(-10, 10);
    const cy = y + 116 + r(-10, 10);
    const a = r(-4, 4);
    const fill = pick(FIELD_COLORS);
    out.push(`<g transform="translate(${n(cx)} ${n(cy)}) rotate(${n(a)})">`);
    out.push(`<rect x="${n(-w / 2)}" y="${n(-h / 2)}" width="${n(w)}" height="${n(h)}" fill="${fill}"/>`);
    // crop rows on a subset of parcels
    if (rnd() > 0.45) {
      const rows = Math.floor(r(6, 13));
      const step = w / rows;
      const rc = rnd() > 0.5 ? 'rgba(0,0,0,0.10)' : 'rgba(255,255,255,0.09)';
      for (let i = 1; i < rows; i++) {
        out.push(`<line x1="${n(-w / 2 + i * step)}" y1="${n(-h / 2)}" x2="${n(-w / 2 + i * step)}" y2="${n(h / 2)}" stroke="${rc}" stroke-width="1.4" stroke-dasharray="9 6"/>`);
      }
    }
    out.push(`</g>`);
  }
}
out.push(`</g>`);

// ---- forest / woodland ------------------------------------------------------
function forest(cx, cy, radius, blobs) {
  // soft dark under-canopy to give the woodland mass
  out.push(`<g filter="url(#softblur)" opacity="0.55">`);
  for (let i = 0; i < Math.round(blobs / 6); i++) {
    const ang = rnd() * Math.PI * 2;
    const dist = Math.pow(rnd(), 0.7) * radius * 0.75;
    out.push(`<circle cx="${n(cx + Math.cos(ang) * dist)}" cy="${n(cy + Math.sin(ang) * dist * 0.85)}" r="${n(r(26, 46))}" fill="#2b4326"/>`);
  }
  out.push(`</g>`);
  // individual tree crowns, varied size + tone, with a lit side
  out.push(`<g filter="url(#treeblur)">`);
  for (let i = 0; i < blobs; i++) {
    const ang = rnd() * Math.PI * 2;
    const dist = Math.pow(rnd(), 0.6) * radius;
    const bx = cx + Math.cos(ang) * dist;
    const by = cy + Math.sin(ang) * dist * 0.85;
    const br = r(6, 15);
    out.push(`<circle cx="${n(bx)}" cy="${n(by)}" r="${n(br)}" fill="${pick(FOREST)}"/>`);
    out.push(`<circle cx="${n(bx - br * 0.25)}" cy="${n(by - br * 0.3)}" r="${n(br * 0.55)}" fill="#4a6b3c" opacity="0.55"/>`);
  }
  out.push(`</g>`);
}
forest(210, 260, 200, 150);
forest(1560, 340, 220, 170);
forest(360, 1620, 210, 150);
forest(1620, 1520, 190, 130);
forest(1230, 1750, 160, 100);

// ---- river ------------------------------------------------------------------
const river = 'M -40 1180 C 240 1120, 420 1010, 620 1040 C 830 1072, 980 1210, 1180 1200 C 1380 1190, 1520 1080, 1860 1120';
out.push(`<path d="${river}" fill="none" stroke="#6f7f5c" stroke-width="46" stroke-linecap="round" opacity="0.9"/>`);
out.push(`<path d="${river}" fill="none" stroke="#4f7f9c" stroke-width="30" stroke-linecap="round"/>`);
out.push(`<path d="${river}" fill="none" stroke="#6ba0bd" stroke-width="18" stroke-linecap="round" opacity="0.8"/>`);

// ---- town -------------------------------------------------------------------
out.push(`<rect x="690" y="620" width="540" height="470" rx="34" fill="#8d8779" opacity="0.95"/>`);
out.push(`<rect x="690" y="620" width="540" height="470" rx="34" fill="none" stroke="#7a7568" stroke-width="4" opacity="0.8"/>`);
out.push(`<g stroke="#6f6a5f" stroke-width="11" fill="none" opacity="0.9">
  <path d="M690 760 H1230"/>
  <path d="M690 960 H1230"/>
  <path d="M830 620 V1090"/>
  <path d="M1060 620 V1090"/>
</g>`);

// ---- roads ------------------------------------------------------------------
const mainRoad = 'M -40 560 C 300 520, 620 470, 900 430 C 1180 390, 1480 300, 1860 240';
out.push(`<path d="${mainRoad}" fill="none" stroke="#b7b2a6" stroke-width="20" stroke-linecap="round"/>`);
out.push(`<path d="${mainRoad}" fill="none" stroke="#d9d5cb" stroke-width="12" stroke-linecap="round"/>`);
out.push(`<path d="${mainRoad}" fill="none" stroke="#efece4" stroke-width="2.4" stroke-dasharray="26 22" stroke-linecap="round"/>`);

const crossRoad = 'M 1210 -40 C 1180 320, 1140 620, 1180 900 C 1220 1180, 1300 1480, 1330 1860';
out.push(`<path d="${crossRoad}" fill="none" stroke="#b7b2a6" stroke-width="16" stroke-linecap="round"/>`);
out.push(`<path d="${crossRoad}" fill="none" stroke="#d9d5cb" stroke-width="9" stroke-linecap="round"/>`);

const sideRoads = [
  'M 180 900 C 380 860, 560 880, 760 830',
  'M 640 1180 C 760 1120, 860 1080, 940 980',
  'M 1080 1320 C 1180 1260, 1300 1220, 1460 1240',
  'M 420 1380 C 520 1320, 640 1300, 740 1240',
  'M 1420 620 C 1520 600, 1620 580, 1760 560',
];
for (const d of sideRoads) {
  out.push(`<path d="${d}" fill="none" stroke="#a9a498" stroke-width="9" stroke-linecap="round"/>`);
  out.push(`<path d="${d}" fill="none" stroke="#cfccc2" stroke-width="5" stroke-linecap="round"/>`);
}

// ---- scattered trees / hedgerows -------------------------------------------
out.push(`<g>`,);
for (let i = 0; i < 130; i++) {
  const x = rnd() * W;
  const y = rnd() * H;
  out.push(`<circle cx="${n(x)}" cy="${n(y)}" r="${n(r(5, 13))}" fill="${pick(FOREST)}" opacity="0.75"/>`);
}
out.push(`</g>`);

// ---- global grain -----------------------------------------------------------
out.push(`<rect width="${W}" height="${H}" filter="url(#grain)" opacity="0.5" style="mix-blend-mode:overlay"/>`);

out.push(`</svg>`);

const dest = path.join(__dirname, '..', 'assets', 'satellite.svg');
fs.mkdirSync(path.dirname(dest), { recursive: true });
fs.writeFileSync(dest, out.join('\n'));
console.log('wrote', dest, (out.join('\n').length / 1024).toFixed(1) + 'kb');
