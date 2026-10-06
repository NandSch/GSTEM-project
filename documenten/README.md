---
tags: [gstem, documenten, index]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
---

# documenten/ — index

De **afgewerkte stukken** van het G-Stem-project: specificaties, PCB-materiaal, beheersbladen
en de scripts die de Excel- en beeldbestanden opnieuw opbouwen. De lopende notities en
beslissingen staan in de hub [[index|GEBRUIKER]]; deze map bevat enkel de deliverables.

> [!info] Structuur sinds `2026-10-06`
> Herschikt in vier submappen. Zie [[beslissingen]] voor de motivering. De archief-chatlogs
> bewaren de oude paden; de actieve documentatie is bijgewerkt.

## Wat staat waar

| Map | Bestanden | Waarvoor |
| --- | --- | --- |
| `specificaties/` | `GStem-Specificaties.md` | De door de gebruiker afgewerkte gebruikersspecificaties (`2026-10-06`). Zie [[gstem-specificaties]]. |
| | `Ontwerp-meetmodule.md` + `.docx` | De volledige technische ontwerptekst (markdown-bron + Word-versie). Zie [[meetmodule-voorbereiding]]. |
| `pcb/` | `PCB-schets.md` + `PCB-schets-draagprint.svg` + `.png` | Bovenaanzicht, verbindingsschema's (Mermaid) en voedingsboom van de draagprint. Zie [[pcb-schets]]. |
| | `PCB-eindbeeld.png` | Schets van de eind-PCB met de gekozen breakouts, de losse componenten en de Arduino Uno. |
| | `Communicatie-overzicht-GSTEM.drawio` | Bewerkbaar draw.io-schema (twee tabbladen: systeemcommunicatie en draagprint-UART-detail). Zie [[communicatie-overzicht]]. |
| | `review-mockup-controleblad.png` | Geannoteerd controleblad van de (verwijderde) Blender-mock-up; bewaard als naslag. Zie [[blender-mockup]]. |
| `beheer/` | `Bestellijst-GSTEM.xlsx` | Bestellijst met legende en bestelschema PCB. Zie [[bestellijst]] en [[bestelschema-pcb]]. |
| | `Planning-GSTEM.xlsx` | Twee bladen: **Planning** (schoolplanning) en **Actieplan**. Zie [[planning]] en [[actieplan]]. |
| `scripts/` | `build-bestellijst.py` | Bouwt `beheer/Bestellijst-GSTEM.xlsx`. |
| | `build-communicatie-overzicht.py` | Bouwt `pcb/Communicatie-overzicht-GSTEM.drawio`. |
| | `build-pcb-eindbeeld.py` | Bouwt `pcb/PCB-eindbeeld.png` (PIL). |
| | `build-controleblad.py` | Bouwde `pcb/review-mockup-controleblad.png`; kan pas opnieuw draaien met de review-renders uit git. |

## Scripts gebruiken

Alle scripts bepalen hun uitvoerpad via `__file__`, dus je kan ze vanuit de projectmap draaien:

```bash
python documenten/scripts/build-bestellijst.py
python documenten/scripts/build-communicatie-overzicht.py
python documenten/scripts/build-pcb-eindbeeld.py
```

Vereist: `openpyxl` (bestellijst) en `Pillow` (eindbeeld, controleblad).

## Verwijderd

| Pad | Wanneer | Waarom | Herstellen |
| --- | --- | --- | --- |
| `documenten/blender/` | `2026-10-06` | Mock-up niet meer gebruikt | `git checkout 28e4fae -- documenten/blender` |
| `Verbindingsschema-GSTEM.drawio` + `.png`, `build-verbindingsschema.py` | `2026-10-06` | Vervangen door `pcb/Communicatie-overzicht-GSTEM.drawio` | `git checkout 28e4fae -- <pad>` |
| `Handleiding-meettoestel.*`, `build-handleiding.py`, `maak-screenshots.py`, `afbeeldingen/` | `2026-10-01` (commit `b16c501`) | Opgeruimd bij de grote herschikking | `git checkout b16c501^ -- <pad>` |

> [!question] Open
> Of de gebruikershandleiding opnieuw gegenereerd wordt (of de verwijzingen opgeruimd) staat
> open in [[open-vragen]].

## Gerelateerd

- [[index]] — startpunt van de hub
- [[onderwerpen]] — register van alle besproken onderwerpen
- [[links]] — bronnen en bestandspaden
- `docs/` en `GEBRUIKER/Projectdocumentatie/` — de projectdocumentatieset (identiek)
