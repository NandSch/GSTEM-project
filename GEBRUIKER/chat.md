---
tags: [gstem, chatlog]
sessie: "01a11055-3adb-75ac-bebb-aceae8363733"
gestart: 2026-10-06T08:29:46.001Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11055-3adb-75ac-bebb-aceae8363733` · gestart 2026-10-06_1029
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 10:30

> [!quote] Verbatim
> Ga 1 per 1 af welke componenten ik nog moeten zoeken.

## AI · 10:31

Ik heb de bestaande stukken (`componenten.md`, `open-vragen.md`, `actieplan.md`, `pcb-methodes-kosten.md`, `pcb-ontwerp.md`) naast elkaar gelegd. Hieronder staat de volledige zoeklijst in een werkbare volgorde, en daarna begin ik met nummer 1.

---

## AI · 10:31

> [!info] Opgeslagen: zoekvolgorde → [[componenten]] (`Te zoeken: werkorder 1 per 1`)

## Wat je nog moet zoeken (volledige lijst)

**A. Bordkritisch — eerst, want dit bepaalt de PCB-footprints**
1. Barometer — BMP581 of BME280
2. RTK-GNSS-module — u-blox ZED-F9P / ArduSimple / SparkFun RTK
3. Bron RTK-correctie — eigen basisstation of NTRIP-dienst
4. Sockettype — precisie/gefreesd, dual-wipe of direct solderen
5. Uitbreidingsconnector — exacte stekker voor UART (TX/RX)
6. I2C-pull-ups en level shifter (3,3 V vs 5 V)
7. Wat komt op de print (LED + sockets) vs losse modules (buck, LDO, zekering, TVS)

**B. Voeding en RF**
8. 7,4 V-accu + beschermcircuit + connector
9. Zekering, ompoolbeveiliging, TVS
10. Buck 5 V
11. LDO 3,3 V
12. Aan/uit-schakelaar
13. GNSS-antenne (actief + LNA + ground plane)
14. LoRa IPEX → SMA-pigtail + SMA-bulkhead
15. Controleren of LoRa-antenne bij de kit zit

**C. Verbindingen en montage**
16. USB-C datakabel
17. UART-draden + ground + level shifter
18. Dupont-/siliconendraad
19. M3-schroeven, moeren, standoffs, spacers

**D. Laptop-/ontvangerzijde**
20. LoRa-ontvanger (tweede XIAO-kit of USB-dongle)
21. USB-kabel ontvanger

**E. Mock-up (vliegtuigje)**
22. Arduino (Uno/Nano)
23. Drie servo's + type
24. Servo-voeding/BEC
25. Stuurstangen, scharnieren, roerbladen, rompmateriaal

**F. Gereedschap en verbruik**
26. Digitale schuifmaat · 27. soldeerbout/tin/flux · 28. multimeter · 29. USB-serieel adapter

---

## Nummer 1 — Barometer

| Optie | Meet | Voordeel | Nadeel |
| --- | --- | --- | --- |
| **Adafruit BMP581** | druk + temperatuur | veel lagere ruis, fijnere hoogteresolutie; al prijs gecheckt ($9,95); klein | geen luchtvochtigheid |
| Adafruit BME280 | druk + temperatuur + vochtigheid | zeer goed ondersteund | ouder, meer ruis, vocht heb je niet nodig |

> [!tip] Advies
> **BMP581.** Voor een positie-/hoogtetoestel telt resolutie en stabiliteit, niet luchtvochtigheid. De BMP581 is nauwkeuriger en zuiniger; de BME280 voegt enkel vochtigheid toe die je niet gebruikt.

Beslissing? Zeg **"BMP581"** (of een alternatief), dan noteer ik dat in [[componenten]] en [[beslissingen]] en gaan we verder met **nummer 2 — RTK-GNSS-module**.

---

## Gebruiker · 10:43

> [!quote] Verbatim
> A
> 1 Het meest accurate dat je vind
> 2 LC29H(DA)?
> 3 Ntrip dienst
> 4 Dual wipe voor ESP en precisie voor de rest.
> 5 Nog niks, hou in opslag dat dit nog niet is gedaan of gevonden
> 6 Ken ik niks van hou in opslag
> 7 Led plus sockets, Voor de rest weet ik niet. Zoek zelf wat essentieel is. Buck converter doe ik.
> B
> 8 7,4V batterij, Buck converter, Beschermcircuit nog niks, barrelconnector
> 9 Ken ik niks van, hou in opslag
> 10 heb ik al
> 11 Ken ik niks van hou in opslag
> 12 Apparaat springt aan wanneer verbonden aan voeding
> 13 Zoek het best passende, De ESP32-S3 die ik had gevonden zat een antenne passend bij
> 14 Ken ik niks van hou in opslag
> 15 Zit erbij
> C
> 16 geen datakabel nodig?
> 17 UART draden met zo'n connectoren waar je een draad in vast schroeft. Ground weet ik niet. Ik weet niet wat een level shifter is.
> 18 ik weet niet wat dit is, slaag op in opslag
> 19 sowiso nodig zoek die wanneer we de bestellijst maken
> D
> 20 tweede XIAO-kit
> 21 Usb A kabel
> E
> 22 arduino uno
> 23 meer dan drie servos, type doet er niet aan toe, ik heb zelf servos thuis liggen en zal die gebruiken, zet deze wel nog op de bestellijst wanneer we die maken.
> 24 Servovoeding = aparte buck converter, die heb ik zelf ook.
> 25 Maak ik zelf wel met 3D printen
> F
> 26 ik heb alles.

## AI · 10:43

Ik verwerk je antwoorden en doe meteen het zoekwerk dat je vraagt (1, 2, 13 en 7).

---

## AI · 10:44

Zoekwerk klaar. Ik verwerk nu alles in het archief.

---

## AI · 10:45

> [!info] Opgeslagen
> - [[componenten]] — bijgewerkt: gekozen/nog te kiezen/nog te noteren + werkorder + "essentieel op de print"
> - [[beslissingen]] — 7 nieuwe beslissingen (`2026-10-06`)
> - [[open-vragen]] — barometer, RTK en correctiebron afgesloten; nieuwe open punten toegevoegd
> - [[afgevoerd]] — BME280/BMP581 en eigen basisstation
> - [[specificaties]], [[actieplan]], [[links]] — bijgewerkt

## Wat deze ronde beslist is

| # | Functie | Keuze |
| --- | --- | --- |
| 1 | Barometer | **Adafruit BMP390** — meest accurate van de makkelijk verkrijgbare breakouts (±3 Pa ≈ 0,25 m, ruis 0,02 Pa). De BMP581 en BME280 vallen af. |
| 2 | RTK-GNSS | **Quectel LC29H(DA)** — dual-band L1+L5, RTK rover, centimeter-niveau. |
| 3 | Correcties | **NTRIP-dienst** via de laptop (geen eigen basisstation). |
| 4 | Sockets | **Dual-wipe** voor de XIAO, **precisie/gefreesd** voor de rest. |
| 7 | Op de print | LED + sockets + per module ontkoppeling (100 nF + 10 uF), bulk-elco 100 uF op 5 V, barrel + schroefklemmen, 4x M3-gaten. |
| 8 | Voeding | 7,4 V-accu + **barrel-connector** + buck 5 V (heb je). |
| 12 | Aan/uit | **Geen schakelaar** — toestel start bij voeding. |
| 15 | LoRa-antenne | **Zit bij de kit**. |
| 20 | Ontvanger | **Tweede XIAO-kit** + USB A-kabel. |
| 22-25 | Mock-up | **Arduino Uno**, eigen servo's (> 3), eigen servo-buck, eigen 3D-print. |
| 26-29 | Gereedschap | Alles aanwezig. |

## Uitleg bij je vragen

> [!question] 16 — Geen datakabel nodig?
> Voor het **flashen/programmeren** van de XIAO heb je toch een **USB-C datakabel** nodig (geen laadkabel). Die blijft dus op de lijst, maar wordt niet permanent aangesloten.

> [!question] 17 — Ground en level shifter
> - **Ground:** toestel en Arduino moeten een **gemeenschappelijke GND** delen, anders heeft het UART-signaal geen referentie. Er komt dus een grounddraad naast TX/RX.
> - **Level shifter:** een klein bordje dat **3,3 V <-> 5 V** omzet. De XIAO is 3,3 V, de Arduino Uno 5 V; zonder omzetting kan je de XIAO-ingang beschadigen of onbetrouwbaar lezen. Ik zoek het juiste type uit (AI-taak).

> [!question] 18 — Dupont/siliconendraad
> Soepele jumperdraadjes voor de bedrading binnenin. Nog open; nemen we mee bij de bestellijst.

## Wat nog open blijft om te zoeken of te beslissen

- [ ] **5. Uitbreidingsconnector** — exacte stekker (je stelt schroefklemmen voor de draden voor).
- [ ] **6. I2C-pull-ups en level shifter** — pull-ups zitten al op de BNO055- en BMP390-breakouts; level shifter: AI-taak.
- [ ] **9. Zekering / ompoolbeveiliging / TVS** — je kent dit niet; ik zoek het uit.
- [ ] **11. LDO 3,3 V** — waarschijnlijk overbodig: de XIAO levert zelf 3,3 V.
- [ ] **13. GNSS-antenne** — advies: dual-band L1+L5 actieve antenne (zoals die van de Waveshare LC29H-HAT).
- [ ] **14. LoRa IPEX -> SMA-pigtail** — enkel als de antenne door de behuizing moet.
- [ ] **NTRIP-provider** — gratis of betaald.
- [ ] **M3-schroeven/standoffs en servo's** — toevoegen bij het opmaken van de bestellijst.

## AI-taken die ik op mij neem

- [ ] Pinout-tabel XIAO + pin-budget (IMU + barometer + GNSS + UART).
- [ ] Level shifter 3,3 V <-> 5 V uitzoeken voor de Arduino Uno.
- [ ] Bescherming van de voeding (zekering/ompoolbeveiliging/TVS) voorstellen.
- [ ] Antenne-advies L1+L5 concreet maken.

Wil je dat ik meteen een van deze AI-taken uitvoer, of eerst de volgende componentenrondes (5, 6, 9, 11, 14) samen doorlopen?

---

## Gebruiker · 10:50

> [!quote] Verbatim
> 16. Ik heb zelf een kabel voor flashen en programeren 17. Oké goed ook met schroefconnector. Oké moet er ook bijzitten dan 18. Heb ik zelf.

## AI · 10:50

> [!info] Opgeslagen: [[componenten]], [[beslissingen]], [[open-vragen]] bijgewerkt

**Verwerkt:**
- **16. USB-C datakabel** — in bezit, gaat **niet** op de bestellijst.
- **18. Dupont-/siliconendraad** — in bezit, gaat **niet** op de bestellijst.
- **17. UART-koppeling** — bevestigd: **schroefklemmen** + **gemeenschappelijke ground** + **level shifter (3,3 V <-> 5 V)**. Ground en level shifter horen er dus bij.

**Wat hieruit nog te zoeken blijft:** het **exacte type level shifter** (AI-taak) en nog een **grounddraad** in de bestellijst — de rest van de UART-draden heb je zelf.

**Open om samen af te handelen (5, 6, 9, 11, 14):**
- [ ] 5. Uitbreidingsconnector — exacte schroefklem/stekker
- [ ] 6. I2C-pull-ups (zitten al op BNO055 + BMP390) en de level shifter
- [ ] 9. Zekering / ompoolbeveiliging / TVS
- [ ] 11. LDO 3,3 V (waarschijnlijk overbodig door de XIAO)
- [ ] 14. LoRa IPEX -> SMA-pigtail (enkel bij montage door de behuizing)

Zeg maar of ik deze vijf verder uitzoek, of dat ik eerst de AI-taken (pinout, level shifter, voedingsbescherming) afwerk.

---

## Gebruiker · 10:54

> [!quote] Verbatim
> 5. Kies zelf iets passend dat goed werkt. 6. Kies jij, deze moet op het pcb bordje komen neem ik aan 9. Hetgene dat nodig is volgens jou 11. Is goed. Is ook nodig voor aan de Lora ontvanger USB! 14. Wat is dit?

## AI · 10:54

Ik zoek de juiste onderdelen uit en leg uit wat de pigtail is.

---

## AI · 10:55

> [!info] Opgeslagen: [[componenten]], [[beslissingen]], [[open-vragen]], [[specificaties]], [[links]], [[actieplan]]

## Jouw punten verwerkt

**5. Uitbreidingsconnector — gekozen**
- **4-pins schroefklem, 3,5 mm raster** (KF128/KF301), pinout **GND / +5 V / TX / RX**. Robuust en past bij de schroefconnectoren die je al wilde.

**6. Level shifter en pull-ups — gekozen**
- **Level shifter: TXB0104** (4-kanaals bidirectioneel). Ja, die komt **op de print**: hij zet de 3,3 V van de XIAO om naar 5 V voor de Arduino Uno (en terug).
- **I2C-pull-ups: niet op de print.** De BNO055- en BMP390-breakouts hebben ze al; extra pull-ups zouden de I2C-bus te zwaar belasten. Ik voorzie wel 2 reserve-footprints voor later.

**9. Voedingsbescherming — gekozen (wat nodig is)**
- **2 A PTC-zekering** + **P-MOSFET ompoolbeveiliging (DMG2301L)** + **TVS-diode SMBJ10A** + **bulk-elco 100 uF/16 V**. Samen de standaard minimale bescherming voor een 7,4 V-accu.

**11. LDO 3,3 V — behouden**
- **AP2112K-3.3** geeft een eigen schone 3,3 V-rail voor de sensoren.
- Let op voor de **LoRa-ontvanger**: de tweede XIAO-kit hangt via **USB** aan de laptop en heeft **zelf al een 3,3 V-regelaar**. Daar is dus **geen losse LDO** nodig — die 3,3 V zit al in de XIAO.

**14. Wat is een IPEX -> SMA-pigtail?**
> [!question] Uitleg
> Op de XIAO zit een piepklein **IPEX/U.FL**-antennecontact. Een **pigtail** is een kort kabeltje van dat kleine contact naar een groter **SMA**-contact dat je door de behuizing monteert, zodat je de antenne **buiten** kunt schroeven.
> - De **kitantenne zit erbij** en past **rechtstreeks** op de IPEX.
> - **Je hebt de pigtail dus niet nodig** als de antenne **in de behuizing** blijft (PLA/PETG laat het LoRa-signaal goed door).
> - Enkel nodig als je de antenne **extern** wilt monteren. Ik heb dit als open punt laten staan, maar het is standaard **niet nodig**.

## Nog open (klein)

- [ ] **13. GNSS-antenne** — advies: actieve dual-band L1+L5 (zoals bij de Waveshare LC29H-HAT). Bevestig of we die meebestellen.
- [ ] **NTRIP-provider** — gratis of betaald.
- [ ] **Socket exact model** — precisie- en dual-wipe-merk kiezen.
- [ ] **LoRa IPEX-pigtail** — enkel als je de antenne buiten wilt.
- [ ] **M3-schroeven/standoffs + servo's** — bij het opmaken van de bestellijst.
- [ ] **AI-taak:** pinout-tabel XIAO + pin-budget controleren.

Wil je dat ik nu de **pinout-tabel** en het **pin-budget** van de XIAO uitwerk?

---

## Gebruiker · 11:00

> [!quote] Verbatim
> Zeker een SMA pigtail nodig zodat ik de antenna buiten het vliegtuigje kan connecteren. 13 Zoals jij passend ziet. Gratis NTRIP, zoek ik wel. Welk merk precisie en dualwipe zien we nog wel. Moet niet percé op de bestellijst. Wacht met AI taak.

## AI · 11:00

> [!info] Opgeslagen: [[componenten]], [[beslissingen]], [[open-vragen]], [[specificaties]], [[links]]

**Verwerkt:**
- **14. LoRa-antenne extern** — gekozen: **IPEX/U.FL -> SMA female bulkhead pigtail**, zodat je de antenne buiten het vliegtuigje kunt schroeven. De kitantenne blijft behouden.
- **13. GNSS-antenne** — gekozen: **actieve dual-band L1/L5-antenne met SMA, LNA + ground plane** (compacte uitvoering, voorbeeld de Waveshare-antenne), passend bij de LC29H(DA).
- **NTRIP** — wordt een **gratis** dienst; **jij zoekt de provider**. Als gebruikersactie genoteerd.
- **Socket-merken** — later bepalen, **niet per se op de bestellijst**.
- **AI-taak (pinout/budget)** — laat ik wachten zoals gevraagd.

**Kleine aandachtspunten die hieruit volgen:**
- De **3D-geprinte behuizing** krijgt een **SMA-bulkhead-doorvoer** voor de LoRa-antenne.
- De GNSS-antenne heeft een **SMA-aansluiting**; de LC29H-module moet die ook bieden (HAT/module met SMA, of anders een tweede IPEX-pigtail). Dit verifiëren we bij de modulekeuze.

**Nog open:**
- [ ] Gratis NTRIP-provider (jij)
- [ ] Socket-merken (later)
- [ ] Pinout-tabel + pin-budget (AI-taak, wacht op jouw teken)
- [ ] Bestellijst opmaken: GNSS-antenne, LoRa-pigtail, M3/standoffs, servo's

Zeg maar wanneer ik de pinout-taak of de bestellijst mag oppakken.

---
