---
tags: [gstem, chatlog]
sessie: "01a110f1-572a-76f2-a0e8-3dc3f275d550"
gestart: 2026-10-06T11:20:14.682Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a110f1-572a-76f2-a0e8-3dc3f275d550` · gestart 2026-10-06_1320
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 13:21

> [!quote] Verbatim
> Waar zou ik het best mijn pcb bord laten maken? denk aan prijs en simpel gebruik. geef ook een keuze binnen europa en buiten.

## AI · 13:21

Er is al veel archief over PCB. Ik lees de relevante bestanden om aan te sluiten.

---

## AI · 13:21

Ik zoek actuele prijzen en gebruiksvriendelijkheid van PCB-fabrikanten (binnen en buiten Europa).

---

## AI · 13:23

Ik heb genoeg actuele data. Ik maak het antwoord en werk het archief bij.

---

## AI · 13:23

## Kort antwoord

Voor jullie draagprint (2-laags carrier, klein prototype) zijn er twee duidelijke winnaars, afhankelijk van wat je voorrang geeft:

| Prioriteit | Fabrikant | Waar | Richtprijs 5 st. (10x8 cm, 2-laags) | Gemak |
| --- | --- | --- | --- | --- |
| **Goedkoopst** | **JLCPCB** | China | ± € 8-20 totaal (bord ± € 2-5 + verzending) | Zeer makkelijk, browserpreview |
| **Makkelijkst binnen Europa** | **AISLER** | DE/NL | ± € 28 excl. / € 34 incl. btw (min. 3 st.) | Zeer makkelijk, KiCad/ODB++ direct, gratis verzending |
| **Professioneel / studentenkorting** | **Eurocircuits** | BE | ± € 30-60 | Meer configuratie, studentenprogramma |

### Buiten Europa
- **JLCPCB** — de prijsbreker. 2 lagen is meer dan genoeg. Bord kost bijna niets; de verzendkeuze bepaalt de rekening. Btw/inklaring komt erbij, levertijd 1-3 weken.
- **PCBWay** — vergelijkbaar, iets duurder, goede support en assemblage-opties.
- **OSH Park** (VS) — mooie kwaliteit en ENIG, maar $5/inch² per set van 3: voor 80 cm² (± 12,4 inch²) al ± $62. Duur per cm².

### Binnen Europa
- **AISLER** — het simpelst: vaste prijs per oppervlak (Job fee € 12 + € 0,067/cm² voor 2-laags HASL), geen verrassingen voor gaten/via's, productie vanaf 2 werkdagen, gratis verzending. Voor ± 80 cm² × 3 st. ≈ € 28 excl. btw.
- **Eurocircuits** (BE) — professioneel, meer instelmogelijkheden, en belangrijk: ze hebben een **studenten-/lerarenprogramma met korting**. Voor een schoolproject het bekijken waard.
- **Multi-CB**, **BETA LAYOUT / LeitOn** (DE) — degelijke Duitse alternatieven, iets duurder.

> [!info] Opgeslagen
> - `data/pcb-fabrikanten.md` — volledige vergelijking (prijs + gemak, binnen/buiten EU), met het advies.
> - `data/links.md` — links naar JLCPCB, PCBWay, OSH Park, AISLER, Eurocircuits, Multi-CB.
> - `data/open-vragen.md` — de fabrikantkeuze bijgewerkt; definitieve keuze staat nog open.
> - `onderwerpen.md` — nieuw topic [[pcb-fabrikanten]].

**Mijn advies voor dit project:** **JLCPCB voor de prijs, AISLER voor het gemak binnen Europa.** Overweeg Eurocircuits als de studentenkorting de meerprijs goedmaakt en je een "EU-verhaal" wil. Voor gewoon 2-laags is beide ruim voldoende.

---

## Gebruiker · 13:25

> [!quote] Verbatim
> Wij gaan voor aisler. onthoud de rest ook. Zet de kost onderdelen voor de pcb bij aisler ook het betellingschema. probeer zo accuraat mogelijk de prijs in te schatten.

## AI · 13:25

Beslissing genoteerd. Ik lees eerst de bestellijst en de PCB-schets om de prijs zo accuraat mogelijk te berekenen.

---

## AI · 13:26

Ik probeer nog actuele prijzen op te halen voor de discrete onderdelen zonder link.

---

## AI · 13:26

## Beslissing: AISLER

Genoteerd. De draagprint laten we maken bij **AISLER** (EU). Alle andere fabrikanten (JLCPCB, PCBWay, Seeed Fusion, OSH Park, Eurocircuits, Multi-CB, BETA LAYOUT/LeitOn) blijven bewaard in het archief als gekend-maar-niet-gekozen.

## Kostenschatting — bestelschema PCB

De volledige berekening staat in `data/bestelschema-pcb.md`. AISLER rekent **enkel op oppervlak**, dus ik heb de bordgrootte afgeleid uit de schetsverhouding.

> [!warning] Aanname
> Bord = **100 x 75 mm (75 cm²)**, 2-laags 1,6 mm HASL. De definitieve maat volgt pas uit de KiCad-layout; de prijs schuift evenredig mee.

### 1. Productie bij AISLER
Formule Budget: `€ 12,00 + € 0,067/cm² × oppervlak × aantal` (sets van 3, gratis verzending, 2 werkdagen)

| Oppervlak | 3 stuks incl. 21% btw | 6 stuks incl. btw |
| --- | --- | --- |
| 60 cm² | € 29,11 | € 43,71 |
| **75 cm² (aanname)** | **€ 32,76** | € 50,99 |
| 90 cm² | € 36,41 | € 58,30 |
| 100 cm² (100x100) | € 38,84 | € 63,16 |

Blitz (sneller): ± € 61,74. 4-laags ENIG later (castellated): ± € 52,33 voor 3.

### 2. Onderdelen op de print

| Post | Bedrag |
| --- | --- |
| Apart te bestellen: sockets, voeding (PTC+DMG2301L+TVS), AP2112K-3.3, schroefklem, M3-montage | € 10,85 |
| Uit hoofd-bestellijst: TXB0108, LED+weerstand, condensatoren, bulk-elco | ± € 10,01 |
| **Totaal onderdelen op de print** | **± € 20,86** |
| _variant met TXB0104-IC i.p.v. breakout_ | _± € 13,96 (bespaart ± € 6,90)_ |

### 3. Totaal (3 borden, incl. btw)

| Post | Bedrag |
| --- | --- |
| AISLER print | € 32,76 |
| Onderdelen op de print | € 20,86 |
| **Totaal** | **± € 53,62** |
| _waarvan al in de hoofd-bestellijst_ | _± € 10,01_ |
| **Werkelijk nieuw te bestellen** | **± € 43,61** |

Niet inbegrepen: de losse modules (XIAO-kit, BNO085, BMP581, LC29H, antenne), accu/buck/barrel-adapter — die staan in de hoofd-bestellijst.

## Bestelvolgorde
1. KiCad-layout afronden, Gerbers/ODB++ exporteren.
2. Bordmaat definitief meten → AISLER-calculator controleren.
3. Print bestellen bij AISLER (3 of 6 stuks, Budget).
4. Tegelijk de `geen-link`-onderdelen (sockets, voeding, LDO, klem, montage) bestellen — langste levertijd uit China.
5. Kiwi/antratek-bestelling (level shifter, LED, caps, elco).
6. Rendering vs. echt bord controleren, dan solderen.

> [!info] Opgeslagen
> - `data/beslissingen.md` — beslissing **PCB-fabrikant: AISLER**.
> - `data/bestelschema-pcb.md` — nieuw: productiekost + onderdelen op de print + bestelvolgorde.
> - `data/pcb-fabrikanten.md` — AISLER gemarkeerd als gekozen; rest bewaard.
> - `data/open-vragen.md` — fabrikantvraag afgesloten; nieuwe open punten: **bordafmeting** en **TXB0108-breakout vs. TXB0104-IC**.
> - `data/bestellijst.md` en `data/links.md` — AISLER + verwijzing naar het bestelschema.
> - `onderwerpen.md` — nieuw topic [[bestelschema-pcb]].

Twee open punten om de schatting definitief te maken: de **bordafmeting** en of je de **level shifter als IC of breakout** neemt (± € 6,90 verschil).

---

## Gebruiker · 13:28

> [!quote] Verbatim
> update excel bestand

## AI · 13:28

Ik werk de generator `documenten/build-bestellijst.py` bij (AISLER + PCB-onderdelen) en genereer daarna de xlsx opnieuw.

---

## AI · 13:29

Klaar. Het Excel-bestand is bijgewerkt en opnieuw gegenereerd met `python documenten/build-bestellijst.py`.

**`documenten/Bestellijst-GSTEM.xlsx`** heeft nu drie bladen:

1. **Bestellijst** — aangevuld met:
   - Nieuwe categorie **Draagprint (PCB bij AISLER)**: 3 stuks, ± € 10,92/st = **€ 32,76**.
   - De PCB-onderdelen kregen geschatte prijzen en status `schatting`: sockets € 5,00, voedingsbescherming € 0,95, LDO € 0,35, schroefklem € 0,55, M3-montage € 4,00.
   - Nieuwe totalen: Kiwi, antratek, **AISLER (€ 32,76)**, **PCB-onderdelen (€ 10,85)** en **totaal alles**.

2. **Legende** — tags `aisler` en `schatting` toegevoegd.

3. **Bestelschema PCB** (nieuw) — AISLER-formule + prijstabel per oppervlak (3/6 stuks), de onderdelen op de print, de totalen (€ 53,62 totaal / € 43,61 nieuw) en de bestelvolgorde.

De rekenbladen gebruiken formules (`SUMIF`), dus zodra je prijzen of de bordmaat aanpast, rekenen de totalen automatisch mee.

> [!info] Opgeslagen
> - `documenten/build-bestellijst.py` — AISLER-categorie, `schatting`-prijzen, extra totalen en het blad **Bestelschema PCB**.
> - `documenten/Bestellijst-GSTEM.xlsx` — opnieuw gegenereerd.
> - `data/links.md` — notitie bijgewerkt (drie bladen).

Let op: de bordmaat is nog een aanname (100 × 75 mm). Zodra de KiCad-layout klaar is, vul je de echte oppervlakte in en schuift de AISLER-prijs evenredig mee.

---
