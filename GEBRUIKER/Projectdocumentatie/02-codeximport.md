# 02 · Map `CODEXIMPORT` — inventaris en uitleg

Oorspronkelijke locatie: `C:\Users\Nand Schoovaerts\Documents\ChatGPT\G-Stem Project`.
Gekopieerd naar: `CODEXIMPORT/` (zonder het niet-gerelateerde Negau B-helm-materiaal).

Dit is de **documenten- en generator-map** die via Codex/ChatGPT is opgebouwd voor het
G-Stem/GSN-project.

## Git-geschiedenis

```text
aac45cd  Refresh G-Stem prototype with light editor layout   (laatste commit)
672714b  Add G-Stem visual app prototype and project context
```

Branch: `master`. Alleen `PROJECT_CONTEXT.md` en `visual-prototype/index.html` zijn gevolgd door
Git; de andere bestanden in de map zijn untracked. De Git-objectendatabase is opgeschoond
(`git gc --prune=now`), zodat de map nu ±267 KB groot is.

## Bestandsinventaris

| Bestand | Type | Beschrijving |
| --- | --- | --- |
| `PROJECT_CONTEXT.md` | Markdown | Oriëntatiedocument voor vervolgchats: doel, status, meetmodule, softwareketen, appflow, open vragen. |
| `G-Stem_specificaties_concept.docx` | Word | Concept-specificaties hardware en software in korte punten. |
| `GSN-project_draadloze_3D-meetmodule.docx` | Word | Opdrachtomschrijving + blokschema (gegenereerd door `create_gsn_document.py`). |
| `Blokschema_AeroLink.drawio` | diagrams.net | Blokschema van de volledige keten (zie `04-blokschema-aerolink.md`). |
| `create_gsn_document.py` | Python | Genereert `GSN-project_draadloze_3D-meetmodule.docx` met `python-docx`. |
| `visual-prototype/index.html` | HTML | Oud zelfstandig visueel prototype van de laptopapp (fictieve waarden). |
| `.git/` | Git | Repositoryhistoriek (opgeschoond). |

## `create_gsn_document.py`

Genereert het Word-document `GSN-project_draadloze_3D-meetmodule.docx` met `python-docx`.
- Stelt marges, het lettertype *Aptos* en een blauwe titelstijl in.
- Secties: **Opdrachtomschrijving**, **Blokschema** (3×5-tabel met gekleurde cellen:
  `GPS-RTK/Barometer/IMU → Microcontroller+LoRa → LoRa-ontvanger/Laptop`, met daaronder
  `Tweede microcontroller → 2 servo's / vliegtuig-mock-up`), en **Doel**.
- Hulpfuncties `shade()` en `borders()` voor celopmaak.

> Let op: hardgecodeerd uitvoerpad is `GSN-project_draadloze_3D-meetmodule.docx` naast het script.

## `visual-prototype/index.html` (oud prototype)

Eén zelfstandig HTML-bestand (geen externe afhankelijkheden) van ±110 regels. Dit is de eerste
mock-up; de nieuwere, werkende versie staat in `GSTEMAPPPREVIEWWEB/`.

- **Startscherm** dat USB- en LoRa-controles *simuleert*; knop "Open demonstratie".
- **Livekaart**: getekende SVG-terreinvisualisatie rond **Spa, België** (met labels SPA, Lac de
  Warfaaz, Bois de la Heid, Route de Barisart), een rode voorbeeldroute, een richtingspijl en een
  "MEETMODULE"-marker. Geen echte kaartdienst.
- **Live meetwaarden**: breedtegraad 50.49606°, lengtegraad 5.85614°, hoogte 284.6 m, snelheid
  12.8 km/u, oriëntatie (roll −2.4°, pitch +1.8°, yaw 038°), plus verbindingspaneel
  (USB, LoRa, −67 dBm, 12 Hz / 84 ms).
- **Programmering & besturing**: grote code-editor met illustratieve voorbeeldcode in
  pseudocode-achtige `besturing.gstem`-syntax (RC-auto, helling > 12 graden → snelheid
  verminderen). Geen uitvoering of voertuigbesturing.
- Vormgeving later omgezet naar **wit/grijs**, met het terrein als enige gekleurde vlak.

## `G-Stem_specificaties_concept.docx` (samengevat)

**Hardware:** eigen PCB met vervangbare breakoutmodules; ESP32-S3 + LoRa + antenne; 9-DoF IMU met
sensorfusie; barometer; RTK-GNSS; tweede ESP met LoRa als USB-adapter; batterij met beveiliging;
USB-C; 3D-geprinte behuizing met demping; uitbreidingsconnector naar voertuigcontroller;
optioneel tweede microcontroller + 2 servo's op vliegtuigmock-up.

**Software:** één installeerbare laptopapp; firmware op meetmodule en op LoRa-adapter; startscherm
met USB- en LoRa-controle; hoofdscherm met Livekaart en Programmering & besturing; live
meetwaarden; 3D-kaart met routelijn; eigen verwerkingscode; lokale interface naar extern proces;
commando's terug via LoRa; veilige stop; opslag voor latere analyse.

**Nog te bepalen:** bordmodellen/pinbezetting/spanningen/stroombudget; RTK-correctiebron;
meetfrequentie/LoRa-formaat/nauwkeurigheid/gedrag bij wegvallen; commandoformaat/terugkoppeling/
veiligheidsgrenzen; kaartbron en detailniveau 3D-weergave.

## `GSN-project_draadloze_3D-meetmodule.docx` (samengevat)

Bevat de **opdrachtomschrijving** (compacte draadloze meetmodule in 3D-geprinte behuizing met
GPS-RTK, barometer, IMU, LoRa; laptop met 3D-weergave; dempingsmechanisme; uitbreiding met
vliegtuigmock-up en twee servo's voor rolroer en hoogteroer), een **blokschema** en het **doel**.
Inhoudelijk gelijk aan `create_gsn_document.py`.
