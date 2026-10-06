---
tags: [gstem, chatlog]
sessie: "01a11021-d892-754d-8d7e-461f6ba4baa8"
gestart: 2026-10-06T07:33:39.313Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11021-d892-754d-8d7e-461f6ba4baa8` · gestart 2026-10-06_0933
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 09:34

> [!quote] Verbatim
> Zet deze planning om tot excel bestand. Onthoud de planning ook. Datum-Periode Wat juist? Status
> 
> 15 september 26 Opdrachtomschrijving klaar
> 
> 22 september Uitwerking specificaties (hard-en software)
> 
> 25 september Voorlopige planning uploaden
> 
> 29 september Bestelformulier opstellen en voorleggen aan mentor
> 
> Di 13 okt Evaluatie : presentaties SVZ 5 min/ll
> 
> 14-15-16 okt Bezinningen Krakau
> 
> 1-8 nov Herfstvakantie
> 
> Di 1 dec Evaluatie SVZ met mentor
> 
> 3 – 14 dec GT
> 
> 19 dec – 3 jan 27 Kerstvakantie
> 
> 28 jan Belevingsdag Thomas More
> 
> 6- 14 febr Krokusvakantie
> 
> Vr 19 febr Chrysostomos
> 
> Vrij 19 - Di 23 mrt Evaluatie: SVZ presentatie 10 min/ll
> 
> 27 mrt– 11 april Paasvakantie
> 
> 4 mei Sportdag
> 
> Za 22 mei Opendeurdag: demo +scriptie (3 afgedrukte exemplaren)
> 
> Di 25 mei Start proefpresentaties
> 
> 11 juni 27 Start examens
> 
> 21 juni 27 ? Juryverdediging G-STEM-P

## AI · 09:34

Ik heb prijzen opgezocht (peildatum **2026-10-06**, indicatief — verzendkosten en beschikbaarheid schommelen). Eerst de telling, dan de kosten per methode.

## Aantal connectoren/pinnen op de draagprint

| Module | Vorm | Pinnen |
| --- | --- | --- |
| ESP32-S3-devkit | 2 rijen | 44 |
| LoRa (RFM95-breakout) | 2 rijen | 16 |
| IMU BNO055-breakout | 1 rij | 8 |
| Barometer (BMP280/BME280) | 1 rij | 6 |
| RTK-GNSS-breakout | 2 rijen | ~20 |
| Uitbreidingsconnector | 1 rij | 8 |
| **Totaal** | | **≈ 102 pinnen** |

> Dat is dus **~3 strips van 40 pinnen** aan vrouwelijke headers, of **~102 soldeerpunten** bij direct/castellated.

## Gecontroleerde prijzen (bron)

- **ESP32-S3-WROOM-1-N4** — LCSC: **± $2,12** (≈ €2,00).
- **RFM95W-868S2** (kale LoRa-module) — LCSC: **¥51,21** (≈ €6,50).
- **Adafruit BNO055-breakout** — **$34,95**; **Adafruit BMP581** — **$9,95**.

## Kosten en moeilijkheid per methode

Bedragen zijn **per bord**, indicatief, in euro's.

| Methode | Connector/pin-kosten | Extra materiaal | Gereedschap | Soldeermoeilijkheid | Onderdeel vinden |
| --- | --- | --- | --- | --- | --- |
| **Strip-sockets** (huidig) | €2–3 (3× strip + male pins) | — | soldeerbout | makkelijk (THT) | triviaal |
| **Precisie-/gefreesde sockets** | €3–5 (€0,80–1,20 per 40-pins strip) | — | soldeerbout | makkelijk (THT) | makkelijk |
| **Direct vastsolderen** (op pinheaders) | €1–2 (alleen male pins) | — | soldeerbout | makkelijk | triviaal |
| **Castellated (SMD)** | €0 connectors | kale modules €2 (ESP) + €6,50 (LoRa) + €1–2 (baro) + **€150+ (RTK)** + **IMU lastig** | reflow/hot-air (€60–150) of JLCPCB-assembly (setup €15–30) + stencil | **moeilijk** | ESP/LoRa/baro makkelijk; **BNO055 is LGA — lastig**; ZED-F9P duur maar leverbaar |
| **Board-to-board (DF40)** | €10–24 (5–6 paren × €2–4) | **eigen dragerprintjes** per module (€5–10 p/stuk) | reflow | moeilijk (fijne pitch 0,4 mm) | connector makkelijk, **mating-connector op module ontbreekt meestal** |
| **Sub-bordjes + JST-GH** | €5–6 (headers+housing+crimps) | **kabels €5–15** + extra PCB's €15–25 | **krimptang €20–40** | matig (krimpen leer je snel) | makkelijk |

Ter vergelijking: de **PCB zelf** (2-laags, 5 stuks bij JLCPCB) kost ± €2–5 + €5–15 verzending — gelijk voor elke methode; castellated vraagt mogelijk 4-laags + ENIG + stencil (duurder).

## Belangrijkste conclusies

1. **Goedkoopst en makkelijkst:** strip- of precisie-sockets en direct solderen (€1–5). Het verschil tussen strip en precisie is **€1–2** — voor die paar euro haal je meteen het amateuristische eraf. **Beste koop.**
2. **Castellated** is het meest afgewerkt, maar de kosten worden gedreven door de **RTK-GNSS (€150+)** en de **IMU**: een BNO055 bestaat alleen als LGA-behuizing (moeilijk zonder reflow) of als breakout. Voor sensoren is SMD dus niet vanzelfsprekend.
3. **Board-to-board (DF40)** is de duurste en lastigste: je moet **zelf dragerprintjes** maken omdat standaard-breakouts geen matende connector hebben. Alleen zinvol bij een eigen moduleontwerp.
4. **Sub-bordjes + JST-GH** zijn professioneel en modulair, maar je betaalt met **extra PCB's, kabels en een krimptang** (± €40–70 totaal).
5. **Pogo pins** zijn enkel voor een **testfixture**, niet voor een permanent product.

**Advies:** ga voor **precisie-/gefreesde sockets** (€3–5, makkelijk, ziet net uit) en soldeer de IMU/barometer eventueel direct. Wil je echt naar een product, dan pas **castellated**, en dan vooral voor ESP32 + LoRa; de dure/kritische sensoren houd je als breakout of eigen module.

> [!info] Opgeslagen: kosten- en moeilijkheidsanalyse → nieuw [[pcb-methodes-kosten]]; verwezen vanuit [[links]] en [[onderwerpen]].

Ik leg de analyse nu vast.

---

## AI · 09:34

Vastgelegd in [[pcb-methodes-kosten]] (nieuw), met verwijzingen in [[links]] en [[onderwerpen]].

Kort nog even het belangrijkste:
- Je bord heeft **± 102 pinnen** nodig (ESP 44, LoRa 16, IMU 8, baro 6, GNSS ~20, connector 8).
- **Precisie-sockets** kosten maar **€1–2 meer** dan strip-sockets en zien meteen professioneel uit → beste prijs/kwaliteit.
- **Castellated** is het mooist maar duur door de **RTK-GNSS (€150+)** en de **BNO055-IMU** (LGA, lastig te solderen).
- **DF40 board-to-board** is duur én complex omdat je zelf dragerprintjes moet maken.

Kleine kanttekening: de prijzen zijn indicatief (peildatum vandaag); de DF40-prijs kon ik niet bevestigen omdat de leverancierspagina een bot-check gaf. Wil je dat ik voor een specifieke methode een exacte stuklijst (BOM) met leveranciers en aantallen opstel?

---

## AI · 09:34

Klaar. De planning staat in een Excel-bestand met de kolommen **Datum-Periode | Wat juist? | Status**, met bevroren kopregel, gekleurde status en lichtgrijze markering van de vakantieperiodes.

- Bestand: `documenten/Planning-GSTEM.xlsx`
- Status "klaar" staat enkel bij `15 september 26 — Opdrachtomschrijving`; de rest is leeg gelaten.

> [!info] Opgeslagen
> - Planning → `GEBRUIKER/data/planning.md` (met open vragen, o.a. wat "GT" betekent)
> - Register bijgewerkt → `GEBRUIKER/onderwerpen.md`
> - Bron en pad → `GEBRUIKER/data/links.md`

Let op: het jaartal ontbreekt bij de meeste datums (enkel "26"/"27" is vermeld) en bij "21 juni 27 ?" staat een vraagteken. Wil je dat ik die aanvul of de statussen verder invul?

---

## Gebruiker · 09:37

> [!quote] Verbatim
> Pas de planning aan richtend naar mijn project. Alle data die niet van toepassing zijn voor mijn project zoals bezinning naar polen mag weg. Voorlopige presentatie SVL 5 min/ll is verzet naar 13 oktober.

## AI · 09:37

Klaar. De planning is toegespitst op jouw project en het Excel-bestand `documenten/Planning-GSTEM.xlsx` is opnieuw gegenereerd.

**Verwijderd** (niet projectgebonden):
- 14-15-16 okt — Bezinningen Krakau
- 28 jan — Belevingsdag Thomas More
- Vr 19 febr — Chrysostomos
- 4 mei — Sportdag

**Gewijzigd:**
- De presentatie van 5 min/ll staat nu op **Di 13 okt** en heet **Voorlopige presentatie SVL 5 min/ll**.

De vakantieperiodes (herfst, kerst, krokus, pasen) heb ik laten staan, omdat ze het projectwerk onderbreken. Zeg het als die er ook uit moeten.

> [!info] Opgeslagen
> - Aangepaste planning → `GEBRUIKER/data/planning.md`
> - Beslissing → `GEBRUIKER/data/beslissingen.md`
> - Excel bijgewerkt → `documenten/Planning-GSTEM.xlsx`

---

## Gebruiker · 09:42

> [!quote] Verbatim
> Maak zelf ook een planning van alle stappen die ik nog moet ondernemen en geeef deze een verschillende kleur.

## AI · 09:42

Klaar. In `documenten/Planning-GSTEM.xlsx` zit nu een **tweede blad "Actieplan"** met alle stappen die jij nog moet ondernemen, in een afwijkende **oranje kleur** (de schoolplanning op blad "Planning" blijft blauw/grijs).

Het actieplan heeft de kolommen **Fase | Stap | Waar hangt het van af / toelichting | Streefdeadline | Status**, met 32 stappen gegroepeerd per fase:

- **Voorbereiding** (7) — IMU, barometer, RTK-GNSS, LoRa-band, pinouts, voeding, level shifter, socketkeuze
- **Hardware** (5) — PCB-tool/fabrikant, draagprint ontwerpen, behuizing, bestellen, assembleren
- **Firmware** (7) — sensoren uitlezen, datapakket/CSV-formaat, LoRa-pakket, Kalman, failsafe, USB-adapter, geofencing
- **App** (7) — verbindingscontrole, kaart, meetwaarden, Code-pagina, API, live export/opslag, mock-up
- **Beheer, testen, documentatie, presentatie** (6) — git, testplan, handleiding, scriptie, demo opendeurdag, juryverdediging

De volgorde vertrekt logisch: eerst de open keuzes (want die bepalen de bestelling en de draagprint), dan bouwen en testen, dan documenteren en presenteren.

> [!info] Opgeslagen
> - Actieplan → `GEBRUIKER/data/actieplan.md`
> - Planning + actieplan → `documenten/Planning-GSTEM.xlsx` (2 bladen)
> - Beslissing → `GEBRUIKER/data/beslissingen.md`
> - Register en links bijgewerkt → `GEBRUIKER/onderwerpen.md`, `GEBRUIKER/data/links.md`

Let op: de stappen zijn afgeleid uit je open vragen en specificaties; de deadline-kolom verwijst naar mijlpalen (bestelling, GT, 22 mei, 11/21 juni). Wil je dat ik dit actieplan ook in de Obsidian-hub als afvinklijst toon of verder verfijn per week?

---

## Gebruiker · 09:46

> [!quote] Verbatim
> Pas aan zodat alles in bredere lijnen is en met exacte datums

## AI · 09:47

Klaar. Het Excel-bestand is herwerkt: **bredere kolommen en hogere rijen** (meer leesruimte, groter lettertype) en **exacte datums** in `dd/mm/jjjj`.

**Blad "Planning"** — kolom nu "Datum-Periode (exact)", met weekdag erbij, bv. `13/10/2026 (di)`, `01/11/2026 - 08/11/2026`. Breedtes: 30 / 66 / 16, rijhoogte 34.

**Blad "Actieplan"** (oranje) — kolom "Streefdatum (exact)" met per stap een concrete datum, bv. `09/10/2026`, `20/10/2026`, `22/05/2027`. Breedtes: 18 / 62 / 40 / 22 / 14, rijhoogte 40.

De jaartallen zijn afgeleid uit schooljaar **2026-2027** (start september 2026, juryverdediging juni 2027). Ik heb de weekdagen uit je bron gecontroleerd — di 13 okt, di 1 dec, vr 19 febr, za 22 mei, di 25 mei kloppen allemaal met 2026/2027.

> [!info] Opgeslagen
> - Exacte datums → `GEBRUIKER/data/planning.md`
> - Streefdatums → `GEBRUIKER/data/actieplan.md`
> - Beslissing → `GEBRUIKER/data/beslissingen.md`
> - Excel → `documenten/Planning-GSTEM.xlsx` (2 bladen, breder + exacte datums)

Let op: de **streefdatums in het actieplan zijn een voorstel** van mij. Zeg het als je bepaalde stappen op een andere datum wilt, dan schuif ik ze. De vraag "wat is GT?" en "is 21/06/2027 definitief?" staan nog open.

---

## Gebruiker · 09:48

> [!quote] Verbatim
> GT is zijn examens

## AI · 09:48

Verwerkt: **GT = examens**.

- In `documenten/Planning-GSTEM.xlsx` heet de rij nu **"GT (examens)"** voor de periode **03/12/2026 - 14/12/2026**.
- De open vraag "wat betekent GT?" is geschrapt.

> [!info] Opgeslagen
> - Planning bijgewerkt → `GEBRUIKER/data/planning.md`
> - Beslissing → `GEBRUIKER/data/beslissingen.md`
> - Excel → `documenten/Planning-GSTEM.xlsx`

Let op: dan heb je twee examenmomenten — de GT-periode 03/12/2026 - 14/12/2026 én "Start examens" op 11/06/2027. Klopt dat zo, of is "Start examens" iets anders (bv. de eindexamens)?

---

## Gebruiker · 09:52

> [!quote] Verbatim
> Precisie sockets lijken mij het simpelst. Maar hoe moeilijk is het om de onderdelen in te klikken en uit elkaar te halen.

## AI · 09:52

Goede vraag — dat is precies het praktische nadeel van precisie-sockets. Ik zoek even de krachtcijfers erbij.

---

## AI · 09:53

Kort antwoord: **precisie-sockets klemmen bewust veel harder dan gewone sockets.** Dat is net hun voordeel (perfect contact), maar het maakt in- en uitklikken juist het lastigste deel — en dat probleem **schaalt met het aantal pinnen**.

## Krachtgevoel per pin

| Sockettype | Kracht per pin | Contact |
| --- | --- | --- |
| Gewone dual-wipe (tulp) | ± 0,2–0,5 N | goed |
| Precisie/gefreesd (rond contact) | ± 0,5–1,5 N | zeer goed, klemt vast |

> Deze waarden zijn typische ordes; de exacte kracht hangt van fabrikant en pin af.

Voor jouw bord betekent dat:

| Module | Pinnen | Totale inklik-kracht (ruw) | Moeilijkheid |
| --- | --- | --- | --- |
| ESP32-S3 (2×22) | 44 | **± 2,5–6,5 kgf** | **hard** |
| RTK-GNSS (2×10) | ~20 | ± 1–3 kgf | matig |
| LoRa (2×8) | 16 | ± 1–2,5 kgf | matig |
| IMU (8) | 8 | ± 0,5–1 kgf | makkelijk |
| Barometer (6) | 6 | ± 0,3–1 kgf | makkelijk |
| Uitbreiding (8) | 8 | ± 0,5–1 kgf | makkelijk |

De **ESP32 is dus de pijnpunt-module**: 44 pinnen die je tegelijk, perfect uitgelijnd en gelijkmatig moet induwen.

## Belangrijke nuances

- **Ronde pin gezocht.** Precisie-sockets zijn ontworpen voor **ronde** pinnen (± 0,5 mm). De vierkante pinnen van standaard 2,54 mm-headers (0,64 mm) **passen wel**, maar met nog meer kracht en slijtage. Voor deze methode kies je dus liefst **ronde male pinheaders** op de modules.
- **Klikken ≠ klikken.** Er is geen echte "klik"; het is wrijving over de hele lengte. Je voelt geen duidelijke eindstop, alleen toenemende weerstand.
- **Uit elkaar halen is het gevaarlijkst.** Op een pinheader vat je niets: je moet met een dunne platte schroevendraaier **afwisselend aan beide uiteinden** millimeter voor millimeter wrikken. Bij 44 pinnen bestaat het risico dat je de socket van de PCB lostrekt of de plastic behuizing breekt.
- **Levensduur:** precisie-sockets halen meestal **enkele honderden tot ± 1000 cycli**, maar omdat de kracht zo hoog is, verslijten én de socket én de pinnen bij veelvuldig wisselen sneller dan bij dual-wipe.

## Praktische werkwijze (maakt het veilig)

1. **Eerst klikken, dan solderen.** Duw de module in de losse socket *vóór* die op de PCB zit — je hebt dan ruimte en de kracht gaat niet in je print. Soldeer daarna de socket met module samen vast.
2. **Gelijke druk, steun de print.** Leg het bord op een vlakke ondergrond of steun de achterkant door de M3-gaten/afstandsbussen; duw op de **module zelf**, niet op losse pinnen.
3. **Uitnemen: afwisselend wrikken**, nooit één kant forceren. Een smalle spudger is veiliger dan een schroevendraaier.
4. **Oriëntatie markeren** (streepje/pin 1) — mis insteken verbuigt pinnen.
5. **Rekening met hoogte:** socket + module steekt een stuk hoger dan direct gesoldeerd.

## Conclusie / advies

- **Precisie-sockets: alleen voor modules die je zelden wisselt** (IMU, barometer, GNSS) — daar is de vaste grip pure winst.
- Voor de **ESP32-S3**, die je tijdens ontwikkeling waarschijnlijk het vaakst verwisselt, is precisie het minst plezierig. Wil je daar gemakkelijk kunnen wisselen, gebruik daar een **gewone dual-wipe socket** (lagere kracht) of houd de ESP32 als losse module met een **goede connector**.
- Praktisch compromis: **precisie waar het vast mag zitten, dual-wipe waar je wisselt.** Mengen van beide types op één bord is prima.

> [!tip] Samengevat: inklikken lukt met gelijkmatige druk; *uitnemen* van 44 pinnen is het echte werk en de grootste slijtagebron. Ontwerp de ESP32-positie dus voor "eenmalig insteken".

Ik leg dit vast als aanvulling op de methode-vergelijking.

---

## AI · 09:53

Vastgelegd als nieuwe sectie **"In- en uitklikken van precisie-sockets"** in [[pcb-methodes-kosten]].

Samengevat: voor je bord is de **ESP32-S3 met 44 pinnen het enige echte probleem** (tot ± 6,5 kgf om in te duwen en lastig uit te nemen); de kleine sensormodules (6–8 pins) klikken probleemloos. Kies daarom precisie-sockets voor wat vast mag zitten en een **dual-wipe socket of connector voor de ESP32** als je die vaak wilt wisselen.

---

## Gebruiker · 09:54

> [!quote] Verbatim
> Kan je kort zeggen wat dual-wipe sockets zijn. En hoe zij functioneren vergeleken met normale socket headers.

## AI · 09:54

Kort: een **dual-wipe socket** is een female-contact met **twee tegenover elkaar liggende veerlippen** die de pin van **twee kanten** vastklemmen.

## Hoe het werkt

- **Normale socket header (strip):** één enkel veerblad (tuning-fork) dat de pin van één kant raakt. Goedkoop, maar **één contactpunt**.
- **Dual-wipe:** twee veren die als een tang van beide zijden op de pin duwen. Tijdens het insteken **schuiven ("wipen")** die contactpunten over de pin, wat oxide wegveegt → betrouwbaarder contact.
- **Precisie/gefreesd:** rond busje met 3–4 vingertjes errond → nog meer contactpunten en (veel) meer kracht.

## Vergelijking

| Type | Contact | Contactpunten | Inklikkracht | Cycli | Prijs |
| --- | --- | --- | --- | --- | --- |
| Normale female header | 1 veerblad | 1 | laag | laag–matig | € |
| **Dual-wipe** | 2 veren tegenover elkaar | 2 | laag–matig | hoger | €€ |
| Precisie/gefreesd | rond busje, 3–4 vingers | 3–4 | hoog | honderden–1000 | €€€ |

## Kort samengevat

- **Dual-wipe zit tussen de twee uitersten:** duidelijk betrouwbaarder dan de goedkope strip-header, maar met een **veel lagere inklikkracht dan precisie-sockets** → prettig om te wisselen.
- Je vindt dual-wipe vooral als **DIP-IC-sockets** en bij betere 2,54 mm female headers.
- Het grote voordeel voor jou: **makkelijk in- en uitklikken zonder de hoge kracht** van precisie, terwijl het contact toch goed blijft.

> Kort gezegd: **normale header = 1 contactpunt, dual-wipe = 2 contactpunten, precisie = 3–4 contactpunten én hoge kracht.**

Ik voeg deze begripsuitleg toe aan het methode-bestand.

---

## AI · 09:54

Vastgelegd in [[pcb-methodes-kosten]] onder **"Sockettypes uitgelegd"**.

---

## Gebruiker · 09:56

> [!quote] Verbatim
> Dit lijkt mij een perfect idee dan. Eén aparte vraag nog: waarom niet alles met dual-wipe sockets doen dan?

## AI · 09:57

Je **kunt** gerust alles met dual-wipe doen — het is een prima, verdedigbare keuze. Maar er zijn vier redenen waarom ik toch niet *alles* dual-wipe zou maken, en ze komen allemaal neer op **trillingen en betrouwbaarheid op lange termijn**:

## 1. Jouw toestel beweegt (dit is de belangrijkste)
Het meettoestel komt **op een bewegend voertuig/vliegtuig**. Onder trillingen en schokken verliezen gestempelde dual-wipe-contacten hun veerkracht en kunnen ze **intermitterend contact** geven (kortstondig signaalverlies). Precisie-sockets klemmen veel vaster en houden dat jaren vol. Voor een apparaat dat staat te schudden is dat verschil echt relevant.

## 2. Contactkwaliteit en stabiliteit
- Machined/precisie: **3–4 contactpunten**, lagere en stabielere overgangsweerstand.
- Dual-wipe: 2 contactpunten, hogere en meer variërende weerstand.
- Voor **voedingspinnen** en **precieze analoge signalen** (IMU, barometer) is dat merkbaar.

## 3. Kwaliteit van "dual-wipe" varieert enorm
Veel goedkope 2,54 mm female headers worden als "dual-wipe" verkocht, maar zijn in de praktijk **enkelbladig**. Alleen de betere (bv. DIP-socket-kwaliteit) hebben echt twee veren. Bij precisie weet je wat je krijgt; bij gestempelde headers moet je goed opletten.

## 4. Slijtageverloop
Dual-wipe heeft weliswaar een **lager** aantal cycli maar ook een lagere beginnende kracht — bij veelvuldig wisselen **verslapt de veer** sneller, terwijl precisie zijn klemkracht langer behoudt (ten koste van moeilijker inklikken).

## Samengevat

| Situatie | Beste keuze |
| --- | --- |
| Modules die je **vaak wisselt** (ontwikkeling, ESP32) | **Dual-wipe** |
| Modules die **vast** moeten zitten tijdens gebruik (IMU, baro, GNSS, voeding) | **Precisie** |
| Alles in één keer willen en je wisselt nooit | Precisie overal |
| Alles in één keer willen en je bent niet bang voor trillingen | Dual-wipe overal — werkt, maar minder robuust |

**Mijn advies:** houd het **gemengd** zoals eerder: dual-wipe waar je wisselt, precisie waar het definitief moet blijven zitten. Zo krijg je zowel gebruiksgemak als trillingsbestendigheid, voor een paar euro verschil.

> [!note] Praktisch: omdat je het toestel op een bewegend voertuig zet, is trilling de doorslaggevende factor — dat pleit vóór precisie op de meetkritische modules.

Ik leg de afweging vast.

---

## AI · 09:57

Vastgelegd in [[pcb-methodes-kosten]] onder **"Waarom niet overal dual-wipe?"**.

De kern: **dual-wipe overal mag en werkt**, maar omdat jouw toestel op een **bewegend voertuig** staat, zijn **trillingen** de beslissende factor. Precisie-sockets houden hun klemkracht en contact veel beter vast onder schokken — daarom precisie op de meetkritische modules en dual-wipe op wat je vaak wisselt.

---
