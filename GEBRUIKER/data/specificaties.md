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
- **Specificatie:** De titelregel van de handleiding staat in de body (Calibri 13) als `Handleiding voor ***Positie- en beweging meetmodule met LoRa integratie***`, met de projectnaam **vet-cursief** — gelijk aan de titelregel van `GStem-Specificaties (1).docx`. Schermafbeeldingen van de webdemo worden met `documenten/maak-screenshots.py` gegenereerd in `documenten/afbeeldingen/` en in de markdown ingevoegd met `![onderschrift](afbeeldingen/bestand.png)`; de build zet ze gecentreerd met een cursief onderschrift.
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
- **Specificatie:** Nog geen harde specificaties. Een uitgebreide voorbereiding is vastgelegd in [[meetmodule-voorbereiding|Positie- en beweging meetmodule met LoRa — voorbereiding]].
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
- **Specificatie:** Het Google Doc *Ontwerp voor Positie- en beweging meetmodule met LoRa integratie* is de formele, in lopende tekst geschreven ontwerpbeschrijving van het systeem, met de delen **Hardware Specificaties** (meetmodule: eigen PCB met vervangbare breakout-modules en bevestigingspunten in de hoeken; ESP32-S3 met LoRa en antenne plus heatsink; 9-DoF IMU; barometer; RTK-GNSS met antenne; voeding via externe batterij zoals 7,4 V of barrel-connector met spanningsregelaar; extra pinnen en grounds voor het besturingssysteem van een mockup-vliegtuigje; zelf ontworpen 3D-geprinte dempende behuizing; LoRa-adapter als tweede ESP aan de laptop via USB) en **Software Specificaties** (continu uitlezen van IMU, barometer en RTK-GNSS; samenvoegen tot datapakketten; sensorfusie met een Kalman-filter; verzending via LoRa en USB-doorgifte naar de laptop; errorhandling bij wegvallende GPS of uitvallende sensoren; grenzen die waarschuwen buiten een bepaald gebied).
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
