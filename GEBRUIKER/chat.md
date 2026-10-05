---
tags: [gstem, chatlog]
sessie: "01a10d8f-a2d1-7321-8c4f-260aceceeb67"
gestart: 2026-10-05T19:34:42.336Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a10d8f-a2d1-7321-8c4f-260aceceeb67` · gestart 2026-10-05_2134
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 21:37

> [!quote] Verbatim
> Ik wil alles in deze folder herschikken. Alle data uit coddeximport en hoe de webdemo werking in elkaar zit moet ergens genoteerd zijn en mogen dan zelf verwijderd worden aangezien ze te veel opslag innemen.

## AI · 21:37

Ik begin met het lezen van de skill en het verkennen van de projectstructuur.

---

## AI · 21:37

Ik heb de structuur in kaart gebracht. Belangrijke bevindingen voordat ik iets verwijder:

- **Documentatie bestaat al grotendeels**: `docs/02-codeximport.md` + `docs/03-gstemapppreviewweb.md` beschrijven beide mappen volledig, en `GEBRUIKER/Projectdocumentatie/` is daar een **nieuwere kopie** van (de versie daar kent de API-pagina en het nieuwe code-ontwerp; `docs/03` is verouderd).
- **Echte opslagslurpers zijn niet deze twee mappen**: `CODEXIMPORT` = 264 KB, `GSTEMAPPPREVIEWWEB` = 277 KB, maar `documenten/` = **29 MB** (vooral `.docx.bak-*`-back-ups van ~19 MB + afbeeldingen 9,7 MB).
- Alles is gecommit in git ("Begin GIT"), dus verwijderen is herstelbaar zolang we dat niet wissen.

Voordat ik wis, wil ik zeker weten wat weg mag.

---

## AI · 21:39

Duidelijk. Ik maak een plan en voer het uit.

---
