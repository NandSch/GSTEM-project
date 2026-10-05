---
tags: [gstem, data, open-vragen]
---

# Open vragen

- [x] **Wat moet de definitieve productnaam worden?** — `2026-10-01`: **Positie- en beweging meetmodule met LoRa integratie**. De werktitel *AeroLink* vervalt.
- [ ] **Welke IMU wordt het?** — BNO055 is een kandidaat, niet vastgelegd.
- [ ] **LoRa-pakketformaat en gedrag bij pakketverlies?**
- [ ] **Kaartbron, licentie en offline gebruik voor de 3D-weergave?**
- [ ] **Welke exacte 9-DoF IMU met sensorfusie?** — uit voorbereiding meetmodule.
- [ ] **Welke barometer en welke RTK-GNSS-module?** — uit voorbereiding meetmodule.
- [ ] **Exacte LoRa-frequentie/band en configuratie?** — uit voorbereiding meetmodule.
- [ ] **Formaat en protocol van datapakketten tussen meetmodule en laptop (uplink en downlink)?**
- [ ] **LoRa downlink: met of zonder ACK, en hoe omgaan met pakketverlies bij besturingscommando's?**
- [ ] **Commandoformaat: binair, JSON, tekst of protobuf?**
- [ ] **Welk programmeermodel: laptop doet alles, edge-script op module, of hybride?**
- [ ] **Uitbreidingsconnector: PWM, UART, I2C, CAN of analoog?** — bepaalt het firmwarecommandoformaat
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
- [ ] **Aantal servo's en exact voertuigtype?** — secundair, later te bepalen
- [ ] **Route en meetgegevens opslaan als bestand, en dat bestand direct openen in de website** — werkpunt, nog niet gebouwd (`2026-10-01`). Genoteerd in [[handleiding]].
- [ ] **Handleiding en screenshots bijwerken na herindeling code-pagina** — de handleiding beschrijft nog "variabelen aanklikken als voorbeeld"; in de demo zijn de variabelen nu een niet-klikbaar overzicht, schrijft de gebruiker zelf de CSV-regel en kreeg de API een eigen sectie (`#page-api`). (`2026-10-04`)
- [ ] **API-downlink definitief: vrije CSV-regel of vaste commando's?** — in de demo stuurt het externe programma nu een vrije CSV-regel terug (beslissing `2026-10-04`); de techniek zelf (WebSocket/TCP/HTTP) blijft open. (`2026-10-04`)
- [x] **Welke versie van de Code-pagina wordt de definitieve: A of B?** — `2026-10-04`: **versie B** (één kolom met uitklapbare hulp) is gepromoveerd tot `index.html`; de A/B-testbestanden zijn verwijderd.
- [ ] **Waar komen de RTK-correctiegegevens vandaan?** — eigen basisstation of een correctiedienst via de laptop. (`2026-10-05`)
- [ ] **Op welk spanningsniveau werkt de uitbreidingsconnector?** — de meetmodule is 3,3 V-logica; de voertuigcontroller kan 5 V verwachten. Niveau-afstemming nodig vóór het aansluiten. (`2026-10-05`)
