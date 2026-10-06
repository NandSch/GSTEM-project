---
tags: [gstem, data, pcb, hardware, fabrikant, kosten, vergelijking]
aangemaakt: 2026-10-06
status: analyse
---

# PCB-fabrikanten: binnen en buiten Europa

> [!info] Doel
> Waar laten we de **draagprint** maken? Vergelijking op **prijs** en **simpel gebruik**,
> met een keuze **binnen Europa** en **buiten Europa**. Hoort bij [[pcb-ontwerp]],
> [[pcb-methodes-kosten]] en [[bestellijst]].

## Uitgangspunt

- **Bord:** 2-laags draagprint (carrier) met sockets/headers; 2 lagen volstaan (zie [[pcb-methodes-kosten]]).
- **Aantal:** klein prototype, 3-5 stuks.
- **Werkwijze:** Gerber-zip uploaden, fabriek doet eigen DRC. Zie [[pcb-ontwerp]].

## Indicatieve prijzen (peildatum 2026-10-06)

Rekenvoorbeeld: 2-laags bord van **± 10 x 8 cm (± 80 cm²)**, **5 stuks**. Prijzen schommelen en
zijn richtprijzen; altijd de online calculator gebruiken.

### Buiten Europa

| Fabrikant | Land | Prijs (5 st., 2-laags) | Levertijd | Gemak | Opmerking |
| --- | --- | --- | --- | --- | --- |
| **JLCPCB** | China | ± € 8-20 totaal (bord ± € 2-5 + verzending ± € 6-18) | 1-3 weken | Zeer makkelijk; browserpreview, autofix van Gerbers | Goedkoopst. Btw/inklaringskosten komen erbij. Zeer veel gebruikt. |
| **PCBWay** | China | ± € 15-30 totaal | 1-3 weken | Zeer makkelijk; ook assemblage | Iets duurder dan JLCPCB, goede support/opties. |
| **Seeed Studio Fusion** | China | vergelijkbaar met JLCPCB | 1-3 weken | Makkelijk | Alternatief met eigen ecosysteem. |
| **OSH Park** | VS | ± € 55-60 per set van 3 ($5/inch²) | 2-3 weken | Makkelijk, gratis verzending wereldwijd | Mooie kwaliteit + ENIG, maar prijzig per cm². |

### Binnen Europa

| Fabrikant | Land | Prijs (5 st., 2-laags) | Levertijd | Gemak | Opmerking |
| --- | --- | --- | --- | --- | --- |
| **AISLER** | DE/NL | ± € 28 excl. btw / ± € 34 incl. (min. 3 st.) | vanaf 2 werkdagen productie | Makkelijkst in EU; accepteert **KiCad-native/ODB++**, gratis verzending | Enkel prijs op **oppervlak** (Job fee € 12 + € 0,067/cm² voor 2-laags HASL Budget). |
| **Eurocircuits** | BE | ± € 30-60 | enkele dagen-week | Meer configuratie, professioneel | **Studenten-/lerarenprogramma met korting** — interessant voor een schoolproject. |
| **Multi-CB** | DE | ± € 25-40 | week | Redelijk makkelijk | Duitse kwaliteit. |
| **BETA LAYOUT / LeitOn** | DE | ± € 30-50 | week | Redelijk makkelijk | Professionele Duitse fabrikanten. |

> [!note] Btw en invoer
> Binnen de EU zit btw in de prijs en is er geen douane-afhandeling. Bij China (JLCPCB/PCBWay)
> komt btw + eventuele inklaringskosten bovenop; het eindbedrag kan met de verzendkeuze sterk
> variëren (DHL snel/duur vs. traag/goedkoop).

## Advies

> [!success] Gekozen: AISLER (`2026-10-06`)
> De gebruiker koos **AISLER**. De andere fabrikanten hieronder blijven **gekend en bewaard**,
> maar worden niet gebruikt. Productie- en onderdelenkost staan in [[bestelschema-pcb]].

- **Goedkoopst en toch simpel, leverdtijd minder belangrijk:** **JLCPCB** (buiten EU). Bord zelf bijna niets; de verzending bepaalt de prijs. Voor 2 lagen ruim voldoende. _(niet gekozen)_
- **Binnen Europa, zonder invoergedoe en snel:** **AISLER** (makkelijkst: KiCad/ODB++ direct, vaste prijs per cm², gratis verzending). **Gekozen.**
- **Binnen Europa, professionaliteit of studentenkorting:** **Eurocircuits** — bekijk het studenten-/lerarenprogramma. _(niet gekozen)_
- **Eindproduct op termijn (castellated, 4 lagen):** dezelfde fabrikanten, maar dan met ENIG; JLCPCB/PCBWay zijn dan het goedkoopst, AISLER/Eurocircuits het meest "EU". _(toekomst)_

Kort: **JLCPCB voor de prijs, AISLER voor het gemak binnen Europa.** Voor dit schoolproject is een
2-laags bord bij beide volledig toereikend.

## Gerelateerd

- [[pcb-ontwerp]] - werkwijze, Gerber-export
- [[pcb-methodes-kosten]] - socketkeuze en bordcomplexiteit
- [[bestellijst]] - aankoop van modules en onderdelen
- [[open-vragen]] - definitieve fabrikantkeuze
