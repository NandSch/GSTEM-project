---
tags: [gstem, data, planning, actieplan]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
---

# Actieplan G-STEM-P

> [!info] Wat is dit?
> De nog te ondernemen stappen voor het project, afgeleid uit [[open-vragen]],
> [[specificaties]] en [[meetmodule-voorbereiding]]. In `documenten/beheer/Planning-GSTEM.xlsx` staat dit
> als **tweede blad "Actieplan"** in een afwijkende (oranje) kleur. De **streefdatums zijn een
> voorstel** en kunnen verschoven worden.

## Voorbereiding

- [x] 09/10/2026 — Exacte 9-DoF IMU met sensorfusie kiezen — **gedaan `2026-10-06`:** Adafruit BNO055 ([[componenten]])
- [x] 09/10/2026 — Barometer en RTK-GNSS-module kiezen — **gedaan `2026-10-06`:** BMP390 en Quectel LC29H(DA) ([[componenten]])
- [x] 09/10/2026 — Bron RTK-correctie kiezen — **gedaan `2026-10-06`:** NTRIP-dienst; provider nog open
- [ ] 09/10/2026 — LoRa-frequentie/band en configuratie vastleggen (868 MHz voor België staat vast; rest van de configuratie nog open)
- [ ] 12/10/2026 — Exacte breakout-modellen en pinouts bepalen (barometer + GNSS gekozen `2026-10-06`; pinouts nog te noteren)
- [x] 12/10/2026 — Voedingsketen vastleggen — **gedaan `2026-10-06`:** 7,4 V-accu -> zekering/ompoolbeveiliging -> buck 5 V -> LDO 3,3 V ([[componenten]])
- [ ] 12/10/2026 — **AI-taak:** pinout-tabel XIAO opstellen en pin-budget controleren (IMU + barometer + GNSS + UART)
- [ ] 12/10/2026 — Level shifter en I2C-pull-ups uitzoeken (3,3 V vs 5 V)
- [x] 13/10/2026 — Socket-header of alternatief kiezen — **gedaan `2026-10-06`:** dual-wipe voor de XIAO, precisie/gefreesd voor de rest ([[pcb-methodes-kosten]])
- [x] 20/10/2026 — Uitbreidingsconnector, level shifter en bescherming van de voeding kiezen — **gedaan `2026-10-06`:** schroefklem 3,5 mm, TXB0104, PTC + TVS SMBJ10A, LDO AP2112K-3.3 ([[componenten]]) — de **P-MOSFET vervalt** (`2026-10-06`, zie [[afgevoerd]])

## Hardware

- [ ] 16/10/2026 — PCB-ontwerpgereedschap (KiCad?) en fabrikant kiezen
- [ ] 20/10/2026 — Bestelformulier afronden en componenten + PCB bestellen
- [ ] 30/10/2026 — Draagprint ontwerpen: schema, layout, afmetingen, laagcount, connectoren
- [ ] 13/11/2026 — Behuizing 3D-ontwerpen (PETG/PLA met rubberdemping)
- [ ] 27/11/2026 — PCB assembleren, modules plaatsen, voeding en power-LED doormeten

## Firmware

- [ ] 23/10/2026 — Datapakket- en CSV-formaat vastleggen: veldvolgorde en waardeschaal
- [ ] 23/10/2026 — LoRa-pakketformaat en gedrag bij pakketverlies vastleggen
- [ ] 20/11/2026 — Meetmodule: IMU, barometer en RTK-GNSS uitlezen met tijdstempel
- [ ] 27/11/2026 — LoRa-adapter: USB-doorgifte naar laptop en downlink terug
- [ ] 04/12/2026 — Sensorfusie / Kalman-filter implementeren
- [ ] 04/12/2026 — Failsafe en veiligheidsstop in de firmware (safe-state per toesteltype)
- [ ] 11/12/2026 — Geofencing-grenzen instellen en opslaan

## App

- [ ] 13/11/2026 — Code-pagina afwerken (versie B) en eigen CSV-instructies laten uploaden
- [ ] 27/11/2026 — Verbindingscontrole: USB-ontvanger en geldige datapakketten
- [ ] 04/12/2026 — Kaartscherm: 3D Google-satelliet, route en kijkrichting
- [ ] 04/12/2026 — Tabel met actuele meetwaarden (coordinaten, hoogte, snelheid, orientatie)
- [ ] 11/12/2026 — API-pagina: aan/uit, testen, adres; techniek kiezen (WebSocket/TCP/HTTP/pipe)
- [ ] 18/12/2026 — Live export en data-opslag: route opslaan en bestand openen in de website
- [ ] 18/12/2026 — Mock-up programma: Arduino via UART/CSV, drie besturingsvlakken en servo's

## Beheer, testen, documentatie en presentatie

- [ ] 09/10/2026 — Git-versiebeheer opzetten voor firmware en app
- [ ] 15/01/2027 — Testplan in vijf stappen uitvoeren (sensoren, communicatie, bereik, veiligheid)
- [ ] 30/04/2027 — Handleiding en screenshots bijwerken na herindeling code-pagina/API
- [ ] 22/05/2027 — Scriptie schrijven (3 afgedrukte exemplaren)
- [ ] 22/05/2027 — Demo voorbereiden voor de opendeurdag
- [ ] 25/05/2027 - 21/06/2027 — Proefpresentaties en juryverdediging voorbereiden
