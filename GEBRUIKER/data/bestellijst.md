---
tags: [gstem, data, bestellijst, bom, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: werklijst
---

# Bestellijst meettoestel (aan te kopen)

> [!info] Werkwijze
> Alle onderdelen uit [[componenten]]. Eerst gezocht op **www.antratek.be**; wat daar niet staat,
> is **niet elders** gezocht (afspraak gebruiker `2026-10-06`). Prijzen zijn **incl. btw** en
> onder voorbehoud (anratek `2026-10-06`). De Excel-versie staat in
> `documenten/Bestellijst-GSTEM.xlsx`.

## Legende (tags)

| Tag | Betekenis |
| --- | --- |
| `antratek` | Aankooplink gevonden op antratek.be |
| `al-in-bezit` | Heeft de gebruiker al; niet aankopen |
| `geen-link` | Niet gevonden op antratek.be, dus geen aankooplink |
| `niet-nodig` | Bewust niet voorzien |

## Rekenkern en communicatie

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `antratek` | Rekenkern + LoRa (toestel + ontvanger) | XIAO ESP32S3 & Wio-SX1262 Kit for Meshtastic & LoRa | 2 | € 15,13 | https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora |

> [!note] Antenne inbegrepen
> De LoRa-antenne zit bij de kit; er is geen losse LoRa-antenne nodig (zie `al-in-bezit`).

## Sensoren

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `antratek` | 9-DoF IMU | 9-DOF Absolute Orientation IMU Fusion Breakout - BNO055 - STEMMA QT/Qwiic | 1 | € 36,24 | https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055 |
| `antratek` | Barometer | Atmospheric Sensor Breakout - BME280 (Qwiic) | 1 | € 19,97 | https://www.antratek.be/atmospheric-sensor-breakout-bme280 |
| `geen-link` | RTK-GNSS-module | Quectel LC29H(DA) | 1 | - | Niet op antratek.be |

> [!warning] Barometer: goedkopere keuze
> De gekozen **Adafruit BMP390** staat **niet op antratek**. De **BME280** (€ 19,97) is op antratek
> wel leverbaar en goedkoper, maar **minder nauwkeurig** (druk ±1 hPa i.p.v. ±0,03 hPa). Voor een
> precisiehoogtemeter is de BMP390 beter; die moet dan elders besteld worden. Standaard genomen:
> **BME280** (goedkoopst en direct leverbaar).

> [!warning] RTK-module niet op antratek
> De gekozen **Quectel LC29H(DA)** heeft antratek niet. De goedkoopste RTK-alternatieven daar zijn
> veel duurder (zie hieronder), dus die zijn **niet in het totaal** opgenomen.

> [!example]- Alternatieven op antratek (niet gekozen)
> - Quadband GNSS RTK Breakout - LG290P (Qwiic) - € 217,74 - https://www.antratek.be/quadband-gnss-rtk-breakout-lg290p-qwiic
> - GPS-RTK-SMA Board - ZED-F9P (Qwiic) - € 302,44 - https://www.antratek.be/gps-rtk-sma-board-zed-f9p-qwiic

## Antennes en RF

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `antratek` | GNSS-antenne (actief, SMA) | GPS/GNSS Magnetic Mount Antenna SMA - 3m, SparkFun GPS-14986 | 1 | € 19,30 | https://www.antratek.be/gps-gnss-magnetic-mount-antenna-sma-3m |
| `antratek` | LoRa IPEX/U.FL -> SMA pigtail | Interface Cable SMA to U.FL (150 mm), SparkFun WRL-18568 | 1 | € 3,57 | https://www.antratek.be/u-fl-sma-150mm-cable |
| `al-in-bezit` | LoRa-antenne | Inbegrepen bij de XIAO-kit | 1 | - | - |

> [!tip] Goedkoopste passende GNSS-antenne
> De **GPS/GNSS Magnetic Mount Antenna SMA - 3m** (€ 19,30) is de goedkoopste **actieve** antenne met
> **SMA** op antratek; ze is multi-constellatie maar **enkelbandig (L1)**. Daarmee is RTK mogelijk,
> maar minder robuust dan met een dual-band antenne.

> [!example]- Duurdere, nauwkeurigere optie (L1/L5)
> **GNSS L1/L5 Multi-Band High Precision Antenna - 5m (SMA)** - € 120,94 -
> https://www.antratek.be/gnss-l1-l5-multi-band-high-precision-antenna-5m-sma.
> Nodig voor de volledige dual-band RTK-prestatie van de LC29H(DA); ca. € 101,64 duurder.
> Er is ook een **Molex Flexible GNSS Antenna - U.FL** voor € 8,41
> (https://www.antratek.be/molex-flexible-gnss-antenna-u-fl-adhesive), maar dat is een klein
> L1-printantennetje zonder SMA-kabel — minder geschikt voor montage aan het vliegtuigje.

## Voeding

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Accu (7,4 V) | 2S LiPo met connector en kabel (heeft de gebruiker) | 1 | - | - |
| `al-in-bezit` | Voedingsaansluiting | DC Barrel Jack Adapter - Female (heeft de gebruiker) | 1 | - | - |
| `al-in-bezit` | Buck-converter 5 V | Heeft de gebruiker | 1 | - | - |
| `geen-link` | Bescherming voeding | 2 A PTC + P-MOSFET DMG2301L + TVS SMBJ10A | 1 set | - | Niet op antratek.be |
| `geen-link` | LDO 3,3 V | AP2112K-3.3 (of AMS1117-3.3) | 1 | - | Niet op antratek.be |
| `niet-nodig` | Aan/uit-schakelaar | Geen; toestel start bij voeding | - | - | - |

> [!note] Barrel-adapter
> De gevonden `DC Barrel Jack Adapter - Female` is een **adapter met schroefklem**, niet rechtstreeks
> PCB-montage. Voor de draagprint is een PCB-barreljack (of een draad naar de klem) nodig.

## Print en verbindingen

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `antratek` | Level shifter 3,3 V <-> 5 V | Logic Level Converter Bi-Directional, SparkFun BOB-12009 (alternatief voor TXB0104) | 1 | € 4,78 | https://www.antratek.be/logic-level-converter-bi-directional-bob-12009 |
| `geen-link` | Schroefklem 4-pins 3,5 mm | KF128/KF301 | 1 | - | Niet op antratek.be |
| `geen-link` | Sockets | Dual-wipe (ESP32) + precisie voor de rest | set | - | Niet op antratek.be |
| `geen-link` | Power-LED + serieweerstand | Status voeding | 1 | - | Niet op antratek.be |
| `geen-link` | Ontkoppelcondensatoren | 100 nF + 10 uF per modulevoedingspin | set | - | Niet op antratek.be |
| `geen-link` | Bulk-elco | 100 uF / 16 V op de 5 V-ingang | 1 | - | Niet op antratek.be |
| `niet-nodig` | I2C-pull-ups op de print | Breakouts hebben ze al; 2 reserve-footprints | 2 | - | - |
| `geen-link` | Montage | M3-schroeven, moeren, standoffs, nylon spacers | set | - | Niet op antratek.be |

> [!warning] Gekozen level shifter wijkt af
> De gekozen **TXB0104** staat niet op antratek. Het gevonden **Logic Level Converter
> Bi-Directional** (BSS138, 4 kanaals) is een bruikbaar alternatief voor de UART naar de Arduino.
> Nog te bevestigen.

## Kabels en verbruik (in bezit)

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | USB-C datakabel | Eigen kabel (flashen/programmeren) | 1 | - | - |
| `al-in-bezit` | Dupont-/siliconendraad | Heeft de gebruiker | - | - | - |
| `al-in-bezit` | USB A-kabel LoRa-ontvanger | USB-A -> USB-C voor de XIAO (heeft de gebruiker) | 1 | - | - |
| `al-in-bezit` | Gereedschap | Schuifmaat, soldeerbout, tin, flux, multimeter, USB-serieel adapter | - | - | - |

## Mock-up (vliegtuigje)

| Tag | Component | Onderdeel | Aantal | Prijs/st | Link |
| --- | --- | --- | --- | --- | --- |
| `al-in-bezit` | Arduino | Heeft de gebruiker thuis (Arduino Uno) | 1 | - | - |
| `al-in-bezit` | Servo's | Bestaande voorraad (> 3) | 3+ | - | - |
| `al-in-bezit` | Servo-voeding | Aparte buck-converter | 1 | - | - |
| `al-in-bezit` | Romp en roeren | Eigen 3D-print | 1 | - | - |

## Totalen

| Scenario | Te bestellen bij antratek | Bedrag (incl. btw) |
| --- | --- | --- |
| **Goedkoopste complete set (standaard)** | 2x XIAO-kit, BNO055, BME280, magneetantenne, U.FL-SMA, level converter | **€ 114,12** |
| Met L1/L5-antenne i.p.v. magneetantenne | Idem, maar dual-band L1/L5-antenne (€ 120,94) | **€ 215,76** |
| Zonder barometer (BMP390 niet leverbaar bij antratek) | Idem als standaard, maar zonder BME280 | **€ 94,15** |

> [!info] Buiten deze bedragen
> De `geen-link`-onderdelen (LC29H, bescherming, LDO, schroefklem, sockets, montage) komen niet bij
> antratek en zijn dus niet in het totaal opgenomen. Voor de RTK-module is het goedkoopste
> antratek-alternatief (LG290P) € 217,74 en zou het totaal dan naar ca. € 331,86 stijgen; daarom
> staat de LC29H als `geen-link` (elders te regelen).

## Open acties

- [ ] `geen-link`-onderdelen elders of via een andere weg regelen (LC29H(DA), 2S LiPo, PTC + DMG2301L + SMBJ10A, AP2112K, schroefklem, sockets, M3-montage).
- [ ] Barometer: BME280 (goedkoop, leverbaar) of toch de nauwkeurigere BMP390 elders nemen?
- [ ] GNSS-antenne: magneetantenne (€ 19,30, L1) of dual-band L1/L5 (€ 120,94) voor volledige RTK?
- [ ] Level shifter: TXB0104 of het gevonden BSS138-alternatief kiezen.
- [ ] Barrel-connector: PCB-montage of adapter met schroefklem bevestigen.
- [ ] Voorraad/prijzen en beschikbaarheid bij antratek controleren voor het bestellen.

## Gerelateerd

- [[componenten]] - volledige BOM en keuzes
- [[specificaties]] - technische afspraken
- [[pcb-ontwerp]] - footprints en gatmaten
- [[links]] - bronnen
