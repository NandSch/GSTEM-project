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
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md)

## 2026-09-29 — Voertuigbesturing is secundaire demonstratie, geen hoofddoel
- **Beslissing:** Het **hoofddoel** van het project is de **meetmodule zelf** (sensoren, eigen PCB, LoRa-communicatie, laptopapp) plus de **USB-ontvanger**. Het aansturen van een voertuig (vliegtuigmock-up, RC-auto) is een **zijde of demonstratie aan het einde**. Het aantal servo's, het exacte voertuigtype en de besturingslogiek zijn daarom **niet urgent** en mogen later worden vastgelegd.
- **Reden:** De gebruiker bevestigt expliciet dat de module en de ontvanger de kern zijn; de voertuigkoppeling is optioneel/flexibel.
- **Gevolg:** Architectuur en protocol worden ontworpen met een **variabel aantal servo-velden** in de CSV-lijst, zodat het eenvoudig uitbreidbaar is. De veldvolgorde begint met twee placeholders (`servo_roll`, `servo_pitch`) maar kan worden uitgebreid zonder de rest van het protocol te verstoren.
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md)

## 2026-09-29 — Protocol tussen meetmodule en Arduino: CSV over seriele verbinding
- **Beslissing:** De meetmodule (ESP32-S3) en de voertuig-Arduino communiceren via een **vaste CSV-lijst** (kommagescheiden waarden). Elke positie in de lijst staat voor een vast commandoveld (bijv. servo roll, servo pitch, motor links, motor rechts, throttle, modus).
- **Reden:** CSV is leesbaar in de seriele monitor, makkelijk te parsen met `split(',')`, en snel genoeg voor de verwachte updatefrequentie. Geen bibliotheek nodig.
- **Gevolg:** Beide kanten moeten dezelfde veldvolgorde afspreken. Firmware aan beide kanten kan met standaard seriele print/parsen werken.
- **Nog open:** exacte veldvolgorde, buskeuze (UART is de voor de hand liggende keuze bij CSV), en of er een checksum of terminator nodig is.
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md), [besturing-en-commandos](besturing-en-commandos.md)

## 2026-09-29 — Arduino is aparte voertuigcontroller, ESP32-S3 is doorgeefluik
- **Beslissing:** Het voertuig heeft een **eigen Arduino-microcontroller** die motoren en servo's aanstuurt. De **ESP32-S3 op de meetmodule** fungeert als doorgeefluik: hij ontvangt commando's via LoRa van de laptop en stuurt die via een paar kabels door naar de Arduino.
- **Reden:** De gebruiker geeft expliciet aan dat de Arduino apart op het vliegtuig zit en de ESP alleen doorgeeft. Dit houdt de besturing los van de meetmodule en maakt het makkelijker om bestaande Arduino-servo/motorcode te hergebruiken.
- **Gevolg:** De ESP32-S3 hoeft geen PWM naar servo's te genereren; zijn taak is seriele communicatie met de Arduino. De Arduino bevat de PWM-logica.
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md)

## 2026-09-29 — Frontmatter van de skill gefixt
- **Beslissing:** De `description` in `.pi/skills/gstem-archief/SKILL.md` staat tussen dubbele quotes; de `: ` in de tekst is vervangen door ` — `.
- **Reden:** pi gaf een *Skill conflict*: "Nested mappings are not allowed in compact mappings". Een dubbele punt gevolgd door een spatie in een niet-gequote YAML-waarde start een geneste mapping.
- **Gevolg:** De skill laadt weer zonder fouten. Let op bij toekomstige skills: zet waarden met `: ` altijd tussen quotes.
- **Link:** gstem-archief

## 2026-10-01 — Handleiding in eenvoudige taal, zonder technische protocolnamen
- **Beslissing:** De gebruikershandleiding (`documenten/Handleiding-meettoestel.md` -> `.docx`) beschrijft alles in **eenvoudige taal**. In de sectie over besturing wordt **niet** vermeld dat het protocol CSV is; er staat dat de gebruiker **zelf een programma schrijft** (of een **voorbereid voorbeeldprogramma** gebruikt) en dat de meetmodule de stuurwaarden doorgeeft aan de controller.
- **Reden:** Gebruikersvraag: de handleiding moet begrijpelijk zijn voor wie de techniek niet kent.
- **Gevolg:** Technische details (CSV, UART, JSON) blijven in [app-architectuur-besturing](app-architectuur-besturing.md) en [besturing-en-commandos](besturing-en-commandos.md); de handleiding verwijst er niet naar.
- **Link:** [handleiding](handleiding.md)

## 2026-10-01 — Screenshots en AI-afbeeldingen expliciet aangegeven in de handleiding
- **Beslissing:** Op elke plaats waar beeld nodig is, staat een blok **SCREENSHOT** of **AI-AFBEELDING** met wat er vastgelegd moet worden. De AI maakt zelf geen schermafbeeldingen; de gebruiker voegt ze in.
- **Reden:** Gebruikersvraag: expliciet zeggen wat te screenshotten, en waar een AI-afbeelding (bv. connecties tussen de bordjes) duidelijker is dan een foto.
- **Gevolg:** Lijst met 11 screenshots en 3 AI-afbeeldingen in [handleiding](handleiding.md).
- **Link:** [handleiding](handleiding.md)

## 2026-10-01 — Screenshots van de webdemo zelf gegenereerd
- **Beslissing:** De screenshots van de laptopapp worden **automatisch gemaakt** van de webdemo (`GSTEMAPPPREVIEWWEB`) met `documenten/maak-screenshots.py` (Playwright + de Chrome op de pc). Ze staan in `documenten/afbeeldingen/` en worden in de handleiding ingevoegd.
- **Reden:** Gebruikersvraag: zelf schermafbeeldingen maken en gebruiken waar mogelijk.
- **Gevolg:** Schermafbeeldingen 4 t/m 7 en de beelden bij hoofdstuk 5 zijn echte beelden; de foto's van hardware (toestel, USB-ontvanger, controller, testopstelling) blijven `SCREENSHOT`-blokken.
- **Link:** [handleiding](handleiding.md), [links](links.md)

## 2026-10-01 — Projectnaam vastgelegd: Positie- en beweging meettoestel met LoRa integratie
- **Beslissing:** De definitieve projectnaam is **Positie- en beweging meettoestel met LoRa integratie**. De werktitel **AeroLink** vervalt.
- **Reden:** Gebruikersvraag: het project noemen naar de naam die eerder al gebruikt werd.
- **Gevolg:** Handleiding en README gebruiken de nieuwe naam; de titelregel van de handleiding volgt de referentie-opmaak (`Handleiding voor ***Positie- en beweging meettoestel met LoRa integratie***`, naam vet-cursief). De mappen `docs/` en `CODEXIMPORT/` zijn voorlopig ongewijzigd gelaten.
- **Link:** [handleiding](handleiding.md), [open-vragen](open-vragen.md)

## 2026-09-29 — Geen emoji's in chat.md (en het archief)
- **Beslissing:** De logger schrijft koppen als `## Gebruiker · ...` en `## AI · ...` zonder emoji. In de sectie Opmaak van de skill staat nu: geen emoji's in antwoorden of archiefbestanden; gebruik tekstlabels zoals `Let op:` of `Klaar.`.
- **Reden:** Gebruikersvraag: geen emoji's in de sessielogs. AI-antwoorden komen letterlijk in `chat.md` terecht.
- **Gevolg:** Bestaande emoji-koppen in `GEBRUIKER/chat.md` zijn eenmalig opgeruimd. Nieuwe logs zijn emoji-vrij.
- **Gewijzigd:** `.pi/extensions/gstem-logger.ts`, `.pi/skills/gstem-archief/SKILL.md`.
- **Link:** gstem-archief

## 2026-10-01 — Code-pagina: variabelen als niet-klikbaar overzicht, API met eigen handleidingpagina
- **Beslissing:** De rechterkolom van de pagina **Code** wordt in twee delen gesplitst. Bovenaan een **alleen-lezen variabelenoverzicht** (niet klikbaar, met voorbeeldcode); onderaan een **API-paneel** met status, knoppen om de API aan/uit te zetten en te testen, en een kleine link naar een aparte handleidingspagina. De variabelen worden niet meer gebruikt om in te voegen.
- **Reden:** Gebruikersvraag: het rechterpaneel moet gewoon tonen welke variabelen je kan gebruiken en hoe, zonder invoegknoppen; het onderste deel is voor de API met eigen handleiding en bedieningsknoppen.
- **Gevolg:** `insertAtCursor()` en `data-insert` zijn verwijderd uit `GSTEMAPPPREVIEWWEB/index.html`. Nieuwe pagina `GSTEMAPPPREVIEWWEB/api-handleiding.html`. Upload-info en de knop Uploaden blijven als vaste voettekst.
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md), [handleiding](handleiding.md), [specificaties](specificaties.md)

## 2026-10-04 — CSV schrijft de gebruiker zelf; API krijgt eigen sectie
- **Beslissing:** De pagina **Code** bevat **geen vaste uitgangsvariabelen** meer (geen `uit.servo1`, `uit.motorLinks`, enz.). De gebruiker schrijft de **CSV-regel zelf in de code**, bijvoorbeeld `Serial.println("15,-5,75,60")`. De **API** voor een extern programma verhuist naar een **eigen navigatie-sectie** `#page-api` met eigen bediening en documentatie; `api-handleiding.html` verwijst nu door naar die sectie.
- **Reden:** Gebruikersvraag: geen vooraf ingestelde servo-/uitgangsvelden meer — de output-CSV hoort in de code. De API moet een eigen sectie en documentatie krijgen.
- **Gevolg:** `index.html`: navigatie uitgebreid met **API**, rechterkolom van Code toont alleen nog **leesvariabelen** plus de groep **Zelf de CSV-regel schrijven**, en er is een nieuwe sectie `#page-api`. De API-downlink is nu een **vrije CSV-regel** in plaats van vaste commando's (`throttle`, `servo_roll`, ...). `api-handleiding.html` is een doorverwijspagina naar `index.html#page-api`.
- **Link:** [app-architectuur-besturing](app-architectuur-besturing.md), [specificaties](specificaties.md), [afgevoerd](afgevoerd.md)

## 2026-10-04 — A/B-test voor de Code-pagina
- **Beslissing:** We vergelijken twee versies van de Code-pagina naast elkaar: **A** = de huidige versie (`index.html`, code + rechterkolom Variabelen), **B** = een herziene versie (`index-b.html`) in **één kolom** met een korte **uitklapbare hulp**: *Wat kan ik gebruiken?* en *Hoe stuur ik iets?*. De uitklapbare uitleg is **kort** gehouden zodat ze weinig plaats inneemt.
- **Reden:** Gebruikersvraag: een A/B-test met een herziene code-pagina die zeer eenvoudig en niet druk is.
- **Gevolg:** Nieuwe bestanden `GSTEMAPPPREVIEWWEB/index-b.html` en `GSTEMAPPPREVIEWWEB/ab-vergelijken.html` (twee frames naast elkaar). Beide versies laden met `?embed=1` zodat de setup-popup in de frames wegblijft. Versie A blijft ongewijzigd.
- **Link:** [specificaties](specificaties.md), [ab-test-code-pagina](ab-test-code-pagina.md)

## 2026-10-04 — Versie B is de officiële Code-pagina
- **Beslissing:** Versie B (Code-pagina in **één kolom** met korte **uitklapbare hulp**) is de **officiële** versie en vervangt `GSTEMAPPPREVIEWWEB/index.html`. De oude tweekoloms Code-pagina en de A/B-testbestanden verdwijnen.
- **Reden:** Gebruikersvraag: maak versie B de nieuwe officiële versie.
- **Gevolg:** `index-b.html` en `ab-vergelijken.html` zijn verwijderd; `index.html` is nu de één-kolomsversie (titel terug naar "GSTEM · Live Tracking", de `?embed`-popup-onderdrukking is verwijderd). Ongebruikte CSS voor de oude rechterkolom (`.code-side`, `.var-*`, `.side-*`, `.upload-*`, `.api-manual-link`) is uit `style.css` gehaald; die ging van ±1477 naar ±1391 regels.
- **Link:** [specificaties](specificaties.md), [ab-test-code-pagina](ab-test-code-pagina.md), [afgevoerd](afgevoerd.md)

## 2026-10-05 — Ontwerp volledig uitgewerkt in `documenten/`; niet rechtstreeks in Google Docs
- **Beslissing:** De ontwerptekst *Positie- en beweging meettoestel met LoRa integratie* wordt volledig uitgewerkt in het project zelf — `documenten/specificaties/Ontwerp-meetmodule.md` als bron, `documenten/specificaties/Ontwerp-meetmodule.docx` als Word-versie via `documenten/build-ontwerp.py`. De inhoud van het Google Doc wordt **niet** rechtstreeks door de AI gewijzigd; de gebruiker plakt of uploadt de tekst zelf in het Doc.
- **Reden:** Er is geen schrijftoegang tot Google Docs (alleen lezen via de publieke link). Bestanden in het project zijn bovendien versioneerbaar en herbouwbaar.
- **Gevolg:** De bron blijft de markdown in `documenten/`. Word opnieuw genereren met `python documenten/build-ontwerp.py`. Het Google Doc loopt achter op de bron tot de tekst wordt overgezet.
- **Link:** [meetmodule-voorbereiding](meetmodule-voorbereiding.md), [links](links.md), [specificaties](specificaties.md)

## 2026-10-05 — Veiligheidsstop in de firmware van de meetmodule
- **Beslissing:** De veiligheidsstop zit in de **firmware van de meetmodule** en niet alleen in de laptopapplicatie: geen geldig commando binnen de ingestelde tijd -> motoren naar nul en servo's naar neutraal; ongeldige regels negeren en tellen; verbroken verbinding -> de meetmodule gaat zelf naar de veilige toestand; geofencing-schending -> veilige toestand.
- **Reden:** Het toestel moet ook veilig zijn als de laptop of de LoRa-verbinding wegvalt; de module is de enige laag die altijd aanwezig is.
- **Gevolg:** Vastgelegd in `documenten/specificaties/Ontwerp-meetmodule.md` (sectie Besturing en veiligheid). Blijft open: de omschakeltijd in seconden en de precieze veilige toestand per toesteltype.
- **Link:** [besturing-en-commandos](besturing-en-commandos.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md), [open-vragen](open-vragen.md)

## 2026-10-05 — AI-mappen en tussenversies verwijderd na vastleggen in documentatie
- **Beslissing:** `CODEXIMPORT/`, `GSTEMAPPPREVIEWWEB/`, de ziparchieven in `archief/` en de oude `.docx.bak-*`-bestanden in `documenten/` zijn verwijderd. Hun inhoud blijft beschreven in `docs/01`–`docs/04` en in `GEBRUIKER/Projectdocumentatie/`. `docs/` en de Obsidian-kopie `GEBRUIKER/Projectdocumentatie/` worden **identiek** gehouden.
- **Reden:** Gebruikersvraag: de hele map herschikken en ruimte winnen; de documentenmap en de webdemo namen te veel opslag in en waren dubbel met de documentatie.
- **Gevolg:** De map `archief/` is opgeheven. Alles blijft herstelbaar via git-commit `5acdfa0`. README en `docs/05` beschrijven de opgeruimde toestand.
- **Link:** [links](links.md), [afgevoerd](afgevoerd.md), [specificaties](specificaties.md)

## 2026-10-06 — Projectnaam gewijzigd: van "meetmodule" naar "meettoestel"
- **Beslissing:** De definitieve projectnaam is voortaan **Positie- en beweging meettoestel met LoRa integratie**. Het woord *meetmodule* in de naam is vervangen door *meettoestel*.
- **Reden:** Gebruikersvraag; *toestel* dekt het volledige product beter dan *module*, dat alleen naar het elektronische insteekdeel verwijst.
- **Gevolg:** Naam bijgewerkt in `README.md`, `documenten/specificaties/Ontwerp-meetmodule.md`, `data/beslissingen.md`, `data/specificaties.md`, `data/links.md`, `data/open-vragen.md`, `data/meetmodule-voorbereiding.md`, `onderwerpen.md` en de topiclinks. Bestandsnamen (`Ontwerp-meetmodule.md`, `meetmodule-voorbereiding.md`) en [meetmodule-voorbereiding](meetmodule-voorbereiding.md) verwijzen nog naar de oude slug; de technische term *meetmodule* voor het insteekdeel blijft in de tekst staan. De Word-versie (`Ontwerp-meetmodule.docx`) moet opnieuw gebouwd worden met `python documenten/build-ontwerp.py`.
- **Link:** [beslissingen](beslissingen.md), [open-vragen](open-vragen.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md)

## 2026-10-06 — Meetprestaties en bereik vastgelegd
- **Beslissing:** Het meettoestel meet vier grootheden: **richting** (graden, horizontaal en verticaal vlak), **snelheid** (km/u), **hoogte** (nauwkeurig tot **1,5 m**) en **locatie** (nauwkeurig tot **0,5 m**). Het draadloze **bereik** tussen toestel en USB-ontvanger is **maximaal 4 km**.
- **Reden:** Vastgelegd in de door de gebruiker afgewerkte specificaties; dit zijn de beoogde productprestaties.
- **Gevolg:** Vastgelegd in `documenten/specificaties/GStem-Specificaties.md` en [specificaties](specificaties.md). De haalbaarheid per grootheid hangt af van de nog te kiezen sensoren ([open-vragen](open-vragen.md)).
- **Link:** [specificaties](specificaties.md), [gstem-specificaties](gstem-specificaties.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md)

## 2026-10-06 — Ontvanger in USB-stickvorm; toestel en app starten automatisch
- **Beslissing:** De draadloze ontvanger heeft de vorm van een **USB-stick** en steekt in de laptop. Het meettoestel **start automatisch** mee met het voertuig waarop het gemonteerd is (LED toont dat het actief is). De laptopapplicatie **start vanzelf** zodra de USB-ontvanger wordt ingestoken.
- **Reden:** Gebruiksgemak; de gebruiker hoeft niets handmatig aan te zetten.
- **Gevolg:** Vastgelegd in [specificaties](specificaties.md) en [gstem-specificaties](gstem-specificaties.md).
- **Link:** [specificaties](specificaties.md), [app-architectuur-besturing](app-architectuur-besturing.md)

## 2026-10-06 — App-schermopbouw: verbinding, kaart, Code en API
- **Beslissing:** De laptopapp controleert eerst de verbindingen en gaat pas verder na **OK**. Daarna volgt het kaartscherm met **3D-kaart met Google-satellietfoto's** (afgelegde weg en kijkrichting) én een **tabel** met de losse meetwaarden. De knop **Code** opent de editor met rechtervensters voor uitleg en variabelen; code stuurt CSV-instructies terug naar de controller en wordt met een knop **geüpload**. De knop **API** opent de pagina om de API **aan/uit** te zetten, de verbinding te **testen** en het **adres** te tonen. Op elk scherm staat de status van USB-ontvanger en meettoestel.
- **Reden:** Vastgelegd in de afgewerkte specificaties; bevestigt en concretiseert de bestaande app-architectuur.
- **Gevolg:** Vastgelegd in [specificaties](specificaties.md) en [gstem-specificaties](gstem-specificaties.md); sluit aan op [app-architectuur-besturing](app-architectuur-besturing.md), [code-pagina](code-pagina.md) en [handleiding](handleiding.md).
- **Link:** [specificaties](specificaties.md), [app-architectuur-besturing](app-architectuur-besturing.md), [code-pagina](code-pagina.md)

## 2026-10-06 — RC-vliegtuig-mock-up: Arduino via UART TX/RX, drie besturingsvlakken
- **Beslissing:** Het mock-up vliegtuigje wordt bestuurd door een **Arduino** die **CSV-waarden** aanneemt en via zijn **TX/RX-punten** met het meettoestel is verbonden (UART). Het meettoestel wordt met zijn **voorkant gelijk** aan die van het vliegtuigje gericht. De **rolroeren, het hoogteroer en het richtingsroer** reageren op de metingen; de Arduino stelt de **servo's** in, real-time. Dit is een **zittend voorbeeld**, geen volledig functioneel vliegtuig.
- **Reden:** Vastgelegd in de afgewerkte specificaties; hiermee is de elektrische koppeling (UART TX/RX) en het aantal besturingsvlakken (drie) definitief.
- **Gevolg:** De open vraag over de uitbreidingsconnector (PWM/UART/I2C/CAN/analoog) is daarmee beantwoord: **UART**. Het exacte CSV-veldformaat en de spanningsniveaus blijven open. Vastgelegd in [specificaties](specificaties.md), [besturing-en-commandos](besturing-en-commandos.md) en [open-vragen](open-vragen.md).
- **Link:** [specificaties](specificaties.md), [besturing-en-commandos](besturing-en-commandos.md), [app-architectuur-besturing](app-architectuur-besturing.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Afgewerkte gebruikersspecificaties als bron opgenomen
- **Beslissing:** Het bestand `documenten/specificaties/GStem-Specificaties.md` (aangeleverd door de gebruiker) is de **afgewerkte gebruikersspecificatie** en wordt als bron in het project bewaard naast de technische [meetmodule-voorbereiding](meetmodule-voorbereiding.md) en [specificaties](specificaties.md).
- **Reden:** De gebruiker leverde een volledig uitgewerkte, gebruikersgerichte specificatietekst aan.
- **Gevolg:** Samengevat in [gstem-specificaties](gstem-specificaties.md) en vastgelegd in [specificaties](specificaties.md); opgenomen in [links](links.md). De tekst wordt nog niet als Word-document gegenereerd.
- **Link:** [specificaties](specificaties.md), [links](links.md), [gstem-specificaties](gstem-specificaties.md)

## 2026-10-06 — Aanpak bevestigd: losse componenten als breakout-modules op een eigen draagprint
- **Beslissing:** Alle componenten (sensoren en ESP's) worden als **breakout-modules** aangekocht en op **socket-headers** van een zelfontworpen **draagprint** geplaatst. De print bevat de weerstanden, voedingspaden, connectiepunten en een **power-LED**; de modules blijven vervangbaar.
- **Reden:** Gebruikerskeuze: modulair, vervangbaar en eenvoudiger te solderen dan losse IC's; de foutenlast bij montage daalt.
- **Gevolg:** Vastgelegd in [specificaties](specificaties.md). De exacte modulekeuzes, pinouts, regelaars en het PCB-ontwerpgereedschap moeten nog worden bepaald ([open-vragen](open-vragen.md)).
- **Link:** [specificaties](specificaties.md), [meetmodule-voorbereiding](meetmodule-voorbereiding.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Planning toegespitst op het project
- **Beslissing:** De aangeleverde planning is toegespitst op het project. Niet-projectgebonden school- en sociale momenten zijn verwijderd: **Bezinningen Krakau** (14-15-16 okt), **Belevingsdag Thomas More** (28 jan), **Chrysostomos** (Vr 19 febr) en **Sportdag** (4 mei). De presentatie van 5 min/ll is **verzet naar Di 13 okt** en heet nu **Voorlopige presentatie SVL 5 min/ll**.
- **Reden:** Gebruikersvraag: de planning moet enkel het project volgen; losse schoolactiviteiten horen er niet in.
- **Gevolg:** `documenten/beheer/Planning-GSTEM.xlsx` en [planning](planning.md) zijn bijgewerkt. De vakantieperiodes blijven staan omdat ze het werk aan het project onderbreken.
- **Link:** [planning](planning.md), [links](links.md)

## 2026-10-06 — Actieplan toegevoegd als tweede blad in het Excel-bestand
- **Beslissing:** Naast de schoolplanning komt er een **actieplan** met alle nog te ondernemen projectstappen (voorbereiding, hardware, firmware, app, beheer, testen, documentatie, presentatie). Het staat als **tweede blad "Actieplan"** in `documenten/beheer/Planning-GSTEM.xlsx`, in een **oranje kleur** die afwijkt van de blauwe schoolplanning.
- **Reden:** Gebruikersvraag: een eigen planning van de resterende stappen, visueel onderscheiden van de schoolplanning.
- **Gevolg:** Vastgelegd in [actieplan](actieplan.md); bijgewerkt in [planning](planning.md), [links](links.md) en `onderwerpen.md`. De stappen zijn afgeleid uit [open-vragen](open-vragen.md), [specificaties](specificaties.md) en [meetmodule-voorbereiding](meetmodule-voorbereiding.md).
- **Link:** [actieplan](actieplan.md), [planning](planning.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Excel met brede rijen en exacte datums
- **Beslissing:** `documenten/beheer/Planning-GSTEM.xlsx` is herwerkt met **bredere kolommen en hogere rijen** (betere leesbaarheid) en met **exacte datums** in `dd/mm/jjjj`-notatie. De schoolplanning kreeg exacte datums voor schooljaar **2026-2027**; het actieplan kreeg per stap een **voorstel-streefdatum**. De kolomtitels zijn verduidelijkt: "Datum-Periode (exact)" en "Streefdatum (exact)".
- **Reden:** Gebruikersvraag: alles breder en met exacte datums.
- **Gevolg:** Vastgelegd in [planning](planning.md) en [actieplan](actieplan.md). De weekdagen in de bron (di/vr/za/ma) kloppen met de afgeleide jaartallen; dit staat als aanname in [planning](planning.md).
- **Link:** [planning](planning.md), [actieplan](actieplan.md)

## 2026-10-06 — "GT" in de planning betekent examens
- **Beslissing:** In de planning staat **GT voor examens**. De periode **03/12/2026 - 14/12/2026** is dus een examenperiode, naast "Start examens" op 11/06/2027.
- **Reden:** Verduidelijking door de gebruiker.
- **Gevolg:** Rij in `documenten/beheer/Planning-GSTEM.xlsx` heet nu "GT (examens)"; [planning](planning.md) bijgewerkt en de open vraag over GT geschrapt.
- **Link:** [planning](planning.md)

## 2026-10-06 — Aankoop: alle componenten zelf, enkel de print wordt gemaakt
- **Beslissing:** De gebruiker **koopt alle componenten zelf aan**: alle breakout-modules (ESP32-S3, LoRa, IMU, barometer, RTK-GNSS), de voeding en alle losse onderdelen. Het **PCB-bordje zelf is het enige stuk dat niet als kant-en-klare module wordt gekocht**; daarop staan de **LED en de sockets** (en eventueel de overige printonderdelen).
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** De draagprint is in de praktijk een **drager**; de stuklijst (BOM) wordt gesplitst in "zelf aankopen" en "op de print". De print bevat minstens LED + sockets. Of de voedingsonderdelen (buck, LDO, zekering, weerstanden, condensatoren) ook op de print komen, is nog te bevestigen — zie [open-vragen](open-vragen.md).
- **Link:** [pcb-ontwerp](pcb-ontwerp.md), [specificaties](specificaties.md), [pcb-methodes-kosten](pcb-methodes-kosten.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Gekozen componenten: XIAO ESP32S3 + Wio-SX1262 kit en Adafruit BNO055
- **Beslissing:** Als **rekenkern + LoRa** wordt de **XIAO ESP32S3 + Wio-SX1262 kit** gebruikt (ESP32-S3 en SX1262 via B2B-connector, SPI, IPEX-antenne, USB-C, ingebouwde LiPo-lader). Als **9-DoF IMU** wordt de **Adafruit BNO055-breakout** gebruikt (sensorfusie aan boord, I2C 0x28/0x29). Beide bij antratek.be aangekocht.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** ESP32 en LoRa zijn nu **één module** op de draagprint. De XIAO heeft een **ingebouwde LiPo-lader**, waardoor de geplande 7,4 V -> buck -> LDO-keten mogelijk vervalt (3,7 V LiPo volstaat). Het **pin-budget** van de XIAO (± 14 I/O) moet gecontroleerd worden tegen IMU + barometer + GNSS + UART. Centrale lijst in [componenten](componenten.md); open punten (barometer, RTK-GNSS, voeding) in [open-vragen](open-vragen.md).
- **Link:** [componenten](componenten.md), [specificaties](specificaties.md), [open-vragen](open-vragen.md), [links](links.md)

## 2026-10-06 — Voedingsroute: 7,4 V-accu met buck naar 5 V
- **Beslissing:** De hoofdvoeding blijft de **7,4 V-accu** met **zekering/ompoolbeveiliging -> buck-converter naar 5 V** en een **LDO naar 3,3 V** voor de 3,3 V-modules. De XIAO wordt op zijn **5 V-pin** gevoed; de **ingebouwde LiPo-lader van de XIAO wordt niet gebruikt**. Het 3,7 V LiPo-alternatief vervalt.
- **Reden:** Gebruikerskeuze `2026-10-06`.
- **Gevolg:** De batterij- en regelaaronderdelen (accu, zekering, ompoolbeveiliging, buck 5 V, LDO 3,3 V) blijven in de stuklijst. Zie [componenten](componenten.md).
- **Link:** [componenten](componenten.md), [specificaties](specificaties.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Pin-budget XIAO als AI-taak voor later
- **Beslissing:** Het controleren van het **pin-budget** van de XIAO (± 14 I/O) tegen IMU + barometer + GNSS + UART, en het opstellen van de **pinout-tabel**, wordt een **taak die de AI later uitvoert** (geen gebruikersactie).
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** Vastgelegd als AI-taak in [open-vragen](open-vragen.md) en [actieplan](actieplan.md). De uitkomst bepaalt of alle modules op de XIAO passen of dat een I2C-multiplexer/expander nodig is.
- **Link:** [open-vragen](open-vragen.md), [actieplan](actieplan.md), [componenten](componenten.md)

## 2026-10-06 — Barometer: Adafruit BMP390 (meest accurate)
- **Beslissing:** De barometer wordt de **Adafruit BMP390-breakout** (druk + temperatuur, I2C/SPI).
- **Reden:** Gebruikersvraag: *het meest accurate dat je vind*. Uit de datasheets heeft de BMP390 de beste relatieve nauwkeurigheid (±3 Pa ≈ 0,25 m) en de laagste ruis (0,02 Pa) van de makkelijk verkrijgbare breakouts — beter dan de BMP581 (±6 Pa, 0,08 Pa) en de BME280. Luchtvochtigheid is niet nodig.
- **Gevolg:** Vastgelegd in [componenten](componenten.md). De BME280 en BMP581 vallen af als actieve keuze ([afgevoerd](afgevoerd.md)).
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md), [afgevoerd](afgevoerd.md)

## 2026-10-06 — RTK-GNSS: Quectel LC29H(DA) met NTRIP-correctie
- **Beslissing:** De RTK-GNSS-module wordt de **Quectel LC29H(DA)** (dual-band L1+L5, multi-constellatie, RTK **rover**, ingebouwde LNA + SAW). De correcties komen van een **NTRIP-dienst** via de laptop; er komt **geen eigen basisstation**.
- **Reden:** Gebruikerskeuze. De LC29H(DA) is een betaalbaar alternatief voor de dure ZED-F9P en haalt centimeter-niveau; de (DA)-variant is precies de rover. NTRIP vermijdt extra basishardware.
- **Gevolg:** Vastgelegd in [componenten](componenten.md). De (BS)-variant (basisstation) is niet nodig. De **NTRIP-provider** en de exacte configuratie blijven open. De **GNSS-antenne** moet dual-band L1+L5 actief zijn (advies: die van de Waveshare LC29H-HAT).
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md), [links](links.md)

## 2026-10-06 — Sockettype: dual-wipe voor de ESP32, precisie voor de rest
- **Beslissing:** De vaak gewisselde **XIAO ESP32S3** komt in een **dual-wipe** socket; alle vast gemonteerde modules (IMU, barometer, GNSS, voeding) komen in **precisie-/gefreesde** sockets.
- **Reden:** Gebruikerskeuze; sluit aan op [pcb-methodes-kosten](pcb-methodes-kosten.md) (trillingen in een bewegend voertuig vragen vaste precisie-contacten; de ESP wordt tijdens ontwikkeling vaker gewisseld).
- **Gevolg:** Op de print komen **twee sockettypes**; de landpatronen blijven 2,54 mm. Het exacte merk/model blijft open.
- **Link:** [componenten](componenten.md), [pcb-methodes-kosten](pcb-methodes-kosten.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Voeding en schakelaar: barrel-connector, geen aan/uit-schakelaar
- **Beslissing:** Er komt **geen aan/uit-schakelaar**: het toestel **springt aan zodra het aan de voeding hangt**. De voeding is de **7,4 V-accu** met een **barrel-connector** en de **buck-converter 5 V** die de gebruiker al heeft. De **bescherming (zekering/ompoolbeveiliging/TVS)** en de **LDO 3,3 V** zijn nog niet gekozen.
- **Reden:** Gebruikerskeuze. De XIAO levert zelf 3,3 V op zijn 3V3-pin, dus een losse LDO is mogelijk overbodig.
- **Gevolg:** Geen schakelaar-footprint op de print; wel een barrel-connector. Bescherming en LDO blijven als open punten in [open-vragen](open-vragen.md) en [componenten](componenten.md).
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md)

## 2026-10-06 — LoRa-ontvanger wordt een tweede XIAO-kit
- **Beslissing:** De draadloze **ontvanger** aan de laptopzijde is een **tweede XIAO ESP32S3 + Wio-SX1262 kit**, aangesloten met een **USB A-kabel**.
- **Reden:** Gebruikerskeuze; identieke hardware als het toestel, dus dezelfde firmware-basis.
- **Gevolg:** Vastgelegd in [componenten](componenten.md). De USB-stick-vorm uit de specificaties wordt met deze kit ingevuld (kit in een behuizing/aan een kabel).
- **Link:** [componenten](componenten.md), [specificaties](specificaties.md)

## 2026-10-06 — Mock-up: Arduino Uno, eigen servo's en eigen 3D-print
- **Beslissing:** De mock-up gebruikt een **Arduino Uno**, **meer dan drie servo's uit de eigen voorraad** (type vrij) met een **aparte buck-converter als servo-voeding** (heeft de gebruiker al). De romp/stuurstangen/roerbladen worden **zelf 3D-geprint**.
- **Reden:** Gebruikerskeuze; de gebruiker heeft de servo's, de buck en de printer al.
- **Gevolg:** Enkel de **servo's** moeten nog op de bestellijst om niets te vergeten. De UART tussen toestel en Uno vraagt **niveau-afstemming** (3,3 V <-> 5 V).
- **Link:** [componenten](componenten.md), [besturing-en-commandos](besturing-en-commandos.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Zoekvolgorde open componenten vastgelegd (1 per 1)
- **Beslissing:** De open componenten worden **een per een** afgehandeld in een vaste werkorder: eerst bordkritisch, dan voeding/RF, verbindingen, ontvanger, mock-up, gereedschap. De lijst staat in [componenten](componenten.md) onder *Te zoeken: werkorder*.
- **Reden:** Gebruikersvraag: systematisch nagaan wat nog gezocht moet worden.
- **Gevolg:** In deze ronde zijn de punten 1-4, 7, 10, 12, 15, 20-29 afgehandeld; de rest blijft open.
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md)

## 2026-10-06 — UART-koppeling: schroefconnectoren, gemeenschappelijke ground en level shifter
- **Beslissing:** Tussen het meettoestel en de Arduino Uno komt een **UART met schroefklem-connectoren**, voorzien van een **gemeenschappelijke ground (GND)** en een **level shifter (3,3 V <-> 5 V)**. De **USB-C datakabel** en de **Dupont-/siliconendraad** heeft de gebruiker al in huis; die komen **niet** op de bestellijst.
- **Reden:** Gebruikersaanwijzing `2026-10-06`: de schroefconnector is bevestigd, de ground en level shifter horen erbij, en de kabel + jumperdraad zijn al aanwezig.
- **Gevolg:** Het type level shifter blijft te zoeken (AI-taak). Grounddraad en level shifter moeten in de bestellijst/op de print worden voorzien. Vastgelegd in [componenten](componenten.md) en [open-vragen](open-vragen.md).
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md), [besturing-en-commandos](besturing-en-commandos.md), [specificaties](specificaties.md)

## 2026-10-06 — Uitbreidingsconnector en level shifter gekozen
- **Beslissing:** De uitbreidingsconnector wordt een **4-pins schroefklem op 3,5 mm-raster** (KF128/KF301) met pinout GND / +5 V / TX / RX. De level shifter wordt de **TXB0104** (4-kanaals bidirectioneel, VCCA 3,3 V, VCCB 5 V), **op de draagprint** geplaatst. **I2C-pull-ups komen niet op de print**: de BNO055- en BMP390-breakouts hebben ze al (enkel 2 reserve-footprints).
- **Reden:** Gebruikersvraag: *kies zelf iets passends*. De schroefklem is robuust en past bij de eerder gekozen schroefconnectoren. TXB0104 is de juiste soort (push-pull, voor UART/SPI); de I2C-bus blijft volledig 3,3 V en heeft dus geen shifter nodig.
- **Gevolg:** De print krijgt een schroefklem-footprint en een TXB0104. De 5 V-referentie voor de shifter komt van de 5 V-rail (buck). Vastgelegd in [componenten](componenten.md).
- **Link:** [componenten](componenten.md), [pcb-ontwerp](pcb-ontwerp.md), [besturing-en-commandos](besturing-en-commandos.md)

## 2026-10-06 — Bescherming van de voeding: PTC, P-MOSFET en TVS
- **Beslissing:** De 7,4 V-ingang krijgt een **2 A PTC-zekering**, een **P-MOSFET ompoolbeveiliging** (DMG2301L) en een **TVS-diode SMBJ10A**, plus een **bulk-elco 100 uF/16 V**.
- **Reden:** Gebruikersvraag: *hetgeen dat nodig is volgens jou*. De P-MOSFET beschermt tegen omgekeerde polariteit met weinig spanningsverlies; de PTC begrenst de stroom; de TVS vangt spanningspieken op. Samen de standaard minimale bescherming voor een accugevoed bord.
- **Gevolg:** Vastgelegd in [componenten](componenten.md) en de essentials-tabel. Deze onderdelen komen op de draagprint.
- **Link:** [componenten](componenten.md), [pcb-ontwerp](pcb-ontwerp.md), [specificaties](specificaties.md)

## 2026-10-06 — Extra 3,3 V-LDO op de print (AP2112K-3.3)
- **Beslissing:** Er komt een **eigen 3,3 V-rail** met een **AP2112K-3.3** (of AMS1117-3.3) op de draagprint voor de sensoren, ook al levert de XIAO zelf 3,3 V.
- **Reden:** Gebruikerskeuze: de LDO is goed en wordt nuttig geacht. Een eigen rail houdt de sensoren gescheiden van de XIAO-rail.
- **Gevolg:** Let op de **LoRa-ontvanger** (tweede XIAO-kit): die hangt via **USB** aan de laptop en heeft zijn **eigen 3,3 V-regelaar** — daar is geen losse LDO nodig. Vastgelegd in [componenten](componenten.md).
- **Link:** [componenten](componenten.md), [specificaties](specificaties.md)

## 2026-10-06 — Externe antennes: SMA-pigtail voor LoRa en actieve GNSS-antenne
- **Beslissing:** De LoRa-antenne wordt **buiten het vliegtuigje** geconnecteerd via een **IPEX/U.FL -> SMA female bulkhead pigtail**. Voor de GNSS komt een **actieve dual-band L1/L5-antenne met SMA, LNA en ground plane** (compacte uitvoering, voorbeeld: de dual-band GNSS-antenne van Waveshare), passend bij de LC29H(DA).
- **Reden:** Gebruikersvraag `2026-10-06`: beslist dat de antenne buiten het vliegtuigje moet; voor de GNSS-antenne mocht de AI iets passends kiezen.
- **Gevolg:** Beide antennes komen op de bestellijst. De LoRa-kitantenne blijft behouden. Vastgelegd in [componenten](componenten.md).
- **Link:** [componenten](componenten.md), [links](links.md), [pcb-ontwerp](pcb-ontwerp.md)

## 2026-10-06 — Bestellijst: alles eerst op antratek.be zoeken
- **Beslissing:** Er komt een **bestellijst** met alle componenten. Elk onderdeel wordt **eerst op www.antratek.be** gezocht; **niet gevonden = niet elders zoeken**. Per onderdeel staan link, kost en aantal; de gebruiker tagt zelf de onderdelen die hij al heeft. De lijst wordt ook als **Excel** bewaard.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** `GEBRUIKER/data/bestellijst.md` en `documenten/beheer/Bestellijst-GSTEM.xlsx` (via `documenten/scripts/build-bestellijst.py`). Niet op antratek: BMP390, LC29H(DA), 2S LiPo, voedingsbescherming, AP2112K, 4-pins schroefklem, sockets, passieven en M3-montage.
- **Link:** [bestellijst](bestellijst.md), [componenten](componenten.md), [links](links.md)

## 2026-10-06 — Zo veel mogelijk bij Kiwi Electronics
- **Beslissing:** Onderdelen zo veel mogelijk bij **Kiwi Electronics** kopen om verzendkosten te beperken; wat daar **goedkoper** is of als **reserve** dient blijft bij **antratek.be**.
- **Ingevuld:** **BNO085** (€ 32,05, goedkoper + nieuwer dan BNO055), **BMP581** (€ 10,88, nauwkeuriger dan BME280), actieve **GNSS SMA-antenne** (€ 16,93), **TXB0108** level converter (€ 8,70), LED/weerstand (€ 2,16), condensatorkit (€ 10,27), bulk-elco (€ 0,59) → Kiwi € 81,58. Bij antratek blijven de **XIAO-kit** (€ 30,26, Wio-SX1262 bij Kiwi uit voorraad) en de **U.FL→SMA pigtail** (€ 3,57) → antratek € 33,83.
- **Gevolg:** Totaal te bestellen **€ 115,41**. Nodig blijft nog een **tweede winkel** voor RTK-module, discrete voeding, connectoren, sockets en M3-montage (niet bij Kiwi of antratek).
- **Link:** [bestellijst](bestellijst.md), [links](links.md), [componenten](componenten.md)

## 2026-10-06 — Voedingsbescherming en LDO op de draagprint
- **Beslissing:** De **2 A PTC-zekering, P-MOSFET DMG2301L (ompoolbeveiliging), TVS SMBJ10A en LDO AP2112K-3.3** komen **op de draagprint**, samen met de bulk-elco en power-LED, in de **voedingssectie linksboven bij de ingang**. Enkel de buck-converter, accu, barrel-connector en sensormodules blijven losse modules.
- **Reden:** Gebruikersvraag `2026-10-06`; bescherming hoort zo dicht mogelijk bij de ingangsconnector (kortste pad, beste klemming) en de LDO zo dicht mogelijk bij de sensoren (schone 3,3 V).
- **Gevolg:** De printstuklijst bevat deze onderdelen; in KiCad footprint + behuizing kiezen (SMD of through-hole). Zie [componenten](componenten.md) en [pcb-schets](pcb-schets.md).
- **Link:** [componenten](componenten.md), [pcb-schets](pcb-schets.md), [pcb-ontwerp](pcb-ontwerp.md)

## 2026-10-06 — Accu, barrel-adapter en USB-A-kabel al in bezit
- **Beslissing:** De gebruiker heeft al: een **2S LiPo-accu met connector en kabel**, de **DC Barrel Jack Adapter - Female** en een **USB-A naar USB-C kabel** voor de XIAO. Deze staan op `al in bezit` en vallen uit het te-bestellen-totaal.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** Standaard te-bestellen-totaal bij antratek zakt naar **EUR 114,12** (met magneetantenne) of **EUR 215,76** (met L1/L5-antenne). Bijgewerkt in [bestellijst](bestellijst.md), [componenten](componenten.md) en `documenten/beheer/Bestellijst-GSTEM.xlsx`.
- **Link:** [bestellijst](bestellijst.md), [componenten](componenten.md)

## 2026-10-06 — Goedkoopste passende onderdelen kiezen (totaal beperken)
- **Beslissing:** Waar een goedkoper passend alternatief op antratek bestaat, wordt dat gebruikt, zodat het totaal niet absurd wordt. Concreet: **BME280** (EUR 19,97) i.p.v. de niet-verkrijgbare BMP390, en de **GPS/GNSS magneetantenne SMA 3m** (EUR 19,30, L1) i.p.v. de dual-band L1/L5-antenne (EUR 120,94). De nauwkeurigere L1/L5-antenne blijft als **optionele upgrade** vermeld.
- **Reden:** Gebruikersaanwijzing `2026-10-06`: gebruik goedkopere onderdelen waar mogelijk.
- **Gevolg:** Te-bestellen-totaal bij antratek: **EUR 118,90** (standaard), **EUR 220,54** met L1/L5-antenne, **EUR 98,93** zonder barometer. Let op: de goedkope magneetantenne is **enkelbandig (L1)**, dus mindere RTK-robuustheid dan dual-band. Bijgewerkt in [bestellijst](bestellijst.md), `documenten/beheer/Bestellijst-GSTEM.xlsx` en [links](links.md).
- **Link:** [bestellijst](bestellijst.md), [links](links.md), [componenten](componenten.md)

## 2026-10-06 — Arduino Uno al in bezit
- **Beslissing:** De **Arduino Uno** voor de mock-up heeft de gebruiker **thuis**; die staat in de bestellijst op `al in bezit` en valt uit het te-bestellen-totaal.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** Te-bestellen-totaal bij antratek zakt naar **EUR 200,57** (met L1/L5-antenne) of **EUR 98,93** (magneetantenne). Bijgewerkt in [bestellijst](bestellijst.md), [componenten](componenten.md) en `documenten/beheer/Bestellijst-GSTEM.xlsx`.
- **Link:** [bestellijst](bestellijst.md), [componenten](componenten.md)

## 2026-10-06 — NTRIP gratis (gebruiker zoekt); socket-merken later
- **Beslissing:** De NTRIP-correctiedienst wordt een **gratis** provider; de **gebruiker zoekt die zelf**. De exacte **merken** voor precisie- en dual-wipe-sockets worden later bepaald en hoeven **niet per se op de bestellijst**.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** NTRIP-provider blijft als gebruikersactie open; de socket-keuze is een detail voor het schema, geen blokkade. Vastgelegd in [componenten](componenten.md) en [open-vragen](open-vragen.md).
- **Link:** [componenten](componenten.md), [open-vragen](open-vragen.md), [links](links.md)

## 2026-10-06 — PCB-fabrikant: AISLER
- **Beslissing:** De draagprint wordt gefabriceerd bij **AISLER** (Duitsland/Nederland, binnen de EU). De andere onderzochte fabrikanten (JLCPCB, PCBWay, Seeed Fusion, OSH Park, Eurocircuits, Multi-CB, BETA LAYOUT/LeitOn) zijn **gekend en bewaard**, maar niet gekozen.
- **Reden:** Gebruikersaanwijzing `2026-10-06`. AISLER is het **makkelijkst binnen Europa** (KiCad/ODB++ direct, vaste prijs per oppervlak, geen extra kosten voor gaten/via's, gratis verzending, productie vanaf 2 werkdagen) en vermijdt invoer/btw-gedoe.
- **Gevolg:** 2-laags 1,6 mm HASL Budget: € 12,00 job fee + € 0,067/cm² × oppervlak × aantal (sets van 3). Bij een aangenomen bord van 100 × 75 mm: **± € 32,76 incl. btw voor 3 stuks**. Productie- en onderdelenkost samengebracht in [bestelschema-pcb](bestelschema-pcb.md); vergelijking in [pcb-fabrikanten](pcb-fabrikanten.md).
- **Link:** [pcb-fabrikanten](pcb-fabrikanten.md), [bestelschema-pcb](bestelschema-pcb.md), [bestellijst](bestellijst.md), [beslissingen](beslissingen.md)

## 2026-10-06 — Eindbeeld van de eind-PCB als PNG genereren
- **Beslissing:** Er wordt een **PNG-eindbeeld** gemaakt van de eind-PCB met de **definitief gekozen** breakouts (XIAO ESP32S3 + Wio-SX1262, BNO085, BMP581, LC29H(DA)), de losse printcomponenten en de **Arduino Uno** met al zijn verbindingen. Bestand: `documenten/pcb/PCB-eindbeeld.png`, gebouwd met `documenten/scripts/build-pcb-eindbeeld.py` (PIL, geen extra software nodig).
- **Reden:** Gebruikersvraag `2026-10-06`: een beeld van de **eindtoestand** met alle breakouts, exacte componenten, de Arduino en de verbindingen. De bestaande schets gebruikte nog de oudere BNO055/BMP390-varianten.
- **Gevolg:** Het eindbeeld toont de voedingsbussen (5 V / 3,3 V / GND), I2C, GNSS-UART, de Arduino-UART via de **TXB0104**, de LoRa-RF en de 4-aderige kabel naar de Arduino. De **pinout blijft een voorstel** (open AI-taak); schematisch en niet op schaal. Vastgelegd in [pcb-schets](pcb-schets.md) en [links](links.md).
- **Link:** [pcb-schets](pcb-schets.md), [links](links.md), [componenten](componenten.md)

## 2026-10-06 — LC29H(DA) als breakout + overige artikelen bij EU-winkels
- **Beslissing:** De RTK-GNSS-module wordt een **breakout board**: de **Waveshare LC29H(DA) GPS/RTK HAT (SKU 25279)**, gekocht bij **Botland (Polen, EU)** voor **€ 70,50 incl. btw**. De module wordt **niet** als losse SMD-module gekocht. De overige `geen-link`-onderdelen komen bij **EU-winkels**: LDO AP2112K-3.3TRG1 + TVS SMBJ10A bij **TME (PL)**, P-MOSFET DMG2301L-7 + PTC Littelfuse 1812L200/16 bij **Mouser.be/DigiKey (EU-magazijn)**, 4-pins 3,5 mm schroefklem DEGSON DG250-3.5-04P bij **HESTORE (HU)**/TME, precisie/dual-wipe sockets bij **TME**/RS, en de M3-montageset bij **TinyTronics (NL)**.
- **Reden:** Gebruikersaanwijzing `2026-10-06`: zoek de resterende artikelen bij **andere websites**, liefst **EU** (China enkel als het echt moet), en de **LC29H(DA) moet een breakout board** zijn. Botland/Kamami/HESTORE zijn EU (geen invoer), de HAT is kant-en-klaar en levert de antenne mee.
- **Gevolg:** Alle `geen-link`-onderdelen zijn nu vindbaar; de **aparte GNSS-antenne (€ 16,93) vervalt** omdat de HAT een **dual-band actieve L1/L5-antenne** meelevert. Te-bestellen-totaal ± **€ 184,48** incl. btw (Kiwi + antratek + Botland + TME/Mouser + TinyTronics). Let op: de HAT is **65 × 30,5 mm met 40-pins header** — footprint op de draagprint nog afwegen. Bijgewerkt in [bestellijst](bestellijst.md), [bestelschema-pcb](bestelschema-pcb.md), [links](links.md) en [open-vragen](open-vragen.md); de Excel `documenten/beheer/Bestellijst-GSTEM.xlsx` is **herbouwd** via `documenten/scripts/build-bestellijst.py` (per-winkel-subtotalen, EUR 184,16 onderdelen / EUR 216,92 incl. AISLER-print).
- **Link:** [bestellijst](bestellijst.md), [links](links.md), [bestelschema-pcb](bestelschema-pcb.md), [open-vragen](open-vragen.md), [componenten](componenten.md)

## 2026-10-06 — GPS/RTK-module gekocht bij Eckstein (DE), niet Botland
- **Beslissing:** De **Waveshare LC29H(DA) GPS/RTK HAT (art. WS25279, EAN 4060137304156)** wordt besteld bij **Eckstein (Duitsland, EU)** voor **€ 71,39 incl. btw**, i.p.v. de eerdere keuze **Botland** (€ 70,50 incl.).
- **Reden:** Gebruikersaanwijzing `2026-10-06` ("pak de gps maar van Eckstein"). Eckstein is een Duitse EU-winkel met prijs in EUR en snelle levering; het bord blijft dezelfde **breakout** (geen losse SMD-module).
- **Gevolg:** Te-bestellen-onderdelen stijgen van **€ 184,16** naar **€ 185,05** incl. btw (+ € 0,89); incl. AISLER-print **€ 217,81**. Alternatieven blijven Kamami (PL, ± € 63) en Botland (PL/DE, € 70,50); HESTORE (HU, ± € 110 incl.) is te duur. Bijgewerkt in [bestellijst](bestellijst.md), [gps-rtk-prijzen](gps-rtk-prijzen.md), [bestelbaarheid](bestelbaarheid.md), [links](links.md) en [open-vragen](open-vragen.md); de Excel `documenten/beheer/Bestellijst-GSTEM.xlsx` is **herbouwd** via `documenten/scripts/build-bestellijst.py` (nieuwe status `eckstein`).
- **Link:** [bestellijst](bestellijst.md), [gps-rtk-prijzen](gps-rtk-prijzen.md), [links](links.md), [open-vragen](open-vragen.md)

## 2026-10-06 — Geen P-MOSFET-ompoolbeveiliging
- **Beslissing:** De **P-MOSFET-ompoolbeveiliging vervalt**. Noch de **DMG2301L** noch het alternatief **AO3401A** komt op de print of op de bestellijst. De **2 A PTC-zekering** en de **TVS SMBJ10A** blijven behouden.
- **Reden:** Gebruikersaanwijzing `2026-10-06` ("Zet P-MOSFET-keuze: dat we dat niet doen"). Bijkomend: de DMG2301L was met Vgs(max) ±8 V te krap voor een 2S-accu van max 8,4 V, en TME had de `-13` niet op voorraad (MOQ 10 000).
- **Gevolg:** Omgekeerd aansluiten wordt **fysiek** voorkomen met een **gepolariseerde connector** (XT60/JST-XH) i.p.v. elektronisch. Te-bestellen-onderdelen dalen van **€ 185,05** naar **€ 184,75** incl. btw (− € 0,30); incl. AISLER-print **€ 217,51**. Bijgewerkt in [bestellijst](bestellijst.md), [componenten](componenten.md), [specificaties](specificaties.md), [bestelschema-pcb](bestelschema-pcb.md), [open-vragen](open-vragen.md) en [afgevoerd](afgevoerd.md); de Excel `documenten/beheer/Bestellijst-GSTEM.xlsx` is **herbouwd** (nieuwe `niet nodig`-regel).
- **Link:** [bestellijst](bestellijst.md), [componenten](componenten.md), [specificaties](specificaties.md), [bestelschema-pcb](bestelschema-pcb.md), [open-vragen](open-vragen.md), [afgevoerd](afgevoerd.md)

## 2026-10-06 — Power-LED + 330 Ω-weerstand al in bezit
- **Beslissing:** De **3 mm rode LED (10-pack)** en de **330 Ω-weerstand (10-pack)** staan op `al in bezit`: de gebruiker heeft ze **thuis**. Ze worden **niet** bij Kiwi besteld.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** Kiwi Electronics zakt van **€ 64,65** naar **€ 62,49**; te-bestellen-onderdelen van **€ 184,75** naar **€ 182,59** incl. btw (incl. AISLER-print **€ 215,35**). In [bestelschema-pcb](bestelschema-pcb.md) zakt subtotaal 3b van **€ 10,01** naar **€ 9,79** en het printtotaal van **€ 57,65** naar **€ 57,43**; **werkelijk nieuw te bestellen blijft € 47,64**. Bijgewerkt in [bestellijst](bestellijst.md), [bestelschema-pcb](bestelschema-pcb.md) en [bestelbaarheid](bestelbaarheid.md); de Excel `documenten/beheer/Bestellijst-GSTEM.xlsx` is **herbouwd** via `documenten/scripts/build-bestellijst.py` (status `al in bezit`).
- **Link:** [bestellijst](bestellijst.md), [bestelschema-pcb](bestelschema-pcb.md), [bestelbaarheid](bestelbaarheid.md)

## 2026-10-06 — Blender-mock-up: volledige opstelling in 3D
- **Beslissing:** Er komt een **Blender-mock-up** van het volledige toestel: de draagprint met de breakouts op sockets, de losse printonderdelen, de antennes/bekabeling, de **Arduino Uno met servo's**, de **tweede XIAO-kit** als LoRa-ontvanger en de laptopzijde. Gebouwd met het herhaalbare sript `documenten/blender/build_gstem_mockup.py`, opgeslagen als `documenten/blender/gstem-mockup.blend`, met **drie studio-renders** in `documenten/blender/renders/`.
- **Reden:** Gebruikersvraag `2026-10-06`: een semi-accurate model plus een paar renders van de print met alle breakouts en toebehoren verbonden (medium detail, maar accuraat).
- **Gevolg:** Modulevarianten **BNO085 + BMP581** (zoals [bestellijst](bestellijst.md) en `documenten/pcb/PCB-eindbeeld.png`; [componenten](componenten.md) noemt nog BNO055/BMP390). Bordafmeting **100 x 75 mm** uit [bestelschema-pcb](bestelschema-pcb.md), modulematen uit de **datasheets** ([gstem-hardware-afmetingen](gstem-hardware-afmetingen.md)). Belangrijkste vondst: de **LC29H(DA) is een 65 x 30,5 mm Pi-HAT**, geen klein breakout. De **layout op de print is een voorstel** — de KiCad-layout bestaat nog niet. Zie [blender-mockup](blender-mockup.md).
- **Link:** [blender-mockup](blender-mockup.md), [gstem-hardware-afmetingen](gstem-hardware-afmetingen.md), [pcb-schets](pcb-schets.md), [componenten](componenten.md)

## 2026-10-06 — Draw.io-schema's verwijderd
- **Beslissing:** De **Communicatieschema-GSTEM.drawio/.png** en **Verbindingsschema-GSTEM.drawio/.png** met hun bouwscripts (`build-communicatieschema.py`, `build-verbindingsschema.py`) zijn **verwijderd** uit `documenten/`; de bijhorende notitiepagina's verbindingsschema en communicatieschema zijn verwijderd en alle verwijzingen zijn uit de andere documentatie gehaald.
- **Reden:** Gebruikersaanwijzing `2026-10-06` ("Verwijder dit uit de documenten map samen met verbindingsschema. Haal dit ook uit de doc's.").
- **Gevolg:** Overzicht van verbindingen en communicatie blijft beschikbaar via `documenten/pcb/PCB-schets.md` (Mermaid-schema's), `documenten/pcb/PCB-eindbeeld.png` en [app-architectuur-besturing](app-architectuur-besturing.md).
- **Link:** [pcb-schets](pcb-schets.md), [app-architectuur-besturing](app-architectuur-besturing.md), [componenten](componenten.md)

## 2026-10-06 — `documenten/` herschikt in submappen
- **Beslissing:** `documenten/` is herschikt in vier submappen: **`specificaties/`** (`GStem-Specificaties.md`, `Ontwerp-meetmodule.md` + `.docx`), **`pcb/`** (`PCB-schets.md` + draagprint-SVG/PNG, `PCB-eindbeeld.png`, `Communicatie-overzicht-GSTEM.drawio`, `review-mockup-controleblad.png`), **`beheer/`** (`Bestellijst-GSTEM.xlsx`, `Planning-GSTEM.xlsx`) en **`scripts/`** (`build-*.py`). De losse resten `documenten/.pi/` en `documenten/__pycache__/` zijn verwijderd. De bouwscripts bepalen hun uitvoerpad nu via `__file__` in plaats van hardgecodeerde paden.
- **Reden:** Gebruikersaanwijzing `2026-10-06` ("Reorganize everything in documenten"), met de keuze voor indeling per soort.
- **Gevolg:** Alle actieve padverwijzingen in `docs/`, `GEBRUIKER/data/`, `GEBRUIKER/Projectdocumentatie/`, `README.md` en `GEBRUIKER/onderwerpen.md` zijn bijgewerkt; `documenten/README.md` is de nieuwe index. De archief-chatlogs zijn **niet** aangepast, zodat historische paden daar blijven staan. De verbindingsschema-bestanden (`Verbindingsschema-GSTEM.*`, `build-verbindingsschema.py`) blijven verwijderd.
- **Link:** [links](links.md), onderwerpen

## 2026-10-06 — Blender-mock-up verwijderd
- **Beslissing:** De map `documenten/blender/` (model, scripts, drie renders en de review-set) is **verwijderd**; de eerdere mock-up-beslissing komt te vervallen. Het geannoteerde `documenten/pcb/review-mockup-controleblad.png` en het script `documenten/scripts/build-controleblad.py` blijven bewaard als naslag, maar dat script kan pas opnieuw draaien als de review-renders uit git teruggehaald zijn.
- **Reden:** Gebruikerskeuze `2026-10-06` ("verwijderd laten"): de 3D-mock-up wordt niet verder gebruikt.
- **Gevolg:** Alles blijft herstelbaar uit git (commit `28e4fae`). [blender-mockup](blender-mockup.md) is op status **verwijderd** gezet; de mock-up-gerelateerde open vragen (HAT-montage, onderdelenposities) blijven gelden voor de nog te maken KiCad-layout. Zie [afgevoerd](afgevoerd.md).
- **Link:** [blender-mockup](blender-mockup.md), [afgevoerd](afgevoerd.md), [open-vragen](open-vragen.md)

## 2026-10-07 — LC29HDA via China, AliExpress liefst
- **Beslissing:** De aankoopvoorkeur voor de RTK-GNSS verschuift van Eckstein (EU) naar **China, bij voorkeur AliExpress**. De technische keuze blijft **Quectel LC29HDA als RTK-rover**, op een geassembleerde breakout/development board. Er is nog **geen specifieke aanbieding goedgekeurd**.
- **Reden:** Gebruikerskeuze `2026-10-07`: "Let's do china, aliexpress preferably". Controle van de officiële Waveshare-variantbeschrijving bevestigt dat **DA** de rover-/terminalvariant is; **BS** is de basisstationvariant. "DA" is deel van de modulevariant, geen D/A-converterbord.
- **Gevolg:** De oude Waveshare LC29H(DA) HAT bij Eckstein (€ 71,39) wordt terugvaloptie. AliExpress-resultaten zijn tegenstrijdig (sommige advertenties zeggen "base station" terwijl LC29HDA genoemd wordt); koop pas na verificatie van modulevariant, breakout/pinout, antenne, prijs en checkout-totaal. De GNSS-antenne is niet langer als inbegrepen beschouwd totdat bundelinhoud bevestigd is. Bestellijst en Excel-status zijn bijgewerkt; zie [gps-rtk-prijzen](gps-rtk-prijzen.md), [bestellijst](bestellijst.md), [open-vragen](open-vragen.md) en [links](links.md).
- **Link:** [gps-rtk-prijzen](gps-rtk-prijzen.md), [bestellijst](bestellijst.md), [open-vragen](open-vragen.md), [links](links.md)

## 2026-10-07 — AliExpress-kandidaat voor LC29HDA gevonden
- **Beslissing:** Kandidaatlisting **AliExpress item 1005010036256167** wordt verder gecontroleerd. De geïndexeerde titel noemt **Quectel LC29HDA**, dual-frequency, **Mobile Station** en **Board Kit**, dus hij lijkt het best bij de gekozen rover-breakout te passen. Het is nog **geen goedgekeurde bestelling**.
- **Reden:** De gebruiker vroeg om een AliExpress-link. Andere gevonden advertenties waren expliciet als base-station gelabeld of lieten meerdere LC29H-varianten door elkaar lopen. De AliExpress-productpagina van deze kandidaat blokkeerde inhoudscontrole.
- **Gevolg:** Verkoper/listing moet nog bevestigen: exacte LC29HDA-variant (niet LC29HBS), geassembleerd board versus bare SMD, UART/pinout en voedings-/logicaniveaus, afmetingen, en wat "dual antenna" inhoudt (poorten en meegeleverde antennes). Prijs en checkout-totaal ook nog te controleren. Bijgewerkt in [gps-rtk-prijzen](gps-rtk-prijzen.md), [bestellijst](bestellijst.md), [open-vragen](open-vragen.md) en [links](links.md).
- **Link:** https://www.aliexpress.com/item/1005010036256167.html

## 2026-10-07 — AliExpress-listing vervangen
- **Beslissing:** De niet-werkende kandidaatlink **1005010036256167** wordt vervangen door de door de gebruiker aangeleverde AliExpress-listing **1005009915138674**.
- **Reden:** De gebruiker meldde dat de vorige listinglink niet werkte en leverde een vervangende productlink.
- **Gevolg:** Bestellijst, Excel, componentenoverzicht, linkregister en open vragen verwijzen nu naar item 1005009915138674. De listinginhoud is nog niet technisch gecontroleerd; de LC29HDA-rovervariant, geassembleerde breakout, pinout, antennes en actuele prijs blijven te verifiëren. De bestaande antennekandidaat blijft ongewijzigd.
- **Link:** https://nl.aliexpress.com/item/1005009915138674.html

## 2026-10-07 — Bestellijst definitief gemaakt
- **Beslissing:** De bestellijst is definitief afgewerkt: elk onderdeel heeft een **gekozen model, winkel, aantal en prijs**. Toegevoegd: **2,1 mm PCB-barreljack** (Kiwi, € 1,20) voor montage op de draagprint; **level shifter definitief = TXB0108-breakout** (Kiwi, € 8,70); **sockets** als set standaard 2,54 mm dual-wipe/turned-pin (Mouser/DigiKey/TME, ± € 5,00); **GNSS-antenne** als voorwaardelijke losse post (Waveshare SKU 25346, ± € 15,70).
- **Reden:** Gebruikersvraag `2026-10-07`: "Update de bestellijst zodat ik alles finale heb en niks mis."
- **Gevolg:** Totalen: **€ 134,59** onderdelen excl. losse GNSS-antenne en AISLER; **€ 150,29** incl. losse antenne; **€ 183,05** alles incl. AISLER-print (3 st.). De LC29HDA-listing blijft de gekozen GPS-aankoop met richtprijs ± € 22,19; bij het bestellen de **LC29HDA-variant** kiezen. Excel herbouwd via `documenten/scripts/build-bestellijst.py`.
- **Link:** [bestellijst](bestellijst.md), [bestelbaarheid](bestelbaarheid.md), [gps-rtk-prijzen](gps-rtk-prijzen.md), [links](links.md)

## 2026-10-07 — GPS/RTK: gekozen listing + veilige alternatieven
- **Beslissing:** De RTK-GNSS wordt bij **AliExpress (China)** gekocht als **LC29HDA-developmentboard** (richtprijs ± € 22,19). De door de gebruiker aangeleverde listing **1005009915138674** blijft de referentie, maar omdat de titel "LC29H" vermeldt, worden twee eenduidige alternatieven met variantkeuzemenu toegevoegd: **1005010758488281** (USB-C-devboard) en **1005010162466640** (LC29HDA-boardkit). Terugvaloptie blijft de **Waveshare LC29H(DA) HAT** (Eckstein € 71,39 / Kamami ± € 63).
- **Reden:** Onderzoek `2026-10-07` via DuckDuckGo/AliExpress: de gebruikerslink noemt geen DA-variant, terwijl andere listings LC29HDA expliciet in de titel of het variantkeuzemenu hebben. De AliExpress-productpagina blokkeert directe inhoudscontrole.
- **Gevolg:** Bij het bestellen de **LC29HDA (rover)** selecteren, geen LC29HBS en geen losse SMD-module. Vastgelegd in [bestellijst](bestellijst.md), [gps-rtk-prijzen](gps-rtk-prijzen.md) en [links](links.md).
- **Link:** [gps-rtk-prijzen](gps-rtk-prijzen.md), [bestellijst](bestellijst.md), [links](links.md)

## 2026-10-09 — Eigen bedrading en 3D-geprinte montage in plaats van draagprint
- **Beslissing:** De gebruiker verbindt de breakoutmodules zelf met draden en soldeert de verbindingen. De onderdelen worden daarna gemonteerd aan een zelf 3D-geprinte behuizing. De aparte draagprint/carrier-PCB en alle socket-headers vervallen.
- **Reden:** De gebruiker wil de modules niet langer via een eigen PCB met elkaar verbinden, maar zelf bedraden en solderen en de onderdelen rechtstreeks in/aan een geprinte behuizing monteren.
- **Gevolg:** De AISLER-draagprint en sockets worden uit de actieve bestellijst en Excel-totalen gehaald. De breakoutmodules zelf blijven behouden. Behuizingsbevestiging, connectoren, bedrading en de fysieke montage van losse voedingsonderdelen moeten nog worden bepaald; er wordt hiervoor nog niets online opgezocht of nieuw op de bestellijst gezet.
- **Link:** [bedrading-en-behuizing](bedrading-en-behuizing.md), [specificaties](specificaties.md), [bestellijst](bestellijst.md), [open-vragen](open-vragen.md)

## 2026-10-10 — Herziene specificaties: code- en API-pagina vervangen door besturing-apps
- **Beslissing:** De herziene gebruikersspecificaties (pdf in Downloads, 2026-10-10) vervangen de oude schermen 3 en 4. De code-pagina (editor met CSV-upload) en de API-pagina (extern programma koppelen) vervallen uit de specificatie. Scherm 3 is nu een Besturing-menu met drie applicatie-iconen (eentje per voertuigtype); scherm 4 is zo'n voertuigspecifieke besturingspagina, als voorbeeld uitgewerkt voor een auto met stuur (klikken en slepen) en gaspedaal (ingedrukt houden). De mock-up is van een RC-vliegtuigje met drie roeren en servo's een generiek demonstratievoertuig geworden (auto als voorbeeld); de installatie blijft UART via TX/RX + GND.
- **Reden:** De gebruiker heeft de specificaties geupdate en gevraagd er conclusies uit te trekken; de nieuwe pdf is de actuele gebruikersgerichte versie van het product.
- **Gevolg:** De webdemo-onderdelen #page-code en #page-api zijn niet langer onderdeel van de beoogde app; een nieuwe webdemo/bouw moet scherm 3 en 4 als besturing-apps uitwerken. CSV-over-UART naar de Arduino blijft de koppeling met het voertuig, maar het CSV-formaat wordt nu door de besturing-app bepaald i.p.v. door gebruikerscode. De feedbacklus-test via het codeerscherm vervalt; de validatietest is nu enkel de handmatige kantel-/beweegtest met synchrone 3D-visualisatie. Bronbestand documenten/specificaties/GStem-Specificaties.md herschreven met de nieuwe inhoud en de pdf-afbeeldingen in documenten/specificaties/afbeeldingen/. Bijgewerkt: gstem-specificaties, code-pagina (vervangen-status), app-architectuur-besturing (deels vervangen), open-vragen.
- **Link:** [gstem-specificaties](gstem-specificaties.md), [code-pagina](code-pagina.md), [app-architectuur-besturing](app-architectuur-besturing.md), [open-vragen](open-vragen.md)

## 2026-10-10 — Presentatie als PowerPoint in documenten/presentatie
- **Beslissing:** Er is een PowerPoint-presentatie van het project aangemaakt in `documenten/presentatie/Presentatie-GSTEM.pptx`, herbouwbaar met `documenten/presentatie/build_gstem_presentatie.py`. Structuur (7 dia's, 16:9): titel met naam en conceptillustratie van het meettoestel, algemene inleiding met de vier metingen, sensoren (IMU, barometer, RTK-GNSS, ESP32-S3 + LoRa), app-scherm 1 en 2, app-scherm 3 en 4, communicatieschema met diagram, slotdia. De titelillustratie is programmatisch getekend (Pillow) als `device-illustratie.png`; de app-schermen zijn de bestaande mock-upafbeeldingen uit `documenten/specificaties/afbeeldingen/`.
- **Reden:** Gebruikersvraag van 2026-10-10: een eenvoudige PowerPoint met titel, voorbeeldbeeldje van het meettoestel, de app-schermen uit de specificaties, een communicatiediagram en de sensoren; strakke visuele opmaak zonder overbodige versiering.
- **Gevolg:** De Canva-plugin en de ingebouwde fotogenerator waren niet beschikbaar in deze sessie; de illustratie is daarom code-natief getekend en kan later vervangen worden door een foto of AI-beeld. Inhoud volgt de herziene specificaties (scherm 3 en 4 als besturing-apps, auto als voorbeeld). De presentatie wordt nog niet in `documenten/README.md` vermeld tot de gebruiker hem goedkeurt.
- **Link:** [gstem-specificaties](gstem-specificaties.md), [specificaties](specificaties.md), [communicatie-overzicht](communicatie-overzicht.md)

## 2026-10-10 — Presentatie herwerkt: betere diagrammen, planning en budgetdia
- **Beslissing:** De presentatie is herwerkt naar 9 dia's. Het communicatiediagram is overzichtelijker gemaakt (aparte I²C- en UART-labels, dubbele LoRa-pijlen met het 4 km-bereik, aparte gestippelde terugweg voor stuurcommando's, uitlegblok met veiligheidsstop onderaan). Nieuw zijn dia 7 (planning met deadlines: voorlopige presentatie 13/10/2026, onderdelen bestellen en apart testen nov-dec 2026, evaluatie SVZ 01/12/2026, demo-app dec 2026-feb 2027, volledige app feb-mei 2027, SVZ-presentatie 19-23/03/2027, monteren en testen mrt-mei 2027, opendeurdag 22/05/2027, juryverdediging 21/06/2027) en dia 8 (bestellijst per groep met staafjes: sensoren € 79,92 / 59 %, rekenkern + LoRa € 30,26 / 22 %, bedrading en losse elektronica € 19,56 / 15 %, antennes € 3,57 / 3 %, voeding € 1,27 / 1 %; totaal € 134,58, of € 150,28 met de voorwaardelijke losse GNSS-antenne; grootste kostenpost zijn de sensoren, vooral RTK-GNSS € 36,99 en IMU € 32,05).
- **Reden:** Gebruikersvraag van 2026-10-10: alle diagrammen verbeteren en op leesbaarheid controleren, plus een deadlineslide en een budgetslide per groep toevoegen.
- **Gevolg:** De Canva-connector bleef in deze sessie zonder uitvoerbare tools, ondanks pogingen via de plugin-catalogus en de document-toolbrug; de diagrammen zijn daarom rechtstreeks in het bouwscript verbeterd. De groepering van de bestellijst volgt de secties uit [bestellijst](bestellijst.md); de deadlines volgen [planning](planning.md) aangevuld met de werffases uit de open acties.
- **Link:** [bestellijst](bestellijst.md), [planning](planning.md), [communicatie-overzicht](communicatie-overzicht.md), [gstem-specificaties](gstem-specificaties.md)
