# Werkinstructies voor AI-assistenten in deze map

Deze afspraken gelden voor elke AI-assistent (Codex of anders) die in deze map werkt.
Het doel: het project blijft ook zonder de oude pi-hulpmiddelen volledig en correct
gedocumenteerd.

## Alles correct documenteren

- Elke wijziging met betekenis voor het project (code, ontwerp, documenten, bestellijst,
  planning, werkwijze) wordt bij het maken ervan vastgelegd in de juiste kennisbestanden
  in `GEBRUIKER/data/` en, als het de afgewerkte stukken raakt, ook in `documenten/`
  of `docs/`.
- Werk de bestanden die een wijziging raakt **meteen bij**, niet "later wel". Een
  beslissing die alleen in een chatlog bestaat, is verloren.
- Nieuwe kennis gaat in het bestaande kennisbestand dat er het dichtst bij staat
  (componenten, bestellijst, open-vragen, ...); maak alleen een nieuw bestand als er
  echt geen past. Vergeet niet de betrokken bestanden naar elkaar te laten verwijzen.
- Laat geen losse einden achter: dode links, verouderde tabellen of statussen die niet
  meer kloppen worden bij dezelfde wijziging gecorrigeerd.
- Word-versies (`.docx`) en Excel-bestanden (`xlsx`) in `documenten/` worden gebouwd uit
  de markdown-bronnen met de scripts in `documenten/scripts/`; pas de bron aan en bouw
  opnieuw, pas niet alleen het binaire bestand aan.

## Beslissingen documenteren

**Elke projectbeslissing** (ontwerp, componenten, aankopen, architectuur, documentatie of
werkwijze) wordt direct vastgelegd in `GEBRUIKER/data/beslissingen.md`, onderaan, in dit
formaat:

```markdown
## JJJJ-MM-DD — Korte titel
- **Beslissing:** wat er is besloten.
- **Reden:** waarom.
- **Gevolg:** wat dit betekent voor andere onderdelen.
- **Link:** [gerelateerd-bestand](gerelateerd-bestand.md), ...
```

Regels daarbij:

- Eén sectie per beslissing, chronologisch (nieuwste onderaan), zonder emoji's.
- Ook besluiten die *niets* worden (afgewezen opties) horen thuis in
  `GEBRUIKER/data/afgevoerd.md`, zelfde formaat.
- Gebruik gewone markdown-links `[tekst](bestand.md)`, geen `[[wikilinks]]`.
- Verwijs met de Link-regel naar de kennisbestanden die door de beslissing veranderen, en
  werk die bestanden zelf ook bij zodat ze consistent blijven met de beslissing.
- Gebeurtenissen die geen beslissing zijn (vragen, tussenstand, losse bevindingen) horen
  niet in `beslissingen.md`; open punten gaan naar `GEBRUIKER/data/open-vragen.md`.
