---
tags: [gstem, data, pcb, bestelschema, kosten, aankoop, aisler]
aangemaakt: 2026-10-06
status: werklijst
---

# Bestelschema PCB bij AISLER

> [!success] Beslissing
> De draagprint wordt gefabriceerd bij **AISLER** (beslissing `2026-10-06`, zie [[beslissingen]]).
> Dit bestelschema zet de **productiekost bij AISLER** en de **kost van de onderdelen op de
> print** samen, zo accuraat mogelijk geschat. Hoort bij [[bestellijst]], [[pcb-ontwerp]],
> [[pcb-methodes-kosten]] en [[componenten]].

## 1. Bordgegevens (uitgangspunt)

| Gegeven | Waarde | Bron |
| --- | --- | --- |
| Laagopbouw | 2 lagen, 1,6 mm, HASL | [[pcb-methodes-kosten]] |
| Afmeting (aanname) | **100 x 75 mm = 75 cm²** | afgeleid uit de schets (verhouding ± 1,36) — [[pcb-schets]] |
| Aantal | 3 (minimum) of 6 | AISLER levert in sets van 3 |
| Service | Budget (standaard) | AISLER |

> [!warning] Aanname
> De **exacte bordafmeting staat nog niet vast**. 100 x 75 mm is een schatting op basis van de
> schetsverhouding en de modulegroottes. Pas de berekening aan zodra de layout in KiCad klaar is.
> **AISLER rekent enkel op oppervlak**, dus de prijs schuift evenredig mee.

## 2. Productiekost bij AISLER

**Formule (2-laags 1,6 mm HASL Budget):**

```text
Prijs (netto) = € 12,00 job fee + € 0,067 per cm² x oppervlak x aantal
```

| Oppervlak | 3 stuks (netto) | 3 stuks (incl. 21% btw) | 6 stuks (netto) | 6 stuks (incl. 21% btw) |
| --- | --- | --- | --- | --- |
| 60 cm² (bv. 100x60) | € 24,06 | € 29,11 | € 36,12 | € 43,71 |
| **75 cm² (100x75, aanname)** | **€ 27,08** | **€ 32,76** | **€ 42,15** | **€ 50,99** |
| 90 cm² (bv. 120x75) | € 30,09 | € 36,41 | € 48,18 | € 58,30 |
| 100 cm² (100x100) | € 32,10 | € 38,84 | € 52,20 | € 63,16 |

> [!info] Wat zit erin
> **Gratis verzending** (wereldwijd), productie vanaf **2 werkdagen** (Budget). Geen extra kosten
> voor gaten, vias of aantal drills. Btw wordt als EU-consument aan het Belgische tarief (21%)
> gerekend. Met een btw-nummer (bv. school) kan netto gefactureerd worden.
> **Blitz-service** (sneller): € 22 job fee + € 0,129/cm² → 75 cm² × 3 = € 51,03 netto (± € 61,74 incl.).

> [!example]- Toekomstoptie: 4-laags ENIG (voor castellated eindversie)
> 4 Layer 1.6mm ENIG Budget: € 14,00 + € 0,13/cm² → 75 cm² × 3 = € 43,25 netto (± € 52,33 incl.).
> Pas relevant als later voor castellated of een professioneler eindproduct wordt gekozen.

## 3. Onderdelen op de print (BOM)

Wat rechtstreeks op de draagprint komt (niet de losse modules). Bron: [[componenten]],
[[open-vragen]] `2026-10-06`.

### 3a. Apart te bestellen — nu gevonden bij EU-winkels (`2026-10-06`)

| Onderdeel | Type / bestelcode | Aantal | Prijs/st | Regel | Winkel |
| --- | --- | --- | --- | --- | --- |
| Sockets | Dual-wipe (XIAO) + precisie/turned-pin Preci-Dip | set | ± € 5,00 | € 5,00 | TME / RS / Mouser |
| Voedingsbescherming | 2 A PTC **Littelfuse 1812L200/16** + **SMBJ10A-TR** — **zonder P-MOSFET** (`2026-10-06`, zie [[afgevoerd]]) | 1 set | ± € 1,00 | € 1,00 | Mouser.be / TME |
| LDO 3,3 V | **AP2112K-3.3TRG1** (SOT-23-5) | 1 | € 0,27 | € 0,27 | TME |
| Schroefklem | 4-pins 3,5 mm **DEGSON DG250-3.5-04P** (of KF128) | 1 | € 0,61 | € 0,61 | HESTORE / TME |
| Montage | M3-schroeven, moeren, standoffs, nylon spacers | set | € 8,00 | € 8,00 | TinyTronics (NL) |
| **Subtotaal 3a** | | | | **± € 14,88** | |

### 3b. Al in de hoofd-[[bestellijst]] (Kiwi/antratek)

| Onderdeel | Type | Prijs (aankoop) | Verbruik per bord | Bron |
| --- | --- | --- | --- | --- |
| Level shifter | TXB0108 (Kiwi) | € 8,70 | € 8,70 | [[bestellijst]] |
| Power-LED + serieweerstand | 3 mm LED + 330 Ω (10-packs) — **heeft de gebruiker thuis** (`2026-10-06`) | € 0,00 | € 0,00 | [[bestellijst]] |
| Ontkoppelcondensatoren | Keramische kit (15 soorten) | € 10,27 | ± € 0,50 | [[bestellijst]] |
| Bulk-elco | 100 µF / 16 V | € 0,59 | € 0,59 | [[bestellijst]] |
| **Subtotaal 3b (per bord gebruikt)** | | | **± € 9,79** | |

> [!note] Level shifter: breakout of IC
> De [[bestellijst]] koos de **TXB0108-breakout (€ 8,70)** voor het gemak. Soldeer je de
> **TXB0104-IC (TSSOP-14)** rechtstreeks, dan kost dat ± **€ 1,80** — een verschil van ± € 6,90.
> Dit is nog een **open keuze** (zie [[open-vragen]]). In de totalen hieronder reken ik met de
> breakout (€ 8,70).

### 3c. Totaal onderdelen op de print

| Variant | Bedrag |
| --- | --- |
| Met TXB0108-breakout | **± € 24,67** |
| Met TXB0104-IC direct gesoldeerd | ± € 17,77 |
| Optioneel: PCB-barreljack (i.p.v. adapter met schroefklem) | + € 1,00 |

## 4. Bestelvolgorde en timing

- [ ] 1. **PCB ontwerpen in KiCad** — layout afronden, DRC, Gerbers/ODB++ exporteren ([[pcb-ontwerp]]).
- [ ] 2. **Bordafmeting definitief nameten** → prijs in AISLER-calculator controleren.
- [ ] 3. **Print bestellen bij AISLER** — Gerber/ODB++ of native KiCad-bestand uploaden, rendering nakijken, 3 of 6 stuks, Budget-service.
- [ ] 4. **Tegelijk: PCB-onderdelen bestellen** — de `geen-link`-set (sockets, voeding, LDO, klem, montage); levertijd is de bottleneck, dus vroeg bestellen.
- [ ] 5. **Kiwi/antratek-bestelling** — level shifter, condensatoren, elco zitten al in de hoofd-[[bestellijst]]; de **LED + 330 Ω heeft de gebruiker thuis** (`2026-10-06`).
- [ ] 6. **Ontvangst en controle** — Gerber-rendering vergelijken met het echte bord (AISLER Rendering Guarantee), daarna solderen.

> [!tip] Timing
> AISLER Budget: bord in **± 2 werkdagen** gemaakt, daarna verzending (Europa ± 1-3 dagen).
> De **losse onderdelen** komen nu bij **EU-winkels** (TME, Eckstein, TinyTronics, Mouser) → geen
> lange levertijd of invoer uit China meer.

## 5. Totaaloverzicht (schatting, incl. btw, 3 borden)

| Post | Bedrag |
| --- | --- |
| AISLER print, 3 st., 75 cm² Budget | € 32,76 |
| Onderdelen op de print (met TXB0108) | € 24,67 |
| **Totaal dit bestelschema** | **± € 57,43** |
| _waarvan al in de hoofd-[[bestellijst]]_ | _± € 9,79_ |
| **Werkelijk nieuw te bestellen** | **± € 47,64** |

> [!warning] Niet inbegrepen
> De **losse modules** (XIAO-kit, BNO085, BMP581, LC29H, GNSS-antenne, pigtail), accu, buck en
> barrel-adapter. Die staan in de hoofd-[[bestellijst]] (losse modules bij Kiwi, antratek en de
> EU-winkels). Dit schema dekt **enkel de print + wat erop gesoldeerd wordt**.

## Gerelateerd

- [[pcb-fabrikanten]] - fabrikantvergelijking (AISLER gekozen)
- [[bestellijst]] - volledige aankooplijst meettoestel
- [[pcb-ontwerp]] - werkwijze en Gerber-export
- [[componenten]] - BOM en keuzes
- [[beslissingen]] - fabrikantkeuze AISLER
