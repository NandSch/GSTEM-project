---
tags: [gstem, data, pcb, hardware, schema]
aangemaakt: 2026-10-06
status: werklijst
---

# Verbindingsschema meetmodule (draw.io + PNG)

> [!info] Doel
> Eén overzichtelijk schema van de **hele meetmodule**: welke componenten met wat
> verbonden zijn en **hoe** (voeding, I2C, UART, RF, GND). Opvolger/aanscherping van de
> schets in [[pcb-schets]]. Bron: [[componenten]], [[bestelschema-pcb]], [[beslissingen]],
> `documenten/PCB-schets.md` en `documenten/Ontwerp-meetmodule.md`.

## Bestanden

| Rol | Pad |
| --- | --- |
| draw.io-bron (bewerkbaar) | `documenten/Verbindingsschema-GSTEM.drawio` |
| Afbeelding | `documenten/Verbindingsschema-GSTEM.png` (3120 x 2300) |
| Bouwsript | `documenten/build-verbindingsschema.py` |

Bouwen: `python documenten/build-verbindingsschema.py` (schrijft beide bestanden).
Het `.drawio` opent op https://app.diagrams.net of met de draw.io-VS Code-extensie.

## Wat staat erop

**Voedingsketen** (rood = VBAT, oranje = 5 V, geel = 3,3 V, grijs streeplijn = GND):

```text
Accu 2S LiPo 7,4 V (max 8,4 V)  \ 
Barrel-connector (adapter)       >-- PTC-zekering 2 A --+-- TVS SMBJ10A --> GND
                                  (Littelfuse 1812L200) |
                                                        v
                              buck-converter 7,4 V -> 5 V -- bulk-elco 100 uF/16 V
                                                        |
                                          5 V-rail -----+-- power-LED + 330 Ohm --> GND
                                                        |
                                           LDO AP2112K-3.3 (5 V -> 3,3 V) --> 3,3 V-rail
```

**Databussen:**

- **I2C (blauw):** XIAO <-> BNO085 (9-DoF IMU) en XIAO <-> BMP581 (barometer), 3,3 V,
  pull-ups zitten in de breakouts.
- **UART1 (groen):** XIAO <-> LC29H(DA) RTK-GNSS, 3,3 V.
- **UART2 (groen):** XIAO -> TXB0104 (3,3 V) -> J2 uitbreidingsconnector (5 V, TX/RX)
  -> Arduino Uno. Nodig omdat de Uno 5 V-logica gebruikt.
- **LoRa/RF (paars):** XIAO + Wio-SX1262 (SPI intern) -> IPEX/U.FL->SMA-pigtail ->
  LoRa-antenne; draadloos naar de LoRa-adapter (2e XIAO-kit) aan de laptop.
- **GNSS-RF (paars):** LC29H(DA) -> actieve dual-band L1/L5-antenne (SMA).

**Componenten die op de draagprint horen** (geel, streeplijn-omlijnd, als notities):

- ontkoppeling 100 nF + 10 uF per module + 100 uF bulk op de 5 V;
- sockets: dual-wipe (XIAO), precisie/turned-pin voor de vaste modules;
- I2C-pull-ups zitten al op de BNO085- en BMP581-breakouts (2 reserve-footprints).

**Interface en mock-up:**

- J2 uitbreidingsconnector (4-pins 3,5 mm schroefklem): **GND / +5 V / TX / RX**.
- Arduino Uno (5 V-logica) -> 3 servo's (rolroer, hoogteroer, richtingsroer),
  servo's op een **aparte buck-converter** (5 V BEC).
- LoRa-adapter (2e XIAO ESP32S3 + Wio-SX1262) aan de laptop via USB-A -> USB-C.

## Legende kleuren (gelijk aan [[pcb-schets]])

- **rood** = VBAT (ruwe accuspanning) · **oranje** = 5 V · **geel** = 3,3 V
- **blauw** = I2C · **groen** = UART · **paars** = LoRa / RF · **grijs streeplijn** = GND

## Let op

- Schematisch en **niet op schaal**; pijlen tonen de richting van voeding of data.
- De **pinout is nog een voorstel** (open AI-taak: pinout-tabel XIAO opstellen, zie
  [[open-vragen]] en [[componenten]]). De GNSS-module is hier als **3,3 V**-belasting
  getekend; breakout-modellen met eigen regelaar kunnen ook 5 V krijgen.

## Gerelateerd

- [[pcb-schets]] - bovenaanzicht en oude schets van de draagprint
- [[componenten]] - BOM en keuzes
- [[bestelschema-pcb]] - onderdelen op de print en productie
- [[beslissingen]] - de keuzes van `2026-10-06`
- [[links]] - bestandspaden en bronnen
