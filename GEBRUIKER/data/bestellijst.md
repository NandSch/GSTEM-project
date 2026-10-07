---
tags: [gstem, data, bestellijst, bom, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-07
status: definitief; enkel de LC29HDA-variant aanduiden bij het bestellen
---

# Bestellijst meettoestel (aan te kopen)

> [!info] Werkwijze
> Alle onderdelen uit [[componenten]]. Voorkeur blijft: **zo veel mogelijk bij Kiwi Electronics**
> en de rest bij passende EU-winkels, behalve de **RTK-GNSS-module (LC29HDA)** die sinds
> `2026-10-07` bij **AliExpress (China)** gekocht wordt. Prijzen zijn **incl. btw** tenzij anders
> vermeld en onder voorbehoud. De Excel-versie staat in `documenten/beheer/Bestellijst-GSTEM.xlsx`
> (bron: `documenten/scripts/build-bestellijst.py`).

> [!success] Alles is nu definitief
> Alle functies hebben een **gekozen onderdeel, winkel, aantal en prijs**. Er blijft nog één
> controle bij het bestellen: de AliExpress-GPS moet de **LC29HDA-variant** (RTK-**rover**) zijn,
> niet de LC29HBS (basisstation) en niet de losse SMD-module. Zie de callout bij de sensoren.

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
| `aisler` | Draagprint gefabriceerd bij AISLER |

> [!info] Bestelbaarheid geverifieerd (`2026-10-06`)
> De onderdelen bij de EU-winkels zijn nagelopen en bestelbaar. Aandachtspunten:
> - **Kiwi:** lage voorraad bij de **keramische condensatorkit (2 st.)** en de **BMP581 (4 st.)**.
> - **Sockets:** standaard 2,54 mm turned-pin of dual-wipe sockets nemen; de Preci-Dip bij TME is
>   business/MOQ 380 en dus onpraktisch.
> - **P-MOSFET vervalt** (beslissing `2026-10-06`): er komt **geen** ompoolbeveiliging. Zie [[afgevoerd]].
> - **KF128-3.5 schroefklem bestaat niet bij TME**; neem de push-in **DEGSON DG250-3.5-04P** of de
>   schroefvariant **DEGSON 15EDGK-3.5/4P** (€ 1,10 bij HESTORE).
>
> Volledige verificatietabel: [[bestelbaarheid]]. GPS/RTK-prijsvergelijking: [[gps-rtk-prijzen]].

> [!tip] Winkels
> **TME (Polen)** dekt de **discrete elektronica** (LDO, TVS, schroefklemmen, sockets).
> De **LC29HDA-RTK-rover** komt bij **AliExpress (China)**. **Eckstein (Duitsland)** met de
> Waveshare-HAT (€ 71,39) blijft de **terugvaloptie**. **TinyTronics (NL)** en **Bits & Parts (NL)**
> dekken de **M3-montage**. Voor exacte/EOL-onderdelen: **Mouser.be** of **DigiKey** (EU-magazijn, btw).

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
>   houd hier rekening mee bij de **draagprint-footprint** ([[pcb-ontwerp]], [[bestelschema-pcb]]).

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
| `kiwi` | Voedingsaansluiting (op de print) | 2,1 mm DC-barreljack, breadboard-/PCB-compatibel | 1 | € 1,20 | https://www.kiwi-electronics.com/nl/2-1mm-dc-barrel-jack-breadboard-compatible-415 |
| `al-in-bezit` | Buck-converter 5 V | Heeft de gebruiker | 1 | - | - |
| `mouser` | Bescherming voeding | 2 A PTC Littelfuse 1812L200/16 + TVS SMBJ10A-TR (op de print) | 1 set | ± € 1,00 | https://www.mouser.com/ProductDetail/Littelfuse/1812L200-16DR |
| `niet-nodig` | Ompoolbeveiliging (P-MOSFET) | P-MOSFET DMG2301L / AO3401A (SOT-23) | - | - | **vervalt** (`2026-10-06`) |
| `tme` | LDO 3,3 V | AP2112K-3.3TRG1 (SOT-23-5) (op de print) | 1 | € 0,27 | https://www.tme.eu/en/details/ap2112k-3.3trg1/ldo-fixed-voltage-regulators/diodes-incorporated/ |
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

> [!note] Barrel-connector
> De gebruiker heeft een **female barrel-adapter met schroefklem** (voor de kabelzijde). Voor een
> nette montage op de draagprint komt daar de **PCB-breadboard-barreljack** (€ 1,20, Kiwi) bij.

> [!info] Printkost
> De productie van de draagprint bij **AISLER** (± € 32,76 incl. btw voor 3 stuks) en de
> onderdelen op de print staan apart in [[bestelschema-pcb]].

## Print en verbindingen

> [!success] Print bij AISLER (`2026-10-06`)
> De draagprint wordt gemaakt bij **AISLER** (2-laags, 1,6 mm HASL Budget). Schatting **± € 32,76
> incl. btw voor 3 stuks** (aanname 100 x 75 mm). Alle productie- en onderdelenkosten staan in
> [[bestelschema-pcb]].

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `aisler` | Draagprint (PCB) | 2-laags 1,6 mm HASL, set van 3 | 3 | ± € 10,92 | https://aisler.net |
| `kiwi` | Level shifter 3,3 V <-> 5 V | 8-kanaals bidirectionele Logic Level Converter - TXB0108 (breakout) | 1 | € 8,70 | https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836 |
| `hestore` | Schroefklem 4-pins 3,5 mm | DEGSON **DG250-3.5-04P-11-00A(H)** (push-in) of KF128 (schroef) | 1 | € 0,61 | https://www.hestore.eu/en/prod_10044104.html |
| `tme` | Sockets | Dual-wipe female headers (XIAO + sensoren) + turned-pin precisie-sockets (vaste modules) | set | ± € 5,00 | https://www.mouser.com/c/connectors/headers-wire-housings/ |
| `al-in-bezit` | Power-LED + serieweerstand | 3 mm LED rood (10-pack) + weerstand 330 Ω (10-pack) — **heeft de gebruiker thuis** | 1 | - | - |
| `kiwi` | Ontkoppelcondensatoren | Keramische condensator kit (15 soorten, 450 st.) | 1 | € 10,27 | https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492 |
| `kiwi` | Bulk-elco | 100 µF / 16 V op de 5 V-ingang | 1 | € 0,59 | https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440 |
| `niet-nodig` | I2C-pull-ups op de print | Breakouts hebben ze al; 2 reserve-footprints | 2 | - | - |
| `tinytronics` | Montage | M3-schroeven, moeren, afstandsbusjes, nylon spacers | set | € 8,00 | https://www.tinytronics.nl/nl/gereedschap-en-montage/installatie-en-montagemateriaal/afstandsbusjes/m3-afstandsbusje-kit |

> [!success] Level shifter gekozen (`2026-10-07`)
> Definitief de **TXB0108-breakout** (€ 8,70, Kiwi): 8 kanalen, direct bruikbaar op de print zonder
> TSSOP-soldeerwerk. Het alternatief — de **TXB0104-IC** (4 kanalen, TSSOP-14, ± € 1,80) — blijft
> enkel een optimalisatie en wordt **niet** besteld.

> [!warning] Gekozen level shifter
> De **TXB0108** past bij de gekozen **TXB-serie** en is leverbaar bij Kiwi.
> Het antratek-alternatief (BSS138-converter, € 4,78) is goedkoper maar een ander type.

> [!success] Schroefklem, sockets en M3-montage gevonden — `2026-10-06`
> - **4-pins 3,5 mm schroefklem:** DEGSON **DG250-3.5-04P-11-00A(H)** bij HESTORE (€ 0,61) en TME;
>   de schroefvariant **KF128** is in de EU minder courant (vaak AliExpress/China), de push-in
>   DG250 is het EU-alternatief. Kiwi heeft enkel 3-weg.
> - **Sockets:** standaard **2,54 mm turned-pin (machined) sockets** en **dual-wipe female headers**
>   uit de hobbyhandel (Mouser/DigiKey/TME); de Preci-Dip is bij TME enkel business/MOQ 380.
> - **M3-montage:** **TinyTronics (NL)** *M3 Afstandsbusje Kit* € 8,00, of **Bits & Parts (NL)**
>   180-delige spacer-set € 6,95 — https://www.bitsandparts.nl/Afstandsbus-Spacer-Standoff-M3-set-180-delig-zwart-p1885552.

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
| **Kiwi Electronics** | BNO085, BMP581, TXB0108, condensatorkit, bulk-elco, PCB-barreljack | **€ 63,69** |
| **antratek.be** | 2× XIAO-kit, U.FL→SMA pigtail | **€ 33,83** |
| **TME (EU)** | LDO AP2112K-3.3, sockets | **€ 5,27** |
| **Mouser/DigiKey (EU)** | PTC 1812L200/16 (+ TVS SMBJ10A) — **zonder P-MOSFET** | **€ 1,00** |
| **HESTORE (EU)** | Schroefklem DEGSON DG250-3.5-04P | **€ 0,61** |
| **TinyTronics (NL)** | M3-montageset | **€ 8,00** |
| **AliExpress (China)** | LC29HDA-rover-developmentboard | **€ 36,99** |
| **Waveshare** | Losse GNSS-antenne SKU 25346 (voorwaardelijk) | **€ 15,70** |
| **Totaal onderdelen excl. losse GNSS-antenne en AISLER** | | **€ 149,39** |
| **Totaal onderdelen incl. losse GNSS-antenne (excl. AISLER)** | | **€ 165,09** |
| **Totaal incl. AISLER-print (3 st.) excl. losse antenne** | verzend- en invoerkosten niet inbegrepen | **€ 182,15** |
| **Totaal alles (incl. losse antenne + AISLER-print)** | bovengrens; antenne mogelijk niet nodig | **€ 197,85** |

> [!info] Buiten deze bedragen
> Het **AISLER-printje** en de printspecifieke onderdelen staan in [[bestelschema-pcb]] (samen
> ± € 57,43 incl., waarvan ± € 9,79 al in deze lijst verrekend). Bij AliExpress komen mogelijk
> verzending/btw (IOSS) bovenop; bij een EU-kit betaal je die via de winkelprijs.

## Open acties

- [x] **Andere winkel(s) voor de `geen-link`-onderdelen** — gevonden bij **TME, HESTORE,
      TinyTronics en Mouser/DigiKey (EU)** (`2026-10-06`).
- [x] **Prijzen en winkels definitief** (`2026-10-07`): Kiwi, antratek, TME, Mouser/DigiKey,
      HESTORE, TinyTronics, AliExpress en AISLER.
- [x] **Level shifter** — **TXB0108-breakout** (Kiwi, € 8,70); TXB0104-IC enkel als alternatief (`2026-10-07`).
- [x] **Voedingsaansluiting op de print** — PCB-breadboard-barreljack (Kiwi, € 1,20) toegevoegd naast de bestaande adapter (`2026-10-07`).
- [x] **Power-LED + 330 Ω (10-packs):** heeft de gebruiker **thuis** (`2026-10-06`).
- [x] **Ompoolbeveiliging (P-MOSFET):** **vervalt** (`2026-10-06`). Zie [[afgevoerd]].
- [ ] **LC29HDA-variant kiezen bij het bestellen** — op de AliExpress-pagina de **LC29HDA** (rover)
      selecteren, geassembleerd board (geen LC29HBS, geen losse SMD). Terugvaloptie: Waveshare-HAT (Eckstein € 71,39).
- [ ] **GNSS-antennebundel controleren** — eerst kijken of de boardkit een passende L1/L5-antenne meelevert;
      anders de Waveshare SKU 25346 (± € 15,70) bestellen en de connector (SMA vs. IPEX) checken.
- [ ] **Socket-aantal definitief maken** zodra de KiCad-footprints vastliggen (aantal pinnen per module).
- [ ] **Footprint en montage van de LC29HDA-breakout** opnemen in [[pcb-ontwerp]] zodra bordmaat en pinout gekend zijn.
- [ ] **Barrel-connector op de print** afstemmen (positive tip, 2,1 mm) met de bestaande kabel-adapter.

## Gerelateerd

- [[componenten]] - volledige BOM en keuzes
- [[specificaties]] - technische afspraken
- [[pcb-ontwerp]] - footprints en gatmaten
- [[links]] - bronnen
