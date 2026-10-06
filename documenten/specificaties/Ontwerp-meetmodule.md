# Ontwerp voor ***Positie- en beweging meettoestel met LoRa integratie***

*Versie: concept, aangevuld met de technische uitwerking.*

> [!tip] Zo lees je dit document
> De tekst beschrijft het volledige systeem: hardware, firmware, communicatie en de laptopapplicatie.
> Wat **vastgelegd** is, staat als gewone tekst. Wat nog niet beslist is, staat in een blok **Nog te bepalen**.
> Achteraan staat een tabel met alle open keuzes bij elkaar.

## Inleiding

Ik ga de technische specificaties van een systeem beschrijven voor het meten van positie en beweging. Het project richt zich op het ontwikkelen van een eigen hardware-module en bijbehorende software. Het doel is om nauwkeurige sensordata op te vangen, te verwerken en visueel weer te geven via een applicatie op een laptop.

Het systeem bestaat uit drie onderdelen die samen een keten vormen:

- **De meetmodule** zit in of op het toestel dat we meten. Hij leest de sensoren uit, bundelt de metingen tot datapakketten en verstuurt die draadloos met LoRa.
- **De LoRa-adapter** hangt met een USB-kabel aan de laptop. Hij ontvangt de pakketten van de meetmodule en stuurt ze door naar de laptop. In de andere richting geeft hij de commando's van de laptop terug door naar de meetmodule.
- **De laptopapplicatie** toont de meetgegevens live op een kaart en in een cijfertabel, laat de gebruiker zelf besturingscode schrijven en kan de meetgegevens live doorgeven aan een eigen programma.

De gegevensstroom loopt dus in twee richtingen: van de sensoren naar de laptop (uplink) en van de laptop terug naar het toestel (downlink). Hieronder beschrijf ik eerst de hardware en daarna de software.

| Onderdeel | Plaats | Taak |
| --- | --- | --- |
| Meetmodule | in of op het toestel | sensoren uitlezen, pakketten maken, LoRa zenden en ontvangen |
| LoRa-adapter | aan de laptop, via USB | doorgeefluik tussen LoRa en de laptop |
| Laptopapplicatie | laptop | weergeven, code uitvoeren, gegevens doorgeven aan een eigen programma |

## Hardware Specificaties

### De Meetmodule

De kern van het project is een zelfontworpen printplaat (PCB). Op deze PCB worden verschillende breakout modules geplaatst die indien nodig vervangen kunnen worden. De sporen op de printplaat zorgen voor de verbindingen voor voeding en datacommunicatie tussen de componenten. De PCB is voorzien van bevestigingspunten in de hoeken om de module veilig te monteren aan de dempingsbehuizing.

De breakout modules worden op **socket-headers** geplaatst in plaats van rechtstreeks vastgesoldeerd. Zo kan een defecte of verbeterde module vervangen worden zonder de hele print opnieuw te maken. De sporen op de print doen twee dingen:

- **Voeding:** vaste rails voor de accuspanning, 5 V en 3,3 V, telkens met een eigen ground.
- **Datacommunicatie:** I2C voor de IMU en de barometer, UART voor de RTK-GNSS-module en voor de verbinding met het besturingssysteem van het toestel, en de nodige pinnen voor de LoRa-radio.

De print krijgt een **power-LED** met serieweerstand op de geregelde voedingsrail, zodat zichtbaar is dat de module onder spanning staat. Verder krijgt de print **decoupling** (100 nF per module, bulk per rail), de nodige **I2C-pull-ups** en de **beveiliging van de voeding** (zekering, beveiliging tegen omgekeerde polariteit).

De print krijgt **vier bevestigingsgaten in de hoeken** (bijvoorbeeld M3) met afstandsbussen, zodat de print vrij van de behuizing blijft. De LoRa-radio zendt met een antenne dicht bij de gevoelige sensoren; daarom krijgt de print een ground plane en worden de antenne en de sensoren zo ver mogelijk uit elkaar geplaatst om storing op de IMU en de barometer te beperken.

> [!question] Nog te bepalen
> De afmetingen en de laagopbouw van de print. Voorlopig gaan we uit van een twee-laags print; of dat voldoende is, hangt af van het aantal netten en de storingsgevoeligheid.

### Elektronische Componenten

Centraal in de meetmodule staat de ESP32-S3-breakoutbord met een LoRa-radio en antenne. Deze microcontroller fungeert als het centrale brein. Omdat de ESP warmte genereert, is een heatsink voorzien voor eventuele koeling. Voor positie- en bewegingmetingen zijn een 9-DoF IMU sensor en een barometer voor luchtdruk geïntegreerd. Een RTK-GNSS-module met antenne zorgt voor de nauwkeurige positiebepaling.

De ESP32-S3 doet al het werk in de meetmodule: hij leest de sensoren uit, bundelt de metingen tot datapakketten, rekent de sensorfusie uit en stuurt de LoRa-radio aan. Daarnaast geeft hij commando's van de laptop door aan het besturingssysteem van het toestel.

| Component | Rol | Status |
| --- | --- | --- |
| ESP32-S3-breakout | centrale microcontroller, leest sensoren, maakt pakketten, stuurt LoRa | gekozen als type, exacte breakout nog te kiezen |
| LoRa-radio met antenne | draadloze verbinding met de adapter | EU-band 868 MHz; exacte module nog te bepalen |
| 9-DoF IMU | oriëntatie en beweging (versnelling, rotatie, magneetveld) | BNO055 is kandidaat, niet vastgelegd |
| Barometer | luchtdruk, gebruikt voor de hoogte | nog te bepalen |
| RTK-GNSS met antenne | nauwkeurige positie | nog te bepalen; ook de correctiebron moet nog gekozen worden |
| Heatsink | koeling van de ESP | nog te bepalen |

De keuze van de IMU bepaalt hoe de oriëntatie tot stand komt. Een module als de BNO055 rekent de sensorfusie zelf uit en levert een kant-en-klare oriëntatie. Een ruwere 9-DoF IMU zonder eigen fusie is goedkoper en sneller, maar dan moet de ESP32-S3 de fusie zelf doen. De barometer wordt samen met de GNSS gebruikt voor de hoogte: de GNSS alleen is daar te onnauwkeurig voor. De RTK-GNSS haalt zijn nauwkeurigheid uit correctiegegevens; die moeten ergens vandaan komen, bijvoorbeeld via de laptop of via een eigen basisstation.

De heatsink houdt de ESP koel, maar mag de barometer niet opwarmen: warme lucht verandert de drukmeting. Daarom komen de barometer en de warmtebron uit elkaar te liggen, met een opening in de behuizing voor de luchtdruk.

> [!question] Nog te bepalen
> Welke IMU (met of zonder ingebouwde fusie), welke barometer en welke RTK-GNSS-module. Voor de RTK-correcties: van een eigen basisstation of via een correctiedienst op de laptop. Voor de LoRa-radio: welke module en welke exacte frequentie en instellingen.

### Voeding en Interface

De module wordt gevoed via een externe batterij, bijvoorbeeld een 7.4V accu, of via een barrel-connector op de PCB. Een spanningsregelaar zorgt ervoor dat de spanning geschikt wordt gemaakt voor de elektronica. De PCB beschikt over extra pinnen en grounds zodat het besturingssysteem van externe toestellen, zoals een mockup-vliegtuigje die kan verbonden worden met de module.

De accu (bijvoorbeeld een 2S LiPo van 7,4 V) of de barrel-connector komt binnen op de ruwe voedingsrail. Van daaruit gaat de spanning door een **buck-converter** naar 5 V en daarna naar 3,3 V voor de logica. Heeft een breakout-module al een eigen regelaar, dan krijgt hij 5 V aangevoerd; is dat niet zo, dan krijgt hij 3,3 V.

De **uitbreidingsconnector** krijgt ten minste deze pinnen:

- de voedingsspanning van de print (5 V en 3,3 V), elk met een eigen ground;
- een ground die gemeenschappelijk is met de rest van het systeem;
- een UART met vrij te kiezen TX- en RX-pinnen voor de verbinding met het besturingssysteem van het toestel.

Die UART is de verbinding waarover de meetmodule stuurwaarden doorgeeft aan de controller van het toestel. Tussen de meetmodule en de voertuigcontroller gebruiken we **kommagescheiden waarden (CSV)**: één leesbare regel per update, met een vaste veldvolgorde, geen checksum en een regeleinde als afsluiting. Dat is makkelijk te lezen in een seriële monitor en met eenvoudige code te ontleden. De exacte veldvolgorde en de schaal van de waarden leggen we later vast.

> [!warning] Let op
> De logische spanning van de meetmodule is 3,3 V. Sommige controllers verwachten 5 V. De niveaus moeten op elkaar afgestemd worden voordat de UART aangesloten wordt.

> [!question] Nog te bepalen
> De definitieve accuspecificatie en de accuduur, de precieze spanningsregelaars, en de beveiliging van de voeding (zekering, beveiliging tegen omgekeerde polariteit). Ook het aantal en de functie van de pinnen op de uitbreidingsconnector.

### Bevestiging en Behuizing

De behuizing is zelf ontworpen en 3D-geprint. De behuizing biedt fysieke bescherming voor de delicate elektronica tijdens tests en gebruik. Het houd ook zo veel mogelijk trillingen tegen om de sensoren min mogelijk in de war te brengen.

De behuizing wordt in **PETG of PLA** geprint en bestaat uit een onderplaat met de montagegaten voor de print en een deksel dat erop klikt of met schroeven vastzit. De print zit op **rubberen dempingsbussen** of op een laagje schuim, zodat trillingen van het toestel niet rechtstreeks op de IMU en de barometer terechtkomen. Dat is belangrijk: een IMU die meetrillt met de behuizing levert een onrustig signaal.

De antennes krijgen vrij zicht en mogen niet door de behuizing afgeschermd worden. Voor de GNSS-antenne komt er een vlakke plek met een ground plane onder de antenne, met de opening naar boven. De behuizing krijgt ook een opening voor de luchtdruk van de barometer en voor de connectors (voeding en uitbreidingsconnector).

> [!question] Nog te bepalen
> Het definitieve ontwerp, de afmetingen en het printmateriaal, en de manier waarop de demping wordt uitgevoerd. Ook de bevestiging van de behuizing aan het toestel zelf moet nog vastgelegd worden.

### LoRa Adapter

Er is een tweede ESP met LoRa aangekoppeld aan de laptop. Dit dient als een communicatie-adapter. De verbinding met de laptop gebeurt via een USB-kabel. Deze adapter maakt het mogelijk om data van de module te ontvangen en commando's terug te sturen.

De adapter is een **doorgeefluik** en rekent zelf niets uit. Zijn firmware doet twee dingen:

- wat hij via LoRa ontvangt, zet hij om naar een regel tekst en stuurt hij over USB naar de laptop;
- wat de laptop over USB stuurt, zet hij om naar een LoRa-pakket en zendt hij terug naar de meetmodule.

Op de print van de adapter zit de ESP met de LoRa-radio en een **USB-naar-serieel-omzetter** (of de native USB van de ESP, als die gebruikt wordt). De adapter krijgt zijn voeding via de USB-kabel van de laptop en heeft een eigen antenne. Omdat de adapter los van de meetmodule staat, kunnen de twee antennes vrij op elkaar gericht worden, wat het bereik ten goede komt.

> [!info] Waarom een aparte adapter?
> De laptop kan geen LoRa ontvangen. De adapter maakt van de draadloze verbinding een gewone seriële verbinding, zodat de laptopapplicatie met één kabel klaar is.

## Software Specificaties

### Data Verwerking

De IC's op de meetmodule lezen continu de waarden uit van de IMU, barometer en RTK-GNSS. Deze gegevens worden verzameld en samengevoegd tot datapakketten in de ESP. Om de data nauwkeuriger te maken wordt er gebruik gemaakt van sensorfusie met een algoritme zoals een Kalman filter.

De sensoren worden niet allemaal even snel uitgelezen. De IMU levert de meeste metingen per seconde, de barometer minder en de GNSS-module nog minder, omdat die afhankelijk is van de satellieten. De firmware leest elke sensor op zijn eigen tempo uit en voegt de laatste waarden samen tot één datapakket. Elk pakket krijgt een **tijdstempel**, zodat de laptop de metingen later kan ordenen en opnieuw kan afspelen.

Een datapakket bevat minstens:

- het tijdstip van de meting;
- de positie: breedtegraad en lengtegraad;
- de hoogte, uit de barometer en de GNSS samen;
- de snelheid: totaal, horizontaal en verticaal;
- de richting (kompas) en de verticale hoek, en bij een volledige IMU ook de rol- en gierhoek;
- statusgegevens: het aantal satellieten, het type positiebepaling en of elke sensor nog werkt.

De **sensorfusie** gebeurt in de ESP32-S3. Met een Kalman-filter worden de ruwe metingen van de IMU gladgestreken tot een stabiele oriëntatie, en worden de hoogtemetingen van de barometer en de GNSS gecombineerd: de GNSS houdt de hoogte op lange termijn juist, de barometer vangt de snelle veranderingen op. Bij de barometer wordt ook de temperatuur meegerekend.

> [!question] Nog te bepalen
> Het exacte pakketformaat: binair (compact, minder datavolume over LoRa) of tekst in JSON (leesbaar en makkelijk te maken). En de uitleesfrequenties per sensor, de precieze inhoud van het pakket, en de variant en de bibliotheek van het Kalman-filter.

### Communicatie en Beveiliging

De datapakketten worden verzonden via de LoRa-verbinding. De adapter aan de laptop stuurt deze metingen door via USB.

Van de meetmodule naar de laptop loopt de keten als volgt: de sensoren gaan naar de ESP32-S3, die er pakketten van maakt; de LoRa-radio zendt ze naar de adapter; de adapter zet ze om naar tekstregels over USB; de laptopapplicatie leest die regels in en toont ze.

In de andere richting loopt de keten omgekeerd: de applicatie of een eigen programma bepaalt de stuurwaarden, stuurt ze als regel naar de adapter, de adapter zendt ze via LoRa naar de meetmodule, en de meetmodule geeft ze via de UART door aan het besturingssysteem van het toestel.

### De laptopapplicatie

De applicatie is één programma dat de hele keten bedient. Bij het opstarten komt er eerst een **startscherm** dat vraagt om de LoRa-adapter in te steken. Daarna controleert de applicatie twee dingen apart: of de USB-verbinding met de adapter werkt, en of er geldige datapakketten van de meetmodule binnenkomen. Beide statussen worden afzonderlijk getoond, zodat meteen duidelijk is waar het misloopt als er geen data is.

Na een geslaagde verbinding komt het **hoofdscherm**. Dat toont langs de ene kant de actuele meetwaarden (coördinaten, hoogte, snelheid en oriëntatie) en langs de andere kant een kaart met de positie van de meetmodule, een richtingspijl en de afgelegde route. De meetgegevens en de route worden bewaard, zodat een vlucht of rit later opnieuw bekeken kan worden.

De applicatie heeft drie werkmodi:

- **Kaart:** de kaart met de route en de actuele meetwaarden.
- **Code:** de gebruiker schrijft zelf korte code die de meetwaarden omzet in stuurwaarden. De pagina toont het codevenster met een uploadknop en houdt de uitleg kort: welke meetwaarden je kan gebruiken, en hoe je een regel met stuurwaarden verstuurt. Er zijn geen vaste uitgangsvelden; de gebruiker schrijft de regel zelf.
- **API:** hier schakelt de gebruiker de API aan of uit, test hij de verbinding, en staat de documentatie van de koppeling.

Via die **API** kan een eigen programma buiten de applicatie meedoen. De applicatie stuurt de meetgegevens live als JSON door naar dat programma, en dat programma stuurt zijn stuurwaarden terug. De applicatie geeft die dan verder door aan de meetmodule. Zo kan de gebruiker complexere berekeningen maken zonder de applicatie zelf te wijzigen.

> [!question] Nog te bepalen
> De techniek van de API tussen de applicatie en een eigen programma: een lokale WebSocket, een TCP-verbinding, HTTP of een benoemde pijplijn. In de demo werkt het met een WebSocket op de lokale computer, met de meetgegevens als JSON naar buiten en een vrije kommagescheiden regel terug.

### Besturing en veiligheid

Ongeacht waar de stuurwaarden vandaan komen, moet de meetmodule zichzelf in veiligheid brengen als er iets misgaat. De veiligheidsstop zit daarom in de firmware van de meetmodule en niet alleen in de laptopapplicatie, zodat het toestel ook veilig is als de verbinding wegvalt.

| Situatie | Gedrag |
| --- | --- |
| Geen geldig commando binnen de ingestelde tijd | motoren naar nul, servo's naar neutraal |
| Ongeldige of onvolledige regel | negeren en tellen; bij te veel fouten naar de veilige toestand |
| Verbinding met de laptop verbroken | de meetmodule gaat zelf naar de veilige toestand |
| Toestel buiten de ingestelde grenzen | de besturing gaat naar de veilige toestand |

De **grenzen** worden in de software ingesteld. De applicatie waarschuwt zodra het toestel buiten het toegelaten gebied komt en kan de besturing laten stoppen. De sensorfusie helpt daarbij: als de GNSS-verbinding even wegvalt, blijft de positie met de andere sensoren bij benadering bekend, en de applicatie meldt dat de positie minder betrouwbaar is.

> [!question] Nog te bepalen
> Hoeveel seconden zonder geldig commando mogen verlopen voordat de veiligheidsstop ingrijpt, wat de veilige toestand precies is voor het gebruikte toestel, en hoe de grenzen worden ingesteld en bewaard.

### Versiebeheer

Alle software voor de meetmodule, de adapter en de laptopapplicatie wordt in één **git-project** bewaard. Zo kan altijd teruggekeerd worden naar een oudere werkende versie als een wijziging problemen geeft. Elke versie die op een van de ESP's gezet wordt, krijgt een nummer dat in het project terug te vinden is.

### Testen

Het systeem wordt in stappen getest:

- **Sensoren apart:** elke sensor afzonderlijk uitlezen en vergelijken met bekende waarden.
- **Kalibratie:** de IMU en de barometer kalibreren en de GNSS een goede positiebepaling laten vinden.
- **Communicatie:** het bereik en de betrouwbaarheid van de LoRa-verbinding meten, en nagaan wat er gebeurt bij pakketverlies.
- **Veiligheid:** de verbinding bewust verbreken en controleren of de veiligheidsstop op het juiste moment ingrijpt.
- **Veldtest:** een volledige testvlucht of testrit met een route, en de bewaarde gegevens daarna opnieuw bekijken in de applicatie.

> [!question] Nog te bepalen
> Welke testen eerst gebeuren, welke meetwaarden als goed of fout gelden, en met welk toestel we de besturing testen. Het aansturen van een voertuig is een demonstratie aan het einde van het project; het belangrijkste doel is de meetmodule zelf met de adapter en de applicatie.

## Overzicht van de nog te bepalen punten

| Onderwerp | Wat nog vastgelegd moet worden |
| --- | --- |
| Print | afmetingen, laagopbouw, layout |
| LoRa | module, frequentie en band, instellingen, antenne |
| IMU | welke 9-DoF IMU, met of zonder ingebouwde fusie |
| Barometer | welk type |
| RTK-GNSS | welke module en waar de correctiegegevens vandaan komen |
| Voeding | accuspecificatie, regelaars, beveiliging, accuduur |
| Uitbreidingsconnector | aantal pinnen, functie per pin, spanningsniveau |
| Behuizing | ontwerp, materiaal, demping, bevestiging aan het toestel |
| Pakketformaat | binair of JSON, exacte velden, uitleesfrequenties |
| Sensorfusie | variant en bibliotheek van het Kalman-filter |
| API | techniek tussen de applicatie en een eigen programma |
| Besturing | veldvolgorde en schaal van de stuurwaarden, aantal servo's |
| Veiligheid | omschakeltijd naar de veilige toestand, definitie van de veilige toestand, geofencing-grenzen |
| Testen | testplan, toestel voor de demonstratie |
