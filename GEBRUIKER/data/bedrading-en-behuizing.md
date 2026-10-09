---
tags: [gstem, data, hardware, bedrading, behuizing]
aangemaakt: 2026-10-09
status: ontwerpkeuze vastgelegd; montage-details open
---

# Bedrading en 3D-geprinte behuizing

## Huidige ontwerpkeuze — 2026-10-09

De breakoutmodules worden niet meer via een eigen draagprint en sockets met elkaar verbonden. De gebruiker verbindt de onderdelen zelf met draden en soldeert de verbindingen. Daarna wordt een behuizing 3D-geprint waaraan de onderdelen gemonteerd worden.

- De aparte draagprint/carrier-PCB vervalt.
- Alle socket-headers vervallen.
- De bestaande breakoutmodules blijven de gekozen componenten; dit besluit slaat op de extra draagprint en de socketverbindingen, niet op de printjes waarop de breakoutmodules zelf gemonteerd zijn.
- De manier waarop de draden, losse componenten en breakoutmodules mechanisch in de behuizing vastzitten, is nog niet bepaald.
- Er wordt nog niets nieuws online opgezocht of aan de bestellijst toegevoegd totdat de gebruiker de montage- en bedradingsvragen hieronder heeft beantwoord.

> [!question] Nog te bepalen
> - Hoe worden de breakoutmodules en losse componenten in de behuizing bevestigd (bijvoorbeeld bestaande montagegaten, klemmen of een andere methode)?
> - Worden de gekozen discrete voedingsonderdelen (PTC, TVS en LDO) behouden en rechtstreeks bedraad, of wordt hun fysieke uitvoering aangepast?
> - Blijven de vierpolige schroefklem en de PCB-barreljack nodig, of worden voeding en UART rechtstreeks bedraad / op een andere manier door de behuizing gevoerd?
> - Is de bestaande Dupont-/siliconendraad geschikt en voldoende voor alle interne verbindingen? De gebruiker heeft draad en soldeergereedschap al.
> - Is er printmateriaal beschikbaar voor de behuizing, of moet dat later op de bestellijst?
> - Is montagehardware nodig? De bestaande M3-set was bedoeld voor de draagprint en wordt voorlopig niet als bestelling meegerekend.

## Bestellijstgevolgen

| Post | Huidige behandeling |
|---|---|
| Draagprint bij AISLER | Vervallen; geen PCB bestellen |
| Socket-headers | Vervallen; niet bestellen |
| M3-set voor draagprint | Niet meer als actieve bestelling; behuizingsbevestiging nog bepalen |
| PCB-barreljack | Vervallen als PCB-onderdeel; voedingsinvoer via behuizing nog bepalen |
| Vierpolige schroefklem | Nog bepalen; mogelijk overbodig bij rechtstreeks bedraden |
| Bestaande sensoren, rekenkern, LoRa en GNSS-breakouts | Blijven in de componentenlijst |
| Bescherming, LDO, ontkoppeling, level shifter en LED | Functie blijft voorlopig behouden; fysieke bedrading/montage moet worden uitgewerkt |

Zie [bestellijst](bestellijst.md), [componenten](componenten.md), [specificaties](specificaties.md), [open-vragen](open-vragen.md) en [beslissingen](beslissingen.md). De vroegere PCB-schets en AISLER-raming zijn alleen nog historische referenties: [pcb-schets](pcb-schets.md), [bestelschema-pcb](bestelschema-pcb.md) en [pcb-ontwerp](pcb-ontwerp.md).
