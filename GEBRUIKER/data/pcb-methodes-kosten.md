---
tags: [gstem, data, pcb, hardware, kosten, vergelijking]
aangemaakt: 2026-10-06
status: analyse
---

# PCB-methodes: kosten en moeilijkheid

> [!info] Doel
> Vergelijking van manieren om de componenten op de draagprint te plaatsen: kosten,
> soldeermoeilijkheid en hoe makkelijk het passende onderdeel te vinden is. Hoort bij
> [[specificaties]] en [[pcb-schets]].

## Telling van connectoren/pinnen

| Module | Vorm | Pinnen |
| --- | --- | --- |
| ESP32-S3-devkit | 2 rijen | 44 |
| LoRa (RFM95-breakout) | 2 rijen | 16 |
| IMU BNO055-breakout | 1 rij | 8 |
| Barometer (BMP280/BME280) | 1 rij | 6 |
| RTK-GNSS-breakout | 2 rijen | ~20 |
| Uitbreidingsconnector | 1 rij | 8 |
| **Totaal** | | **≈ 102 pinnen** |

Dat is ± 3 strips van 40 pinnen, of ± 102 soldeerpunten.

## Gecontroleerde prijzen (peildatum 2026-10-06, indicatief)

| Onderdeel | Prijs | Bron |
| --- | --- | --- |
| ESP32-S3-WROOM-1-N4 | ± $2,12 | LCSC |
| RFM95W-868S2 | ¥51,21 (≈ €6,50) | LCSC |
| Adafruit BNO055-breakout | $34,95 | Adafruit |
| Adafruit BMP581 | $9,95 | Adafruit |

## Kosten en moeilijkheid per methode (per bord, indicatief in euro)

| Methode | Connector/pin-kosten | Extra materiaal | Gereedschap | Soldeermoeilijkheid | Onderdeel vinden |
| --- | --- | --- | --- | --- | --- |
| Strip-sockets (huidig) | €2–3 | — | soldeerbout | makkelijk (THT) | triviaal |
| Precisie-/gefreesde sockets | €3–5 | — | soldeerbout | makkelijk (THT) | makkelijk |
| Direct vastsolderen (pinheaders) | €1–2 | — | soldeerbout | makkelijk | triviaal |
| Castellated (SMD) | €0 | kale modules: ESP €2, LoRa €6,50, baro €1–2, RTK €150+, IMU lastig | reflow/hot-air (€60–150) of JLCPCB-assembly (setup €15–30) + stencil | moeilijk | ESP/LoRa/baro makkelijk; BNO055 is LGA (lastig); ZED-F9P duur maar leverbaar |
| Board-to-board (DF40) | €10–24 (5–6 paren × €2–4) | eigen dragerprintjes (€5–10 p/stuk) | reflow | moeilijk (pitch 0,4 mm) | connector makkelijk, mating-connector op module ontbreekt meestal |
| Sub-bordjes + JST-GH | €5–6 | kabels €5–15 + extra PCB's €15–25 | krimptang €20–40 | matig | makkelijk |

De **PCB zelf** (2-laags, 5 stuks JLCPCB) kost ± €2–5 + verzending €5–15; castellated vraagt mogelijk 4-laags + ENIG + stencil.

## Conclusies

- **Goedkoopst en makkelijkst:** strip- of precisie-sockets en direct solderen (€1–5). Het verschil strip ↔ precisie is slechts €1–2; precisie-sockets halen meteen het amateuristische eraf.
- **Castellated** is het meest afgewerkt, maar de kosten zitten in de **RTK-GNSS (€150+)** en de **IMU** (BNO055 enkel als LGA of breakout). Voor sensoren niet vanzelfsprekend.
- **Board-to-board (DF40)** is duurst en lastigst: je moet zelf dragerprintjes maken omdat standaard-breakouts geen matende connector hebben.
- **Sub-bordjes + JST-GH** zijn professioneel en modulair, maar kosten extra PCB's, kabels en een krimptang (± €40–70).
- **Pogo pins** enkel voor een testfixture.

**Advies:** precisie-/gefreesde sockets, met IMU/barometer eventueel direct gesoldeerd. Echt productniveau pas met castellated voor ESP32 + LoRa.

## Waarom niet overal dual-wipe? (2026-10-06)

Alles met dual-wipe kan, maar vier bezwaren:

1. **Trillingen** — het toestel staat op een bewegend voertuig; gestempelde contacten verliezen veerkracht en geven intermitterend contact, precisie klemt vaster.
2. **Contactkwaliteit** — precisie heeft 3–4 contactpunten en lagere/stabielere overgangsweerstand dan dual-wipe (2 punten); belangrijk voor voeding en analoge sensoren (IMU, barometer).
3. **Kwaliteitsverschil** — veel goedkope female headers heten dual-wipe maar zijn in de praktijk enkelbladig.
4. **Slijtageverloop** — dual-wipe verliest bij veelvuldig wisselen sneller zijn klemkracht; precisie behoudt die langer.

| Situatie | Beste keuze |
| --- | --- |
| Vaak gewisselde modules (ontwikkeling, ESP32) | Dual-wipe |
| Vast gemonteerde modules (IMU, baro, GNSS, voeding) | Precisie |
| Nooit wisselen | Precisie overal |
| Niet bang voor trillingen | Dual-wipe overal (minder robuust) |

**Advies:** gemengd — dual-wipe waar je wisselt, precisie waar het definitief blijft. Trillingen zijn de doorslaggevende factor (bewegend voertuig).

## Sockettypes uitgelegd (2026-10-06)

Een dual-wipe socket is een female-contact met **twee tegenover elkaar liggende veerlippen** die de pin van twee kanten vastklemmen. Bij het insteken schuiven ("wipen") die contactpunten over de pin, wat oxide wegveegt.

| Type | Contact | Contactpunten | Inklikkracht | Cycli | Prijs |
| --- | --- | --- | --- | --- | --- |
| Normale female header (strip) | 1 veerblad (tuning-fork) | 1 | laag | laag–matig | € |
| Dual-wipe | 2 veren tegenover elkaar | 2 | laag–matig | hoger | €€ |
| Precisie/gefreesd | rond busje met 3–4 vingers | 3–4 | hoog | honderden–1000 | €€€ |

Kort: normale header = 1 contactpunt, dual-wipe = 2, precisie = 3–4 én hoge kracht. Dual-wipe komt vooral voor als DIP-IC-socket en bij betere 2,54 mm female headers.

## In- en uitklikken van precisie-sockets (2026-10-06)

Precisie-/gefreesde sockets klemmen veel harder dan gewone dual-wipe sockets: ± 0,5–1,5 N per pin tegen ± 0,2–0,5 N. De totale inklik-kracht schaalt met het aantal pinnen:

| Module | Pinnen | Totale kracht (ruw) | Moeilijkheid |
| --- | --- | --- | --- |
| ESP32-S3 (2×22) | 44 | ± 2,5–6,5 kgf | hard |
| RTK-GNSS (2×10) | ~20 | ± 1–3 kgf | matig |
| LoRa (2×8) | 16 | ± 1–2,5 kgf | matig |
| IMU (8) | 8 | ± 0,5–1 kgf | makkelijk |
| Barometer (6) | 6 | ± 0,3–1 kgf | makkelijk |
| Uitbreiding (8) | 8 | ± 0,5–1 kgf | makkelijk |

- Precisie-sockets zijn ontworpen voor **ronde** pinnen (± 0,5 mm); vierkante 2,54 mm-pinnen passen maar met meer kracht en slijtage → liefst ronde male pinheaders gebruiken.
- Geen echte klik; wrijving over de hele lengte.
- **Uitnemen is het gevaarlijkst**: afwisselend aan beide uiteinden wrikken, anders lost de socket of breekt de behuizing.
- Levensduur ± honderden tot 1000 cycli, maar door de hoge kracht sneller slijtage bij frequent wisselen.

**Werkwijze:** eerst module in de losse socket klikken, dan pas solderen; gelijke druk op de module met ondersteunde PCB; oriëntatie markeren; rekening houden met extra hoogte.

**Advies:** precisie-sockets voor zelden gewisselde modules (IMU, baro, GNSS); voor de vaak gewisselde ESP32-S3 een dual-wipe socket of connector overwegen. Mengen van beide types mag.

## Gerelateerd

- [[specificaties]] — draagprint-aanpak en heroverweging sockets
- [[pcb-schets]] — bovenaanzicht en verbindingsschema
- [[open-vragen]] — socket-headers vs. alternatief
