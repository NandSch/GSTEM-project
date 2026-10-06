---
tags: [gstem, data, open-vragen]
---

# Open vragen

- [x] **Wat moet de definitieve productnaam worden?** — `2026-10-01`: **Positie- en beweging meettoestel met LoRa integratie**. De werktitel *AeroLink* vervalt. (`2026-10-06`: in de naam is *meetmodule* vervangen door *meettoestel*.)
- [x] **Welke IMU wordt het?** — `2026-10-06`: **Adafruit BNO055-breakout** (9-DoF, sensorfusie aan boord, I2C 0x28/0x29). Zie [[componenten]].
- [ ] **LoRa-pakketformaat en gedrag bij pakketverlies?**
- [ ] **Kaartbron, licentie en offline gebruik voor de 3D-weergave?** — `2026-10-06`: de kaart is een **3D-kaart met Google-satellietfotografie**; licentie en offline gebruik blijven open.
- [ ] **Welke exacte 9-DoF IMU met sensorfusie?** — uit voorbereiding meetmodule.
- [x] **Welke barometer en welke RTK-GNSS-module?** — `2026-10-06`: barometer **Adafruit BMP390** (meest accurate, ±3 Pa, laagste ruis); RTK-GNSS **Quectel LC29H(DA)** (dual-band L1+L5, rover). Zie [[componenten]] en [[beslissingen]].
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
- [x] **Waar komen de RTK-correctiegegevens vandaan?** — `2026-10-06`: een **NTRIP-dienst** via de laptop (geen eigen basisstation). Enkel de **provider** (gratis/betaald) blijft nog te kiezen. (`2026-10-05`)
- [ ] **Welke NTRIP-provider en abonnement?** — `2026-10-06`: wordt een **gratis** dienst; de **gebruiker zoekt die zelf**. Vraagt internet op de laptop tijdens het meten. (`2026-10-06`)
- [x] **Welke level shifter voor de UART 3,3 V <-> 5 V?** — `2026-10-06`: **TXB0104** (4-kanaals bidirectioneel) op de draagprint; VCCA 3,3 V, VCCB 5 V. (`2026-10-06`)
- [x] **Zekering, ompoolbeveiliging en TVS: welke onderdelen?** — `2026-10-06`: **2 A PTC-zekering + P-MOSFET ompoolbeveiliging (DMG2301L) + TVS SMBJ10A**. (`2026-10-06`)
- [x] **Is een losse LDO 3,3 V nodig?** — `2026-10-06`: ja, **AP2112K-3.3** voor een eigen 3,3 V-rail. Let op: de LoRa-ontvanger (tweede XIAO) krijgt 3,3 V via USB uit de XIAO zelf. (`2026-10-06`)
- [x] **Exacte uitbreidingsconnector voor de UART?** — `2026-10-06`: **4-pins schroefklem 3,5 mm (KF128/KF301)**, pinout GND/+5 V/TX/RX. (`2026-10-06`)
- [x] **LoRa IPEX -> SMA-pigtail en SMA-bulkhead?** — `2026-10-06`: **nodig**, de antenne wordt buiten het vliegtuigje geconnecteerd; gekozen: IPEX/U.FL -> SMA female bulkhead pigtail. (`2026-10-06`)
- [x] **Welke GNSS-antenne?** — `2026-10-06`: actieve **dual-band L1/L5-antenne met SMA, LNA + ground plane** (compact; voorbeeld Waveshare), passend bij de LC29H(DA). (`2026-10-06`)
- [x] **Wat komt er naast LED + sockets nog op de print?** — `2026-10-06`: ontkoppelcondensatoren (100 nF + 10 uF per module), bulk-elco 100 uF, schroefklem, level shifter TXB0104, LDO AP2112K-3.3, voedingsbescherming, 4x M3-gaten. Zie [[componenten]]. (`2026-10-06`)
- [x] **Op welk spanningsniveau werkt de uitbreidingsconnector?** — `2026-10-06`: de connector voert 5 V-niveau via de **TXB0104**-level shifter; de XIAO-zijde blijft 3,3 V. (`2026-10-05`)

- [ ] **Welke exacte breakout-modellen en bijbehorende pinouts?** — `2026-10-06`: **XIAO ESP32S3 + Wio-SX1262 kit** (rekenkern + LoRa), **Adafruit BNO055** (IMU), **Adafruit BMP390** (barometer) en **Quectel LC29H(DA)** (RTK-GNSS) zijn gekozen. Enkel de **pinouts** en het **pin-budget** van de XIAO (± 14 I/O) moeten nog genoteerd/gecontroleerd worden. Zie [[componenten]].
- [x] **Wordt de 7,4 V-accu of de barrel-connector de hoofdvoeding?** — `2026-10-06`: **7,4 V-accu + zekering/ompoolbeveiliging -> buck 5 V -> LDO 3,3 V**. De XIAO wordt op 5 V gevoed; de ingebouwde LiPo-lader wordt niet gebruikt. Zie [[componenten]] en [[beslissingen]].
- [ ] **Welk PCB-ontwerpgereedschap (KiCad?) en welke fabrikant?** — advies `2026-10-06`: **KiCad** als app, **JLCPCB/PCBWay** als fabrikant. Werkwijze in [[pcb-ontwerp]]. Keuze nog te bevestigen. (`2026-10-06`)
- [x] **Dubbele I2C-pull-ups en level shifter: welke breakouts hebben al pull-ups, en is 5 V-aansturing nodig?** — `2026-10-06`: de BNO055- en BMP390-breakouts hebben al pull-ups, dus **geen extra op de print**; de **TXB0104** verzorgt de 3,3 V <-> 5 V voor de UART. (`2026-10-06`)

- [x] **Socket-headers of een alternatief (precisie-sockets, direct solderen, castellated, board-to-board)?** — `2026-10-06`: **dual-wipe** voor de XIAO, **precisie/gefreesd** voor de overige modules. (`2026-10-06`)
- [x] **Wat komt er precies op de print zelf?** — `2026-10-06`: **LED + sockets** plus ontkoppeling, bulk-elco, schroefklem, level shifter (TXB0104), LDO (AP2112K-3.3) en voedingsbescherming (PTC/P-MOSFET/TVS). De **buck, accu, barrel-connector en sensormodules** blijven losse modules. Zie [[componenten]]. (`2026-10-06`)

## Nog te beslissen: bestellijst (`2026-10-06`)

- [ ] **BMP390 en LC29H(DA) niet op antratek** — kiezen of elders bestellen of een antratek-alternatief nemen (LG290P of ZED-F9P).
- [ ] **Barometer: beter model dan de BME280** — `2026-10-06`: gebruiker kiest liever een **nauwkeuriger model** (BMP390 of beter) i.p.v. de BME280. antratek heeft geen BMP390/BMP388/BMP581; **zoeken op andere leveranciers is door de gebruiker uitgesteld** (nog niet doen). BME280 staat voorlopig als plaatsvervanger in [[bestellijst]].
- [ ] **Level shifter** — gekozen TXB0104 staat niet op antratek; het gevonden bidirectionele Logic Level Converter (BSS138) als alternatief aanvaarden?
- [ ] **GNSS-antenne** — dure L1/L5-antenne (EUR 120,94) of goedkopere magneetantenne (EUR 19,30)?
- [ ] **Barrel-connector** — PCB-montage of de adapter met schroefklem gebruiken?

## AI-taken (voert de AI later uit)

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`, zie [[componenten]] en [[beslissingen]])
