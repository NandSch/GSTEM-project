---
tags: [gstem, data, webdemo, code-pagina, handleiding]
aangemaakt: 2026-10-05
status: vervangen (2026-10-10)
---

# Handleiding — de Code-pagina van de webdemo

> [!warning] Vervangen per `2026-10-10`
> De herziene specificaties (pdf, `2026-10-10`) hebben **geen code-pagina en geen API-pagina**
> meer: scherm 3 is nu een **Besturing**-menu met voertuigspecifieke besturings-apps (bijv. auto
> met stuur en gaspedaal) en scherm 4 is zo'n besturingspagina. Deze handleiding beschrijft de
> oude webdemo en blijft alleen als historische naslag bestaan.

> [!info] Doel
> Deze handleiding beschrijft **elk onderdeel** van de Code-pagina en **wat het doet**. Ze hoort bij
> de webdemo (`GSTEMAPPPREVIEWWEB/`) en bij de A/B-uitkomst in [ab-test-code-pagina](ab-test-code-pagina.md). Gemaakt op
> verzoek van de gebruiker.

## Waar zit de pagina?

| Rol | Pad |
| --- | --- |
| Pagina (officieel) | `GSTEMAPPPREVIEWWEB/index.html` -> sectie `#page-code` |
| Stijl | `GSTEMAPPPREVIEWWEB/style.css` |
| Scripts/logica | in `index.html` (onderaan, vanaf ca. regel 632) |

Starten: `python -m http.server 8080` in `GSTEMAPPPREVIEWWEB`, dan `http://localhost:8080/#page-code`.
Met `?embed=1` wordt de setup-popup overgeslagen.

> [!note] Wat de pagina in één zin is
> Een **codevenster** waarin de leerling zelf een klein Arduino-programma schrijft. De meetmodule
> voert dat uit en print zelf de stuurregel die naar de voertuigcontroller gaat.

## Bouwstenen van de pagina (van boven naar onder)

### 1. Navigatiebalk

- Drie links: **Kaart** (`#page-kaart`), **Code** (`#page-code`), **API** (`#page-api`).
- Functie: wisselen tussen de schermen van de app. Het actieve scherm krijgt de klasse `active`.
- Links daarnaast twee **statusvakjes**: `USB` en `Device` (zie punt 2).

### 2. Statusvakjes USB en Device

- Twee afgevinkte checkboxen (`#nav-usb-checkbox`, `#nav-device-checkbox`), uitgeschakeld en
  automatisch gezet.
- Functie: tonen of de **USB-ontvanger** en het **meettoestel** verbonden zijn.
- Ze zijn read-only: de gebruiker kan ze niet met de hand aanpassen.

### 3. Setup-popup (verschijnt bij het opstarten)

- Overscherm met titel **Setup** en de statusregel *"Verbinding maken met de hardware…"*.
- Zelfde twee statusvakjes (`USB-ontvanger`, `Meettoestel`) en een knop **OK**.
- Functie: de gebruiker laten bevestigen zodra beide verbindingen klaar zijn; daarna sluit de popup.
- Laad je met `?embed=1`, dan blijft deze popup weg.

### 4. Het codevenster

Eén kolom, gecentreerd (max. 1060 px). Bestaat uit vier delen:

**4a. Titelbalk**
- Drie bolletjes (rood/oranje/groen): puur decoratief, ziet eruit als een editorvenster.
- `missie.ino` — de bestandsnaam van het programma.
- `Arduino C++` — de taal waarin gewerkt wordt.
- `Ctrl` + `Enter` — een hint dat je met dat toetsenpaar direct kan uploaden.

**4b. Knop Uploaden** (`#upload-btn`)
- Functie: de geschreven code naar de meetmodule sturen.
- Staat **uit** zolang de editor leeg is, en **aan** zodra er code staat.
- Klik of druk `Ctrl` + `Enter` roept `uploadCode()` aan.
- In de demo verschijnt een melding: *"Code geupload. Jouw code print de CSV-regels zelf met
  Serial.println(). De module stuurt elke regel ongewijzigd door naar de voertuigcontroller."*

**4c. Editor** (`#code-editor`)
- Een groot tekstvak met als plaatshouder *"Typ hier uw Arduino-code..."*.
- Spellingcontrole en automatisch aanvullen staan uit, zodat code netjes blijft.
- Bij het openen staat er al een **startcode** in (11 regels): een `void loop()` die de hoogte
  vergelijkt met 125.0 en dan ofwel `Serial.println("15,-5,75,60");` ofwel `"0,0,50,50"` print,
  gevolgd door `delay(100)`.

**4d. Statusbalk** (onder de editor)
- `#code-lines` — aantal regels, bv. "11 regels".
- `#code-chars` — aantal tekens.
- Functie: live meestellen terwijl je typt (functie `updateCodeStats()`).

### 5. Uitklapbare hulp (standaard dicht)

Twee blokken (`<details>`) onder het codevenster, zodat het scherm rustig blijft.

**5a. Wat kan ik gebruiken?**
- Compacte lijst van de live waarden die je in je code kan uitlezen:

| Waarde | Eenheid |
| --- | --- |
| `meting.hoogte` | m |
| `meting.snelheid` | km/u |
| `meting.horizontaleSnelheid` | m/s |
| `meting.verticaleSnelheid` | m/s (+ omhoog) |
| `meting.richting` | graden |
| `meting.verticaleHoek` | graden |
| `meting.breedtegraad` | graden |
| `meting.lengtegraad` | graden |

**5b. Hoe stuur ik iets?**
- Eén voorbeeldregel: `Serial.println("15,-5,75,60");`
- Uitleg: *"Print zelf een regel met kommagescheiden waarden. Jij kiest wat elk cijfer betekent."*
- Noot: *"Eén regel per keer, altijd afsluiten met een newline."*

## Wat de onderliggende functies doen

| Functie / stukje | Functie |
| --- | --- |
| `setActive()` | Leest het `#hash` uit de URL en zet het juiste scherm + de juiste nav-knop op `active`. |
| `updateCodeStats()` | Telt regels en tekens en zet de Uploaden-knop aan/uit. |
| `keydown`-luisteraar op de editor | Vangt `Ctrl` (of `Cmd`) + `Enter` op en start `uploadCode()`. |
| `uploadCode()` | Controleert of er code is; leeg -> melding "Voer eerst code in.". Anders de demo-bevestiging dat de module de CSV-regels doorstuurt. |
| `closePopup()` | Sluit de setup-popup met een korte animatie. |
| `?embed=1` | Onderdrukt de setup-popup (gebruikt bij vergelijkingsframes). |

## Kort samengevat — wat doet welk deel?

- **Navigatie:** van scherm wisselen (Kaart / Code / API).
- **USB- en Device-vakjes:** tonen of de hardware verbonden is.
- **Titelbalk:** bestandsnaam, taal en de upload-sneltoets.
- **Uploaden:** de code naar de module sturen.
- **Editor:** hier schrijf je het programma.
- **Statusbalk:** aantal regels en tekens.
- **Wat kan ik gebruiken?:** welke meetwaarden je kan uitlezen.
- **Hoe stuur ik iets?:** hoe je zelf een stuurregel print.

## Gerelateerd

- [A/B-test: Code-pagina herzien](ab-test-code-pagina.md) — hoe versie B de officiële werd
- [Specificaties](specificaties.md)
- [App-architectuur](app-architectuur-besturing.md) — waar de code-modus in de keten past
- [Besturing en commando's](besturing-en-commandos.md)
