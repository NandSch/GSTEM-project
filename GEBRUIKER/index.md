---
tags: [gstem, hub]
---

# GEBRUIKER — hub

Startpunt van de communicatie- en archiefhub van het G-Stem-project.

## Nu

- [[chat]] — live transcript van de huidige sessie

## Overzicht

- [[onderwerpen]] — register van besproken onderwerpen
- [[beslissingen]] — genomen beslissingen en keuzes
- [[specificaties]] — technische en functionele afspraken
- [[open-vragen]] — wat nog te beslissen valt
- [[links]] — bronnen, links en bestandspaden
- [[afgevoerd]] — opties die we zeker niet gebruiken

## Archief

- [[archief/README|Sessiearchief]] — elke afgeronde sessie met `chat.md` + `meta.md`

## Afspraken

- De **live logger** schrijft automatisch `chat.md` (gebruikersberichten verbatim, AI-antwoorden
  volledig, zonder denkproces; geen tool-calls).
- Zodra je pi **afsluit** of een **nieuwe sessie** start, wordt de vorige `chat.md` verplaatst naar
  `archief/<JJJJ-MM-DD_UUMM_slug>/` met een `meta.md`.
- Commando's: `/archiveer`, `/logboek`, `/onderwerp <naam>`.
