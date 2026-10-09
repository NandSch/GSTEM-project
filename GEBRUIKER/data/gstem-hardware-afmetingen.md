---
tags: [gstem, data, hardware, afmetingen, datasheet]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-09
status: verzameld uit datasheets voor behuizingsmontage
---

# Mechanische afmetingen van de onderdelen

> [!info] Waarvoor
> De **echte** bord- en behuizingsmaten van de modules, opgezocht uit datasheets en productpagina's. De maten helpen bij het ontwerpen van de 3D-geprinte behuizing en de montage. De eigen carrier-PCB en KiCad-footprints zijn vervallen; zie [bedrading-en-behuizing](bedrading-en-behuizing.md).

## Breakout-modules

| Onderdeel | Afmeting L x B x H (mm) | Opmerking | Bron |
| --- | --- | --- | --- |
| Seeed **XIAO ESP32S3** | **21 x 17,8** | 2 rijen van 7 pinnen, pitch 2,54 mm; dikte niet gepubliceerd | seeedstudio.com wiki |
| Seeed **Wio-SX1262** (module) | **11,6 x 11,0 x 2,95** | 12-pins SMT; stapelhoogte met XIAO ± **21**; IPEX/U.FL | Seeed datasheet |
| Adafruit **BNO085** (4754) | **25,6 x 22,7 x 4,6** | 2x STEMMA QT (JST-SH), 2,5 g; **geen** gepubliceerde montagegaten | adafruit.com/product/4754 |
| Adafruit **BMP581** (**6407**) | **± 25,4 x 17,8** | STEMMA QT-formaat (1,0" x 0,7"); PID 4968 is iets anders | adafruit.com/product/6407 |
| Waveshare **LC29H(DA) HAT** | **65 x 30,5** | 2x20 GPIO-header (2,54 mm), **micro-USB**, IPEX gen-1 + IPEX->SMA-kabel ± 17 cm; antenne niet op het bord | waveshare.com wiki |

> [!warning] Let op: PID-correctie
> De BMP581-breakout is Adafruit **6407**, niet 4968 (4968 = ScoutMakes FM-radio, vervallen).

## Arduino, servo's en antennes

| Onderdeel | Afmeting (mm) | Opmerking |
| --- | --- | --- |
| **Arduino Uno R3** | 68,58 x 53,34, PCB 1,6 | 4x M3-gat (3,2); USB-B links, barrel jack onder; headerhoogte ± 8,5 |
| Hobby-servo **SG90** | 23 x 12,5 x 22,5 | waslijst ± 27,8 mm; flens ± 32,5; 3-draads |
| Waveshare **L1/L5 GNSS-antenne** | **50 x 50 x 19,1** | magnetische voet, **SMA-J** (female jack), RG174 ± 3 m |
| Seeed **868/915 MHz LoRa-antenne** | lengte **195**, diameter ± 13 | SMA male, opvouwbaar; zit bij de kit |

## Losse printonderdelen

| Onderdeel | Afmeting (mm) | Voetafdruk |
| --- | --- | --- |
| SMA female bulkhead | schroefdraad 1/4-36, paneelgat **Ø 6,5** (± 6,35), paneel <= 2,8 dik | door paneel |
| IPEX/U.FL -> SMA pigtail | kabel **Ø 1,13** (mini-coax) | lengtes 5/10/15/20 cm |
| 3 mm LED (T-1) | lens Ø 3,0, hoogte 5,3, poten Ø 0,5 | pitch 2,54 |
| Weerstand 330 ohm (1/4 W) | lichaam 6,3 x Ø 2,4 | potafstand P 10,0 |
| Elco 100 uF / 16 V | can **Ø 5 x 11** | potafstand 2,0 |
| PTC 1812 | 4,6 x 3,2, hoogte 0,8-1,2 | 2 landen |
| TVS SMBJ10A (DO-214AA) | ± 5,4 x 3,6 x 2,3 | 2 gull-wing landen |
| LDO AP2112K-3.3 (SOT-23-5) | 2,8 x 1,6, hoogte 1,1 | pitch 0,95 |
| TXB0104 (TSSOP-14) | 4,9-5,1 x 4,3-4,5, hoogte <= 1,2 | pitch 0,65, leadspan 6,4 |
| TXB0108-breakout | ± 20 x 18 | Kiwi-versie (zie [bestellijst](bestellijst.md)) |
| DC barrel jack 5.5/2.1 (DC-005) | **14 x 9 x 11** | 3 THT-pennen; barrel Ø 5,5 / pin Ø 2,1 |
| Schroefklem 4P 3,5 mm (DG250-3.5-04P) | lengte **15,5**, diepte **12,0**, hoogte **11,5** | pitch 3,5; **push-in spring**, niet schroef |
| Socket 2,54 mm | dual-wipe **8,5** hoog; precisie/turned-pin **4,20** hoog | pitch 2,54, pin Ø 0,64 |

## Standaard gatmaten (altijd geldig)

- pinheader 2,54 mm: gat **1,0**, pad 1,7-1,8
- pinheader 2,0 mm (JST-GH): gat **0,8**
- M3: vrij gat **3,2**; M3 heat-set inslagmoer **4,0-4,5**
- M2,5: **2,7**; M2: **2,2**

## Bronnen

- XIAO ESP32S3: https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/
- Wio-SX1262: https://files.seeedstudio.com/products/SenseCAP/Wio_SX1262/Wio-SX1262_Module_Datasheet.pdf
- BNO085: https://www.adafruit.com/product/4754
- BMP581: https://www.adafruit.com/product/6407
- LC29H(DA) HAT: https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT
- Arduino Uno: https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf
- SG90: https://components101.com/sites/default/files/component_datasheet/MG90S-Datasheet.pdf
- GNSS-antenne: https://www.waveshare.com/gps-external-antenna-d.htm
- LoRa-antenne: https://www.seeedstudio.com/External-Antenna-868-915MHZ-2dBi-SMA-L195mm-Foldable-p-5863.html
- SMA-bulkhead (Wurth): https://www.we-online.com/components/products/datasheet/60326421110220.pdf
- AP2112: https://www.mouser.com/datasheet/2/115/AP2112-271550.pdf
- TXB0104: https://www.ti.com/lit/ds/symlink/txb0104.pdf
- DG250: https://www.degson.com/content/details_552_879687.html?lang=en
- Sockethoogtes: Wayconn FH254 (8,5) / Mill-Max 801 (4,20)

> [!question] Nog te verifieren met de schuifmaat
> Sommige maten komen uit tekeningen of secundaire listings, niet uit een tekstuele
> dimensietabel: de **Arduino-gatposities**, de **servo-flens**, de **paneelgatmaat van de
> barrel jack**, en de **exacte BMP581-afmeting**. Nameten zodra de onderdelen in huis zijn.
