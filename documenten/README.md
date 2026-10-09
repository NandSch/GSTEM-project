---
tags: [gstem, documenten, index]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-09
---

# documenten/ — index

De **afgewerkte stukken** van het G-Stem-project: technische specificaties, historische PCB-referenties, beheersbladen en scripts. De lopende notities en beslissingen staan in de hub [[index|GEBRUIKER]]; deze map bevat de projectdeliverables.

> [!info] Structuur sinds `2026-10-06`
> Herschikt in vier submappen. Zie [[beslissingen]] voor de motivering. De archief-chatlogs bewaren de oude paden; de actieve documentatie is bijgewerkt.
>
> [!warning] Ontwerpwijziging `2026-10-09`
> De eigen draagprint en sockets zijn vervallen. De inhoud onder `pcb/` toont het oude ontwerp en is alleen nog historische referentie. De actuele aanpak is handbedrading en montage aan een 3D-geprinte behuizing; zie [[bedrading-en-behuizing]].

## Wat staat waar

| Map | Bestanden | Waarvoor |
| --- | --- | --- |
| `specificaties/` | `GStem-Specificaties.md` | De door de gebruiker afgewerkte gebruikersspecificaties (`2026-10-06`). Zie [[gstem-specificaties]]. |
| | `Ontwerp-meetmodule.md` | Actuele technische ontwerptekst (bronbestand; handbedrading en behuizing). Zie [[meetmodule-voorbereiding]]. |
| | `Ontwerp-meetmodule.docx` | Oudere Word-versie; loopt achter op de Markdown-bron. Het bouwscript ontbreekt nog; zie [[open-vragen]]. |
| `pcb/` | `PCB-schets.md` + `PCB-schets-draagprint.svg` + `.png` | Historisch bovenaanzicht, verbindingsschema's en voedingsboom van de vervallen draagprint. Niet gebruiken als actuele montage-instructie. Zie [[pcb-schets]]. |
| | `PCB-eindbeeld.png` | Historisch eindbeeld met carrier-PCB en sockets; niet meer actueel. |
| | `Communicatie-overzicht-GSTEM.drawio` | Systeemcommunicatie blijft als context bruikbaar; tabblad met draagprint-UART-detail is historisch. Zie [[communicatie-overzicht]]. |
| | `review-mockup-controleblad.png` | Geannoteerd controleblad van de (verwijderde) Blender-mock-up; bewaard als naslag. Zie [[blender-mockup]]. |
| `beheer/` | `Bestellijst-GSTEM.xlsx` | Actieve bestellijst, legende en open montage-/bedradingskeuzes. PCB- en socketskosten verwijderd. Zie [[bestellijst]]. |
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

Vereist: `openpyxl` en `xlsx_kit` voor de bestellijst; `Pillow` voor het eindbeeld en controleblad.

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
