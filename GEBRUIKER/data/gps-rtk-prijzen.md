---
tags: [gstem, data, gps, rtk, prijsvergelijking, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: gekozen — Eckstein (DE)
---

# GPS/RTK-module — waar te kopen en prijsverschillen

> [!info] Waarom dit bestand
> De gekozen RTK-module is de **Quectel LC29H(DA)** als **breakout board**. Hiervan bestaat een
> kant-en-klaar bord: de **Waveshare LC29H(DA) GPS/RTK HAT (SKU 25279)** — 65 × 30,5 mm, L1+L5
> dual-band RTK rover, UART/I²C, Micro-USB, 40-pins header, **incl. actieve dual-band antenne +
> IPEX→SMA-kabel + schroefset**. Dit bestand vergelijkt **alle vindplaatsen** en de prijsverschillen
> (nagegaan op `2026-10-06`).

## 1. Hetzelfde bord (Waveshare 25279) — prijs per winkel

| Winkel | Land | Prijs (zoals getoond) | ≈ EUR incl. btw | Voorraad | Opmerking |
| --- | --- | --- | --- | --- | --- |
| **Kamami** | Polen (EU) | 270,81 zł incl. (220,17 zł excl.) | **± € 63** | 24 u levering | **goedkoopste EU** |
| **Botland** (store/de) | Polen/Duitsland (EU) | € 70,50 incl. | € 70,50 | op voorraad | alternatief |
| **Eckstein** | Duitsland (EU) | € 71,39 | € 71,39 | leverbaar | art. WS25279 — **gekozen** (`2026-10-06`) |
| Grobotronics | Griekenland (EU) | ~€ 67–75 (niet hard bevestigd) | ~€ 67–75 | ? | prijs niet paginageverifieerd |
| **HESTORE** | Hongarije (EU) | € 91,21 **excl.** btw | **± € 110 incl.** | beperkt (> 2) | **duurste EU** |
| The Pi Hut | VK (**niet EU**) | £ 52,80 incl. (~£ 44 excl.) | ± € 61 | 7 stuks | douane + btw erbij |
| BlackPi | VK (**niet EU**) | £ 51,60 | ± € 60 | **uitverkocht** | — |
| Waveshare (fabrikant) | China | $ 53,99 (1 st.) | ± € 50 | op voorraad | + verzending + invoer/btw |
| allinbest / Alibaba | China | $ 52,99–77,30 | ± € 49–71 | op voorraad | dropship |
| RobotShop | VS/CA | $ 68,54 | ± € 63 | op voorraad | buiten EU |
| malina314 | Servië | 7 999 RSD | ± € 68 | — | niet EU |
| Hubtronics | India | ₹ 6 690 | ± € 66 | — | niet EU |
| motorobit | Turkije | 6 781,50 TL + btw | ± € 170 | 3 st. | erg duur |

> [!success] Conclusie prijsverschil
> Binnen de **EU** loopt de prijs uiteen van **± € 63 (Kamami)** tot **± € 110 (HESTORE)** — een
> verschil van **± € 47** voor exact hetzelfde bord. **Kamami** is nominaal het goedkoopst (± € 63),
> **Botland** (€ 70,50) rekent in EUR. **Gekozen is Eckstein (DE, € 71,39 incl.)** — `2026-10-06`:
> een Duitse EU-winkel, snelle levering, prijs in EUR, `WS25279`. **HESTORE** is duidelijk te duur
> (± € 110 incl.) voor dit bord.
>
> Buiten de EU is het nominaal goedkoper (Pi Hut ± € 61, Waveshare ± € 50), maar dan komen
> **verzendkosten + invoer/btw + douane** erbij (en het is geen EU-garantie).

## 2. Alternatieven met dezelfde chip (andere breakouts)

| Bord | Prijs | Land | Opmerking |
| --- | --- | --- | --- |
| **7Semi LC29HDA Dual-Band GNSS RTK Board** (Qwiic/USB-C) | $ 42 (~€ 39) | India | mooiere/kleinere breakout, **niet EU** |
| **MIKROE GNSS RTK 3 Click** (MIKROE-5914, mikroBUS) | € onbekend | EU (TME/DigiKey) | TME **niet op voorraad**; DigiKey levert met **4 weken** levertijd |
| Generiek "LC29HDA RTK board" | € 30,43 | Ierland/CN (Amazon.ie) | dropship, **geen Waveshare**, kwaliteit onbekend |
| Losse module **LC29H-DA** (geen breakout) | € 20,69 excl. | NL (TOP-electronics) | **uitverkocht**; losse SMD-module — gebruiker wil een **breakout** |

## 3. Andere RTK-modules (duurder alternatief, met andere chip)

Beschikbaar bij **antratek.be (BE, EU)**, allemaal op voorraad — maar veel duurder:

| Module | Prijs incl. btw |
| --- | --- |
| Quadband GNSS RTK Breakout — LG290P (Qwiic) | € 217,74 |
| GPS-RTK Postcard (Qwiic) | € 266,14 |
| GPS-RTK-SMA Board — ZED-F9P | € 302,44 |
| GPS-RTK Dead Reckoning — ZED-F9R | € 362,94 |
| All-Band GNSS RTK Breakout — ZED-X20P | € 362,94 |

> [!note] Waarom de LC29H(DA) blijft
> De LC29H(DA)-breakout (± € 63–71 in de EU) is **3 tot 5 keer goedkoper** dan de ZED-F9P/LG290P-
> alternatieven en levert dezelfde **centimeter-nauwkeurigheid** met RTK + NTRIP. Daarom blijft de
> Waveshare LC29H(DA) HAT de keuze; de **winkel** is **Eckstein (DE)** geworden (`2026-10-06`).

## Bronnen

- Waveshare (fabrikant): waveshare.com/lc29h-gps-hat.htm
- Kamami: kamami.pl (EN-productpagina, prijs + levering)
- Botland: botland.store / botland.de
- Eckstein: eckstein-shop.de
- HESTORE: hestore.eu/prod_10047904.html
- The Pi Hut: thepihut.com · BlackPi: blackpi.shop
- antratek: antratek.be (RTK-alternatieven)
- 7Semi: 7semi.com · TOP-electronics: top-electronics.com

## Gerelateerd

- [[bestelbaarheid]] — verificatie van alle bestellijst-artikelen
- [[bestellijst]] — de volledige bestellijst
- [[links]] — winkels en URL's
- [[componenten]] — waarom juist de LC29H(DA)
