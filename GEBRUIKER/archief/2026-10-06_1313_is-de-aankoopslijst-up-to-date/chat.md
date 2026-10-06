---
tags: [gstem, chatlog]
sessie: "01a11077-574a-75ac-bebb-acedd806a11d"
gestart: 2026-10-06T11:13:56.149Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11077-574a-75ac-bebb-acedd806a11d` · gestart 2026-10-06_1313
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 13:14

> [!quote] Verbatim
> Is de aankoopslijst up to date?

## AI · 13:14

Even de bestellijst controleren.

---

## AI · 13:14

Nee — hij is **gedeeltelijk verouderd**. De "in bezit"-regels en de antratek-prijzen kloppen nog, maar de Kiwi-bevindingen van net en jouw keuzes zijn er nog niet in verwerkt.

## Wat niet meer klopt

| Regel in de lijst | Huidige stand |
| --- | --- |
| Kopnoot: *"eerst antratek, wat daar niet staat is niet elders gezocht"* | Achterhaald — Kiwi is nu doorzocht |
| IMU: **BNO055** antratek € 36,24 | Jouw vondst: **BNO085** bij Kiwi **€ 32,05** (goedkoper + nieuwer) |
| Barometer: **BME280** antratek € 19,97 (plaatsvervanger) | Jouw voorkeur: beter model → **BMP581** bij Kiwi **€ 10,88**; BMP390L bij Kiwi **uit voorraad** |
| GNSS-antenne: antratek magneet € 19,30 | Kiwi actieve SMA **€ 16,93** (goedkoper) |
| Pigtail: antratek **€ 3,57** | Kiwi **€ 4,22** (duurder → afwegen per winkel) |
| Level shifter: antratek BSS138 **€ 4,78** | Kiwi **TXB0108 € 8,70** (past bij de gekozen TXB-serie) |
| Rekenkern: kit antratek **€ 15,13** | Kiwi: XIAO **€ 8,46** los + Wio-SX1262 **€ 5,43** (maar **uit voorraad**) |
| Noot barometer: *"zoeken elders uitgesteld"* | Klopt niet meer — Kiwi is bekeken |
| Totalen: antratek-only **€ 114,12** | Nog niet herrekend met Kiwi-prijzen |

## Wat nog wél klopt
- Alle `al-in-bezit`-regels (Arduino, LiPo, barrel, USB-kabels, gereedschap, servo's, 3D-print).
- De `geen-link`-onderwerpen blijven terecht: Kiwi heeft óók geen **RTK-module**, **discrete voeding** (PTC/MOSFET/TVS/LDO), **4-pins schroefklem**, **sockets** of **M3-montage**.

## Blijvende knelpunten
- **Wio-SX1262 uit voorraad** bij Kiwi → LoRa kan daar nu niet vandaan.
- **Geen RTK** bij Kiwi → minstens één andere winkel sowieso nodig.

Zal ik de bestellijst nu herwerken naar deze stand: een **Kiwi-kolom/tag** voor alles wat daar kan (BNO085, BMP581, antenne, XIAO, TXB0108, LED/R/C), **antratek** behouden waar goedkoper (pigtail) of als reserve (Wio-kit), en de **RTK + discrete onderdelen + connectoren + M3** als tweede-winkel markeren? Dan herreken ik ook de totalen en werk ik de Excel bij.

---

## Gebruiker · 13:15

> [!quote] Verbatim
> Update excel bestand om overeen te komen hiermee.

## AI · 13:15

Ik werk de Excel bij. Eerst de exacte Kiwi-links en prijzen nog eens verifiëren zodat de links kloppen.

---

## AI · 13:16

Alle links en prijzen zijn bevestigd. Nu de build-script herwerken en de Excel opnieuw genereren.

---

## AI · 13:16

Excel is bijgewerkt. Nu de markdown-bestellijst gelijktrekken zodat archief en Excel overeenkomen.

---

## AI · 13:16

Klaar — de Excel is bijgewerkt en komt nu overeen met de nieuwe stand.

## `documenten/Bestellijst-GSTEM.xlsx` (opnieuw gegenereerd)

- **Nieuwe tag `kiwi`** (lichtblauw) naast `antratek` (groen); legenda-blad bijgewerkt.
- **BNO085** (€ 32,05) vervangt de BNO055 → Kiwi
- **BMP581** (€ 10,88) vervangt de BME280 → Kiwi
- **GNSS-antenne** Kiwi (€ 16,93)
- **TXB0108** level converter Kiwi (€ 8,70)
- **LED + weerstand** (€ 2,16), **condensatorkit** (€ 10,27), **bulk-elco** (€ 0,59) → Kiwi
- **XIAO-kit** blijft antratek (Wio-SX1262 bij Kiwi uit voorraad), **pigtail** blijft antratek (goedkoper)
- Alle Kiwi-links zijn gecontroleerd en kloppen (exacte product-URL's).

### Totalen in de Excel
| Winkel | Bedrag |
| --- | --- |
| Kiwi Electronics | **€ 81,58** |
| antratek.be | **€ 33,83** |
| **Totaal te bestellen** | **€ 115,41** |

De totalen staan als Excel-formules (`=SUMIF(...)`), dus ze rekenen automatisch mee als je prijzen aanpast.

## Verder bijgewerkt
- `GEBRUIKER/data/bestellijst.md` — gelijkgetrokken met de Excel (Kiwi-tag, links, totalen, open acties).
- `GEBRUIKER/data/beslissingen.md` — beslissing "zo veel mogelijk bij Kiwi Electronics" met bedragen.
- `GEBRUIKER/data/links.md` — Kiwi-productlinks (al eerder toegevoegd).

**Blijft open:** een tweede winkel voor de `geen-link`-onderdelen (RTK-module, discrete voeding, 4-pins schroefklem, sockets, M3-montage). Wil je dat ik daarvoor een geschikte leverancier zoek zodat het bij 2 winkels blijft?

---
