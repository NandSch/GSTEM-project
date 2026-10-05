# 05 · Blokschema AeroLink

Bestand: `CODEXIMPORT/Blokschema_AeroLink.drawio` (diagrams.net / draw.io, type `device`,
aangemaakt door "Codex", v24.7.17).

De diagram-ID is `aerolink-blockschema`, naam **"Blokschema AeroLink"**.

## Titel

> Draadloze 3D-positie- en oriëntatiemodule met LoRa en servo-aangestuurde vliegtuigmock-up
> Blokschema — meten, draadloos verzenden, verwerken en testen

## Nodes en labels (letterlijk uit het diagram)

**Sensoren aan boord**
- GPS-RTK-module — *positie*
- Barometer — *hoogte*
- Versnellingsmeter — *versnelling en schokken*
- Gyroscoop — *draaiing / kanteling*
- Magnetometer / kompas — *richting*

**Behuizing en verwerking**
- 3D-geprinte behuizing met trillingsdemping
- Microcontroller / PCB — *sensordata verwerken*
- LoRa-zender

**Ontvangst en verwerking**
- LoRa-ontvanger
- Laptop / grondstation — *dataopslag en 3D-weergave*
- Berekenprogramma — *eenvoudige stuurcorrectie*

**Aansturing / mock-up**
- Tweede microcontroller
- Servo rolroer
- Servo hoogteroer
- Stilstaande vliegtuig-mock-up

**Verbindingslabels (pijlen)**
- sensordata
- meetdata
- draadloos via LoRa
- telemetrie
- dataanalyse
- testcorrecties
- rol
- hoogte
- aansturing (×2)

## Interpretatie van de keten

```text
[GPS-RTK] [Barometer] [Versnellingsmeter] [Gyroscoop] [Magnetometer/kompas]
        └────────────── sensordata ──────────────┘
                          ↓
        Microcontroller / PCB  (in 3D-geprinte behuizing met demping)
                          ↓  meetdata
                     LoRa-zender
                          ↓  draadloos via LoRa
                    LoRa-ontvanger
                          ↓  telemetrie
        Laptop / grondstation  (dataopslag en 3D-weergave)
                          ↓  dataanalyse
                   Berekenprogramma (eenvoudige stuurcorrectie)
                          ↓  testcorrecties / aansturing
                   Tweede microcontroller
                    ┌─────┴─────┐
              Servo rolroer  Servo hoogteroer   (rol / hoogte)
                    └─────┬─────┘
            Stilstaande vliegtuig-mock-up
```

## Relatie met de andere documenten

- Dit schema komt inhoudelijk overeen met het blokschema in
  `CODEXIMPORT/GSN-project_draadloze_3D-meetmodule.docx` en de ketenbeschrijving in
  `CODEXIMPORT/PROJECT_CONTEXT.md` (zie `01-projectoverzicht.md`).
- In het schema zijn de sensoren nog als **losse componenten** opgenomen (versnellingsmeter,
  gyroscoop, magnetometer), terwijl de specifi caties spreken van een geïntegreerde **9-DoF IMU met
  sensorfusie**. Ook wordt de **tweede ESP als USB-adapter bij de laptop** hier impliciet als
  "LoRa-ontvanger" aangeduid.

## Details

- Het bestand is XML (`<mxfile>` → `<diagram>` → `<mxGraphModel>`), direct te openen op
  https://app.diagrams.net of met de draw.io-VS Code-extensie.
- De exacte geometrie (posities, verbindingslijnen) zit in de `mxGraphModel`-laag; de bovenstaande
  labels komen uit de `value="..."`-attributen van de cellen.
