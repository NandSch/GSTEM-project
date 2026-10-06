---
tags: [gstem, chatlog]
sessie: "01a11038-43c9-7350-ad92-6d8720ca78ed"
gestart: 2026-10-06T07:58:05.499Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11038-43c9-7350-ad92-6d8720ca78ed` · gestart 2026-10-06_0958
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 09:58

> [!quote] Verbatim
> Hoe ga ik de pcb ontwerpen? Met welke app en hoe moet ik alle afmetingen van de gaten voor de componenten vinden et cetera?

## AI · 09:58

Ik lees eerst de skill en de bestaande archiefdata.

---

## AI · 09:59

Ik heb genoeg context. Hieronder het antwoord, daarna leg ik het vast in het archief.

## Kort antwoord

**App:** gebruik **KiCad 8/9** (gratis, open source, Windows). Wil je zo weinig mogelijk gedoe en bestel je toch bij JLCPCB, dan is **EasyEDA** een prima alternatief omdat onderdelen en bestelling aan elkaar hangen. Vermijd Altium/Fusion 360 Electronics voor dit project (duur, overkill).

**Afmetingen van gaten:** je meet of zoekt ze **per module** op, je verzint ze nooit zelf. Drie bronnen, in deze volgorde:

1. **Datasheet / mechanische tekening van de breakout** (Adafruit, SparkFun, Waveshare, DFRobot zetten daar "board dimensions", pin pitch en mounting-hole diameter in).
2. **Standaardmaten** die altijd gelden: 2,54 mm pitch voor pinheaders, gat 1,0 mm, pad 1,7–1,8 mm; M3-bevestigingsgat = 3,2 mm vrij gat; M2,5 = 2,7 mm.
3. **Zelf nameten met een digitale schuifmaat** (€15–25) op de module die je echt in huis hebt — dan klopt het altijd.

En de gouden truc: **print je layout 1:1 op papier en leg de echte modules erop**. Klopt het, dan is je footprint goed.

---

## Uitgebreider: de werkwijze

### 1. KiCad opzetten
- Symbolen (schema) → Footprints (landpatronen) → PCB-layout → DRC → Gerbers → bestellen.
- Voor dit bord heb je nauwelijks een echt schema nodig: elke module wordt een **connector** (rij pinnen), dus je gebruikt vooral `Connector_PinSocket_2.54mm`-footprints en wat losse onderdelen (buck, LDO, LED, weerstanden, zekering).

### 2. Footprints voor de modules
- ESP32-S3-devkit, LoRa-breakout, IMU, barometer, GNSS: allemaal **2,54 mm-raster**.
- In KiCad kies je bv. `PinSocket_1x08_P2.54mm_Vertical` of `1x22`. Je hoeft alleen te weten **hoeveel pinnen per rij** en **hoe ver de twee rijen uit elkaar staan** (meestal 2,54 mm of 15,24/22,86 mm bij grotere devkits — dat staat in de datasheet of meet je).
- Voeg per module een **silkscreen-omtrek** toe, zodat je op de print ziet waar de module zit en hoe ze georiënteerd moet worden.

### 3. Gaten: welke maten
| Doel | Gat | Notitie |
| --- | --- | --- |
| Pinheader 2,54 mm | 1,0 mm | pad 1,7–1,8 mm |
| Pinheader 2,0 mm (JST-GH) | 0,8 mm | |
| M3-bevestiging (vrij) | 3,2 mm | schroef door bord |
| M3 + inslagmoer (heat-set) | 4,0–4,5 mm | voor 3D-print/behuizing |
| M2,5 | 2,7 mm | |
| M2 | 2,2 mm | |

Gebruik in KiCad de `MountingHole`-footprints; die hebben de juiste maat al.

### 4. Bestellen
- JLCPCB of PCBWay: 2-laags, 5 stuks, ± €2–5 + verzending. Minimale order is 5, dus geen probleem.
- Exporteer **Gerbers + drill files** (`File → Fabrication Outputs`), zip en upload. Laat de fabriek de default-regels (min. spoor 0,2 mm, min. gat 0,3 mm) controleren met hun eigen DRC.

### 5. Waar het bij dit bord op aankomt
- **Ground plane** op de onderlaag, aparte rails VBAT/5V/3V3.
- **Antenne-keep-out** voor LoRa en GNSS (geen koper onder de antenne).
- Buck-spoel en ESP weg van IMU/barometer.
- I2C kort houden.
- Denk aan de **socket-keuze** (precisie vs. dual-wipe) — die bepaalt de landpatronen.

> [!info] Opgeslagen: nieuw topic `data/pcb-ontwerp.md`, aangevuld in `onderwerpen.md`, `links.md`, `specificaties.md` en `open-vragen.md`.

Nu leg ik het vast.

---

## AI · 09:59

Klaar. Opgeslagen in het G-Stem-archief:

- **Nieuw topic** `GEBRUIKER/data/pcb-ontwerp.md` — volledige werkwijze (app, KiCad-stappen, gatmaten-tabel, controle via 1:1-print).
- **`onderwerpen.md`** — link `[[pcb-ontwerp]]` toegevoegd.
- **`data/links.md`** — KiCad en JLCPCB als bronnen.
- **`data/specificaties.md`** — entry `2026-10-06 — PCB-ontwerp: gereedschap en gatmaten`.
- **`data/open-vragen.md`** — de vraag over ontwerpgereedschap heeft nu een advies (KiCad + JLCPCB/PCBWay), nog te bevestigen.

Wil je dat ik in `documenten/` een startende KiCad-notitie of een invultabel per module (pinrijen, rijafstand, bordafmeting, gatpositie) aanmaak zodra je de exacte breakouts kiest?

---

## Gebruiker · 10:02

> [!quote] Verbatim
> Ik al sowiso alle componenten zelf aankopen buiten het pcb bordje zelf. (waarop led en sockets geplaatst zijn)

## AI · 10:03

Duidelijk. Dat verandert de rol van de print: het bordje is dan in principe een **drager** — jij koopt alle modules en losse onderdelen zelf, de print is het enige stuk dat je (laat) maakt. Ik leg dat vast en scherp één punt aan.

Eén ding wil ik zeker juist hebben: bedoel je dat er op de print **enkel de LED en de sockets** komen (dus als kant-en-klaar-gesoldeerd bord, of door jou gesoldeerd), of komen daar ook de voedingsonderdelen op (buck, LDO, zekering, weerstanden/condensatoren)? Dat bepaalt hoeveel voetafdrukken en welke stuklijst we in de print opnemen.

---

## AI · 10:03

Opgeslagen:

- **`data/beslissingen.md`** — beslissing `2026-10-06`: alle componenten zelf aankopen; de print is het enige gemaakte stuk, met LED + sockets erop.
- **`data/pcb-ontwerp.md`** — nieuwe sectie "2b. Wat koopt de gebruiker zelf aan" (BOM splitsen in "zelf kopen" vs. "op de print").
- **`data/open-vragen.md`** — open vraag: wat komt er precies op de print (enkel LED + sockets, of ook buck/LDO/zekering/passieven)?

Laat weten of de voedingsonderdelen op de print horen; dan werk ik de voetafdrukken- en stuklijst in `pcb-ontwerp.md` verder uit.

---

## Gebruiker · 10:04

> [!quote] Verbatim
> /Welke componenten mis ik nog die nog niet genoteerd zijn. Ik heb al https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora en https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055?utm_source=google&utm_medium=cpc&utm_campaign=**Pmax%20shopping%20-%20BE&utm_id=21792943403&gad_source=1&gad_campaignid=21786496926&gbraid=0AAAAADlsH-RVkRNPxCk_phI1YyHZBuSbQ&gclid=CjwKCAjwwrPVBhA1EiwAv_YO-a2l1pldsOrys8-FClir3oxheNCzRPChLfDNbAfEPx7hYAYMa2NA8hoCctoQAvD_BwE

## AI · 10:04

Ik kijk eerst wat die twee modules precies bevatten, dan vergelijk ik met de componentenlijst in het project.

---

## AI · 10:04

Antratek blokkeert geautomatiseerde toegang. Ik zoek de specificaties elders op.

---

## AI · 10:04

Even opnieuw, zoekproviders gaven een rate limit.

---

## AI · 10:05

Ik heb beide modules opgezocht. Belangrijk: de XIAO-kit is **ESP32-S3 + LoRa (SX1262) in één**, dus die twee posten zijn nu samen gekozen. Hieronder eerst je antwoord, daarna leg ik alles vast.

## Wat je al hebt (nu officieel gekozen)

| Functie | Onderdeel | Bron |
| --- | --- | --- |
| Rekenkern + LoRa | **XIAO ESP32S3 + Wio-SX1262 kit** (`SX1262`, SPI via B2B, IPEX-antenne, USB-C, LiPo-lader) | antratek |
| 9-DoF IMU + sensorfusie | **Adafruit BNO055-breakout** (I2C 0x28/0x29, 3,3 V regelaar + level shifting, 20×27×4 mm, gaten 20×12 mm) | antratek |

Let op: dit verandert je bord. De XIAO en SX1262 zitten via een **board-to-board-connector** aan elkaar, dus op de draagprint is dat één module. Bovendien heeft de XIAO een **ingebouwde LiPo-lader** — daardoor kan de hele 7,4 V → buck → LDO-voeding vervallen en volstaat een 3,7 V LiPo. Dat is een grote open vraag.

## Componenten die nog ontbreken of niet genoteerd zijn

**Sensoren — nog te kiezen**
- Barometer (BMP581/BME280 kandidaat, nog niet gekozen)
- RTK-GNSS-module (de Seeed L76K is GNSS maar **geen RTK**; voor 0,5 m heb je een RTK-module nodig, bv. u-blox ZED-F9P)
- RTK-correctiebron: eigen basisstation of NTRIP-dienst

**Antennes / RF**
- **GNSS-antenne** (actieve antenne met LNA + ground plane) — nog niet genoteerd
- LoRa IPEX → SMA-pigtail + SMA-bulkhead als je antenne door de behuizing wil
- (LoRa-antenne zit vermoedelijk bij de kit — controleer dat)

**Voeding — grotendeels nog niet genoteerd**
- **Aan/uit-schakelaar of knop** — ontbreekt volledig in de lijst
- Batterij: 3,7 V LiPo met beschermcircuit (XIAO-laadroute) **of** 7,4 V + buck/LDO — nog te beslissen
- Buck 5 V, LDO 3,3 V, zekering, ompoolbeveiliging, TVS (afhankelijk van die keuze)
- JST-batterijconnector + kabel
- (Power-LED + weerstand, decoupling: al genoteerd)

**Verbindingen**
- **USB-C datakabel** (programmeren) — nog niet genoteerd
- UART-draden meettoestel ↔ Arduino + gemeenschappelijke ground + level shifter
- Uitbreidingsconnector: exacte stekker nog niet gekozen
- Dupont/siliconendraad voor interne bekabeling

**Montage / behuizing**
- M3-schroeven, moeren, **afstandsbusjes (standoffs)**, nylon spacers — nog niet genoteerd
- (3D-behuizing + rubberen dempingsbussen: al genoteerd)

**Laptop-/ontvangerzijde**
- LoRa-ontvanger aan de laptop: tweede XIAO-kit of USB-LoRa-dongle — nog geen keuze
- De **USB-stick-ontvanger** uit de specs: hardware nog niet gekozen

**Mock-up (vliegtuigje)**
- Arduino-bord (welk model?) — nog niet gekozen
- 3× servo's + **servo-voeding/BEC** — nog niet genoteerd
- Stuurstangen/scharnieren/roerbladen, rompmateriaal

**Gereedschap/verbruik (vaak vergeten)**
- Digitale **schuifmaat** (nodig voor de footprint-maten), soldeerbout/tin/flux, multimeter, USB-serieel adapter

> [!warning] Belangrijkste gevolg
> Door de XIAO-kit is ESP32 **en** LoRa in één, en de pinlijst is beperkt tot ± 14 I/O. Check of er genoeg pinnen overblijven voor IMU + barometer + GNSS + UART naar de Arduino. En beslis de voedingsroute (3,7 V vs 7,4 V) — dat schrapt of voegt een hoop onderdelen toe.

Ik leg dit nu vast als centrale componentenlijst.

---

## AI · 10:06

Opgeslagen:

- **`data/componenten.md`** — nieuwe centrale **BOM/werklijst**: gekozen (XIAO-kit, BNO055), nog te kiezen (barometer, RTK-GNSS, voeding, ontvanger, servo's) en "nog te noteren" (antennes, aan/uit-schakelaar, standoffs, USB-C-kabel, servo-voeding, gereedschap).
- **`data/beslissingen.md`** — beslissing `2026-10-06`: XIAO ESP32S3 + Wio-SX1262 kit (ESP32 + LoRa in één) en Adafruit BNO055 als IMU.
- **`data/specificaties.md`** — specificatie met de gevolgen voor de print.
- **`data/open-vragen.md`** — IMU-vraag afgevinkt; LoRa-band → 868 MHz voor België; voedingsroute (3,7 V LiPo vs 7,4 V) toegevoegd als groot open punt; pin-budget XIAO genoteerd.
- **`data/links.md`** — antratek-URL's, Seeed-wiki en Adafruit-datasheet.
- **`onderwerpen.md`** — link `[[componenten]]`.

Twee dingen om nu te beslissen, want ze bepalen hoeveel er nog op de print komt:
1. **Voeding:** 3,7 V LiPo (XIAO laadt zelf, keten vervalt) of toch 7,4 V + buck/LDO?
2. **Pin-budget:** tel na of de ± 14 I/O van de XIAO volstaan voor IMU + barometer + GNSS + UART naar de Arduino.

---

## Gebruiker · 10:08

> [!quote] Verbatim
> 1. 7,4V + buck 2. Zet als taak die de ai later doet

## AI · 10:09

Klaar. Opgeslagen:

- **`data/beslissingen.md`** — twee entries:
  - Voedingsroute: **7,4 V-accu → zekering/ompoolbeveiliging → buck 5 V → LDO 3,3 V**; XIAO op 5 V-pin, ingebouwde LiPo-lader niet gebruikt.
  - Pin-budget XIAO = **AI-taak voor later**.
- **`data/componenten.md`** — voedingsroute als "gekozen" gezet; voeding-onderdelen (accu, zekering, ompoolbeveiliging, buck, LDO, aan/uit-schakelaar) in de lijst; nieuwe sectie **AI-taken**.
- **`data/open-vragen.md`** — voedingsvraag afgevinkt; nieuwe sectie **AI-taken (voert de AI later uit)** met de pinout-/pin-budget-taak.
- **`data/actieplan.md`** — IMU- en voedingstaken afgevinkt; **AI-taak pinout-tabel** toegevoegd bij Voorbereiding.

De AI-taak staat klaar: pinout-tabel van de XIAO opstellen en nagaan of ± 14 I/O volstaan — die pak ik op wanneer je wil.

---
