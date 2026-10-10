---
tags: [gstem, data, open-vragen]
---

# Open vragen

- [x] **Wat moet de definitieve productnaam worden?** — `2026-10-01`: **Positie- en beweging meettoestel met LoRa integratie**. De werktitel *AeroLink* vervalt. (`2026-10-06`: in de naam is *meetmodule* vervangen door *meettoestel*.)
- [x] **Welke IMU wordt het?** — `2026-10-06`: **Adafruit BNO055-breakout** (9-DoF, sensorfusie aan boord, I2C 0x28/0x29). Zie [componenten](componenten.md).
- [ ] **LoRa-pakketformaat en gedrag bij pakketverlies?**
- [ ] **Kaartbron, licentie en offline gebruik voor de 3D-weergave?** — `2026-10-06`: de kaart is een **3D-kaart met Google-satellietfotografie**; licentie en offline gebruik blijven open.
- [ ] **Welke exacte 9-DoF IMU met sensorfusie?** — uit voorbereiding meetmodule.
- [x] **Welke barometer en welke RTK-GNSS-module?** — `2026-10-06`: barometer **Adafruit BMP390** (meest accurate, ±3 Pa, laagste ruis); RTK-GNSS **Quectel LC29H(DA)** (dual-band L1+L5, rover). Zie [componenten](componenten.md) en [beslissingen](beslissingen.md).
- [ ] **Exacte LoRa-frequentie/band en configuratie?** — de gekozen Wio-SX1262 bestaat in 868/915 MHz; voor België is **868 MHz** nodig. Rest van de configuratie nog open. (`2026-10-06`)
- [ ] **Formaat en protocol van datapakketten tussen meetmodule en laptop (uplink en downlink)?** — `2026-10-10`: de besturingsinstructies komen nu uit de besturing-apps (scherm 3/4), niet meer uit gebruikerscode of de API; het LoRa-pakketformaat blijft open.
- [ ] **LoRa downlink: met of zonder ACK, en hoe omgaan met pakketverlies bij besturingscommando's?**
- [ ] **Commandoformaat richting voertuig: wie bepaalt de CSV-velden?** — `2026-10-10`: de besturing-apps bepalen de stuurregels; de exacte velden per voertuigtype (bijv. stuurhoek + gastempo voor de auto) zijn nog niet vastgelegd.
- [x] **Uitbreidingsconnector: PWM, UART, I2C, CAN of analoog?** — `2026-10-06`: **UART via TX/RX**; de Arduino van het vliegtuigje neemt CSV-waarden aan op zijn TX/RX-punten.
- [ ] **Geofencing-grenzen: hoe ingesteld en opgeslagen?**
- [ ] **Batterijspecificatie definitief vastleggen** — voorbereiding noemt 7.4 V 2 A als voorbeeld.
- [ ] **Spanningsregelaar: welke specs en component?**
- [ ] **Heatsink-ontwerp of -keuze voor de ESP32-S3?**
- [x] **PCB-afmetingen en laagcount?** — niet meer van toepassing: eigen draagprint/carrier-PCB vervallen `2026-10-09`. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
- [ ] **Mock-up details: materiaal, servo-type, microcontroller?** — optionele uitbreiding.
- [ ] **Veiligheidsstop-gedrag: welke acties bij verlies van verbinding, en na hoeveel seconden?**
- [ ] **Besturing-apps uitwerken (scherm 3/4)** — drie voertuigtypes/icoontjes; de auto is uitgewerkt (stuur slepen, gaspedaal houden). De twee andere voertuigtypes, hun bedieningselementen en de techniek (webdemo opnieuw bouwen?) staan open. (`2026-10-10`)
- [ ] **Safe-state definitie: neutrale servo's, throttle nul, of ander gedrag per toesteltype?**
- [ ] **Kalman-filter implementatie: welke variant en bibliotheek?**
- [ ] **API-techniek tussen app en extern programma: WebSocket, TCP-socket, HTTP of named pipe?**
- [x] **Bus tussen meetmodule en Arduino: SPI, I2C of UART?** — `2026-09-29`: seriele verbinding (UART) bij CSV-tekstprotocol
- [x] **Protocol tussen meetmodule en Arduino: binair, tekst of iets anders?** — `2026-09-29`: CSV (kommagescheiden waarden), vaste veldvolgorde
- [x] **Checksum of terminator nodig in CSV-protocol tussen ESP en Arduino?** — `2026-09-29`: geen checksum, `\n` als terminator is voldoende
- [ ] **Exacte veldvolgorde en waardeschaal in het CSV-protocol?**
- [x] **Aantal servo's en exact voertuigtype?** — `2026-10-06`: mock-up **vliegtuigje** met **drie besturingsvlakken** (rolroeren, hoogteroer, richtingsroer); de Arduino stelt de servo's in. Een volledig functioneel vliegtuig is niet vereist.
- [ ] **Route en meetgegevens opslaan als bestand, en dat bestand direct openen in de website** — werkpunt, nog niet gebouwd (`2026-10-01`). Genoteerd in [handleiding](handleiding.md).
- [ ] **Handleiding en screenshots bijwerken na herindeling code-pagina** — de handleiding beschrijft nog "variabelen aanklikken als voorbeeld"; in de demo zijn de variabelen nu een niet-klikbaar overzicht, schrijft de gebruiker zelf de CSV-regel en kreeg de API een eigen sectie (`#page-api`). (`2026-10-04`)
- [ ] **API-downlink definitief: vrije CSV-regel of vaste commando's?** — in de demo stuurt het externe programma nu een vrije CSV-regel terug (beslissing `2026-10-04`); de techniek zelf (WebSocket/TCP/HTTP) blijft open. (`2026-10-04`)
- [x] **Welke versie van de Code-pagina wordt de definitieve: A of B?** — `2026-10-04`: **versie B** (één kolom met uitklapbare hulp) is gepromoveerd tot `index.html`; de A/B-testbestanden zijn verwijderd.
- [x] **Waar komen de RTK-correctiegegevens vandaan?** — `2026-10-06`: een **NTRIP-dienst** via de laptop (geen eigen basisstation). Enkel de **provider** (gratis/betaald) blijft nog te kiezen. (`2026-10-05`)
- [ ] **Welke NTRIP-provider en abonnement?** — `2026-10-06`: wordt een **gratis** dienst; de **gebruiker zoekt die zelf**. Vraagt internet op de laptop tijdens het meten. (`2026-10-06`)
- [x] **Welke level shifter voor de UART 3,3 V <-> 5 V?** — de gekozen module is de **TXB0108-breakout**; de extra carrier-PCB is vervallen. De converterfunctie blijft voorlopig behouden, maar handbedrading en montage moeten worden uitgewerkt (`2026-10-09`).
- [x] **Zekering, ompoolbeveiliging en TVS: welke onderdelen?** — `2026-10-06`: **2 A PTC-zekering + TVS SMBJ10A**; de **P-MOSFET-ompoolbeveiliging vervalt** (`2026-10-06`).
- [x] **Is een losse LDO 3,3 V nodig?** — `2026-10-06`: ja, **AP2112K-3.3** voor een eigen 3,3 V-rail. Let op: de LoRa-ontvanger (tweede XIAO) krijgt 3,3 V via USB uit de XIAO zelf. (`2026-10-06`)
- [x] **Exacte uitbreidingsconnector voor de UART?** — `2026-10-06`: **4-pins schroefklem 3,5 mm (KF128/KF301)**, pinout GND/+5 V/TX/RX. (`2026-10-06`)
- [x] **LoRa IPEX -> SMA-pigtail en SMA-bulkhead?** — `2026-10-06`: **nodig**, de antenne wordt buiten het vliegtuigje geconnecteerd; gekozen: IPEX/U.FL -> SMA female bulkhead pigtail. (`2026-10-06`)
- [x] **Welke GNSS-antenne?** — `2026-10-06`: actieve **dual-band L1/L5-antenne met SMA, LNA + ground plane** (compact; voorbeeld Waveshare), passend bij de LC29H(DA). (`2026-10-06`)
- [x] **Welke functies waren voorzien op de draagprint?** — historische lijst: LED, ontkoppeling, bulk-elco, externe connector, level shifter, LDO en voedingsbescherming. Carrier-PCB vervallen `2026-10-09`; elektrische functies voorlopig behouden, uitvoering en montage open. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
- [x] **Op welk spanningsniveau werkt de uitbreidingsconnector?** — `2026-10-06`: de connector voert 5 V-niveau via de **TXB0104**-level shifter; de XIAO-zijde blijft 3,3 V. (`2026-10-05`)

- [ ] **Welke exacte breakout-modellen en bijbehorende pinouts?** — `2026-10-06`: **XIAO ESP32S3 + Wio-SX1262 kit** (rekenkern + LoRa), **Adafruit BNO085** (IMU), **Adafruit BMP581** (barometer) en **Quectel LC29HDA** (RTK-GNSS) zijn gekozen. Enkel de **pinouts** en het **pin-budget** van de XIAO (± 14 I/O) moeten nog genoteerd/gecontroleerd worden. Zie [componenten](componenten.md).
- [x] **Wordt de 7,4 V-accu of de barrel-connector de hoofdvoeding?** — `2026-10-06`: **7,4 V-accu + zekering/ompoolbeveiliging -> buck 5 V -> LDO 3,3 V**. De XIAO wordt op 5 V gevoed; de ingebouwde LiPo-lader wordt niet gebruikt. Zie [componenten](componenten.md) en [beslissingen](beslissingen.md).
- [x] **PCB-ontwerpgereedschap en fabrikant?** — niet meer van toepassing sinds `2026-10-09`: er komt geen eigen draagprint; de eerdere KiCad/AISLER-keuze is vervallen. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
- [x] **Level-shifter-variant?** — `2026-10-07`: **TXB0108-breakout** gekozen. De breakout wordt handbedraad; PCB-montage is vervallen. Zie [bestellijst](bestellijst.md).
- [x] **Exacte bordafmeting en laagopbouw?** — vervallen, want er komt geen eigen draagprint (`2026-10-09`).
- [x] **I2C-pull-ups en spanningsniveaus?** — geen extra pull-ups voorzien op basis van de breakoutmodules; de UART-level-shifter blijft de gekozen TXB0108-breakout. De fysieke bedrading wordt nog uitgewerkt.

- [x] **Socket-headers of een alternatief?** — `2026-10-09`: sockets en eigen draagprint vervallen; breakoutmodules worden met handbedrade en gesoldeerde verbindingen aangesloten en aan een 3D-geprinte behuizing gemonteerd. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
- [x] **Wat komt er precies op de draagprint?** — niet meer van toepassing: de eigen draagprint is vervallen `2026-10-09`. De elektrische functies (LED, ontkoppeling, bulk-elco, voedingsbescherming, LDO, level shifter en externe verbindingen) blijven voorlopig behouden; de bedrade uitvoering en fysieke montage moeten nog worden uitgewerkt. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).

## Nog te beslissen: bestellijst (`2026-10-06`)

- [x] **BMP390 en LC29H(DA) niet op antratek** — BMP581 bij **Kiwi**. Voor LC29H(DA) is de Waveshare-HAT bij Eckstein (€ 71,39) een geverifieerde **terugvaloptie**; voorkeursbron is nu China/AliExpress, listing nog open. Zie [bestellijst](bestellijst.md) en [gps-rtk-prijzen](gps-rtk-prijzen.md).
- [x] **Barometer: beter model dan de BME280** — `2026-10-06`: gebruiker kiest liever een **nauwkeuriger model**; **Kiwi heeft de BMP581 (€ 10,88) op voorraad**. Definitief (`2026-10-07`).
- [ ] **Level shifter** — gekozen TXB0108-breakout bij Kiwi (€ 8,70); de open keuze blijft breakout vs. **TXB0104-IC** rechtstreeks (± € 1,80).
- [ ] **GNSS-antennebundel en aansluiting** — controleer of de gekozen LC29HDA-kit een actieve L1/L5-antenne meelevert en of die past. Losse kandidaat (voorwaardelijk, ± € 15,70): Waveshare GPS External Antenna (D), SKU 25346 (L1+L5, LNA 28±2 dB, SMA-J); boardconnector (SMA/IPEX) en eventuele adapter nog verifiëren. (`2026-10-07`)
- [x] **PCB-barreljack** — vervallen als PCB-onderdeel `2026-10-09`; de bestaande barrel-adapter blijft in bezit. De wijze waarop de voedingsinvoer door/aan de behuizing komt, staat open.
- [x] **Eerdere leveranciers voor overige onderdelen** — historisch gevonden: TME/Mouser/DigiKey voor elektronica; HESTORE voor schroefklem; TinyTronics voor de PCB-M3-set. De schroefklem en montagehardware zijn niet langer actieve bestellingen totdat de bedrade uitvoering is bepaald.
- [x] **P-MOSFET ompoolbeveiliging: DMG2301L of AO3401A?** — **Beslissing `2026-10-06`: geen van beide — de P-MOSFET vervalt.** Er komt **geen ompoolbeveiliging**; voorkom omgekeerd aansluiten met een **gepolariseerde connector** (XT60/JST-XH). De PTC-zekering en de TVS blijven behouden. Zie [beslissingen](beslissingen.md), [afgevoerd](afgevoerd.md) en [componenten](componenten.md).
- [x] **Sockets: Preci-Dip of standaard?** — vervallen `2026-10-09`: er komen geen sockets of eigen draagprint. De eerdere socketkeuze is historisch en wordt niet besteld.
- [ ] **GPS/RTK-winkel en concrete listing** — `2026-10-07`: AliExpress-item **1005009915138674** (richtprijs ± € 22,19) blijft de referentie; de titel noemt "LC29H", dus **kies de LC29HDA-variant**. Eenduidige alternatieven: **1005010758488281** en **1005010162466640**. Controleer variant (geen LC29HBS), geassembleerd board (geen SMD-module), pinout, antennebundel en checkout. Eckstein/Waveshare (€ 71,39) blijft terugvaloptie. Zie [gps-rtk-prijzen](gps-rtk-prijzen.md).
- [ ] **Montage van de breakoutmodules in de behuizing** — bepaal hoe boards zonder geschikte montagegaten, waaronder mogelijk de LC29HDA-breakout, vastgezet worden. Controleer de fysieke maten en pinout zodra de gekozen listing vaststaat. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md) en [gps-rtk-prijzen](gps-rtk-prijzen.md).

## AI-taken (voert de AI later uit)

- [ ] **Pinout-tabel XIAO opstellen** en controleren of ± 14 I/O volstaat voor IMU + barometer + GNSS + UART; anders I2C-multiplexer/expander voorzien. (`2026-10-06`, zie [componenten](componenten.md) en [beslissingen](beslissingen.md))

## Nog te beslissen: behuizingsmontage en bevestiging

- [x] **Past het gekozen LC29HDA-breakout op de draagprint?** — niet meer van toepassing, want de carrier-PCB is vervallen. Boardafmetingen en bevestigingsmogelijkheden blijven wel nodig voor montage in de behuizing; zie [bedrading-en-behuizing](bedrading-en-behuizing.md) en [gps-rtk-prijzen](gps-rtk-prijzen.md).
- [x] **Welke sensormodellen zijn definitief: BNO085/BMP581 of BNO055/BMP390?** — **Beslissing `2026-10-07`: BNO085 + BMP581** (zoals de bestellijst). [componenten](componenten.md) is bijgewerkt; de oudere BNO055/BMP390 vallen af.
- [ ] **Indeling en bevestiging in de 3D-geprinte behuizing vastleggen** — plaats breakoutmodules, losse componenten en bedrading zonder draagprint; houd rekening met antennes, warmte en de barometeropening. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
- [ ] **Montagematen controleren** — Arduino-gaten, servo-flens, eventuele voedings-/antenne-doorvoeren en de afmetingen van de breakoutmodules moeten voor de behuizing worden gecontroleerd. Zie [gstem-hardware-afmetingen](gstem-hardware-afmetingen.md).
- [ ] **Arduino Uno-voeding controleren** — wordt de Uno gevoed via de +5 V-pin van de uitbreidingsconnector of apart? Controleer stroomlimiet, gemeenschappelijke GND en voorkom terugvoeding via USB.
- [ ] **RTCM-correcties naar de rover uitwerken** — valideren hoe NTRIP-correcties vanaf de laptop via USB-adapter en LoRa bij de UART-ingang van de LC29H(DA) komen, inclusief formaat en updatesnelheid.
- [ ] **Aparte servobuck aansluiten** — voedingsbron, uitgangsspanning en stroomcapaciteit afstemmen op de gebruikte servo's.

## Nog te beslissen: bedrading en behuizing (`2026-10-09`)

- [ ] **Montagemethode voor modules en losse onderdelen** — bevestiging aan de 3D-geprinte behuizing; bepaal of montagemateriaal nodig is. De eerder gekozen M3-set was voor de draagprint en wordt niet besteld zolang de nieuwe montage niet duidelijk is.
- [ ] **Voedingsonderdelen handmatig verbinden en ondersteunen** — bevestig of PTC, TVS en AP2112K in de gekozen uitvoering behouden blijven en hoe ze zonder draagprint mechanisch worden vastgezet.
- [ ] **Externe voeding en UART-aansluiting** — de PCB-barreljack is vervallen; bepaal of de bestaande barrel-adapter en de eerder gekozen vierpolige schroefklem rechtstreeks worden bedraad of een andere behuizingsdoorvoer nodig hebben.
- [ ] **Draad en printmateriaal** — nagaan of de aanwezige Dupont-/siliconendraad volstaat voor de bedrading en of er geschikt filament beschikbaar is; nog niets toevoegen of online opzoeken.

## Nog te beslissen: documentatie in `documenten/` (`2026-10-06`)

- [ ] **De gebruikershandleiding staat niet (meer) in `documenten/`** — [handleiding](handleiding.md), [links](links.md) en [specificaties](specificaties.md) verwijzen nog naar `documenten/Handleiding-meettoestel.md/.docx`, `documenten/build-handleiding.py` en `documenten/afbeeldingen/`, maar die bestanden zijn bij commit `b16c501` (`2026-10-01`) verwijderd. Opnieuw genereren (bron + script uit git terughalen) of de verwijzingen opruimen? (`2026-10-06`)
- [ ] **Word-versie van het ontwerp synchroniseren** — de actuele bron `documenten/specificaties/Ontwerp-meetmodule.md` is bijgewerkt met de handbedrade aanpak. `Ontwerp-meetmodule.docx` is een oudere versie; `build-ontwerp.py` ontbreekt. Bepaal of Word handmatig wordt bijgewerkt of dat het bouwscript wordt teruggehaald. (`2026-10-09`)
