# G-Stem / GSN — projectcontext voor volgende chats

## Doel en status

Dit is een schoolproject rond een compacte, draadloze module die 3D-positie en beweging meet. De werktitel **AeroLink** is genoemd, maar de definitieve productnaam ligt niet vast. De hardware, firmware en laptopapp zijn in ontwerp. Het bestand `G-Stem_specificaties_concept.docx` is een aanvullende conceptbron; details daarin zijn nog geen definitieve technische specificatie.

De map [`visual-prototype`](visual-prototype/) bevat een **visuele mock-up** van de geplande laptopapp. Die toont de beoogde indeling en gegevensstroom met fictieve waarden. De demo maakt geen echte USB- of LoRa-verbinding, leest geen sensoren uit, voert geen gebruikerscode uit en bestuurt geen voertuig.

## Beoogde meetmodule

- Een eigen PCB verbindt insteekbare breakoutboards via pinheaders of connectoren. PCB-sporen verzorgen data en voeding; de exacte borden en pinbezetting moeten nog gekozen worden.
- Een ESP32-S3 met LoRa-radio en antenne is voorzien als centrale controller. Firmware leest de sensoren, bundelt de metingen in pakketten en zendt die draadloos uit.
- Een 9-DoF IMU met absolute-orientation sensorfusie is voorzien. **BNO055 is een mogelijke kandidaat, geen vastgelegde keuze.** Gewenste gegevens zijn quaternion en/of Euler-hoeken, hoeksnelheid, versnelling, magnetisch veld, lineaire versnelling, zwaartekracht en sensortemperatuur.
- Een barometer levert luchtdruk en een hoogte-inschatting. Een RTK-GNSS-module met antenne levert geografische positie.
- Een batterij, USB-C-aansluiting en passende beveiliging en spanningsregeling zijn voorzien. De precieze laad-, programmeer- en voedingsschakeling moet nog worden uitgewerkt.
- Een zelf ontworpen 3D-geprinte behuizing met demping is voorzien. Het project vergelijkt meetgedrag met en zonder schokken of trillingen.
- De PCB krijgt een uitbreidingsconnector met signaalpinnen en massa voor kabels naar een bestaande voertuigcontroller. Signaaltype, elektrische interface, spanningsniveaus en veiligheidsgrenzen zijn nog te bepalen.

## Draadloze en softwareketen

```text
IMU + barometer + RTK-GNSS
          ↓
ESP32-S3 op de meetmodule → LoRa → tweede ESP met LoRa → USB → laptopapp
          ↑                                                    ↓
bestaande voertuigcontroller ← kabel/connector ← meetmodule ← LoRa ← USB-adapter ← berekend commando
```

Het tweede ESP-bord met LoRa dient bij de laptop als ontvanger én zender en is via USB aangesloten. De laptopsoftware is bedoeld als één installeerbare app, met benodigde bibliotheken en onderdelen inbegrepen.

### Beoogde appflow

1. Het startscherm vraagt om de USB-adapter aan te sluiten en controleert die verbinding.
2. Vervolgens controleert de app apart of geldige meetpakketten via LoRa aankomen.
3. Na een geslaagde verbinding opent het hoofdscherm met twee modi: **Livekaart** en **Programmering & besturing**.

**Livekaart:** links een interactieve, Google-Earth-achtige 3D-kaart met actuele positie, richting en snelheid en een rode lijn voor de afgelegde route. Rechts ruwe actuele waarden, waaronder coördinaten, hoogte, snelheid, oriëntatie en verbindingsstatus. Het conceptdocument noemt ook het bewaren van metingen en route voor latere analyse.

**Programmering & besturing:** meetdata gaat naar eigen code of via een gedocumenteerde lokale interface naar een extern proces. Dat kan acties berekenen voor een RC-auto of een stilstaande vliegtuigmock-up. Berekende commando's keren via USB-adapter en LoRa naar de meetmodule terug en gaan via de uitbreidingsconnector naar de bestaande voertuigcontroller. Een veilige stop bij verbindingsverlies of ongeldige commando's is een vereiste voor een werkende uitvoering; de concrete aanpak moet nog worden ontworpen.

Als optionele demonstratie is eerder een stilstaande vliegtuigmock-up met een tweede microcontroller en twee servo's genoemd. Een vliegend toestel is geen vereiste.

## Huidige visuele demo

- [`visual-prototype/index.html`](visual-prototype/index.html) is een lokaal te openen, responsieve HTML-demo zonder externe afhankelijkheden.
- Het startscherm **simuleert** de USB- en LoRa-controles. Beide statussen zijn voorbeeldstatussen.
- De Livekaart gebruikt een getekende terreinvisualisatie rond Spa, België, een voorbeeldroute, positiepijl en fictieve telemetrie. Het is geen echte kaartdienst.
- De tab **Programmering & besturing** toont alleen een grote, overzichtelijke editor met illustratieve voorbeeldcode voor een RC-auto. Er is geen code-uitvoering of voertuigbesturing.
- De interface buiten de kaart gebruikt een witte en grijze vormgeving; de terreinvisualisatie is het enige gekleurde vlak.
- Tabs en de knop om de demo te openen dienen alleen om de schermen van de mock-up te bekijken. Kaartknoppen zijn presentatief.

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

## Bronnen binnen dit project

- `G-Stem_specificaties_concept.docx` — conceptpunten voor hardware en software; geraadpleegd voor dit contextbestand.
- `GSN-project_draadloze_3D-meetmodule.docx` — aanvullend projectdocument.
- `Blokschema_AeroLink.drawio` — blokschema; de naam AeroLink blijft voorlopig.

Gebruik dit bestand als oriëntatie voor vervolgwerk en controleer nieuwe technische keuzes steeds tegen de actuele projectdocumenten en beslissingen van de gebruiker.
