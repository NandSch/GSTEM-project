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
| Barometer BMP390 | https://www.adafruit.com/product/4816 | Gekozen barometer (`2026-10-06`): druk + temperatuur, I2C/SPI, meest accurate relatieve nauwkeurigheid (±3 Pa). |
| Bosch BMP581 vs BMP390 (forum) | https://community.bosch-sensortec.com/mems-sensors-forum-jrmujtaw/post/barometric-pressure-sensor-for-altitude-estimation-3B0In1wt54B65CZ | Onderbouwing: BMP390 ±3 Pa / 0,02 Pa ruis; BMP581 ±6 Pa / 0,08 Pa ruis. |
| RTK-GNSS LC29H(DA) | https://www.quectel.com/product/gnss-lc29h/ | Gekozen RTK-module (`2026-10-06`): dual-band L1+L5, multi-constellatie, RTK rover. Datasheet: https://www.quectel.com/content/uploads/2024/03/Quectel_LC29H_Series_GNSS_Module_Specification_V1.9.pdf |
| Waveshare LC29H(XX) GPS/RTK HAT | https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT | Breakout/HAT met actieve GNSS-antenne; (DA) = rover, (BS) = basisstation. Levert ook de passende dual-band L1+L5-antenne. |
| ESP32 hardware design guidelines | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/index.html | Referentie voor ontkoppeling en layout van de draagprint (decoupling, ground plane, antenne-keep-out). |
| ESP32-S3 power & I2C theorie | https://electricalflux.com/learn-guides/esp32-s3-i2c-power-theory-pcb-board-projects | Achtergrond bij ontkoppelcondensatoren en I2C-pull-up-berekening voor de draagprint (`2026-10-06`). |
| Level shifter TXB0104 | https://www.ti.com/product/TXB0104 | Gekozen 4-kanaals bidirectionele level shifter (3,3 V <-> 5 V) voor de UART naar de Arduino Uno (`2026-10-06`). |
| LDO AP2112K-3.3 | https://www.diodes.com/part/view/AP2112K | Gekozen 3,3 V-LDO (600 mA, lage dropout) voor een eigen senserrail (`2026-10-06`). |
| Voedingsbescherming | https://www.littelfuse.com/products/tvs-diodes / https://www.diodes.com/assets/Datasheets/DMG2301L.pdf | 2 A PTC-zekering, P-MOSFET DMG2301L (ompoolbeveiliging), TVS SMBJ10A (`2026-10-06`). |
| Schroefklem 3,5 mm (KF128/KF301) | https://www.cuidevices.com/product/interconnect/terminal-blocks | 4-pins uitbreidingsconnector voor de UART (`2026-10-06`). |
| GNSS-antenne (dual-band L1/L5) | https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT | Gekozen actieve GNSS-antenne met SMA, LNA + ground plane; bron verwijst naar de Waveshare-antenne bij de LC29H-HAT (`2026-10-06`). |
| IPEX/U.FL -> SMA pigtail | https://www.antratek.be (zoek: U.FL naar SMA bulkhead) | Kort antennekabeltje om de LoRa-antenne buiten het vliegtuigje te monteren (`2026-10-06`). |
| Bestellijst (markdown) | [[bestellijst]] | Alle onderdelen met status/tag, link, kost en aantal; bron voor de Excel (`2026-10-06`). |
| Bestellijst (Excel) | `documenten/Bestellijst-GSTEM.xlsx` | Gegenereerd met `documenten/build-bestellijst.py`. |
| XIAO ESP32S3 + Wio-SX1262 kit (prijs) | https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora | EUR 15,13 incl. btw op antratek (`2026-10-06`). |
| BNO055 (prijs) | https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055 | EUR 36,24 incl. btw op antratek (`2026-10-06`). |
| GNSS-antenne L1/L5 (antratek) | https://www.antratek.be/gnss-l1-l5-multi-band-high-precision-antenna-5m-sma | Actieve multi-band L1/L5 met SMA, u-blox/SparkFun GPS-23814, EUR 120,94 incl. btw (`2026-10-06`). |
| Goedkopere GNSS-antenne (antratek) | https://www.antratek.be/gps-gnss-magnetic-mount-antenna-sma-3m | GPS/GNSS magneetantenne SMA 3m, EUR 19,30 incl. btw; geen L1/L5 (`2026-10-06`). |
| Interface Cable SMA to U.FL (antratek) | https://www.antratek.be/u-fl-sma-150mm-cable | 150 mm U.FL/IPEX naar SMA, SparkFun WRL-18568, EUR 3,57 incl. btw (`2026-10-06`). |
| DC Barrel Jack Adapter - Female (antratek) | https://www.antratek.be/dc-barrel-jack-adapter-female | Adapter met schroefklem, SparkFun PRT-10288, EUR 4,78 incl. btw; geen PCB-montage (`2026-10-06`). |
| Logic Level Converter (antratek) | https://www.antratek.be/logic-level-converter-bi-directional-bob-12009 | Bidirectioneel 4-kanaals (BSS138), SparkFun BOB-12009, EUR 4,78 incl. btw; alternatief voor TXB0104 (`2026-10-06`). |
| Arduino Uno Rev3 (antratek) | https://www.antratek.be/arduino-uno-rev3-a000066 | EUR 41,75 incl. btw (`2026-10-06`). |
| RTK-alternatieven op antratek | https://www.antratek.be/quadband-gnss-rtk-breakout-lg290p-qwiic | LG290P RTK EUR 217,74; ZED-F9P EUR 302,44. Gekozen LC29H(DA) staat niet op antratek (`2026-10-06`). |
| Barometer BME280 (antratek) | https://www.antratek.be/atmospheric-sensor-breakout-bme280 | Goedkoopst/leverbaar alternatief voor de niet-verkrijgbare BMP390, EUR 19,97 incl. btw; minder nauwkeurig (`2026-10-06`). |
| GPS/GNSS magneetantenne (antratek) | https://www.antratek.be/gps-gnss-magnetic-mount-antenna-sma-3m | Goedkoopste passende actieve SMA-antenne, SparkFun GPS-14986, EUR 19,30 incl. btw (L1). Gebruikt als standaard in de bestellijst (`2026-10-06`). |
| Molex flexibele GNSS-antenne (antratek) | https://www.antratek.be/molex-flexible-gnss-antenna-u-fl-adhesive | Nog goedkoper (EUR 8,41), maar klein U.FL-printantennetje; niet gekozen (`2026-10-06`). |
