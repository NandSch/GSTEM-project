---
tags: [gstem, data, handleiding, documentatie, gebruikershandleiding]
aangemaakt: 2026-10-01
status: concept
---

# Gebruikershandleiding meettoestel

> [!info] Doel
> Een **Word-document** dat in eenvoudige taal uitlegt wat het meettoestel doet en hoe de
> gebruiker het opstart, de live data leest, eigen code toevoegt en het toestel aan een
> voertuigcontroller koppelt.

> [!info] Bron `2026-10-06`
> De door de gebruiker **afgewerkte specificaties** (`documenten/specificaties/GStem-Specificaties.md`, zie
> [gstem-specificaties](gstem-specificaties.md)) zijn de inhoudelijke basis voor de handleiding: de meetgrootheden en
> nauwkeurigheden, het automatisch aanzetten, de app-schermen (verbinding, kaart, Code, API) en de
> RC-vliegtuig-mock-up met Arduino via TX/RX en de drie besturingsvlakken.

## Bestanden

> [!warning] Niet meer aanwezig
> De onderstaande bestanden zijn bij commit `b16c501` (`2026-10-01`) uit `documenten/` verwijderd.
> Opnieuw genereren betekent: bron + script uit git terughalen. Zie [open-vragen](open-vragen.md).

| Rol | Pad |
| --- | --- |
| Markdown-bron (bewerk hier) | `documenten/Handleiding-meettoestel.md` *(verwijderd)* |
| Word-document | `documenten/Handleiding-meettoestel.docx` *(verwijderd)* |
| Bouwscript | `documenten/build-handleiding.py` *(verwijderd)* |

Opnieuw genereren: bron en script uit git terughalen en daarna `python documenten/build-handleiding.py`.

## Opbouw van het document

1. Inleiding: welke data het toestel meet (hoogte, positie, snelheid, richting, verticale hoek)
2. Toestel aanzetten en verbinden (aanzetten -> USB-ontvanger -> eerste scherm -> OK)
3. Tweede scherm: kaart en live data (3D-kaart met satellietfoto's + cijfertabel)
4. Codescherm: zelf besturing bepalen (editor, variabelen, uploaden)
5. Gegevens doorgeven aan een eigen programma
6. Meettoestel verbinden met de controller van het voertuig
7. Veiligheid en goede gewoontes
8. Gegevens bewaren
9. Startchecklist
10. Problemen oplossen
11. Technische gegevens
12. Woordenlijst
13. Extra onderdelen die nog kunnen worden toegevoegd

## Afspraken over de tekst

- Alles in **eenvoudige taal**, voor een gebruiker zonder technische voorkennis.
- **Geen CSV of andere technische protocolnamen** in de handleiding. In de sectie over besturing
  staat alleen dat de gebruiker **zelf een programma schrijft** (of een **voorbereid
  voorbeeldprogramma** gebruikt) en dat de meetmodule de stuurwaarden doorgeeft aan de controller.
- Overal staat expliciet een **SCREENSHOT**- of **AI-AFBEELDING**-blok: wat je moet vastleggen en
  waar het in het document komt. De AI maakt zelf geen schermafbeeldingen.

## Schrijfstijl

- Korte stukjes van één of twee zinnen.
- Veel witruimte en opsommingen, zodat het snel te lezen is.

## Werkpunten (nog niet gebouwd)

- [ ] **Route en meetgegevens opslaan als een bestand**, en dat bestand later **direct openen in de website**. Dit is bewust nog niet uitgewerkt; het staat in de handleiding als werkpunt en in [open-vragen](open-vragen.md).

## Nog in te voegen door de gebruiker

- [ ] SCREENSHOT 1 — overzicht van het toestel
- [ ] SCREENSHOT 2 — toestel aanzetten
- [ ] SCREENSHOT 3 — USB-ontvanger insteken
- [ ] SCREENSHOT 4 — eerste scherm (verbindingscontrole)
- [ ] SCREENSHOT 5 — volledig kaartscherm
- [ ] SCREENSHOT 6 — detail meetwaarden
- [ ] SCREENSHOT 7 — codescherm
- [ ] AI-AFBEELDING 1 — werking van de code (blokschema)
- [ ] AI-AFBEELDING 2 — gegevens doorgeven aan eigen programma
- [ ] AI-AFBEELDING 3 — connecties tussen de bordjes
- [ ] SCREENSHOT 8 — aansluiting op de controller
- [ ] SCREENSHOT 9 — veiligheid en testopstelling
- [ ] SCREENSHOT 10 — opgeslagen gegevens
- [ ] SCREENSHOT 11 — technische gegevens

## Gerelateerd

- [App-architectuur](app-architectuur-besturing.md) — de lagen die de handleiding vereenvoudigd beschrijft
- [Besturing en commando's](besturing-en-commandos.md) — de technische achtergrond (niet in de handleiding)
- [Meetmodule — voorbereiding](meetmodule-voorbereiding.md) — hardwarecontext
- [Specificaties](specificaties.md)
