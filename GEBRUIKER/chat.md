---
tags: [gstem, chatlog]
sessie: "01a11077-574a-75ac-bebb-acedd806a11d"
gestart: 2026-10-06T09:21:55.535Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11077-574a-75ac-bebb-acedd806a11d` · gestart 2026-10-06_1121
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 11:21

> [!quote] Verbatim
> werk verder

## AI · 11:25

Ik controleer een paar productpagina's op details (prijs, specificatie).

---

## AI · 11:27

Ik heb alle gegevens. Nu maak ik de bestellijst (markdown) en de Excel aan.

---

## AI · 11:28

De bestanden zijn gemaakt. Nu werk ik het archief bij.

---

## AI · 11:28

Klaar. Ik heb alles op **www.antratek.be** gezocht (via hun eigen zoekfunctie; directe paginatoegang was geblokkeerd, dus ik heb met een script de zoekresultaten en prijzen uitgelezen). Wat daar niet staat, is niet elders gezocht, precies zoals gevraagd.

## Resultaat

**Bestanden aangemaakt**
- `GEBRUIKER/data/bestellijst.md` — de volledige bestellijst met tags, link, kost en aantal
- `documenten/Bestellijst-GSTEM.xlsx` — de Excel-versie (met legende-blad, statuskleuren, hyperlinks en een totaalformule)
- `documenten/build-bestellijst.py` — script om de Excel opnieuw te genereren

**Op antratek gevonden (te bestellen)**

| Component | Aantal | Prijs/st |
| --- | --- | --- |
| XIAO ESP32S3 & Wio-SX1262 kit (toestel + ontvanger) | 2 | € 15,13 |
| Adafruit BNO055 9-DoF IMU | 1 | € 36,24 |
| GNSS L1/L5 multi-band antenne (SMA, actief) | 1 | € 120,94 |
| Interface Cable SMA to U.FL (pigtail) | 1 | € 3,57 |
| DC Barrel Jack Adapter - Female | 1 | € 4,78 |
| Logic Level Converter Bi-Directional (i.p.v. TXB0104) | 1 | € 4,78 |
| Arduino Uno Rev3 | 1 | € 41,75 |

**Totaal:** € 242,32 incl. btw (met de L1/L5-antenne). Met de goedkopere magneetantenne (€ 19,30) wordt dat € 140,68.

**Niet op antratek (tag `geen-link`)** — dus geen aankooplink: BMP390, Quectel LC29H(DA), 2S LiPo-accu, voedingsbescherming (PTC + DMG2301L + SMBJ10A), AP2112K-3.3, 4-pins schroefklem, sockets, power-LED, condensatoren, bulk-elco en M3-montage. Voor de RTK-module staan wel antratek-alternatieven in de lijst (LG290P € 217,74 / ZED-F9P € 302,44).

**Tag `al in bezit`:** LoRa-kitantenne, buck 5 V, servo's, servo-voeding, 3D-print, USB-C datakabel, Dupont-draad en gereedschap.

**Let op:** de gekozen TXB0104 staat niet op antratek; de gevonden bidirectionele level converter (BSS138) is een bruikbaar alternatief. De barrel-adapter is geen PCB-montage. Deze punten staan als open vragen.

> [!info] Opgeslagen: `data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx`, `documenten/build-bestellijst.py`, en bijgewerkt: `onderwerpen.md`, `data/componenten.md`, `data/links.md`, `data/beslissingen.md`, `data/open-vragen.md`

---

## Gebruiker · 11:29

> [!quote] Verbatim
> Arduino uno heb ik zelf thuis nog.

## AI · 11:30

Aangepast: de Arduino Uno staat nu op tag `al in bezit` (heeft de gebruiker thuis), met een verwijzing naar de antratek-prijs als referentie.

**Nieuwe totalen (te bestellen bij antratek):**
- Met L1/L5-antenne: **€ 200,57** incl. btw
- Met goedkopere magneetantenne: **€ 98,93** incl. btw

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/componenten.md` en `data/beslissingen.md`.

> [!info] Opgeslagen: aanpassing Arduino → `al in bezit` in `data/bestellijst.md`, `data/componenten.md` en `data/beslissingen.md`; Excel vernieuwd.

---

## Gebruiker · 11:30

> [!quote] Verbatim
> Zorg ervoor dat de onderdelen die je goedkoper kan vinden dat je die gebruikt. dat het totaal niet absurt wordt

## AI · 11:30

Ik ga voor elk onderdeel op antratek naar goedkopere alternatieven zoeken en die gebruiken waar ze aan de eisen voldoen.

---

## AI · 11:32

Ik lees de huidige bestellijst om de goedkopere keuzes door te voeren.

---

## AI · 11:33

Klaar. Ik heb waar mogelijk het goedkoopste passende alternatief op antratek gekozen.

## Wat is goedkoper geworden

| Component | Was | Nu (goedkoopst op antratek) | Verschil |
| --- | --- | --- | --- |
| GNSS-antenne | L1/L5 multi-band € 120,94 | GPS/GNSS magneetantenne SMA 3m (actief, L1) € 19,30 | − € 101,64 |
| Barometer | BMP390 (niet op antratek) | BME280 breakout € 19,97 | leverbaar i.p.v. geen link |
| Arduino Uno | € 41,75 | in bezit (thuis) | − € 41,75 |

De rest was al de goedkoopste passende optie op antratek: XIAO-kit € 15,13 (losse XIAO + Wio-SX1262 is zelfs 14 cent duurder), BNO055 € 36,24 (goedkoopste 9-DoF met fusie), U.FL–SMA pigtail € 3,57, barreljack € 4,78 en level converter € 4,78.

## Nieuwe totalen (incl. btw)

| Scenario | Bedrag |
| --- | --- |
| **Standaard goedkoopste complete set** | **€ 118,90** |
| Met dual-band L1/L5-antenne (optionele upgrade) | € 220,54 |
| Zonder barometer (BMP390 elders) | € 98,93 |

**Let op:** de goedkope magneetantenne is enkelbandig (L1), dus RTK werkt wel maar minder robuust dan met L1/L5. De dure antenne staat als expliciete upgrade vermeld.

**Niet in het totaal:** de RTK-module (LC29H(DA)) staat niet op antratek. Het goedkoopste antratek-alternatief (LG290P) kost € 217,74 en zou het totaal naar ~€ 336,64 duwen — daarom blijft de LC29H als `geen-link` (elders te regelen).

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/links.md`, `data/beslissingen.md` en `data/componenten.md`.

> [!info] Opgeslagen: goedkopere alternatieven (BME280, magneetantenne) → `data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx`, `data/links.md`, `data/beslissingen.md` en `data/componenten.md`.

---

## Gebruiker · 11:38

> [!quote] Verbatim
> Deze onderdelen heb ik: USB-A naar USB-C voor de XIAO, DC Barrel Jack Adapter - Female, 2S LiPo met connector en kabel,

## AI · 11:39

Toegevoegd als `al in bezit` (had je al): 2S LiPo-accu, DC Barrel Jack Adapter - Female en de USB-A naar USB-C kabel. Ze vallen uit het te-bestellen-totaal.

## Nog te bestellen bij antratek

| Component | Bedrag |
| --- | --- |
| 2x XIAO ESP32S3 + Wio-SX1262 kit | € 30,26 |
| Adafruit BNO055 IMU | € 36,24 |
| BME280 barometer | € 19,97 |
| GPS/GNSS magneetantenne (SMA) | € 19,30 |
| U.FL naar SMA pigtail | € 3,57 |
| Logic Level Converter | € 4,78 |
| **Totaal** | **€ 114,12** |

Alternatieven: met de dual-band L1/L5-antenne wordt het **€ 215,76**; zonder barometer **€ 94,15**.

Bijgewerkt: `GEBRUIKER/data/bestellijst.md`, `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd), `documenten/build-bestellijst.py`, `data/componenten.md` en `data/beslissingen.md`.

> [!info] Opgeslagen: 2S LiPo, barrel-adapter en USB-A/USB-C kabel → `al in bezit` in `data/bestellijst.md`, `data/componenten.md` en `data/beslissingen.md`; Excel vernieuwd.

---
