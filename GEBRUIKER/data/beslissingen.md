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

## 2026-10-01 — Projectnaam vastgelegd: Positie- en beweging meettoestel met LoRa integratie
- **Beslissing:** De definitieve projectnaam is **Positie- en beweging meettoestel met LoRa integratie**. De werktitel **AeroLink** vervalt.
- **Reden:** Gebruikersvraag: het project noemen naar de naam die eerder al gebruikt werd.
- **Gevolg:** Handleiding en README gebruiken de nieuwe naam; de titelregel van de handleiding volgt de referentie-opmaak (`Handleiding voor ***Positie- en beweging meettoestel met LoRa integratie***`, naam vet-cursief). De mappen `docs/` en `CODEXIMPORT/` zijn voorlopig ongewijzigd gelaten.
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
- **Beslissing:** De ontwerptekst *Positie- en beweging meettoestel met LoRa integratie* wordt volledig uitgewerkt in het project zelf — `documenten/Ontwerp-meetmodule.md` als bron, `documenten/Ontwerp-meetmodule.docx` als Word-versie via `documenten/build-ontwerp.py`. De inhoud van het Google Doc wordt **niet** rechtstreeks door de AI gewijzigd; de gebruiker plakt of uploadt de tekst zelf in het Doc.
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

## 2026-10-06 — Projectnaam gewijzigd: van "meetmodule" naar "meettoestel"
- **Beslissing:** De definitieve projectnaam is voortaan **Positie- en beweging meettoestel met LoRa integratie**. Het woord *meetmodule* in de naam is vervangen door *meettoestel*.
- **Reden:** Gebruikersvraag; *toestel* dekt het volledige product beter dan *module*, dat alleen naar het elektronische insteekdeel verwijst.
- **Gevolg:** Naam bijgewerkt in `README.md`, `documenten/Ontwerp-meetmodule.md`, `data/beslissingen.md`, `data/specificaties.md`, `data/links.md`, `data/open-vragen.md`, `data/meetmodule-voorbereiding.md`, `onderwerpen.md` en de topiclinks. Bestandsnamen (`Ontwerp-meetmodule.md`, `meetmodule-voorbereiding.md`) en [[meetmodule-voorbereiding]] verwijzen nog naar de oude slug; de technische term *meetmodule* voor het insteekdeel blijft in de tekst staan. De Word-versie (`Ontwerp-meetmodule.docx`) moet opnieuw gebouwd worden met `python documenten/build-ontwerp.py`.
- **Link:** [[beslissingen]], [[open-vragen]], [[meetmodule-voorbereiding]]

## 2026-10-06 — Meetprestaties en bereik vastgelegd
- **Beslissing:** Het meettoestel meet vier grootheden: **richting** (graden, horizontaal en verticaal vlak), **snelheid** (km/u), **hoogte** (nauwkeurig tot **1,5 m**) en **locatie** (nauwkeurig tot **0,5 m**). Het draadloze **bereik** tussen toestel en USB-ontvanger is **maximaal 4 km**.
- **Reden:** Vastgelegd in de door de gebruiker afgewerkte specificaties; dit zijn de beoogde productprestaties.
- **Gevolg:** Vastgelegd in `documenten/GStem-Specificaties.md` en [[specificaties]]. De haalbaarheid per grootheid hangt af van de nog te kiezen sensoren ([[open-vragen]]).
- **Link:** [[specificaties]], [[gstem-specificaties]], [[meetmodule-voorbereiding]]

## 2026-10-06 — Ontvanger in USB-stickvorm; toestel en app starten automatisch
- **Beslissing:** De draadloze ontvanger heeft de vorm van een **USB-stick** en steekt in de laptop. Het meettoestel **start automatisch** mee met het voertuig waarop het gemonteerd is (LED toont dat het actief is). De laptopapplicatie **start vanzelf** zodra de USB-ontvanger wordt ingestoken.
- **Reden:** Gebruiksgemak; de gebruiker hoeft niets handmatig aan te zetten.
- **Gevolg:** Vastgelegd in [[specificaties]] en [[gstem-specificaties]].
- **Link:** [[specificaties]], [[app-architectuur-besturing]]

## 2026-10-06 — App-schermopbouw: verbinding, kaart, Code en API
- **Beslissing:** De laptopapp controleert eerst de verbindingen en gaat pas verder na **OK**. Daarna volgt het kaartscherm met **3D-kaart met Google-satellietfoto's** (afgelegde weg en kijkrichting) én een **tabel** met de losse meetwaarden. De knop **Code** opent de editor met rechtervensters voor uitleg en variabelen; code stuurt CSV-instructies terug naar de controller en wordt met een knop **geüpload**. De knop **API** opent de pagina om de API **aan/uit** te zetten, de verbinding te **testen** en het **adres** te tonen. Op elk scherm staat de status van USB-ontvanger en meettoestel.
- **Reden:** Vastgelegd in de afgewerkte specificaties; bevestigt en concretiseert de bestaande app-architectuur.
- **Gevolg:** Vastgelegd in [[specificaties]] en [[gstem-specificaties]]; sluit aan op [[app-architectuur-besturing]], [[code-pagina]] en [[handleiding]].
- **Link:** [[specificaties]], [[app-architectuur-besturing]], [[code-pagina]]

## 2026-10-06 — RC-vliegtuig-mock-up: Arduino via UART TX/RX, drie besturingsvlakken
- **Beslissing:** Het mock-up vliegtuigje wordt bestuurd door een **Arduino** die **CSV-waarden** aanneemt en via zijn **TX/RX-punten** met het meettoestel is verbonden (UART). Het meettoestel wordt met zijn **voorkant gelijk** aan die van het vliegtuigje gericht. De **rolroeren, het hoogteroer en het richtingsroer** reageren op de metingen; de Arduino stelt de **servo's** in, real-time. Dit is een **zittend voorbeeld**, geen volledig functioneel vliegtuig.
- **Reden:** Vastgelegd in de afgewerkte specificaties; hiermee is de elektrische koppeling (UART TX/RX) en het aantal besturingsvlakken (drie) definitief.
- **Gevolg:** De open vraag over de uitbreidingsconnector (PWM/UART/I2C/CAN/analoog) is daarmee beantwoord: **UART**. Het exacte CSV-veldformaat en de spanningsniveaus blijven open. Vastgelegd in [[specificaties]], [[besturing-en-commandos]] en [[open-vragen]].
- **Link:** [[specificaties]], [[besturing-en-commandos]], [[app-architectuur-besturing]], [[open-vragen]]

## 2026-10-06 — Afgewerkte gebruikersspecificaties als bron opgenomen
- **Beslissing:** Het bestand `documenten/GStem-Specificaties.md` (aangeleverd door de gebruiker) is de **afgewerkte gebruikersspecificatie** en wordt als bron in het project bewaard naast de technische [[meetmodule-voorbereiding]] en [[specificaties]].
- **Reden:** De gebruiker leverde een volledig uitgewerkte, gebruikersgerichte specificatietekst aan.
- **Gevolg:** Samengevat in [[gstem-specificaties]] en vastgelegd in [[specificaties]]; opgenomen in [[links]]. De tekst wordt nog niet als Word-document gegenereerd.
- **Link:** [[specificaties]], [[links]], [[gstem-specificaties]]

## 2026-10-06 — Aanpak bevestigd: losse componenten als breakout-modules op een eigen draagprint
- **Beslissing:** Alle componenten (sensoren en ESP's) worden als **breakout-modules** aangekocht en op **socket-headers** van een zelfontworpen **draagprint** geplaatst. De print bevat de weerstanden, voedingspaden, connectiepunten en een **power-LED**; de modules blijven vervangbaar.
- **Reden:** Gebruikerskeuze: modulair, vervangbaar en eenvoudiger te solderen dan losse IC's; de foutenlast bij montage daalt.
- **Gevolg:** Vastgelegd in [[specificaties]]. De exacte modulekeuzes, pinouts, regelaars en het PCB-ontwerpgereedschap moeten nog worden bepaald ([[open-vragen]]).
- **Link:** [[specificaties]], [[meetmodule-voorbereiding]], [[open-vragen]]

## 2026-10-06 — Planning toegespitst op het project
- **Beslissing:** De aangeleverde planning is toegespitst op het project. Niet-projectgebonden school- en sociale momenten zijn verwijderd: **Bezinningen Krakau** (14-15-16 okt), **Belevingsdag Thomas More** (28 jan), **Chrysostomos** (Vr 19 febr) en **Sportdag** (4 mei). De presentatie van 5 min/ll is **verzet naar Di 13 okt** en heet nu **Voorlopige presentatie SVL 5 min/ll**.
- **Reden:** Gebruikersvraag: de planning moet enkel het project volgen; losse schoolactiviteiten horen er niet in.
- **Gevolg:** `documenten/Planning-GSTEM.xlsx` en [[planning]] zijn bijgewerkt. De vakantieperiodes blijven staan omdat ze het werk aan het project onderbreken.
- **Link:** [[planning]], [[links]]

## 2026-10-06 — Actieplan toegevoegd als tweede blad in het Excel-bestand
- **Beslissing:** Naast de schoolplanning komt er een **actieplan** met alle nog te ondernemen projectstappen (voorbereiding, hardware, firmware, app, beheer, testen, documentatie, presentatie). Het staat als **tweede blad "Actieplan"** in `documenten/Planning-GSTEM.xlsx`, in een **oranje kleur** die afwijkt van de blauwe schoolplanning.
- **Reden:** Gebruikersvraag: een eigen planning van de resterende stappen, visueel onderscheiden van de schoolplanning.
- **Gevolg:** Vastgelegd in [[actieplan]]; bijgewerkt in [[planning]], [[links]] en `onderwerpen.md`. De stappen zijn afgeleid uit [[open-vragen]], [[specificaties]] en [[meetmodule-voorbereiding]].
- **Link:** [[actieplan]], [[planning]], [[open-vragen]]

## 2026-10-06 — Excel met brede rijen en exacte datums
- **Beslissing:** `documenten/Planning-GSTEM.xlsx` is herwerkt met **bredere kolommen en hogere rijen** (betere leesbaarheid) en met **exacte datums** in `dd/mm/jjjj`-notatie. De schoolplanning kreeg exacte datums voor schooljaar **2026-2027**; het actieplan kreeg per stap een **voorstel-streefdatum**. De kolomtitels zijn verduidelijkt: "Datum-Periode (exact)" en "Streefdatum (exact)".
- **Reden:** Gebruikersvraag: alles breder en met exacte datums.
- **Gevolg:** Vastgelegd in [[planning]] en [[actieplan]]. De weekdagen in de bron (di/vr/za/ma) kloppen met de afgeleide jaartallen; dit staat als aanname in [[planning]].
- **Link:** [[planning]], [[actieplan]]

## 2026-10-06 — "GT" in de planning betekent examens
- **Beslissing:** In de planning staat **GT voor examens**. De periode **03/12/2026 - 14/12/2026** is dus een examenperiode, naast "Start examens" op 11/06/2027.
- **Reden:** Verduidelijking door de gebruiker.
- **Gevolg:** Rij in `documenten/Planning-GSTEM.xlsx` heet nu "GT (examens)"; [[planning]] bijgewerkt en de open vraag over GT geschrapt.
- **Link:** [[planning]]

## 2026-10-06 — Aankoop: alle componenten zelf, enkel de print wordt gemaakt
- **Beslissing:** De gebruiker **koopt alle componenten zelf aan**: alle breakout-modules (ESP32-S3, LoRa, IMU, barometer, RTK-GNSS), de voeding en alle losse onderdelen. Het **PCB-bordje zelf is het enige stuk dat niet als kant-en-klare module wordt gekocht**; daarop staan de **LED en de sockets** (en eventueel de overige printonderdelen).
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** De draagprint is in de praktijk een **drager**; de stuklijst (BOM) wordt gesplitst in "zelf aankopen" en "op de print". De print bevat minstens LED + sockets. Of de voedingsonderdelen (buck, LDO, zekering, weerstanden, condensatoren) ook op de print komen, is nog te bevestigen — zie [[open-vragen]].
- **Link:** [[pcb-ontwerp]], [[specificaties]], [[pcb-methodes-kosten]], [[open-vragen]]

## 2026-10-06 — Gekozen componenten: XIAO ESP32S3 + Wio-SX1262 kit en Adafruit BNO055
- **Beslissing:** Als **rekenkern + LoRa** wordt de **XIAO ESP32S3 + Wio-SX1262 kit** gebruikt (ESP32-S3 en SX1262 via B2B-connector, SPI, IPEX-antenne, USB-C, ingebouwde LiPo-lader). Als **9-DoF IMU** wordt de **Adafruit BNO055-breakout** gebruikt (sensorfusie aan boord, I2C 0x28/0x29). Beide bij antratek.be aangekocht.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** ESP32 en LoRa zijn nu **één module** op de draagprint. De XIAO heeft een **ingebouwde LiPo-lader**, waardoor de geplande 7,4 V -> buck -> LDO-keten mogelijk vervalt (3,7 V LiPo volstaat). Het **pin-budget** van de XIAO (± 14 I/O) moet gecontroleerd worden tegen IMU + barometer + GNSS + UART. Centrale lijst in [[componenten]]; open punten (barometer, RTK-GNSS, voeding) in [[open-vragen]].
- **Link:** [[componenten]], [[specificaties]], [[open-vragen]], [[links]]

## 2026-10-06 — Voedingsroute: 7,4 V-accu met buck naar 5 V
- **Beslissing:** De hoofdvoeding blijft de **7,4 V-accu** met **zekering/ompoolbeveiliging -> buck-converter naar 5 V** en een **LDO naar 3,3 V** voor de 3,3 V-modules. De XIAO wordt op zijn **5 V-pin** gevoed; de **ingebouwde LiPo-lader van de XIAO wordt niet gebruikt**. Het 3,7 V LiPo-alternatief vervalt.
- **Reden:** Gebruikerskeuze `2026-10-06`.
- **Gevolg:** De batterij- en regelaaronderdelen (accu, zekering, ompoolbeveiliging, buck 5 V, LDO 3,3 V) blijven in de stuklijst. Zie [[componenten]].
- **Link:** [[componenten]], [[specificaties]], [[open-vragen]]

## 2026-10-06 — Pin-budget XIAO als AI-taak voor later
- **Beslissing:** Het controleren van het **pin-budget** van de XIAO (± 14 I/O) tegen IMU + barometer + GNSS + UART, en het opstellen van de **pinout-tabel**, wordt een **taak die de AI later uitvoert** (geen gebruikersactie).
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** Vastgelegd als AI-taak in [[open-vragen]] en [[actieplan]]. De uitkomst bepaalt of alle modules op de XIAO passen of dat een I2C-multiplexer/expander nodig is.
- **Link:** [[open-vragen]], [[actieplan]], [[componenten]]

## 2026-10-06 — Barometer: Adafruit BMP390 (meest accurate)
- **Beslissing:** De barometer wordt de **Adafruit BMP390-breakout** (druk + temperatuur, I2C/SPI).
- **Reden:** Gebruikersvraag: *het meest accurate dat je vind*. Uit de datasheets heeft de BMP390 de beste relatieve nauwkeurigheid (±3 Pa ≈ 0,25 m) en de laagste ruis (0,02 Pa) van de makkelijk verkrijgbare breakouts — beter dan de BMP581 (±6 Pa, 0,08 Pa) en de BME280. Luchtvochtigheid is niet nodig.
- **Gevolg:** Vastgelegd in [[componenten]]. De BME280 en BMP581 vallen af als actieve keuze ([[afgevoerd]]).
- **Link:** [[componenten]], [[open-vragen]], [[afgevoerd]]

## 2026-10-06 — RTK-GNSS: Quectel LC29H(DA) met NTRIP-correctie
- **Beslissing:** De RTK-GNSS-module wordt de **Quectel LC29H(DA)** (dual-band L1+L5, multi-constellatie, RTK **rover**, ingebouwde LNA + SAW). De correcties komen van een **NTRIP-dienst** via de laptop; er komt **geen eigen basisstation**.
- **Reden:** Gebruikerskeuze. De LC29H(DA) is een betaalbaar alternatief voor de dure ZED-F9P en haalt centimeter-niveau; de (DA)-variant is precies de rover. NTRIP vermijdt extra basishardware.
- **Gevolg:** Vastgelegd in [[componenten]]. De (BS)-variant (basisstation) is niet nodig. De **NTRIP-provider** en de exacte configuratie blijven open. De **GNSS-antenne** moet dual-band L1+L5 actief zijn (advies: die van de Waveshare LC29H-HAT).
- **Link:** [[componenten]], [[open-vragen]], [[links]]

## 2026-10-06 — Sockettype: dual-wipe voor de ESP32, precisie voor de rest
- **Beslissing:** De vaak gewisselde **XIAO ESP32S3** komt in een **dual-wipe** socket; alle vast gemonteerde modules (IMU, barometer, GNSS, voeding) komen in **precisie-/gefreesde** sockets.
- **Reden:** Gebruikerskeuze; sluit aan op [[pcb-methodes-kosten]] (trillingen in een bewegend voertuig vragen vaste precisie-contacten; de ESP wordt tijdens ontwikkeling vaker gewisseld).
- **Gevolg:** Op de print komen **twee sockettypes**; de landpatronen blijven 2,54 mm. Het exacte merk/model blijft open.
- **Link:** [[componenten]], [[pcb-methodes-kosten]], [[open-vragen]]

## 2026-10-06 — Voeding en schakelaar: barrel-connector, geen aan/uit-schakelaar
- **Beslissing:** Er komt **geen aan/uit-schakelaar**: het toestel **springt aan zodra het aan de voeding hangt**. De voeding is de **7,4 V-accu** met een **barrel-connector** en de **buck-converter 5 V** die de gebruiker al heeft. De **bescherming (zekering/ompoolbeveiliging/TVS)** en de **LDO 3,3 V** zijn nog niet gekozen.
- **Reden:** Gebruikerskeuze. De XIAO levert zelf 3,3 V op zijn 3V3-pin, dus een losse LDO is mogelijk overbodig.
- **Gevolg:** Geen schakelaar-footprint op de print; wel een barrel-connector. Bescherming en LDO blijven als open punten in [[open-vragen]] en [[componenten]].
- **Link:** [[componenten]], [[open-vragen]]

## 2026-10-06 — LoRa-ontvanger wordt een tweede XIAO-kit
- **Beslissing:** De draadloze **ontvanger** aan de laptopzijde is een **tweede XIAO ESP32S3 + Wio-SX1262 kit**, aangesloten met een **USB A-kabel**.
- **Reden:** Gebruikerskeuze; identieke hardware als het toestel, dus dezelfde firmware-basis.
- **Gevolg:** Vastgelegd in [[componenten]]. De USB-stick-vorm uit de specificaties wordt met deze kit ingevuld (kit in een behuizing/aan een kabel).
- **Link:** [[componenten]], [[specificaties]]

## 2026-10-06 — Mock-up: Arduino Uno, eigen servo's en eigen 3D-print
- **Beslissing:** De mock-up gebruikt een **Arduino Uno**, **meer dan drie servo's uit de eigen voorraad** (type vrij) met een **aparte buck-converter als servo-voeding** (heeft de gebruiker al). De romp/stuurstangen/roerbladen worden **zelf 3D-geprint**.
- **Reden:** Gebruikerskeuze; de gebruiker heeft de servo's, de buck en de printer al.
- **Gevolg:** Enkel de **servo's** moeten nog op de bestellijst om niets te vergeten. De UART tussen toestel en Uno vraagt **niveau-afstemming** (3,3 V <-> 5 V).
- **Link:** [[componenten]], [[besturing-en-commandos]], [[open-vragen]]

## 2026-10-06 — Zoekvolgorde open componenten vastgelegd (1 per 1)
- **Beslissing:** De open componenten worden **een per een** afgehandeld in een vaste werkorder: eerst bordkritisch, dan voeding/RF, verbindingen, ontvanger, mock-up, gereedschap. De lijst staat in [[componenten]] onder *Te zoeken: werkorder*.
- **Reden:** Gebruikersvraag: systematisch nagaan wat nog gezocht moet worden.
- **Gevolg:** In deze ronde zijn de punten 1-4, 7, 10, 12, 15, 20-29 afgehandeld; de rest blijft open.
- **Link:** [[componenten]], [[open-vragen]]

## 2026-10-06 — UART-koppeling: schroefconnectoren, gemeenschappelijke ground en level shifter
- **Beslissing:** Tussen het meettoestel en de Arduino Uno komt een **UART met schroefklem-connectoren**, voorzien van een **gemeenschappelijke ground (GND)** en een **level shifter (3,3 V <-> 5 V)**. De **USB-C datakabel** en de **Dupont-/siliconendraad** heeft de gebruiker al in huis; die komen **niet** op de bestellijst.
- **Reden:** Gebruikersaanwijzing `2026-10-06`: de schroefconnector is bevestigd, de ground en level shifter horen erbij, en de kabel + jumperdraad zijn al aanwezig.
- **Gevolg:** Het type level shifter blijft te zoeken (AI-taak). Grounddraad en level shifter moeten in de bestellijst/op de print worden voorzien. Vastgelegd in [[componenten]] en [[open-vragen]].
- **Link:** [[componenten]], [[open-vragen]], [[besturing-en-commandos]], [[specificaties]]

## 2026-10-06 — Uitbreidingsconnector en level shifter gekozen
- **Beslissing:** De uitbreidingsconnector wordt een **4-pins schroefklem op 3,5 mm-raster** (KF128/KF301) met pinout GND / +5 V / TX / RX. De level shifter wordt de **TXB0104** (4-kanaals bidirectioneel, VCCA 3,3 V, VCCB 5 V), **op de draagprint** geplaatst. **I2C-pull-ups komen niet op de print**: de BNO055- en BMP390-breakouts hebben ze al (enkel 2 reserve-footprints).
- **Reden:** Gebruikersvraag: *kies zelf iets passends*. De schroefklem is robuust en past bij de eerder gekozen schroefconnectoren. TXB0104 is de juiste soort (push-pull, voor UART/SPI); de I2C-bus blijft volledig 3,3 V en heeft dus geen shifter nodig.
- **Gevolg:** De print krijgt een schroefklem-footprint en een TXB0104. De 5 V-referentie voor de shifter komt van de 5 V-rail (buck). Vastgelegd in [[componenten]].
- **Link:** [[componenten]], [[pcb-ontwerp]], [[besturing-en-commandos]]

## 2026-10-06 — Bescherming van de voeding: PTC, P-MOSFET en TVS
- **Beslissing:** De 7,4 V-ingang krijgt een **2 A PTC-zekering**, een **P-MOSFET ompoolbeveiliging** (DMG2301L) en een **TVS-diode SMBJ10A**, plus een **bulk-elco 100 uF/16 V**.
- **Reden:** Gebruikersvraag: *hetgeen dat nodig is volgens jou*. De P-MOSFET beschermt tegen omgekeerde polariteit met weinig spanningsverlies; de PTC begrenst de stroom; de TVS vangt spanningspieken op. Samen de standaard minimale bescherming voor een accugevoed bord.
- **Gevolg:** Vastgelegd in [[componenten]] en de essentials-tabel. Deze onderdelen komen op de draagprint.
- **Link:** [[componenten]], [[pcb-ontwerp]], [[specificaties]]

## 2026-10-06 — Extra 3,3 V-LDO op de print (AP2112K-3.3)
- **Beslissing:** Er komt een **eigen 3,3 V-rail** met een **AP2112K-3.3** (of AMS1117-3.3) op de draagprint voor de sensoren, ook al levert de XIAO zelf 3,3 V.
- **Reden:** Gebruikerskeuze: de LDO is goed en wordt nuttig geacht. Een eigen rail houdt de sensoren gescheiden van de XIAO-rail.
- **Gevolg:** Let op de **LoRa-ontvanger** (tweede XIAO-kit): die hangt via **USB** aan de laptop en heeft zijn **eigen 3,3 V-regelaar** — daar is geen losse LDO nodig. Vastgelegd in [[componenten]].
- **Link:** [[componenten]], [[specificaties]]

## 2026-10-06 — Externe antennes: SMA-pigtail voor LoRa en actieve GNSS-antenne
- **Beslissing:** De LoRa-antenne wordt **buiten het vliegtuigje** geconnecteerd via een **IPEX/U.FL -> SMA female bulkhead pigtail**. Voor de GNSS komt een **actieve dual-band L1/L5-antenne met SMA, LNA en ground plane** (compacte uitvoering, voorbeeld: de dual-band GNSS-antenne van Waveshare), passend bij de LC29H(DA).
- **Reden:** Gebruikersvraag `2026-10-06`: beslist dat de antenne buiten het vliegtuigje moet; voor de GNSS-antenne mocht de AI iets passends kiezen.
- **Gevolg:** Beide antennes komen op de bestellijst. De LoRa-kitantenne blijft behouden. Vastgelegd in [[componenten]].
- **Link:** [[componenten]], [[links]], [[pcb-ontwerp]]

## 2026-10-06 — NTRIP gratis (gebruiker zoekt); socket-merken later
- **Beslissing:** De NTRIP-correctiedienst wordt een **gratis** provider; de **gebruiker zoekt die zelf**. De exacte **merken** voor precisie- en dual-wipe-sockets worden later bepaald en hoeven **niet per se op de bestellijst**.
- **Reden:** Gebruikersaanwijzing `2026-10-06`.
- **Gevolg:** NTRIP-provider blijft als gebruikersactie open; de socket-keuze is een detail voor het schema, geen blokkade. Vastgelegd in [[componenten]] en [[open-vragen]].
- **Link:** [[componenten]], [[open-vragen]], [[links]]
