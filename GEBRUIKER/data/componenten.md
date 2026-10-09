---
tags: [gstem, data, componenten, bom, hardware]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: componenten-BOM; fysieke bedrading en montage nog uit te werken
---

# Componentenlijst (BOM) meettoestel

> [!warning] Ontwerpwijziging — 2026-10-09
> De gebruiker bedradt en soldeert de breakoutmodules zelf en monteert de onderdelen aan een 3D-geprinte behuizing. De extra draagprint en alle sockets zijn vervallen; de breakoutmodules zelf blijven behouden. Oude regels hieronder die spreken over montage op de print zijn historisch en worden herzien zodra de bedrading en behuizing zijn uitgewerkt. Zie [[bedrading-en-behuizing]].

## Gekozen

| Functie | Onderdeel | Details | Bron |
| --- | --- | --- | --- |
| Rekenkern + LoRa | **XIAO ESP32S3 + Wio-SX1262 kit** | ESP32-S3 + SX1262 (sub-GHz, 868/915 MHz) via B2B; SPI; IPEX-antenne; USB-C; LiPo-lader; ± 14 I/O | antratek |
| 9-DoF IMU | **Adafruit BNO085-breakout** | I2C 0x28/0x29, 3,3 V-regelaar + level shifting, STEMMA QT/Qwiic, 25,6 x 22,7 mm | Kiwi Electronics |
| Barometer | **Adafruit BMP581** | Druk + temperatuur, I2C/SPI, STEMMA QT; nauwkeurig en bij Kiwi leverbaar (BMP390 is daar uit voorraad) | Kiwi Electronics |
| RTK-GNSS | **Quectel LC29HDA** | Dual-band L1+L5, multi-constellatie, RTK **rover** (centimeter-niveau), ingebouwde LNA + SAW; vervangende gebruikerslisting AliExpress-item 1005009915138674; variant, board/pinout en bundelinhoud nog te verifiëren | Quectel / [[gps-rtk-prijzen]] |
| RTK-correctie | **NTRIP-dienst** (via laptop) | Correcties (RTCM) naar de rover sturen; provider nog te kiezen | - |
| Moduleverbinding | **Handbedraden en solderen** | Geen sockets of eigen carrier-PCB; de concrete bedradingsroute en trekontlasting zijn nog open | [[bedrading-en-behuizing]] |
| Voeding | **7,4 V-accu -> buck 5 V** (buck heeft de gebruiker), **barrel-connector** | XIAO op 5 V-pin; interne LiPo-lader niet gebruikt | - |
| Aan/uit | **Geen schakelaar** | Het toestel springt aan zodra het aan de voeding hangt | - |
| LoRa-ontvanger laptop | **Tweede XIAO ESP32S3 + Wio-SX1262 kit** | Zelfde hardware als het toestel | - |
| Arduino (mock-up) | **Arduino Uno** | Neemt CSV aan op TX/RX; heeft de gebruiker thuis (`2026-10-06`) | - |
| Servo's (mock-up) | **Bestaande servo's van de gebruiker (> 3)** | Type maakt niet uit; op de bestellijst zetten bij het opmaken | - |
| Servo-voeding (mock-up) | **Aparte buck-converter** | Heeft de gebruiker al | - |
| Behuizing/romp mock-up | **Eigen 3D-print** | Door de gebruiker zelf gemaakt | - |
| Gereedschap/verbruik | **Alles aanwezig** | Schuifmaat, soldeerbout, multimeter, enz. | - |
| Uitbreidingsconnector | **4-pins schroefklem, 3,5 mm (KF128/KF301)** | Pinout GND / +5 V / TX / RX; robuuste aansluiting voor de UART naar de Arduino | - |
| Level shifter | **TXB0108-breakout** (8-kanaals) | Voor UART naar de Arduino Uno (5 V); VCCA 3,3 V, VCCB 5 V. Breakout wordt handbedraad; mechanische montage nog uit te werken. | TI / Kiwi |
| I2C-pull-ups | **Geen extra** | Breakouts hebben pull-ups; de reserve-footprints van het oude PCB-ontwerp zijn niet meer nodig | Adafruit |
| Bescherming voeding | **2 A PTC-zekering + TVS SMBJ10A** (de P-MOSFET vervalt, `2026-10-06`) | 7,4 V-accu, max 8,4 V; TVS-standoff 10 V; bulk-elco 100 uF/16 V; fysieke montage/bedrading nog uit te werken | - |
| LDO 3,3 V | **AP2112K-3.3** (of AMS1117-3.3) | Eigen schone 3,3 V-rail voor sensoren; component en functie voorlopig behouden, handbedrading/montage nog uit te werken | - |
| GNSS-antenne | **Actieve dual-band L1/L5 GNSS-antenne met passende connector, LNA + ground plane** | Nodig als de gekozen LC29HDA-breakout deze niet meelevert; bundelinhoud en RF-connector controleren bij de listing | Nog te verifiëren |
| LoRa-antenne buiten | **IPEX/U.FL -> SMA female bulkhead pigtail** | Om de LoRa-antenne door/buiten de behuizing te monteren; de kitantenne blijft behouden | - |

> [!warning] Gevolg van de XIAO-kit
> ESP32 en LoRa zijn **één kit/module** en worden volgens de nieuwe opbouw met draden aangesloten; er komt geen carrier-footprint of socket. De XIAO heeft een ingebouwde LiPo-lader en eigen 3,3 V-regelaar (op de 3V3-pin). Pin-budget: controleer of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART.

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
| Bedrading en montage | Draadverbindingen solderen; bevestiging aan geprinte behuizing | De aanpak is gekozen; details nog te bepalen in [[bedrading-en-behuizing]]. |

## Nog te noteren (ontbrak in de lijst)

**Voeding**
- 7,4 V-accu met connector en kabel: **heeft de gebruiker** (`2026-10-06`, 2S LiPo).
- Barrel-connector (gekozen als voedingsaansluiting): **DC Barrel Jack Adapter - Female heeft de gebruiker** (`2026-10-06`).
- Buck-converter 5 V (heeft de gebruiker).
- Bescherming: 2 A PTC-zekering + TVS SMBJ10A (geen P-MOSFET; `2026-10-06`).

**Verbindingen**
- USB-C datakabel: **in bezit** (eigen kabel voor flashen/programmeren `2026-10-06`) — niet op de bestellijst.
- UART-draden meettoestel <-> Arduino met gemeenschappelijke ground en de gekozen level shifter; bevestig nog of de oude schroefklem nodig blijft bij de handbedrade uitvoering.
- Dupont-/siliconendraad: **in bezit** (gebruiker heeft dit zelf `2026-10-06`) — niet op de bestellijst.
- USB A-kabel voor de LoRa-ontvanger: **heeft de gebruiker** (USB-A naar USB-C, `2026-10-06`) — niet op de bestellijst.

**RF**
- GNSS-antenne: gekozen (zie "Gekozen").
- LoRa IPEX -> SMA-pigtail: gekozen (zie "Gekozen") — nodig om de antenne buiten het vliegtuigje te connecteren.

**Montage / behuizing**
- Modules en losse componenten worden aan een zelf 3D-geprinte behuizing gemonteerd; bevestigingsmethode nog te bepalen.
- De eerder genoemde M3-set was bedoeld voor de vervallen draagprint en staat niet als actieve aankoop.
- Beschikbaarheid van geschikt 3D-printmateriaal nog bevestigen; nog niet toevoegen aan de bestellijst.

**Mock-up (vliegtuigje)**
- Servo's (bestaande voorraad) — op de bestellijst zetten.
- Servo-voeding/BEC = aparte buck (heeft de gebruiker).

**Laptop-/ontvangerzijde**
- USB A-kabel; tweede XIAO-kit.

## Historische lijst: onderdelen op de vervallen draagprint

> [!warning] Niet meer gebruiken als montageplan
> De draagprint en sockets zijn vervallen. Elektrische functies van onderdelen kunnen behouden blijven, maar de bedradingsmethode en mechanische ondersteuning in de behuizing moeten opnieuw worden uitgewerkt. Zie [[bedrading-en-behuizing]].

De onderstaande lijst is de oude carrier-PCB-opzet en dient alleen als naslag voor elektrische functies:

| Onderdeel | Waarom | Aantal |
| --- | --- | --- |
| Power-LED + serieweerstand | Status van de voeding | 1 |
| Socket-headers (2,54 mm) | Vervallen; modules worden zelf bedraad en gesoldeerd | niet nodig |
| 100 nF + 10 uF per voedingspin van de modules | Ontkoppeling tegen ruis/brownouts | per socket |
| Bulk-elco 100 uF op de 5 V-ingang | Vangt stroompieken op (LoRa-zenden) | 1 |
| I2C-pull-ups 4,7 kOhm | **Enkel indien** de breakouts ze niet al hebben; BNO055 en BMP390-breakout hebben ze mee | 2 (reserve) |
| Barrel-connector + schroefklemmen | Voeding en UART naar buiten | 1 + 1 |
| Bevestigingsgaten M3 in carrier-PCB | De carrier-PCB is vervallen; montage in de behuizing nog te bepalen | niet nodig |
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

**A. Oude PCB-kritische keuzes (vervallen als PCB-taken)**
- [x] 1. Barometer -> **Adafruit BMP390** (`2026-10-06`)
- [x] 2. RTK-GNSS-module -> **Quectel LC29H(DA)** (`2026-10-06`)
- [x] 3. Bron RTK-correctie -> **NTRIP-dienst** (`2026-10-06`)
- [x] 4. Sockettype -> **vervallen**; modules worden handbedraad en gesoldeerd (`2026-10-09`)
- [x] 5. Uitbreidingsconnector -> **4-pins schroefklem 3,5 mm** (`2026-10-06`)
- [x] 6. I2C-pull-ups en level shifter -> **geen extra pull-ups** (breakouts hebben ze); **level shifter TXB0104** (`2026-10-06`)
- [x] 7. Wat komt op de print vs losse modules -> carrier-PCB vervallen; elektrische functies voorlopig behouden, montage nog uit te werken (`2026-10-09`)

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
- [ ] 17. UART-bedrading naar de Arduino + gemeenschappelijke ground + level shifter; bevestig of de oude schroefklem nodig blijft (`2026-10-09`)
- [x] 18. Dupont-/siliconendraad -> **in bezit** (`2026-10-06`)
- [ ] 19. Bevestigingsmethode en hardware voor de 3D-geprinte behuizing bepalen; oude PCB-M3-set niet bestellen

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
- [[specificaties]] - actuele technische afspraken; draagprint-aanpak historisch vervallen
- [[bedrading-en-behuizing]] - actuele handbedrading en montage
- [[pcb-ontwerp]] - historische PCB-werkwijze, vervallen voor het actuele ontwerp
- [[pcb-schets]] - bovenaanzicht en verbindingsschema
- [[open-vragen]] - nog te beslissen punten
- [[beslissingen]] - de keuzes van `2026-10-06`

## AI-taken

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`)
- [x] Meest accurate barometer zoeken -> **BMP390** (`2026-10-06`)
- [x] RTK-GNSS-module en GNSS-antenne zoeken -> **LC29H(DA)** + dual-band actieve antenne (`2026-10-06`)
- [x] Oude carrier-PCB-onderdeleninventaris opstellen (`2026-10-06`); draagprint en sockets vervallen `2026-10-09`, montage opnieuw bepalen
- [x] Level shifter 3,3 V <-> 5 V uitzoeken -> **TXB0104** (`2026-10-06`)
- [x] Bescherming van de voeding uitzoeken -> **PTC + TVS SMBJ10A**; geen P-MOSFET (`2026-10-06`)
