---
tags: [gstem, data, specificaties]
---

# Specificaties

Technische en functionele afspraken. Eén subsectie per specificatie.

<!-- Voorbeeld:
## 2026-09-29 — Onderdeel
- **Specificatie:** ...
- **Status:** voorlopig / vastgelegd
- **Bron:** ...
-->

## 2026-10-01 — Indeling rechterkolom code-pagina: variabelen en API gescheiden
- **Specificatie:** De rechterkolom van de pagina **Code** (`#page-code` in `GSTEMAPPPREVIEWWEB/index.html`) bestaat uit twee delen:
  1. **Bovenaan — Variabelen (alleen-lezen overzicht).** Twee groepen: "Variabelen die je kan gebruiken" (ingangen, lezen) en "Variabelen die je moet instellen" (uitgangen, schrijven). Elk item toont naam, type/eenheid en omschrijving. De items zijn **niet klikbaar** en voegen niets in; onder elke groep staat een **voorbeeldcodeblok** dat toont hoe de variabelen gebruikt worden.
  2. **Onderaan — API.** Statusindicator, knoppen **API aanzetten/uitzetten** en **Verbinding testen**, en een kleine link **Handleiding API ->** die de aparte pagina `api-handleiding.html` opent.
  De upload-info en de knop **Uploaden** blijven als vaste voettekst onderaan.
- **Status:** doorgevoerd (demo)
- **Bron:** gebruikersvraag; `GSTEMAPPPREVIEWWEB/index.html`, `GSTEMAPPPREVIEWWEB/style.css`, `GSTEMAPPPREVIEWWEB/api-handleiding.html`
- **Gevolg:** Variabelen zijn niet langer invoegknoppen. De API-handleiding is een nieuwe losse pagina.

## 2026-10-01 — Titel en screenshots van de handleiding
- **Specificatie:** De titelregel van de handleiding staat in de body (Calibri 13) als `Handleiding voor ***Positie- en beweging meettoestel met LoRa integratie***`, met de projectnaam **vet-cursief** — gelijk aan de titelregel van `GStem-Specificaties (1).docx`. Schermafbeeldingen van de webdemo worden met `documenten/maak-screenshots.py` gegenereerd in `documenten/afbeeldingen/` en in de markdown ingevoegd met `![onderschrift](afbeeldingen/bestand.png)`; de build zet ze gecentreerd met een cursief onderschrift.
- **Status:** doorgevoerd
- **Bron:** `documenten/build-handleiding.py`, `documenten/Handleiding-meettoestel.md`, `documenten/maak-screenshots.py`
- **Gevolg:** Zelfgemaakte beelden voor de setup, het kaartscherm, de meetwaarden, het codescherm, de variabelen, de API en de uploadknop. Hardwarefoto's blijven open `SCREENSHOT`-blokken.

## 2026-10-01 — Opmaak handleiding volgt GStem-Specificaties
- **Specificatie:** De gegenereerde handleiding krijgt dezelfde opmaakstijl als het bestaande document `GStem-Specificaties (1).docx`: body Calibri 12, secties (`##`) als Heading 1 (Calibri 17, vet, cursief, zwart) en tussenkoppen (`###`) als Subtitle (Calibri 13, vet, cursief, zwart). Kernwoorden worden met **vet** uitgelicht. Hoofdstuk 5 is dieper uitgewerkt in die stijl.
- **Status:** doorgevoerd
- **Bron:** `documenten/build-handleiding.py` + `documenten/Handleiding-meettoestel.md`
- **Gevolg:** De Word-versie wordt opnieuw gegenereerd met `python documenten/build-handleiding.py`.

## 2026-10-01 — Handleiding krijgt hoofdstuk "Meer in detail"
- **Specificatie:** De handleiding bevat een extra hoofdstuk "Meer in detail" met korte subsecties: wat de knop Uploaden doet, variabelen aanklikken als voorbeeld, wat de app zelf doet, en de API voor een eigen programma buiten de app. De API-sectie is bewust kort en algemeen: app stuurt meetgegevens (JSON) naar een eigen programma op de computer, dat programma stuurt stuurwaarden terug, en de app stuurt die verder naar het toestel. Exacte techniek (WebSocket/TCP/HTTP/named pipe) blijft open.
- **Status:** concept
- **Bron:** `documenten/Handleiding-meettoestel.md`
- **Gevolg:** Hoofdstuknummers 5 t/m 13 zijn opgeschoven naar 6 t/m 14.

## 2026-10-01 — Opbouw van de gebruikershandleiding
- **Specificatie:** De handleiding volgt de opstartketen van het toestel en heeft 13 secties: inleiding/data, aanzetten en verbinden, kaart + live data, codescherm, data doorgeven aan eigen programma, koppeling met voertuigcontroller, veiligheid, gegevens bewaren, startchecklist, probleemoplossing, technische gegevens, woordenlijst en extra onderdelen.
- **Status:** concept
- **Bron:** `documenten/Handleiding-meettoestel.md`
- **Gevolg:** Word-versie via `python documenten/build-handleiding.py`.

## 2026-09-29 — Meetmodule: voorbereiding vastgelegd als denkrichting
- **Specificatie:** Nog geen harde specificaties. Een uitgebreide voorbereiding is vastgelegd in [[meetmodule-voorbereiding|Positie- en beweging meettoestel met LoRa — voorbereiding]].
- **Status:** voorbereiding / denkwijze
- **Bron:** gebruikersinput projectvoorbereiding
- **Samenvatting:** Hardware (ESP32-S3, LoRa, IMU, barometer, RTK-GNSS, eigen PCB, 3D-geprinte behuizing), software (sensorfusie, laptopapp met kaart en programmeermodus, veiligheidsstop, git-versiebeheer) en optionele mock-up-uitbreiding.

## 2026-10-04 — Code-pagina: eigen CSV-output; API als aparte sectie
- **Specificatie:** In de webdemo (`GSTEMAPPPREVIEWWEB/index.html`):
  1. De navigatie (`.island-nav`) heeft drie knoppen: **Kaart**, **Code** en **API** (`#page-kaart`, `#page-code`, `#page-api`).
  2. De rechterkolom van **Code** toont alleen nog **leesvariabelen** (`meting.*`) en de groep **Zelf de CSV-regel schrijven**: de gebruiker kiest zelf de velden en print een kommagescheiden regel met `Serial.println(...)`. Er zijn **geen vaste uitgangsvariabelen** meer.
  3. De **API-sectie** (`#page-api`) bundelt de bediening (status, **API aanzetten/uitzetten**, **Verbinding testen**, endpoint `ws://localhost:9001`) en de documentatie (werking, verbinding, uplink-JSON, downlink-CSV, snelstart). De downlink is een **vrije CSV-regel**, niet een vaste commandolijst.
  4. `api-handleiding.html` is een doorverwijspagina naar `index.html#page-api`.
- **Status:** doorgevoerd (demo)
- **Bron:** gebruikersvraag; `GSTEMAPPPREVIEWWEB/index.html`, `GSTEMAPPPREVIEWWEB/style.css`, `GSTEMAPPPREVIEWWEB/api-handleiding.html`
- **Gevolg:** `STARTER_CODE` en `uploadCode()` in `index.html` zijn aangepast; de upload-info toont **CSV met eigen velden**.

## 2026-10-04 — Versie B: Code-pagina in één kolom
- **Specificatie:** `GSTEMAPPPREVIEWWEB/index.html` toont de Code-pagina als **één gecentreerde kolom** (max. 1060 px):
  1. Het codevenster met in de titelbalk de **Uploaden**-knop en de hint `Ctrl`+`Enter`.
  2. Daaronder twee **uitklapbare hulpblokken** (standaard dicht): **Wat kan ik gebruiken?** (compacte lijst van `meting.*` met eenheid in twee kolommen) en **Hoe stuur ik iets?** (`Serial.println("15,-5,75,60")` + één regel uitleg).
  De startcode is minimaal (11 regels). Kaart- en API-pagina zijn gelijk aan versie A.
- **Status:** definitief — gepromoveerd tot `GSTEMAPPPREVIEWWEB/index.html` (`2026-10-04`); `index-b.html` en `ab-vergelijken.html` zijn verwijderd.
- **Bron:** gebruikersvraag; `GSTEMAPPPREVIEWWEB/index.html`, `GSTEMAPPPREVIEWWEB/style.css`
- **Vergelijken:** de A/B-test is afgerond; versie B is nu `index.html` en de vergelijkingspagina is verwijderd (`2026-10-04`).
- **Aanvulling `2026-10-04`:** De **Uploaden**-knop in versie B krijgt expliciet `appearance: none` (geen native browseropmaak) en de stylesheet wordt met `style.css?v=3` geladen om cacheproblemen te vermijden. Hetzelfde geldt voor `.popup-btn` en `.api-btn`.

## 2026-10-05 — Ontwerptekst meetmodule vastgelegd als formele ontwerpbeschrijving
- **Specificatie:** Het Google Doc *Ontwerp voor Positie- en beweging meettoestel met LoRa integratie* is de formele, in lopende tekst geschreven ontwerpbeschrijving van het systeem, met de delen **Hardware Specificaties** (meetmodule: eigen PCB met vervangbare breakout-modules en bevestigingspunten in de hoeken; ESP32-S3 met LoRa en antenne plus heatsink; 9-DoF IMU; barometer; RTK-GNSS met antenne; voeding via externe batterij zoals 7,4 V of barrel-connector met spanningsregelaar; extra pinnen en grounds voor het besturingssysteem van een mockup-vliegtuigje; zelf ontworpen 3D-geprinte dempende behuizing; LoRa-adapter als tweede ESP aan de laptop via USB) en **Software Specificaties** (continu uitlezen van IMU, barometer en RTK-GNSS; samenvoegen tot datapakketten; sensorfusie met een Kalman-filter; verzending via LoRa en USB-doorgifte naar de laptop; errorhandling bij wegvallende GPS of uitvallende sensoren; grenzen die waarschuwen buiten een bepaald gebied).
- **Status:** concept — ontwerptekst, geen harde specificaties. Waarden zoals accuspanning, pakketformaat en exacte onderdelen blijven open.
- **Bron:** Google Doc (openbaar gedeeld `2026-10-05`) — zie [[links]]. Inhoudelijke toelichting en verhouding tot de voorbereiding in [[meetmodule-voorbereiding]].
- **Gevolg:** De eerdere denkrichting wordt bevestigd; het Doc mist de app-schermopbouw, programmeermodus, live export, data-opslag, git-versiebeheer en testaanpak die wel in [[meetmodule-voorbereiding]] staan.

## 2026-10-05 — Ontwerptekst volledig uitgewerkt (hardware, firmware, communicatie, applicatie)
- **Specificatie:** De ontwerptekst is volledig uitgewerkt in `documenten/Ontwerp-meetmodule.md` en `documenten/Ontwerp-meetmodule.docx` (bron respectievelijk build via `documenten/build-ontwerp.py`). Toegevoegd ten opzichte van het Google Doc:
  1. **Hardware:** socket-headers voor vervangbare breakout-modules; voedingsrails (accu, 5 V, 3,3 V) en ground per rail; ground plane en antenne-plaatsing tegen storing op IMU en barometer; tabel met componenten en hun status; warmte van de ESP weg van de barometer; accu -> buck naar 5 V -> 3,3 V; uitbreidingsconnector met voeding, gemeenschappelijke ground en vrije UART-pinnen; CSV over UART als vastgelegd protocol naar de voertuigcontroller (geen checksum, regeleinde als terminator); 3D-print in PETG/PLA op rubberen dempingsbussen; adapter als zuiver doorgeefluik met USB-naar-serieel-omzetter.
  2. **Firmware en data:** uitleesfrequentie per sensor en tijdstempel per pakket; veldenlijst van het datapakket (positie, hoogte, snelheid, richting en hoeken, plus status- en kwaliteitsgegevens); Kalman-filter voor oriëntatie en voor de combinatie barometer/GNSS.
  3. **Communicatie:** de uplink- en downlinkketen stap per stap; de laptopapplicatie met startscherm (USB en geldige pakketten apart gecontroleerd), hoofdscherm met kaart en meetwaarden, en de drie modi Kaart, Code en API; de API stuurt meetgegevens als JSON naar een eigen programma en ontvangt een vrije kommagescheiden regel terug.
  4. **Besturing en veiligheid:** failsafe-tabel met veilige toestand in de **firmware van de meetmodule** (zie [[beslissingen]]), geofencing-waarschuwing en het gebruik van de sensorfusie bij een wegvallende GNSS-verbinding.
  5. **Versiebeheer en testen:** git-project voor alle software; testplan in vijf stappen (sensoren apart, kalibratie, communicatie en bereik, veiligheid, veldtest).
- **Status:** concept — uitgewerkte ontwerptekst; alle waarden die nog niet gekozen zijn, staan in een blok *Nog te bepalen* en in de slottabel *Overzicht van de nog te bepalen punten*.
- **Bron:** gebruikersvraag `2026-10-05` ("vul het Google Doc aan"); `documenten/Ontwerp-meetmodule.md`.
- **Gevolg:** De ontbrekende onderdelen zijn nu vastgelegd in een versioneerbaar bestand. Het Google Doc loopt achter tot de tekst wordt overgezet. Nieuwe open vragen: RTK-correctiebron en spanningsniveau van de uitbreidingsconnector ([[open-vragen]]).

## 2026-10-06 — Afgewerkte gebruikersspecificaties vastgelegd
- **Specificatie:** De door de gebruiker afgewerkte specificaties (`documenten/GStem-Specificaties.md`, aangeleverd `2026-10-06`) leggen het product gebruikersgericht vast. Kern:
  1. **Doel:** klein meettoestel op een bewegend voertuig of apparaat (vliegtuig, bootje, autootje).
  2. **Meetprestaties:** vier grootheden — **richting** (graden, horizontaal en verticaal vlak), **snelheid** (km/u), **hoogte** (nauwkeurig tot **1,5 m**), **locatie** (nauwkeurig tot **0,5 m**).
  3. **Ontvanger en bereik:** een kleine draadloze ontvanger in de vorm van een **USB-stick**; **bereik max. 4 km**.
  4. **Aanzetten:** het meettoestel start **automatisch** mee met het voertuig (LED toont actief); de laptopapplicatie **start vanzelf** zodra de USB-ontvanger wordt ingestoken.
  5. **App-schermen:** scherm 1 verbindingscontrole met **OK**; scherm 2 **3D-kaart met Google-satellietfoto's** (afgelegde weg + kijkrichting) plus **tabel** met losse meetwaarden; scherm **Code** (editor + rechtervensters met uitleg en variabelen, CSV terug naar de controller, uploadknop); scherm **API** (aan/uit, verbinding testen, adres, uitleg links). Op **elk** scherm staat de status van USB-ontvanger en meettoestel.
  6. **CSV:** alle waarden naar de controller reizen als **comma separated values**; de gebruiker bepaalt zelf de betekenis van elke waarde en kan variabelen benoemen.
  7. **API:** geeft alle metingen door aan een **extern programma**, dat waarden op zijn eigen manier gebruikt en **instructies terugstuurt** (zelfde weg als het codeerscherm).
  8. **RC-vliegtuig-mock-up:** een **Arduino** neemt CSV-waarden aan en is via **TX/RX** met het meettoestel verbonden; het meettoestel moet met zijn **voorkant gelijk** aan die van het vliegtuigje worden gericht; de **besturingsvlakken rolroeren, hoogteroer en richtingsroer** reageren op de metingen; de Arduino stelt de **servo's** in (real-time). Dit is een **zittend voorbeeld**, geen volledig functioneel vliegtuig.
  9. **Testen:** **kalibratie** (kantelen en 3D-visualisatie/live data vergelijken) en **feedbacklus** (testcode stuurt stuursignaal terug, controleer de Arduino-actie).
- **Status:** afgewerkt — gebruikersspecificatie; technische keuzes (IMU, barometer, frequentie, exacte veldvolgorde) blijven in [[open-vragen]].
- **Bron:** gebruikersaanlevering `2026-10-06`; `documenten/GStem-Specificaties.md`. Samenvatting in [[gstem-specificaties]].
- **Gevolg:** de mock-up heeft nu **drie** besturingsvlakken (rolroer, hoogteroer, richtingsroer) en de verbinding meettoestel ↔ Arduino is **UART via TX/RX** (was open). Zie [[beslissingen]].

## 2026-10-06 — Draagprint-aanpak: breakout-modules op socket-headers
- **Specificatie:** De zelfontworpen PCB is een **draagprint (carrier)**. Alle functionele componenten worden als **kant-en-klare breakout-modules aangekocht** (ESP32-S3, LoRa, 9-DoF IMU, barometer, RTK-GNSS) en op **socket-headers (vrouwelijke 2,54 mm)** geplaatst. De draagprint levert de **verbindingen, voeding en status**; de modules leveren de functie.
- **Elektrisch:** voedingsingang via accu (7,4 V) of barrel-connector, met zekering en beveiliging tegen omgekeerde polariteit; **buck-converter naar 5 V** en **LDO naar 3,3 V**; **power-LED met serieweerstand** op de geregelde rail; decoupling (100 nF per module + bulk per rail). Datapaden: **I2C** naar IMU en barometer (met pull-ups), **UART** naar GNSS en uitbreidingsconnector, **level shifter** naar een eventuele 5 V-controller. Optioneel reset-/bootknop voor de ESP.
- **Layout:** 2-laags met ground plane op de onderlaag; aparte rails `VBAT`/`5V`/`3V3`/`GND`; I2C kort en weg van de antenne; antenne-keep-out voor LoRa en GNSS; buck-spoel weg van IMU en barometer; 4 bevestigingsgaten (M3) in de hoeken.
- **Status:** aanpak bevestigd; exacte modulekeuzes, pinouts, regelaars en het ontwerpgereedschap blijven open ([[open-vragen]]).
- **Bron:** gebruikersvraag `2026-10-06`; sluit aan op `documenten/Ontwerp-meetmodule.md` (secties De Meetmodule, Elektronische Componenten, Voeding en Interface).
- **Gevolg:** de **power-LED op de print** is nu expliciet als ontwerpelement vastgelegd (naast het "LED-lampje toont actief" uit de afgewerkte specificaties).

## 2026-10-06 — Heroverweging socket-headers: alternatieven verkend
- **Specificatie:** De aanpak met **strip-socket-headers** (zie draagprint-aanpak) wordt heroverwogen omdat die amateuristisch oogt. Verkende alternatieven:
  1. **Precisie-/gefreesde sockets (machined turned-pin):** zelfde modulariteit, laag profiel, ronde gouden contacten, ziet professioneel uit. Goedkoopste upgrade.
  2. **Direct vastsolderen** van de breakout op mannelijke pinheaders: steviger, geen losraken; vervangen = desolderen.
  3. **Castellated modules** (kale SMD-modules zoals ESP32-S3-WROOM-1, RFM95W, u-blox ZED-F9P, BME280) vlak op de PCB: laagste profiel, beste RF, meest afgewerkt; verliest verwisselbaarheid.
  4. **Board-to-board / mezzanine-connectoren** (DF40, Samtec, Hirose DF): solide en professioneel; vereist een matching connector op module of eigen dragerprint.
  5. **Sub-bordjes met JST-GH/Molex-kabels:** modulair en professioneel; meer onderdelen en bekabeling.
  6. **Pogo pins:** enkel voor testfixtures, niet permanent.
- **Afweging:** precisie-sockets = snel professioneel + vervangbaar; direct solderen = beste bij trillingen (vliegtuigje); castellated = meest afgewerkt eindproduct.
- **Status:** in heroverweging — nog niet beslist.
- **Bron:** gebruikersvraag `2026-10-06`.
- **Gevolg:** de keuze staat open in [[open-vragen]]; de [[pcb-schets]] toont nog de strip-sockets en wordt aangepast zodra de keuze valt.

## 2026-10-06 — PCB-ontwerp: gereedschap en gatmaten vastgelegd als werkwijze
- **Specificatie:** De draagprint wordt ontworpen met **KiCad 8/9** (gratis, open source); **EasyEDA** is het alternatief als er toch bij JLCPCB/LCSC besteld wordt. Bestelling bij **JLCPCB/PCBWay** (2-laags, 5 stuks, Gerbers + drill files). Elke breakout-module wordt als **connector op 2,54 mm-raster** (`Connector_PinSocket_2.54mm`) ingevoerd, met silkscreen-omtrek per module en `MountingHole`-footprints voor de bevestiging. Gatmaten: pinheader 2,54 mm = 1,0 mm gat / 1,7-1,8 mm pad; JST-GH = 0,8 mm; M3 = 3,2 mm; M3 heat-set = 4,0-4,5 mm; M2,5 = 2,7 mm; M2 = 2,2 mm. Afmetingen komen uit de datasheet/mechanische tekening van de module, uit deze standaardmaten, en anders uit eigen nameting met een schuifmaat. **Controle:** layout 1:1 op papier printen en de echte modules erop leggen.
- **Status:** werkwijze aanbevolen; app- en fabrikantkeuze nog te bevestigen.
- **Bron:** gebruikersvraag `2026-10-06`; uitgewerkt in [[pcb-ontwerp]].
- **Gevolg:** de open vraag over het ontwerpgereedschap heeft nu een concreet advies; de fabrikant en de exacte module-footprints blijven te bevestigen.

## 2026-10-06 — Componentenkeuze en gevolgen voor de print
- **Specificatie:** Als **rekenkern + LoRa** is de **XIAO ESP32S3 + Wio-SX1262 kit** gekozen (B2B-connector, SPI, IPEX-antenne, USB-C, LiPo-lader, ± 14 I/O). Als **9-DoF IMU** de **Adafruit BNO055-breakout** (I2C 0x28/0x29, 20x27x4 mm, montagegaten 20x12 mm). De gebruiker koopt alles zelf; enkel de print wordt gemaakt (met LED + sockets).
- **Status:** gekozen; gevolgen deels open.
- **Bron:** gebruikersaanwijzing `2026-10-06`; volledige werklijst in [[componenten]].
- **Gevolg:** ESP32 + LoRa = één footprint; de **LiPo-laadoptie** kan de 7,4 V-voedingsketen overbodig maken; **pin-budget** en **voedingsroute** te controleren. Barometer en RTK-GNSS blijven te kiezen; ontbrekende onderdelen (antennes, aan/uit-schakelaar, standoffs, USB-C-kabel, servo-voeding) staan in [[componenten]].
