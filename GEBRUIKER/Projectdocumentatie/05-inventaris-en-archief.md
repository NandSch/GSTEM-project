# 05 · Inventaris en archief

Dit document beschrijft wat er in `GSTEM-Project/` staat, waar het vandaan komt en hoe het
ziparchief is opgebouwd.

## Eindstructuur van `C:\Users\Nand Schoovaerts\Documents\GSTEM-Project`

```text
GSTEM-Project/
├── README.md                         # ingang en overzicht
├── docs/
│   ├── 01-projectoverzicht.md        # G-Stem/GSN: doel, hardware, software, open vragen
│   ├── 02-codeximport.md             # map CODEXIMPORT volledig gedocumenteerd
│   ├── 03-gstemapppreviewweb.md      # webdemo volledig gedocumenteerd
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
│   └── archief/                      # elke afgeronde sessie (chat.md + meta.md)
├── CODEXIMPORT/                      # kopie van C:\...\Documents\ChatGPT\G-Stem Project
├── GSTEMAPPPREVIEWWEB/               # kopie van C:\...\Downloads\GSTEMAPPPREVIEWWEB
└── archief/
    ├── CODEXIMPORT.zip
    ├── GSTEMAPPPREVIEWWEB.zip
    ├── GSTEM-Project-AI-mappen.zip     # beide AI-mappen samen
    └── GSTEM-skill-en-GEBRUIKER.zip    # .pi/ + GEBRUIKER/
```

## Kopieerstap

Beide bronmappen zijn gekopieerd naar deze projectmap:

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

Sinds de inrichting als pi-project:

| Onderdeel | Functie |
| --- | --- |
| `.pi/skills/gstem-archief/SKILL.md` | Afspraken voor het systematisch opslaan van onderwerpen en data. |
| `.pi/skills/gstem-archief/references/templates.md` | Obsidian-sjablonen voor `chat.md`, `onderwerpen.md`, `data/*` en `meta.md`. |
| `.pi/extensions/gstem-logger.ts` | Live logger: gebruikersberichten verbatim, AI-antwoorden volledig (geen denkproces, geen tool-calls); archiveert bij het afsluiten van pi én bij elke nieuwe sessie. |
| `.pi/APPEND_SYSTEM.md` | Korte, altijd-geladen verwijzing naar de skill. |
| `GEBRUIKER/chat.md` | Live transcript van de huidige sessie. |
| `GEBRUIKER/data/` | `beslissingen.md`, `specificaties.md`, `open-vragen.md`, `links.md`, `afgevoerd.md`. |
| `GEBRUIKER/archief/` | Afgeronde sessies met `chat.md` + `meta.md`, vernoemd als `JJJJ-MM-DD_UUMM_<slug>`. |

Commando's: `/archiveer`, `/logboek`, `/onderwerp <naam>`. Extensie en `APPEND_SYSTEM.md` laden na projectvertrouwen.

## Resterende inhoud van `CODEXIMPORT/`

```text
CODEXIMPORT/
├── PROJECT_CONTEXT.md
├── G-Stem_specificaties_concept.docx
├── GSN-project_draadloze_3D-meetmodule.docx
├── Blokschema_AeroLink.drawio
├── create_gsn_document.py
├── visual-prototype/index.html
└── .git/   (opgeschoond, branch master, 2 commits)
```

## Resterende inhoud van `GSTEMAPPPREVIEWWEB/`

```text
GSTEMAPPPREVIEWWEB/
├── index.html          # HTML + alle inline scripts (kaart, telemetrie, editor, popup)
├── style.css           # stylesheet (design tokens, layout, HUD, markers)
├── assets/satellite.svg        # legacy procedurele satelliettextuur
├── scripts/gen-satellite.js    # legacy Node-generator
├── .pi/agents/start-website.md # startinstructie voor de lokale webserver
├── .vscode/launch.json # Chrome-debugconfig naar http://localhost:8080
├── server.log          # log van de lokale http.server
└── .git/               # repositoryhistoriek
```

## Het archief

Aangemaakt met **PowerShell `Compress-Archive`** in `GSTEM-Project/archief/`.

| Archief | Inhoud | Aantal entries | Grootte | SHA-256 |
| --- | --- | --- | --- | --- |
| `CODEXIMPORT.zip` | Map `CODEXIMPORT` | 112 | 147.6 KB | `EE682BD53AC7736B8FF6A91F83908F45AACAA4671CC112A5C6D548192C6D53C6` |
| `GSTEMAPPPREVIEWWEB.zip` | Map `GSTEMAPPPREVIEWWEB` | 60 | 132.7 KB | `CD6DBB066BB1355B388FE4ED89BDC933796D2817D8147BB2C17161853A59BD1F` |
| `GSTEM-Project-AI-mappen.zip` | Beide mappen samen | 172 | 280.2 KB | `350DB6686FE2E9AFF6CDF6BF02E7CFEF54C097560EDE77F331A3C9364A88A33E` |
| `GSTEM-skill-en-GEBRUIKER.zip` | `.pi/` + `GEBRUIKER/` | 14 | 10.8 KB | `4D515EC57226625DDDB6D8F9D1DB6A262D583A6BE5538303E178C8FE8DFB2347` |

Alle archieven zijn gecontroleerd met `zipfile.testzip()` (**integriteit OK**) en bevatten **geen**
bestanden met "negau", "build_negau" of "reading_test" in de naam.

## Verificatie

```powershell
# Hashes opnieuw controleren
Get-FileHash -Algorithm SHA256 .\archief\*.zip

# Integriteit controleren (Python)
python -c "import zipfile; print(zipfile.ZipFile('archief/CODEXIMPORT.zip').testzip())"
```

## Herkomst per document

| Document | Gebaseerd op |
| --- | --- |
| `01-projectoverzicht.md` | `PROJECT_CONTEXT.md`, beide docx-bestanden, `Blokschema_AeroLink.drawio` |
| `02-codeximport.md` | bestandsinventaris + `create_gsn_document.py` + `visual-prototype/index.html` |
| `03-gstemapppreviewweb.md` | `index.html`, `style.css`, `scripts/gen-satellite.js`, `.pi/agents/start-website.md`, git-log |
| `04-blokschema-aerolink.md` | `Blokschema_AeroLink.drawio` |

## Aantekeningen / waarschuwingen

- `create_gsn_document.py` vereist de Python-package **`python-docx`** (niet meegeleverd) en
  schrijft naar een vast pad naast het script.
- `GSTEMAPPPREVIEWWEB/server.log` is een log van de lokale `http.server` (alleen `GET /` en
  `/style.css`).
- `GSTEMAPPPREVIEWWEB/assets/satellite.svg` en `scripts/gen-satellite.js` zijn **legacy** en worden
  niet meer door de pagina geladen.
- De `.git`-mappen zijn meegekopieerd; beide mappen blijven zelfstandige Git-repositories.
