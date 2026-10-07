---
tags: [gstem, data, gps, rtk, prijsvergelijking, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-07
status: LC29HDA rover gekozen; AliExpress-listing te verifiëren
---

# GPS/RTK-module — waar te kopen en prijsverschillen

> [!info] Waarom dit bestand
> De gekozen RTK-module is de **Quectel LC29H(DA)** als **breakout board**. Hiervan bestaat een
> kant-en-klaar bord: de **Waveshare LC29H(DA) GPS/RTK HAT (SKU 25279)** — 65 × 30,5 mm, L1+L5
> dual-band RTK rover, UART/I²C, Micro-USB, 40-pins header, **incl. actieve dual-band antenne +
> IPEX→SMA-kabel + schroefset**. Dit is de bekende Waveshare-terugvaloptie; de nieuwe voorkeur
> (`2026-10-07`) is een China/AliExpress-aankoop, maar de concrete listing is nog niet gevalideerd.
> De historische winkelprijzen hieronder zijn nagegaan op `2026-10-06`.

## 1. Hetzelfde bord (Waveshare 25279) — prijs per winkel

| Winkel | Land | Prijs (zoals getoond) | ≈ EUR incl. btw | Voorraad | Opmerking |
| --- | --- | --- | --- | --- | --- |
| **Kamami** | Polen (EU) | 270,81 zł incl. (220,17 zł excl.) | **± € 63** | 24 u levering | **goedkoopste EU** |
| **Botland** (store/de) | Polen/Duitsland (EU) | € 70,50 incl. | € 70,50 | op voorraad | alternatief |
| **Eckstein** | Duitsland (EU) | € 71,39 | € 71,39 | leverbaar | art. WS25279 — terugvaloptie, niet meer eerste keuze (`2026-10-07`) |
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
> Binnen de **EU** liep de prijs uiteen van **± € 63 (Kamami)** tot **± € 110 (HESTORE)** voor de
> Waveshare 25279. **Eckstein (€ 71,39)** was op `2026-10-06` de toenmalige keuze, maar is per
> `2026-10-07` gedegradeerd tot terugvaloptie omdat de gebruiker liever uit China koopt, liefst via
> AliExpress. Een concrete AliExpress-prijs, verzending en btw moeten nog uit een echte aanbieding
> worden vastgesteld; een zoekresultaat is geen aankoopverificatie.

## 2. Alternatieven met dezelfde chip (andere breakouts)

| Bord | Prijs | Land | Opmerking |
| --- | --- | --- | --- |
| **7Semi LC29HDA Dual-Band GNSS RTK Board** (Qwiic/USB-C) | $ 42 (~€ 39) | India | mooiere/kleinere breakout, **niet EU** |
| **MIKROE GNSS RTK 3 Click** (MIKROE-5914, mikroBUS) | € onbekend | EU (TME/DigiKey) | TME **niet op voorraad**; DigiKey levert met **4 weken** levertijd |
| Generiek "LC29HDA RTK board" | € 30,43 | Ierland/CN (Amazon.ie) | dropship, **geen Waveshare**, kwaliteit onbekend |
| Losse module **LC29H-DA** (geen breakout) | € 20,69 excl. | NL (TOP-electronics) | **uitverkocht**; losse SMD-module — gebruiker wil een **breakout** |

## 3. AliExpress-zoekrichting en technische controle (`2026-10-07`)

De juiste functie blijft **LC29HDA = RTK rover**. Er zijn geïndexeerde AliExpress-resultaten voor
"LC29HDA development board" en soortgelijke beschrijvingen, maar sommige verkopers noemen hun product
"base station" terwijl de titel tegelijk LC29HDA noemt. Dat is tegenstrijdig en niet genoeg om een
board als geschikt te bestempelen. De vorige kandidaatlink (**1005010036256167**) werkte niet; de gebruiker
heeft die vervangen door AliExpress-item **1005009915138674**. De nieuwe aanbieding is nog niet onafhankelijk
gecontroleerd, dus variant, bordtype, prijs, bundel en pinout moeten op de productpagina worden bevestigd.

- [AliExpress-kandidaat: item 1005009915138674](https://nl.aliexpress.com/item/1005009915138674.html?spm=a2g0o.productlist.main.2.655266fbjTfZeJ&algo_pvid=4fc1f3eb-8eba-45f3-a074-c2f860178059&algo_exp_id=4fc1f3eb-8eba-45f3-a074-c2f860178059-1&pdp_ext_f=%7B%22order%22%3A%2215%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%2123.08%2122.19%21%21%21169.67%21163.17%21%40210384a717913577024408827e0d20%2112000050564705367%21sea%21BE%212399807721%21ACX%211%210%21n_tag%3A-29919%3Bd%3A8a193b71%3Bm03_new_user%3A-29894&curPageLogUid=u9WOlX5tyEMY&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009915138674%7C_p_origin_prod%3A) — door gebruiker aangeleverde vervangende listing; inhoud en prijs nog te controleren.
- [AliExpress-zoekopdracht: Quectel LC29HDA RTK rover board](https://www.aliexpress.com/wholesale?SearchText=Quectel+LC29HDA+RTK+rover+board) — zoekresultaten.
- [Waveshare GPS External Antenna (D), SKU 25346](https://www.waveshare.com/gps-external-antenna-d.htm) — actieve L1+L5-antenne, LNA 28±2 dB, SMA-J, 3 m kabel; technisch passend qua frequentiebanden voor LC29HDA. Prijs op fabrikantspagina: $16,99; niet in besteltotaal.
- [Waveshare-specificatie van de HAT-varianten](https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT) — DA = terminal/rover voor RTK; BS = basisstationvariant.
- [Waveshare-productpagina](https://www.waveshare.com/lc29h-gps-hat.htm) — referentie voor de complete HAT en de gebundelde antenne.

> [!success] Update `2026-10-07`: gekozen listing + eenduidige alternatieven
> De richtprijs voor een LC29HDA-developmentboard op AliExpress ligt rond **± € 22** (snippets tonen
> US $ 18,75–25,55, afhankelijk van bundel/antenne). Omdat de gebruikerslink **1005009915138674**
> "LC29H" vermeldt en niet expliciet "LC29HDA", zijn er twee **eenduidige alternatieven met
> variantkeuzemenu** (kies daar **LC29HDA**):
> - [AliExpress-item 1005010758488281](https://www.aliexpress.com/item/1005010758488281.html) — development board met USB Type-C, keuze uit LC29HDA/LC29HBA/LC29HEA/LC29HBS.
> - [AliExpress-item 1005010162466640](https://www.aliexpress.com/item/1005010162466640.html) — LC29HDA-boardkit, L1+L5, met antenne-opties.
>
> Terugvaloptie in de EU blijft de **Waveshare LC29H(DA) HAT** (Eckstein € 71,39 / Kamami ± € 63),
> die een passende dual-bandantenne meelevert.

> [!warning] Controle vóór aankoop
> De gebruiker heeft [AliExpress-item 1005009915138674](https://nl.aliexpress.com/item/1005009915138674.html?spm=a2g0o.productlist.main.2.655266fbjTfZeJ&algo_pvid=4fc1f3eb-8eba-45f3-a074-c2f860178059&algo_exp_id=4fc1f3eb-8eba-45f3-a074-c2f860178059-1&pdp_ext_f=%7B%22order%22%3A%2215%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%2123.08%2122.19%21%21%21169.67%21163.17%21%40210384a717913577024408827e0d20%2112000050564705367%21sea%21BE%212399807721%21ACX%211%210%21n_tag%3A-29919%3Bd%3A8a193b71%3Bm03_new_user%3A-29894&curPageLogUid=u9WOlX5tyEMY&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009915138674%7C_p_origin_prod%3A) aangeleverd als vervanging van de niet-werkende eerdere link. De nieuwe listing is **nog niet inhoudelijk geverifieerd**. Bevestig vóór bestelling dat het de **LC29HDA-rover** is op een geassembleerd breakout (geen BS-base-stationvariant of losse SMD-module). Controleer pinout (UART TX/RX, voeding en IO-niveau), bordafmetingen, reviews en checkout-totaal. Vraag ook wat antennes/connectoren inbegrepen zijn en of de antenne L1/L5 ondersteunt. RTCM-correctie-invoer vanaf de bestaande NTRIP/laptop/LoRa-keten blijft noodzakelijk.
>
> De passende losse antennekandidaat is de **Waveshare GPS External Antenna (D), SKU 25346**: actief L1+L5, LNA 28±2 dB, SMA-J en 3 m kabel. De RF-specificatie past bij LC29HDA, maar de **connectorcompatibiliteit is nog niet bevestigd** voor het AliExpress-board. Bestel alleen als de kit geen geschikte antenne bevat en de SMA-J-aansluiting (of benodigde adapter) overeenkomt; controleer ook of het board één of twee antennes nodig heeft.

> [!info] Betekenis van "DA"
> `DA` is onderdeel van de modulevariant **LC29HDA** (RTK-rover); het betekent hier niet een D/A-
> converter. De Waveshare-HAT-lijn biedt bovendien **DA (rover)** en **BS (basisstation)** uitvoeringen.

## 4. Andere RTK-modules (duurder alternatief, met andere chip)

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
> alternatieven en levert dezelfde **centimeter-nauwkeurigheid** met RTK + NTRIP. De **LC29HDA blijft
> de technische keuze**; de aankoopwinkel en concrete listing zijn open. Eckstein is sinds `2026-10-07`
> alleen terugvaloptie.

## Bronnen

- AliExpress-vervangende listing item 1005009915138674 (door gebruiker aangeleverd; nog niet technisch geverifieerd): https://nl.aliexpress.com/item/1005009915138674.html
- AliExpress-zoekresultaten: https://www.aliexpress.com/wholesale?SearchText=Quectel+LC29HDA+RTK+rover+board
- Waveshare-specificatie: https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT
- Waveshare (fabrikant): https://www.waveshare.com/lc29h-gps-hat.htm
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
