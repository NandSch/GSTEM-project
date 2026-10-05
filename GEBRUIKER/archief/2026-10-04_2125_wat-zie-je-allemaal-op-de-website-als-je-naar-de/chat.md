---
tags: [gstem, chatlog]
sessie: "01a10860-d617-71e0-9c07-2f3ef80d5bc3"
gestart: 2026-10-04T19:25:26.659Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a10860-d617-71e0-9c07-2f3ef80d5bc3` · gestart 2026-10-04_2125
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 21:25

> [!quote] Verbatim
> Wat zie je allemaal op de website als je naar de pagina code gaat.

## AI · 21:25

Ik kijk eerst naar de projectstructuur en de skill.

---

## AI · 21:26

Dit staat op de **Code-pagina** (`#page-code` in `GSTEMAPPPREVIEWWEB/index.html`, de officiële versie B uit de A/B-test):

**Bovenaan (vaste navigatie)**
- Statusvakjes `USB` en `Device` (uitgeschakeld, automatisch gezet)
- Navigatielinks: Kaart · Code · API

**Codevenster** (één kolom, gecentreerd, max. 1060 px)
- Titelbalk met de drie vensterbolletjes (rood/oranje/groen), bestandsnaam `missie.ino`, label `Arduino C++`
- Rechts in die balk: hint `Ctrl` + `Enter` en de knop **Uploaden** (staat uit tot er verbinding is)
- Grote teksteditor (`#code-editor`, tekstvak) met placeholder *"Typ hier uw Arduino-code..."*
- Statusbalk onderaan: aantal regels en aantal tekens

**Uitklapbare hulp eronder** (standaard dicht)
1. **Wat kan ik gebruiken?** — lijst van 8 live waarden met eenheid:
   - `meting.hoogte` (m), `meting.snelheid` (km/u), `meting.horizontaleSnelheid` (m/s), `meting.verticaleSnelheid` (m/s, + omhoog), `meting.richting` (graden), `meting.verticaleHoek` (graden), `meting.breedtegraad` (graden), `meting.lengtegraad` (graden)
2. **Hoe stuur ik iets?** — voorbeeldregel `Serial.println("15,-5,75,60");` plus de noot *"Eén regel per keer, altijd afsluiten met een newline."*

**Extra:** bij een gewone start verschijnt eerst de Setup-popup ("Verbinding maken met de hardware…"), tenzij je laadt met `?embed=1`.

De startcode in de editor is minimaal (11 regels). Geen nieuwe beslissing of bron opgedoken — er is dus niets gewijzigd in `GEBRUIKER/`; de beschrijving staat al in [[ab-test-code-pagina]] en [[specificaties]].

---

## Gebruiker · 21:27

> [!quote] Verbatim
> vertel waarvoor het dient en wat de functies zijn van elk deel. in de vorm van een  handleiding waarop alles staat wat wat doet

## AI · 21:28

Ik maak er een volwaardige handleiding van in de hub.

---

## AI · 21:28

Hier is de handleiding van de **Code-pagina**. Volledige versie opgeslagen in `GEBRUIKER/data/code-pagina.md`.

## Wat de pagina is
Eén codevenster waarin de leerling zelf een klein Arduino-programma schrijft. De meetmodule voert dat uit en print zelf de stuurregel die naar de voertuigcontroller gaat. Alles zit in `GSTEMAPPPREVIEWWEB/index.html` -> `#page-code`.

## De onderdelen, stuk voor stuk

**1. Navigatiebalk** — links Kaart · Code · API, om van scherm te wisselen. Rechts twee statusvakjes `USB` en `Device` (uitgeschakeld, automatisch gezet) die tonen of de USB-ontvanger en het meettoestel verbonden zijn.

**2. Setup-popup** — verschijnt bij het opstarten met dezelfde twee statusvakjes en een knop **OK**. Bevestigt zodra de hardware klaar is. Laad je met `?embed=1`, dan blijft de popup weg.

**3. Codevenster** (één kolom, gecentreerd):
- **Titelbalk** — de drie vensterbolletjes (decoratief), bestandsnaam `missie.ino`, taal `Arduino C++`, en de hint `Ctrl` + `Enter`.
- **Knop Uploaden** (`#upload-btn`) — stuurt de code naar de module. Staat uit zolang de editor leeg is. Klik of `Ctrl` + `Enter` roept `uploadCode()` aan; in de demo volgt de melding dat jouw code zelf de CSV-regels print en de module die ongewijzigd doorstuurt.
- **Editor** (`#code-editor`) — groot tekstvak, spellingcontrole uit, met 11 regels **startcode**: een `void loop()` die `meting.hoogte` vergelijkt met 125.0 en dan `"15,-5,75,60"` of `"0,0,50,50"` print, gevolgd door `delay(100)`.
- **Statusbalk** — telt live het aantal **regels** en **tekens** (`updateCodeStats()`).

**4. Uitklapbare hulp** (standaard dicht):
- **Wat kan ik gebruiken?** — de 8 live waarden met eenheid: `meting.hoogte` (m), `meting.snelheid` (km/u), `meting.horizontaleSnelheid` (m/s), `meting.verticaleSnelheid` (m/s, + omhoog), `meting.richting` (°), `meting.verticaleHoek` (°), `meting.breedtegraad` (°), `meting.lengtegraad` (°).
- **Hoe stuur ik iets?** — voorbeeld `Serial.println("15,-5,75,60");`, uitleg dat jij kiest wat elk cijfer betekent, en de noot: één regel per keer, altijd met newline.

## Onderliggende functies
- `setActive()` — leest de `#hash` en zet het juiste scherm + de nav-knop op actief.
- `updateCodeStats()` — regels/tekens tellen, Uploaden aan/uit.
- `keydown`-luisteraar — vangt `Ctrl`/`Cmd` + `Enter` op.
- `uploadCode()` — leeg vak geeft "Voer eerst code in.", anders de demo-bevestiging.
- `closePopup()` — sluit de setup-popup.

> [!info] Opgeslagen: handleiding → `GEBRUIKER/data/code-pagina.md`, en het onderwerp is gekoppeld in `GEBRUIKER/onderwerpen.md`.

---
