---
tags: [gstem, chatlog]
sessie: "01a111dc-e614-7490-b89e-c75c3e014649"
gestart: 2026-10-06T15:37:37.179Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a111dc-e614-7490-b89e-c75c3e014649` · gestart 2026-10-06_1737
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 17:50

> [!quote] Verbatim
> Kijk naar de bestellijst en zoek de overige artikelen bij andere websites. Liever EU dan China, maar als het echt moet mag het wel. Quectel LC29H(DA) moet ook een breakout board zijn.

## AI · 17:50

Ik ga de `geen-link`-onderdelen uit de bestellijst onderzoeken bij andere (bij voorkeur EU-)leveranciers.

---

## AI · 17:52

Ik heb genoeg bronnen. Nu werk ik de bestellijst en het archief bij.

---

## AI · 17:53

Klaar. Ik heb de `geen-link`-onderdelen bij andere winkels gezocht (EU-first) en alles in het archief bijgewerkt.

## Wat ik gevonden heb

**Quectel LC29H(DA) — als breakout board (EU)**
- **Waveshare LC29H(DA) GPS/RTK HAT (SKU 25279)** bij **Botland (Polen, EU)**: **€ 70,50 incl. btw**, op voorraad, verzendt binnen 24 u. Dit is een kant-en-klaar bord (geen losse SMD-module) met UART/I²C + Micro-USB, 40-pins header én **meegeleverde actieve dual-band L1/L5-antenne**.
- Alternatieven: **Kamami (PL)** ~€63 · **HESTORE (HU)** €91,21 excl. · **MIKROE GNSS RTK 3 Click** (mikroBUS-breakout) bij TME — momenteel niet op voorraad.
- Niet-EU terugval: **7Semi LC29HDA RTK Board** (Qwiic/USB-C, ~$42, India) — mooiere breakout-vorm, maar buiten de EU.

**Belangrijk gevolg:** de aparte GNSS-antenne (€ 16,93) **vervalt** — de HAT levert een betere dual-band antenne mee.

**Overige onderdelen (EU)**
- LDO **AP2112K-3.3TRG1** → TME (PL), ± €0,27
- TVS **SMBJ10A-TR** → TME, ± €0,50
- P-MOSFET **DMG2301L-7** → Mouser.be/DigiKey (EU-magazijn), ± €0,30 (TME's `-13` is uit voorraad)
- 2 A PTC **Littelfuse 1812L200/16** → Mouser.be/DigiKey, ± €0,40
- 4-pins 3,5 mm schroefklem **DEGSON DG250-3.5-04P** → HESTORE/TME, €0,61
- Precisie/dual-wipe sockets → TME/RS (Preci-Dip)
- M3-montageset → **TinyTronics (NL)** €8,00 / Bits & Parts (NL) €6,95

Nieuw te-bestellen-totaal: **± € 184,48 incl. btw**.

> [!info] Opgeslagen
> - `data/bestellijst.md` — alle rijen + totalen + callouts bijgewerkt, nieuwe winkeltags (TME, Botland, HESTORE, TinyTronics, Mouser)
> - `data/links.md` — nieuwe sectie "Andere winkels" met alle bestelcodes en links
> - `data/bestelschema-pcb.md` — onderdelen op de print nu met concrete bestelcodes/prijzen
> - `data/open-vragen.md` — LC29H, GNSS-antenne en overige `geen-link`-punten afgevinkt
> - `data/beslissingen.md` — beslissing `2026-10-06` toegevoegd

Nog open: DMG2301L leverancier bevestigen (Mouser vs TME-alternatief AO3401A) en de **footprint-afweging** van de 65×30,5 mm HAT op de draagprint.

---

## Gebruiker · 17:59

> [!quote] Verbatim
> update bestellijst excel. leg uit: DMG2301L leverancier bevestigen (Mouser vs TME-alternatief AO3401A) en de footprint-afweging van de 65×30,5 mm HAT op de
>  draagprint.

## AI · 18:01

Nu werk ik `build-bestellijst.py` bij met de nieuwe gegevens en draai ik hem.

---

## AI · 18:02

Ik heb de Excel herbouwd. Even de twee open punten technisch onderbouwen — ik check eerst de MOSFET-specificaties.

---

## AI · 18:03

Klaar. De Excel is herbouwd en de twee open punten zijn uitgezocht. Hieronder de uitleg.

## 1. Excel bijgewerkt

`documenten/Bestellijst-GSTEM.xlsx` is opnieuw gegenereerd via `documenten/build-bestellijst.py` (ik heb eerst `openpyxl` geïnstalleerd). Wijzigingen in het script/de Excel:
- Nieuwe statussen/tags met eigen kleur: `botland`, `tme`, `mouser`, `hestore`, `tinytronics`.
- LC29H-rij is nu de **Waveshare LC29H(DA) HAT** bij Botland (€ 70,50); de **GNSS-antenne-rij staat op "al in bezit"** (meegeleverd).
- Bescherming/LDO/schroefklem/sockets/montage hebben nu echte prijzen + leveranciers i.p.v. "schatting".
- Onderaan **per-winkel-subtotalen** (via `SUMIF`) en een totaalregel.

Gecontroleerde uitkomsten (per winkel, incl. btw):

| Winkel | Bedrag |
| --- | --- |
| Kiwi | € 64,65 |
| antratek.be | € 33,83 |
| Botland (EU) | € 70,50 |
| TME (EU) | € 5,27 |
| Mouser/DigiKey (EU) | € 1,30 |
| HESTORE (EU) | € 0,61 |
| TinyTronics (NL) | € 8,00 |
| **Onderdelen totaal** | **€ 184,16** |
| **+ AISLER-print (3 st.)** | **€ 216,92** |

Het bestelschema-blad in de Excel is ook bijgewerkt: printonderdelen **€ 15,18**, totaal op de print **€ 25,19**, nieuw te bestellen **€ 47,94**.

## 2. DMG2301L vs AO3401A (moet bevestigd worden)

**Waarom dit een echt probleem is** — ik checkte de datasheets:

| | DMG2301L | AO3401A |
| --- | --- | --- |
| Vds | -20 V | **-30 V** |
| **Vgs(max)** | **±8 V** | **±12 V** |
| Rds(on) | 120 mΩ @ -4,5 V | ~60 mΩ @ -4,5 V |
| Leverbaar | TME `-13` **niet op voorraad** (MOQ 10 000); `-7` bij Mouser/DigiKey | **op voorraad bij TME (EU)** |

Twee knelpunten:
1. **Vgs-max**: bij ompoolbeveiliging in de +-lijn hangt de gate aan massa en de source aan de accu → **Vgs = -8,4 V**, terwijl de DMG2301L maar **±8 V** mag. Dat is **over de absolute maximumrating**, dus zonder gate-clamp (bv. 6,2 V-zener) te krap voor onze 2S-accu.
2. **Leverbaarheid**: de DMG2301L-13 die in de BOM staat is bij TME niet leverbaar.

**Wat "bevestigen" betekent** — je kiest één van twee routes en verifieert dat vóór het schema/PCB:
- **Route A – DMG2301L-7 bij Mouser/DigiKey**: BOM en footprint blijven ongewijzigd, maar sinds we de PTC (`1812L200/16`) daar toch al halen kost het geen extra bestelling. Je moet dan wél een **gate-clamp/weerstandsdeler** toevoegen (of een 12 V-variant van de MOSFET kiezen).
- **Route B – AO3401A bij TME**: ruim binnen de specificaties (Vds -30 V, Vgs ±12 V), goedkoper, en dan komen **alle discrete onderdelen in één TME-bestelling** (LDO, TVS, sockets) → minder verzendkosten/leveringen. Nadeel: BOM + KiCad-footprint aanpassen (SOT-23-pinout is standaard G/S/D, maar moet gecontroleerd).

Kort: het gaat dus niet alleen om "welke winkel", maar om **een elektrische correctheid** (Vgs) én **orderbundeling**.

## 3. Footprint-afweging LC29H(DA)-HAT (65 × 30,5 mm)

De draagprint is ontworpen rond **kleine breakouts op sockets**, maar de gekozen Waveshare HAT is met **65 × 30,5 mm** fors en heeft een **2×20 (40-pins) Raspberry Pi-header**, plus Micro-USB en SMA. We gebruiken maar ~6 pinnen (5 V, GND, TX/RX, SDA/SCL). Drie opties:

- **A. HAT rechtstreeks op de draagprint** met een 2×20 female header. Voordeel: mechanisch stevig. Nadeel: 40-pins footprint + veel routing voor 6 nuttige signalen; de HAT overhangt; Micro-USB/SMA moeten bereikbaar blijven; stapelhoogte.
- **B. HAT als los sub-bord aan de rand** (M3-standoffs; SMA naar buiten), verbonden met een korte 6-pins kabel/connector naar de draagprint. Voordeel: draagprint blijft klein, mechanisch ontkoppeld, antenne-aansluiting vrij te plaatsen. Nadeel: extra bedrading/connector, trekontlasting nodig.
- **C. Kleinere breakout kiezen** — bv. de **7Semi LC29HDA** (Qwiic, klein) of **MIKROE GNSS RTK 3 Click** (mikroBUS, ~57×25 mm) — veel makkelijker op een draagprint. Nadeel: 7Semi zit buiten de EU; MIKROE/TME niet op voorraad.

**Waarom dit een afweging (en niet zomaar een detail) is**: de **bordafmeting bepaalt de AISLER-prijs** (€ 0,067/cm²) en de plaatsing van de twee antennes (GNSS-SMA + LoRa-pigtail). Vandaar open vraag.

> [!info] Opgeslagen
> - `documenten/Bestellijst-GSTEM.xlsx` + `build-bestellijst.py` — herbouwd met nieuwe winkels, prijzen en subtotalen
> - `data/bestellijst.md` — totalen gecorrigeerd naar de exacte cijfers (€ 184,16 / € 216,92) en verwijzing naar de Excel
> - `data/componenten.md` — waarschuwingscallout over **Vgs-max DMG2301L (±8 V) vs 8,4 V accu** + AO3401A-alternatief
> - `data/open-vragen.md` — de twee punten uitgewerkt: **MOSFET-keuze** en **HAT-footprint/montage**
> - `data/beslissingen.md` — vermeld dat de Excel herbouwd is

Wil je dat ik meteen één van de twee MOSFET-routes of de montagewijze voor de HAT vastleg?

---

## Gebruiker · 18:07

> [!quote] Verbatim
> Zijn de DMG2301L en AO3401A echt nodig?

## AI · 18:07

Goede vraag — laten we de noodzaak per onderdeel bekijken in plaats van klakkeloos over te nemen. Ik lees eerst wat er al vastligt.

---

## AI · 18:07

Kort antwoord: **nee — en het zijn ook geen twee onderdelen die je naast elkaar nodig hebt.**

## Belangrijkste misverstand eerst

**DMG2301L en AO3401A zijn twee kandidaten voor dezelfde functie** (één P-MOSFET voor ompoolbeveiliging). Je hebt er dus **maximaal één** nodig, nooit beide. De vraag is alleen: *welke*, of *geen enkele*.

## Zijn ze nodig?

Geen van de drie beschermingsonderdelen is **strikt noodzakelijk** om het toestel te laten werken — ze beschermen tegen fouten, ze maken het niet functioneel beter.

| Onderdeel | Functie | Strikt nodig? | Risico als je het weglaat |
| --- | --- | --- | --- |
| **2 A PTC** | zekering tegen kortsluiting | Nee, wel nuttig | LiPo kan bij kortsluiting tientallen A's leveren → hete draden/brand |
| **P-MOSFET** (DMG2301L **of** AO3401A) | ompoolbeveiliging | Nee | accu omgekeerd → buck/XIAO/sensoren stuk (€100+) |
| **TVS SMBJ10A** | spanningspieken dempen | Nee, minst nuttig | spike van servo/buck/hot-plug kan IC's beschadigen |

## Wanneer de MOSFET echt overbodig is

- **Gepolariseerde connector** (XT60, Deans/T-plug, JST-XH): omgekeerd aansluiten is fysiek onmogelijk → ompoolbeveiliging is dan echt niet nodig. De meeste hobby-opstellingen doen het hiermee.
- **Barrel-jack** (wat nu gepland staat): daar kan iemand wél een verkeerde/omgekeerde plug in steken → dán is bescherming zinvol. Dus de noodzaak hangt af van de connector, niet van het toestel.

## Als je tóch een MOSFET wilt: neem de AO3401A

De DMG2301L is niet "fout", maar heeft **Vgs(max) = ±8 V** terwijl de accu 8,4 V levert → je moet er een **zener + weerstand** bijzetten (méér onderdelen). De **AO3401A** (Vds −30 V, Vgs ±12 V) kan rechtstreeks, is goedkoper en zit bij TME. Kortom: **AO3401A vervangt de DMG2301L**, het is geen extraatje.

Simpeler alternatief voor beide: **één Schottky-diode in serie** (~€0,10), maar met ~0,3–0,4 V verlies (bij 5 V/0,5 A → ~0,2 W warmte).

## Drie smaken

- **Minimaal** — PTC behouden (brandveiligheid), MOSFET + TVS schrappen. Scheelt ~€1,70 en 2 SOT-23-footprints.
- **Midden (aanbevolen)** — PTC + AO3401A. Eén correcte MOSFET, geen zener nodig, ~€1.
- **Volledig** — PTC + AO3401A + TVS (huidige plan, maar met de juiste MOSFET).

> [!note] Context
> De XIAO heeft zelf al een **LiPo-lader en 3,3 V-regelaar**, en de **LDO is eerder al als "mogelijk overbodig"** gemarkeerd. De voedingsketen is dus sowieso gegroeid t.o.v. wat strikt nodig is. Als eenvoud het doel is, kun je terug naar **PTC + (diode óf AO3401A)** en de rest schrappen.

Zal ik dit als open vraag archiveren en je voorkeur (minimaal / midden / volledig) doorvoeren in [[bestellijst]] + Excel?

---

## Gebruiker · 18:10

> [!quote] Verbatim
> Zoek alle onderdelen op de lijst zodat ze zeker bestelbaar zijn en kijk naar de verschillende plaatsen waar je de gps rtk kan kopen en zeg dan de verschillen in prijs.

## AI · 18:13

Ik pak dit systematisch aan: ik laat een paar agents de winkels stuk voor stuk verifiëren, terwijl ik zelf de GPS-RTK-prijzen uitzoek.

---
