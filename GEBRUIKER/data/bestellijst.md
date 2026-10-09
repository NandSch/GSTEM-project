---
tags: [gstem, data, bestellijst, bom, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-09
status: actieve bestellijst; bedrading en behuizingsmontage nog uit te werken
---

# Bestellijst meettoestel (aan te kopen)

> [!info] Werkwijze
> Alle onderdelen uit [[componenten]]. Voorkeur blijft: **zo veel mogelijk bij Kiwi Electronics**
> en de rest bij passende EU-winkels, behalve de **RTK-GNSS-module (LC29HDA)** die sinds
> `2026-10-07` bij **AliExpress (China)** gekocht wordt. Prijzen zijn **incl. btw** tenzij anders
> vermeld en onder voorbehoud. De Excel-versie staat in `documenten/beheer/Bestellijst-GSTEM.xlsx`
> (bron: `documenten/scripts/build-bestellijst.py`).

> [!warning] Montage en bedrading nog niet definitief
> De AISLER-draagprint, sockets, PCB-barreljack en M3-set voor de oude print zijn geen actieve bestellingen meer. De montage van componenten, voedingsinvoer, UART-connectoren en voedingsonderdelen moet nog worden uitgewerkt. Er worden hiervoor geen nieuwe onderdelen online opgezocht of aan de lijst toegevoegd totdat de uitvoering is bevestigd. Zie [[bedrading-en-behuizing]].

## Legende (tags)

| Tag | Betekenis |
| --- | --- |
| `kiwi` | Aankooplink gevonden bij Kiwi Electronics (NL) |
| `antratek` | Aankooplink gevonden bij antratek.be (goedkoper of reserve) |
| `tme` | Transfer Multisort Elektronik (Polen, EU) |
| `eckstein` | Eckstein (Duitsland, EU) — enkel terugvaloptie |
| `hestore` | HESTORE (Hongarije, EU) |
| `tinytronics` | TinyTronics (Nederland, EU) |
| `mouser` | Mouser.be / DigiKey met **EU-magazijn** (levert binnen de EU, EU-btw) |
| `aliexpress` | AliExpress (China); gekozen bron voor de LC29HDA-module |
| `waveshare` | Waveshare (fabrikant, China) — losse GNSS-antenne |
| `al-in-bezit` | Heeft de gebruiker al; niet aankopen |
| `geen-link` | Nog niet bij een geschikte winkel gevonden |
| `onderzoek` | Zoekresultaat gevonden, maar exacte listing/prijs nog niet geverifieerd |
| `niet-nodig` | Bewust niet voorzien |
| `aisler` | Historische vermelding van de vervallen draagprint; niet bestellen |
| `te-bepalen` | Uitvoering of noodzaak nog open; niet als actieve bestelling meetellen |

> [!info] Bestaande bestelbaarheid (controle `2026-10-06`)
> De historische voorraad- en winkelinformatie blijft ter referentie in [[bestelbaarheid]]. Socket- en PCB-aankoopadviezen zijn vervallen. De 4-pins schroefklem is nog niet definitief nodig nu de verbindingen handbedraad worden; zie [[bedrading-en-behuizing]]. De P-MOSFET-ompoolbeveiliging blijft vervallen (beslissing `2026-10-06`); zie [[afgevoerd]].
>
> GPS/RTK-prijsvergelijking: [[gps-rtk-prijzen]].

> [!tip] Winkels
> **TME (Polen)** dekt de eerder gekozen discrete elektronica (LDO/TVS); **Mouser.be/DigiKey** de PTC. De **LC29HDA-RTK-rover** blijft de kandidaat bij **AliExpress (China)**. Eerdere socket- en M3-winkellinks zijn alleen historische referenties; nieuwe behuizingshardware wordt pas bepaald na het montageontwerp.

## Rekenkern en communicatie

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `antratek` | Rekenkern + LoRa (toestel + ontvanger) | XIAO ESP32S3 & Wio-SX1262 Kit for Meshtastic & LoRa | 2 | € 15,13 | https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora |

> [!note] Antenne inbegrepen
> De LoRa-antenne zit bij de kit. **Kiwi-alternatief:** XIAO ESP32S3 (€ 8,46) + Wio-SX1262
> (€ 5,43) apart — maar de **Wio-SX1262-module is bij Kiwi niet op voorraad**, dus de kit blijft
> de zekere optie.

## Sensoren

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `kiwi` | 9-DoF IMU | Adafruit BNO085 (BNO080) 9-DoF Orientation IMU Fusion, STEMMA QT/Qwiic | 1 | € 32,05 | https://www.kiwi-electronics.com/nl/adafruit-9-dof-orientation-imu-fusion-breakout-bno085-bno080-stemma-qt-qwiic-11273 |
| `kiwi` | Barometer | Adafruit BMP581 I²C/SPI druk- en temperatuursensor, STEMMA QT | 1 | € 10,88 | https://www.kiwi-electronics.com/nl/adafruit-bmp581-i2c-spi-druk-en-temperatuursensor-stemma-qt-20534 |
| `aliexpress` | RTK-GNSS-module (**breakout board**, **LC29HDA rover**) | Quectel LC29HDA dual-band L1+L5 RTK-GNSS-developmentboard (geassembleerd) — **kies de LC29HDA-variant** | 1 | € 36,99 | https://nl.aliexpress.com/item/1005009915138674.html |

> [!warning] RTK-GNSS: koop de LC29HDA-**rover**, niet de BS-variant
> De technische variant voor dit toestel is **Quectel LC29HDA (RTK-rover)**. `DA` hoort bij de
> modulevariant; het is **geen** D/A-converterbord. Vermijd de **LC29HBS** (basisstation) en de
> **losse SMD-module**. Op de productpagina moet de gekozen optie ondubbelzinnig **LC29HDA** zijn
> en een **geassembleerd development board** (UART/I²C, USB/5 V-voeding, antenne-aansluiting).
>
> Bij de gekozen [AliExpress-listing](https://nl.aliexpress.com/item/1005009915138674.html) is de
> titel eerder "LC29H" dan "LC29HDA": controleer bij het bestellen dat de **variant LC29HDA** is.
> Dezelfde module is ook eenduidig te koop bij deze alternatieven (variantkeuzemenu):
> [item 1005010758488281](https://www.aliexpress.com/item/1005010758488281.html) en
> [item 1005010162466640](https://www.aliexpress.com/item/1005010162466640.html).
> Prijsvergelijking: [[gps-rtk-prijzen]].
>
> **Terugvaloptie (EU, volledig geverifieerd en mét antenne):** de **Waveshare LC29H(DA) GPS/RTK HAT
> (SKU 25279)** bij Eckstein (€ 71,39) of Kamami (± € 63). Deze wordt gebruikt als de AliExpress-
> variant niet klopt of niet geleverd raakt.

### Terugvaloptie-breakout: eigenschappen (Waveshare 25279)
> [!example]- Details LC29H(DA) HAT
> - **65 × 30,5 mm**, 5 V (5 V-pin of Micro-USB), ± 40 mA.
> - L1+L5 dual-band, GPS/QZSS/GLONASS/BeiDou/Galileo, **RTK rover** (centimeter-niveau).
> - Interfaces: **UART** (9600–3 Mbps, standaard 115200), **I²C**, 40-pins GPIO-header, Micro-USB.
> - Ingebouwde LNA + SAW-filter; onboard ML1220-batterijhouder; 4 status-LED's.
> - Meegeleverd: **dual-band actieve GNSS-antenne**, IPEX-1→SMA-kabel (17 cm), schroefset, 2×20-pins female header.
> - Let op: door de vorm (65 mm) en de 40-pins header is het bord groter dan een losse module —
>   controleer de afmetingen en bevestigingsmogelijkheden voor de **3D-geprinte behuizing**; een draagprint-footprint is niet meer nodig. Zie [[bedrading-en-behuizing]] en [[gps-rtk-prijzen]].

## Antennes en RF

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `waveshare` | GNSS-antenne (actief, L1/L5) | Waveshare GPS External Antenna (D), SKU 25346 — actief L1+L5, LNA 28±2 dB, SMA-J, 3 m. **Alleen bestellen als de LC29HDA-kit geen passende antenne meelevert** | 1 | € 15,70 (≈ $ 16,99) | https://www.waveshare.com/gps-external-antenna-d.htm |
| `antratek` | LoRa IPEX/U.FL -> SMA pigtail | Interface Cable SMA to U.FL (150 mm), SparkFun WRL-18568 | 1 | € 3,57 | https://www.antratek.be/u-fl-sma-150mm-cable |
| `al-in-bezit` | LoRa-antenne | Inbegrepen bij de XIAO-kit | 1 | - | - |

> [!warning] GNSS-antenne: eerst de bundel controleren
> Veel AliExpress-LC29HDA-kits leveren een **L1/L5-antenne** mee. Controleer dat vóór aankoop van
> de losse antenne. De **Waveshare GPS External Antenna (D), SKU 25346** is een passende losse
> kandidaat (actief L1+L5, LNA 28±2 dB, SMA-J) — controleer de **connector** van het board
> (SMA vs. IPEX) en of een adapter nodig is. Prijs wordt niet in het basistotaal meegerekend
> omdat ze mogelijk al in de kit zit.

> [!note] Pigtail
> Goedkoper op antratek (€ 3,57) dan Kiwi (€ 4,22) → op antratek laten staan.

## Voeding

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Accu (7,4 V) | 2S LiPo met connector en kabel | 1 | - | - |
| `al-in-bezit` | Voedingsaansluiting (kabelzijde) | DC Barrel Jack Adapter - Female (schroefklem) | 1 | - | - |
| `niet-nodig` | PCB-voedingsaansluiting | 2,1 mm breadboard-/PCB-barreljack — alleen gekozen voor montage op de vervallen draagprint | - | - | - |
| `al-in-bezit` | Buck-converter 5 V | Heeft de gebruiker | 1 | - | - |
| `mouser` | Bescherming voeding | 2 A PTC Littelfuse 1812L200/16 + TVS SMBJ10A-TR — fysieke montage/bedrading nog te bepalen | 1 set | ± € 1,00 | https://www.mouser.com/ProductDetail/Littelfuse/1812L200-16DR |
| `niet-nodig` | Ompoolbeveiliging (P-MOSFET) | P-MOSFET DMG2301L / AO3401A (SOT-23) | - | - | **vervalt** (`2026-10-06`) |
| `tme` | LDO 3,3 V | AP2112K-3.3TRG1 (SOT-23-5) — fysieke montage/bedrading nog te bepalen | 1 | € 0,27 | https://www.tme.eu/en/details/ap2112k-3.3trg1/ldo-fixed-voltage-regulators/diodes-incorporated/ |
| `niet-nodig` | Aan/uit-schakelaar | Geen; toestel start bij voeding | - | - | - |

> [!success] Discrete voeding gevonden bij TME (EU) — `2026-10-06`
> | Onderdeel | Exacte bestelcode | Winkel | Prijs (1 st.) |
> | --- | --- | --- | --- |
> | LDO 3,3 V, 600 mA | **AP2112K-3.3TRG1** (Diodes Inc., SOT-23-5) | TME (PL) | ± € 0,27 (8 000+ op voorraad) |
> | TVS SMBJ10A | **SMBJ10A-TR** (ST) of **SMBJ10A/TR7** (Yageo) | TME (PL) | ± € 0,50 (1 800+ op voorraad) |
> | 2 A PTC-zekering, 1812 | **Littelfuse 1812L200/16** | Mouser.be / DigiKey / TME | ± € 0,40 |
>
> **P-MOSFET vervalt** (`2026-10-06`): de gebruiker kiest **geen** ompoolbeveiliging. De kandidaten
> **DMG2301L-7** en **AO3401A** komen dus **niet** op de lijst; zie [[afgevoerd]]. Voorkom omgekeerd
> aansluiten met een **gepolariseerde connector** (XT60/JST-XH).

> [!note] Voedingsinvoer en behuizing
> De gebruiker heeft een **female barrel-adapter met schroefklem**. Of deze rechtstreeks wordt bedraad of via een doorvoer in de nieuwe behuizing wordt gemonteerd, staat nog open. De PCB-breadboard-barreljack van Kiwi is alleen voor de vervallen draagprint gekozen en is daarom uit de actieve bestellijst gehaald.

## Bedrading en losse elektronica

> [!info] Geen carrier-PCB of sockets
> De gebruiker verbindt en soldeert de componenten zelf en monteert ze aan de 3D-geprinte behuizing. De elektrische functies blijven voorlopig op de BOM; de mechanische ondersteuning en exacte verbindingsmethode zijn nog niet vastgesteld. Zie [[bedrading-en-behuizing]].

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `niet-nodig` | Draagprint (PCB) | AISLER-carrierprint; ontwerp vervallen op 2026-10-09 | - | - | - |
| `kiwi` | Level shifter 3,3 V <-> 5 V | 8-kanaals bidirectionele Logic Level Converter - TXB0108-breakout | 1 | € 8,70 | https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836 |
| `te-bepalen` | UART-/uitbreidingsconnector | Eerder gekozen DEGSON 4-pins 3,5 mm; rechtstreeks bedraden kan de connector overbodig maken | - | - | - |
| `niet-nodig` | Socket-headers | Dual-wipe en turned-pin sockets; vervallen met de draagprint | - | - | - |
| `al-in-bezit` | Power-LED + serieweerstand | 3 mm LED rood (10-pack) + weerstand 330 Ω (10-pack) — **heeft de gebruiker thuis** | 1 | - | - |
| `kiwi` | Ontkoppelcondensatoren | Keramische condensator kit (15 soorten, 450 st.) | 1 | € 10,27 | https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492 |
| `kiwi` | Bulk-elco | 100 µF / 16 V op de 5 V-ingang | 1 | € 0,59 | https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440 |
| `niet-nodig` | I2C-pull-ups | Breakouts hebben ze al; eerdere reserve-footprints zijn niet nodig | - | - | - |
| `te-bepalen` | Behuizingsmontage | M3-set was bedoeld voor draagprintmontage; nieuwe bevestiging nog te ontwerpen | - | - | - |

> [!success] Level shifter gekozen (`2026-10-07`)
> De **TXB0108-breakout** (€ 8,70, Kiwi) blijft gekozen. De breakout wordt met draadverbindingen aangesloten; de concrete montage in de behuizing wordt nog uitgewerkt. De TXB0104-IC blijft geen gekozen aankoop.

> [!warning] Gekozen level shifter
> De **TXB0108** past bij de gekozen **TXB-serie** en is leverbaar bij Kiwi.
> Het antratek-alternatief (BSS138-converter, € 4,78) is goedkoper maar een ander type.

> [!warning] Historische montagekeuzes (`2026-10-06`)
> De eerder onderzochte 4-pins DEGSON-klem, sockets en M3-afstandbusjes waren bedoeld voor de draagprintopbouw. Ze zijn niet langer actieve bestelposten. Of een externe connector of bevestigingsmateriaal nodig is voor de 3D-geprinte behuizing, blijft open; zie [[bedrading-en-behuizing]].

> [!success] Power-LED en weerstand al in bezit (`2026-10-06`)
> De gebruiker heeft de **3 mm rode LED (10-pack)** en de **330 Ω-weerstand (10-pack)** al thuis.
> Deze regel staat op `al-in-bezit` en valt uit het te-bestellen-totaal (referentie Kiwi: € 1,20 +
> € 0,96 = € 2,16). Er blijft ruim overschot over de 10-packs.

## Kabels en verbruik (in bezit)

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | USB-C datakabel | Eigen kabel (flashen/programmeren) | 1 | - | - |
| `al-in-bezit` | Dupont-/siliconendraad | Heeft de gebruiker | - | - | - |
| `al-in-bezit` | USB A-kabel LoRa-ontvanger | USB-A -> USB-C voor de XIAO | 1 | - | - |
| `al-in-bezit` | Gereedschap | Schuifmaat, soldeerbout, tin, flux, multimeter, USB-serieel adapter | - | - | - |

## Mock-up (vliegtuigje)

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Arduino | Arduino Uno | 1 | - | - |
| `al-in-bezit` | Servo's | Bestaande voorraad (> 3) | 3+ | - | - |
| `al-in-bezit` | Servo-voeding | Aparte buck-converter | 1 | - | - |
| `al-in-bezit` | Romp en roeren | Eigen 3D-print | 1 | - | - |

## Totalen

| Winkel | Onderdelen | Bedrag (incl. btw) |
| --- | --- | --- |
| **Kiwi Electronics** | BNO085, BMP581, TXB0108, condensatorkit, bulk-elco | **€ 62,49** |
| **antratek.be** | 2× XIAO-kit, U.FL→SMA pigtail | **€ 33,83** |
| **TME (EU)** | LDO AP2112K-3.3 | **€ 0,27** |
| **Mouser/DigiKey (EU)** | PTC 1812L200/16 + TVS SMBJ10A (raming) — zonder P-MOSFET | **€ 1,00** |
| **AliExpress (China)** | LC29HDA-rover-developmentboard | **€ 36,99** |
| **Totaal actieve onderdelen excl. losse GNSS-antenne** | excl. nog te bepalen connectoren en behuizingsmontage | **€ 134,58** |
| **Totaal incl. voorwaardelijke losse GNSS-antenne** | antenne mogelijk al bij de kit | **€ 150,28** |
| **Niet meegerekend** | AISLER-print, sockets, PCB-barreljack, schroefklem en M3-set oude ontwerp | **€ 0,00** |

> [!info] Aannames bij de totalen
> De totalen gebruiken de laatst vastgelegde richtprijzen en sluiten de vervallen PCB/sockets en de nog onbesliste aansluit- en montagehardware uit. De Waveshare-antenne is voorwaardelijk. Bij AliExpress kunnen verzending en btw/checkoutkosten de richtprijs wijzigen.

## Open acties

- [x] **Andere winkel(s) voor de `geen-link`-onderdelen** — gevonden bij **TME, HESTORE,
      TinyTronics en Mouser/DigiKey (EU)** (`2026-10-06`).
- [x] **Bestaande prijzen en leveranciers vastgelegd** (`2026-10-07`); AISLER is door de ontwerpwijziging vervallen en montage-/connectorposten zijn tijdelijk uit de actieve totalen gehaald.
- [x] **Level shifter** — **TXB0108-breakout** (Kiwi, € 8,70); TXB0104-IC enkel als alternatief (`2026-10-07`).
- [x] **PCB-barreljack verwijderd** — niet meer nodig als printonderdeel; voedingsinvoer door/aan de behuizing blijft open (`2026-10-09`).
- [x] **Power-LED + 330 Ω (10-packs):** heeft de gebruiker **thuis** (`2026-10-06`).
- [x] **Ompoolbeveiliging (P-MOSFET):** **vervalt** (`2026-10-06`). Zie [[afgevoerd]].
- [ ] **LC29HDA-variant kiezen bij het bestellen** — op de AliExpress-pagina de **LC29HDA** (rover)
      selecteren, geassembleerd board (geen LC29HBS, geen losse SMD). Terugvaloptie: Waveshare-HAT (Eckstein € 71,39).
- [ ] **GNSS-antennebundel controleren** — eerst kijken of de boardkit een passende L1/L5-antenne meelevert;
      anders de Waveshare SKU 25346 (± € 15,70) bestellen en de connector (SMA vs. IPEX) checken.
- [ ] **Bedrading en mechanische montage uitwerken** — zie [[bedrading-en-behuizing]]; nog geen nieuwe hardware online zoeken of toevoegen.
- [ ] **LC29HDA-breakout in de behuizing monteren** — controleer boardafmetingen en bevestigingsmogelijkheden zodra de listing en variant bevestigd zijn.
- [ ] **Externe UART-verbinding bepalen** — bevestig of de eerder gekozen schroefklem nodig blijft of rechtstreeks bedraad wordt.

## Gerelateerd

- [[componenten]] - volledige BOM en keuzes
- [[specificaties]] - technische afspraken
- [[pcb-ontwerp]] - footprints en gatmaten
- [[links]] - bronnen
