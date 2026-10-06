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

Het SVG opent in elke browser; het markdown-bestand toont de verbindingsschema's en de
voedingsboom. Het PNG is een gerenderde versie van het SVG.

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
