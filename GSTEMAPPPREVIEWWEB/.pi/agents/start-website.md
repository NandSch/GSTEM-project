# Start Website

A skill for the GSTEMAPPPREVIEWWEB project to start a local web server and open the website in the browser.

## How to Use

When asked to "start the website" or "run the website", follow these steps:

1. **Start HTTP server**: Launch Python's built-in HTTP server on port 8080
   ```bash
   python -m http.server 8080
   ```

2. **Open in browser**: Navigate to http://localhost:8080 in your web browser

## Implementation Notes

- This project is a static site — no build process. Files are served directly from the project root.
- The server runs in a separate terminal window; stop it with Ctrl+C.
- An internet connection is required: the map loads MapLibre GL from a CDN and fetches map tiles at runtime.
- The website must be opened over HTTP (not `file://`) so the map tiles and CDN resources load correctly.
- All application logic lives in inline `<script>` blocks in `index.html`; there is no separate JS bundle.

## Pages

- `#page-kaart` — live tracking: MapLibre GL satellite map (Esri World Imagery + place labels, AWS Terrarium terrain), the device trail and heading marker, and the live telemetry panel.
- `#page-code` — G-code editor with upload panel.

## Map Details

- Library: MapLibre GL JS (loaded from `https://unpkg.com/maplibre-gl@<version>/dist/...`).
- Imagery: Esri World Imagery — `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`.
- Labels: Esri World Boundaries and Places.
- Terrain: AWS Terrarium DEM — `https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png`.
- The trail is defined as the `TRAIL` array (local map pixels) in `index.html` and converted to real lat/lon centred on the device position `52.370012, 4.895431`.

## Related Files

- `index.html` — main HTML file, including all inline scripts (map, telemetry, editor, setup popup).
- `style.css` — stylesheet (design tokens, layout, HUD, marker styles).
- `assets/` — static assets.
- `scripts/` — legacy helper scripts (not used by the running site).
- `.vscode/launch.json` — Chrome debug config pointing at http://localhost:8080.

## Legacy / Unused

- `assets/satellite.svg` and `scripts/gen-satellite.js` were part of the old placeholder map and are no longer loaded by the page.
