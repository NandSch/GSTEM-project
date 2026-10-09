---
tags: [gstem, data, pcb, hardware, ontwerp]
aangemaakt: 2026-10-06
status: historisch; draagprintontwerp vervallen
---

# Oud plan: PCB ontwerpen

> [!warning] Vervangen op 2026-10-09
> De gebruiker heeft gekozen voor zelf bedraden en solderen en de onderdelen aan een 3D-geprinte behuizing monteren. De eigen draagprint, PCB-footprints en sockets zijn niet meer nodig. Deze pagina bewaart de oude ontwerpwerkwijze als naslag; voer de PCB-stappen hieronder niet uit. Actuele aanpak: [bedrading-en-behuizing](bedrading-en-behuizing.md).

> [!info] Doel
> Praktische werkwijze om de draagprint te ontwerpen: welke app, hoe je de footprints van de
> breakout-modules vindt en hoe je alle gatmaten bepaalt. Hoort bij [specificaties](specificaties.md)
> (draagprint-aanpak), [pcb-schets](pcb-schets.md) en [pcb-methodes-kosten](pcb-methodes-kosten.md).

## 1. Welke app

| App | Platform | Kost | Waarom wel/niet |
| --- | --- | --- | --- |
| **KiCad 8/9** | Windows/mac/Linux | gratis, open source | **Voorkeur.** Grote ingebouwde footprint-bibliotheek, 2-laags zonder licentie, exporteert Gerbers voor elke fabrikant. |
| **EasyEDA** | browser | gratis | Alternatief als je toch bij **JLCPCB/LCSC** bestelt: onderdelen, footprint en bestelling hangen aan elkaar. Iets minder krachtig. |
| Fusion 360 Electronics (ex-EAGLE) | Windows | abonnement | Overkill en duur voor dit project. |
| Altium / OrCAD | Windows | duur | Professioneel, niet nodig. |
| LibrePCB | cross-platform | gratis | Simpel, maar kleinere bibliotheek. |

**Advies:** KiCad, en de bestelling bij JLCPCB of PCBWay.

## 2. Werkwijze in KiCad

1. **Schema:** elke module wordt een **connector** (een rij pinnen) met een eigen symbool. Verder
   losse onderdelen: buck, LDO, zekering, ompoolbeveiliging, LED + weerstand, decoupling.
2. **Footprints toewijzen:** pinnen op **2,54 mm-raster** met `Connector_PinSocket_2.54mm`
   (female, want de breakouts zijn op sockets geplaatst). Bevestigingsgaten met `MountingHole`.
3. **PCB-layout:** modules plaatsen, silkscreen-omtrek per module tekenen (zodat je oriëntatie en
   plaats ziet), ground plane op de onderlaag, rails `VBAT`/`5V`/`3V3`/`GND`.
4. **DRC** draaien, dan **Gerbers + drill files** exporteren (`File -> Fabrication Outputs`).
5. Bestellen: zip met Gerbers uploaden; de fabriek controleert met haar eigen DRC.

## 2b. Wat koopt de gebruiker zelf aan

Alle **breakout-modules** (ESP32-S3, LoRa, IMU, barometer, RTK-GNSS) en de losse onderdelen
worden **zelf aangekocht**. De **print** is het enige gemaakte stuk; daarop staan minstens de
**LED en de sockets** (en eventueel de voedingsonderdelen). Zie [beslissingen](beslissingen.md) `2026-10-06`.
Dus: de BOM splitsen in "zelf kopen" en "op de print"; de printstuklijst beperkt zich tot wat
rechtstreeks op het bord gesoldeerd wordt.

## 3. Afmetingen van gaten: waar vind je ze

Nooit zelf verzinnen. Drie bronnen, in deze volgorde:

1. **Datasheet / mechanische tekening** van de breakout (Adafruit, SparkFun, Waveshare, DFRobot):
   daar staan "board dimensions", pin pitch en mounting-hole diameter in. Zoek op de productpagina
   naar "dimensions", "mechanical drawing" of "downloads".
2. **Standaardmaten** (gelden altijd):
   - pinheader 2,54 mm: gat **1,0 mm**, pad **1,7-1,8 mm**;
   - pinheader 2,0 mm (JST-GH): gat **0,8 mm**;
   - M3-bevestiging: vrij gat **3,2 mm**;
   - M3 + inslagmoer (heat-set): **4,0-4,5 mm**;
   - M2,5: **2,7 mm**; M2: **2,2 mm**.
3. **Zelf nameten** met een digitale schuifmaat (schuifmaat EUR 15-25) op de module die je in huis
   hebt: pinpitch, rijafstand, bordafmetingen en gatdiameter.

## 4. Dat wat je per module moet weten

Voor elke breakout vul je in:

- aantal pinnen per rij en **rijafstand** (meestal 2,54 mm; grotere devkits 15,24 of 22,86 mm);
- **bordafmetingen** (voor de silkscreen-omtrek en de keep-out);
- **bevestigingsgaten** (diameter + positie vanaf de rand);
- **antenne-keep-out** (LoRa en GNSS).

> [!tip] Controle voor het bestellen
> Print de layout **1:1 op papier** en leg de echte modules erop. Klopt de positie van elk gat,
> dan is de footprint goed. Dit vangt de meeste fouten voordat je bestelt.

## 5. Aandachtspunten voor dit bord

- Ground plane op de onderlaag; aparte rails `VBAT`/`5V`/`3V3`/`GND`.
- Antenne-keep-out voor LoRa en GNSS (geen koper onder de antenne).
- Buck-spoel en ESP weg van IMU en barometer (warmte + storing).
- I2C kort houden; pull-ups niet dubbel plaatsen als een breakout ze al heeft.
- De **socket-keuze** (precisie/gefreesd vs. dual-wipe, zie [pcb-methodes-kosten](pcb-methodes-kosten.md)) bepaalt het
  landpatroon en de extra hoogte.
- 4 bevestigingsgaten (M3) in de hoeken.

## Gerelateerd

- [specificaties](specificaties.md) - draagprint-aanpak
- [pcb-schets](pcb-schets.md) - bovenaanzicht en verbindingsschema
- [pcb-methodes-kosten](pcb-methodes-kosten.md) - socketkeuze en kosten
- [open-vragen](open-vragen.md) - exacte breakouts, pinouts en fabrikant
