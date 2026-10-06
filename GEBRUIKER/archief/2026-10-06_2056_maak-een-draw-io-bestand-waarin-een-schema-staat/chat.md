---
tags: [gstem, chatlog]
sessie: "01a11292-9378-74c6-95f1-ccad14b04f7b"
gestart: 2026-10-06T18:56:02.303Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11292-9378-74c6-95f1-ccad14b04f7b` · gestart 2026-10-06_2056
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 20:56

> [!quote] Verbatim
> Maak een draw.io bestand waarin een schema staat van alle componenten en hoe ze met elkaar communiceren inclusief laptop en arduino uno.

## AI · 20:56

Ik lees eerst de skill en verken het project zodat het schema klopt met jullie architectuur.

---

## AI · 20:57

Ik heb genoeg context. Ik maak een communicatiegericht schema (alle componenten + hoe ze met elkaar praten), als draw.io mét bouwsript en PNG, in dezelfde stijl als het bestaande verbindingsschema.

---

## AI · 20:57

Het schema staat er. Twee kleine correcties (label liep over de laptopkolom en een typo in de ondertitel):

---

## AI · 20:57

Schema klopt. Nu het archief bijwerken.

---

## AI · 20:57

Klaar. Ik heb een communicatieschema gemaakt met alle componenten en hoe ze met elkaar praten.

**Nieuwe bestanden**
- `documenten/Communicatieschema-GSTEM.drawio` — bewerkbaar in draw.io / app.diagrams.net
- `documenten/Communicatieschema-GSTEM.png` — afbeelding (3240 x 2360)
- `documenten/build-communicatieschema.py` — bouwsript: `python documenten/build-communicatieschema.py`

**Wat staat erop**
- **Laptopzijde:** NTRIP-dienst, laptopapplicatie (kaart + Code + API), extern programma, LoRa-ontvanger/USB-stick (2e XIAO-kit)
- **Meetmodule:** XIAO ESP32S3 + Wio-SX1262, BNO085 (I2C), BMP581 (I2C), LC29H(DA) RTK-GNSS (UART), LoRa- en GNSS-antenne
- **Mock-up:** TXB0104 level shifter → J2 uitbreidingsconnector → **Arduino Uno** → 3 servo's + servo-BEC
- **Communicatie per kleur:** blauw = I2C, groen = UART, paars = RF (LoRa/GNSS), donkergroen = NTRIP/internet, zwart = USB/serieel, bruin = PWM
- **Voedingsband onderaan** (accu → PTC/TVS → buck 5 V → LDO 3,3 V), met verwijzing voor het detail

> [!info] Opgeslagen: `data/communicatieschema.md` (nieuw topic), `data/links.md` (paden), `data/verbindingsschema.md` (kruisverwijzing), `onderwerpen.md` (register).

Let op: het schema blijft schematisch; CSV-formaat en NTRIP-provider staan er expliciet als "nog open". Het detail van de voeding/GND blijft in `Verbindingsschema-GSTEM.drawio`.

---
