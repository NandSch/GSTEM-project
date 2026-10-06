#!/usr/bin/env python3
"""Bouwt documenten/Bestellijst-GSTEM.xlsx uit de BOM/bestellijst van G-Stem.

Uitvoeren:  python documenten/build-bestellijst.py
Bron/afspraken: GEBRUIKER/data/bestellijst.md en GEBRUIKER/data/componenten.md
Strategie: zo veel mogelijk bij Kiwi Electronics (BE/NL) om verzendkosten te beperken;
wat daar goedkoper is of als reserve dient, bij antratek.be.
"""

import os
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
    ("Sensoren", "RTK-GNSS-module", "Quectel LC29H(DA)", 1, None, "geen link", "-",
     "", "Niet bij Kiwi (alleen niet-RTK L76K) of antratek. Alternatief: LG290P RTK (EUR 217,74) "
     "of ZED-F9P (EUR 302,44)"),

    ("Antennes en RF", "GNSS-antenne (actief, SMA)",
     "GPS Antenne - Externe Actieve Antenne - 3-5V 28dB 5 Meter SMA", 1, 16.93,
     "kiwi", "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/gps-antenne-externe-actieve-antenne-3-5v-28db-5-meter-sma-620",
     "Goedkoopste passende actieve SMA-antenne (L1). Upgrade voor dual-band RTK: L1/L5-antenne EUR 120,94"),
    ("Antennes en RF", "LoRa IPEX/U.FL naar SMA pigtail", "Interface Cable SMA to U.FL (150 mm)",
     1, 3.57, "antratek", "antratek.be", "https://www.antratek.be/u-fl-sma-150mm-cable",
     "Goedkoper op antratek (EUR 3,57) dan Kiwi (EUR 4,22); bulkhead-bevestiging apart controleren"),
    ("Antennes en RF", "LoRa-antenne", "Inbegrepen bij de XIAO-kit", 1, None, "al in bezit", "-",
     "", ""),

    ("Voeding", "Accu 7,4 V", "2S LiPo met connector en kabel (heeft de gebruiker)", 1, None,
     "al in bezit", "-", "", ""),
    ("Voeding", "Voedingsaansluiting", "DC Barrel Jack Adapter - Female (heeft de gebruiker)",
     1, None, "al in bezit", "-", "", "Adapter met schroefklem; geen PCB-montage"),
    ("Voeding", "Buck-converter 5 V", "Heeft de gebruiker", 1, None, "al in bezit", "-",
     "", "Referentie antratek: Buck Regulator Breakout 5V (EUR 12,04)"),
    ("Voeding", "Bescherming voeding", "2 A PTC + P-MOSFET DMG2301L + TVS SMBJ10A", 1, 0.95,
     "schatting", "componentenwinkel", "",
     "Niet bij Kiwi of antratek; prijs is een schatting (Mouser/LCSC)"),
    ("Voeding", "LDO 3,3 V", "AP2112K-3.3 (of AMS1117-3.3)", 1, 0.35, "schatting",
     "componentenwinkel", "",
     "Niet bij Kiwi of antratek; prijs is een schatting"),
    ("Voeding", "Aan/uit-schakelaar", "Geen; toestel start bij voeding", None, None,
     "niet nodig", "-", "", ""),

    ("Draagprint (PCB bij AISLER)", "Draagprint (printplaat)",
     "2-laags 1,6 mm HASL, set van 3 stuks - AISLER", 3, 10.92, "aisler", "AISLER",
     "https://aisler.net",
     "Schatting 75 cm2 (100x75 mm), incl. btw; Budget-service. Formule: EUR 12,00 + "
     "EUR 0,067/cm2 x oppervlak x aantal. AISLER levert in sets van 3; gratis verzending. "
     "Definitieve maat volgt uit de KiCad-layout"),

    ("Print en verbindingen", "Level shifter 3,3 V <-> 5 V",
     "8-kanaals bidirectionele Logic Level Converter - TXB0108", 1, 8.70, "kiwi",
     "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/8-channel-bi-directional-logic-level-converter-txb0108-836",
     "Past bij de gekozen TXB-serie; antratek-alternatief BSS138-converter EUR 4,78"),
    ("Print en verbindingen", "Schroefklem 4-pins 3,5 mm", "KF128/KF301", 1, 0.55, "schatting",
     "componentenwinkel", "", "Niet bij Kiwi (alleen 3-weg) of antratek; prijs schatting"),
    ("Print en verbindingen", "Sockets", "Dual-wipe (ESP32) + precisie voor de rest", 1, 5.00,
     "schatting", "componentenwinkel", "",
     "Niet bij Kiwi of antratek; prijs schatting (zie pcb-methodes-kosten)"),
    ("Print en verbindingen", "Power-LED + serieweerstand",
     "3 mm LED rood (10-pack) + weerstand 330 Ohm (10-pack)", 1, 2.16, "kiwi",
     "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/3mm-led-diffuus-rood-10-pack-3085",
     "10-packs: 1 LED + 1 weerstand nodig; weerstand EUR 0,96; rest overschot"),
    ("Print en verbindingen", "Ontkoppelcondensatoren",
     "Keramische condensator kit (15 soorten, 450 st.) - dekt 100 nF + 10 uF", 1, 10.27,
     "kiwi", "Kiwi Electronics",
     "https://www.kiwi-electronics.com/nl/keramische-condensator-kit-in-doos-15-soorten-450-stuks-10492",
     "Kit i.p.v. losse condensatoren"),
    ("Print en verbindingen", "Bulk-elco", "100 uF / 16 V op de 5 V-ingang", 1, 0.59, "kiwi",
     "Kiwi Electronics", "https://www.kiwi-electronics.com/nl/100uf-16v-condensator-440", ""),
    ("Print en verbindingen", "I2C-pull-ups op de print",
     "Niet nodig; breakouts hebben ze al", 2, None, "niet nodig", "-", "", "2 reserve-footprints"),
    ("Print en verbindingen", "Montage", "M3-schroeven, moeren, standoffs, nylon spacers", 1, 4.00,
     "schatting", "componentenwinkel", "",
     "Niet bij Kiwi of antratek; prijs schatting"),

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
    "aisler": "E1D5E7",
    "schatting": "FCE4D6",
    "al in bezit": "D9D9D9",
    "geen link": "FFEB9C",
    "niet nodig": "F2F2F2",
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
                "(Kiwi Electronics + antratek + AISLER, 2026-10-06)")
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

    r += 1  # lege regel
    totaalrij("Totaal te bestellen bij Kiwi Electronics",
              '=SUMIF(G3:G%d,"kiwi",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal te bestellen bij antratek",
              '=SUMIF(G3:G%d,"antratek",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Subtotaal onderdelen (Kiwi + antratek)",
              "=F%d+F%d" % (r - 2, r - 1))
    totaalrij("Totaal draagprint bij AISLER (3 stuks)",
              '=SUMIF(G3:G%d,"aisler",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal PCB-onderdelen (schatting, apart bestellen)",
              '=SUMIF(G3:G%d,"schatting",F3:F%d)' % (laatste_data, laatste_data))
    totaalrij("Totaal alles (incl. print + PCB-onderdelen)",
              "=F%d+F%d+F%d" % (r - 3, r - 2, r - 1))
    r += 1

    ws.cell(row=r, column=1,
            value="Let op: prijzen onder voorbehoud (Kiwi Electronics + antratek + AISLER, 2026-10-06). "
                  "De PCB-onderdelen op status 'schatting' zijn benaderd (o.a. sockets, discrete voeding, "
                  "LDO, schroefklem, M3-montage). Het 'geen link'-onderdeel (RTK-module LC29H) is niet in "
                  "de totalen opgenomen. Details: GEBRUIKER/data/bestelschema-pcb.md."
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
        ("aisler", "Gefabriceerd bij AISLER (EU); print zelf, geen componenten"),
        ("schatting", "Prijs is een schatting; apart te bestellen bij een componentenwinkel"),
        ("al in bezit", "Heeft de gebruiker al; niet aankopen"),
        ("geen link", "Niet gevonden bij Kiwi of antratek; nog geen prijs"),
        ("niet nodig", "Bewust niet voorzien"),
    ]:
        ws2.append([tag, bet])
        ws2.cell(row=ws2.max_row, column=1).fill = PatternFill(
            "solid", fgColor=KLEUR_STATUS.get(tag, "FFFFFF"))
    ws2.column_dimensions["A"].width = 14
    ws2.column_dimensions["B"].width = 70

    # Derde blad: bestelschema draagprint bij AISLER
    ws3 = wb.create_sheet("Bestelschema PCB")
    ws3.merge_cells("A1:D1")
    ws3["A1"] = "Bestelschema draagprint bij AISLER - schatting (2026-10-06)"
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

    sheet_kop("AISLER-productie - 2-laags 1,6 mm HASL Budget")
    sheet_rij("Formule: EUR 12,00 job fee + EUR 0,067/cm2 x oppervlak x aantal "
              "(sets van 3, gratis verzending, productie vanaf 2 werkdagen)")
    sheet_rij("Oppervlak", "3 stuks incl. btw", "6 stuks incl. btw", vet=True)
    sheet_rij("60 cm2 (bv. 100x60)", 29.11, 43.71, geld=True)
    sheet_rij("75 cm2 (100x75, aanname)", 32.76, 50.99, geld=True)
    sheet_rij("90 cm2 (120x75)", 36.41, 58.30, geld=True)
    sheet_rij("100 cm2 (100x100)", 38.84, 63.16, geld=True)
    rr += 1

    sheet_kop("Onderdelen op de print")
    sheet_rij("Onderdeel", "Prijs (EUR)", "Leverancier", vet=True)
    sheet_rij("Sockets (dual-wipe + precisie)", 5.00, "componentenwinkel (schatting)", geld=True)
    sheet_rij("Voedingsbescherming (2 A PTC + DMG2301L + SMBJ10A)", 0.95,
              "componentenwinkel (schatting)", geld=True)
    sheet_rij("LDO AP2112K-3.3", 0.35, "componentenwinkel (schatting)", geld=True)
    sheet_rij("Schroefklem 4-pins 3,5 mm (KF128/KF301)", 0.55,
              "componentenwinkel (schatting)", geld=True)
    sheet_rij("M3-schroeven, moeren, standoffs, spacers", 4.00,
              "componentenwinkel (schatting)", geld=True)
    sheet_rij("Subtotaal apart te bestellen", 10.85, "schatting", vet=True, geld=True)
    sheet_rij("TXB0108 level shifter", 8.70, "Kiwi Electronics", geld=True)
    sheet_rij("LED + serieweerstand (per bord gebruikt)", 0.22, "Kiwi Electronics", geld=True)
    sheet_rij("Ontkoppelcondensatoren (per bord gebruikt)", 0.50, "Kiwi Electronics", geld=True)
    sheet_rij("Bulk-elco 100 uF", 0.59, "Kiwi Electronics", geld=True)
    sheet_rij("Subtotaal al in hoofd-bestellijst", 10.01, "Kiwi Electronics", vet=True, geld=True)
    sheet_rij("Totaal onderdelen op de print (met TXB0108)", 20.86,
              "met TXB0104-IC direct: ca. 13,96", vet=True, geld=True)
    rr += 1

    sheet_kop("Totalen (3 borden, incl. btw)")
    sheet_rij("AISLER print, 3 stuks, 75 cm2 Budget", 32.76, geld=True)
    sheet_rij("Onderdelen op de print", 20.86, geld=True)
    sheet_rij("Totaal", 53.62, vet=True, geld=True)
    sheet_rij("Waarvan al in de hoofd-bestellijst", 10.01, geld=True)
    sheet_rij("Werkelijk nieuw te bestellen", 43.61, vet=True, geld=True)
    rr += 1

    sheet_kop("Bestelvolgorde")
    for stap in [
        "1. PCB ontwerpen in KiCad; layout afronden, DRC, Gerbers/ODB++ exporteren",
        "2. Bordafmeting definitief nameten en AISLER-calculator controleren",
        "3. Print bestellen bij AISLER (3 of 6 stuks, Budget-service)",
        "4. Tegelijk de 'schatting'-onderdelen bestellen (sockets, voeding, LDO, klem, montage)",
        "5. Kiwi/antratek-bestelling: level shifter, LED, condensatoren, bulk-elco",
        "6. Rendering vergelijken met het echte bord, daarna solderen",
    ]:
        sheet_rij(stap)

    ws3.freeze_panes = "A2"

    doel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Bestellijst-GSTEM.xlsx")
    wb.save(doel)
    print("Opgeslagen:", doel)


if __name__ == "__main__":
    bouw()
