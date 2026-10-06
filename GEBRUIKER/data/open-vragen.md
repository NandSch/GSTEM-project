---
tags: [gstem, data, open-vragen]
---

# Open vragen

- [x] **Wat moet de definitieve productnaam worden?** — `2026-10-01`: **Positie- en beweging meettoestel met LoRa integratie**. De werktitel *AeroLink* vervalt. (`2026-10-06`: in de naam is *meetmodule* vervangen door *meettoestel*.)
- [x] **Welke IMU wordt het?** — `2026-10-06`: **Adafruit BNO055-breakout** (9-DoF, sensorfusie aan boord, I2C 0x28/0x29). Zie [[componenten]].
- [ ] **LoRa-pakketformaat en gedrag bij pakketverlies?**
- [ ] **Kaartbron, licentie en offline gebruik voor de 3D-weergave?** — `2026-10-06`: de kaart is een **3D-kaart met Google-satellietfotografie**; licentie en offline gebruik blijven open.
- [ ] **Welke exacte 9-DoF IMU met sensorfusie?** — uit voorbereiding meetmodule.
- [ ] **Welke barometer en welke RTK-GNSS-module?** — uit voorbereiding meetmodule. Barometer nog open (BMP581/BME280); RTK-GNSS nog open (de Seeed L76K is geen RTK). Zie [[componenten]].
- [ ] **Exacte LoRa-frequentie/band en configuratie?** — de gekozen Wio-SX1262 bestaat in 868/915 MHz; voor België is **868 MHz** nodig. Rest van de configuratie nog open. (`2026-10-06`)
- [ ] **Formaat en protocol van datapakketten tussen meetmodule en laptop (uplink en downlink)?**
- [ ] **LoRa downlink: met of zonder ACK, en hoe omgaan met pakketverlies bij besturingscommando's?**
- [ ] **Commandoformaat: binair, JSON, tekst of protobuf?**
- [ ] **Welk programmeermodel: laptop doet alles, edge-script op module, of hybride?**
- [x] **Uitbreidingsconnector: PWM, UART, I2C, CAN of analoog?** — `2026-10-06`: **UART via TX/RX**; de Arduino van het vliegtuigje neemt CSV-waarden aan op zijn TX/RX-punten.
- [ ] **Geofencing-grenzen: hoe ingesteld en opgeslagen?**
- [ ] **Batterijspecificatie definitief vastleggen** — voorbereiding noemt 7.4 V 2 A als voorbeeld.
- [ ] **Spanningsregelaar: welke specs en component?**
- [ ] **Heatsink-ontwerp of -keuze voor de ESP32-S3?**
- [ ] **PCB-afmetingen, laagcount en connectorkeuze?**
- [ ] **Mock-up details: materiaal, servo-type, microcontroller?** — optionele uitbreiding.
- [ ] **Veiligheidsstop-gedrag: welke acties bij verlies van verbinding, en na hoeveel seconden?**
- [ ] **Safe-state definitie: neutrale servo's, throttle nul, of ander gedrag per toesteltype?**
- [ ] **Kalman-filter implementatie: welke variant en bibliotheek?**
- [ ] **API-techniek tussen app en extern programma: WebSocket, TCP-socket, HTTP of named pipe?**
- [x] **Bus tussen meetmodule en Arduino: SPI, I2C of UART?** — `2026-09-29`: seriele verbinding (UART) bij CSV-tekstprotocol
- [x] **Protocol tussen meetmodule en Arduino: binair, tekst of iets anders?** — `2026-09-29`: CSV (kommagescheiden waarden), vaste veldvolgorde
- [x] **Checksum of terminator nodig in CSV-protocol tussen ESP en Arduino?** — `2026-09-29`: geen checksum, `\n` als terminator is voldoende
- [ ] **Exacte veldvolgorde en waardeschaal in het CSV-protocol?**
- [x] **Aantal servo's en exact voertuigtype?** — `2026-10-06`: mock-up **vliegtuigje** met **drie besturingsvlakken** (rolroeren, hoogteroer, richtingsroer); de Arduino stelt de servo's in. Een volledig functioneel vliegtuig is niet vereist.
- [ ] **Route en meetgegevens opslaan als bestand, en dat bestand direct openen in de website** — werkpunt, nog niet gebouwd (`2026-10-01`). Genoteerd in [[handleiding]].
- [ ] **Handleiding en screenshots bijwerken na herindeling code-pagina** — de handleiding beschrijft nog "variabelen aanklikken als voorbeeld"; in de demo zijn de variabelen nu een niet-klikbaar overzicht, schrijft de gebruiker zelf de CSV-regel en kreeg de API een eigen sectie (`#page-api`). (`2026-10-04`)
- [ ] **API-downlink definitief: vrije CSV-regel of vaste commando's?** — in de demo stuurt het externe programma nu een vrije CSV-regel terug (beslissing `2026-10-04`); de techniek zelf (WebSocket/TCP/HTTP) blijft open. (`2026-10-04`)
- [x] **Welke versie van de Code-pagina wordt de definitieve: A of B?** — `2026-10-04`: **versie B** (één kolom met uitklapbare hulp) is gepromoveerd tot `index.html`; de A/B-testbestanden zijn verwijderd.
- [ ] **Waar komen de RTK-correctiegegevens vandaan?** — eigen basisstation of een correctiedienst via de laptop. (`2026-10-05`)
- [ ] **Op welk spanningsniveau werkt de uitbreidingsconnector?** — de meetmodule is 3,3 V-logica; de voertuigcontroller kan 5 V verwachten. Niveau-afstemming nodig vóór het aansluiten. (`2026-10-05`)

- [ ] **Welke exacte breakout-modellen en bijbehorende pinouts?** — `2026-10-06`: **XIAO ESP32S3 + Wio-SX1262 kit** (rekenkern + LoRa) en **Adafruit BNO055** (IMU) zijn gekozen. Barometer en RTK-GNSS nog open; pin-budget van de XIAO (± 14 I/O) te controleren. Zie [[componenten]].
- [x] **Wordt de 7,4 V-accu of de barrel-connector de hoofdvoeding?** — `2026-10-06`: **7,4 V-accu + zekering/ompoolbeveiliging -> buck 5 V -> LDO 3,3 V**. De XIAO wordt op 5 V gevoed; de ingebouwde LiPo-lader wordt niet gebruikt. Zie [[componenten]] en [[beslissingen]].
- [ ] **Welk PCB-ontwerpgereedschap (KiCad?) en welke fabrikant?** — advies `2026-10-06`: **KiCad** als app, **JLCPCB/PCBWay** als fabrikant. Werkwijze in [[pcb-ontwerp]]. Keuze nog te bevestigen. (`2026-10-06`)
- [ ] **Dubbele I2C-pull-ups en level shifter: welke breakouts hebben al pull-ups, en is 5 V-aansturing nodig?** (`2026-10-06`)

- [ ] **Socket-headers of een alternatief (precisie-sockets, direct solderen, castellated, board-to-board)?** — socket-headers worden amateuristisch gevonden; keuze bepaalt de landpatronen op de draagprint. (`2026-10-06`)
- [ ] **Wat komt er precies op de print zelf?** — vast staat LED + sockets (alle componenten worden zelf aangekocht, `2026-10-06`). Nog te bevestigen of de voedingsonderdelen (buck, LDO, zekering, weerstanden, condensatoren) ook op de print komen of als losse modules. Bepaalt de voetafdrukken en de stuklijst. (`2026-10-06`)

## AI-taken (voert de AI later uit)

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`, zie [[componenten]] en [[beslissingen]])
