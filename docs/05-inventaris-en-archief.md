# 05 · Inventaris en archief

Dit document beschrijft wat er in `GSTEM-Project/` staat, waar het vandaan komt en wat op
`2026-10-05` is opgeruimd.

> [!warning] Opgeruimd op 2026-10-05
> `CODEXIMPORT/`, `GSTEMAPPPREVIEWWEB/`, de ziparchieven in `archief/` en de oude `.docx.bak-*`
> in `documenten/` zijn verwijderd om ruimte te winnen. Hun inhoud is blijvend vastgelegd in
> `docs/02`–`docs/04` en in `GEBRUIKER/Projectdocumentatie/`. Alles blijft herstelbaar via git:
> `git checkout 5acdfa0 -- <pad>`. Zie ook [[links]].

## Huidige structuur van `C:\Users\Nand Schoovaerts\Documents\GSTEM-Project`

```text
GSTEM-Project/
├── README.md                         # ingang en overzicht
├── docs/                             # documentatieset in de repo
│   ├── 01-projectoverzicht.md        # G-Stem/GSN: doel, hardware, software, open vragen
│   ├── 02-codeximport.md             # archiefbeschrijving van de verwijderde map CODEXIMPORT
│   ├── 03-gstemapppreviewweb.md      # archiefbeschrijving van de verwijderde webdemo
│   ├── 04-blokschema-aerolink.md     # blokschema node voor node
│   └── 05-inventaris-en-archief.md   # dit bestand
├── .pi/
│   ├── APPEND_SYSTEM.md              # altijd-geladen projectinstructie
│   ├── extensions/gstem-logger.ts    # live chatlogger + /archiveer, /logboek, /onderwerp
│   └── skills/gstem-archief/         # skill: SKILL.md + references/templates.md
├── GEBRUIKER/                        # communicatie- en archiefhub
│   ├── chat.md                       # live transcript huidige sessie
│   ├── index.md, onderwerpen.md
│   ├── data/                         # beslissingen, specificaties, open-vragen, links, afgevoerd
│   ├── Projectdocumentatie/          # Obsidian-kopie van docs/ (identiek)
│   └── archief/                      # elke afgeronde sessie (chat.md + meta.md)
└── documenten/                       # afgewerkte stukken van het project
    ├── README.md                     # index van documenten/
    ├── specificaties/                # GStem-Specificaties.md, Ontwerp-meetmodule.md/.docx
    ├── pcb/                          # PCB-schets, draagprint-SVG/PNG, PCB-eindbeeld, drawio, controleblad
    ├── beheer/                       # Bestellijst-GSTEM.xlsx, Planning-GSTEM.xlsx
    └── scripts/                      # build-*.py (padonafhankelijk via __file__)
```

> [!info] Herschikt op 2026-10-06
> `documenten/` is in submappen herschikt (`specificaties/`, `pcb/`, `beheer/`, `scripts/`) en
> heeft een eigen `README.md` als index. Zie [[beslissingen]]. De map `documenten/blender/`
> (Blender-mock-up) en de verbindingsschema-bestanden zijn verwijderd.

`docs/` en `GEBRUIKER/Projectdocumentatie/` worden **identiek** gehouden: `docs/` is de
repo-canonieke set, `GEBRUIKER/Projectdocumentatie/` is de Obsidian-kopie met wikilinks.

## Verwijderd op 2026-10-05

| Pad | Type | Omvang | Waarom | Vastgelegd in |
| --- | --- | --- | --- | --- |
| `CODEXIMPORT/` | map | ±264 KB | Vervangen door documentatie | `docs/02`, `docs/01` |
| `GSTEMAPPPREVIEWWEB/` | map | ±277 KB | Vervangen door documentatie | `docs/03` |
| `archief/CODEXIMPORT.zip` | zip | 147,6 KB | Duplicaat van de map | `docs/05` (hieronder) |
| `archief/GSTEMAPPPREVIEWWEB.zip` | zip | 132,7 KB | Duplicaat van de map | `docs/05` |
| `archief/GSTEM-Project-AI-mappen.zip` | zip | 280,2 KB | Bundel van beide mappen | `docs/05` |
| `archief/GSTEM-skill-en-GEBRUIKER.zip` | zip | 10,8 KB | Snapshot van `.pi/` + `GEBRUIKER/` | `docs/05` |
| `documenten/Handleiding-meettoestel.docx.bak-entagged` | Word-back-up | 9,5 MB | Tussenversie | git |
| `documenten/Ontwerp-meetmodule.docx.bak-entagged` | Word-back-up | 44,5 KB | Tussenversie | git |
| `documenten/Ontwerp-meetmodule.docx.bak-before-typos` | Word-back-up | 44,5 KB | Tussenversie | git |

De map `archief/` is na het verwijderen van de zips leeg en opgeheven.

> [!info] Herstellen
> Alles staat nog in de git-structuur onder commit `5acdfa0`. Haal één pad terug met
> `git checkout 5acdfa0 -- CODEXIMPORT` (of `GSTEMAPPPREVIEWWEB`, `archief/…`). Het opruimen
> zelf is vastgelegd in een aparte commit, zodat de geschiedenis klopt.

## Kopieerstap (historiek)

Beide bronmappen waren gekopieerd naar deze projectmap:

| Bestemming | Bron | Omvang kopie |
| --- | --- | --- |
| `GSTEM-Project/CODEXIMPORT/` | `C:\Users\Nand Schoovaerts\Documents\ChatGPT\G-Stem Project` | ±267 KB |
| `GSTEM-Project/GSTEMAPPPREVIEWWEB/` | `C:\Users\Nand Schoovaerts\Downloads\GSTEMAPPPREVIEWWEB` | ±421 KB |

### Verwijderd: niet-gerelateerd Negau B-helm-materiaal

In de oorspronkelijke `CODEXIMPORT`-map zat ook een **los leestoets-subproject over de Negau
B-helm** (taalkunde, pagina's 11–17). Dat hoorde niet bij het G-Stem-project en is uit de kopieën
en archieven verwijderd:

- `Negau_B-helm_met_annotaties.pdf`, `Negau_B-helm_zonder_annotaties.pdf`
- `build_negau_pdfs.py`, `make_reading_test_pdfs.py`
- `output/` (studiebundel-PDF's + previews) en `__pycache__/`
- de bijbehorende documentatie (`04-negau-b-helm.md`)

Ook de Git-objectendatabase is opgeschoond (`git gc --prune=now` plus het verwijderen van een
Codex-checkpoint-ref), waardoor de map kromp van **±112 MB → ±267 KB**. De originele bronmappen op
schijf zijn **niet** aangepast.

## Pi-skill en gebruikershub (`.pi/` + `GEBRUIKER/`)

| Onderdeel | Functie |
| --- | --- |
| `.pi/skills/gstem-archief/SKILL.md` | Afspraken voor het systematisch opslaan van onderwerpen en data. |
| `.pi/skills/gstem-archief/references/templates.md` | Obsidian-sjablonen voor `chat.md`, `onderwerpen.md`, `data/*` en `meta.md`. |
| `.pi/extensions/gstem-logger.ts` | Live logger: gebruikersberichten verbatim, AI-antwoorden volledig (geen denkproces, geen tool-calls); archiveert bij het afsluiten van pi én bij elke nieuwe sessie. |
| `.pi/APPEND_SYSTEM.md` | Korte, altijd-geladen verwijzing naar de skill. |
| `GEBRUIKER/chat.md` | Live transcript van de huidige sessie. |
| `GEBRUIKER/data/` | `beslissingen.md`, `specificaties.md`, `open-vragen.md`, `links.md`, `afgevoerd.md`. |
| `GEBRUIKER/archief/` | Afgeronde sessies met `chat.md` + `meta.md`, vernoemd als `JJJJ-MM-DD_UUMM_<slug>`. |

Commando's: `/archiveer`, `/logboek`, `/onderwerp <naam>`. Extensie en `APPEND_SYSTEM.md` laden na
projectvertrouwen.

## Historische inhoud van `CODEXIMPORT/` (verwijderd)

```text
CODEXIMPORT/
├── PROJECT_CONTEXT.md
├── G-Stem_specificaties_concept.docx
├── GSN-project_draadloze_3D-meetmodule.docx
├── Blokschema_AeroLink.drawio
├── create_gsn_document.py
├── visual-prototype/index.html
└── .git/   (opgeschond, branch master, 2 commits)
```

## Historische inhoud van `GSTEMAPPPREVIEWWEB/` (verwijderd)

```text
GSTEMAPPPREVIEWWEB/
├── index.html          # HTML + alle inline scripts (kaart, telemetrie, editor, API, popup)
├── style.css           # stylesheet (design tokens, layout, HUD, markers, API-pagina)
├── api-handleiding.html# doorverwijspagina naar index.html#page-api
├── assets/satellite.svg        # legacy procedurele satelliettextuur
├── scripts/gen-satellite.js    # legacy Node-generator
├── .pi/agents/start-website.md # startinstructie voor de lokale webserver
├── .vscode/launch.json # Chrome-debugconfig naar http://localhost:8080
├── server.log          # log van de lokale http.server
└── .git/               # repositoryhistoriek
```

## Het vroegere ziparchief (verwijderd)

De archieven waren aangemaakt met **PowerShell `Compress-Archive`** in `GSTEM-Project/archief/`.
Ter administratie blijven de namen, groottes en SHA-256-hashes hieronder bewaard.

| Archief | Inhoud | Aantal entries | Grootte | SHA-256 |
| --- | --- | --- | --- | --- |
| `CODEXIMPORT.zip` | Map `CODEXIMPORT` | 112 | 147,6 KB | `EE682BD53AC7736B8FF6A91F83908F45AACAA4671CC112A5C6D548192C6D53C6` |
| `GSTEMAPPPREVIEWWEB.zip` | Map `GSTEMAPPPREVIEWWEB` | 60 | 132,7 KB | `CD6DBB066BB1355B388FE4ED89BDC933796D2817D8147BB2C17161853A59BD1F` |
| `GSTEM-Project-AI-mappen.zip` | Beide mappen samen | 172 | 280,2 KB | `350DB6686FE2E9AFF6CDF6BF02E7CFEF54C097560EDE77F331A3C9364A88A33E` |
| `GSTEM-skill-en-GEBRUIKER.zip` | `.pi/` + `GEBRUIKER/` | 14 | 10,8 KB | `4D515EC57226625DDDB6D8F9D1DB6A262D583A6BE5538303E178C8FE8DFB2347` |

Alle archieven waren gecontroleerd met `zipfile.testzip()` (**integriteit OK**) en bevatten **geen**
bestanden met "negau", "build_negau" of "reading_test" in de naam.

## Herkomst per document

| Document | Gebaseerd op |
| --- | --- |
| `01-projectoverzicht.md` | `PROJECT_CONTEXT.md`, beide docx-bestanden, `Blokschema_AeroLink.drawio` |
| `02-codeximport.md` | bestandsinventaris + `create_gsn_document.py` + `visual-prototype/index.html` |
| `03-gstemapppreviewweb.md` | `index.html`, `style.css`, `scripts/gen-satellite.js`, `.pi/agents/start-website.md`, git-log |
| `04-blokschema-aerolink.md` | `Blokschema_AeroLink.drawio` |
| `05-inventaris-en-archief.md` | mappenstructuur, archieven, git-historiek |

## Aantekeningen / waarschuwingen

- `create_gsn_document.py` vereiste de Python-package **`python-docx`** (niet meegeleverd) en
  schreef naar een vast pad naast het script. Dit script is nu verwijderd; de beschrijving staat in
  `docs/02`.
- `GSTEMAPPPREVIEWWEB` had een `server.log` van de lokale `http.server` (alleen `GET /` en
  `/style.css`).
- `GSTEMAPPPREVIEWWEB/assets/satellite.svg` en `scripts/gen-satellite.js` waren **legacy** en werden
  niet meer door de pagina geladen.
- De geneste `.git`-mappen van beide verwijderde mappen zijn mee verdwenen; hun historiek blijft
  beschikbaar via de commit `5acdfa0` in de hoofdrepo.
