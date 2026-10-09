# Werkinstructies voor AI-assistenten in deze map

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
