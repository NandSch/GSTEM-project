
## AI · 18:26

Klaar — de GPS/RTK gaat van Eckstein.

## Gewijzigd

**Bestellijst (`data/bestellijst.md`)**
- RTK-regel: tag `botland` → `eckstein`, prijs **€ 70,50 → € 71,39**, link → `eckstein-shop.de/lc29h-dual-band-gps-module-raspberry-pi_1`, met vermelding art. **WS25279** / EAN 4060137304156.
- Winkelvergelijking in de callout: **Eckstein (DE) = gekozen**, Botland/Kamami/HESTORE blijven als alternatief.
- Totalen: **onderdelen € 185,05** (was 184,16) · **incl. AISLER-print € 217,81** (was 216,92).
- Open actie "GPS-winkel kiezen" → **afgevinkt**.

**Excel (`documenten/Bestellijst-GSTEM.xlsx`)**
- `build-bestellijst.py` aangepast: nieuwe status **`eckstein`** (kleur + legende), rij bijgewerkt, SUMIF-totaalrij "Eckstein (DE, EU)", titel/footnote/legende mee.
- Herborend. Controle: Eckstein **71,39** · onderdelen **185,05** · incl. AISLER **217,81** ✔
- Blad **Bestelbaarheid**: Eckstein = *gekozen*, Botland/Kamami als alternatief erbij.

**Archief**
- `beslissingen.md` — nieuwe beslissing *"GPS/RTK-module gekocht bij Eckstein (DE), niet Botland"* met reden + gevolgen.
- `gps-rtk-prijzen.md` — status → *gekozen — Eckstein*, tabel + conclusie aangepast.
- `links.md` — Eckstein als **gekozen** winkel opgenomen (winkeltabel + onderdelenlijst), Botland naar alternatief.
- `open-vragen.md` — GPS-winkelvraag afgevinkt en bijgewerkt.

> [!note] Klein detail
> Eckstein is € 0,89 duurder dan Botland en ± € 8 duurder dan Kamami, maar je koos Eckstein (DE, EU, prijs in EUR). Het blijft dezelfde breakout/HAT met meegeleverde dual-band antenne.

Wil je dat ik meteen ook de **P-MOSFET op AO3401A** vastleg? Dat staat nog open.

---

## Gebruiker · 18:32

> [!quote] Verbatim
> neen

## AI · 18:32

Oké, de P-MOSFET-keuze (DMG2301L vs AO3401A) blijft open in [[open-vragen]] en op de bestellijst — daar verandert niets. Verder is alles bijgewerkt zoals hierboven.

---

## Gebruiker · 18:32

> [!quote] Verbatim
> Zet Pmosfetkeuze dat we dat niet doen.

## AI · 18:35

Vastgelegd: **geen P-MOSFET-ompoolbeveiliging**.

## Beslissing
De kandidaten **DMG2301L** en **AO3401A** komen **niet** op de print of de bestellijst. Omgekeerd aansluiten wordt **fysiek** voorkomen met een **gepolariseerde connector** (XT60/JST-XH). De **PTC-zekering** en de **TVS SMBJ10A** blijven wél.

## Bestellijst + Excel
- Beschermingsregel: `2 A PTC + P-MOSFET + TVS` → **`2 A PTC + TVS (zonder P-MOSFET)`**, **€ 1,30 → € 1,00**.
- Nieuwe regel met status **`niet nodig`**: *Ompoolbeveiliging (P-MOSFET)* — telt niet mee in de totalen.
- Mouser/DigiKey: **€ 1,30 → € 1,00**.

| | oud | nieuw |
| --- | --- | --- |
| Onderdelen | € 185,05 | **€ 184,75** |
| Incl. AISLER-print | € 217,81 | **€ 217,51** |

`documenten/Bestellijst-GSTEM.xlsx` is herbouwd (status `eckstein` + `niet nodig`, bijgewerkte legende en het blad Bestelbaarheid waar de P-MOSFET nu als *niet gebruikt* staat). Bestelschema-PCB in de Excel: subtotaal 3a **€ 14,88**, totaal **€ 57,65**, nieuw te bestellen **€ 47,64**.

## Archief
- `beslissingen.md` — nieuwe beslissing *"Geen P-MOSFET-ompoolbeveiliging"* (reden, gevolg, totalen).
- `afgevoerd.md` — **DMG2301L / AO3401A** als afgevoerde optie.
- `open-vragen.md` — P-MOSFET-vraag **afgevinkt**; de vragenlijsten "welke bescherming" en "wat op de print" bijgewerkt naar PTC + TVS.
- `componenten.md`, `specificaties.md`, `bestelschema-pcb.md`, `bestelbaarheid.md`, `links.md`, `pcb-schets.md`, `actieplan.md` — alle P-MOSFET-vermeldingen omgezet naar "vervalt".

> [!note] Twee kanttekeningen
> - De **€ 1,00** voor PTC + TVS is een **schatting** (was € 1,30 voor PTC + MOSFET + TVS); de exacte PTC bij Mouser/DigiKey komt rond € 1,09, de TVS ± € 0,50 bij TME — dus reken eerder op **± € 1,50** als je beide exact bestelt.
> - De **TVS is nog niet expliciet door jou bevestigd**; ik heb hem laten staan. Zeg het als die ook weg moet.

---
