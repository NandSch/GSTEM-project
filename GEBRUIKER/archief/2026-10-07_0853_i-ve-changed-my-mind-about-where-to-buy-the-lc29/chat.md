---
tags: [gstem, chatlog]
sessie: "01a11523-5f94-73cb-ba13-ee11fb6d2827"
gestart: 2026-10-07T06:53:23.226Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a11523-5f94-73cb-ba13-ee11fb6d2827` · gestart 2026-10-07_0853
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 08:54

> [!quote] Verbatim
> I've changed my mind about where to buy the LC29H from. Let's do china, aliexpress preferably. Check that it's the right board for the job, eg DA board or something, I don't remmember.?

## AI · 09:01

## Juiste variant

Ja: voor ons toestel is **Quectel LC29HDA** de juiste variant — dat is de **RTK-rover**. `DA` hoort bij de modulevariant; het is hier geen D/A-converterbord. Vermijd **LC29HBS**: dat is de basisstationvariant. De rover heeft RTCM-correcties nodig via onze geplande NTRIP/laptop/LoRa-route om RTK-nauwkeurigheid te halen.

De AliExpress-resultaten zijn verwarrend: sommige advertenties noemen “base station” terwijl ze ook LC29HDA vermelden. Ik kan daarom nog geen specifieke advertentie of verkoper veilig aanbevelen. [Hier staat de AliExpress-zoekopdracht](https://www.aliexpress.com/wholesale?SearchText=Quectel+LC29HDA+RTK+rover+board), maar dat is **geen geverifieerde productlisting**.

Koop alleen een **geassembleerde breakout/development board**, geen losse SMD-module. Controleer bij een kandidaat ook UART TX/RX, 5V-voeding, 3,3V-compatibele logicaniveaus, antenne en connector, afmetingen en retourvoorwaarden.

De Waveshare LC29H(DA) HAT bij Eckstein blijft als terugvaloptie technisch geschikt. Hij heeft UART/I²C en een meegeleverde dual-bandantenne, maar is met **65 × 30,5 mm en een 40-pins header** vrij groot voor onze draagprint. De antenne en afmetingen daarvan gelden niet automatisch voor AliExpress-boards. [Waveshare-variantinformatie](https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT).

> [!info] Opgeslagen
> De aankoopvoorkeur is gewijzigd naar China, liefst AliExpress. De LC29HDA-rover blijft de technische keuze; de exacte listing, antennebundel en footprint staan nog open. Bijgewerkt in [[beslissingen]], [[gps-rtk-prijzen]], [[bestellijst]], [[open-vragen]], [[links]] en de Excel-bestellijst.

---

## Gebruiker · 09:02

> [!quote] Verbatim
> Zoek naar een link naar de module op aliexpress.

## AI · 09:07

Ik heb een concrete kandidaat gevonden: [AliExpress — Quectel LC29HDA Dual-Frequency RTK Mobile Station GNSS Board Kit](https://www.aliexpress.com/item/1005010036256167.html) — item **1005010036256167**.

De geïndexeerde titel noemt **LC29HDA**, **Mobile Station** (rover) en **Board Kit**, dus dit is de beste match die ik vond. Ik kon de productpagina zelf niet uitlezen: AliExpress vroeg om een sliderverificatie. **Beschouw dit daarom als een kandidaat, niet als een volledig gecontroleerde kooplink.**

Controleer vóór bestellen dat de gekozen optie echt **LC29HDA** is, dat je een **gemonteerd board** krijgt en niet alleen de losse module, en dat UART, voeding, pinout en antenne-aansluitingen passen. De “dual antenna”-bundel moet ook verduidelijkt worden. Vermijd de **LC29HBS**-basisstationvariant; de [Waveshare-variantbeschrijving](https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT) onderscheidt die van de DA-rover.

> [!info] Opgeslagen
> De kandidaatlink en de resterende controles staan in [[gps-rtk-prijzen]], [[bestellijst]], [[open-vragen]] en [[links]]. De Excel-bestellijst is bijgewerkt; prijs en listingdetails blijven nog te verifiëren.

---

## Gebruiker · 09:09

> [!quote] Verbatim
> update excel.

## AI · 09:09

Bijgewerkt en opnieuw opgebouwd: `documenten/beheer/Bestellijst-GSTEM.xlsx`.

De LC29HDA-regel linkt nu naar [AliExpress-item 1005010036256167](https://www.aliexpress.com/item/1005010036256167.html), met status **onderzoek**. De prijs blijft leeg omdat ik de listingdetails en prijs nog niet onafhankelijk kon controleren. De antenne staat ook op **onderzoek** totdat we weten wat de aanbieding meelevert.

---
