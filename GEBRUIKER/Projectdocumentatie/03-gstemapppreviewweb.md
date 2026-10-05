# 03 · Map `GSTEMAPPPREVIEWWEB` — de webdemo

Oorspronkelijke locatie: `C:\Users\Nand Schoovaerts\Downloads\GSTEMAPPPREVIEWWEB`.
Gekopieerd naar: `GSTEMAPPPREVIEWWEB/`.

Een **statische webversie** van de G-Stem laptopapp-mock-up. Geen framework, geen buildstap:
alles wordt direct geserveerd. De app draait in de browser en haalt kaartmateriaal online op.

## Git-geschiedenis

```text
1b7658b  After polish
7112d12  Met kaart en code.
492a993  Base website with popup, placeholder map and realtime data
```

Branch: `master`.

## Bestandsstructuur

```text
GSTEMAPPPREVIEWWEB/
├── index.html          # HTML + alle inline scripts (kaart, telemetrie, editor, popup, API)
├── style.css           # volledige stylesheet (design tokens, layout, HUD, markers, API-pagina)
├── api-handleiding.html# doorverwijspagina naar index.html#page-api (oude losse API-doc)
├── assets/
│   └── satellite.svg   # procedureel gegenereerde satelliettextuur (1800×1800) — legacy
├── scripts/
│   └── gen-satellite.js# Node-script dat satellite.svg genereert — legacy, niet meer geladen
├── .pi/agents/
│   └── start-website.md# skill/handleiding: website lokaal starten
├── .vscode/
│   └── launch.json     # Chrome-debugconfig naar http://localhost:8080
├── server.log          # log van de lokale http.server
└── .git/               # repositoryhistoriek
```

## Starten

```bash
cd GSTEMAPPPREVIEWWEB
python -m http.server 8080
# open http://localhost:8080
```

Vereisten en aandachtspunten (uit `.pi/agents/start-website.md`):
- **Internet nodig**: MapLibre GL komt van een CDN en de kaarttegels worden live opgehaald.
- **Via HTTP openen**, niet via `file://`, anders laden de tegels/CDN-resources niet goed.
- Alle applicatielogica zit in **inline `<script>`-blokken** in `index.html`; er is geen aparte JS-bundel.
- Stop de server met Ctrl+C.

## Pagina's / routing

De app werkt met **hash-routing**: `#page-kaart` (standaard), `#page-code` en `#page-api`. De
navigatie (`.island-nav`) toont twee statusbolletjes (USB, Device) en knoppen **Kaart**, **Code**
en **API**.

### `#page-kaart` — Live Tracking

**Links: MapLibre GL 3D-kaart.**
- Kaartstijl volledig in `index.html` gedefinieerd:
  - Satellietbeeld: Esri World Imagery
    `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`
  - Plaatslabels: Esri World Boundaries and Places.
  - Terrein: AWS Terrarium DEM
    `https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png` (encoding `terrarium`),
    met `setTerrain(..., exaggeration: 1.35)`.
- Beginpunt `MAP_START = { lat: 52.370012, lon: 4.895431 }` (Amsterdam).
- De afgelegde route (`TRAIL`) is een reeks lokale kaartpixels die met `PX_TO_M = 1.5` en de
  breedtegraad-correctie naar echte lat/lon wordt omgezet, gecentreerd rond het toestel.
- Lagen: `trail-shadow` (donkere gloed), `trail-path` (rode lijn `#ff2f2f`), `trail-dash`
  (witte "marching ants"-stippellijn, geanimeerd via `setInterval` met een `dashSeq`).
- **Toestelmarker**: SVG met pulserende cirkel, halo, stip en richtingspijl; rotatie volgt de
  koers en lijnt uit met de kaart (`rotationAlignment: 'map'`). Aparte **startmarker** op het begin
  van de route.
- **HUD**: kompas (N), zoomknoppen (+/−, met animatie), dynamische schaalbalk (`updateScale()`),
  "LIVE VOLGING"-indicator en een `map-haze`-overlay.
- Fallback: als `maplibregl` ontbreekt, verschijnt een melding dat de kaart niet geladen kon worden.

**Rechts: Live Data-paneel.**
- Hero-metriek **Hoogte** met een sparkline (`renderSpark()`).
- Groepen **Beweging** (snelheid, horizontale snelheid, verticale snelheid), **Richting**
  (horizontale/verticale richting) en **Positie** (coördinaten).
- Voettekst-legende: "Gemeten traject" en "Huidige positie".

> Alle waarden zijn **fictief**. `tick()` (elke 700 ms) laat de waarden licht schommelen binnen
> vaste grenzen en tekent de sparkline opnieuw. Er is geen echte hardware-verbinding.

### `#page-code` — Code-editor

De Code-pagina is een **één-koloms** opzet (`.code-solo`, max. 1060 px breed), rustig en zonder
rechterkolom.

- Een code-venster met titelbalk (`missie.ino`, "Arduino C++"), daarin rechts de hint
  `Ctrl` + `Enter` en de **Uploaden**-knop (`.code-upload`, rood).
- Een `textarea` (`#code-editor`) met korte startcode (`STARTER_CODE`, 11 regels).
- Daaronder een statusbalk met aantal regels en tekens.
- Daaronder twee **uitklapbare hulpblokken** (`<details class="help-item">`, standaard dicht):
  - **Wat kan ik gebruiken?** — compacte lijst van `meting.*` met eenheid, in twee kolommen.
  - **Hoe stuur ik iets?** — één voorbeeld `Serial.println("15,-5,75,60");` met één zin uitleg.

`updateCodeStats()` werkt de tellers bij en schakelt de uploadknop in/uit. `uploadCode()` toont enkel
een `alert`; er wordt niets echt geüpload.

### `#page-api` — API voor een extern programma

**Links: documentatie** (scrollbaar, `.api-doc`): hoe de koppeling werkt, verbinding maken
(endpoint `ws://localhost:9001`), uplink-JSON met de meetdata, downlink als **vrije CSV-regel**,
randvoorwaarden (komma, `\n`, frequentie) en een snelstart.

**Rechts: API-besturing** (`.api-side`): statusindicator, knoppen **API aanzetten/uitzetten**
(`toggleApiMock()`) en **Verbinding testen** (`testApi()`), plus voorbeeld van de regel terug en de
meting heen. De knoppen zijn een mock; er wordt geen echte socket geopend.

`api-handleiding.html` is een **doorverwijspagina** naar `index.html#page-api`.

## Setup-popup

Bij het laden verschijnt een modal (`#popup`) "Setup":
- Twee checkboxes: **USB-ontvanger** en **Meettoestel** (beide `disabled`, dus niet handmatig te wijzigen).
- Na **2 s** wordt USB op aangevinkt, na **4 s** het meettoestel (`setTimeout`), telkens via
  `checkAllChecked()`. De OK-knop wordt actief zodra beide aangevinkt zijn.
- `syncNavCheckboxes()` houdt de bolletjes in de navigatiebalk in sync met de popup.
- `closePopup()` sluit de modal met een korte fade-out.

## `style.css`

±1391 regels, opgebouwd rond CSS-variabelen (design tokens) in `:root`:

| Token | Waarde |
| --- | --- |
| `--navy` | `#0e2233` |
| `--ink` | `#101c27` |
| `--accent` | `#ff2f2f` |
| `--accent-deep` | `#d81f1f` |
| `--ok` | `#35e06b` |
| `--line` | `#e6ebf1` |
| `--surface` | `#ffffff` |
| `--surface-soft` | `#f7f9fc` |
| `--radius-lg/md/sm` | 22 / 16 / 11 px |
| `--shadow-sm/md/lg` | gelaagde schaduwen |
| `--font` / `--mono` | Segoe UI Variable / Cascadia Code |

Secties in het bestand (op basis van de commentaarkoppen): basis & tokens, ambient backdrop,
navigatie/island-nav + auto-checkbox-status, panelen (header, hero metric, data groups, footer
legend), kaart (MapLibre canvas, toestelmarker, atmosfeer/HUD), code-editor + uitklapbare hulp,
API-pagina (documentatie + bediening), daarna popup/overlay en responsive/utility-regels. Er is ook
een `--map-zoom` variabele.

## Legacy / niet meer gebruikt

- `assets/satellite.svg` en `scripts/gen-satellite.js` hoorden bij de **oude placeholderkaart**
  (een procedureel SVG-satellietbeeld van 1800×1800 met velden, bos, rivier, dorp en wegen).
  Ze worden door de huidige pagina **niet meer geladen**. `gen-satellite.js` is een Node-script dat
  met een deterministische PRNG (mulberry32, seed 20240929) de SVG genereert; uitvoeren met
  `node scripts/gen-satellite.js`.

## Herziene Code-pagina (voorheen versie B)

De Code-pagina is in **één kolom** herzien: grote editor, **Uploaden** en `Ctrl`+`Enter` in de
titelbalk, en twee korte **uitklapbare hulpblokken** (*Wat kan ik gebruiken?* en *Hoe stuur ik
 iets?*). Deze opzet is nu de **officiële** versie in `index.html`. De A/B-testbestanden
(`index-b.html`, `ab-vergelijken.html`) zijn verwijderd. Details in [[ab-test-code-pagina]].

## Verband met het oudere prototype

| | `CODEXIMPORT/visual-prototype/` (oud) | `GSTEMAPPPREVIEWWEB/` (nieuw) |
| --- | --- | --- |
| Kaart | Getekende SVG rond Spa, België | Echte MapLibre 3D-satellietkaart (Amsterdam) |
| Data | Statische fictieve waarden | Live-schommelende fictieve waarden |
| Editor | Alleen-lezen voorbeeldcode | Bewerkbare `textarea` + uitklapbare hulp + uploadknop |
| Setup | Startscherm met "Open demonstratie" | Modal-popup met auto-checkboxen |
| Navigatie | Tabs binnen één pagina | Hash-routing + island-nav |
