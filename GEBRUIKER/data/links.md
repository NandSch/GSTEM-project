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
| JLCPCB | https://jlcpcb.com | Fabrikant voor de print (2-laags, 5 stuks); upload Gerbers. Goedkoopst, buiten EU. |
| PCBWay | https://www.pcbway.com | Alternatieve fabrikant buiten EU (China); ook assemblage. |
| OSH Park | https://oshpark.com | Fabrikant in de VS; ENIG, gratis verzending, prijs per inch². |
| AISLER | https://aisler.net | Fabrikant binnen Europa (DE/NL); accepteert KiCad/ODB++, prijs op oppervlak. Makkelijkst in EU. **Gekozen fabrikant** (`2026-10-06`). |
| Eurocircuits | https://www.eurocircuits.com | Fabrikant binnen Europa (BE); professioneel, met studenten-/lerarenprogramma. |
| Multi-CB | https://www.multi-circuit-boards.eu | Fabrikant binnen Europa (DE). |
| PCB-fabrikanten (vergelijking) | [[pcb-fabrikanten]] | Prijs en gemak binnen/buiten Europa (`2026-10-06`). |
| Bestelschema PCB (AISLER) | [[bestelschema-pcb]] | Productiekost AISLER + onderdelen op de print (`2026-10-06`). |
| XIAO ESP32S3 + Wio-SX1262 kit | https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora | Gekozen rekenkern + LoRa (SX1262). Specificaties: https://wiki.seeedstudio.com/xiao_esp32s3_%26_wio_sx1262_kit_for_meshtastic/ |
| BNO055 IMU-breakout | https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055 | Gekozen 9-DoF IMU. Datasheet/afmetingen: https://www.adafruit.com/product/2472 (20x27x4 mm, gaten 20x12 mm). |
| PCB-schets (draagprint) | `documenten/PCB-schets.md` + `documenten/PCB-schets-draagprint.svg` (+ `.png`) | Bovenaanzicht en verbindingsschema van de draagprint met breakout-modules (`2026-10-06`). Zie ook [[pcb-schets]]. |
| Eindbeeld eind-PCB (PNG) | `documenten/PCB-eindbeeld.png` | Gedetailleerde schets van de **eind-PCB** met alle gekozen breakouts (XIAO ESP32S3 + Wio-SX1262, BNO085, BMP581, LC29H(DA)), de losse componenten, de **Arduino Uno** en alle verbindingen (`2026-10-06`). Zie [[pcb-schets]]. |
| Eindbeeld (bouwsript) | `documenten/build-pcb-eindbeeld.py` | Bouwt `PCB-eindbeeld.png` met PIL: `python documenten/build-pcb-eindbeeld.py`. |
| Verbindingsschema (draw.io) | `documenten/Verbindingsschema-GSTEM.drawio` | Volledig schema **wie met wat en hoe verbonden is**: accu/barrel, PTC + TVS, buck 5 V, bulk-elco, power-LED, LDO 3,3 V, XIAO ESP32S3 + LoRa, BNO085/BMP581 (I2C), LC29H(DA) (UART), TXB0104, uitbreidingsconnector, Arduino + servo's + servo-buck, LoRa-adapter + laptop (`2026-10-06`). Te openen op https://app.diagrams.net. Zie [[verbindingsschema]]. |
| Verbindingsschema (PNG) | `documenten/Verbindingsschema-GSTEM.png` | Afbeelding (3120x2300) van het verbindingsschema. |
| Verbindingsschema (bouwsript) | `documenten/build-verbindingsschema.py` | Bouwt zowel de `.drawio` als de `.png` uit een enkele definitie: `python documenten/build-verbindingsschema.py`. |
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
| Voedingsbescherming | https://www.littelfuse.com/products/tvs-diodes | 2 A PTC-zekering + TVS SMBJ10A (`2026-10-06`). De **P-MOSFET-ompoolbeveiliging vervalt** — zie [[afgevoerd]]. |
| Schroefklem 3,5 mm (KF128/KF301) | https://www.cuidevices.com/product/interconnect/terminal-blocks | 4-pins uitbreidingsconnector voor de UART (`2026-10-06`). |
| GNSS-antenne (dual-band L1/L5) | https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT | Gekozen actieve GNSS-antenne met SMA, LNA + ground plane; bron verwijst naar de Waveshare-antenne bij de LC29H-HAT (`2026-10-06`). |
| IPEX/U.FL -> SMA pigtail | https://www.antratek.be (zoek: U.FL naar SMA bulkhead) | Kort antennekabeltje om de LoRa-antenne buiten het vliegtuigje te monteren (`2026-10-06`). |
| Bestellijst (markdown) | [[bestellijst]] | Alle onderdelen met status/tag, link, kost en aantal; bron voor de Excel (`2026-10-06`). |
| Bestellijst (Excel) | `documenten/Bestellijst-GSTEM.xlsx` | Gegenereerd met `documenten/build-bestellijst.py`. Drie bladen: **Bestellijst**, **Legende** en **Bestelschema PCB** (AISLER-productie + onderdelen op de print, `2026-10-06`). |
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

## Kiwi Electronics (`2026-10-06`)

Doel: **zo veel mogelijk onderdelen bij één winkel** (Kiwi Electronics, NL) bestellen om verzendkosten te beperken. Onderzocht via de eigen zoekfunctie `https://www.kiwi-electronics.com/nl/zoeken?search=<term>`.

| Onderdeel | Link / SKU | Prijs | Voorraad |
| --- | --- | --- | --- |
| XIAO ESP32S3 (los bord) | https://www.kiwi-electronics.com/nl/seeed-studio-xiao-esp32s3-11429 | € 8,46 | op voorraad |
| Wio-SX1262 voor XIAO (LoRa-module) | https://www.kiwi-electronics.com/nl/wio-sx1262-voor-xiao-20459 | € 5,43 | **niet op voorraad** |
| Adafruit BNO085 (BNO080) 9-DoF fusion | https://www.kiwi-electronics.com/nl/adafruit-9-dof-orientation-imu-fusion-breakout-bno085-bno080-stemma-qt-qwiic-11273 | € 32,05 | op voorraad |
| Adafruit BNO055 9-DoF fusion | https://www.kiwi-electronics.com/nl/adafruit-9-dof-absolute-orientation-imu-fusion-breakout-bno055-stemma-qt-qwiic-10417 | € 32,66 | op voorraad |
| Adafruit BMP581 I2C/SPI (barometer) | https://www.kiwi-electronics.com/nl/adafruit-bmp581-i2c-spi-druk-en-temperatuursensor-stemma-qt-20534 | € 10,88 | op voorraad |
| Adafruit BMP390L (barometer) | https://www.kiwi-electronics.com/nl/adafruit-bmp390l-precision-barometric-pressure-and-altimeter-stemma-qt-qwiic-10424 | € 12,09 | **niet op voorraad** |
| GPS Antenne - Externe Actieve Antenne - 3-5V 28dB 5m SMA | https://www.kiwi-electronics.com/nl/gps-antenne-externe-actieve-antenne-3-5v-28db-5-meter-sma-620 | € 16,93 | op voorraad |
| SMA naar uFL/u.FL/IPX/IPEX RF kabel (pigtail) | https://www.kiwi-electronics.com/nl/sma-naar-ufl-u-fl-ipx-ipex-rf-kabel-619 | € 4,22 | op voorraad |
| 8-kanaals bidirectionele Logic Level Converter TXB0108 | https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836 | € 8,70 | op voorraad |
| Schroefterminal 3,5 mm pitch - 3-weg | https://www.kiwi-electronics.com/nl/schroefterminal-3-5mm-pitch-3-weg-2506 | € 1,20 | op voorraad |
| 3 mm LED (10-pack, o.a. rood) | https://www.kiwi-electronics.com/nl/3mm-led-diffuus-rood-10-pack-3085 | € 1,20 | op voorraad |
| Weerstand 330 Ohm - 10 stuks | https://www.kiwi-electronics.com/nl/weerstand-330-ohm-1-4-watt-5-10-stuks-653 | € 0,96 | op voorraad |
| 100uF 16V condensator (bulk-elco) | https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440 | € 0,59 | op voorraad |

**Niet bij Kiwi** (`2026-10-06`): RTK-GNSS-module (geen LC29H/ZED-F9P; enkel de niet-RTK **L76K** € 15,11), discrete voeding (2 A PTC-zekering, P-MOSFET DMG2301L, TVS SMBJ10A, AP2112K-3.3), een **4-pins** 3,5 mm schroefklem (alleen 3-weg), precisie/dual-wipe sockets en M3-schroeven/standoffs.

## Andere winkels — de `geen-link`-onderdelen (`2026-10-06`)

Zoektocht naar de onderdelen die **niet** bij Kiwi of antratek te vinden waren. Voorkeur: **EU**
(geen invoerrechten/btw-gedoe). China (AliExpress/LCSC) enkel als terugval.

| Winkel | Land | Rol in dit project | URL |
| --- | --- | --- | --- |
| **TME** (Transfer Multisort Elektronik) | Polen (EU) | Discrete elektronica: LDO, MOSFET, TVS, PTC, schroefklemmen, precisie-sockets | https://www.tme.eu |
| **Eckstein** | Duitsland (EU) | **Gekozen winkel voor de Waveshare LC29H(DA)-HAT** (art. WS25279, `2026-10-06`) | https://eckstein-shop.de |
| **Botland** | Polen (EU) | Alternatief voor de Waveshare LC29H(DA)-breakout/HAT, M3-montage, connectoren | https://botland.store |
| **Kamami** | Polen (EU) | Alternatief voor de Waveshare LC29H(DA)-HAT | https://kamami.pl |
| **HESTORE** | Hongarije (EU) | Schroefklem DEGSON, LC29H-HAT (duurder) | https://www.hestore.eu |
| **TinyTronics** | Nederland (EU) | M3-afstandsbusjes/montagesets; levert uit Eindhoven | https://www.tinytronics.nl |
| **Bits & Parts** | Nederland (EU) | 180-delige M3 spacer/standoff-set | https://www.bitsandparts.nl |
| **Mouser.be / DigiKey** | VS, **EU-magazijn** | Exacte/EOL-onderdelen (1812L200/16), EU-btw, geen invoer | https://be.mouser.com · https://www.digikey.be |
| **RS Components** | BE (EU) | Preci-Dip precisie-sockets | https://be.rs-online.com |

### Gevonden onderdelen

| Onderdeel | Bestelcode | Winkel | Link |
| --- | --- | --- | --- |
| RTK-GNSS **breakout** (LC29H(DA)) | Waveshare **LC29H(DA) GPS/RTK HAT**, art. **WS25279**, EAN 4060137304156 | **Eckstein (DE, EU) — gekozen** `2026-10-06` | https://eckstein-shop.de/lc29h-dual-band-gps-module-raspberry-pi_1 |
| idem (alternatief) | Waveshare 25279 LC29H(DA) HAT | Botland (PL/DE, EU) | https://botland.store/raspberry-pi-hat-connection/23875-dual-band-gpsrtk-l1l5-module-with-lc29hda-gnss-chip-overlay-for-raspberry-pi-waveshare-25279.html |
| idem (alternatief) | Waveshare 25279 LC29H(DA) HAT | Kamami (PL, EU) | https://kamami.pl/en/gps-modules/1187927-lc29h-series-dual-band-gps-module-for-raspberry-pi-dual-band-l1-l5-positioning-technology-optional-5906623465965.html |
| RTK-breakout (alternatief) | MIKROE **GNSS RTK 3 Click** (LC29HDA, mikroBUS) | TME / mikroe.com | https://www.tme.eu/en/details/mikroe-5914/add-on-boards/mikroe/gnss-rtk-3-click-lc29hda/ |
| LDO 3,3 V | **AP2112K-3.3TRG1** (Diodes, SOT-23-5) | TME | https://www.tme.eu/en/details/ap2112k-3.3trg1/ldo-fixed-voltage-regulators/diodes-incorporated/ |
| ~~P-MOSFET (ompoolbeveiliging)~~ | DMG2301L-7 / AO3401A (SOT-23) | ~~Mouser / TME~~ | **vervalt** (`2026-10-06`) — zie [[afgevoerd]] |
| TVS-diode | **SMBJ10A-TR** (ST) / **SMBJ10A/TR7** (Yageo) | TME | https://www.tme.eu/en/details/smbj10a-tr/unidirectional-tvs-smd-diodes/stmicroelectronics/ |
| 2 A PTC-zekering (1812) | **Littelfuse 1812L200/16** | Mouser.be / DigiKey / TME | https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-pptc-devices/surface-mount-polyswitch-resettable-pptc-devices/1812l/1812l200 |
| Schroefklem 4-pins 3,5 mm | DEGSON **DG250-3.5-04P-11-00A(H)** | HESTORE / TME | https://www.hestore.eu/en/prod_10044104.html |
| Precisie/turned-pin socket | **Preci-Dip** 110-serie 2,54 mm (DIL, turned pin) | TME / RS | https://int.rsdelivers.com/product/preci-dip/110-87-304-41-001101/preci-dip-110-254-mm-pitch-vertical-4-way-through/7020644P |
| M3-montageset | TinyTronics **M3 Afstandsbusje Kit** | TinyTronics (NL) | https://www.tinytronics.nl/nl/gereedschap-en-montage/installatie-en-montagemateriaal/afstandsbusjes/m3-afstandsbusje-kit |
| M3-montageset (alternatief) | 180-delige spacer/standoff-set | Bits & Parts (NL) | https://www.bitsandparts.nl/Afstandsbus-Spacer-Standoff-M3-set-180-delig-zwart-p1885552 |

> [!note] Breakout vs losse module
> De **losse Quectel LC29H-DA SMD-module** (Maritex PL, Soyter PL, ± € 18–21) is **niet** gekozen:
> de gebruiker wil een **breakout board**. De **7Semi LC29HDA RTK Board** (Qwiic/USB-C, ~$ 42) is een
> mooie breakout, maar wordt uit **India** verzonden (niet EU).

## Datasheets en mechanische maten (Blender-mock-up, `2026-10-06`)

Voor de 3D-mock-up zijn de echte bordmaten opgezocht (samengevat in [[gstem-hardware-afmetingen]]):

| Onderdeel | Link |
| --- | --- |
| XIAO ESP32S3 | https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/ |
| Wio-SX1262 (datasheet) | https://files.seeedstudio.com/products/SenseCAP/Wio_SX1262/Wio-SX1262_Module_Datasheet.pdf |
| Adafruit BNO085 | https://www.adafruit.com/product/4754 |
| Adafruit BMP581 (6407) | https://www.adafruit.com/product/6407 |
| Waveshare LC29H(XX) HAT | https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT |
| Arduino Uno R3 (datasheet) | https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf |
| SG90/MG90S servo | https://components101.com/sites/default/files/component_datasheet/MG90S-Datasheet.pdf |
| Waveshare L1/L5 GNSS-antenne | https://www.waveshare.com/gps-external-antenna-d.htm |
| Seeed LoRa-antenne 868/915 | https://www.seeedstudio.com/External-Antenna-868-915MHZ-2dBi-SMA-L195mm-Foldable-p-5863.html |
| SMA-bulkhead (Wurth) | https://www.we-online.com/components/products/datasheet/60326421110220.pdf |
| AP2112 (LDO) | https://www.mouser.com/datasheet/2/115/AP2112-271550.pdf |
| TXB0104 | https://www.ti.com/lit/ds/symlink/txb0104.pdf |
| DEGSON DG250-3.5 | https://www.degson.com/content/details_552_879687.html?lang=en |
