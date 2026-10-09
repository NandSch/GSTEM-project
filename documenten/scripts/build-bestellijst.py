#!/usr/bin/env python3
"""Bouwt documenten/beheer/Bestellijst-GSTEM.xlsx uit de BOM/bestellijst van G-Stem.

Uitvoeren:  python documenten/scripts/build-bestellijst.py
Bron/afspraken: GEBRUIKER/data/bestellijst.md en GEBRUIKER/data/componenten.md
Strategie: zo veel mogelijk bij Kiwi Electronics (NL) om verzendkosten te beperken; wat daar
goedkoper is of als reserve dient, bij antratek.be. Overige elektronica komt bij passende EU-winkels.
Voor de RTK-GNSS is China/AliExpress sinds 2026-10-07 de voorkeur; de exacte listing is nog niet bevestigd.
De draagprint en sockets zijn vervallen (2026-10-09); montage- en connectorbehoeften staan op te bepalen.
"""

import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / ".pi/agent/npm/node_modules/@sttronn/pi-sheets/skills/xlsx/scripts"))
import xlsx_kit
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# (categorie, functie, onderdeel, aantal, prijs_incl_btw, status, leverancier, link, opmerking)
RIJEN = [
    ("Rekenkern en communicatie", "Rekenkern + LoRa (toestel + ontvanger)",
     "XIAO ESP32S3 & Wio-SX1262 Kit for Meshtastic & LoRa", 2, 15.13, "antratek",
     "antratek.be", "https://www.antratek.be/xiao-esp32s3-for-meshtastic-lora",
     "1x toestel, 1x LoRa-ontvanger laptop; antenne inbegrepen. Kiwi verkoopt XIAO (EUR 8,46) "
     "+ Wio-SX1262 (EUR 5,43) apart, maar de Wio-module is daar NIET op voorraad"),

    ("Sensoren", "9-DoF IMU",
     "Adafruit 9-DOF Orientation IMU Fusion Breakout - BNO085 (BNO080) - STEMMA QT/Qwiic",
     1, 32.05, "kiwi", "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/adafruit-9-dof-orientation-imu-fusion-breakout-bno085-bno080-stemma-qt-qwiic-11273",
     "Goedkoper en nieuwer dan de BNO055 (anratek EUR 36,24)"),
    ("Sensoren", "Barometer",
     "Adafruit BMP581 I2C/SPI Druk- en Temperatuursensor - STEMMA QT", 1, 10.88,
     "kiwi", "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/adafruit-bmp581-i2c-spi-druk-en-temperatuursensor-stemma-qt-20534",
     "Nauwkeuriger dan BME280; BMP390L is bij Kiwi uit voorraad en niet op antratek"),
    ("Sensoren", "RTK-GNSS-module (breakout, LC29HDA rover)",
     "Quectel LC29HDA dual-band L1+L5 RTK-GNSS-developmentboard (geassembleerd) - kies de LC29HDA-variant",
     1, 36.99, "aliexpress", "AliExpress (China)",
     "https://nl.aliexpress.com/item/1005009915138674.html",
     "Kies bij het bestellen de LC29HDA (rover)-variant, geen LC29HBS (basisstation) en geen losse "
     "SMD-module. Richtprijs volgens de listing. Alternatieven met eenduidige variantkeuze op AliExpress: "
     "item 1005010758488281 en item 1005010162466640. Terugvaloptie EU: Waveshare LC29H(DA) HAT "
     "(Eckstein EUR 71,39 / Kamami ca. EUR 63)."),

    ("Antennes en RF", "GNSS-antenne (actief, L1/L5)",
     "Waveshare GPS External Antenna (D), SKU 25346 - actief L1+L5, LNA 28+-2 dB, SMA-J; alleen los kopen als de LC29HDA-kit geen passende antenne bevat",
     1, 15.70, "waveshare", "Waveshare (China)",
     "https://www.waveshare.com/gps-external-antenna-d.htm",
     "RF-banden en actieve antenne passen bij LC29HDA. AliExpress-boardconnector en bundelinhoud zijn niet bevestigd: "
     "controleer SMA-J/boardzijde, eventuele adapter en of het board één of twee antennes vereist. 3 m kabel; prijs niet in totaal opgenomen."),
    ("Antennes en RF", "LoRa IPEX/U.FL naar SMA pigtail", "Interface Cable SMA to U.FL (150 mm)",
     1, 3.57, "antratek", "antratek.be", "https://www.antratek.be/u-fl-sma-150mm-cable",
     "Goedkoper op antratek (EUR 3,57) dan Kiwi (EUR 4,22); bulkhead-bevestiging apart controleren"),
    ("Antennes en RF", "LoRa-antenne", "Inbegrepen bij de XIAO-kit", 1, None, "al in bezit", "-",
     "", ""),

    ("Voeding", "Accu 7,4 V", "2S LiPo met connector en kabel (heeft de gebruiker)", 1, None,
     "al in bezit", "-", "", ""),
    ("Voeding", "Voedingsaansluiting", "DC Barrel Jack Adapter - Female (heeft de gebruiker)",
     1, None, "al in bezit", "-", "", "Adapter met schroefklem; voor de kabelzijde"),
    ("Vervallen ontwerp", "PCB-voedingsaansluiting",
     "2,1 mm breadboard-/PCB-barreljack - alleen bedoeld voor de vervallen draagprint", None, None,
     "niet nodig", "-", "", "Niet bestellen. De bestaande barrel-adapter blijft; voedingsinvoer via de behuizing nog te bepalen."),
    ("Voeding", "Buck-converter 5 V", "Heeft de gebruiker", 1, None, "al in bezit", "-",
     "", "Referentie antratek: Buck Regulator Breakout 5V (EUR 12,04)"),
    ("Voeding", "Bescherming voeding",
     "2 A PTC Littelfuse 1812L200/16 + TVS SMBJ10A-TR (zonder P-MOSFET)", 1, 1.00,
     "mouser", "Mouser.be / DigiKey (EU-magazijn)",
     "https://www.mouser.com/ProductDetail/Littelfuse/1812L200-16DR",
     "PTC bij Mouser/DigiKey (EU); TVS SMBJ10A bij TME. P-MOSFET vervalt (beslissing 2026-10-06)."),
    ("Voeding", "Ompoolbeveiliging (P-MOSFET)",
     "P-MOSFET DMG2301L / AO3401A (SOT-23)", 1, None, "niet nodig", "-", "",
     "BESLISSING 2026-10-06: NIET voorzien. Geen P-MOSFET-ompoolbeveiliging; voorkom omgekeerd "
     "aansluiten met een gepolariseerde connector (XT60/JST-XH). Zie data/afgevoerd.md."),
    ("Voeding", "LDO 3,3 V", "AP2112K-3.3TRG1 (Diodes Inc., SOT-23-5)", 1, 0.27, "tme",
     "TME (Polen, EU)",
     "https://www.tme.eu/en/details/ap2112k-3.3trg1/ldo-fixed-voltage-regulators/diodes-incorporated/",
     "8000+ op voorraad bij TME"),
    ("Voeding", "Aan/uit-schakelaar", "Geen; toestel start bij voeding", None, None,
     "niet nodig", "-", "", ""),

    ("Vervallen ontwerp", "Draagprint (carrier-PCB)",
     "Eigen PCB bij AISLER", None, None, "niet nodig", "-", "",
     "Vervallen op 2026-10-09: de gebruiker bedradt en soldeert de onderdelen zelf en monteert ze aan een 3D-geprinte behuizing."),

    ("Bedrading en losse elektronica", "Level shifter 3,3 V <-> 5 V",
     "8-kanaals bidirectionele Logic Level Converter - TXB0108", 1, 8.70, "kiwi",
     "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836",
     "DEFINITIEF (2026-10-07): TXB0108-breakout. De TXB0104-IC (TSSOP-14, ca. EUR 1,80) is enkel "
     "een alternatief; antratek BSS138-converter EUR 4,78 is een ander type"),
    ("Bedrading en losse elektronica", "UART-/uitbreidingsconnector",
     "Eerder gekozen DEGSON 4-pins 3,5 mm; mogelijk overbodig bij rechtstreeks bedraden", None, None,
     "te bepalen", "-", "", "Nog geen keuze of aankoop; eerst bevestigen hoe de kabel naar buiten wordt aangesloten."),
    ("Vervallen ontwerp", "Socket-headers",
     "Dual-wipe en turned-pin sockets", None, None, "niet nodig", "-", "",
     "Vervallen op 2026-10-09: breakoutmodules worden handbedraad en gesoldeerd; niet bestellen."),
    ("Bedrading en losse elektronica", "Power-LED + serieweerstand",
     "3 mm LED rood (10-pack) + weerstand 330 Ohm (10-pack) - heeft de gebruiker thuis",
     1, None, "al in bezit", "-", "",
     "HEEFT DE GEBRUIKER THUIS (2026-10-06): 10-pack rode 3 mm LED + 10-pack 330 Ohm; niet "
     "aankopen. Referentie Kiwi: LED EUR 1,20 + weerstand EUR 0,96 = EUR 2,16"),
    ("Bedrading en losse elektronica", "Ontkoppelcondensatoren",
     "Keramische condensator kit (15 soorten, 450 st.) - dekt 100 nF + 10 uF", 1, 10.27,
     "kiwi", "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492",
     "Kit i.p.v. losse condensatoren"),
    ("Bedrading en losse elektronica", "Bulk-elco", "100 uF / 16 V op de 5 V-ingang", 1, 0.59, "kiwi",
     "Kiwi Electronics", "https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440", ""),
    ("Bedrading en losse elektronica", "I2C-pull-ups",
     "Niet nodig; breakouts hebben ze al", None, None, "niet nodig", "-", "", "Geen extra pull-ups voorzien."),
    ("Bedrading en losse elektronica", "Behuizingsmontage",
     "Bevestigingsmateriaal nog te bepalen; eerdere M3-set was voor de draagprint", None, None,
     "te bepalen", "-", "", "Niet bestellen of online opzoeken voordat de gebruiker de montagewijze heeft bevestigd."),

    ("Kabels en verbruik (in bezit)", "USB-C datakabel", "Eigen kabel", 1, None, "al in bezit",
     "-", "", ""),
    ("Kabels en verbruik (in bezit)", "Dupont-/siliconendraad", "Heeft de gebruiker", 1, None,
     "al in bezit", "-", "", ""),
    ("Kabels en verbruik (in bezit)", "USB A-kabel LoRa-ontvanger",
     "USB-A naar USB-C voor de XIAO (heeft de gebruiker)", 1, None, "al in bezit", "-", "", ""),
    ("Kabels en verbruik (in bezit)", "Gereedschap",
     "Schuifmaat, soldeerbout, tin, flux, multimeter, USB-serieel adapter", 1, None,
     "al in bezit", "-", "", ""),

    ("Mock-up (vliegtuigje)", "Arduino", "Arduino Uno (heeft de gebruiker thuis)", 1, None,
     "al in bezit", "-", "", "Referentie antratek: Arduino Uno Rev3 (EUR 41,75)"),
    ("Mock-up (vliegtuigje)", "Servo's", "Bestaande voorraad (> 3)", 3, None, "al in bezit", "-",
     "", ""),
    ("Mock-up (vliegtuigje)", "Servo-voeding", "Aparte buck-converter", 1, None, "al in bezit",
     "-", "", ""),
    ("Mock-up (vliegtuigje)", "Romp en roeren", "Eigen 3D-print", 1, None, "al in bezit", "-",
     "", ""),
]

KOPPEN = ["Categorie", "Functie", "Onderdeel", "Aantal", "Prijs/st (EUR)", "Totaal (EUR)",
          "Status", "Leverancier", "Link", "Opmerking"]
BREEDTES = [24, 30, 46, 8, 14, 14, 12, 16, 52, 52]

KLEUR_STATUS = {
    "kiwi": "DDEBF7",
    "antratek": "C6EFCE",
    "eckstein": "FFF2CC",
    "tme": "FCE4D6",
    "mouser": "E2EFDA",
    "hestore": "F8CBAD",
    "tinytronics": "DDEBF7",
    "aisler": "E1D5E7",
    "schatting": "FCE4D6",
    "al in bezit": "D9D9D9",
    "geen link": "FFEB9C",
    "onderzoek": "FFF2CC",
    "aliexpress": "FCE4D6",
    "waveshare": "E5D5F0",
    "niet nodig": "F2F2F2",
    "te bepalen": "FFF2CC",
}
KLEUR_KOP = "1F3864"
KLEUR_CATEGORIE = "D6DCE4"

dun = Side(style="thin", color="BFBFBF")
RAND = Border(left=dun, right=dun, top=dun, bottom=dun)


def bouw():
    wb = Workbook()
    ws = wb.active
    ws.title = "Bestellijst"

    # Titel
    ws.merge_cells("A1:J1")
    ws["A1"] = ("Bestellijst G-Stem meettoestel - prijzen incl. btw "
                "(Kiwi + antratek + TME + Mouser + AliExpress; bijgewerkt 2026-10-09)")
    ws["A1"].font = Font(bold=True, size=13, color="FFFFFF")
    ws["A1"].fill = PatternFill("solid", fgColor=KLEUR_KOP)
    ws["A1"].alignment = Alignment(vertical="center", horizontal="left")
    ws.row_dimensions[1].height = 24

    # Kopregel
    for c, (kop, breedte) in enumerate(zip(KOPPEN, BREEDTES), start=1):
        cel = ws.cell(row=2, column=c, value=kop)
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = PatternFill("solid", fgColor=KLEUR_KOP)
        cel.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cel.border = RAND
        ws.column_dimensions[get_column_letter(c)].width = breedte
    ws.row_dimensions[2].height = 22

    r = 3
    vorige_cat = None
    for cat, functie, onderdeel, aantal, prijs, status, lev, link, opm in RIJEN:
        if cat != vorige_cat:
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
            cel = ws.cell(row=r, column=1, value=cat)
            cel.font = Font(bold=True, color="1F3864")
            cel.fill = PatternFill("solid", fgColor=KLEUR_CATEGORIE)
            cel.alignment = Alignment(vertical="center")
            for c in range(1, 11):
                ws.cell(row=r, column=c).border = RAND
            ws.row_dimensions[r].height = 18
            vorige_cat = cat
            r += 1

        totaal = (aantal * prijs) if (aantal and prijs) else None
        waarden = [cat, functie, onderdeel, aantal, prijs, totaal, status, lev, link, opm]
        for c, waarde in enumerate(waarden, start=1):
            cel = ws.cell(row=r, column=c, value=waarde)
            cel.border = RAND
            cel.alignment = Alignment(vertical="top", wrap_text=(c in (2, 3, 9, 10)))
            if c in (5, 6) and waarde is not None:
                cel.number_format = '#,##0.00 "EUR"'
                cel.alignment = Alignment(horizontal="right", vertical="top")
            if c == 4 and waarde is not None:
                cel.alignment = Alignment(horizontal="center", vertical="top")
            if c == 7:
                cel.fill = PatternFill("solid", fgColor=KLEUR_STATUS.get(status, "FFFFFF"))
                cel.alignment = Alignment(horizontal="center", vertical="top")
            if c == 9 and waarde:
                cel.hyperlink = waarde
                cel.font = Font(color="0563C1", underline="single")
        r += 1

    laatste_data = r - 1

    # Totaalregels per winkel
    def totaalrij(label, formule, vet=True):
        nonlocal r
        deze = r
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        cel = ws.cell(row=r, column=1, value=label)
        cel.font = Font(bold=vet)
        cel.alignment = Alignment(horizontal="right", vertical="center")
        tot = ws.cell(row=r, column=6, value=formule)
        tot.number_format = '#,##0.00 "EUR"'
        tot.font = Font(bold=vet)
        tot.alignment = Alignment(horizontal="right")
        for c in range(1, 11):
            ws.cell(row=r, column=c).border = Border(
                top=Side(style="medium", color=KLEUR_KOP), bottom=dun, left=dun, right=dun)
        r += 1
        return deze

    r += 1  # lege regel
    totaalrij("Totaal te bestellen bij Kiwi Electronics",
              '=SUMIF(G3:G%d,"kiwi",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal te bestellen bij antratek",
              '=SUMIF(G3:G%d,"antratek",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal te bestellen bij AliExpress (China)",
              '=SUMIF(G3:G%d,"aliexpress",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal te bestellen bij TME (EU)",
              '=SUMIF(G3:G%d,"tme",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal te bestellen bij Mouser/DigiKey (EU)",
              '=SUMIF(G3:G%d,"mouser",F3:F%d)' % (laatste_data, laatste_data))
    rij_waveshare = totaalrij("Waveshare: losse GNSS-antenne (voorwaardelijk)",
              '=SUMIF(G3:G%d,"waveshare",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Eckstein-terugvaloptie (niet gekozen; geen actieve regel)",
              '=SUMIF(G3:G%d,"eckstein",F3:F%d)' % (laatste_data, laatste_data))
    rij_totaal_onderdelen = totaalrij(
        "TOTAAL actieve onderdelen (incl. voorwaardelijke GNSS-antenne)",
        "=SUM(F3:F%d)" % laatste_data)
    totaalrij("TOTAAL actieve onderdelen excl. losse GNSS-antenne",
              "=F%d-F%d" % (rij_totaal_onderdelen, rij_waveshare))
    r += 1

    ws.cell(row=r, column=1,
            value="Let op: prijzen zijn onder voorbehoud en incl. btw. Bij de AliExpress-GPS moet je de "
                  "LC29HDA (rover)-variant kiezen, geen LC29HBS (basisstation) en geen losse SMD-module. "
                  "De losse Waveshare-antenne (SKU 25346) is voorwaardelijk: eerst checken of de boardkit "
                  "een passende L1/L5-antenne meelevert. Terugvaloptie GPS in de EU: Waveshare LC29H(DA) HAT "
                  "(Eckstein ca. EUR 71,39 / Kamami ca. EUR 63). De LED + 330 Ohm-weerstand (10-packs) heeft "
                  "de gebruiker thuis en is dus niet meer te bestellen. Carrier-PCB en sockets zijn vervallen; "
                  "montage- en connectorbehoefte is nog te bepalen. Zie GEBRUIKER/data/bedrading-en-behuizing.md."
            ).font = Font(italic=True, size=9)

    ws.freeze_panes = "A3"
    ws.auto_filter.ref = "A2:J%d" % laatste_data

    # Tweede blad: volledige uitleg tags
    ws2 = wb.create_sheet("Legende")
    ws2.append(["Tag", "Betekenis"])
    for cel in ws2[1]:
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = PatternFill("solid", fgColor=KLEUR_KOP)
    for tag, bet in [
        ("kiwi", "Aankooplink gevonden op Kiwi Electronics (kiwi-electronics.com)"),
        ("antratek", "Aankooplink gevonden op antratek.be (goedkoper of als reserve)"),
        ("aliexpress", "AliExpress (China): gekozen bron voor de LC29HDA-RTK-rover-module"),
        ("waveshare", "Waveshare (fabrikant, China): losse actieve L1/L5-GNSS-antenne (voorwaardelijk)"),
        ("eckstein", "Eckstein (Duitsland, EU): Waveshare LC29H(DA)-HAT terugvaloptie; niet de huidige voorkeur"),
        ("tme", "TME (Polen, EU): eerder gekozen LDO/TVS; montage van de componenten nog open"),
        ("mouser", "Mouser.be / DigiKey met EU-magazijn: PTC, exacte onderdelen"),
        ("niet nodig", "Niet bestellen of bewust niet voorzien; o.a. carrier-PCB en sockets vervallen (2026-10-09)"),
        ("te bepalen", "Montage- of connectorbehoefte nog open; niet opgenomen in actieve totalen"),
        ("hestore", "HESTORE (Hongarije, EU): historische schroefklemoptie; niet meer actief besteld"),
        ("tinytronics", "TinyTronics (Nederland, EU): historische M3-set voor oude printmontage"),
        ("aisler", "Historische fabrikant van de vervallen carrier-PCB; niet bestellen"),
        ("schatting", "Prijs is een schatting; apart te bestellen bij een componentenwinkel"),
        ("al in bezit", "Heeft de gebruiker al; niet aankopen"),
        ("geen link", "Niet gevonden bij Kiwi of antratek; nog geen prijs"),
        ("onderzoek", "Zoekrichting bekend, maar productlisting/prijs nog niet gevalideerd"),
        ("niet nodig", "Bewust niet voorzien"),
    ]:
        ws2.append([tag, bet])
        ws2.cell(row=ws2.max_row, column=1).fill = PatternFill(
            "solid", fgColor=KLEUR_STATUS.get(tag, "FFFFFF"))
    ws2.column_dimensions["A"].width = 14
    ws2.column_dimensions["B"].width = 70

    # Derde blad: actuele bedrading en montagekeuzes
    ws3 = wb.create_sheet("Bedrading en montage")
    ws3.merge_cells("A1:D1")
    ws3["A1"] = "Bedrading en montage - open keuzes (2026-10-09)"
    ws3["A1"].font = Font(bold=True, size=13, color="FFFFFF")
    ws3["A1"].fill = PatternFill("solid", fgColor=KLEUR_KOP)
    ws3["A1"].alignment = Alignment(vertical="center")
    ws3.row_dimensions[1].height = 24
    ws3.column_dimensions["A"].width = 44
    ws3.column_dimensions["B"].width = 16
    ws3.column_dimensions["C"].width = 18
    ws3.column_dimensions["D"].width = 46

    rr = 2

    def sheet_kop(tekst):
        nonlocal rr
        ws3.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=4)
        cel = ws3.cell(row=rr, column=1, value=tekst)
        cel.font = Font(bold=True, color="1F3864")
        cel.fill = PatternFill("solid", fgColor=KLEUR_CATEGORIE)
        cel.alignment = Alignment(vertical="center")
        rr += 1

    def sheet_rij(a, b=None, c=None, d=None, vet=False, geld=False):
        nonlocal rr
        for i, w in enumerate((a, b, c, d), start=1):
            cel = ws3.cell(row=rr, column=i, value=w)
            cel.border = RAND
            cel.alignment = Alignment(vertical="top", wrap_text=True)
            if vet:
                cel.font = Font(bold=True)
            if geld and i == 2 and w is not None:
                cel.number_format = '#,##0.00 "EUR"'
                cel.alignment = Alignment(horizontal="right", vertical="top")
        rr += 1

    sheet_kop("Huidige aanpak: handbedrading en behuizing")
    sheet_rij("Geen eigen carrier-PCB en geen socket-headers. De gebruiker bedradt en soldeert zelf; de onderdelen worden aan een 3D-geprinte behuizing gemonteerd.")
    sheet_rij("Breakoutmodules", "Blijven behouden", "Zelf bedraden; exacte verbindingen nog uit te werken")
    sheet_rij("Montagehardware", "Nog te bepalen", "Niet toevoegen of online opzoeken voordat montagewijze bevestigd is")
    sheet_rij("UART-/uitbreidingsconnector", "Nog te bepalen", "Eerder gekozen schroefklem kan vervallen bij rechtstreeks bedraden")
    sheet_rij("Voedingsinvoer", "Nog te bepalen", "Bestaande barrel-adapter aanwezig; paneel-/behuizingsmontage open")
    sheet_rij("PTC, TVS, LDO en ontkoppeling", "Functies voorlopig behouden", "Handbedrading en mechanische ondersteuning nog uit te werken")
    rr += 1

    sheet_kop("Vervallen bestellingen")
    sheet_rij("Carrier-PCB bij AISLER", "Niet nodig", "Geen print produceren of bestellen")
    sheet_rij("Socket-headers", "Niet nodig", "Breakoutmodules worden met draden aangesloten en gesoldeerd")
    sheet_rij("PCB-barreljack", "Niet nodig", "Specifiek gekozen voor montage op de vervallen PCB")
    sheet_rij("Oude M3-set", "Niet actief", "Was bedoeld voor printmontage; behuizingsbevestiging nog te bepalen")
    rr += 1

    sheet_kop("Vervolgstappen (geen nieuwe aankopen vastgelegd)")
    for stap in [
        "1. Bevestig hoe de breakoutmodules en losse componenten aan de behuizing worden gemonteerd",
        "2. Werk bedradingsroute, isolatie/ondersteuning en trekontlasting uit",
        "3. Bevestig of de UART-klem en voedingsaansluiting nodig blijven",
        "4. Controleer of aanwezige draad en printmateriaal volstaan; koop niets nieuws zonder bevestiging",
        "5. Herbereken de bestellijst nadat de montagekeuzes vastliggen",
    ]:
        sheet_rij(stap)

    ws3.freeze_panes = "A2"

    # Vierde blad: bestelbaarheid (gecontroleerd 2026-10-06)
    ws4 = wb.create_sheet("Bestelbaarheid")
    ws4.merge_cells("A1:D1")
    ws4["A1"] = "Bestelbaarheid - historische controle op 2026-10-06 (geen actuele besteladviezen)"
    ws4["A1"].font = Font(bold=True, size=13, color="FFFFFF")
    ws4["A1"].fill = PatternFill("solid", fgColor=KLEUR_KOP)
    ws4["A1"].alignment = Alignment(vertical="center")
    ws4.row_dimensions[1].height = 24
    for kol, br in zip("ABCD", (26, 42, 20, 40)):
        ws4.column_dimensions[kol].width = br
    ws4.append(["Winkel", "Artikel", "Voorraad", "Opmerking"])
    for cel in ws4[2]:
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = PatternFill("solid", fgColor=KLEUR_KOP)
    BESTELBAAR = [
        ("Kiwi Electronics", "Adafruit BNO085 9-DoF IMU", "11 st.", "prijs bevestigd"),
        ("Kiwi Electronics", "Adafruit BMP581 barometer", "4 st.", "KNAPPE voorraad"),
        ("Kiwi Electronics", "TXB0108 level converter", "17 st.", ""),
        ("Kiwi Electronics", "3 mm LED rood (10-pack)", "193 st.",
         "HEEFT DE GEBRUIKER THUIS - niet bestellen"),
        ("Kiwi Electronics", "Weerstand 330 Ohm (10 st.)", "115 st.",
         "HEEFT DE GEBRUIKER THUIS - niet bestellen"),
        ("Kiwi Electronics", "Keramische condensator kit", "2 st.", "KNAPPE voorraad"),
        ("Kiwi Electronics", "100 uF / 16 V elco", "72 st.", ""),
        ("antratek.be", "XIAO ESP32S3 + Wio-SX1262 kit", "op voorraad", "2x nodig"),
        ("antratek.be", "SMA -> U.FL pigtail 150 mm", "op voorraad", ""),
        ("TME (EU)", "AP2112K-3.3TRG1 (LDO)", "8 198", "prijs uit snippet (TME 403)"),
        ("TME (EU)", "SMBJ10A-TR (TVS)", "1 820", "prijs uit snippet"),
        ("TME (EU)", "AO3401A (P-MOSFET)", "22 840", "NIET GEBRUIKT - P-MOSFET vervalt (2026-10-06)"),
        ("Mouser/DigiKey", "DMG2301L-7 (P-MOSFET)", "losse aantallen", "NIET GEBRUIKT - P-MOSFET vervalt (2026-10-06)"),
        ("Mouser/DigiKey", "1812L200/16DR (PTC 2 A 16 V)", "14 555 / 9 900", ""),
        ("TME (EU)", "Preci-Dip socket 2,54 mm", "MOQ 380 (business)", "historische regel; sockets vervallen op 2026-10-09"),
        ("HESTORE (EU)", "DEGSON DG250-3.5-04P (push-in)", "> 10", "EUR 0,52 excl."),
        ("HESTORE (EU)", "DEGSON 15EDGK-3.5/4P (schroef)", "> 15", "schroefvariant"),
        ("TinyTronics (NL)", "M3 Afstandsbusje Kit", "50+", "historische prijs; bedoeld voor de vervallen PCB-montage"),
        ("Bits & Parts (NL)", "M3 spacer-set 180-delig", "op voorraad", "historische prijs; montage voor behuizing nog te bepalen"),
        ("Eckstein (DE)", "Waveshare LC29H(DA) HAT 25279 (WS25279)", "leverbaar", "Terugvaloptie - EUR 71,39 incl.; niet huidige voorkeur"),
        ("AliExpress (China)", "LC29HDA RTK-GNSS-developmentboard (item 1005009915138674)", "richtprijs EUR 36,99", "kies de LC29HDA (rover)-variant, geen LC29HBS en geen losse SMD-module"),
        ("Kamami (PL)", "Waveshare LC29H(DA) HAT 25279", "24 u", "~EUR 63 = goedkoopste EU"),
        ("Botland (EU)", "Waveshare LC29H(DA) HAT 25279", "op voorraad", "EUR 70,50"),
        ("HESTORE (EU)", "Waveshare LC29H(DA) HAT 25279", "> 2", "~EUR 110 incl. = duur"),
    ]
    for rij in BESTELBAAR:
        ws4.append(list(rij))
        for cel in ws4[ws4.max_row]:
            cel.border = RAND
            cel.alignment = Alignment(vertical="top", wrap_text=True)
    ws4.freeze_panes = "A3"

    doel = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "beheer", "Bestellijst-GSTEM.xlsx")
    xlsx_kit.save(wb, doel)
    print("Opgeslagen:", doel)


if __name__ == "__main__":
    bouw()
