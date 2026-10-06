---
tags: [gstem, data, blender, 3d, mockup, hardware]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: verwijderd (2026-10-06); layout was een voorstel
---

# Blender-mock-up van de draagprint en opstelling

> [!info] Doel
> Een semi-accurate 3D-mock-up van het meettoestel in **Blender**: de draagprint met alle
> breakout-modules, de losse printonderdelen, de antennes/bekabeling, de **Arduino Uno** met
> servo's en de **LoRa-ontvanger**. Plus drie studio-renders. Hoort bij [[pcb-schets]],
> [[componenten]] en [[specificaties]].

> [!warning] Verwijderd op 2026-10-06
> De map `documenten/blender/` (model, scripts, renders en review-set) is verwijderd; de
> mock-up wordt niet verder gebruikt. Alles blijft herstelbaar uit git (commit `28e4fae`).
> Het geannoteerde overzichtsblad blijft staan als `documenten/pcb/review-mockup-controleblad.png`.
> Zie [[beslissingen]] en [[afgevoerd]].

> [!warning] De layout is een voorstel
> De KiCad-layout is nog niet gemaakt. De plaatsing van de modules op de print in dit model is
> dus een **plausibel voorstel**, geen productietekening. De bordrand en de gatmaten kloppen;
> de posities van de onderdelen zijn nog vrij te kiezen.

## Bestanden (verwijderd `2026-10-06`)

| Rol | Pad |
| --- | --- |
| Bouwsript (herhaalbaar) | `documenten/blender/build_gstem_mockup.py` *(verwijderd)* |
| Blender-bestand | `documenten/blender/gstem-mockup.blend` *(verwijderd)* |
| Render 1 — bovenaanzicht (orthografisch) | `documenten/blender/renders/01_bovenaanzicht.png` *(verwijderd)* |
| Render 2 — 3/4-perspectief (volledige opstelling) | `documenten/blender/renders/02_drie_kwart.png` *(verwijderd)* |
| Render 3 — detail voeding + XIAO-socket | `documenten/blender/renders/03_detail_voeding.png` *(verwijderd)* |
| Geannoteerd overzicht | `documenten/pcb/review-mockup-controleblad.png` *(bewaard)* |

Herbouwen (indien nodig): `git checkout 28e4fae -- documenten/blender` en voer in een live
Blender-sessie `exec(open(r".../documenten/blender/build_gstem_mockup.py").read())` uit. Het script wist zijn
eigen collecties en bouwt alles opnieuw; met `GSTEM_RENDER=1` rendert het ook de drie beelden.

## Opbouw van het model

Het sript werkt in **millimeters** en groepeert in collecties: `00_Studio`, `01_Board`,
`02_Modules`, `03_Components`, `04_Wiring`, `05_Mockup`.

**Draagprint:** 100 x 75 x 1,6 mm, afgeronde hoeken (r 3 mm), 4x M3-gat (3,2 mm) op 4 mm van de
rand, groen soldeermasker met FR4-zijkant, koperen onderlaag en witte silkscreen.

**Zones op de print (voorstel):**

| Zone | Wat | Waar |
| --- | --- | --- |
| Voeding | barrel jack, 2 A PTC, TVS SMBJ10A, buck 5 V, elco, LDO AP2112K, power-LED | linksboven |
| Rekenkern | XIAO ESP32S3 + Wio-SX1262 op dual-wipe sockets | midden-boven |
| IMU + barometer | BNO085 en BMP581 op de I2C-bus | links-midden en links-onder |
| LoRa-RF | SMA-bulkhead + antenne met keep-out | boven, naast de XIAO |
| Level shifter | TXB0108-breakout (3,3 V <-> 5 V voor de UART) | midden-onder |
| UART-uitgang | 4-pins schroefklem 3,5 mm (GND/5V/TX/RX) | onder-midden |
| RTK-GNSS | Waveshare LC29H(DA) HAT, 2x20-header | verticale strook rechts |

**Buiten de print (mock-up):** Arduino Uno met USB-B en barrel jack, drie servo's, de tweede
XIAO-kit als LoRa-ontvanger op een voetje, de actieve L1/L5 GNSS-antenne op een voetje, en de
laptopzijde. Kabels: IPEX->SMA-pigtail (LoRa), GNSS-coax en de 4-aderige UART-kabel.

## Renders

- **Beeld 1** toont enkel de print (mock-up en bekabeling verborgen) — bedoeld als leesbaar
  bovenaanzicht.
- **Beeld 2** toont de volledige opstelling in 3/4.
- **Beeld 3** is een detail van de voedingssectie samen met de XIAO-socket.

Studio-opstelling: donkere achtergrond, zachte key + fill + rim + top (area-lights), Cycles met
64 samples en denoising.

## Gebruikte afmetingen

De echte datasheet-maten staan in [[gstem-hardware-afmetingen]]. Belangrijkste gevolgen:

- De **LC29H(DA) is een Pi-HAT van 65 x 30,5 mm** (niet een klein breakout). Op 100 x 75 mm past
  hij alleen als **verticale strook** rechts op de print. Zie [[open-vragen]].
- **BNO085 = 25,6 x 22,7 mm** en **BMP581 = 25,4 x 17,8 mm** (STEMMA QT-formaat); dat is groter
  dan de BNO055/BMP390 in [[componenten]].
- De **XIAO** is 21 x 17,8 mm; de kit stapelt via de B2B-connector tot ± 21 mm hoog.

## Gerelateerd

- [[pcb-schets]] — bovenaanzicht en verbindingsschema
- [[pcb-ontwerp]] — footprints en gatmaten
- [[componenten]] — BOM en keuzes
- [[specificaties]] — draagprint-aanpak
- [[gstem-hardware-afmetingen]] — datasheet-maten
