# Sjablonen voor de GEBRUIKER-hub

## `chat.md` (automatisch beheerd — niet handmatig bewerken)

```markdown
---
tags: [gstem, chatlog]
sessie: "<session-id>"
gestart: <ISO-datum>
---

# Live chat — huidige sessie

## 🧑 Gebruiker · HH:MM

> [!quote] Verbatim
> <jouw bericht>

## 🤖 AI · HH:MM

<volledig antwoord, zonder denkproces>

---
```

## `onderwerpen.md`

```markdown
---
tags: [gstem, moc]
---

# Onderwerpen

- [[beslissingen|Beslissingen en keuzes]]
- [[specificaties|Specificaties]]
- [[open-vragen|Open vragen]]
- [[afgevoerd|Afgevoerde opties]]
```

## `data/beslissingen.md`

```markdown
---
tags: [gstem, data, beslissingen]
---

# Beslissingen en keuzes

## <JJJJ-MM-DD> — <korte titel>
- **Beslissing:** ...
- **Reden:** ...
- **Gevolg:** ...
```

## `data/specificaties.md`

```markdown
---
tags: [gstem, data, specificaties]
---

# Specificaties

## <JJJJ-MM-DD> — <onderdeel>
- **Specificatie:** ...
- **Status:** voorlopig / vastgelegd
- **Bron:** ...
```

## `data/open-vragen.md`

```markdown
---
tags: [gstem, data, open-vragen]
---

# Open vragen

- [ ] **<vraag>** — context: ... (sinds <JJJJ-MM-DD>)
- [x] **<vraag>** — beantwoord op <JJJJ-MM-DD>: ...
```

## `data/links.md`

```markdown
---
tags: [gstem, data, links]
---

# Links en bronnen

| Onderwerp | Link | Notitie |
| --- | --- | --- |
| ... | ... | ... |
```

## `data/afgevoerd.md`

> [!warning] Alleen opties die we **zeker niet** gebruiken, met reden.
> Zo weten we later waarom iets is afgevallen, zonder de actieve bestanden te vervuilen.

```markdown
---
tags: [gstem, data, afgevoerd]
---

# Afgevoerde opties

## <JJJJ-MM-DD> — <optie>
- **Reden afvoer:** ...
- **Eventueel later opnieuw bekijken?** nee / misschien
```

## `data/<onderwerp>.md` (via `/onderwerp`)

```markdown
---
tags: [gstem, onderwerp]
onderwerp: "<naam>"
aangemaakt: <ISO-datum>
---

# <naam>

## Achtergrond
...

## Beslissingen / specificaties
...

## Open vragen
- [ ] ...
```

## `archief/<JJJJ-MM-DD_UUMM_slug>/meta.md`

```markdown
---
tags: [gstem, chatarchief]
sessie: "<session-id>"
gestart: <ISO>
gearchiveerd: <ISO>
berichten: <aantal>
---

# Sessie <JJJJ-MM-DD_UUMM_slug>

## Onderwerpen
- [[slug|Titel]]

Volledig transcript: `chat.md` in deze map.
```
