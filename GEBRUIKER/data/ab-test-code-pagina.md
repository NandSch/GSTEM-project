---
tags: [gstem, data, ab-test, webdemo, code-pagina]
aangemaakt: 2026-10-04
status: afgerond
---

# A/B-test: Code-pagina herzien

> [!info] Doel
> Twee versies van de **Code-pagina** naast elkaar leggen en kiezen welke het duidelijkst is,
> zonder rommel.

## Bestanden

| Rol | Pad |
| --- | --- |
| Versie A (oud) | tweekoloms Code-pagina — **verwijderd** |
| Versie B (officieel) | `GSTEMAPPPREVIEWWEB/index.html` -> `#page-code` |
| Stijl | `GSTEMAPPPREVIEWWEB/style.css` |

Starten: `python -m http.server 8080` in `GSTEMAPPPREVIEWWEB`, dan `http://localhost:8080/`
(`#page-code`).

## Versie A

- Twee kolommen: links de editor, rechts een rechterkolom met **Variabelen** (8 kaarten) en de
  groep **Zelf de CSV-regel schrijven**, plus de uploadvoettekst.
- Veel informatie in één beeld.

## Versie B

- **Eén kolom**, gecentreerd, max. 1060 px. Rustig en overzichtelijk.
- **Uploaden** staat in de titelbalk van het codevenster, naast `Ctrl`+`Enter`.
- **Uitklapbare hulp** (standaard dicht, dus weinig plaats):
  - **Wat kan ik gebruiken?** — compacte lijst van `meting.*` met eenheid, in twee kolommen.
  - **Hoe stuur ik iets?** — één voorbeeldregel `Serial.println("15,-5,75,60");` en één uitleg.
- **Startcode** is minimaal (11 regels).

## Afspraken

- De uitklapbare uitleg blijft **kort**: enkel wat nodig is om te begrijpen en te gebruiken.
- Beide versies laden met `?embed=1`, zodat de setup-popup niet verschijnt in de vergelijkingsframes.
- API en Kaart blijven in beide versies hetzelfde.

## Uitkomst

Versie **B** is op `2026-10-04` de **officiële** Code-pagina geworden en staat nu in
`GSTEMAPPPREVIEWWEB/index.html`. De bestanden `index-b.html` en `ab-vergelijken.html` zijn
verwijderd. Zie [[beslissingen]] en [[specificaties]].

## Te beslissen

- [x] Welke versie wordt de definitieve Code-pagina: **B** (één kolom met uitklapbare hulp).
