#!/usr/bin/env python3
"""Bouwt documenten/Bestellijst-GSTEM.xlsx uit de BOM/bestellijst van G-Stem.

Uitvoeren:  python documenten/build-bestellijst.py
Bron/afspraken: GEBRUIKER/data/bestellijst.md en GEBRUIKER/data/componenten.md
Alles is gezocht op antratek.be; niet gevonden = geen link (niet elders gezocht).
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
     "1x toestel, 1x LoRa-ontvanger laptop; antenne inbegrepen"),

    ("Sensoren", "9-DoF IMU", "9-DOF Absolute Orientation IMU Fusion Breakout - BNO055",
     1, 36.24, "antratek", "antratek.be",
     "https://www.antratek.be/9-dof-absolute-orientation-imu-fusion-breakout-bno055", ""),
    ("Sensoren", "Barometer", "Atmospheric Sensor Breakout - BME280 (Qwiic)", 1, 19.97,
     "antratek", "antratek.be", "https://www.antratek.be/atmospheric-sensor-breakout-bme280",
     "Goedkoopst/leverbaar alternatief voor BMP390; minder nauwkeurig (EUR 1 hPa i.p.v. 0,03 hPa)"),
    ("Sensoren", "RTK-GNSS-module", "Quectel LC29H(DA)", 1, None, "geen link", "-",
     "", "Niet op antratek.be. Alternatief: LG290P RTK (EUR 217,74) of ZED-F9P (EUR 302,44)"),

    ("Antennes en RF", "GNSS-antenne (actief, SMA)",
     "GPS/GNSS Magnetic Mount Antenna SMA - 3m, SparkFun GPS-14986", 1, 19.30,
     "antratek", "antratek.be", "https://www.antratek.be/gps-gnss-magnetic-mount-antenna-sma-3m",
     "Goedkoopste passende antenne (L1, multi-constellatie). Upgrade voor dual-band RTK: L1/L5-antenne EUR 120,94"),
    ("Antennes en RF", "LoRa IPEX/U.FL naar SMA pigtail", "Interface Cable SMA to U.FL (150 mm)",
     1, 3.57, "antratek", "antratek.be", "https://www.antratek.be/u-fl-sma-150mm-cable",
     "Bulkhead-bevestiging apart controleren"),
    ("Antennes en RF", "LoRa-antenne", "Inbegrepen bij de XIAO-kit", 1, None, "al in bezit", "-",
     "", ""),

    ("Voeding", "Accu 7,4 V", "2S LiPo met connector en kabel (heeft de gebruiker)", 1, None,
     "al in bezit", "-", "", ""),
    ("Voeding", "Voedingsaansluiting", "DC Barrel Jack Adapter - Female (heeft de gebruiker)",
     1, None, "al in bezit", "-", "", "Adapter met schroefklem; geen PCB-montage"),
    ("Voeding", "Buck-converter 5 V", "Heeft de gebruiker", 1, None, "al in bezit", "-",
     "", "Referentie antratek: Buck Regulator Breakout 5V (EUR 12,04)"),
    ("Voeding", "Bescherming voeding", "2 A PTC + P-MOSFET DMG2301L + TVS SMBJ10A", 1, None,
     "geen link", "-", "", "Niet op antratek.be"),
    ("Voeding", "LDO 3,3 V", "AP2112K-3.3 (of AMS1117-3.3)", 1, None, "geen link", "-",
     "", "Niet op antratek.be"),
    ("Voeding", "Aan/uit-schakelaar", "Geen; toestel start bij voeding", None, None,
     "niet nodig", "-", "", ""),

    ("Print en verbindingen", "Level shifter 3,3 V <-> 5 V",
     "Logic Level Converter Bi-Directional (alternatief voor TXB0104)", 1, 4.78, "antratek",
     "antratek.be", "https://www.antratek.be/logic-level-converter-bi-directional-bob-12009",
     "Gekozen TXB0104 niet op antratek; dit is een bruikbaar alternatief"),
    ("Print en verbindingen", "Schroefklem 4-pins 3,5 mm", "KF128/KF301", 1, None, "geen link",
     "-", "", "Niet op antratek.be; antratek heeft wel terminal-block pluggen"),
    ("Print en verbindingen", "Sockets", "Dual-wipe (ESP32) + precisie voor de rest", 1, None,
     "geen link", "-", "", "Niet op antratek.be"),
    ("Print en verbindingen", "Power-LED + serieweerstand", "Status voeding", 1, None, "geen link",
     "-", "", "Niet op antratek.be"),
    ("Print en verbindingen", "Ontkoppelcondensatoren", "100 nF + 10 uF per modulevoedingspin",
     1, None, "geen link", "-", "", "Niet op antratek.be"),
    ("Print en verbindingen", "Bulk-elco", "100 uF / 16 V op de 5 V-ingang", 1, None, "geen link",
     "-", "", "Niet op antratek.be"),
    ("Print en verbindingen", "I2C-pull-ups op de print",
     "Niet nodig; breakouts hebben ze al", 2, None, "niet nodig", "-", "", "2 reserve-footprints"),
    ("Print en verbindingen", "Montage", "M3-schroeven, moeren, standoffs, nylon spacers", 1, None,
     "geen link", "-", "", "Niet op antratek.be"),

    ("Kabels en verbruik (in bezit)", "USB-C datakabel", "Eigen kabel", 1, None, "al in bezit",
     "-", "", ""),
    ("Kabels en verbruik (in bezit)", "Dupont-/siliconendraad", "Heeft de gebruiker", 1, None,
     "al in bezit", "-", "", ""),
    ("Kabels en verbruik (in bezit)", "USB A-kabel LoRa-ontvanger",
     "USB-A naar USB-C voor de XIAO (heeft de gebruiker)", 1, None, "al in bezit", "-", "", ""),
    ("Kabels en verbruik (in bezit)", "Gereedschap",
     "Schuifmaat, soldeerbout, tin, flux, multimeter, USB-serieel adapter", 1, None,
     "al in bezit", "-", "", ""),

    ("Mock-up (vliegtuigje)", "Arduino", "Arduino Uno (heeft de gebruiker thuis)", 1, None, "al in bezit", "-",
     "", "Referentie antratek: Arduino Uno Rev3 (EUR 41,75)"),
    ("Mock-up (vliegtuigje)", "Servo's", "Bestaande voorraad (> 3)", 3, None, "al in bezit", "-",
     "", ""),
    ("Mock-up (vliegtuigje)", "Servo-voeding", "Aparte buck-converter", 1, None, "al in bezit",
     "-", "", ""),
    ("Mock-up (vliegtuigje)", "Romp en roeren", "Eigen 3D-print", 1, None, "al in bezit", "-",
     "", ""),
]

KOPPEN = ["Categorie", "Functie", "Onderdeel", "Aantal", "Prijs/st (EUR)", "Totaal (EUR)",
          "Status", "Leverancier", "Link", "Opmerking"]
BREEDTES = [24, 30, 46, 8, 14, 14, 12, 14, 52, 52]

KLEUR_STATUS = {
    "antratek": "C6EFCE",
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
    ws["A1"] = "Bestellijst G-Stem meettoestel - prijzen incl. btw, gezocht op antratek.be (2026-10-06)"
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

    # Totaalregel (enkel antratek-regels)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    cel = ws.cell(row=r, column=1, value="Totaal te bestellen bij antratek (excl. geen-link-onderdelen)")
    cel.font = Font(bold=True)
    cel.alignment = Alignment(horizontal="right", vertical="center")
    tot_cel = ws.cell(row=r, column=6)
    tot_cel.value = "=SUMIF(G3:G%d,\"antratek\",F3:F%d)" % (r - 1, r - 1)
    tot_cel.number_format = '#,##0.00 "EUR"'
    tot_cel.font = Font(bold=True)
    for c in range(1, 11):
        ws.cell(row=r, column=c).border = Border(top=Side(style="medium", color=KLEUR_KOP),
                                                 bottom=dun, left=dun, right=dun)
    ws.cell(row=r, column=6).alignment = Alignment(horizontal="right")
    r += 2

    ws.cell(row=r, column=1,
            value="Let op: prijzen onder voorbehoud (anratek 2026-10-06). Niet-gevonden onderdelen "
                  "staan op 'geen link' en zijn niet in het totaal opgenomen.").font = Font(italic=True, size=9)

    ws.freeze_panes = "A3"
    ws.auto_filter.ref = "A2:J%d" % (r - 3)

    # Tweede blad: volledige uitleg tags
    ws2 = wb.create_sheet("Legende")
    ws2.append(["Tag", "Betekenis"])
    for cel in ws2[1]:
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = PatternFill("solid", fgColor=KLEUR_KOP)
    for tag, bet in [
        ("antratek", "Aankooplink gevonden op antratek.be"),
        ("al in bezit", "Heeft de gebruiker al; niet aankopen"),
        ("geen link", "Niet gevonden op antratek.be; niet elders gezocht"),
        ("niet nodig", "Bewust niet voorzien"),
    ]:
        ws2.append([tag, bet])
    ws2.column_dimensions["A"].width = 14
    ws2.column_dimensions["B"].width = 60

    doel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Bestellijst-GSTEM.xlsx")
    wb.save(doel)
    print("Opgeslagen:", doel)


if __name__ == "__main__":
    bouw()
