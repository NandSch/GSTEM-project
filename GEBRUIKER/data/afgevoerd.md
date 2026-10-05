---
tags: [gstem, data, afgevoerd]
---

# Afgevoerde opties

> [!warning] Alleen opties die we **zeker niet** gebruiken, met reden.

<!-- Voorbeeld:
## 2026-09-29 — Optie X
- **Reden afvoer:** ...
- **Later opnieuw bekijken?** nee
-->

## 2026-10-04 — Vaste uitgangsvariabelen op de code-pagina
- **Wat:** Vooraf ingestelde uitgangen zoals `uit.servo1`, `uit.servo2`, `uit.motorLinks`, `uit.motorRechts`, `uit.throttle` en `uit.modus`, die de app automatisch naar CSV omzet.
- **Reden afvoer:** Gebruikersvraag: geen vooraf bepaald servo-/uitgangsschema. De gebruiker schrijft zelf de CSV-regel in de code, zodat eender welk toestel of veldindeling mogelijk is.
- **Later opnieuw bekijken?** nee — de vrije CSV-regel vervangt dit bewust.

## 2026-10-05 — Ziparchieven en .bak-docx als permanente back-up
- **Wat:** De ziparchieven in `archief/` en de `.docx.bak-*`-tussenversies in `documenten/` als back-up bewaren.
- **Reden afvoer:** Dubbel werk: de mappen stonden ook als bestanden in de repo (git) en de ziparchieven dupliceerden die. De `.bak`-bestanden waren slechts tussenversies. Git bewaart de volledige historiek.
- **Later opnieuw bekijken?** nee — de documentatie en git zijn de back-up.

## 2026-10-04 — Tweekoloms Code-pagina met variabelenkaarten (versie A)
- **Wat:** De Code-pagina met links de editor en rechts een rechterkolom vol variabelenkaarten, CSV-groep en uploadvoettekst.
- **Reden afvoer:** Gebruikersvraag: versie B (één kolom met uitklapbare hulp) is rustiger en duidelijker en werd de officiële versie.
- **Later opnieuw bekijken?** nee — de één-kolomsopzet is definitief.
