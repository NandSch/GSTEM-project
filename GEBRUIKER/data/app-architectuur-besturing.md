---
tags: [gstem, data, architectuur, besturing, api, app]
aangemaakt: 2026-09-29
status: denkwijze / voorbereiding
---

# App-architectuur: meetdata, extern programma en besturing

> [!info] Dit document beschrijft de door de gebruiker voorgestelde gelaagde architectuur voor de verwerking en terugsturing van besturingscommando's.

## Architectuur in lagen

```text
+-------------------------------------------------------+
|  LAGEN                                                |
+-------------------------------------------------------+
|  L4  Voertuigcontroller (Arduino) — **secundaire demonstratie** |
|       - Ontvangt commando's van meetmodule            |
|       - Stuurt motoren, servo's, roer aan             |
|       - Protocol: CSV over UART, aantal servo's flexibel |
+-------------------------------------------------------+
|  L3  Meetmodule (ESP32-S3 op PCB)                   |
|       - Sensoren uitlezen (IMU, baro, RTK-GNSS)     |
|       - LoRa-communicatie met laptop                  |
|       - Doorgeefluik: ontvangt commando's via LoRa   |
|         en stuurt die door naar Arduino (L4)          |
+-------------------------------------------------------+
|  L2  Laptopapp                                        |
|       - GUI: kaart, live telemetrie, setup            |
|       - Modus "Code": eenvoudige besturingslogica     |
|       - Data-router: stuurt live JSON naar externe    |
|         programma's en ontvangt hun output terug      |
|       - Commando's naar meetmodule via USB-LoRa       |
+-------------------------------------------------------+
|  L1  Extern programma (buiten de app)                 |
|       - Ontvangt meetdata live in JSON-formaat        |
|       - Complexe berekeningen, AI, visualisatie, etc.  |
|       - Stuurt acties / commando's terug naar app     |
+-------------------------------------------------------+
```

## Datastroom

### Uplink (sensordata naar laptop)

```text
Sensoren → ESP32-S3 → LoRa → USB-adapter → Laptopapp
```

### Verwerkingspaden in de laptopapp

De app krijgt meetdata binnen en die kan naar drie bestemmingen:

1. **Interne GUI** — direct weergave op kaart en in meters
2. **Interne "Code"-modus** — eenvoudige besturingslogica (Python/Arduino/C-achtig) die direct commando's genereert
3. **Extern programma** — via een API / lokale interface in JSON-formaat

### Downlink (besturing naar toestel)

```text
Laptopapp (code of extern programma)
    → commando's genereren
    → USB-adapter → LoRa
    → Meetmodule ESP32-S3
    → UART (TX/RX) → Arduino (voertuigcontroller)
    → motoren / servo's
```

## Communicatie tussen lagen

### A. Tussen laptopapp en extern programma

| Aspect | Mogelijkheid |
|--------|--------------|
| **Techniek** | Lokale WebSocket, TCP-socket, HTTP POST/GET, of named pipe |
| **Formaat** | JSON (afgesproken) |
| **Richting** | Bidirectioneel: app stuurt meetdata uit; extern programma stuurt commando's terug |
| **Voorbeeld JSON (uit)** | `{ "timestamp": 1234567890, "lat": 50.8, "lon": 4.3, "alt": 120, "heading": 45, "speed": 12.5, ... }` |
| **Voorbeeld JSON (terug)** | Eerder: `{ "cmd": "throttle", "value": 0.75 }`. **Bijgesteld op 2026-10-04:** in de demo stuurt het externe programma een **vrije CSV-regel** terug (bv. `15,-5,75,60`), zodat er geen vaste velden of commando's nodig zijn. |

> [!question] Open keuze: welke lokale techniek voor de API? WebSocket is snel en bidirectioneel; TCP-socket is eenvoudig; HTTP is makkelijker te debuggen.

> [!info] Update `2026-10-04`: De API kreeg in de webdemo een eigen sectie (`#page-api`) en de downlink is een vrije CSV-regel in plaats van vaste commando's. Zie [[beslissingen]] en [[specificaties]].

### B. Tussen meetmodule (ESP32-S3) en Arduino (voertuigcontroller)

| Aspect | Keuze |
|--------|-------|
| **Bus** | Seriele verbinding (UART) — meest logisch bij CSV-tekst op korte afstand |
| **Master/Slave** | ESP32-S3 stuurt CSV-regel; Arduino ontvangt en parst |
| **Protocol** | **CSV (kommagescheiden waarden)** — leesbaar, geen bibliotheek nodig |
| **Speed** | 115200 baud is standaard voor ESP32-Arduino; voldoende voor ~10–50 regels/s |

> [!info] Beslissing vastgelegd: CSV-protocol is leesbaar via seriele monitor en makkelijk te parsen met `split(',')` op beide kanten.

#### Voorbeeld CSV-regel (richting)

```
15,-5,75,60,80,1\n
```

| Positie | Veld | Bereik / eenheid | Voorbeeld | Opmerking |
|---------|------|------------------|-----------|-----------|
| 1 | `servo_1` | graden, -45 tot 45 | `15` | Type hangt af van voertuig; flexibel |
| 2 | `servo_2` | graden, -45 tot 45 | `-5` | Type hangt af van voertuig; flexibel |
| 3 | `motor_links` | 0 tot 255 of -100 tot 100 | `75` | |
| 4 | `motor_rechts` | 0 tot 255 of -100 tot 100 | `60` | |
| 5 | `throttle` | 0 tot 100 (procent) | `80` | |
| 6 | `modus` | `0`=handmatig, `1`=automatisch, `2`=stop | `1` | |

> [!info] Het aantal servo's is **niet vastgelegd** en is afhankelijk van het uiteindelijke voertuig. De eerste twee velden zijn gereserveerd als servo-placeholders. Bij een vliegtuigmock-up kunnen dit roll en pitch zijn; bij een RC-auto zijn dit misschien andere functies of ongebruikt (waarde `0`).

> [!info] **Geen checksum.** De terminator `\n` is voldoende op een korte seriele kabel binnen hetzelfde voertuig.

> [!info] Update `2026-10-06`: de afgewerkte specificaties bevestigen de **UART TX/RX**-koppeling en noemen **drie** besturingsvlakken (rolroeren, hoogteroer, richtingsroer). Zie [[gstem-specificaties]] en [[beslissingen]].

> [!warning] Voertuigbesturing is een **secundaire demonstratie**. Het hoofddoel is de meetmodule zelf en de USB-ontvanger.

### C. Tussen laptopapp en meetmodule (LoRa)

| Aspect | Mogelijkheid |
|--------|--------------|
| **Formaat** | Binaire structs of JSON (kortere payload = binair) |
| **Downlink payload** | Compacte commando's: throttle, servo-hoeken, modus |
| **Bevestiging** | Met ACK of zonder; voor besturing is ACK wenselijk |

## Voorbeeld commandoformaat (richting)

De gebruiker noemt concrete commando's:

| Commando | Beschrijving | Waardebereik |
|----------|--------------|--------------|
| `motor_links_snelheid` | Snelheid linker motor | -100 tot 100 (of 0 tot 255) |
| `motor_rechts_snelheid` | Snelheid rechter motor | -100 tot 100 (of 0 tot 255) |
| `servo_roll` | Rolroer-hoek | -45 tot 45 graden |
| `servo_pitch` | Hoogteroer-hoek | -45 tot 45 graden |
| `throttle` | Algemene gaspedaal | 0 tot 100 procent |
| `modus` | Besturingsmodus | `handmatig`, `automatisch`, `stop` |

> [!info] Het exacte voertuigtype (RC-auto, vliegtuigmock-up) en het aantal servo's zijn **secundair** en worden later bepaald. De CSV-structuur is flexibel: meer servo-velden kunnen worden toegevoegd zonder de rest te verstoren.

## Besturingsmodi in de app

| Modus | Werking |
|-------|---------|
| **Handmatig** | Gebruiker stuurt direct via GUI-knoppen of joystick |
| **Code (eenvoudig)** | Gebruiker schrijft korte logica in app; app evalueert dat direct en stuurt commando's |
| **Extern programma** | App fungeert als relay: meetdata → extern programma → teruggekregen commando's → LoRa |

## Failsafe (veiligheidsstop)

Ongeacht de bron van de commando's (interne code of extern programma), de module moet een eigen failsafe hebben:

| Scenario | Actie |
|----------|-------|
| Geen geldig commando binnen X seconden | Alle motoren naar nul; servo's naar neutraal |
| Ongeldig commandoformaat | Negeer; teller optellen; bij N fouten → safe state |
| Geofencing overschreden | Forceer `modus: stop` |
| LoRa-verbinding verbroken | Module gaat over op eigen safe-state (autonoom) |

## Vergelijking met bestaande documenten

| Bron | Overlap / verschil |
|------|-------------------|
| `01-projectoverzicht.md` | Specificeert "berekende stuurcommando's" en "programmeermodus", maar niet de splitsing tussen interne en externe verwerking |
| `04-blokschema-aerolink.md` | Schema toont alleen "testcorrecties" naar servo; niet de gelaagde architectuur |
| `GSTEMAPPPREVIEWWEB` | Huidige demo simuleert alleen uplink; downlink en externe API ontbreken |
| `GStem-Specificaties.md` (afgewerkt `2026-10-06`) | Gebruikersgerichte bevestiging: startscherm met OK, 3D-kaart Google-satelliet + tabel, Code-editor met CSV terug, API aan/uit en adres, Arduino via TX/RX, rolroeren/hoogteroer/richtingsroer; zie [[gstem-specificaties]] |

## Gerelateerd

- [[open-vragen|Open vragen]] — specifiek de items over API-techniek, Arduino-protocol en commandoformaat
- [[specificaties|Specificaties]] — wanneer deze architectuur wordt vastgelegd
- [[besturing-en-commandos|Besturing en commando's terug naar het toestel]] — het bredere denkdocument
- [[meetmodule-voorbereiding|Positie- en beweging meettoestel — voorbereiding]] — hardwarecontext
