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
- [x] **Zekering, ompoolbeveiliging en TVS: welke onderdelen?** — `2026-10-06`: **2 A PTC-zekering + TVS SMBJ10A**; de **P-MOSFET-ompoolbeveiliging vervalt** (`2026-10-06`).
- [x] **Is een losse LDO 3,3 V nodig?** — `2026-10-06`: ja, **AP2112K-3.3** voor een eigen 3,3 V-rail. Let op: de LoRa-ontvanger (tweede XIAO) krijgt 3,3 V via USB uit de XIAO zelf. (`2026-10-06`)
- [x] **Exacte uitbreidingsconnector voor de UART?** — `2026-10-06`: **4-pins schroefklem 3,5 mm (KF128/KF301)**, pinout GND/+5 V/TX/RX. (`2026-10-06`)
- [x] **LoRa IPEX -> SMA-pigtail en SMA-bulkhead?** — `2026-10-06`: **nodig**, de antenne wordt buiten het vliegtuigje geconnecteerd; gekozen: IPEX/U.FL -> SMA female bulkhead pigtail. (`2026-10-06`)
- [x] **Welke GNSS-antenne?** — `2026-10-06`: actieve **dual-band L1/L5-antenne met SMA, LNA + ground plane** (compact; voorbeeld Waveshare), passend bij de LC29H(DA). (`2026-10-06`)
- [x] **Wat komt er naast LED + sockets nog op de print?** — `2026-10-06`: ontkoppelcondensatoren (100 nF + 10 uF per module), bulk-elco 100 uF, schroefklem, level shifter TXB0104, LDO AP2112K-3.3, voedingsbescherming, 4x M3-gaten. Zie [[componenten]]. (`2026-10-06`)
- [x] **Op welk spanningsniveau werkt de uitbreidingsconnector?** — `2026-10-06`: de connector voert 5 V-niveau via de **TXB0104**-level shifter; de XIAO-zijde blijft 3,3 V. (`2026-10-05`)

- [ ] **Welke exacte breakout-modellen en bijbehorende pinouts?** — `2026-10-06`: **XIAO ESP32S3 + Wio-SX1262 kit** (rekenkern + LoRa), **Adafruit BNO085** (IMU), **Adafruit BMP581** (barometer) en **Quectel LC29HDA** (RTK-GNSS) zijn gekozen. Enkel de **pinouts** en het **pin-budget** van de XIAO (± 14 I/O) moeten nog genoteerd/gecontroleerd worden. Zie [[componenten]].
- [x] **Wordt de 7,4 V-accu of de barrel-connector de hoofdvoeding?** — `2026-10-06`: **7,4 V-accu + zekering/ompoolbeveiliging -> buck 5 V -> LDO 3,3 V**. De XIAO wordt op 5 V gevoed; de ingebouwde LiPo-lader wordt niet gebruikt. Zie [[componenten]] en [[beslissingen]].
- [x] **Welk PCB-ontwerpgereedschap en welke fabrikant?** — `2026-10-06`: gereedschap **KiCad**; fabrikant **AISLER** (EU). Zie [[pcb-fabrikanten]] en [[bestelschema-pcb]]. De overige fabrikanten (JLCPCB, PCBWay, OSH Park, Eurocircuits, Multi-CB) zijn bewaard maar niet gekozen. (`2026-10-06`)
- [x] **Level shifter op de print: TXB0108-breakout of TXB0104-IC?** — **Beslissing `2026-10-07`: de TXB0108-breakout** (€ 8,70, Kiwi) wordt besteld; de TXB0104-IC (± € 1,80) blijft enkel een alternatief. (`2026-10-06`)
- [ ] **Exacte bordafmeting en laagopbouw van de draagprint?** — aanname in [[bestelschema-pcb]]: **100 x 75 mm, 2 lagen**. Definitief maken zodra de KiCad-layout klaar is. (`2026-10-06`)
- [x] **Dubbele I2C-pull-ups en level shifter: welke breakouts hebben al pull-ups, en is 5 V-aansturing nodig?** — `2026-10-06`: de BNO055- en BMP390-breakouts hebben al pull-ups, dus **geen extra op de print**; de **TXB0104** verzorgt de 3,3 V <-> 5 V voor de UART. (`2026-10-06`)

- [x] **Socket-headers of een alternatief (precisie-sockets, direct solderen, castellated, board-to-board)?** — `2026-10-06`: **dual-wipe** voor de XIAO, **precisie/gefreesd** voor de overige modules. (`2026-10-06`)
- [x] **Wat komt er precies op de print zelf?** — `2026-10-06`: **LED + sockets** plus ontkoppeling, bulk-elco, schroefklem, level shifter (TXB0104), LDO (AP2112K-3.3) en voedingsbescherming (PTC + TVS; geen P-MOSFET). De **buck, accu, barrel-connector en sensormodules** blijven losse modules. Zie [[componenten]]. (`2026-10-06`)

## Nog te beslissen: bestellijst (`2026-10-06`)

- [x] **BMP390 en LC29H(DA) niet op antratek** — BMP581 bij **Kiwi**. Voor LC29H(DA) is de Waveshare-HAT bij Eckstein (€ 71,39) een geverifieerde **terugvaloptie**; voorkeursbron is nu China/AliExpress, listing nog open. Zie [[bestellijst]] en [[gps-rtk-prijzen]].
- [x] **Barometer: beter model dan de BME280** — `2026-10-06`: gebruiker kiest liever een **nauwkeuriger model**; **Kiwi heeft de BMP581 (€ 10,88) op voorraad**. Definitief (`2026-10-07`).
- [ ] **Level shifter** — gekozen TXB0108-breakout bij Kiwi (€ 8,70); de open keuze blijft breakout vs. **TXB0104-IC** rechtstreeks (± € 1,80).
- [ ] **GNSS-antennebundel en aansluiting** — controleer of de gekozen LC29HDA-kit een actieve L1/L5-antenne meelevert en of die past. Losse kandidaat (voorwaardelijk, ± € 15,70): Waveshare GPS External Antenna (D), SKU 25346 (L1+L5, LNA 28±2 dB, SMA-J); boardconnector (SMA/IPEX) en eventuele adapter nog verifiëren. (`2026-10-07`)
- [x] **Barrel-connector** — **Beslissing `2026-10-07`:** een **2,1 mm PCB-barreljack** (Kiwi, € 1,20) op de draagprint, naast de bestaande adapter met schroefklem (kabelzijde).
- [x] **Overige `geen-link`-onderdelen** — `2026-10-06`: gevonden bij EU-winkels: **TME** (LDO AP2112K-3.3TRG1, TVS SMBJ10A, schroefklem, sockets), **Mouser.be/DigiKey** (PTC 1812L200/16), **HESTORE** (schroefklem DEGSON DG250-3.5-04P), **TinyTronics (NL)** (M3-montage).
- [x] **P-MOSFET ompoolbeveiliging: DMG2301L of AO3401A?** — **Beslissing `2026-10-06`: geen van beide — de P-MOSFET vervalt.** Er komt **geen ompoolbeveiliging**; voorkom omgekeerd aansluiten met een **gepolariseerde connector** (XT60/JST-XH). De PTC-zekering en de TVS blijven behouden. Zie [[beslissingen]], [[afgevoerd]] en [[componenten]].
- [x] **Sockets: Preci-Dip of standaard?** — **Beslissing `2026-10-07`:** **standaard 2,54 mm turned-pin (machined) sockets en dual-wipe female headers** uit de hobbyhandel (Mouser/DigiKey/TME); de Preci-Dip is bij TME enkel business/MOQ 380 en valt af. Zie [[bestelbaarheid]].
- [ ] **GPS/RTK-winkel en concrete listing** — `2026-10-07`: AliExpress-item **1005009915138674** (richtprijs ± € 22,19) blijft de referentie; de titel noemt "LC29H", dus **kies de LC29HDA-variant**. Eenduidige alternatieven: **1005010758488281** en **1005010162466640**. Controleer variant (geen LC29HBS), geassembleerd board (geen SMD-module), pinout, antennebundel en checkout. Eckstein/Waveshare (€ 71,39) blijft terugvaloptie. Zie [[gps-rtk-prijzen]].
- [ ] **Footprint/montage LC29HDA-breakout op de draagprint** — Eerst de concrete AliExpress-boardmaat, montagegaten en pinout controleren; daarna kiezen tussen een header op de draagprint of een los subbord aan de rand. De Waveshare-HAT-terugvaloptie is 65 × 30,5 mm met 40-pins header. Bepaalt de footprint en mogelijk AISLER-prijs. Zie [[pcb-ontwerp]], [[bestellijst]] en [[gps-rtk-prijzen]].

## AI-taken (voert de AI later uit)

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`, zie [[componenten]] en [[beslissingen]])

## Nog te beslissen: breakout-footprint en PCB-montage

- [ ] **Past het gekozen LC29HDA-breakout op de draagprint van 100 × 75 mm?** — Nog niet te bepalen voordat de AliExpress-listing en exacte afmetingen bekend zijn. De Waveshare-HAT-terugvaloptie (65 × 30,5 mm) past alleen als verticale strook; eventuele kleinere breakout vraagt om een nieuwe footprint/layout. Bepaalt de bordafmeting en dus de AISLER-prijs. Zie [[bestelschema-pcb]] en [[gps-rtk-prijzen]].
- [x] **Welke sensormodellen zijn definitief: BNO085/BMP581 of BNO055/BMP390?** — **Beslissing `2026-10-07`: BNO085 + BMP581** (zoals de bestellijst). [[componenten]] is bijgewerkt; de oudere BNO055/BMP390 vallen af.
- [ ] **Onderdelenposities op de print vastleggen** — De Blender-mock-up is een **plausibel voorstel**; de echte posities komen pas met de KiCad-layout. Daarna de mock-up bijwerken. (`2026-10-06`)
- [ ] **Gatposities nameten** — Arduino-gaten, servo-flens, paneelgat barrel jack en de exacte BMP581-maat zijn nog niet met de schuifmaat gecontroleerd. Zie [[gstem-hardware-afmetingen]].
- [ ] **Arduino Uno-voeding controleren** — wordt de Uno gevoed via de +5 V-pin van de uitbreidingsconnector of apart? Controleer stroomlimiet, gemeenschappelijke GND en voorkom terugvoeding via USB.
- [ ] **RTCM-correcties naar de rover uitwerken** — valideren hoe NTRIP-correcties vanaf de laptop via USB-adapter en LoRa bij de UART-ingang van de LC29H(DA) komen, inclusief formaat en updatesnelheid.
- [ ] **Aparte servobuck aansluiten** — voedingsbron, uitgangsspanning en stroomcapaciteit afstemmen op de gebruikte servo's.

## Nog te beslissen: documentatie in `documenten/` (`2026-10-06`)

- [ ] **De gebruikershandleiding staat niet (meer) in `documenten/`** — [[handleiding]], [[links]] en [[specificaties]] verwijzen nog naar `documenten/Handleiding-meettoestel.md/.docx`, `documenten/build-handleiding.py` en `documenten/afbeeldingen/`, maar die bestanden zijn bij commit `b16c501` (`2026-10-01`) verwijderd. Opnieuw genereren (bron + script uit git terughalen) of de verwijzingen opruimen? (`2026-10-06`)
- [ ] **`build-ontwerp.py` bestaat niet meer** — `documenten/specificaties/Ontwerp-meetmodule.docx` is ooit met dat script gegenereerd, maar het script staat niet meer in de repo. Wordt Word voortaan handmatig bijgewerkt of halen we het bouwscript terug? (`2026-10-06`)
