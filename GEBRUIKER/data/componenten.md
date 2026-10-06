---
tags: [gstem, data, componenten, bom, hardware]
aangemaakt: 2026-10-06
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
| Rekenkern + LoRa | **XIAO ESP32S3 + Wio-SX1262 kit** | ESP32-S3 + SX1262 (sub-GHz, 868/915 MHz) via B2B-connector; SPI; IPEX-antenne; USB-C; LiPo-lader; ± 14 I/O | antratek |
| 9-DoF IMU | **Adafruit BNO055-breakout** | I2C 0x28/0x29, 3,3 V-regelaar + level shifting, 20x27x4 mm, montagegaten 20x12 mm | antratek |

> [!warning] Gevolg van de XIAO-kit
> ESP32 en LoRa zijn nu **één module**; op de draagprint is dat een enkele footprint. De XIAO heeft
> een **ingebouwde LiPo-lader**, dus de geplande 7,4 V -> buck -> LDO-keten is mogelijk niet nodig.
> Pin-budget: controleer of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART naar de Arduino.

## Nog te kiezen

| Functie | Opties / kandidaten | Opmerking |
| --- | --- | --- |
| Barometer | Adafruit BMP581, BME280 | Nog geen keuze. |
| RTK-GNSS | u-blox ZED-F9P, ArduSimple, SparkFun RTK | Seeed L76K is GNSS maar **geen RTK**; 0,5 m vereist RTK. |
| RTK-correctie | eigen basisstation of NTRIP-dienst | Bepaalt extra hardware. |
| Voedingsroute | **7,4 V-accu + zekering/ompoolbeveiliging + buck 5 V + LDO 3,3 V** (gekozen) | XIAO op 5 V-pin; ingebouwde LiPo-lader niet gebruikt. |
| Aan/uit-schakelaar | nog te kiezen | Zie onder "Nog te noteren". |
| LoRa-ontvanger laptop | tweede XIAO-kit of USB-LoRa-dongle | De USB-stick-ontvanger uit de specs is nog geen hardware. |
| Sockettype | precisie/gefreesd, dual-wipe, direct solderen | Zie [[pcb-methodes-kosten]]. |
| Uitbreidingsconnector | exacte stekker | Concept is UART via TX/RX. |
| Arduino (mock-up) | Uno, Nano, ... | Nog niet gekozen. |
| Servo's (mock-up) | 3 stuks | Type + voeding nog niet gekozen. |

## Nog te noteren (ontbrak in de lijst)

**Antennes / RF**
- GNSS-antenne (actieve antenne met LNA + ground plane).
- LoRa IPEX -> SMA-pigtail + SMA-bulkhead voor montage door de behuizing.
- Controleren of de LoRa-antenne bij de kit zit.

**Voeding** (route gekozen: 7,4 V + buck)
- 7,4 V-accu met beschermcircuit + connector en kabel.
- Zekering, ompoolbeveiliging, TVS.
- Buck-converter 5 V en LDO 3,3 V.
- Aan/uit-schakelaar of knop.

**Verbindingen**
- USB-C datakabel (programmeren).
- UART-draden meettoestel <-> Arduino + gemeenschappelijke ground + level shifter.
- Dupont-/siliconendraad voor interne bekabeling.

**Montage / behuizing**
- M3-schroeven, moeren, afstandsbusjes (standoffs), nylon spacers.

**Laptop-/ontvangerzijde**
- USB-kabel; hardware van de USB-stick-ontvanger.

**Mock-up (vliegtuigje)**
- Servo-voeding / BEC (los van de logica).
- Stuurstangen, scharnieren, roerbladen, rompmateriaal.

**Gereedschap / verbruik (vaak vergeten)**
- Digitale schuifmaat (voor footprint-maten), soldeerbout/tin/flux, multimeter, USB-serieel adapter.

## Gerelateerd

- [[specificaties]] - draagprint-aanpak en gebruikersspecificaties
- [[pcb-ontwerp]] - footprints en gatmaten
- [[pcb-schets]] - bovenaanzicht en verbindingsschema
- [[open-vragen]] - nog te beslissen punten

## AI-taken

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`)
