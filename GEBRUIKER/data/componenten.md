---
tags: [gstem, data, componenten, bom, hardware]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: werklijst
---

# Componentenlijst (BOM) meettoestel

> [!info] Doel
> Centrale lijst van alle onderdelen voor het meettoestel, met status: **gekozen**, **nog te kiezen**
> of **nog te noteren**. De gebruiker koopt alle componenten zelf aan; enkel de print wordt gemaakt
> (zie [[beslissingen]] `2026-10-06`). Hoort bij [[specificaties]], [[pcb-ontwerp]] en [[open-vragen]].

## Gekozen

| Functie | Onderdeel | Details | Bron |
| --- | --- | --- | --- |
| Rekenkern + LoRa | **XIAO ESP32S3 + Wio-SX1262 kit** | ESP32-S3 + SX1262 (sub-GHz, 868/915 MHz) via B2B; SPI; IPEX-antenne; USB-C; LiPo-lader; ± 14 I/O | antratek |
| 9-DoF IMU | **Adafruit BNO085-breakout** | I2C 0x28/0x29, 3,3 V-regelaar + level shifting, STEMMA QT/Qwiic, 25,6 x 22,7 mm | Kiwi Electronics |
| Barometer | **Adafruit BMP581** | Druk + temperatuur, I2C/SPI, STEMMA QT; nauwkeurig en bij Kiwi leverbaar (BMP390 is daar uit voorraad) | Kiwi Electronics |
| RTK-GNSS | **Quectel LC29HDA** | Dual-band L1+L5, multi-constellatie, RTK **rover** (centimeter-niveau), ingebouwde LNA + SAW; vervangende gebruikerslisting AliExpress-item 1005009915138674; variant, board/pinout en bundelinhoud nog te verifiëren | Quectel / [[gps-rtk-prijzen]] |
| RTK-correctie | **NTRIP-dienst** (via laptop) | Correcties (RTCM) naar de rover sturen; provider nog te kiezen | - |
| Sockettype | **Dual-wipe voor XIAO**, **precisie/gefreesd voor de rest** | Dual-wipe waar vaak gewisseld wordt (ESP32-S3); precisie voor vast gemonteerde modules (trillingen) | [[pcb-methodes-kosten]] |
| Voeding | **7,4 V-accu -> buck 5 V** (buck heeft de gebruiker), **barrel-connector** | XIAO op 5 V-pin; interne LiPo-lader niet gebruikt | - |
| Aan/uit | **Geen schakelaar** | Het toestel springt aan zodra het aan de voeding hangt | - |
| LoRa-ontvanger laptop | **Tweede XIAO ESP32S3 + Wio-SX1262 kit** | Zelfde hardware als het toestel | - |
| Arduino (mock-up) | **Arduino Uno** | Neemt CSV aan op TX/RX; heeft de gebruiker thuis (`2026-10-06`) | - |
| Servo's (mock-up) | **Bestaande servo's van de gebruiker (> 3)** | Type maakt niet uit; op de bestellijst zetten bij het opmaken | - |
| Servo-voeding (mock-up) | **Aparte buck-converter** | Heeft de gebruiker al | - |
| Behuizing/romp mock-up | **Eigen 3D-print** | Door de gebruiker zelf gemaakt | - |
| Gereedschap/verbruik | **Alles aanwezig** | Schuifmaat, soldeerbout, multimeter, enz. | - |
| Uitbreidingsconnector | **4-pins schroefklem, 3,5 mm (KF128/KF301)** | Pinout GND / +5 V / TX / RX; robuuste aansluiting voor de UART naar de Arduino | - |
| Level shifter | **TXB0108-breakout** (8-kanaals) op de print | Voor de UART naar de Arduino Uno (5 V); VCCA 3,3 V, VCCB 5 V. I2C blijft 3,3 V, dus geen shifter nodig op de I2C-bus. De TXB0104-IC (TSSOP-14) blijft een alternatief | TI / Kiwi |
| I2C-pull-ups op de print | **Geen extra** | BNO055- en BMP390-breakouts hebben al pull-ups; 2 reserve-footprints voor later | Adafruit |
| Bescherming voeding | **2 A PTC-zekering + TVS SMBJ10A** (de P-MOSFET vervalt, `2026-10-06`) | 7,4 V-accu, max 8,4 V; TVS-standoff 10 V; bulk-elco 100 uF/16 V | - |
| LDO 3,3 V | **AP2112K-3.3** (of AMS1117-3.3) | Eigen schone 3,3 V-rail voor de sensoren, op verzoek van de gebruiker; de XIAO levert ook 3,3 V | - |
| GNSS-antenne | **Actieve dual-band L1/L5 GNSS-antenne met passende connector, LNA + ground plane** | Nodig als de gekozen LC29HDA-breakout deze niet meelevert; bundelinhoud en RF-connector controleren bij de listing | Nog te verifiëren |
| LoRa-antenne buiten | **IPEX/U.FL -> SMA female bulkhead pigtail** | Om de LoRa-antenne door/buiten de behuizing te monteren; de kitantenne blijft behouden | - |

> [!warning] Gevolg van de XIAO-kit
> ESP32 en LoRa zijn **één module**; op de draagprint is dat een enkele footprint. De XIAO heeft
> een **ingebouwde LiPo-lader** en een eigen 3,3 V-regelaar (op de 3V3-pin). Pin-budget: controleer
> of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART.

> [!note] Waarvoor dient de voedingsbescherming en de LDO?
> De energiestroom is: **7,4 V-accu (max 8,4 V) / barrel -> bescherming -> buck 5 V -> bulk-elco -> LDO 3,3 V -> sensoren**.
> - **2 A PTC-zekering** = herstelbare zekering in serie: bij overstroom/kortsluiting wordt ze hoogohmig en begrenst de stroom; koelt af en reset zichzelf. Beschermt de LiPo en de bedrading (brandgevaar).
> - ~~**P-MOSFET DMG2301L** = ompoolbeveiliging~~ — **vervalt** (`2026-10-06`). De gebruiker kiest
>   **geen** ompoolbeveiliging; bescherm tegen omgekeerd aansluiten met een **gepolariseerde
>   connector** (XT60/JST-XH). Zie [[afgevoerd]] en [[beslissingen]].
>
> [!warning] Waarom de P-MOSFET vervalt (`2026-10-06`)
> De kandidaten **DMG2301L** (Vgs(max) ±8 V, te krap bij een 2S-accu van max 8,4 V zonder gate-clamp)
> en **AO3401A** (Vds -30 V, Vgs ±12 V) komen **geen van beide** op de print: er is **geen
> ompoolbeveiliging** voorzien. De PTC-zekering en de TVS blijven wel behouden.
> - **TVS SMBJ10A** = **transiënt-/spikebeveiliging** van + naar GND: klemt snelle spanningspieken (motoren/ESC, hot-plug, ESD) op ~17 V. Standoff 10 V ligt boven de max. accu (8,4 V) en beschermt de buck/LDO/IC's.
> - **AP2112K-3.3 (LDO)** = lineaire regelaar die van de schakelende 5 V een **schone, ruisarme 3,3 V-rail** maakt voor de sensoren (IMU, barometer, GNSS). De XIAO heeft zelf ook 3,3 V, maar die rail deelt de schakelruis van de buck.

> [!note] LoRa-antenne
> De LoRa-antenne **zit bij de kit** (`2026-10-06`). Omdat de antenne **buiten het vliegtuigje**
> geconnecteerd moet worden, komt er een **IPEX/U.FL -> SMA female bulkhead pigtail** bij (zie
> "Gekozen").

## Nog te kiezen

| Functie | Opties / kandidaten | Opmerking |
| --- | --- | --- |
| NTRIP-provider | **gratis dienst** | De gebruiker zoekt zelf een gratis provider. |
| Socket exact model | precisie/gefreesd merk + dual-wipe merk | Nog te bepalen; hoeft **niet per se op de bestellijst**. |

## Nog te noteren (ontbrak in de lijst)

**Voeding**
- 7,4 V-accu met connector en kabel: **heeft de gebruiker** (`2026-10-06`, 2S LiPo).
- Barrel-connector (gekozen als voedingsaansluiting): **DC Barrel Jack Adapter - Female heeft de gebruiker** (`2026-10-06`).
- Buck-converter 5 V (heeft de gebruiker).
- Bescherming: 2 A PTC-zekering + TVS SMBJ10A (geen P-MOSFET; `2026-10-06`).

**Verbindingen**
- USB-C datakabel: **in bezit** (eigen kabel voor flashen/programmeren `2026-10-06`) — niet op de bestellijst.
- UART-draden meettoestel <-> Arduino met **schroefklem-connectoren**; **gemeenschappelijke ground** en **level shifter** horen erbij.
- Dupont-/siliconendraad: **in bezit** (gebruiker heeft dit zelf `2026-10-06`) — niet op de bestellijst.
- USB A-kabel voor de LoRa-ontvanger: **heeft de gebruiker** (USB-A naar USB-C, `2026-10-06`) — niet op de bestellijst.

**RF**
- GNSS-antenne: gekozen (zie "Gekozen").
- LoRa IPEX -> SMA-pigtail: gekozen (zie "Gekozen") — nodig om de antenne buiten het vliegtuigje te connecteren.

**Montage / behuizing**
- M3-schroeven, moeren, afstandsbusjes (standoffs), nylon spacers — nodig, toevoegen bij de bestellijst.
- 3D-printmateriaal voor de romp (door de gebruiker).

**Mock-up (vliegtuigje)**
- Servo's (bestaande voorraad) — op de bestellijst zetten.
- Servo-voeding/BEC = aparte buck (heeft de gebruiker).

**Laptop-/ontvangerzijde**
- USB A-kabel; tweede XIAO-kit.

## Essentieel op de print (advies)

De gebruiker koos **LED + sockets** en vraagt wat verder essentieel is. Voorstel (te bevestigen bij het schema):

| Onderdeel | Waarom | Aantal |
| --- | --- | --- |
| Power-LED + serieweerstand | Status van de voeding | 1 |
| Sockets (2,54 mm) voor alle modules | Modules blijven vervangbaar | - |
| 100 nF + 10 uF per voedingspin van de modules | Ontkoppeling tegen ruis/brownouts | per socket |
| Bulk-elco 100 uF op de 5 V-ingang | Vangt stroompieken op (LoRa-zenden) | 1 |
| I2C-pull-ups 4,7 kOhm | **Enkel indien** de breakouts ze niet al hebben; BNO055 en BMP390-breakout hebben ze mee | 2 (reserve) |
| Barrel-connector + schroefklemmen | Voeding en UART naar buiten | 1 + 1 |
| Bevestigingsgaten M3 | Montage in de behuizing | 4 |
| Zekering + TVS | Bescherming van de voeding | 2 A PTC + SMBJ10A (P-MOSFET vervalt `2026-10-06`) |
| Level shifter | 3,3 V <-> 5 V naar de Arduino | TXB0104 (4-kanaals) |
| Schroefklem 3,5 mm (4-pins) | UART-uitbreiding naar de Arduino | 1 |

> [!tip] Niet dubbel plaatsen
> I2C-pull-ups: de Adafruit BNO055- en BMP390-breakouts hebben al pull-ups. Zet ze op de print
> alleen als een module ze mist, anders wordt de I2C-bus te zwaar belast.

## Te zoeken: werkorder (1 per 1)

> [!info] Werkwijze
> Voorgestelde volgorde om de open componenten een per een af te handelen. **A eerst**, want die
> bepaalt de footprints en de stuklijst van de draagprint. Vink af zodra gekozen en genoteerd.

**A. Bordkritisch (bepaalt de PCB)**
- [x] 1. Barometer -> **Adafruit BMP390** (`2026-10-06`)
- [x] 2. RTK-GNSS-module -> **Quectel LC29H(DA)** (`2026-10-06`)
- [x] 3. Bron RTK-correctie -> **NTRIP-dienst** (`2026-10-06`)
- [x] 4. Sockettype -> **dual-wipe ESP, precisie voor de rest** (`2026-10-06`)
- [x] 5. Uitbreidingsconnector -> **4-pins schroefklem 3,5 mm** (`2026-10-06`)
- [x] 6. I2C-pull-ups en level shifter -> **geen extra pull-ups** (breakouts hebben ze); **level shifter TXB0104** (`2026-10-06`)
- [x] 7. Wat komt op de print vs losse modules -> advies hierboven; nog te bevestigen (`2026-10-06`)

**B. Voeding en RF**
- [x] 8. 7,4 V-accu + beschermcircuit + connector -> accu + barrel + bescherming gekozen (`2026-10-06`)
- [x] 9. Zekering, ompoolbeveiliging, TVS -> **2 A PTC + TVS SMBJ10A** (`2026-10-06`); **ompoolbeveiliging vervalt** (`2026-10-06`)
- [x] 10. Buck-converter 5 V -> heeft de gebruiker (`2026-10-06`)
- [x] 11. LDO 3,3 V -> **AP2112K-3.3** (eigen 3,3 V-rail) (`2026-10-06`)
- [x] 12. Aan/uit-schakelaar -> **geen**; toestel start bij voeding (`2026-10-06`)
- [x] 13. GNSS-antenne -> **actieve dual-band L1/L5 met SMA (Waveshare)** (`2026-10-06`)
- [x] 14. LoRa IPEX -> SMA-pigtail + SMA-bulkhead -> **gekozen: nodig voor externe antenne** (`2026-10-06`)
- [x] 15. LoRa-antenne -> **zit bij de kit** (`2026-10-06`)

**C. Verbindingen en montage**
- [x] 16. USB-C datakabel -> **in bezit** (eigen kabel) (`2026-10-06`)
- [ ] 17. UART-draden met schroefklemmen + gemeenschappelijke ground + level shifter (bevestigd `2026-10-06`; type level shifter nog te zoeken)
- [x] 18. Dupont-/siliconendraad -> **in bezit** (`2026-10-06`)
- [ ] 19. M3-schroeven, moeren, standoffs, spacers (bij de bestellijst)

**D. Laptop-/ontvangerzijde**
- [x] 20. LoRa-ontvanger -> **tweede XIAO-kit** (`2026-10-06`)
- [x] 21. USB A-kabel voor de ontvanger (`2026-10-06`)

**E. Mock-up (vliegtuigje)**
- [x] 22. Arduino -> **Uno** (`2026-10-06`)
- [x] 23. Servo's -> **bestaande voorraad (> 3)**, type vrij (`2026-10-06`)
- [x] 24. Servo-voeding/BEC -> **aparte buck, heeft de gebruiker** (`2026-10-06`)
- [x] 25. Stuurstangen, scharnieren, roerbladen, romp -> **eigen 3D-print** (`2026-10-06`)

**F. Gereedschap en verbruik**
- [x] 26. Digitale schuifmaat -> aanwezig (`2026-10-06`)
- [x] 27. Soldeerbout, tin, flux -> aanwezig (`2026-10-06`)
- [x] 28. Multimeter -> aanwezig (`2026-10-06`)
- [x] 29. USB-serieel adapter -> aanwezig (`2026-10-06`)

## Gerelateerd

- [[bestellijst]] - aan te kopen onderdelen met link, kost en aantal (Excel: `documenten/beheer/Bestellijst-GSTEM.xlsx`). De actieve bestellijst gebruikt de **BNO085 + BMP581** (Kiwi), de **TXB0108-breakout** en een **LC29HDA-breakout**; de oudere BNO055/BMP390 horen hier niet meer bij.
- [[specificaties]] - draagprint-aanpak en gebruikersspecificaties
- [[pcb-ontwerp]] - footprints en gatmaten
- [[pcb-schets]] - bovenaanzicht en verbindingsschema
- [[open-vragen]] - nog te beslissen punten
- [[beslissingen]] - de keuzes van `2026-10-06`

## AI-taken

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`)
- [x] Meest accurate barometer zoeken -> **BMP390** (`2026-10-06`)
- [x] RTK-GNSS-module en GNSS-antenne zoeken -> **LC29H(DA)** + dual-band actieve antenne (`2026-10-06`)
- [x] Bepalen wat essentieel is op de print naast LED + sockets -> advies hierboven (`2026-10-06`)
- [x] Level shifter 3,3 V <-> 5 V uitzoeken -> **TXB0104** (`2026-10-06`)
- [x] Bescherming van de voeding uitzoeken -> **PTC + TVS SMBJ10A**; geen P-MOSFET (`2026-10-06`)
