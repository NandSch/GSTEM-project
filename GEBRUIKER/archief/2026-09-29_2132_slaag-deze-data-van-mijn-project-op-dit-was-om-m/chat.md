---
tags: [gstem, chatlog]
sessie: "01a0eea7-6970-7424-afe7-281513619d55"
gestart: 2026-09-29T19:32:24.154Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a0eea7-6970-7424-afe7-281513619d55` · gestart 2026-09-29_2132
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## 🧑 Gebruiker · 21:34

> [!quote] Verbatim
> Slaag deze data van mijn project op, dit was om mijn denkwijze en project voorbereiding verder te zetten, het zijn wel echt niet echt specificaties. maar je neemt het op zoals hoe jij wilt: 
> Specificaties voor Positie- en beweging meetmodule met LoRa integratie.
> 
> Hardware:
> Eigen PCB waarop breakout modules geplaatst en vervangen kunnen worden.
> PCB-sporen verbinden de modules voor voeding en datacommunicatie.
> De PCB zal in de hoeken bevestigings punten hebben waaraan dat hij gemonteerd kan worden aan de dempings behuizing.
> ESP32-S3-breakoutbord met LoRa-radio en antenne als centrale microcontroller in de meetmodule.
> De ESP zal waarschijnlijk warm worden onder gebruik dus is het nodig voor een heatsink.
> 9-DoF IMU met sensorfusie voor absolute oriëntatie.
> Barometer voor luchtdruk en geschatte hoogte.
> RTK-GNSS-module met antenne voor positiebepaling.
> Tweede ESP met LoRa als zend- en ontvangst adapter bij de laptop. verbinding met de laptop via USB.
> Batterij, met correcte voeding specificaties. Bv, 7.4v 2A
> De pcb zelf heeft een barrel-connector voor stroomvoeding.
> Spanningsregelaar om het voltage van de batterij om te zetten naar een voltage die bruikbaar is voor de pcb.
> Zelf ontworpen, 3D-geprinte behuizing met demping om het effect van schokken en trillingen te onderzoeken.
> De PCB van de meetmodule krijgt overige pinnen en grounds. Zo kan men het besturingssysteem van het toestel verbinden aan de module. (Eg, aan het besturingssysteem van het mockup-vliegtuigje.)
> Optionele uitbreiding: tweede microcontroller en twee servo’s op een stilstaande vliegtuig mock-up.
> Mock-up gemaakt uit één kant van een vliegtuig, alles wordt gecontroleerd door servos.
> Software:
> De IC’s op de meetmodule leest IMU, barometer en RTK-GNSS uit, voegt de gegevens samen in datapakketten en verzendt die via LoRa. (op het PCB-bordje zelf)
> Op de LoRa-adapter geeft die de metingen via USB door aan de laptop en verstuurt eventuele commando’s terug via dezelfde LoRa.
> Eén app met de nodige programma bibliotheken en onderdelen.
> Startscherm van de app vraagt de gebruiker eerst de LoRa-ontvanger via USB aan te sluiten.
> App controleert eerst de USB-verbinding met de ontvanger en daarna of geldige datapakketten van de meetmodule via LoRa binnenkomen. Beide worden apart getoond.
> Na een geslaagde verbinding opent het hoofdscherm met de knoppen Kaart en Programmering.
> Rechts toont het hoofdscherm de actuele meetwaarden, waaronder coördinaten, hoogte, snelheid en oriëntatie.
> Links toont het hoofdscherm een interactieve kaart met de positie van de meetmodule, een richtingspijl en een rode lijn voor de afgelegde route.
> De modus Kaart toont de kaart, route en actuele meetwaarden.
> De modus Programmering laat de gebruiker eigen verwerkingscode of uitbreidingen toevoegen die meetdata omzetten in acties.
> De app kan live meetgegevens aan een extern programma.
> Sensorfusie met een algoritme zoals Kalman filter.
> Errorhandling wanneer gps verbinding verbreekt of sensoren die uitvallen.
> Grenzen binnen de software die waarschuwen of beperken buiten een bepaald gebied. (geofencing)
> Berekende stuurcommando’s gaan vanuit de app via de USB-adapter en LoRa terug naar de meetmodule.
> Bij verlies van verbinding of ongeldige commando’s stopt de voertuigbesturing veilig.
> De app bewaart meetgegevens en de afgelegde route voor latere weergave.
> Alle versies van de software voor de ESP’s en de app worden opgeslagen in een git project. Dit zorgt ervoor dat ik altijd kan teruggaan naar een oude versie.
>  Uitgebreide testen over hoe goed alle sensoren en communicatie werken.
> Optionele uitbreiding: een apart programma in de app berekent acties voor een stilstaande vliegtuig mock

## 🤖 AI · 21:35

Ik sla de projectvoorbereiding op als een apart onderwerp met verwijzingen in het archief

---

## 🤖 AI · 21:35

Opgeslagen in het archief:

> [!info] Opgeslagen: voorbereiding/denkwijze
> - **`GEBRUIKER/data/meetmodule-voorbereiding.md`** — het volledige overzicht van hardware (PCB, ESP32-S3, IMU, barometer, RTK-GNSS, LoRa, behuizing), software (firmware, adapter, laptopapp met kaart/programmeermodus, sensorfusie, geofencing, veiligheidsstop) en de optionele mock-up-uitbreiding. Gemarkeerd als *voorbereiding/denkwijze*, geen harde specs.
> - **`GEBRUIKER/onderwerpen.md`** — nieuw topic `[[meetmodule-voorbereiding]]` toegevoegd.
> - **`GEBRUIKER/data/open-vragen.md`** — uitgebreid met 13 nieuwe concrete open vragen die uit deze voorbereiding volgen (exacte componentkeuzes, LoRa-configuratie, pakketformaat, batterijspecificatie, PCB-afmetingen, Kalman-variant, veiligheidsstop-gedrag, mock-up details, enz.).
> - **`GEBRUIKER/data/specificaties.md`** — verwijzing toegevoegd naar de voorbereiding met status *voorbereiding / denkwijze*, zodat het gescheiden blijft van vastgelegde specificaties.

Als je later delen van deze voorbereiding omzet in concrete beslissingen of specificaties, verplaatsen we die naar `data/beslissingen.md` en `data/specificaties.md` met status *vastgelegd*.

---
