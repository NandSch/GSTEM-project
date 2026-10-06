---
tags: [gstem, data, bestelbaarheid, verificatie, aankoop]
aangemaakt: 2026-10-06
bijgewerkt: 2026-10-06
status: geverifieerd
---

# Bestelbaarheid — verificatie van de bestellijst

> [!info] Wat is dit?
> Van elk artikel op [[bestellijst]] is op **2026-10-06** nagegaan of het **daadwerkelijk
> bestelbaar** is: bestaat de pagina, klopt de prijs, en is er voorraad. Bron per regel: of de
> **productpagina gefetcht** is (sterk) of enkel een **zoekresultaat/snippet** (minder zeker).
> TME, Mouser en DigiKey blokkeren directe fetches met HTTP 403 → daar komt alles uit snippets.

## Samenvatting

> [!success] Alles wat op de bestellijst staat, is bestelbaar
> Alle artikelen waar een winkel voor gekozen is, zijn **nu leverbaar**. Wel drie aandachtspunten:
> 1. **Kiwi: lage voorraad** bij de **keramische condensatorkit (2 st.)** en de **BMP581 (4 st.)** —
>    bestelbaar, maar niet in grote aantallen.
> 2. **Precisie-sockets (Preci-Dip)**: bij TME alleen **business/MOQ 380**, niet in kleine aantallen
>    bevestigd. Alternatief: standaard 2,54 mm turned-pin sockets of dual-wipe headers.
> 3. **TME niet fetchbaar** (403) → TME-prijzen/voorraad komen uit snippets, niet van de pagina zelf.

## Kiwi Electronics (NL) — alles op voorraad

| Artikel | Prijs incl. btw | Voorraad | Betrouwbaarheid |
| --- | --- | --- | --- |
| Adafruit BNO085 9-DoF IMU (STEMMA QT) | € 32,05 | Op voorraad: **11 st.** | pagina gefetcht |
| Adafruit BMP581 druk-/temperatuursensor | € 10,88 | Op voorraad: **4 st.** (krap) | pagina gefetcht |
| 8-kanaals level converter TXB0108 | € 8,70 | Op voorraad: 17 st. | pagina gefetcht |
| 3 mm LED rood (10-pack) | € 1,20 | Op voorraad: 193 st. | **heeft de gebruiker thuis — niet bestellen** (`2026-10-06`) |
| Weerstand 330 Ω (10 st.) | € 0,96 | Op voorraad: 115 st. | **heeft de gebruiker thuis — niet bestellen** (`2026-10-06`) |
| Keramische condensator kit (450 st.) | € 10,27 | Op voorraad: **2 st.** (krap) | pagina gefetcht |
| 100 µF / 16 V elco | € 0,59 | Op voorraad: 72 st. | pagina gefetcht |

> [!warning] Niet op de lijst, maar wel nodig
> De aanbevolen **STEMMA QT/Qwiic-kabel 100 mm (Kiwi 10385)** is **niet op voorraad**. Neem een
> alternatief (JST-SH 4-pins kabel) of soldeer de modules.

## antratek.be (BE) — alles op voorraad

| Artikel | Prijs incl. btw | Voorraad | Betrouwbaarheid |
| --- | --- | --- | --- |
| XIAO ESP32S3 & Wio-SX1262 Kit (102010611) | € 15,13 | Op voorraad | pagina gefetcht |
| Interface Cable SMA → U.FL 150 mm (WRL-18568) | € 3,57 | Op voorraad | pagina gefetcht (JSON-LD) |

> [!note] Losse XIAO/Wio bij antratek
> Los verkrijgbaar maar met **2-3 weken levertijd**: XIAO ESP32-S3 € 9,06 en Wio-SX1262 € 5,93.
> Geen prijsvoordeel t.o.v. de kit (€ 15,13) → **kit blijft de keuze**.

## TME / Mouser / DigiKey (EU) — losse elektronica

| Onderdeel | Bestelcode | Winkel | Prijs (excl. btw) | Voorraad | Betrouwbaarheid |
| --- | --- | --- | --- | --- | --- |
| LDO 3,3 V | AP2112K-3.3TRG1 | TME | $ 0,24 @1 | **8 198** | snippet |
| LDO 3,3 V (alt.) | AP2112K-3.3DICT-ND | DigiKey | $ 0,35 @1 | op voorraad | snippet |
| TVS-diode | SMBJ10A-TR (ST) | TME | $ 0,55 @1 | **1 820** | snippet |
| P-MOSFET (niet gebruikt) | AO3401A | TME | $ 0,34 @1 | **22 840** | snippet |
| P-MOSFET (niet gebruikt) | DMG2301L-13 | TME | geen prijs | **niet op voorraad, MOQ 10 000** | snippet |
| P-MOSFET (niet gebruikt) | DMG2301L-7 | Mouser | ~RM 1,57 @1 (~€ 0,32) | losse aantallen | snippet |
| 2 A PTC 1812, 16 V | 1812L200/16DR | Mouser / DigiKey | ~€ 1,09 @1 | 14 555 (Mouser) / 9 900 (DK) | snippet |
| Precisie-socket 2,54 mm | Preci-Dip 110-87-320-41-001101 | TME | geen prijs | **external stock, MOQ 380, business** | snippet |
| Precisie-socket 2,54 mm (alt.) | Preci-Dip 110-83-320-41-001101 | Mouser / DigiKey / RS 7022704 | onbekend | waarschijnlijk op voorraad | snippet |

> [!important] Twee verbeteringen t.o.v. de bestellijst
> - **P-MOSFET vervalt** (`2026-10-06`): noch de **DMG2301L** noch de **AO3401A** wordt gekocht — er
>   komt **geen ompoolbeveiliging**. De PTC-zekering en de TVS blijven. Zie [[afgevoerd]].
> - De **KF128-3.5 schroefklem** bestaat **niet** bij TME (0 zoekresultaten). Gebruik de push-in
>   **DEGSON DG250-3.5-04P** of de **schroef**-variant **DEGSON 15EDGK-3.5/4P**.

## HESTORE / TinyTronics / Bits & Parts — mechanisch

| Onderdeel | Winkel | Prijs | Voorraad | Betrouwbaarheid |
| --- | --- | --- | --- | --- |
| DEGSON DG250-3.5-04P (push-in klem) | HESTORE (HU) | € 0,521 excl. btw | **> 10 op voorraad** | pagina gefetcht |
| DEGSON 15EDGK-3.5/4P (**schroef**klem) | HESTORE (HU) | € 1,095 excl. btw | **> 15 op voorraad** | pagina gefetcht |
| M3 Afstandsbusje Kit (AFBUSM3-KIT) | TinyTronics (NL) | € 8,00 incl. btw | **Direct leverbaar**, 50+ | pagina gefetcht |
| M3 spacer/standoff-set 180-delig | Bits & Parts (NL) | € 6,95 incl. btw | Direct uit voorraad | pagina gefetcht |
| 4-pins 3,5 mm schroefklem (Sparkfun PRT-15519) | Opencircuit (NL) | € 5,25 incl. btw | extern magazijn, **5-7 werkdagen** | pagina gefetcht |

> [!note] Kleine correcties
> - De klem bij HESTORE is **€ 0,521 excl.** (~€ 0,63 incl.) — iets goedkoper dan de € 0,61 op de lijst.
> - **TinyTronics heeft géén 4-pins 3,5 mm schroefklem** uit eigen voorraad; Opencircuit levert er
>   een, maar met levertijd.

## Bronnen

- Kiwi: kiwi-electronics.com (productpagina's, 2026-10-06)
- antratek: antratek.be (productpagina's)
- TME: tme.eu (via snippets — directe fetch 403)
- Mouser/DigiKey: mouser.com / digikey.ie / digikey.co.uk (via snippets — 403)
- HESTORE: hestore.eu · TinyTronics: tinytronics.nl · Bits & Parts: bitsandparts.nl · Opencircuit: opencircuit.nl

## Gerelateerd

- [[bestellijst]] — de lijst zelf
- [[gps-rtk-prijzen]] — prijsvergelijking van de GPS/RTK-module
- [[links]] — alle winkels en URL's
- [[open-vragen]] — socket-keuze en lage voorraad
