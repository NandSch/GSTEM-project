---
tags: [gstem, chatlog]
sessie: "01a11077-574a-75ac-bebb-acedd806a11d"
gestart: 2026-10-06T09:21:55.535Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11077-574a-75ac-bebb-acedd806a11d` · gestart 2026-10-06_1121
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 11:21

> [!quote] Verbatim
> werk verder

## AI · 11:25

Ik controleer een paar productpagina's op details (prijs, specificatie).

---

## AI · 11:27

Ik heb alle gegevens. Nu maak ik de bestellijst (markdown) en de Excel aan.

---

## AI · 11:28

De bestanden zijn gemaakt. Nu werk ik het archief bij.

---

## AI · 11:28

Klaar. Ik heb alles op **www.antratek.be** gezocht (via hun eigen zoekfunctie; directe paginatoegang was geblokkeerd, dus ik heb met een script de zoekresultaten en prijzen uitgelezen). Wat daar niet staat, is niet elders gezocht, precies zoals gevraagd.

## Resultaat

**Bestanden aangemaakt**
- `GEBRUIKER/data/bestellijst.md` — de volledige bestellijst met tags, link, kost en aantal
- `documenten/Bestellijst-GSTEM.xlsx` — de Excel-versie (met legende-blad, statuskleuren, hyperlinks en een totaalformule)
- `documenten/build-bestellijst.py` — script om de Excel opnieuw te genereren

**Op antratek gevonden (te bestellen)**

| Component | Aantal | Prijs/st |
| --- | --- | --- |
| XIAO ESP32S3 & Wio-SX1262 kit (toestel + ontvanger) | 2 | € 15,13 |
| Adafruit BNO055 9-DoF IMU | 1 | € 36,24 |
| GNSS L1/L5 multi-band antenne (SMA, actief) | 1 | € 120,94 |
| Interface Cable SMA to U.FL (pigtail) | 1 | € 3,57 |
| DC Barrel Jack Adapter - Female | 1 | € 4,78 |
| Logic Level Converter Bi-Directional (i.p.v. TXB0104) | 1 | € 4,78 |
| Arduino Uno Rev3 | 1 | € 41,75 |

**Totaal:** € 242,32 incl. btw (met de L1/L5-antenne). Met de goedkopere magneetantenne (€ 19,30) wordt dat € 140,68.

**Niet op antratek (tag `geen-link`)** — dus geen aankooplink: BMP390, Quectel LC29H(DA), 2S LiPo-accu, voedingsbescherming (PTC + DMG2301L + SMBJ10A), AP2112K-3.3, 4-pins schroefklem, sockets, power-LED, condensatoren, bulk-elco en M3-montage. Voor de RTK-module staan wel antratek-alternatieven in de lijst (LG290P € 217,74 / ZED-F9P € 302,44).

**Tag `al in bezit`:** LoRa-kitantenne, buck 5 V, servo's, servo-voeding, 3D-print, USB-C datakabel, Dupont-draad en gereedschap.

**Let op:** de gekozen TXB0104 staat niet op antratek; de gevonden bidirectionele level converter (BSS138) is een bruikbaar alternatief. De barrel-adapter is geen PCB-montage. Deze punten staan als open vragen.

> [!info] Opgeslagen: `data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx`, `documenten/build-bestellijst.py`, en bijgewerkt: `onderwerpen.md`, `data/componenten.md`, `data/links.md`, `data/beslissingen.md`, `data/open-vragen.md`

---

## Gebruiker · 11:29

> [!quote] Verbatim
> Arduino uno heb ik zelf thuis nog.

## AI · 11:30

Aangepast: de Arduino Uno staat nu op tag `al in bezit` (heeft de gebruiker thuis), met een verwijzing naar de antratek-prijs als referentie.

**Nieuwe totalen (te bestellen bij antratek):**
- Met L1/L5-antenne: **€ 200,57** incl. btw
- Met goedkopere magneetantenne: **€ 98,93** incl. btw

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/componenten.md` en `data/beslissingen.md`.

> [!info] Opgeslagen: aanpassing Arduino → `al in bezit` in `data/bestellijst.md`, `data/componenten.md` en `data/beslissingen.md`; Excel vernieuwd.

---

## Gebruiker · 11:30

> [!quote] Verbatim
> Zorg ervoor dat de onderdelen die je goedkoper kan vinden dat je die gebruikt. dat het totaal niet absurt wordt

## AI · 11:30

Ik ga voor elk onderdeel op antratek naar goedkopere alternatieven zoeken en die gebruiken waar ze aan de eisen voldoen.

---

## AI · 11:32

Ik lees de huidige bestellijst om de goedkopere keuzes door te voeren.

---

## AI · 11:33

Klaar. Ik heb waar mogelijk het goedkoopste passende alternatief op antratek gekozen.

## Wat is goedkoper geworden

| Component | Was | Nu (goedkoopst op antratek) | Verschil |
| --- | --- | --- | --- |
| GNSS-antenne | L1/L5 multi-band € 120,94 | GPS/GNSS magneetantenne SMA 3m (actief, L1) € 19,30 | − € 101,64 |
| Barometer | BMP390 (niet op antratek) | BME280 breakout € 19,97 | leverbaar i.p.v. geen link |
| Arduino Uno | € 41,75 | in bezit (thuis) | − € 41,75 |

De rest was al de goedkoopste passende optie op antratek: XIAO-kit € 15,13 (losse XIAO + Wio-SX1262 is zelfs 14 cent duurder), BNO055 € 36,24 (goedkoopste 9-DoF met fusie), U.FL–SMA pigtail € 3,57, barreljack € 4,78 en level converter € 4,78.

## Nieuwe totalen (incl. btw)

| Scenario | Bedrag |
| --- | --- |
| **Standaard goedkoopste complete set** | **€ 118,90** |
| Met dual-band L1/L5-antenne (optionele upgrade) | € 220,54 |
| Zonder barometer (BMP390 elders) | € 98,93 |

**Let op:** de goedkope magneetantenne is enkelbandig (L1), dus RTK werkt wel maar minder robuust dan met L1/L5. De dure antenne staat als expliciete upgrade vermeld.

**Niet in het totaal:** de RTK-module (LC29H(DA)) staat niet op antratek. Het goedkoopste antratek-alternatief (LG290P) kost € 217,74 en zou het totaal naar ~€ 336,64 duwen — daarom blijft de LC29H als `geen-link` (elders te regelen).

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/links.md`, `data/beslissingen.md` en `data/componenten.md`.

> [!info] Opgeslagen: goedkopere alternatieven (BME280, magneetantenne) → `data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx`, `data/links.md`, `data/beslissingen.md` en `data/componenten.md`.

---

## Gebruiker · 11:38

> [!quote] Verbatim
> Deze onderdelen heb ik: USB-A naar USB-C voor de XIAO, DC Barrel Jack Adapter - Female, 2S LiPo met connector en kabel,

## AI · 11:39

Toegevoegd als `al in bezit` (had je al): 2S LiPo-accu, DC Barrel Jack Adapter - Female en de USB-A naar USB-C kabel. Ze vallen uit het te-bestellen-totaal.

## Nog te bestellen bij antratek

| Component | Bedrag |
| --- | --- |
| 2x XIAO ESP32S3 + Wio-SX1262 kit | € 30,26 |
| Adafruit BNO055 IMU | € 36,24 |
| BME280 barometer | € 19,97 |
| GPS/GNSS magneetantenne (SMA) | € 19,30 |
| U.FL naar SMA pigtail | € 3,57 |
| Logic Level Converter | € 4,78 |
| **Totaal** | **€ 114,12** |

Alternatieven: met de dual-band L1/L5-antenne wordt het **€ 215,76**; zonder barometer **€ 94,15**.

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/componenten.md` en `data/beslissingen.md`.

> [!info] Opgeslagen: 2S LiPo, barrel-adapter en USB-A/USB-C kabel → `al in bezit` in `data/bestellijst.md`, `data/componenten.md` en `data/beslissingen.md`; Excel vernieuwd.

---

## Gebruiker · 11:46

> [!quote] Verbatim
> How accurate is the barometer in height in meters?

## AI · 11:46

Goede vraag — bij een barometer hangt de hoogtenauwkeurigheid rechtstreeks aan de druknauwkeurigheid. Even de omrekening: dicht bij de grond is **1 hPa ≈ 8,3 m** hoogte (de schaalhoogte is ~8434 m; exact: Δh ≈ 8,43 m per hPa op zeeniveau).

## Specificatienauwkeurigheid (datasheet)

| Sensor | Relatieve druk | Absolute druk | Relatieve hoogte | Absolute hoogte |
| --- | --- | --- | --- | --- |
| **BMP390** | ±0,03 hPa | ±0,5 hPa | **±0,25 m** | ±4 m |
| **BME280** | ±0,12 hPa | ±1 hPa | **±1 m** | ±8 m |

- **BMP390**: ±0,03 hPa → **±0,25 m** bij hoogteverschillen (bv. stijgen/dalen in de vlucht).
- **BME280**: ±0,12 hPa → **±1 m** bij hoogteverschillen.

## Maar in de praktijk...

De echte fout wordt zelden bepaald door de sensor, maar door de **referentie**:

1. **Absolute hoogte** (zonder ijkpunt): beperkt door het weer. De luchtdruk op zeeniveau schommelt makkelijk ±5–10 hPa → **tientallen meters fout**. Een barometer alleen geeft dus geen betrouwbare absolute hoogte.
2. **Relatieve hoogte** (t.o.v. een gemeten startdruk): dan haal je de sensorfout — **±0,25 m** (BMP390) of **±1 m** (BME280), over een vlucht van enkele minuten.
3. **Drift**: over 10–30 min kan de luchtdruk door weer veranderen; een verschil van 1 hPa = 8,3 m schijnbare hoogte.

## Voor G-Stem

Omdat je ook GNSS/RTK hebt, is de logische rolverdeling:
- **GNSS/RTK** = trage maar absolute referentie (horizontaal cm, verticaal dm–m).
- **Barometer** = snelle, fijne **relatieve** hoogteveranderingen (stijgen/dalen) waar GNSS te traag/noisy is.

Daarom is de **BMP390** de betere keuze voor een precisiehoogtemeter (factor 4 fijner dan de BME280), terwijl de **BME280** prima is als je enkel ruwe relatieve hoogte wil en kosten wilt drukken.

**Let op:** in de bestellijst stond "±1 hPa" — dat is de *absolute* fout van de BME280; de *relatieve* (belangrijkste voor hoogteverschillen) is ±0,12 hPa ≈ ±1 m. Wil je dat ik die opmerking verfijn en de hoogtecijfers in `data/specificaties.md` opneem?

---

## Gebruiker · 11:48

> [!quote] Verbatim
> Dan ga ik voor de barometer toch liever voor een beter model.

## AI · 11:48

Ik zoek eerst op antratek of er een nauwkeuriger barometer is; anders kijk ik elders.

---

## AI · 11:49

Geen nauwkeurige barometer op antratek. Dan zoek ik elders (Europa/België) naar de BMP390 of beter.

---

## AI · 11:49

Web_search blijft op 429. Ik ga rechtstreeks bij Europese leveranciers kijken.

---

## Gebruiker · 11:50

> [!quote] Verbatim
> Don't search on other sites yet.

## AI · 11:50

Begrepen, ik stop met zoeken op andere sites. Ik heb het tijdelijk opgeslagen HTML-materiaal van externe shops meteen opgeruimd.

---

## AI · 11:50

Genoteerd, ik zoek voorlopig niets meer op andere sites.

Ik leg je voorkeur wel even vast in het archief (zonder al een leverancier te kiezen):

---

## AI · 11:50

Oké, gestopt met zoeken op andere sites.

Vastgelegd (zonder leverancier te kiezen):
- **Voorkeur barometer:** nauwkeuriger model (BMP390 of beter) i.p.v. de BME280.
- **Status:** antratek heeft BMP390/BMP388/BMP581 niet; zoeken bij andere leveranciers is **uitgesteld**.
- De BME280 blijft voorlopig als **plaatsvervanger** in de bestellijst/totalen staan (€ 114,12).

Bijgewerkt: `GEBRUIKER/data/bestellijst.md` en `data/open-vragen.md`. Tijdelijke zoekbestanden van externe shops zijn verwijderd.

Zeg maar wanneer ik verder mag zoeken (en mag ik dan een voorkeur voor regio/leverancier, bv. België/Nederland)?

---

## Gebruiker · 11:54

> [!quote] Verbatim
> Ik wil het aantal aan verschillende websites waarvan ik bestel limiteren om verzendskosten klein te houden. Kijk nu wat je van de overige onderdelen kan aankopen op deze website: https://www.kiwi-electronics.com/nl IK heb hier ookal een goedkopere van deze gevonden: https://www.kiwi-electronics.com/nl/adafruit-9-dof-orientation-imu-fusion-breakout-bno085-bno080-stemma-qt-qwiic-11273

## AI · 11:54

Top — dan gaan we zoveel mogelijk bij **Kiwi Electronics** samenbrengen. Ik bekijk eerst hun zoekmechanisme en de BNO085-pagina.

---

## AI · 11:55

Kiwi heeft de **BNO085 (€ 32,05, op voorraad — goedkoper én nieuwer dan de BNO055)** en de **BMP390L (€ 12,09, maar momenteel niet op voorraad)**. Ik doorzoek nu de rest.

---

## AI · 11:56

Belangrijke vondst: Kiwi heeft de **Adafruit BMP581 (€ 10,88, op voorraad)** — nieuwer en veel nauwkeuriger dan de BME280. Ik check nog RTK, connectoren en bevestiging.

---

## AI · 11:57

Ik heb de hele Kiwi-catalogus doorzocht. Even mijn bevindingen vastleggen en dan het overzicht.

---

## AI · 11:58

Ik heb de volledige **Kiwi Electronics**-catalogus doorzocht op elk nog te kopen onderdeel.

## ✓ Wel bij Kiwi Electronics te koop

| Onderdeel | Kiwi-product | Prijs | Voorraad |
| --- | --- | --- | --- |
| IMU | **Adafruit BNO085 (BNO080)** 9-DoF fusion | € 32,05 | op voorraad |
| Barometer | **Adafruit BMP581** I²C/SPI | € 10,88 | op voorraad |
| GNSS-antenne (actief, SMA) | GPS Antenne – Externe Actieve – 3-5V 28dB 5 m SMA | € 16,93 | op voorraad |
| U.FL → SMA pigtail | SMA naar uFL/u.FL/IPX/IPEX RF kabel | € 4,22 | op voorraad |
| Level shifter 3,3↔5 V | **8-kanaals bidirectionele TXB0108** | € 8,70 | op voorraad |
| Rekenkern | Seeed Studio XIAO ESP32S3 | € 8,46 | op voorraad |
| Power-LED + weerstand | 3 mm LED (10-pack) + weerstand (10-pack) | € 1,20 + € 0,96 | op voorraad |
| Bulk-elco 100 µF/16 V | 100uF 16V condensator | € 0,59 | op voorraad |
| Schroefklem | Schroefterminal 3,5 mm **3-weg** | € 1,20 | op voorraad |
| LoRa-module | Wio-SX1262 voor XIAO | € 5,43 | **niet op voorraad** |

Je **BNO085-tip klopt**: € 32,05 in plaats van € 36,24 voor de BNO055 bij antratek — nieuwer (sensorfusie) én goedkoper.
Ook mooi: de **BMP581** is een *next-generation* barometer (ruis tot 0,08 Pa ≈ 1 cm; rel. nauwkeurigheid ±0,4 Pa ≈ 3 cm; absoluut ±30 Pa ≈ 2,5 m). Veel beter dan BME280, in voorraad, en € 10,88.

## ✗ Niet bij Kiwi Electronics

- **RTK-GNSS-module** — géén LC29H/ZED-F9P; enkel de **niet-RTK L76K** (€ 15,11). Dit is het grote knelpunt.
- **Discrete voeding:** 2 A PTC-zekering, P-MOSFET DMG2301L, TVS SMBJ10A, AP2112K-3.3.
- **4-pins** 3,5 mm schroefklem (alleen 3-weg).
- **Precisie/dual-wipe sockets** en **M3-schroeven/standoffs**.

## Consequentie voor het aantal winkels

- De LoRa-module (Wio-SX1262) is bij Kiwi **uit voorraad** → de radio kan daar nu niet vandaan.
- De **RTK-module** is er niet → daarvoor is sowieso minstens één andere winkel nodig.

Dus zelfs met Kiwi blijft het minimum waarschijnlijk **2 winkels** (Kiwi + één voor RTK/LoRa en de discrete onderdelen). Zal ik de bestellijst omzetten om alles wat kan naar **Kiwi** te verhuizen (BNO085, BMP581, antenne, pigtail, TXB0108, LED/R/C, XIAO), en de rest als tweede-winkel-items markeren? Dan kan ik ook bekijken of die ene tweede winkel dan zowel de LoRa als de RTK-module én de discrete onderdelen kan leveren.

Vastgelegd: alle Kiwi-bevindingen (links, prijzen, voorraad) staan nu in `GEBRUIKER/data/links.md`.

---

## Gebruiker · 11:59

> [!quote] Verbatim
> Waarvoor dienen 2 A PTC-zekering, P-MOSFET DMG2301L, TVS SMBJ10A, AP2112K-3.3.

## AI · 11:59

Die vier onderdelen horen allemaal bij de **voedingsketen** van de draagprint. De volgorde is:

```
7,4 V-accu (max 8,4 V) / barrel
        │
   ┌────┴─────────────────────────────┐
   │ 2A PTC  +  P-MOSFET  +  TVS      │  ← bescherming bij de ingang
   └────┬─────────────────────────────┘
        │
   buck 5 V  ──  bulk-elco 100 µF
        │
   LDO AP2112K-3.3
        │
   3,3 V-rail → IMU, barometer, GNSS, level shifter
```

## 1. 2 A PTC-zekering — overstroombeveiliging
Een **herstelbare zekering** in serie met de voeding.
- Bij te veel stroom (kortsluiting, fout) wordt hij warm en springt naar een hoge weerstand → de stroom wordt begrensd.
- Koelt hij af, dan "reset" hij zichzelf automatisch (geen zekering vervangen).
- **Waarom 2 A:** ruim boven het normale verbruik, maar onder wat de accu/bedrading veilig aankan. Beschermt vooral tegen **brandgevaar bij een LiPo**.

## 2. P-MOSFET DMG2301L — ompoolbeveiliging
Beschermt tegen **verkeerd om aansluiten** van de accu of barrel-plug.
- In de **plus-lijn**, met de gate aan massa.
- Juiste polariteit → de P-MOSFET geleidt met zeer lage Rds(on) (~nauwelijks spanningsval).
- Omgekeerde polariteit → hij **blokkeert** en er loopt geen stroom.
- Voordeel t.o.v. een serie-diode: **geen ~0,7 V verlies** en geen warmte.

## 3. TVS SMBJ10A — spanningspieken opvangen
Een **Transient Voltage Suppressor** van de + naar GND.
- Klemt **snelle spanningspieken** af op ~17 V: inductieve spikes van motoren/servo's/ESC, hot-plug-pieken, ESD.
- Laat de normale 7,4–8,4 V ongemoeid.
- **Waarom 10 V standoff:** boven de maximale accuspanning (8,4 V), maar laag genoeg om de buck, LDO en IC's te beschermen.

## 4. AP2112K-3.3 — schone 3,3 V-rail
Een **lineaire LDO** (600 mA, lage dropout).
- Maakt van de schakelende 5 V een **stabiele, ruisarme 3,3 V** voor de sensoren (IMU, barometer, GNSS).
- Een buck converteert efficiënt maar **schakelt** (ruis); een LDO vlakt dat af → belangrijk voor analoge/RF-gevoelige sensoren.
- De XIAO heeft zelf ook 3,3 V, maar die rail deelt de schakelruis; daarom een **eigen, aparte** 3,3 V-rail.

Kort samengevat: **PTC + P-MOSFET + TVS beschermen de ingang** (stroom, polariteit, pieken), de **AP2112K levert een schone 3,3 V**.

> [!info] Opgeslagen: deze uitleg staat nu als callout in `GEBRUIKER/data/componenten.md` (bij "Gekozen").

---

## Gebruiker · 12:00

> [!quote] Verbatim
> Oké, zou je deze niet beter ook op de pcb zetten?

## AI · 12:00

Goede vraag — even kijken wat er nu al gepland staat voor de print.

---

## AI · 12:00

Ja — sterker nog, dat is al de bedoeling van het ontwerp: alle vier horen **op de draagprint**, in de voedingssectie bij de ingang. Ik maak het in de documenten nu expliciet.

---

## AI · 12:00

Ja, absoluut — en dat is al de opzet. Alle vier zijn losse onderdelen die je **rechtstreeks op de draagprint soldeert**, in de **voedingssectie linksboven bij de ingangsconnector**. De buck, accu, barrel-connector en sensormodules blijven losse modules; de print draagt de bescherming + LDO + LED + sockets + level shifter.

## Waarom op de print (en niet los)

- **Bescherming hoort zo dicht mogelijk bij de ingang** → kortste pad, beste klemming van pieken en de laagste inductie. In de kabel zou de bedrading erachter onbeschermd blijven.
- **LDO dicht bij de sensoren** → korte, schone 3,3 V-sporen.
- **Minder losse onderdelen/draden** die kunnen loskomen in een trillend vliegtuigje.
- Alles in **één soldeer-/fabricagestap**.

## Aandachtspunten

1. **Behuizing kiezen i.f.v. handmatig solderen.** De gekozen types zijn SMD en vrij klein:
   - AP2112K = **SOT-23-5**; DMG2301L = **SOT-23**; SMBJ10A = **DO-214AA** (SMD).
   - Through-hole-alternatieven: **AMS1117-3.3** (SOT-223/TO-220), **P6KE10A** (TVS), radiale **PTC**.
   Voor een met de hand gesoldeerde schoolprint is through-hole of SOT-223 vaak prettiger. Ik heb dit als open punt in [[pcb-schets]] gezet.
2. **Plaatsingsorde op de print:** ingang → PTC → P-MOSFET (ompool) → TVS → naar de buck → 5 V terug → bulk-elco → LDO → 3,3 V-rail.
3. **Kanttekening:** als de PTC óp de print zit, zijn de draden **van accu naar print** niet beschermd. Voor LiPo-veiligheid kan een zekering dicht bij de accu zelf ook nuttig zijn — klein extraatje, geen must.
4. **Footprints in KiCad:** deze vier hebben geen kant-en-klare module-footprint; je neemt de standaard footprint van de gekozen behuizing (SOT-23, DO-214AA, enz.).

Vastgelegd:
- `GEBRUIKER/data/beslissingen.md` — beslissing "voedingsbescherming + LDO op de draagprint".
- `documenten/PCB-schets.md` — voedingsboom en de zone linksboven nu expliciet met PTC + P-MOSFET + TVS + LDO; plus open punt over SMD vs. through-hole behuizing.

Wil je dat ik ook de **buck-converter** op de print zet (i.p.v. een losse module)? Dan is de hele voedingsketen op één bord, wat het aantal losse verbindingen verder verkleint.

---
