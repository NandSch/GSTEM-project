---
tags: [gstem, data, besturing, commandos, protocol, lora]
aangemaakt: 2026-09-29
status: denkwijze / voorbereiding
---

# Besturing en commando's terug naar het toestel

> [!info] Denk- en voorbereidingsdocument
> Dit document verkent hoe de laptopapp commando's, stuurdata of programmeerbare logiek terugstuurt naar de meetmodule en van daaruit naar het aangesloten toestel (vliegtuigmock-up, RC-auto of bestaande voertuigcontroller).

> [!info] Status `2026-10-06`: de afgewerkte specificaties leggen de koppeling (UART TX/RX), het mock-upvliegtuig en de drie besturingsvlakken vast. De overige dimensies hieronder blijven denkrichting. Zie [gstem-specificaties](gstem-specificaties.md).

## Situatie

De keten is bidirectioneel:

```text
Laptopapp → USB-adapter ESP → LoRa ↓
                                      Meetmodule ESP → uitbreidingsconnector → toestelcontroller
Sensoren ↑ ← LoRa ← USB-adapter ESP ←
```

De uplink (sensordata naar laptop) staat redelijk beschreven. De downlink (besturing naar toestel) heeft nog veel open dimensies.

## Ontwerpdimensies

### 1. Transportlaag — LoRa downlink

| Aspect | Opties | Opmerking |
|--------|--------|-----------|
| Bevestiging (ACK) | Met ACK / zonder ACK / optioneel | LoRa heeft beperkte airtime; ACK kost bandbreedte |
| Frequentie | Zelfde band als uplink of apart kanaal | Regionale regelgeving bepaalt duty cycle |
| Downlink-bandbreedte | Klein, grootte beperkt door payload-limiet en duty cycle | Maximale payload ~ 50–243 byte afhankelijk van SF |
| Betrouwbaarheid | Herhaling bij timeout / geen herharding / forward-error-correction | Trade-off tussen betrouwbaarheid en latency |

> [!question] Open keuze: gebruiken we een bevestigd protocol op de downlink, of is unidirectionele besturing acceptabel met een heartbeat als failsafe?

### 2. Protocol en formaat — wat reist er door de lucht?

| Optie | Voordeel | Nadeel |
|-------|----------|--------|
| **Compact binair** (structs, fixed-length) | Minimale payload, snel parsen op ESP32 | Minder leesbaar bij debug, versioning lastiger |
| **JSON** | Leesbaar, flexibel, makkelijk te genereren in webapp | Groter, meer overhead op ESP32 |
| **Protobuf / MessagePack** | Compacter dan JSON, getypt | Extra bibliotheek/complexiteit op beide kanten |
| **Tekstcommando's** (ASCII, zoals MAVLink-lite of NMEA-stijl) | Debugbaar via seriele monitor | Inefficient voor hoge frequentie |

> [!question] Open keuze: welk serialisatieformaat past bij de verwachte payload-grootte en de programmeertaal/framework van de laptopapp?

### 3. Soorten commando's

De app moet minstens deze categorieen kunnen sturen:

1. **Directe stuurwaarden**
   - Servohoeken (rolroer, hoogteroer, evt. meer)
   - Throttle / snelheid
   - Schakelaars (modi, arming, lampen)
2. **Moduswissels**
   - Handmatig / automatisch / programmeermodus
   - Testmodus / kalibratiemodus
3. **Configuratie**
   - Geofencing-grenzen instellen
   - Sensorkalibratie-trigger
   - Maximale stuurhoeken of snelheden beperken
4. **Programmeerbare logica (edge)**
   - Gebruiker schrijft script/regels in de app; meetmodule voert zelfstandig uit zonder continue downlink
   - Dit vermindert LoRa-afhankelijkheid en verlaagt latency

> [!question] Open keuze: is de meetmodule een doorgeefluik (relay) dat alles direct doorstuurt naar de toestelcontroller, of voert de meetmodule zelf stuurberekeningen uit?

### 4. Programmeermodus in de app

De specificaties noemen een "Modus Programmering" waarin de gebruiker eigen verwerkingscode toevoegt.

| Architectuur | Werking | Voordeel | Nadeel |
|--------------|---------|----------|--------|
| **A. Alles op de laptop** | App berekent acties op basis van meetdata; stuurt alleen stuurcommando's terug | Meeste rekenkracht, makkelijk te debuggen | Continue LoRa-verbinding nodig voor elk commando |
| **B. Edge-script op module** | Gebruiker schrijft logica in de app; bij "deploy" wordt het script naar de meetmodule gestuurd en daar uitgevoerd | Module werkt autonoom na deploy; minder LoRa-verkeer | Beperkte rekenkracht op ESP32; scripting-engine nodig (bijv. MicroPython, Lua, of een eenvoudige regelset) |
| **C. Hybride** | Basisstabilisatie/autonoom op module; hogere orde beslissingen op laptop | Beste van beide werelden | Complexer, twee codebase-paden |

> [!question] Open keuze: welk programmeermodel past bij het schoolproject — eenvoudige stuurwaarden vanuit de app, of een scripting-laag op de ESP32?

### 5. Veiligheidsstop en failsafe

| Scenario | Gewenst gedrag |
|----------|----------------|
| Verlies van LoRa-verbinding | Na X seconden geen geldig commando → safe state |
| Verlies van USB-verbinding (laptop) | Idem, via LoRa-adapter of module-eigen watchdog |
| Ongeldig commando | Parsen mislukt → negeren + teller; bij N fouten → safe state |
| Geofencing-schending | Automatisch safe state, ongeacht commando's |

| Safe-state optie | Toepassing |
|------------------|------------|
| Servo's naar neutraal | Stilstaande mock-up |
| Throttle naar nul + rem | RC-auto |
| Behoud laatste geldige stuurstand (kort) → daarna neutraal | Vliegtuigachtige toepassingen |

> [!question] Open keuze: wat is de gewenste safe state voor het toestel dat jij gaat aansturen?
> [!question] Open keuze: hoe lang mag de downlink onderbroken zijn voordat de veiligheidsstop ingrijpt?

### 6. Elektrische koppeling — uitbreidingsconnector

De meetmodule moet fysiek commando's doorgeven naar de bestaande controller.

> [!success] Vastgelegd `2026-10-06`: **UART via TX/RX**. De Arduino van het vliegtuigje neemt CSV-waarden aan en is op zijn TX/RX-punten met het meettoestel verbonden. De eerder verkende opties (PWM, I2C, CAN, analoog) vervallen voor de mock-up. Zie [gstem-specificaties](gstem-specificaties.md) en [beslissingen](beslissingen.md).

| Signaaltype | Status |
|-------------|--------|
| **UART / serieel (TX/RX)** | **Gekozen** — CSV-tekst naar de Arduino van de mock-up |
| PWM (servo) | Vervallen voor de mock-up |
| I2C / CAN | Vervallen voor de mock-up |
| Analoge spanning | Vervallen voor de mock-up |

**Vliegtuig-mock-up: drie besturingsvlakken** — rolroeren, hoogteroer en richtingsroer reageren op de metingen; de Arduino stelt de servo's in (real-time). Zie [gstem-specificaties](gstem-specificaties.md).

> [!warning] Het **exacte CSV-veldformaat** en de **spanningsniveaus** van de koppeling blijven open ([open-vragen](open-vragen.md)).

## Gerelateerd

- [Open vragen](open-vragen.md) — specifiek de items over besturing, veiligheidsstop, LoRa-protocol, geofencing en uitbreidingsconnector
- [Specificaties](specificaties.md) — wanneer deze voorbereiding wordt vastgelegd
- [Positie- en beweging meettoestel — voorbereiding](meetmodule-voorbereiding.md) — hardwarecontext
