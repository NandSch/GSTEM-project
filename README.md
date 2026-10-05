# GSTEM-Project — gearchiveerde AI-mappen en documentatie

Deze map bundelt twee AI-/ontwikkelmappen van het **G-Stem / GSN-project**:

| Map in deze repo | Oorspronkelijke locatie | Inhoud |
| --- | --- | --- |
| [`CODEXIMPORT/`](CODEXIMPORT/) | `C:\Users\Nand Schoovaerts\Documents\ChatGPT\G-Stem Project` | Projectdocumenten (docx), blokschema (drawio), Python-generatorscript, oud visueel HTML-prototype, `PROJECT_CONTEXT.md` |
| [`GSTEMAPPPREVIEWWEB/`](GSTEMAPPPREVIEWWEB/) | `C:\Users\Nand Schoovaerts\Downloads\GSTEMAPPPREVIEWWEB` | Werkende statische webdemo van de laptopapp: MapLibre 3D-kaart, live telemetrie, code-editor, setup-popup |

Beide mappen zijn **volledig gekopieerd** (inclusief `.git`, assets en scripts) en daarnaast gebundeld in een ziparchief (zie `docs/05-inventaris-en-archief.md`).

> Niet-gerelateerd materiaal (een los "Negau B-helm"-leestoets-subproject dat in dezelfde AI-map stond) is uit deze kopieën en archieven verwijderd.

## Pi-skill & gebruikershub

Deze map is ook ingericht als **pi-project met een vaste werkwijze**:

- **Skill** `.pi/skills/gstem-archief/` — de afspraken; wordt altijd toegepast (via `.pi/APPEND_SYSTEM.md`).
- **Live logger** `.pi/extensions/gstem-logger.ts` — schrijft automatisch elk gebruikersbericht (verbatim) en elk AI-antwoord (volledig, zonder denkproces) naar `GEBRUIKER/chat.md`, en archiveert bij het afsluiten van pi én bij elke nieuwe sessie.
- **Hub** [`GEBRUIKER/`](GEBRUIKER/) — `chat.md` (huidige sessie), `onderwerpen.md`, `data/` (beslissingen, specificaties, open vragen, links, afgevoerd) en `archief/` (elke sessie apart).

Commando's: `/archiveer`, `/logboek`, `/onderwerp <naam>`.

> [!note]
> `.pi`-extensies en `APPEND_SYSTEM.md` laden pas nadat je pi **projectvertrouwen** geeft bij de eerste start in deze map.

## Documentatie

De volledige documentatie staat in de map [`docs/`](docs/):

1. [`docs/01-projectoverzicht.md`](docs/01-projectoverzicht.md) — het G-Stem/GSN-project: doel, hardware, softwareketen, appflow, open vragen.
2. [`docs/02-codeximport.md`](docs/02-codeximport.md) — volledige inventaris en uitleg van de map `CODEXIMPORT`.
3. [`docs/03-gstemapppreviewweb.md`](docs/03-gstemapppreviewweb.md) — architectuur en werking van de webdemo `GSTEMAPPPREVIEWWEB`.
4. [`docs/04-blokschema-aerolink.md`](docs/04-blokschema-aerolink.md) — het blokschema van de meetmodule, node voor node.
5. [`docs/05-inventaris-en-archief.md`](docs/05-inventaris-en-archief.md) — bestandsinventaris, herkomst en het ziparchief.

## Snel starten met de webdemo

```bash
cd GSTEMAPPPREVIEWWEB
python -m http.server 8080
# open daarna http://localhost:8080 in de browser
```

> De demo heeft internet nodig (MapLibre GL via CDN + Esri/AWS tegels) en moet via `http://` geopend worden, niet via `file://`.

## Status

- Hardware, firmware en laptopapp zijn **in ontwerp**; de projectnaam is **Positie- en beweging meetmodule met LoRa integratie** (de werktitel *AeroLink* vervalt).
- De webdemo is een **mock-up**: geen echte USB-, LoRa- of sensorverbinding.
