---
tags: [gstem, chatlog]
sessie: "01a111fe-dbc2-7490-b89e-c75e1b0f925e"
gestart: 2026-10-06T16:14:37.515Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a111fe-dbc2-7490-b89e-c75e1b0f925e` · gestart 2026-10-06_1814
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 18:14

> [!quote] Verbatim
> Je verifieert of 7 specifieke artikelen bij de Nederlandse webwinkel **Kiwi Electronics** (kiwi-electronics.com) op dit moment **daadwerkelijk bestelbaar** zijn (dus: pagina bestaat, prijs incl. btw klopt, en voorraadstatus "op voorraad"/"uitverkocht"/"pre-order"). Dit is voor een schoolproject (G-Stem) dat een bestellijst wil waarop álles zeker bestelbaar is.
> 
> Werkwijze:
> - Fetch elke productpagina met de `fetch_content` tool (mode "readable" of "raw"). Als een fetch faalt, probeer dan `web_search` met de productnaam + "kiwi-electronics.com" om de voorraadstatus/prijs uit de snippet te halen.
> - Je MOET per artikel aanwezigheid + prijs + voorraadstatus rapporteren. Verzin niets: als je het niet kunt vaststellen, zeg dat expliciet.
> - Let op: Kiwi toont "Op voorraad" / "Niet op voorraad" / "Levertijd X dagen" en prijzen met "incl. btw".
> 
> De 7 artikelen (prijzen zijn de verwachte prijs incl. btw; controleer of ze kloppen):
> 1. Adafruit 9-DOF Orientation IMU Fusion BNO085 (BNO080) STEMMA QT — verwacht EUR 32,05 — https://www.kiwi-electronics.com/nl/adafruit-9-dof-orientation-imu-fusion-breakout-bno085-bno080-stemma-qt-qwiic-11273
> 2. Adafruit BMP581 I2C/SPI druk- en temperatuursensor STEMMA QT — verwacht EUR 10,88 — https://www.kiwi-electronics.com/nl/adafruit-bmp581-i2c-spi-druk-en-temperatuursensor-stemma-qt-20534
> 3. 8-kanaals bidirectionele Logic Level Converter TXB0108 — verwacht EUR 8,70 — https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836
> 4. 3mm LED diffuus rood (10-pack) — verwacht EUR 1,20 — https://www.kiwi-electronics.com/nl/3mm-led-diffuus-rood-10-pack-3085
> 5. Weerstand 330 Ohm 1/4 watt 5% (10 stuks) — verwacht EUR 0,96 — https://www.kiwi-electronics.com/nl/weerstand-330-ohm-1-4-watt-5-10-stuks-653
> 6. Keramische condensator kit in doos (15 soorten, 450 stuks) — verwacht EUR 10,27 — https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492
> 7. 100uF 16V condensator (bulk-elco) — verwacht EUR 0,59 — https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440
> 
> Rapporteer als een markdown-tabel met kolommen: # | Artikel | Prijs (EUR, incl. btw) | Voorraadstatus | Bron-URL | Betrouwbaarheid (pagina gefetcht / alleen snippet / onbekend). Voeg daarna in max. 5 regels toe welke artikelen twijfelachtig zijn. Houd het geheel onder 400 woorden. Schrijf in het Nederlands.
