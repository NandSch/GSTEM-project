---
tags: [gstem, data, specificaties, gebruikersspecificaties, meettoestel]
aangemaakt: 2026-10-06
status: afgewerkt
---

# GStem-Specificaties (afgewerkt)

> [!info] Bron
> Door de gebruiker aangeleverde, **afgewerkte** specificaties.
> Bestand: `documenten/specificaties/GStem-Specificaties.md` (aangeleverd `2026-10-06`, herkomst `~/Downloads/GStem-Specificaties.md`).
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

### Scherm 3 — Code
- Via de knop **Code** kom je op het **codeerscherm** met twee secties:
  - **Code Editor (grootste venster):** hier schrijf je zelf code. Die code stuurt
    **sturingsinstructies** terug naar het meettoestel, dat ze kan doorgeven aan de
    **besturingscontrole van het voertuig**.
  - **Rechtervensters:** uitleg en **variabelen** van de meetwaarden, om het programma op te bouwen.
- Je haalt met de variabelen alle live data op om ermee verder te werken.
- Er staat korte uitleg over hoe waarden naar de controller worden verstuurd: alles via
  **CSV (comma separated values)**. Je bepaalt zelf welke waarde wat doet, zowel in het programma als
  in de besturing van het toestel.
- Je kunt zelf variabelen aanmaken om ruwe waarden een duidelijke naam te geven.
- Daaronder staat de knop om je programma te **uploaden en op te starten**.

### Scherm 4 — API
- Via de knop **API** (Application Programming Interface) kom je op de pagina waar je de API **aan en
  uit** kunt zetten.
- De API zorgt ervoor dat een gebruiker **alle metingen kan doorgeven naar een extern programma**. Dat
  externe programma kan de waarden op zijn eigen manier gebruiken en **instructies terugsturen** op
  dezelfde manier als bij het codeerscherm.
- **Linkervenster:** uitgebreide uitleg over het gebruik van de API.
- **Rechtervenster:** de **status** van de API plus **twee knoppen**:
  - API aan/uitzetten.
  - Verbinding met de API testen.
- Onder de knoppen staat het **precieze adres** waarnaar je je moet richten om data op te halen en te
  versturen.

## RC-vliegtuig (mock-up)

> [!info] Dit is een **zittend voorbeeld** van hoe het apparaat kan worden gebruikt, geen volledig
> functioneel vliegtuig.

### Installatie
- Het vliegtuigje wordt bestuurd door een **Arduino** die **CSV-waarden** aanneemt van een ander
  apparaat.
- De Arduino is met het meettoestel verbonden op zijn **TX- en RX-connectiepunten**.
- Richt het meettoestel zo dat de **voorkant van het toestel overeenkomt met die van het
  vliegtuigje**.

### Aanzetten
- Zodra het vliegtuigje aan voeding wordt gekoppeld, **start het meettoestel ermee op** (te zien aan
  de voedings-LED).
- Steek de USB-ontvanger in; de applicatie start automatisch op zodra je verbonden bent.
- Beweeg je het vliegtuigje, dan volgen de live waarden **accuraat** mee.

### Besturing
- Via de **code** of de **ingestelde API** bepaal je hoe de **besturingsvlakken** reageren op de
  metingen: **rolroeren**, **hoogteroer** en **richtingsroer**.
- De Arduino leest de ontvangen **CSV-instructies** uit en stelt de **servo's** in. Zo reageert het
  vliegtuigje in **real-time** op de sturing vanuit het programma.

### Testen en validatie
- **Kalibratie:** kantel het vliegtuigje handmatig naar voren, achteren en opzij en controleer of de
  3D-visualisatie en de live data in het kaartscherm **identiek** veranderen.
- **Feedbacklus testen:** upload een eenvoudige testcode in het codeerscherm die een stuursignaal
  terugstuurt naar het vliegtuigje en controleer of de Arduino de bijbehorende actie uitvoert.

## Relatie tot de andere bestanden

- Technische uitwerking en denkwijze: [meetmodule-voorbereiding](meetmodule-voorbereiding.md), [app-architectuur-besturing](app-architectuur-besturing.md),
  [besturing-en-commandos](besturing-en-commandos.md).
- Vastlegging per specificatie en beslissing: [specificaties](specificaties.md), [beslissingen](beslissingen.md).
- Gebruikersvertaling van deze tekst: [handleiding](handleiding.md).
- Openstaande punten: [open-vragen](open-vragen.md).
