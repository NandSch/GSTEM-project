---
name: gstem-archief
description: "G-Stem projectarchief en gebruikershub. Gebruik deze skill ALTIJD wanneer je in ~/Documents/GSTEM-Project werkt — de live logger schrijft GEBRUIKER/chat.md en jij houdt GEBRUIKER/onderwerpen.md en GEBRUIKER/data/ systematisch bij met beslissingen, specificaties, open vragen, links en afgevoerde opties."
---

# G-Stem archief & gebruikershub

> [!info] Altijd actief in dit project
> In `~/Documents/GSTEM-Project` geldt deze werkwijze bij **elke** sessie. De live logger
> (`.pi/extensions/gstem-logger.ts`) schrijft automatisch `GEBRUIKER/chat.md` en archiveert die
> bij het afsluiten van pi én bij de start van een nieuwe sessie. Jij (de AI) houdt
> `onderwerpen.md` en `data/` systematisch bij.

## Communicatie- en archiefhub

Alle relevante, besproken inhoud komt in de submap **`GEBRUIKER/`**:

```text
GEBRUIKER/
├── chat.md            # LIVE transcript van de huidige sessie (automatisch)
├── index.md           # hub / startpunt
├── onderwerpen.md     # register van besproken onderwerpen (MOC)
├── data/
│   ├── beslissingen.md
│   ├── specificaties.md
│   ├── open-vragen.md
│   ├── links.md
│   ├── afgevoerd.md    # opties die we ZEKER NIET gebruiken
│   └── <onderwerp>.md  # extra topic-notities (via /onderwerp)
└── archief/            # afgeronde sessies, elk met chat.md + meta.md
```

## Wat schrijf je waar?

| Soort informatie | Bestemming |
| --- | --- |
| Live gesprek | `GEBRUIKER/chat.md` — **automatisch**, jij hoeft dit niet te schrijven |
| Beslissing / keuze | `data/beslissingen.md` (chronologisch, met datum) |
| Specificatie / technische afspraak | `data/specificaties.md` |
| Open vraag / nog te beslissen | `data/open-vragen.md` |
| Nuttige link / bron / bestandspad | `data/links.md` |
| Optie die we **zeker niet** gebruiken | `data/afgevoerd.md` (kort, met reden) |
| Nieuw onderwerp in wording | `onderwerpen.md` + eventueel `data/<slug>.md` |

## Werkwijze per sessie

1. **Automatisch**: de logger schrijft elk gebruikersbericht (verbatim) en elk AI-antwoord
   (volledig, zonder denkproces) naar `chat.md`. Schrijf **nooit zelf** in `chat.md` — dat botst met
   de logger.
2. **Zodra een beslissing of specificiteit valt**: werk `onderwerpen.md` en het juiste bestand in
   `data/` bij. Voeg een onderwerp toe aan `onderwerpen.md` als het nog niet bestaat (wikilink
   `[[slug|Titel]]`).
3. **Meld kort in je antwoord** wat je hebt opgeslagen, bv.:
   `> [!info] Opgeslagen: beslissing → data/beslissingen.md` — dit komt zo in `chat.md` terecht.
4. **Filter**: bewaar alleen wat we effectief gaan gebruiken. Twijfelachtige of afgewezen opties
   gaan naar `data/afgevoerd.md`, niet naar de actieve bestanden.
5. **Bestaande documenten**: de mappen `docs/`, `CODEXIMPORT/` en `GSTEMAPPPREVIEWWEB/` blijven
   zoals ze zijn. Haal ze alleen op wanneer de gebruiker ze relevant noemt.

## Opmaak (Obsidian)

- **Geen emoji's** in je antwoorden of in de archiefbestanden (dus ook niet in `chat.md`,
  `onderwerpen.md` of `data/`). Gebruik in plaats daarvan tekstlabels zoals `Let op:` of `Klaar.`
- **YAML-frontmatter** met `tags`, `datum`/`aangemaakt` waar zinvol.
- **Callouts**: `> [!info]`, `> [!question]`, `> [!warning]`, `> [!example]-` (inklapbaar).
- **Wikilinks**: `[[onderwerpen]]`, `[[beslissingen]]`, `[[specificaties]]`.
- **Checkboxes** voor open acties: `- [ ] ...`.
- Alles in het **Nederlands**.

## Commando's

| Commando | Werking |
| --- | --- |
| `/archiveer` | Archiveert `chat.md` nu naar `archief/<JJJJ-MM-DD_UUMM_slug>/` en begint een verse log. |
| `/logboek` | Toont het huidige `chat.md`. |
| `/onderwerp <naam>` | Maakt `data/<slug>.md` en koppelt het onderwerp in `onderwerpen.md`. |

## Formaat van `data/`-bestanden

Gebruik per item een gedateerde subsectie, nieuwste onderaan (append-only):

```markdown
## 2026-09-29 — Korte titel
- **Beslissing:** ...
- **Reden:** ...
- **Gevolg:** ...
```

Zie `references/templates.md` in deze skillmap voor volledige sjablonen.
