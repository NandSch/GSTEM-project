---
tags: [gstem, data, links]
---

# Links en bronnen

| Onderwerp | Link / pad | Notitie |
| --- | --- | --- |
| Projectcontext | `CODEXIMPORT/PROJECT_CONTEXT.md` (verwijderd `2026-10-05`) | Oriëntatiedocument G-Stem/GSN; nu in `docs/01` |
| Specificaties (concept) | `CODEXIMPORT/G-Stem_specificaties_concept.docx` (verwijderd) | Hardware + software; samengevat in `docs/01` |
| Blokschema | `CODEXIMPORT/Blokschema_AeroLink.drawio` (verwijderd) | Keten meetmodule → laptop; beschreven in `docs/04` |
| Webdemo | `GSTEMAPPPREVIEWWEB/index.html` (verwijderd `2026-10-05`) | Mock-up laptopapp; werking beschreven in `docs/03`
| API-handleiding (demo) | `GSTEMAPPPREVIEWWEB/api-handleiding.html` (verwijderd) -> `index.html#page-api` | Beschreven in `docs/03` |
| Documentatie | `docs/` | Overzichten en inventaris |
| Handleiding (bron) | `documenten/Handleiding-meettoestel.md` | Markdown-bron van de gebruikershandleiding |
| Handleiding (Word) | `documenten/Handleiding-meettoestel.docx` | Gegenereerd Word-document |
| Handleiding (script) | `documenten/build-handleiding.py` | Bouwt de .docx uit de markdown-bron |
| Screenshots (script) | `documenten/maak-screenshots.py` | Maakt schermafbeeldingen van de webdemo (Playwright + Chrome) |
| Screenshots (map) | `documenten/afbeeldingen/` | Gegenereerde PNG's, gebruikt in de handleiding |
| Opmaakreferentie | `GStem-Specificaties (1).docx` (Downloads) | Bestaand specificatiedocument; basis voor de opmaakstijl van de handleiding |
| Ontwerp (uitgewerkt) | `documenten/Ontwerp-meetmodule.md` | Volledige ontwerptekst: de inhoud van het Google Doc, technisch aangevuld (`2026-10-05`). Bewerk hier. |
| Ontwerp (Word) | `documenten/Ontwerp-meetmodule.docx` | Gegenereerde Word-versie van de ontwerptekst, in de stijl van GStem-Specificaties |
| Ontwerp (script) | `documenten/build-ontwerp.py` | Bouwt de .docx: `python documenten/build-ontwerp.py` |
| PCB-methodes (kosten) | [[pcb-methodes-kosten]] | Vergelijking sockets/direct/castellated/board-to-board/JST (`2026-10-06`). |
| PCB-ontwerp (werkwijze) | [[pcb-ontwerp]] | Gereedschap (KiCad), footprints en gatmaten (`2026-10-06`). |
| KiCad | https://www.kicad.org | Gratis PCB-ontwerpgereedschap; aanbevolen app voor de draagprint. |
| JLCPCB | https://jlcpcb.com | Fabrikant voor de print (2-laags, 5 stuks); upload Gerbers. |
| XIAO ESP32S3 + Wio-SX1262 kit | https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora | Gekozen rekenkern + LoRa (SX1262). Specificaties: https://wiki.seeedstudio.com/xiao_esp32s3_%26_wio_sx1262_kit_for_meshtastic/ |
| BNO055 IMU-breakout | https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055 | Gekozen 9-DoF IMU. Datasheet/afmetingen: https://www.adafruit.com/product/2472 (20x27x4 mm, gaten 20x12 mm). |
| PCB-schets (draagprint) | `documenten/PCB-schets.md` + `documenten/PCB-schets-draagprint.svg` (+ `.png`) | Bovenaanzicht en verbindingsschema van de draagprint met breakout-modules (`2026-10-06`). Zie ook [[pcb-schets]]. |
| Gebruikersspecificaties (afgewerkt) | `documenten/GStem-Specificaties.md` | Door de gebruiker afgewerkte specificaties, aangeleverd `2026-10-06` uit `~/Downloads/GStem-Specificaties.md`. Bevat de gebruikersgerichte beschrijving: meetprestaties, aanzetten, de app-schermen en de RC-vliegtuig-mock-up. |
| Planning (Excel) | `documenten/Planning-GSTEM.xlsx` | Twee bladen: **Planning** (schoolplanning, blauw) en **Actieplan** (projectstappen, oranje). Zie [[planning]] en [[actieplan]]. |
| Ontwerptekst (Google Doc) | https://docs.google.com/document/d/1wbb8LAjXiUpZQBpxv1NKQZ8YBhb32TtkiDcpUfl5o0M/edit | "Ontwerp voor Positie- en beweging meettoestel met LoRa integratie". Openbaar gedeeld op `2026-10-05`; gelezen via `export?format=txt`. **Let op:** dit Doc is nog niet aangevuld — de aanvulling staat in `documenten/Ontwerp-meetmodule.md` en wacht op het overzetten. |
