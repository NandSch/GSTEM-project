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
> Prijzen zijn **incl. btw** en onder voorbehoud (`2026-10-06`). De Excel-versie staat in
> `documenten/Bestellijst-GSTEM.xlsx` (bron: `documenten/build-bestellijst.py`).

## Legende (tags)

| Tag | Betekenis |
| --- | --- |
| `kiwi` | Aankooplink gevonden op Kiwi Electronics |
| `antratek` | Aankooplink gevonden op antratek.be (goedkoper of reserve) |
| `al-in-bezit` | Heeft de gebruiker al; niet aankopen |
| `geen-link` | Niet bij Kiwi of antratek; aparte componentenwinkel nodig |
| `niet-nodig` | Bewust niet voorzien |
| `aisler` | Draagprint gefabriceerd bij AISLER |

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
| `geen-link` | RTK-GNSS-module | Quectel LC29H(DA) | 1 | - | Niet bij Kiwi of antratek |

> [!success] Beter én goedkoper dan voorheen
> De **BNO085** (€ 32,05) is goedkoper **en nieuwer** dan de BNO055 op antratek (€ 36,24).
> De **BMP581** (€ 10,88) is een **nauwkeuriger** barometer dan de BME280 en past bij de
> gebruikersvoorkeur om een beter model te nemen; de BMP390L is bij Kiwi **uit voorraad**.

> [!warning] RTK-module nergens te koop
> De gekozen **Quectel LC29H(DA)** staat bij **Kiwi noch antratek**. Kiwi heeft enkel de
> **niet-RTK L76K** (€ 15,11). Antratek-alternatieven zijn veel duurder: LG290P (€ 217,74),
> ZED-F9P (€ 302,44).

## Antennes en RF

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `kiwi` | GNSS-antenne (actief, SMA) | GPS Antenne – Externe Actieve – 3-5V 28dB 5 m SMA | 1 | € 16,93 | https://www.kiwi-electronics.com/nl/gps-antenne-externe-actieve-antenne-3-5v-28db-5-meter-sma-620 |
| `antratek` | LoRa IPEX/U.FL -> SMA pigtail | Interface Cable SMA to U.FL (150 mm), SparkFun WRL-18568 | 1 | € 3,57 | https://www.antratek.be/u-fl-sma-150mm-cable |
| `al-in-bezit` | LoRa-antenne | Inbegrepen bij de XIAO-kit | 1 | - | - |

> [!tip] Goedkoopste passende GNSS-antenne
> De Kiwi-antenne (€ 16,93) is de goedkoopste **actieve SMA**-antenne; **enkelbandig (L1)**,
> multi-constellatie. Voor volledige dual-band RTK is er de optie hieronder.

> [!example]- Duurdere, nauwkeurigere optie (L1/L5)
> **GNSS L1/L5 Multi-Band High Precision Antenna - 5m (SMA)** - € 120,94 -
> https://www.antratek.be/gnss-l1-l5-multi-band-high-precision-antenna-5m-sma.

> [!note] Pigtail
> Goedkoper op antratek (€ 3,57) dan Kiwi (€ 4,22) → op antratek laten staan.

## Voeding

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Accu (7,4 V) | 2S LiPo met connector en kabel | 1 | - | - |
| `al-in-bezit` | Voedingsaansluiting | DC Barrel Jack Adapter - Female | 1 | - | - |
| `al-in-bezit` | Buck-converter 5 V | Heeft de gebruiker | 1 | - | - |
| `geen-link` | Bescherming voeding | 2 A PTC + P-MOSFET DMG2301L + TVS SMBJ10A (op de print) | 1 set | - | Niet bij Kiwi of antratek |
| `geen-link` | LDO 3,3 V | AP2112K-3.3 (of AMS1117-3.3) (op de print) | 1 | - | Niet bij Kiwi of antratek |
| `niet-nodig` | Aan/uit-schakelaar | Geen; toestel start bij voeding | - | - | - |

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
| `geen-link` | Schroefklem 4-pins 3,5 mm | KF128/KF301 | 1 | - | Niet bij Kiwi (alleen 3-weg) of antratek |
| `geen-link` | Sockets | Dual-wipe (ESP32) + precisie voor de rest | set | - | Niet bij Kiwi of antratek |
| `kiwi` | Power-LED + serieweerstand | 3 mm LED rood (10-pack) + weerstand 330 Ω (10-pack) | 1 | € 2,16 | https://www.kiwi-electronics.com/nl/3mm-led-diffuus-rood-10-pack-3085 |
| `kiwi` | Ontkoppelcondensatoren | Keramische condensator kit (15 soorten, 450 st.) | 1 | € 10,27 | https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492 |
| `kiwi` | Bulk-elco | 100 µF / 16 V op de 5 V-ingang | 1 | € 0,59 | https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440 |
| `niet-nodig` | I2C-pull-ups op de print | Breakouts hebben ze al; 2 reserve-footprints | 2 | - | - |
| `geen-link` | Montage | M3-schroeven, moeren, standoffs, nylon spacers | set | - | Niet bij Kiwi of antratek |

> [!warning] Gekozen level shifter
> De **TXB0108** (€ 8,70) past bij de gekozen **TXB-serie** en is leverbaar bij Kiwi.
> Het antratek-alternatief (BSS138-converter, € 4,78) is goedkoper maar een ander type.

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
| **Kiwi Electronics** | BNO085, BMP581, GNSS-antenne, TXB0108, LED + weerstand, condensatorkit, bulk-elco | **€ 81,58** |
| **antratek.be** | 2× XIAO-kit, U.FL→SMA pigtail | **€ 33,83** |
| **Totaal te bestellen** | Kiwi + antratek | **€ 115,41** |

> [!info] Buiten deze bedragen
> De `geen-link`-onderdelen (LC29H, bescherming, LDO, schroefklem, sockets, montage) komen bij
> geen van beide winkels en zijn dus niet in het totaal opgenomen. De RTK-module is hier het
> grootste knelpunt.

## Open acties

- [ ] **Tweede winkel** zoeken die de `geen-link`-onderdelen levert: RTK-module (LC29H of alternatief), discrete voeding (PTC + DMG2301L + SMBJ10A + AP2112K), 4-pins 3,5 mm schroefklem, sockets en M3-montage.
- [ ] LoRa: wachten op voorraad Wio-SX1262 bij Kiwi, of de antratek-kit nemen?
- [ ] GNSS-antenne: Kiwi actieve L1 (€ 16,93) of dual-band L1/L5 (€ 120,94) voor volledige RTK?
- [ ] Barrel-connector: PCB-montage of adapter met schroefklem bevestigen.
- [ ] Voorraad/prijzen bij Kiwi en antratek controleren vóór het bestellen.

## Gerelateerd

- [[componenten]] - volledige BOM en keuzes
- [[specificaties]] - technische afspraken
- [[pcb-ontwerp]] - footprints en gatmaten
- [[links]] - bronnen
