---
tags: [gstem, data, bestellijst, bom, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: werklijst
---

# Bestellijst meettoestel (aan te kopen)

> [!info] Werkwijze
> Alle onderdelen uit [[componenten]]. Strategie: **zo veel mogelijk bij Kiwi Electronics**
> (verzendkosten beperken). Wat daar **goedkoper** is of als **reserve** dient, bij **antratek.be**.
> Voor de `geen-link`-onderdelen is op `2026-10-06` gezocht bij **andere winkels**: bij voorkeur
> **binnen de EU** (TME, Eckstein, HESTORE, TinyTronics, Bits & Parts, Mouser/DigiKey met EU-magazijn),
> China (AliExpress/LCSC) enkel als het echt niet anders kan.
> Prijzen zijn **incl. btw** en onder voorbehoud (`2026-10-06`). De Excel-versie staat in
> `documenten/Bestellijst-GSTEM.xlsx` (bron: `documenten/build-bestellijst.py`).

## Legende (tags)

| Tag | Betekenis |
| --- | --- |
| `kiwi` | Aankooplink gevonden bij Kiwi Electronics (NL) |
| `antratek` | Aankooplink gevonden bij antratek.be (goedkoper of reserve) |
| `tme` | Transfer Multisort Elektronik (Polen, EU) |
| `eckstein` | Eckstein (Duitsland, EU) |
| `hestore` | HESTORE (Hongarije, EU) |
| `tinytronics` | TinyTronics (Nederland, EU) |
| `mouser` | Mouser.be / DigiKey met **EU-magazijn** (levert binnen de EU, EU-btw) |
| `al-in-bezit` | Heeft de gebruiker al; niet aankopen |
| `geen-link` | Nog niet bij een geschikte winkel gevonden |
| `niet-nodig` | Bewust niet voorzien |
| `aisler` | Draagprint gefabriceerd bij AISLER |

> [!success] Bestelbaarheid geverifieerd (`2026-10-06`)
> Alle artikelen op deze lijst zijn nagelopen: alles is **nu bestelbaar**. Aandachtspunten:
> - **Kiwi:** lage voorraad bij de **keramische condensatorkit (2 st.)** en de **BMP581 (4 st.)**.
> - **Sockets (Preci-Dip):** bij TME enkel **business/MOQ 380** — een standaard 2,54 mm
>   turned-pin of dual-wipe socket is het praktische alternatief.
> - **P-MOSFET vervalt** (beslissing `2026-10-06`): er komt **geen** ompoolbeveiliging. Zie [[afgevoerd]].
> - **KF128-3.5 schroefklem bestaat niet bij TME**; neem de push-in **DEGSON DG250-3.5-04P** of de
>   schroefvariant **DEGSON 15EDGK-3.5/4P** (€ 1,10 bij HESTORE).
>
> Volledige verificatietabel: [[bestelbaarheid]]. GPS/RTK-prijsvergelijking: [[gps-rtk-prijzen]].

> [!tip] Twee nieuwe hoofdwinkels
> **TME (Polen)** dekt vrijwel alle **discrete elektronica** (LDO, MOSFET, TVS, PTC, schroefklemmen,
> precisie-sockets). **Eckstein (Duitsland)** levert de **Waveshare LC29H(DA)-breakout**. Beide zitten in
> de EU (geen invoerrechten, snelle levering). **TinyTronics (NL)** en **Bits & Parts (NL)** dekken de
> **M3-montage**. Voor exacte/EOL-onderdelen: **Mouser.be** of **DigiKey** (EU-magazijn, EU-btw).

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
| `eckstein` | RTK-GNSS-module (**breakout**/HAT) | Waveshare LC29H(DA) GPS/RTK HAT (art. WS25279, EAN 4060137304156) — incl. actieve dual-band L1/L5-antenne + IPEX→SMA-kabel + 40-pins header | 1 | € 71,39 | https://eckstein-shop.de/lc29h-dual-band-gps-module-raspberry-pi_1 |

> [!success] Beter én goedkoper dan voorheen
> De **BNO085** (€ 32,05) is goedkoper **en nieuwer** dan de BNO055 op antratek (€ 36,24).
> De **BMP581** (€ 10,88) is een **nauwkeuriger** barometer dan de BME280 en past bij de
> gebruikersvoorkeur om een beter model te nemen; de BMP390L is bij Kiwi **uit voorraad**.

> [!success] LC29H(DA)-breakout gevonden (EU) — `2026-10-06`
> De gekozen **Quectel LC29H(DA)** zit **niet** bij Kiwi of antratek, maar wel als **kant-en-klare
> breakout/HAT** bij andere EU-winkels. Voorkeur: **Waveshare LC29H(DA) GPS/RTK HAT (SKU 25279)** —
> dat is een **geassembleerd bord** (geen losse SMD-module) met UART/I²C-connector, Micro-USB,
> 40-pins Raspberry Pi-header en **meegeleverde actieve dual-band L1/L5-antenne**.
>
> | Winkel (EU) | Onderdeel | Prijs | Opmerking |
> | --- | --- | --- | --- |
> | **Eckstein (DE)** | Waveshare 25279 LC29H(DA) HAT | **€ 71,39 incl.** | art. WS25279 — **gekozen** (`2026-10-06`) |
> | Botland (PL/DE) | Waveshare 25279 LC29H(DA) HAT | € 70,50 incl. | alternatief, op voorraad |
> | Kamami (PL) | Waveshare 25279 LC29H(DA) HAT | ± € 63 incl. | goedkoopste EU, alternatief |
> | HESTORE (HU) | Waveshare 25279 LC29H(DA) HAT | € 91,21 excl. | duurder (± € 110 incl.) |
> | TME (PL) | MIKROE GNSS RTK 3 Click (LC29HDA, mikroBUS) | prijs op aanvraag | **niet op voorraad** |
>
> **Niet-EU-alternatief (enkel indien nodig):** *7Semi LC29HDA RTK Board* met Qwiic/USB-C (~$ 42,
> 7semi.com — India). Mooiere breakout-vorm, maar buiten de EU. De **losse LC29H-DA SMD-module**
> (bv. bij Maritex/Soyter, ± € 18–21) is **niet** gekozen, want de gebruiker wil een breakout board.

### Gekozen breakout: eigenschappen (Waveshare 25279)
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
| `al-in-bezit` | GNSS-antenne (actief, L1/L5, SMA) | **Inbegrepen bij de Waveshare LC29H(DA) HAT** | 1 | - | - |
| `antratek` | LoRa IPEX/U.FL -> SMA pigtail | Interface Cable SMA to U.FL (150 mm), SparkFun WRL-18568 | 1 | € 3,57 | https://www.antratek.be/u-fl-sma-150mm-cable |
| `al-in-bezit` | LoRa-antenne | Inbegrepen bij de XIAO-kit | 1 | - | - |

> [!success] Aparte GNSS-antenne vervalt
> De LC29H(DA)-HAT wordt **met een dual-band L1/L5-antenne geleverd**. Daardoor is de losse
> Kiwi-antenne (€ 16,93, **enkelbandig L1**) én de dure L1/L5-antenne op antratek (€ 120,94) **niet
> meer nodig** — een besparing en tegelijk een betere (dual-band) antenne. Enkel als reserve of bij
> een losse module blijft een antenne nodig.

> [!example]- Reserve/Terugvaloptie: losse antennes
> **Kiwi (L1, actief SMA):** € 16,93 —
> https://www.kiwi-electronics.com/nl/gps-antenne-externe-actieve-antenne-3-5v-28db-5-meter-sma-620.
> **Antratek (L1/L5, actief SMA),** € 120,94 —
> https://www.antratek.be/gnss-l1-l5-multi-band-high-precision-antenna-5m-sma.

> [!note] Pigtail
> Goedkoper op antratek (€ 3,57) dan Kiwi (€ 4,22) → op antratek laten staan.

## Voeding

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Accu (7,4 V) | 2S LiPo met connector en kabel | 1 | - | - |
| `al-in-bezit` | Voedingsaansluiting | DC Barrel Jack Adapter - Female | 1 | - | - |
| `al-in-bezit` | Buck-converter 5 V | Heeft de gebruiker | 1 | - | - |
| `tme`/`mouser` | Bescherming voeding | 2 A PTC + TVS SMBJ10A (op de print) | 1 set | ± € 1,00 | zie callout hieronder |
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

> [!note] Barrel-adapter
> De gevonden `DC Barrel Jack Adapter - Female` is een **adapter met schroefklem**, niet rechtstreeks
> PCB-montage. Voor de draagprint is een PCB-barreljack (of een draad naar de klem) nodig.

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
| `kiwi` | Level shifter 3,3 V <-> 5 V | 8-kanaals bidirectionele Logic Level Converter - TXB0108 | 1 | € 8,70 | https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836 |
| `hestore`/`tme` | Schroefklem 4-pins 3,5 mm | DEGSON **DG250-3.5-04P-11-00A(H)** (push-in) of KF128 (schroef) | 1 | € 0,61 | https://www.hestore.eu/en/prod_10044104.html |
| `tme`/`mouser` | Sockets | Dual-wipe (ESP32) + precisie/turned-pin (Preci-Dip) voor de rest | set | ± € 5,00 | https://int.rsdelivers.com/product/preci-dip/110-87-304-41-001101/preci-dip-110-254-mm-pitch-vertical-4-way-through/7020644P |
| `al-in-bezit` | Power-LED + serieweerstand | 3 mm LED rood (10-pack) + weerstand 330 Ω (10-pack) — **heeft de gebruiker thuis** | 1 | - | - |
| `kiwi` | Ontkoppelcondensatoren | Keramische condensator kit (15 soorten, 450 st.) | 1 | € 10,27 | https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492 |
| `kiwi` | Bulk-elco | 100 µF / 16 V op de 5 V-ingang | 1 | € 0,59 | https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440 |
| `niet-nodig` | I2C-pull-ups op de print | Breakouts hebben ze al; 2 reserve-footprints | 2 | - | - |
| `tinytronics` | Montage | M3-schroeven, moeren, afstandsbusjes, nylon spacers | set | € 8,00 | https://www.tinytronics.nl/nl/gereedschap-en-montage/installatie-en-montagemateriaal/afstandsbusjes/m3-afstandsbusje-kit |

> [!warning] Gekozen level shifter
> De **TXB0108** (€ 8,70) past bij de gekozen **TXB-serie** en is leverbaar bij Kiwi.
> Het antratek-alternatief (BSS138-converter, € 4,78) is goedkoper maar een ander type.

> [!success] Schroefklem, sockets en M3-montage gevonden — `2026-10-06`
> - **4-pins 3,5 mm schroefklem:** DEGSON **DG250-3.5-04P-11-00A(H)** bij HESTORE (€ 0,61) en TME;
>   de schroefvariant **KF128** is in de EU minder courant (vaak AliExpress/China), de push-in
>   DG250 is het EU-alternatief. Kiwi heeft enkel 3-weg.
> - **Precisie-sockets / dual-wipe:** turned-pin (machined) sockets van **Preci-Dip** (Zwitserland) en
>   **MPE Garry** via **TME** of **RS Components**; dual-wipe female headers via **Mouser.be**/TME.
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
| **Kiwi Electronics** | BNO085, BMP581, TXB0108, condensatorkit, bulk-elco | **€ 62,49** |
| **antratek.be** | 2× XIAO-kit, U.FL→SMA pigtail | **€ 33,83** |
| **Eckstein (DE, EU)** | LC29H(DA)-breakout (incl. dual-band antenne) | **€ 71,39** |
| **TME (EU)** | LDO AP2112K-3.3, precisie-sockets | **€ 5,27** |
| **Mouser/DigiKey (EU)** | PTC 1812L200/16 (+ TVS SMBJ10A) — **zonder P-MOSFET** | **€ 1,00** |
| **HESTORE (EU)** | Schroefklem DEGSON DG250-3.5-04P | **€ 0,61** |
| **TinyTronics (NL)** | M3-montageset | **€ 8,00** |
| **Totaal onderdelen (alle winkels)** | excl. AISLER-print | **€ 182,59** |
| **Totaal incl. AISLER-print (3 st.)** | onderdelen + print | **€ 215,35** |

> [!info] Wat is nieuw t.o.v. de vorige lijst
> Vroeger stonden **LC29H, bescherming, LDO, schroefklem, sockets en montage** als `geen-link` buiten
> het totaal. Nu zijn ze **allemaal gevonden** bij EU-winkels. De **aparte GNSS-antenne (€ 16,93)** is
> geschrapt omdat de LC29H(DA)-HAT er al één (dual-band) meelevert.
>
> Dezelfde cijfers staan in `documenten/Bestellijst-GSTEM.xlsx` (bron: `documenten/build-bestellijst.py`,
> per-winkel-subtotalen via `SUMIF`).

> [!info] Buiten deze bedragen
> Het **AISLER-printje** en de printspecifieke onderdelen staan in [[bestelschema-pcb]] (samen
> ± € 57,43 incl., waarvan ± € 9,79 al in deze lijst verrekend).

## Open acties

- [x] **Andere winkel(s) voor de `geen-link`-onderdelen** — gevonden bij **TME, Eckstein, HESTORE,
      TinyTronics en Mouser/DigiKey (EU)** (`2026-10-06`). Zie de callouts hierboven.
- [x] **RTK-module (LC29H of alternatief)** — **Waveshare LC29H(DA) GPS/RTK HAT** bij **Eckstein (DE, EU)**,
      € 71,39 incl. (`2026-10-06`).
- [ ] LoRa: wachten op voorraad Wio-SX1262 bij Kiwi, of de antratek-kit nemen?
- [x] GNSS-antenne: **vervalt** — de HAT levert een dual-band actieve antenne mee (`2026-10-06`).
- [ ] Barrel-connector: PCB-montage of adapter met schroefklem bevestigen.
- [x] Ompoolbeveiliging (P-MOSFET): **vervalt** (`2026-10-06`). Geen DMG2301L en geen AO3401A; gebruik een gepolariseerde connector. Zie [[afgevoerd]].
- [x] Bestelbaarheid en prijzen gecontroleerd (`2026-10-06`) → zie [[bestelbaarheid]]: alles bestelbaar, met lage voorraad bij Kiwi (BMP581, condensatorkit) en de socket-vraag bij TME.
- [x] **Power-LED + 330 Ω (10-packs):** heeft de gebruiker **thuis** (`2026-10-06`); valt uit het te-bestellen-totaal. Zie [[bestelschema-pcb]].
- [ ] Socket-keuze: Preci-Dip (business/MOQ 380) laten vallen en **standaard 2,54 mm turned-pin/dual-wipe** nemen?
- [x] GPS/RTK-winkel: **Eckstein (DE)** gekozen (`2026-10-06`), € 71,39 incl. Alternatieven blijven Kamami (± € 63) en Botland (€ 70,50). Zie [[gps-rtk-prijzen]].
- [ ] Footprint-afweging LC29H-HAT (65 × 30,5 mm, 40-pins) opnemen in [[pcb-ontwerp]].

## Gerelateerd

- [[componenten]] - volledige BOM en keuzes
- [[specificaties]] - technische afspraken
- [[pcb-ontwerp]] - footprints en gatmaten
- [[links]] - bronnen
