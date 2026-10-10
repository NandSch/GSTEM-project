---
tags: [gstem, data, specificaties, gebruikersspecificaties, meettoestel]
aangemaakt: 2026-10-06
status: afgewerkt
---

# GStem-Specificaties (afgewerkt)

> [!info] Bron
> Door de gebruiker aangeleverde, **afgewerkte** specificaties.
> Bestand: `documenten/specificaties/GStem-Specificaties.md` (aangeleverd `2026-10-06`, herzien `2026-10-10`; de pdf-versie `~/Downloads/GStem-Specificaties.pdf` is de huidige versie).
> Dit is de formele, gebruikersgerichte specificatie van het product; [meetmodule-voorbereiding](meetmodule-voorbereiding.md) en
> [specificaties](specificaties.md) bevatten de technische achtergrond en denkwijze.

## Doel en meetprestaties

Een **klein meettoestel** dat je op een bewegend voertuig of apparaat plaatst (vliegtuig, bootje,
autootje). Het meet tijdens het bewegen **vier grootheden**:

| Grootheid | Omschrijving | Nauwkeurigheid / eenheid |
| --- | --- | --- |
| **Richting** | Hoe schuin of recht het toestel staat | graden, horizontaal en verticaal vlak |
| **Snelheid** | Hoe snel het beweegt | km/u |
| **Hoogte** | Hoe hoog het zich bevindt | nauwkeurig tot op **1,5 meter** |
| **Locatie** | Waar het precies is | nauwkeurig tot op **0,5 meter** |

Bij het toestel hoort een **kleine draadloze ontvanger** die eruitziet als een **USB-stick**. Die
steek je in de laptop. Het **bereik** tussen toestel en ontvanger is **maximaal 4 kilometer**.

## Aanzetten van toestel en laptop

- Zodra het voertuig of toestel waarop het meettoestel is gemonteerd **wordt ingeschakeld**, gaat het
  meettoestel **automatisch aan**. Een **LED-lampje** toont dat het toestel actief is.
- Wanneer je de **USB-ontvanger** in de laptop steekt, **start het bijbehorende programma vanzelf op**.

## Applicatie (laptop)

Het programma controleert eerst de verbindingen voordat je verder kunt. Je ziet op **elk scherm** de
actuele status van zowel de **USB-ontvanger** als het **meettoestel**.

### Scherm 1 — verbindingscontrole
- Controleert de verbindingen; de gebruiker klikt op **OK** om door te gaan naar het volgende scherm.

### Scherm 2 — kaart en live data
Alle live data worden op **twee manieren** getoond:
1. **3D-kaart met satellietfotografie van Google** — toont welke weg het toestel heeft afgelegd en in
   welke richting het op dat moment kijkt.
2. **Tabel** — alle afzonderlijke meetgegevens overzichtelijk in cijferwaarden.

### Scherm 3 — Besturing (menu)
- Via de knop **Besturing** kom je op een pagina met **drie applicatie-iconen**, eentje per
  voertuigtype. Elk icoon opent de bijbehorende besturingspagina.
- Elke besturings-app heeft **eigen, voertuigspecifieke bedieningselementen**.

### Scherm 4 — Besturing (auto)
- Bijvoorbeeld het **auto-icoon**: een pagina met een **stuur** (klikken en slepen) en een
  **gaspedaal** (ingedrukt houden = vooruit rijden).
- Het voorbeeld in de specificatie is een **autootje**; het oude RC-vliegtuig-mock-upverhaal
  (rolroeren/hoogteroer/richtingsroer, servo's via de Arduino) vervalt hiermee als voorbeeld.

## Voertuig (demonstratiemodel)

> [!info] Het voertuig hoeft **geen volledig functioneel voertuig** te zijn; het mag een
> **demonstratiemodel** zijn dat toont hoe het apparaat gebruikt kan worden. Het eerdere
> RC-vliegtuig-mock-upverhaal is vervangen door een generiek voertuigverhaal met de auto als
> concreet voorbeeld.

### Installatie
- De gebruiker verbindt enkel de **Arduino die het voertuig aanstuurt** met het meettoestel:
  data-overdracht en een **gemeenschappelijke ground**.
- Het meettoestel heeft daarvoor **drie connectiepunten: TX, RX en GND**.

### Aanzetten
- Zodra het voertuig op voeding wordt aangesloten, **start het meettoestel automatisch mee op**
  (te zien aan de voedings-LED).
- Steek de USB-ontvanger in en start de applicatie; beweeg je het voertuig, dan volgen de live
  waarden **accuraat** mee.

### Besturing
- Het voertuig wordt bestuurd via een van de **besturing-applicaties** op de pagina Besturing
  (scherm 3/4); de meest geschikte of bijbehorende app stuurt het voertuig.

### Testen
- **Beweeg of kantel het voertuig handmatig** en controleer of de **3D-visualisatie** en de
  **live data synchroon** meeveranderen. De aparte feedbacklus-test via het codeerscherm vervalt
  (die pagina bestaat niet meer).

## Relatie tot de andere bestanden

- Technische uitwerking en denkwijze: [meetmodule-voorbereiding](meetmodule-voorbereiding.md), [app-architectuur-besturing](app-architectuur-besturing.md),
  [besturing-en-commandos](besturing-en-commandos.md).
- Vastlegging per specificatie en beslissing: [specificaties](specificaties.md), [beslissingen](beslissingen.md).
- Openstaande punten: [open-vragen](open-vragen.md).
