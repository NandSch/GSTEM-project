# GSTEM-Project — projectdocumentatie en gebruikershub

Deze map bundelt het **G-Stem / GSN-project**: *Positie- en beweging meettoestel met LoRa
integratie* (de werktitel *AeroLink* vervalt). De map is tegelijk een **pi-project met een vaste
werkwijze** en een **Obsidian-hub**.

## Inhoud van de map

| Pad | Inhoud |
| --- | --- |
| `docs/` | De documentatieset van het project (01 overzicht, 02 en 03 archiefbeschrijvingen, 04 blokschema, 05 inventaris). |
| `GEBRUIKER/` | Communicatie- en archiefhub: live chatlog, onderwerpenregister, `data/`, sessiearchief en een Obsidian-kopie van `docs/` in `Projectdocumentatie/`. |
| `documenten/` | De afgewerkte gebruikersspecificaties, de gebruikershandleiding en de ontwerptekst (markdown-bron, gegenereerde Word-versies, bouwscripts en screenshots). |
| `.pi/` | Pi-skill, altijd-geladen projectinstructie en de live logger. |
| `README.md` | Dit overzicht. |

## Opgeruimd op 2026-10-05

De ooit meegekopieerde AI-mappen zijn **verwijderd** om ruimte te winnen. Hun inhoud is blijvend
vastgelegd in de documentatie:

| Verwijderd | Vastgelegd in |
| --- | --- |
| `CODEXIMPORT/` (projectdocumenten, blokschema, generator, oud HTML-prototype) | `docs/01`, `docs/02`, `docs/04` |
| `GSTEMAPPPREVIEWWEB/` (statische webdemo van de laptopapp) | `docs/03` |
| Ziparchieven in `archief/` | `docs/05` (namen, groottes en hashes) |
| Oude `.docx.bak-*` in `documenten/` | git |

> [!info] Herstellen
> Alles staat nog in de git-structuur onder commit `5acdfa0`. Haal één pad terug met
> `git checkout 5acdfa0 -- CODEXIMPORT` (of `GSTEMAPPPREVIEWWEB`). Het opruimen zelf is in een
> aparte commit vastgelegd. Zie `docs/05-inventaris-en-archief.md`.

## Pi-skill & gebruikershub

- **Skill** `.pi/skills/gstem-archief/` — de afspraken; wordt altijd toegepast (via `.pi/APPEND_SYSTEM.md`).
- **Live logger** `.pi/extensions/gstem-logger.ts` — schrijft automatisch elk gebruikersbericht (verbatim) en elk AI-antwoord (volledig, zonder denkproces) naar `GEBRUIKER/chat.md`, en archiveert bij het afsluiten van pi én bij elke nieuwe sessie.
- **Hub** [`GEBRUIKER/`](GEBRUIKER/) — `chat.md` (huidige sessie), `onderwerpen.md`, `data/` (beslissingen, specificaties, open vragen, links, afgevoerd) en `archief/` (elke sessie apart).

Commando's: `/archiveer`, `/logboek`, `/onderwerp <naam>`.

> [!note]
> `.pi`-extensies en `APPEND_SYSTEM.md` laden pas nadat je pi **projectvertrouwen** geeft bij de
> eerste start in deze map.

## Documentatie

De documentatieset staat zowel in [`docs/`](docs/) als in
[`GEBRUIKER/Projectdocumentatie/`](GEBRUIKER/Projectdocumentatie/) (identiek, voor Obsidian):

1. [`docs/01-projectoverzicht.md`](docs/01-projectoverzicht.md) — het G-Stem/GSN-project: doel, hardware, softwareketen, appflow, open vragen.
2. [`docs/02-codeximport.md`](docs/02-codeximport.md) — archiefbeschrijving van de verwijderde map `CODEXIMPORT`.
3. [`docs/03-gstemapppreviewweb.md`](docs/03-gstemapppreviewweb.md) — archiefbeschrijving van de verwijderde webdemo `GSTEMAPPPREVIEWWEB`.
4. [`docs/04-blokschema-aerolink.md`](docs/04-blokschema-aerolink.md) — het blokschema van de meetmodule, node voor node.
5. [`docs/05-inventaris-en-archief.md`](docs/05-inventaris-en-archief.md) — bestandsinventaris, herkomst en wat opgeruimd is.

## Status

- Hardware, firmware en laptopapp zijn **in ontwerp**; de projectnaam is **Positie- en beweging meettoestel met LoRa integratie**.
- De door de gebruiker **afgewerkte gebruikersspecificaties** staan in `documenten/GStem-Specificaties.md` (aangeleverd `2026-10-06`); samengevat in `GEBRUIKER/data/gstem-specificaties.md` en verwerkt in `docs/01`.
- De webdemo was een **mock-up**: geen echte USB-, LoRa- of sensorverbinding. Hij is verwijderd nadat zijn werking in `docs/03` is vastgelegd.
