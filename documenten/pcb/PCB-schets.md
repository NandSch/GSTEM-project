# PCB-schets — draagprint van het meettoestel

> [!info] Wat dit is
> Een **visuele schets** van hoe de zelfgemaakte draagprint eruitziet en hoe alles
> aangesloten is. Schematisch, niet op schaal. Bron: [[specificaties]] (`2026-10-06`),
> `documenten/specificaties/Ontwerp-meetmodule.md`.

## 1. Bovenaanzicht van de draagprint

![Bovenaanzicht draagprint](PCB-schets-draagprint.png)

> [!info] Eindbeeld met de Arduino (`2026-10-06`)
> Gedetailleerder beeld van de **eindtoestand**: de draagprint met de definitief gekozen
> breakouts, de losse componenten, de **Arduino Uno** en alle verbindingen.
>
> ![Eindbeeld eind-PCB met Arduino](PCB-eindbeeld.png)

> [!tip] Bestanden
> `documenten/pcb/PCB-schets-draagprint.svg` (vector, scherp te vergroten), `documenten/pcb/PCB-schets-draagprint.png` (afbeelding) en dit markdown-bestand.

> [!note] Leeswijzer kleuren
> - **rood** = VBAT (ruwe accuspanning)
> - **oranje** = 5 V (na de buck-converter)
> - **geel** = 3,3 V (na de LDO)
> - **blauw** = I2C-bus (IMU + barometer)
> - **groen** = UART (GNSS + uitbreidingsconnector)
> - **paars** = LoRa-aansturing (SPI/control)
> - **stippellijn roze** = antenne-keep-out

## 2. Verbindingsschema (wie praat met wie)

```mermaid
flowchart TB
    subgraph DRAG["Draagprint (carrier)"]
        PWR["Voeding (op de print)<br/>accu / barrel -> bescherming (PTC + P-MOSFET + TVS)<br/>-> buck 5 V -> LDO 3,3 V<br/>power-LED"]
        ESP["ESP32-S3 breakout<br/>leest sensoren, sensorfusie, LoRa"]
        LORA["LoRa-radio<br/>868 MHz"]
        IMU["9-DoF IMU<br/>I2C"]
        BARO["Barometer<br/>I2C"]
        GNSS["RTK-GNSS<br/>UART"]
        EXT["Uitbreidingsconnector<br/>UART TX/RX + 5 V + 3,3 V + GND"]
    end

    PWR -- "5 V / 3,3 V / GND" --> ESP
    PWR -- "5 V / 3,3 V" --> LORA
    PWR -- "3,3 V" --> IMU
    PWR -- "3,3 V" --> BARO
    PWR -- "3,3 V" --> GNSS
    PWR -- "5 V / 3,3 V / GND" --> EXT

    ESP <-- "SPI + control" --> LORA
    ESP <-- "I2C (SDA/SCL + pull-ups)" --> IMU
    ESP <-- "I2C (SDA/SCL + pull-ups)" --> BARO
    GNSS -- "UART (positie)" --> ESP
    ESP -- "UART (CSV-commando's)" --> EXT

    EXT --> CTRL["Arduino / voertuigcontroller<br/>stelt servo's in"]
    LORA -. "LoRa (draadloos)" .-> ADAPTER["LoRa-adapter<br/>USB naar laptop"]
```

## 3. Voedingsboom

```mermaid
flowchart LR
    BAT["Accu 7,4 V of barrel"] --> PROT["Voedingsbescherming (op de print):<br/>2 A PTC-zekering + P-MOSFET ompoolbeveiliging (DMG2301L)<br/>+ TVS SMBJ10A"]
    PROT --> BUCK["Buck-converter -> 5 V (losse module)"]
    BUCK --> LED["power-LED + serieweerstand"]
    BUCK --> LDO["LDO -> 3,3 V"]
    BUCK --> V5["5 V-rail<br/>breakouts met eigen regelaar + uitbreidingsconnector"]
    LDO --> V33["3,3 V-rail<br/>logica, IMU, barometer, GNSS"]
```

## 4. Fysieke opbouw in het kort

| Zone | Wat | Waarom daar |
| --- | --- | --- |
| Linksboven | Voedingssectie **op de print**: 2 A PTC-zekering, P-MOSFET ompoolbeveiliging (DMG2301L), TVS SMBJ10A, LDO AP2112K-3.3, bulk-elco + power-LED | kort bij de connector, weg van de gevoelige sensoren |
| Midden | ESP32-S3 breakout op socket-headers | centraal knooppunt van alle sporen |
| Rechtsboven | LoRa-radio + antenne-keep-out | antenne vrij, ver van IMU/barometer |
| Midden-onder | IMU en barometer | bij elkaar op de I2C-bus, weg van warmte en antenne |
| Rechtsonder | RTK-GNSS + antenne | vrij zicht naar boven, keep-out rond de antenne |
| Linksonder | Uitbreidingsconnector | UART + voeding naar de Arduino/controller |
| Hoeken | 4× M3-bevestigingsgat | montage op afstandsbussen in de dempende behuizing |

## 5. Nog te bepalen

- Exacte afmetingen en laagopbouw van de print (voorlopig 2-laags).
- Welke breakout-modellen en dus welke pinouts/footprints.
- Of de uitbreidingsconnector volledig 3,3 V is, of dat er een level shifter nodig is.
- **Behuizing van de voedingsonderdelen:** SMD (AP2112K = SOT-23-5, DMG2301L = SOT-23, SMBJ10A = DO-214AA) of through-hole-equivalenten (AMS1117-3.3, P6KE10A, radiale PTC) — kiezen i.f.v. handmatig solderen.

Zie [[open-vragen]] en [[specificaties]].
