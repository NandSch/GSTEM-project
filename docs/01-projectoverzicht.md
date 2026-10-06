# 01 · Projectoverzicht — G-Stem / GSN / AeroLink

> Bronnen: `CODEXIMPORT/PROJECT_CONTEXT.md`, `CODEXIMPORT/G-Stem_specificaties_concept.docx`,
> `CODEXIMPORT/GSN-project_draadloze_3D-meetmodule.docx`, `CODEXIMPORT/Blokschema_AeroLink.drawio`.

## Doel en status

Schoolproject rond een **compact, draadloos meettoestel dat positie en beweging meet**. De
definitieve productnaam is **Positie- en beweging meettoestel met LoRa integratie** (de werktitel
*AeroLink* vervalt, `2026-10-01`). Hardware, firmware en laptopapp zijn in ontwerp. Het document
`G-Stem_specificaties_concept.docx` is een aanvullende conceptbron; de details daarin zijn nog geen
definitieve technische specificatie. De door de gebruiker **afgewerkte gebruikersspecificaties**
(`2026-10-06`, zie hieronder) vormen de actuele productbeschrijving.

De map `CODEXIMPORT/visual-prototype/` bevat een **visuele mock-up** van de geplande laptopapp. Die
toont de beoogde indeling en gegevensstroom met fictieve waarden. De demo maakt geen echte USB- of
LoRa-verbinding, leest geen sensoren uit, voert geen gebruikerscode uit en bestuurt geen voertuig.

## Beoogde meetmodule (hardware)

- **Eigen PCB** met pinheaders/connectoren waarop insteekbare breakoutboards geplaatst en vervangen
  kunnen worden. PCB-sporen verzorgen data en voeding; de exacte borden en pinbezetting moeten nog
  gekozen worden.
- **ESP32-S3 met LoRa-radio en antenne** als centrale controller. Firmware leest de sensoren,
  bundelt metingen in pakketten en zendt die draadloos uit.
- **9-DoF IMU met sensorfusie** voor absolute oriëntatie. **BNO055 is een mogelijke kandidaat, geen
  vastgelegde keuze.** Gewenste gegevens: quaternion en/of Euler-hoeken, hoeksnelheid, versnelling,
  magnetisch veld, lineaire versnelling, zwaartekracht en sensortemperatuur.
- **Barometer** voor luchtdruk en hoogte-inschatting.
- **RTK-GNSS-module met antenne** voor geografische positie.
- **Batterij, USB-C** en passende beveiliging/spanningsregeling (laad-, programmeer- en
  voedingsschakeling nog uit te werken).
- **3D-geprinte behuizing met demping**: het project vergelijkt meetgedrag met en zonder schokken of
  trillingen.
- **Uitbreidingsconnector** met signaalpinnen en massa voor kabels naar een bestaande
  voertuigcontroller. Signaaltype, elektrische interface, spanningsniveaus en veiligheidsgrenzen
  zijn nog te bepalen.
- **Optionele uitbreiding**: tweede microcontroller en twee servo's op een stilstaande
  vliegtuigmock-up.

## Draadloze en softwareketen

```text
IMU + barometer + RTK-GNSS
          ↓
ESP32-S3 op de meetmodule → LoRa → tweede ESP met LoRa → USB → laptopapp
          ↑                                                    ↓
bestaande voertuigcontroller ← kabel/connector ← meetmodule ← LoRa ← USB-adapter ← berekend commando
```

Het tweede ESP-bord met LoRa dient **bij de laptop** als ontvanger én zender en is via USB
aangesloten. De laptopsoftware is bedoeld als **één installeerbare app**, met benodigde
bibliotheken en onderdelen inbegrepen.

### Beoogde appflow

1. Het **startscherm** vraagt om de USB-adapter aan te sluiten en controleert die verbinding.
2. Vervolgens controleert de app apart of geldige **meetpakketten via LoRa** aankomen.
3. Na een geslaagde verbinding opent het **hoofdscherm** met twee modi: **Livekaart** en
   **Programmering & besturing**.

**Livekaart:** links een interactieve, Google-Earth-achtige 3D-kaart met actuele positie, richting
en snelheid en een rode lijn voor de afgelegde route. Rechts ruwe actuele waarden, waaronder
coördinaten, hoogte, snelheid, oriëntatie en verbindingsstatus. Het conceptdocument noemt ook het
bewaren van metingen en route voor latere analyse.

**Programmering & besturing:** meetdata gaat naar eigen code of via een gedocumenteerde lokale
interface naar een extern proces. Dat kan acties berekenen voor een RC-auto of een stilstaande
vliegtuigmock-up. Berekende commando's keren via USB-adapter en LoRa naar de meetmodule terug en
gaan via de uitbreidingsconnector naar de bestaande voertuigcontroller. Een **veilige stop bij
verbindingsverlies of ongeldige commando's** is een vereiste voor een werkende uitvoering; de
concrete aanpak moet nog worden ontworpen.

Als optionele demonstratie is eerder een stilstaande vliegtuigmock-up met een tweede microcontroller
en twee servo's genoemd. Een vliegend toestel is **geen** vereiste.

## Uitgebreide specifi catielijst (concept-docx)

### Hardware
- Eigen PCB met pinheaders/connectoren voor vervangbare breakoutmodules; PCB-sporen verbinden
  voeding en datacommunicatie.
- ESP32-S3-breakout met LoRa-radio en antenne als centrale microcontroller.
- 9-DoF IMU met sensorfusie (quaternion/Euler, hoeksnelheid, versnelling, magnetisch veld, lineaire
  versnelling, zwaartekracht, sensortemperatuur).
- Barometer (luchtdruk + geschatte hoogte).
- RTK-GNSS-module met antenne.
- Tweede ESP met LoRa als zend-/ontvangstadapter bij de laptop, verbonden via USB.
- Batterij met beveiliging en spanningsregeling.
- USB-C voor laden en/of programmeren en testen.
- 3D-geprinte behuizing met demping.
- Uitbreidingsconnector met signaalpinnen en massa naar de bestaande voertuigcontroller.
- Optioneel: tweede microcontroller + twee servo's op een stilstaande vliegtuigmock-up.

### Software
- Eén installeerbare laptopapp met meegeleverde bibliotheken/onderdelen.
- Firmware meetmodule: leest IMU, barometer en RTK-GNSS, bundelt pakketten, verzendt via LoRa.
- Firmware LoRa-adapter: geeft meetpakketten via USB door en stuurt commando's terug via LoRa.
- Startscherm vraagt eerst de LoRa-ontvanger via USB aan te sluiten.
- App controleert eerst USB-verbinding, daarna of geldige datapakketten via LoRa binnenkomen; beide
  statussen worden apart getoond.
- Na geslaagde verbinding: hoofdscherm met **Livekaart** en **Programmering & besturing**.
- Rechts actuele meetwaarden (coördinaten, hoogte, snelheid, oriëntatie).
- Links interactieve 3D-kaart met positie, richtingspijl en rode routelijn.
- Programmering & besturing: eigen verwerkingscode of uitbreidingen toevoegen die meetdata omzetten
  in acties.
- Live meetgegevens via gedocumenteerde lokale interface naar een extern programma.
- Berekende stuurcommando's via USB-adapter en LoRa terug naar de meetmodule → uitbreidingsconnector
  → bestaande voertuigcontroller.
- Veilige stop bij verbindingsverlies of ongeldige commando's.
- Meetgegevens en route bewaren voor latere analyse/weergave.
- Optioneel: apart programma/proces berekent acties voor een RC-auto of vliegtuigmock-up.

## Afgewerkte gebruikersspecificaties (2026-10-06)

De gebruiker leverde de afgewerkte, gebruikersgerichte specificaties aan
(`documenten/GStem-Specificaties.md`; samengevat in `GEBRUIKER/data/gstem-specificaties.md`). Kern:

- **Meetprestaties:** vier grootheden — **richting** (graden, horizontaal en verticaal vlak),
  **snelheid** (km/u), **hoogte** (nauwkeurig tot **1,5 m**) en **locatie** (nauwkeurig tot **0,5 m**).
- **Ontvanger en bereik:** draadloze ontvanger in **USB-stickvorm** in de laptop; bereik
  **max. 4 km**.
- **Aanzetten:** het meettoestel start **automatisch** mee met het voertuig (LED toont actief); de
  laptopapplicatie **start vanzelf** zodra de USB-ontvanger wordt ingestoken.
- **App-schermen:** eerst verbindingscontrole met **OK**; dan **3D-kaart met Google-satellietfoto's**
  (afgelegde weg en kijkrichting) plus **tabel** met losse meetwaarden; het scherm **Code** (editor,
  rechtervensters met uitleg en variabelen, CSV naar de controller, uploadknop); het scherm **API**
  (aan/uit, verbinding testen, adres). Op elk scherm staat de status van USB-ontvanger en
  meettoestel.
- **CSV en API:** waarden naar de controller reizen als **CSV**; de gebruiker bepaalt de betekenis
  per waarde. De **API** geeft alle metingen door aan een **extern programma**, dat instructies kan
  terugsturen.
- **RC-vliegtuig-mock-up:** een **Arduino** neemt CSV-waarden aan en is via **TX/RX** met het
  meettoestel verbonden; de **rolroeren, het hoogteroer en het richtingsroer** reageren op de
  metingen en de Arduino stelt de **servo's** in. Dit is een **zittend voorbeeld**, geen volledig
  functioneel vliegtuig. **Testen:** kalibratie en feedbacklus.

## Nog te beslissen of te onderzoeken

| Onderwerp | Open vraag |
| --- | --- |
| Elektronica | Exacte breakoutboards, IMU-model, pinout, interfaces, voedingsspanningen, batterijcapaciteit en stroombudget. |
| Voeding | USB-C-rol, laden, beveiliging en spanningsregeling. |
| RTK | Correctiebron, transport naar GNSS en haalbare nauwkeurigheid. |
| Metingen | Meetfrequentie, tijdstempels, sensorfusie, kalibratie en dataformaten. |
| LoRa | Pakketformaat, band/regio, snelheid, bereik, bevestiging en gedrag bij pakketverlies. |
| Kaart | Kaartbron, licentie, offline gebruik en gewenst 3D-terreindetail. |
| Laptopapp | Framework, platformen, opslag van metingen, interface voor eigen code of extern proces en beveiliging daarvan. |
| Besturing | Commandoformaat, terugkoppeling, elektrische koppeling met de bestaande controller en veilige stop bij verbindingsverlies. |
| Mechanica | Behuizing, demping en proefopzet voor vergelijking met/zonder schokken en trillingen. |

## Terminologie

- **G-Stem / GSN** — projectnaam.
- **AeroLink** — werktitel van de meetmodule (nog niet definitief).
- **GSTEMAPPPREVIEWWEB** — de nieuwere, werkende webversie van de laptopapp-mock-up.
- **CODEXIMPORT** — de oudere documentenmap met o.a. het eerste `visual-prototype`.
