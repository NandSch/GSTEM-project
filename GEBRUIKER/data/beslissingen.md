---
tags: [gstem, data, beslissingen]
---

# Beslissingen en keuzes

Chronologisch, nieuwste onderaan. Eén subsectie per beslissing.

<!-- Voorbeeld:
## 2026-09-29 — Voorbeeldbeslissing
- **Beslissing:** ...
- **Reden:** ...
- **Gevolg:** ...
-->

## 2026-09-29 — Geen checksum in CSV-protocol tussen ESP en Arduino
- **Beslissing:** Het CSV-protocol tussen de meetmodule (ESP32-S3) en de voertuig-Arduino gebruikt **geen checksum**. De terminator `\n` is voldoende op een korte seriele kabel binnen hetzelfde voertuig.
- **Reden:** De gebruiker geeft aan dat het voertuigbesturingsdeel een secundaire demonstratie is; de betrouwbaarheid van een korte interne UART-verbinding is voldoende zonder checksum.
- **Gevolg:** Parseren blijft simpel: `Serial.readStringUntil('\n')` gevolgd door `split(',')`. Als in de toekomst de kabel langer of de omgeving ruisiger wordt, kan een checksum alsnog worden toegevoegd zonder de veldstructuur te breken.
- **Link:** [[app-architectuur-besturing]]

## 2026-09-29 — Voertuigbesturing is secundaire demonstratie, geen hoofddoel
- **Beslissing:** Het **hoofddoel** van het project is de **meetmodule zelf** (sensoren, eigen PCB, LoRa-communicatie, laptopapp) plus de **USB-ontvanger**. Het aansturen van een voertuig (vliegtuigmock-up, RC-auto) is een **zijde of demonstratie aan het einde**. Het aantal servo's, het exacte voertuigtype en de besturingslogiek zijn daarom **niet urgent** en mogen later worden vastgelegd.
- **Reden:** De gebruiker bevestigt expliciet dat de module en de ontvanger de kern zijn; de voertuigkoppeling is optioneel/flexibel.
- **Gevolg:** Architectuur en protocol worden ontworpen met een **variabel aantal servo-velden** in de CSV-lijst, zodat het eenvoudig uitbreidbaar is. De veldvolgorde begint met twee placeholders (`servo_roll`, `servo_pitch`) maar kan worden uitgebreid zonder de rest van het protocol te verstoren.
- **Link:** [[app-architectuur-besturing]], [[meetmodule-voorbereiding]]

## 2026-09-29 — Protocol tussen meetmodule en Arduino: CSV over seriele verbinding
- **Beslissing:** De meetmodule (ESP32-S3) en de voertuig-Arduino communiceren via een **vaste CSV-lijst** (kommagescheiden waarden). Elke positie in de lijst staat voor een vast commandoveld (bijv. servo roll, servo pitch, motor links, motor rechts, throttle, modus).
- **Reden:** CSV is leesbaar in de seriele monitor, makkelijk te parsen met `split(',')`, en snel genoeg voor de verwachte updatefrequentie. Geen bibliotheek nodig.
- **Gevolg:** Beide kanten moeten dezelfde veldvolgorde afspreken. Firmware aan beide kanten kan met standaard seriele print/parsen werken.
- **Nog open:** exacte veldvolgorde, buskeuze (UART is de voor de hand liggende keuze bij CSV), en of er een checksum of terminator nodig is.
- **Link:** [[app-architectuur-besturing]], [[besturing-en-commandos]]

## 2026-09-29 — Arduino is aparte voertuigcontroller, ESP32-S3 is doorgeefluik
- **Beslissing:** Het voertuig heeft een **eigen Arduino-microcontroller** die motoren en servo's aanstuurt. De **ESP32-S3 op de meetmodule** fungeert als doorgeefluik: hij ontvangt commando's via LoRa van de laptop en stuurt die via een paar kabels door naar de Arduino.
- **Reden:** De gebruiker geeft expliciet aan dat de Arduino apart op het vliegtuig zit en de ESP alleen doorgeeft. Dit houdt de besturing los van de meetmodule en maakt het makkelijker om bestaande Arduino-servo/motorcode te hergebruiken.
- **Gevolg:** De ESP32-S3 hoeft geen PWM naar servo's te genereren; zijn taak is seriele communicatie met de Arduino. De Arduino bevat de PWM-logica.
- **Link:** [[app-architectuur-besturing]], [[meetmodule-voorbereiding]]

## 2026-09-29 — Frontmatter van de skill gefixt
- **Beslissing:** De `description` in `.pi/skills/gstem-archief/SKILL.md` staat tussen dubbele quotes; de `: ` in de tekst is vervangen door ` — `.
- **Reden:** pi gaf een *Skill conflict*: "Nested mappings are not allowed in compact mappings". Een dubbele punt gevolgd door een spatie in een niet-gequote YAML-waarde start een geneste mapping.
- **Gevolg:** De skill laadt weer zonder fouten. Let op bij toekomstige skills: zet waarden met `: ` altijd tussen quotes.
- **Link:** [[gstem-archief]]

## 2026-10-01 — Handleiding in eenvoudige taal, zonder technische protocolnamen
- **Beslissing:** De gebruikershandleiding (`documenten/Handleiding-meettoestel.md` -> `.docx`) beschrijft alles in **eenvoudige taal**. In de sectie over besturing wordt **niet** vermeld dat het protocol CSV is; er staat dat de gebruiker **zelf een programma schrijft** (of een **voorbereid voorbeeldprogramma** gebruikt) en dat de meetmodule de stuurwaarden doorgeeft aan de controller.
- **Reden:** Gebruikersvraag: de handleiding moet begrijpelijk zijn voor wie de techniek niet kent.
- **Gevolg:** Technische details (CSV, UART, JSON) blijven in [[app-architectuur-besturing]] en [[besturing-en-commandos]]; de handleiding verwijst er niet naar.
- **Link:** [[handleiding]]

## 2026-10-01 — Screenshots en AI-afbeeldingen expliciet aangegeven in de handleiding
- **Beslissing:** Op elke plaats waar beeld nodig is, staat een blok **SCREENSHOT** of **AI-AFBEELDING** met wat er vastgelegd moet worden. De AI maakt zelf geen schermafbeeldingen; de gebruiker voegt ze in.
- **Reden:** Gebruikersvraag: expliciet zeggen wat te screenshotten, en waar een AI-afbeelding (bv. connecties tussen de bordjes) duidelijker is dan een foto.
- **Gevolg:** Lijst met 11 screenshots en 3 AI-afbeeldingen in [[handleiding]].
- **Link:** [[handleiding]]

## 2026-10-01 — Screenshots van de webdemo zelf gegenereerd
- **Beslissing:** De screenshots van de laptopapp worden **automatisch gemaakt** van de webdemo (`GSTEMAPPPREVIEWWEB`) met `documenten/maak-screenshots.py` (Playwright + de Chrome op de pc). Ze staan in `documenten/afbeeldingen/` en worden in de handleiding ingevoegd.
- **Reden:** Gebruikersvraag: zelf schermafbeeldingen maken en gebruiken waar mogelijk.
- **Gevolg:** Schermafbeeldingen 4 t/m 7 en de beelden bij hoofdstuk 5 zijn echte beelden; de foto's van hardware (toestel, USB-ontvanger, controller, testopstelling) blijven `SCREENSHOT`-blokken.
- **Link:** [[handleiding]], [[links]]

## 2026-10-01 — Projectnaam vastgelegd: Positie- en beweging meetmodule met LoRa integratie
- **Beslissing:** De definitieve projectnaam is **Positie- en beweging meetmodule met LoRa integratie**. De werktitel **AeroLink** vervalt.
- **Reden:** Gebruikersvraag: het project noemen naar de naam die eerder al gebruikt werd.
- **Gevolg:** Handleiding en README gebruiken de nieuwe naam; de titelregel van de handleiding volgt de referentie-opmaak (`Handleiding voor ***Positie- en beweging meetmodule met LoRa integratie***`, naam vet-cursief). De mappen `docs/` en `CODEXIMPORT/` zijn voorlopig ongewijzigd gelaten.
- **Link:** [[handleiding]], [[open-vragen]]

## 2026-09-29 — Geen emoji's in chat.md (en het archief)
- **Beslissing:** De logger schrijft koppen als `## Gebruiker · ...` en `## AI · ...` zonder emoji. In de sectie Opmaak van de skill staat nu: geen emoji's in antwoorden of archiefbestanden; gebruik tekstlabels zoals `Let op:` of `Klaar.`.
- **Reden:** Gebruikersvraag: geen emoji's in de sessielogs. AI-antwoorden komen letterlijk in `chat.md` terecht.
- **Gevolg:** Bestaande emoji-koppen in `GEBRUIKER/chat.md` zijn eenmalig opgeruimd. Nieuwe logs zijn emoji-vrij.
- **Gewijzigd:** `.pi/extensions/gstem-logger.ts`, `.pi/skills/gstem-archief/SKILL.md`.
- **Link:** [[gstem-archief]]

## 2026-10-01 — Code-pagina: variabelen als niet-klikbaar overzicht, API met eigen handleidingpagina
- **Beslissing:** De rechterkolom van de pagina **Code** wordt in twee delen gesplitst. Bovenaan een **alleen-lezen variabelenoverzicht** (niet klikbaar, met voorbeeldcode); onderaan een **API-paneel** met status, knoppen om de API aan/uit te zetten en te testen, en een kleine link naar een aparte handleidingspagina. De variabelen worden niet meer gebruikt om in te voegen.
- **Reden:** Gebruikersvraag: het rechterpaneel moet gewoon tonen welke variabelen je kan gebruiken en hoe, zonder invoegknoppen; het onderste deel is voor de API met eigen handleiding en bedieningsknoppen.
- **Gevolg:** `insertAtCursor()` en `data-insert` zijn verwijderd uit `GSTEMAPPPREVIEWWEB/index.html`. Nieuwe pagina `GSTEMAPPPREVIEWWEB/api-handleiding.html`. Upload-info en de knop Uploaden blijven als vaste voettekst.
- **Link:** [[app-architectuur-besturing]], [[handleiding]], [[specificaties]]

## 2026-10-04 — CSV schrijft de gebruiker zelf; API krijgt eigen sectie
- **Beslissing:** De pagina **Code** bevat **geen vaste uitgangsvariabelen** meer (geen `uit.servo1`, `uit.motorLinks`, enz.). De gebruiker schrijft de **CSV-regel zelf in de code**, bijvoorbeeld `Serial.println("15,-5,75,60")`. De **API** voor een extern programma verhuist naar een **eigen navigatie-sectie** `#page-api` met eigen bediening en documentatie; `api-handleiding.html` verwijst nu door naar die sectie.
- **Reden:** Gebruikersvraag: geen vooraf ingestelde servo-/uitgangsvelden meer — de output-CSV hoort in de code. De API moet een eigen sectie en documentatie krijgen.
- **Gevolg:** `index.html`: navigatie uitgebreid met **API**, rechterkolom van Code toont alleen nog **leesvariabelen** plus de groep **Zelf de CSV-regel schrijven**, en er is een nieuwe sectie `#page-api`. De API-downlink is nu een **vrije CSV-regel** in plaats van vaste commando's (`throttle`, `servo_roll`, ...). `api-handleiding.html` is een doorverwijspagina naar `index.html#page-api`.
- **Link:** [[app-architectuur-besturing]], [[specificaties]], [[afgevoerd]]

## 2026-10-04 — A/B-test voor de Code-pagina
- **Beslissing:** We vergelijken twee versies van de Code-pagina naast elkaar: **A** = de huidige versie (`index.html`, code + rechterkolom Variabelen), **B** = een herziene versie (`index-b.html`) in **één kolom** met een korte **uitklapbare hulp**: *Wat kan ik gebruiken?* en *Hoe stuur ik iets?*. De uitklapbare uitleg is **kort** gehouden zodat ze weinig plaats inneemt.
- **Reden:** Gebruikersvraag: een A/B-test met een herziene code-pagina die zeer eenvoudig en niet druk is.
- **Gevolg:** Nieuwe bestanden `GSTEMAPPPREVIEWWEB/index-b.html` en `GSTEMAPPPREVIEWWEB/ab-vergelijken.html` (twee frames naast elkaar). Beide versies laden met `?embed=1` zodat de setup-popup in de frames wegblijft. Versie A blijft ongewijzigd.
- **Link:** [[specificaties]], [[ab-test-code-pagina]]

## 2026-10-04 — Versie B is de officiële Code-pagina
- **Beslissing:** Versie B (Code-pagina in **één kolom** met korte **uitklapbare hulp**) is de **officiële** versie en vervangt `GSTEMAPPPREVIEWWEB/index.html`. De oude tweekoloms Code-pagina en de A/B-testbestanden verdwijnen.
- **Reden:** Gebruikersvraag: maak versie B de nieuwe officiële versie.
- **Gevolg:** `index-b.html` en `ab-vergelijken.html` zijn verwijderd; `index.html` is nu de één-kolomsversie (titel terug naar "GSTEM · Live Tracking", de `?embed`-popup-onderdrukking is verwijderd). Ongebruikte CSS voor de oude rechterkolom (`.code-side`, `.var-*`, `.side-*`, `.upload-*`, `.api-manual-link`) is uit `style.css` gehaald; die ging van ±1477 naar ±1391 regels.
- **Link:** [[specificaties]], [[ab-test-code-pagina]], [[afgevoerd]]

## 2026-10-05 — Ontwerp volledig uitgewerkt in `documenten/`; niet rechtstreeks in Google Docs
- **Beslissing:** De ontwerptekst *Positie- en beweging meetmodule met LoRa integratie* wordt volledig uitgewerkt in het project zelf — `documenten/Ontwerp-meetmodule.md` als bron, `documenten/Ontwerp-meetmodule.docx` als Word-versie via `documenten/build-ontwerp.py`. De inhoud van het Google Doc wordt **niet** rechtstreeks door de AI gewijzigd; de gebruiker plakt of uploadt de tekst zelf in het Doc.
- **Reden:** Er is geen schrijftoegang tot Google Docs (alleen lezen via de publieke link). Bestanden in het project zijn bovendien versioneerbaar en herbouwbaar.
- **Gevolg:** De bron blijft de markdown in `documenten/`. Word opnieuw genereren met `python documenten/build-ontwerp.py`. Het Google Doc loopt achter op de bron tot de tekst wordt overgezet.
- **Link:** [[meetmodule-voorbereiding]], [[links]], [[specificaties]]

## 2026-10-05 — Veiligheidsstop in de firmware van de meetmodule
- **Beslissing:** De veiligheidsstop zit in de **firmware van de meetmodule** en niet alleen in de laptopapplicatie: geen geldig commando binnen de ingestelde tijd -> motoren naar nul en servo's naar neutraal; ongeldige regels negeren en tellen; verbroken verbinding -> de meetmodule gaat zelf naar de veilige toestand; geofencing-schending -> veilige toestand.
- **Reden:** Het toestel moet ook veilig zijn als de laptop of de LoRa-verbinding wegvalt; de module is de enige laag die altijd aanwezig is.
- **Gevolg:** Vastgelegd in `documenten/Ontwerp-meetmodule.md` (sectie Besturing en veiligheid). Blijft open: de omschakeltijd in seconden en de precieze veilige toestand per toesteltype.
- **Link:** [[besturing-en-commandos]], [[meetmodule-voorbereiding]], [[open-vragen]]

## 2026-10-05 — AI-mappen en tussenversies verwijderd na vastleggen in documentatie
- **Beslissing:** `CODEXIMPORT/`, `GSTEMAPPPREVIEWWEB/`, de ziparchieven in `archief/` en de oude `.docx.bak-*`-bestanden in `documenten/` zijn verwijderd. Hun inhoud blijft beschreven in `docs/01`–`docs/04` en in `GEBRUIKER/Projectdocumentatie/`. `docs/` en de Obsidian-kopie `GEBRUIKER/Projectdocumentatie/` worden **identiek** gehouden.
- **Reden:** Gebruikersvraag: de hele map herschikken en ruimte winnen; de documentenmap en de webdemo namen te veel opslag in en waren dubbel met de documentatie.
- **Gevolg:** De map `archief/` is opgeheven. Alles blijft herstelbaar via git-commit `5acdfa0`. README en `docs/05` beschrijven de opgeruimde toestand.
- **Link:** [[links]], [[afgevoerd]], [[specificaties]]
