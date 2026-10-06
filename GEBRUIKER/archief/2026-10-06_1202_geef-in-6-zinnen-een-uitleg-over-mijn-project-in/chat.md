---
tags: [gstem, chatlog]
sessie: "01a110aa-427b-714d-859a-585dc364c718"
gestart: 2026-10-06T10:02:37.211Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a110aa-427b-714d-859a-585dc364c718` · gestart 2026-10-06_1202
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 12:02

> [!quote] Verbatim
> Geef in 6 zinnen een uitleg over mijn project inclusief het mockup vliegtuigje

## AI · 12:03

Je project is *"Positie- en beweging meettoestel met LoRa-integratie"*: een klein toestel dat je op een bewegend voertuig of apparaat monteert en dat tijdens het bewegen vier grootheden meet — richting (graden), snelheid (km/u), hoogte (nauwkeurig tot 1,5 m) en locatie (nauwkeurig tot 0,5 m). De meetwaarden gaan draadloos via LoRa naar een kleine USB-stick-ontvanger in je laptop, met een bereik tot 4 kilometer, waarna een laptopapp automatisch opstart zodra je de ontvanger insteekt. In die app zie je de live data op een 3D-satellietkaart van Google én in een cijfertabel, met op elk scherm de status van de ontvanger en het meettoestel. Op het codeerscherm schrijf je zelf code die sturingsinstructies als CSV-waarden terugstuurt, en via het API-scherm kan een extern programma dezelfde metingen ophalen en eigen instructies terugsturen. Het mockup-vliegtuigje is een zittend demonstratievoorbeeld: een Arduino aan boord neemt de CSV-waarden aan via de TX/RX-punten van het meettoestel, waarbij de voorkant van het toestel gelijk moet staan met die van het vliegtuigje. Op basis van die sturing zet de Arduino de servo's van de drie besturingsvlakken — rolroeren, hoogteroer en richtingsroer — real-time in beweging, waarna je met kalibratie- en feedbacklustests controleert of het vliegtuigje correct reageert.

> [!info] Opgeslagen: niets nieuw — dit was een samenvatting van bestaande inhoud (`GEBRUIKER/data/gstem-specificaties.md`, [[beslissingen]] en `README.md`). Er zijn geen nieuwe beslissingen, specificaties of open vragen opgedoken.

---
