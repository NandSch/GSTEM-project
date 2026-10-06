---
tags: [gstem, chatlog]
sessie: "01a112a6-8fe5-74c6-95f1-ccb3dc11a007"
gestart: 2026-10-06T19:17:48.275Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a112a6-8fe5-74c6-95f1-ccb3dc11a007` · gestart 2026-10-06_2117
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 21:18

> [!quote] Verbatim
> Reorganize everything in C:\Users\Nand Schoovaerts\Documents\GSTEM-Project\documenten

## AI · 21:18

Ik heb de map in kaart gebracht. Voor ik verplaats (dat breekt anders tientallen padverwijzingen in `GEBRUIKER/data/` en `docs/`), twee keuzes:

---

## AI · 21:21

Klaar. `documenten/` is herschikt in vier submappen, alle actieve verwijzingen zijn bijgewerkt en de scripts werken vanuit hun nieuwe locatie.

## Nieuwe structuur

```text
documenten/
├── README.md                         # nieuwe index
├── specificaties/                    # GStem-Specificaties.md, Ontwerp-meetmodule.md + .docx
├── pcb/                              # PCB-schets.md, draagprint-SVG/PNG, PCB-eindbeeld.png,
│                                     # Communicatie-overzicht-GSTEM.drawio, review-mockup-controleblad.png
├── beheer/                           # Bestellijst-GSTEM.xlsx, Planning-GSTEM.xlsx
└── scripts/                          # build-bestellijst / -communicatie-overzicht / -controleblad / -pcb-eindbeeld
```

## Wat ik deed

- **Verplaatst** met `git mv` (historiek en rename-detectie behouden); de twee untracked bestanden (`Communicatie-overzicht-GSTEM.drawio`, `build-communicatie-overzicht.py`) met `mv`.
- **Opgeruimd**: `documenten/.pi/` (restconfig) en `documenten/__pycache__/` verwijderd.
- **Blender verwijderd gelaten** volgens je keuze; de map blijft herstelbaar via `git checkout 28e4fae -- documenten/blender`.
- **Scripts padonafhankelijk gemaakt** via `__file__`. Getest: `build-communicatie-overzicht.py`, `build-bestellijst.py` en `build-pcb-eindbeeld.py` draaien en schrijven naar de juiste submap. `build-pcb-eindbeeld.py` had een kapot hardgecodeerd pad (`NandSchoovaerts`, zonder spatie) — ook hersteld. `build-controleblad.py` is enkel syntax-gecontroleerd: het kan pas opnieuw draaien als de Blender-review-renders terugkomen.
- **Verwijzingen bijgewerkt** in `docs/`, `GEBRUIKER/Projectdocumentatie/`, `GEBRUIKER/data/`, `GEBRUIKER/onderwerpen.md` en `README.md` (19 bestanden). Archief-chatlogs zijn bewust niet aangepast.
- `docs/` en `GEBRUIKER/Projectdocumentatie/` zijn opnieuw identiek.

## Vastgesteld in de hub

> [!info] Opgeslagen
> Beslissingen → `data/beslissingen.md` (herschikking `documenten/` en verwijdering Blender-mock-up); afvoer → `data/afgevoerd.md` (Blender-mock-up); status bijgewerkt → `data/blender-mockup.md`; index → `data/links.md`; en twee nieuwe punten in `data/open-vragen.md`.

Let op (open vragen die ik tegenkwam): `data/handleiding.md`, `links.md` en `specificaties.md` verwezen nog naar de gebruikershandleiding en `build-ontwerp.py`, maar die bestanden zijn al op `2026-10-01` (commit `b16c501`) verdwenen. Ik heb ze als "verwijderd" gemarkeerd en de vraag "opnieuw genereren of opruimen?" in `open-vragen.md` gezet. De nieuwe bestanden (`documenten/README.md`, drawio en diens script) staan nog untracked; ik heb niets gecommit.

---
