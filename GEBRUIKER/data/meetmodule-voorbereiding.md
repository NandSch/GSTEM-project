---
tags: [gstem, data, voorbereiding, meetmodule, lora]
aangemaakt: 2026-09-29
status: denkwijze / voorbereiding
---

# Positie- en beweging meetmodule met LoRa — projectvoorbereiding

> [!info] Dit is een denk- en voorbereidingsdocument.
> Nog geen vastgelegde specificaties of beslissingen. De onderdelen hieronder beschrijven de beoogde richting en de componenten die worden overwogen.

## Hardware-overzicht

### Centrale eenheid — meetmodule (op eigen PCB)
- **Eigen PCB** waarop breakout-modules geplaatst en vervangen kunnen worden.
- PCB-sporen verzorgen voeding en datacommunicatie tussen modules.
- Bevestigingspunten in de hoeken voor montage in de dempingsbehuizing.
- Overige pinnen en grounds beschikbaar om het besturingssysteem van het toestel te verbinden (bijv. mockup-vliegtuigje).
- **Barrel-connector** op de PCB voor directe stroomvoeding.
- **Spanningsregelaar** om batterijvoltage om te zetten naar bruikbaar PCB-voltage.
- **Batterij**: bijvoorbeeld 7.4 V 2 A (voedingsspecificatie nog te bepalen).

### Microcontroller en radio
- **ESP32-S3-breakoutbord** met LoRa-radio en antenne als centrale microcontroller.
- Verwachte warmte-ontwikkeling: heatsink nodig.
- **Tweede ESP met LoRa** als zend- en ontvangstadapter bij de laptop, verbonden via USB.

### Sensoren
- **9-DoF IMU** met sensorfusie voor absolute oriëntatie.
- **Barometer** voor luchtdruk en geschatte hoogte.
- **RTK-GNSS-module** met antenne voor positiebepaling.

### Mechanisch
- **Zelf ontworpen, 3D-geprinte behuizing** met demping om schokken en trillingen te onderzoeken.

### Optionele uitbreiding — stilstaande mock-up
- Tweede microcontroller en twee servo’s op een stilstaande vliegtuigmock-up.
- Mock-up bestaat uit één kant van een vliegtuig; alles wordt aangestuurd door servo’s.
- Apart programma in de app berekent acties voor de mock-up.

## Software-overzicht

### Firmware meetmodule (ESP op PCB)
- Leest IMU, barometer en RTK-GNSS uit.
- Voegt gegevens samen in datapakketten.
- Verzendt pakketten via LoRa.

### LoRa-adapter (ESP bij laptop)
- Geeft metingen via USB door aan de laptop.
- Verstuurt eventuele commando’s terug via dezelfde LoRa-verbinding.

### Laptopapp — structuur en schermen
- **Eén app** met benodigde bibliotheken en onderdelen.
- **Startscherm**: vraagt de gebruiker om de LoRa-ontvanger via USB aan te sluiten.
- **Verbindingscontrole**:
  - Controleert USB-verbinding met de ontvanger.
  - Controleert of geldige datapakketten van de meetmodule via LoRa binnenkomen.
  - Beide statussen worden apart getoond.
- **Hoofdscherm** (na geslaagde verbinding):
  - Rechts: actuele meetwaarden — coördinaten, hoogte, snelheid, oriëntatie.
  - Links: interactieve kaart met positie van de meetmodule, richtingspijl en rode lijn voor de afgelegde route.
- **Modus Kaart**: toont kaart, route en actuele meetwaarden.
- **Modus Programmering**: gebruiker kan eigen verwerkingscode of uitbreidingen toevoegen die meetdata omzetten in acties.
- **Live export**: app kan live meetgegevens doorgeven aan een extern programma.
- **Data-opslag**: meetgegevens en afgelegde route worden bewaard voor latere weergave.

### Besturing en veiligheid
- **Sensorfusie** met algoritme zoals Kalman-filter.
- **Errorhandling** bij verbroken GPS-verbinding of uitvallende sensoren.
- **Geofencing**: grenzen binnen de software die waarschuwen of beperken buiten een bepaald gebied.
- **Berekende stuurcommando’s** gaan vanuit de app via de USB-adapter en LoRa terug naar de meetmodule.
- **Veiligheidsstop**: bij verlies van verbinding of ongeldige commando’s stopt de voertuigbesturing veilig.

### Versiebeheer
- Alle softwareversies voor de ESP’s en de app worden opgeslagen in een git-project, zodat altijd teruggekeerd kan worden naar een oudere versie.

### Testen
- Uitgebreide testen over hoe goed alle sensoren en communicatie werken.

## 2026-10-05 — Ontwerptekst "Ontwerp voor Positie- en beweging meetmodule met LoRa integratie"
- **Bron:** Google Doc, gedeeld met iedereen — https://docs.google.com/document/d/1wbb8LAjXiUpZQBpxv1NKQZ8YBhb32TtkiDcpUfl5o0M/edit (zie [[links]]).
- **Wat het is:** een doorlopende-tekst-ontwerpbeschrijving van hetzelfde systeem, in twee delen — **Hardware Specificaties** en **Software Specificaties**.
- **Kern:** eigen PCB met vervangbare breakout-modules, bevestigingspunten in de hoeken, ESP32-S3 + LoRa + antenne + heatsink, 9-DoF IMU, barometer, RTK-GNSS met antenne; voeding via externe batterij (bijv. 7,4 V) of barrel-connector met spanningsregelaar; extra pinnen en grounds naar het besturingssysteem van een mockup-vliegtuigje; zelf ontworpen 3D-geprinte dempende behuizing; tweede ESP met LoRa als USB-adapter bij de laptop. Software: continu uitlezen van IMU, barometer en RTK-GNSS, samenvoegen tot datapakketten, sensorfusie met een Kalman-filter, verzending via LoRa, USB-doorgifte naar de laptop, errorhandling bij wegvallende GPS of sensoren, en grenzen die waarschuwen buiten een bepaald gebied.
- **Verhouding tot dit document:** de ontwerptekst is de compacte, formele variant. Hij noemt **niet**: de schermopbouw van de laptopapp, de programmeermodus, live export en data-opslag, git-versiebeheer, de testaanpak en de optionele mock-up-uitbreiding. Die staan alleen hier.
- **Gevolg:** geen nieuwe beslissingen of open vragen; de tekst bevestigt de bestaande denkrichting. Zie [[specificaties]] voor de vastlegging.

## 2026-10-05 — Ontwerptekst volledig uitgewerkt buiten het Google Doc
- **Wat:** Het Google Doc *Ontwerp voor Positie- en beweging meetmodule met LoRa integratie* is aangevuld tot een volledige ontwerptekst. Omdat er geen schrijftoegang tot Google Docs is, staat de tekst in `documenten/Ontwerp-meetmodule.md` (bron) en `documenten/Ontwerp-meetmodule.docx` (Word-versie in de stijl van GStem-Specificaties). Het Doc zelf moet nog handmatig overschreven worden met deze tekst.
- **Opbouw:** dezelfde secties als het Doc (Inleiding, Hardware Specificaties met De Meetmodule, Elektronische Componenten, Voeding en Interface, Bevestiging en Behuizing, LoRa Adapter; Software Specificaties met Data Verwerking, Communicatie en Beveiliging), aangevuld met **De laptopapplicatie**, **Besturing en veiligheid**, **Versiebeheer** en **Testen**, en met een slottabel **Overzicht van de nog te bepalen punten**.
- **Aanvullingen:** socket-headers en voedingsrails op de PCB; ground plane en antenne-plaatsing tegen storing; tabel met componenten en status; warmte van de ESP bij de barometer vandaan; accu -> buck 5 V -> 3,3 V met ground op de uitbreidingsconnector; CSV over UART als vastgelegd protocol naar de voertuigcontroller; 3D-print in PETG/PLA met rubbergdemping; adapter als zuiver doorgeefluik met USB-naar-serieel-omzetter; uitleesfrequenties per sensor en tijdstempel per pakket; veldenlijst van het datapakket; uplink- en downlinkketen in stappen; startscherm, hoofdscherm en de drie modi Kaart, Code en API; API als JSON naar buiten en vrije CSV-regel terug; failsafe-tabel in de firmware van de meetmodule; git-versiebeheer; testplan in vijf stappen.
- **Kernbeslissing onderweg:** de veiligheidsstop zit in de **firmware van de meetmodule**, niet alleen in de laptopapplicatie, zodat het toestel ook veilig is als de verbinding wegvalt. Zie [[beslissingen]].
- **Nieuwe open vragen:** de bron van de RTK-correctiegegevens en het spanningsniveau van de uitbreidingsconnector — toegevoegd aan [[open-vragen]].
- **Gevolg:** de ontbrekende onderdelen zitten nu in een eigen, versioneerbaar bestand; het Doc blijft voorlopig achter.

## Gerelateerd
- [[open-vragen|Open vragen die uit deze voorbereiding volgen]]
- [[specificaties|Specificaties]] — wanneer deze voorbereiding wordt omgezet in harde afspraken
