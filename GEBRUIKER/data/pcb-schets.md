---
tags: [gstem, data, pcb, hardware, schets]
aangemaakt: 2026-10-06
status: schets
---

# PCB-schets draagprint

> [!info] Doel
> Visuele schets van hoe de zelfgemaakte draagprint eruitziet en hoe alles aangesloten is.
> Hoort bij de draagprint-aanpak in [[specificaties]] (`2026-10-06`).

## Bestanden

| Rol | Pad |
| --- | --- |
| Schets (markdown + Mermaid) | `documenten/PCB-schets.md` |
| Bovenaanzicht (SVG, vector) | `documenten/PCB-schets-draagprint.svg` |
| Bovenaanzicht (PNG, afbeelding) | `documenten/PCB-schets-draagprint.png` |
| Eindbeeld eind-PCB (PNG) | `documenten/PCB-eindbeeld.png` |
| Eindbeeld (bouwsript) | `documenten/build-pcb-eindbeeld.py` |
| Verbindingsschema (draw.io) | `documenten/Verbindingsschema-GSTEM.drawio` |
| Verbindingsschema (PNG) | `documenten/Verbindingsschema-GSTEM.png` |
| Verbindingsschema (bouwsript) | `documenten/build-verbindingsschema.py` |

Het SVG opent in elke browser; het markdown-bestand toont de verbindingsschema's en de
voedingsboom. Het PNG is een gerenderde versie van het SVG.

> [!tip] Nieuw: volledig verbindingsschema (`2026-10-06`)
> Naast de schets is er nu een **compleet verbindingsschema** (draw.io + PNG) met de hele keten:
> accu/barrel -> PTC + TVS -> buck 5 V -> bulk-elco + power-LED -> LDO 3,3 V, de **XIAO ESP32S3 +
> Wio-SX1262**, de sensoren (BNO085 I2C, BMP581 I2C, LC29H(DA) UART), de **TXB0104** level shifter,
> de **4-pins uitbreidingsconnector**, de **Arduino Uno + 3 servo's + servo-buck** en de
> **LoRa-adapter + laptopapplicatie**. Zie [[verbindingsschema]] en
> `documenten/Verbindingsschema-GSTEM.{drawio,png}`; bouwen via `documenten/build-verbindingsschema.py`.

## Eindbeeld met Arduino (`2026-10-06`, `documenten/PCB-eindbeeld.png`)

> [!info] Wat het toont
> Detailbeeld van de **eindtoestand**: de draagprint met de **definitief gekozen** breakouts
> (XIAO ESP32S3 + Wio-SX1262, BNO085, BMP581, LC29H(DA)), de losse printcomponenten
> (PTC + SMBJ10A, buck, AP2112K, TXB0104, schroefklem, LED; de P-MOSFET vervalt `2026-10-06`), de **Arduino Uno**
> ernaast met de servo's, en alle **verbindingen** (5 V / 3,3 V / GND-bus, I2C, GNSS-UART,
> Arduino-UART via de level shifter, LoRa-RF en de 4-aderige kabel).

- **Bron/opvolger van:** de schets van `2026-10-06` hierboven, nu met de definitieve
  bestellijst-onderdelen (BNO085 i.p.v. BNO055, BMP581 i.p.v. BMP390).
- **Kleuren:** rood = VBAT, oranje = 5 V, geel = 3,3 V, grijs = GND, blauw = I2C,
  groen = GNSS-UART, teal = Arduino-UART via TXB0104, roze = LoRa-RF/keep-out.
- **Let op:** schematisch en niet op schaal; de **pinout is een voorstel** (AI-taak, zie
  [[open-vragen]]). Kruising zonder stip = geen verbinding.

## Bestanden van het eindbeeld

- `documenten/PCB-eindbeeld.png` — het eindbeeld.
- `documenten/build-pcb-eindbeeld.py` — bouwsript (PIL).

## In één oogopslag

- **Draagprint (carrier)** met daarop **breakout-modules op socket-headers**: ESP32-S3, LoRa,
  9-DoF IMU, barometer, RTK-GNSS.
- **Voeding:** accu 7,4 V of barrel → zekering/ompoolbeveiliging → buck 5 V → LDO 3,3 V;
  **power-LED** op de geregelde rail; decoupling per rail.
- **Datapaden:** I2C (IMU + barometer, met pull-ups), UART (GNSS en uitbreidingsconnector),
  LoRa-aansturing (SPI/control), CSV-commando's naar de Arduino/voertuigcontroller.
- **Layout:** 2-laags met ground plane; antenne-keep-out voor LoRa en GNSS; sensoren weg van
  warmte en antenne; 4× M3-bevestigingsgat in de hoeken.

## Gerelateerd

- [[specificaties]] — draagprint-aanpak en elektrische basis
- [[meetmodule-voorbereiding]] — hardwarecontext
- [[open-vragen]] — exacte breakouts, pinouts, voeding en gereedschap
