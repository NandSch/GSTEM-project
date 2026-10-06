# -*- coding: utf-8 -*-
"""
Bouwt een PNG-schets van de eind-PCB (draagprint) van het G-Stem meettoestel,
met alle breakout-modules, de losse componenten, de Arduino Uno en alle
verbindingen. Schematisch, niet op schaal.

Output: documenten/pcb/PCB-eindbeeld.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1800
SS = 2  # supersampling

img = Image.new("RGB", (W * SS, H * SS), "#eef2f7")
d = ImageDraw.Draw(img)

_fonts = {}
def font(size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        name = "segoeuib.ttf" if bold else "segoeui.ttf"
        _fonts[key] = ImageFont.truetype("C:/Windows/Fonts/" + name, size * SS)
    return _fonts[key]

def rect(x, y, w, h, fill, outline=None, width=2, radius=10):
    d.rounded_rectangle([x * SS, y * SS, (x + w) * SS, (y + h) * SS],
                        radius=radius * SS, fill=fill, outline=outline,
                        width=width * SS)

def line(pts, color, width=2, dashed=False, dash=12, gap=8):
    if not dashed:
        d.line([(p[0] * SS, p[1] * SS) for p in pts], fill=color,
               width=width * SS, joint="curve")
        return
    import math
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]; x2, y2 = pts[i + 1]
        dist = math.hypot(x2 - x1, y2 - y1)
        if dist == 0:
            continue
        n = int(dist // (dash + gap)) + 1
        for k in range(n):
            t0 = (k * (dash + gap)) / dist
            t1 = min((k * (dash + gap) + dash) / dist, 1.0)
            if t0 >= 1:
                break
            xa, ya = x1 + (x2 - x1) * t0, y1 + (y2 - y1) * t0
            xb, yb = x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1
            d.line([(xa * SS, ya * SS), (xb * SS, yb * SS)], fill=color, width=width * SS)

def circle(cx, cy, r, fill, outline=None, width=1):
    d.ellipse([(cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS],
              fill=fill, outline=outline, width=width * SS)

def dot(cx, cy, color, r=5):
    circle(cx, cy, r, color)

def text(x, y, s, size=16, color="#0f172a", anchor="la", bold=False):
    d.text((x * SS, y * SS), s, font=font(size, bold), fill=color, anchor=anchor)

def panel(x, y, w, h, title, accent, fill="#0f172a"):
    rect(x, y, w, h, fill, accent, 2, 14)
    text(x + 16, y + 12, title, 21, accent, bold=True)

# ---------------------------------------------------------------- kleuren
C = {
    "bg": "#eef2f7",
    "board": "#14532d",
    "board_edge": "#0a2e1a",
    "panel": "#0f172a",
    "panel2": "#1e293b",
    "body": "#e2e8f0",
    "muted": "#94a3b8",
    "vbat": "#ef4444",
    "v5": "#f97316",
    "v33": "#eab308",
    "i2c": "#3b82f6",
    "gnss": "#22c55e",
    "ard": "#14b8a6",
    "rf": "#ec4899",
    "gnd": "#94a3b8",
    "power": "#38bdf8",
    "xiao": "#f59e0b",
    "lora": "#a78bfa",
    "imu": "#4ade80",
    "gnssm": "#22d3ee",
    "txb": "#f87171",
    "term": "#fca5a5",
    "arduino": "#fb7185",
}

# ---------------------------------------------------------------- titel
text(40, 26, "G-Stem meettoestel - eind-PCB (draagprint) met modules, Arduino en verbindingen",
     34, "#0f172a", bold=True)
text(40, 74, "Schematisch, niet op schaal. Pinout = voorstel. "
             "Kruising zonder stip = geen verbinding.", 19, "#475569")

# ---------------------------------------------------------------- bord
BX, BY, BW, BH = 40, 120, 1560, 1520
rect(BX, BY, BW, BH, C["board"], C["board_edge"], 4, 20)
rect(BX + 12, BY + 12, BW - 24, BH - 24, None, "#22c55e", 1, 16)
# mounting holes
for (mx, my) in [(85, 165), (1555, 165), (85, 1595), (1555, 1595)]:
    circle(mx, my, 16, C["bg"], "#334155", 2)
    text(mx, my, "M3", 12, "#334155", anchor="mm")

# ---------------------------------------------------------------- sporen (eerst, panelen erover)
# machtbussen
line([(100, 900), (1500, 900)], C["gnd"], 7)
line([(100, 928), (1500, 928)], C["v5"], 7)
line([(100, 956), (1500, 956)], C["v33"], 7)
text(1508, 886, "GND-bus", 13, C["gnd"], anchor="ra")
text(1508, 914, "5 V-bus", 13, C["v5"], anchor="ra")
text(1508, 942, "3,3 V-bus", 13, C["v33"], anchor="ra")

# voeding -> bussen
line([(140, 642), (140, 956)], C["v33"], 3)
line([(175, 642), (175, 928)], C["v5"], 3)
line([(210, 642), (210, 900)], C["gnd"], 3)
for (x, y) in [(140, 956), (175, 928), (210, 900)]:
    dot(x, y, {"956": C["v33"], "928": C["v5"], "900": C["gnd"]}[str(y)])

# --- 5 V -> XIAO / GNSS / TXB / terminal
line([(600, 640), (585, 640), (585, 250), (610, 250)], C["v5"], 3)
line([(585, 640), (585, 870)], C["v5"], 3)
line([(585, 870), (860, 870), (860, 990)], C["v5"], 3)          # GNSS VCC
line([(585, 870), (180, 870), (180, 928)], C["v5"], 3)           # TXB VCCB via bus
dot(585, 928, C["v5"])
line([(585, 870), (585, 1245), (230, 1245), (230, 1280)], C["v5"], 3)  # terminal +5V

# --- 3,3 V -> XIAO / BNO / BMP / TXB VCCA
line([(600, 640), (565, 640), (565, 330), (610, 330)], C["v33"], 3)
line([(565, 640), (565, 620), (650, 620), (650, 650)], C["v33"], 3)   # BNO VIN
line([(650, 620), (940, 620), (940, 650)], C["v33"], 3)               # BMP VIN
dot(940, 620, C["v33"])
line([(565, 640), (565, 956)], C["v33"], 3)
line([(565, 990), (120, 990), (120, 956)], C["v33"], 3)               # TXB VCCA
dot(120, 956, C["v33"])

# --- GND -> modules (stubs)
for (sx, sy, tx, ty) in [(690, 900, 690, 650), (980, 900, 980, 650),
                         (900, 900, 900, 990), (220, 900, 220, 990),
                         (150, 900, 150, 1280)]:
    line([(sx, sy), (tx, ty)], C["gnd"], 2)
    dot(sx, sy, C["gnd"])
line([(585, 900), (585, 290), (610, 290)], C["gnd"], 2)
dot(585, 900, C["gnd"])

# --- I2C: XIAO D4/D5 -> BNO + BMP
line([(1160, 250), (1190, 250), (1190, 615), (750, 615), (750, 650)], C["i2c"], 3)
line([(1040, 615), (1040, 650)], C["i2c"], 3)
dot(1040, 615, C["i2c"])
line([(1160, 290), (1200, 290), (1200, 635), (790, 635), (790, 650)], C["i2c"], 3)
line([(1080, 635), (1080, 650)], C["i2c"], 3)
dot(1080, 635, C["i2c"])

# --- GNSS UART -> XIAO D3(RX) / D2(TX)
line([(980, 990), (980, 870), (585, 870), (585, 430), (610, 430)], C["gnss"], 3)
line([(1010, 990), (1010, 884), (575, 884), (575, 390), (610, 390)], C["gnss"], 3)

# --- Arduino UART via TXB0104
line([(1160, 350), (1170, 350), (1170, 150), (60, 150), (60, 1080), (70, 1080)], C["ard"], 3)
line([(1160, 390), (1165, 390), (1165, 168), (55, 168), (55, 1120), (70, 1120)], C["ard"], 3)
# TXB B-zijde -> schroefklem
line([(540, 1080), (560, 1080), (560, 1250), (320, 1250), (320, 1280)], C["ard"], 3)
line([(540, 1120), (570, 1120), (570, 1265), (400, 1265), (400, 1280)], C["ard"], 3)

# --- 4-aderige kabel naar Arduino
line([(540, 1410), (1630, 1410), (1630, 430), (1650, 430)], "#0ea5e9", 8)
line([(540, 1410), (1630, 1410), (1630, 430), (1650, 430)], "#e0f2fe", 2)
text(1585, 1385, "4-aderige kabel", 14, "#0f172a", anchor="ra", bold=True)
text(1585, 1405, "GND / +5 V / TX / RX", 13, "#0f172a", anchor="ra")

# --- LoRa RF-pad
line([(1160, 500), (1430, 500), (1430, 300), (1560, 300)], C["rf"], 3, dashed=True)
rect(1470, 200, 120, 200, None, C["rf"], 2, 10)

# ================================================================ PANELEN OP HET BORD
# ---- VOEDING
panel(70, 180, 470, 460, "VOEDING (op de print)", C["power"])
vol = [
    ("J1", "7,4 V-accu / barrel jack"),
    ("F1", "2 A PTC-zekering (herstelbaar)"),
    ("Q1", "DMG2301L P-MOSFET ompoolbeveiliging"),
    ("D1", "TVS SMBJ10A (spike-bescherming)"),
    ("U2", "Buck-converter -> 5 V (losse module)"),
    ("C1", "Bulk-elco 100 uF / 16 V"),
    ("U3", "LDO AP2112K-3.3 -> 3,3 V"),
    ("D2", "Power-LED rood + 330 ohm"),
]
yy = 232
for ref, desc in vol:
    rect(90, yy, 430, 40, C["panel2"], "#334155", 1, 7)
    text(102, yy + 10, ref, 15, C["power"], bold=True)
    text(150, yy + 10, desc, 15, C["body"])
    if yy < 232 + 7 * 50:
        line([(505, yy + 40), (505, yy + 50)], C["power"], 2)
        line([(501, yy + 46), (505, yy + 50), (509, yy + 46)], C["power"], 2)
    yy += 50
text(305, 634, "3,3 V   5 V   GND", 13, C["muted"], anchor="ma")

# ---- XIAO
panel(600, 190, 560, 400, "U1  Seeed XIAO ESP32S3 + Wio-SX1262 (kit)", C["xiao"])
text(616, 218, "socket: dual-wipe 2,54 mm - ESP32 + SX1262 LoRa in een module",
     14, C["muted"])
rect(640, 240, 480, 320, "#020617", "#334155", 2, 10)
text(880, 262, "ESP32-S3 (240 MHz) - SX1262 sub-GHz - USB-C - LiPo-lader",
     14, C["body"], anchor="ma")
text(880, 292, "leest sensoren, sensorfusie (Kalman), CSV naar Arduino",
     14, C["body"], anchor="ma")
# pinnen
pins_left = [("5V", 250, C["v5"]), ("GND", 290, C["gnd"]), ("3V3", 330, C["v33"]),
             ("D2 / TX  GPIO3", 390, C["gnss"]), ("D3 / RX  GPIO4", 430, C["gnss"])]
for name, py, col in pins_left:
    rect(600, py - 7, 16, 14, "#6b7280", "#111827", 1, 3)
    text(625, py, name, 14, col)
pins_right = [("D4 / SDA  GPIO5", 250, C["i2c"]), ("D5 / SCL  GPIO6", 290, C["i2c"]),
              ("D6 / TX  GPIO43", 350, C["ard"]), ("D7 / RX  GPIO44", 390, C["ard"])]
for name, py, col in pins_right:
    rect(1144, py - 7, 16, 14, "#6b7280", "#111827", 1, 3)
    text(1135, py, name, 14, col, anchor="ra")
text(880, 470, "I2C: sensoren   |   D2/D3: GNSS   |   D6/D7: via TXB0104 naar Arduino",
     14, C["muted"], anchor="ma")
text(880, 540, "IPEX/U.FL -> SMA bulkhead (LoRa-antenne buiten de romp)",
     14, C["lora"], anchor="ma")

# ---- LoRa antenne
panel(1210, 180, 350, 250, "LoRa-antenne", C["lora"])
text(1228, 220, "IPEX/U.FL -> SMA female", 15, C["body"])
text(1228, 244, "bulkhead pigtail (150 mm)", 15, C["body"])
text(1228, 276, "Antenne zit bij de kit.", 14, C["muted"])
text(1228, 300, "Keep-out: geen koper onder", 14, C["body"])
text(1228, 322, "de antenne.", 14, C["body"])
text(1228, 360, "868/915 MHz sub-GHz", 14, C["lora"])

# ---- BNO085
panel(600, 650, 260, 200, "BNO085 (IMU)", C["imu"])
text(616, 690, "9-DoF oriëntatie", 15, C["body"])
text(616, 712, "I2C 0x4A/0x4B", 15, C["body"])
text(616, 734, "3,3 V, pull-ups aanwezig", 14, C["muted"])
text(616, 764, "trillingsdemping", 14, C["imu"])
# BMP581
panel(890, 650, 260, 200, "BMP581 (barometer)", C["imu"])
text(906, 690, "druk + temperatuur", 15, C["body"])
text(906, 712, "I2C 0x46/0x47", 15, C["body"])
text(906, 734, "3,3 V, pull-ups aanwezig", 14, C["muted"])
text(906, 764, "weg van de warmte", 14, C["imu"])

# ---- TXB0104
panel(70, 990, 470, 230, "U4  TXB0104 level shifter (3,3 V <-> 5 V)", C["txb"])
text(86, 1026, "A-zijde: XIAO 3,3 V   B-zijde: Arduino 5 V", 14, C["body"])
text(86, 1050, "VCCA 3,3 V - VCCB 5 V - 4 kanalen bidirectioneel", 14, C["body"])
text(86, 1084, "A1 (3,3 V TX)", 14, C["ard"])
text(86, 1124, "A2 (3,3 V RX)", 14, C["ard"])
text(452, 1084, "B1 (5 V TX)", 14, C["ard"], anchor="ra")
text(452, 1124, "B2 (5 V RX)", 14, C["ard"], anchor="ra")
text(86, 1180, "Enkel voor de UART naar de Arduino.", 13, C["muted"])
text(86, 1200, "I2C blijft volledig 3,3 V.", 13, C["muted"])

# ---- schroefklem
panel(70, 1280, 470, 250, "J2  4-pins schroefklem 3,5 mm (KF128/KF301)", C["term"])
for name, px in [("GND", 150), ("+5 V", 230), ("TX", 320), ("RX", 400)]:
    rect(px - 22, 1350, 44, 34, C["panel2"], C["term"], 1, 5)
    text(px, 1367, name, 15, C["body"], anchor="mm", bold=True)
text(305, 1430, "UART naar de Arduino (CSV), gemeenschappelijke ground,",
     14, C["body"], anchor="ma")
text(305, 1452, "5 V-voeding voor de servo-rail.", 14, C["body"], anchor="ma")
text(305, 1490, "Kabel naar de Arduino rechts.", 13, C["muted"], anchor="ma")

# ---- GNSS
panel(800, 990, 740, 400, "U5  Quectel LC29H(DA) RTK-GNSS", C["gnssm"])
text(816, 1028, "dual-band L1+L5, RTK-rover, centimeter-niveau", 15, C["body"])
text(816, 1052, "UART 3,3 V (TX/RX) + PPS-uitgang", 15, C["body"])
text(816, 1076, "ingebouwde LNA + SAW-filter", 15, C["body"])
text(816, 1100, "USB-C voor configuratie", 14, C["muted"])
# pinnen
for name, px, col in [("VCC", 860, C["v5"]), ("GND", 900, C["gnd"]),
                      ("TX", 980, C["gnss"]), ("RX", 1010, C["gnss"]), ("PPS", 1040, C["muted"])]:
    rect(px - 9, 990, 18, 16, "#6b7280", "#111827", 1, 3)
    text(px, 1030, name, 14, col, anchor="ma")
# antenne
circle(1440, 1180, 44, "#0f172a", C["gnssm"], 3)
circle(1440, 1180, 17, C["gnssm"])
text(1440, 1262, "SMA actieve", 14, C["body"], anchor="ma")
text(1440, 1282, "L1/L5-antenne", 14, C["body"], anchor="ma")
line([(1350, 1180), (1396, 1180)], C["gnssm"], 3)
rect(1330, 1090, 220, 260, None, C["rf"], 2, 10)
text(1440, 1075, "antenne-keep-out", 13, C["rf"], anchor="ma")
text(816, 1360, "Correcties (RTCM/NTRIP) via de laptop; rover op de print.", 14, C["muted"])

# ================================================================ BUITEN HET BORD (rechts)
# ---- Arduino
panel(1650, 150, 870, 620, "Arduino Uno (mock-up vliegtuigje)", C["arduino"])
rect(1700, 230, 520, 430, "#005c8f", "#002b45", 3, 14)
text(1960, 260, "ARDUINO UNO", 22, "#e0f2fe", anchor="ma", bold=True)
text(1960, 292, "R3 / ATmega328P", 14, "#bae6fd", anchor="ma")
for name, py, col in [("RX (D0)  <- TX meettoestel", 350, C["ard"]),
                      ("TX (D1)  -> RX meettoestel", 386, C["ard"]),
                      ("5 V", 422, C["v5"]), ("GND", 452, C["gnd"]),
                      ("D9 / D10 / D11 -> servo's", 500, C["imu"])]:
    text(1730, py, name, 15, col)
line([(1650, 430), (1700, 430)], "#0ea5e9", 8)
text(1730, 560, "Ontvangt CSV-regels via de schroefklem,", 15, C["body"])
text(1730, 584, "parst ze en stelt de servo's in (real-time).", 15, C["body"])
text(1730, 620, "115200 baud, geen checksum, terminator \\n", 14, C["muted"])

# ---- Servo's
panel(1650, 800, 870, 330, "Servo's + aparte voeding", C["imu"])
for i, (nm, px) in enumerate([("Rolroer", 1740), ("Hoogteroer", 1955), ("Richtingsroer", 2170)]):
    rect(px, 870, 190, 120, C["panel2"], C["imu"], 2, 10)
    text(px + 95, 900, nm, 16, C["imu"], anchor="ma", bold=True)
    text(px + 95, 930, "servo", 14, C["body"], anchor="ma")
    text(px + 95, 952, "PWM D9/D10/D11", 13, C["muted"], anchor="ma")
    line([(px + 95, 800), (px + 95, 870)], C["imu"], 2, dashed=True)
text(2085, 1030, "Voeding: aparte buck-converter (niet vanaf de meetprint).",
     15, C["body"], anchor="ma")
text(2085, 1058, "> 3 servo's uit eigen voorraad, type vrij.", 14, C["muted"], anchor="ma")

# ---- LoRa ontvanger
panel(1650, 1160, 870, 470, "LoRa-ontvanger (USB-stick) + laptop", C["lora"])
rect(1720, 1240, 360, 180, C["panel2"], C["lora"], 2, 10)
text(1900, 1270, "2e XIAO ESP32S3 +", 15, C["body"], anchor="ma")
text(1900, 1292, "Wio-SX1262 kit", 15, C["body"], anchor="ma")
text(1900, 1320, "USB-A -> USB-C", 14, C["muted"], anchor="ma")
text(1900, 1348, "antenne inbegrepen", 14, C["lora"], anchor="ma")
# draadloos
line([(1500, 300), (1600, 300), (1600, 1180), (1720, 1180), (1720, 1240)],
     C["rf"], 3, dashed=True)
text(1615, 760, "LoRa draadloos", 15, C["rf"], bold=True)
text(1615, 782, "max. 4 km", 14, C["rf"])
# laptop
panel(2130, 1240, 360, 180, "Laptop - app", "#38bdf8")
text(2150, 1285, "verbindingscontrole", 14, C["body"])
text(2150, 1307, "kaart + tabel (live data)", 14, C["body"])
text(2150, 1329, "Code / API scherm", 14, C["body"])
text(2150, 1351, "start automatisch op", 13, C["muted"])
line([(2080, 1330), (2130, 1330)], "#38bdf8", 4)

# ================================================================ LEGENDA
ly = 1665
rect(40, ly, 2480, 115, "#ffffff", "#cbd5e1", 2, 12)
text(60, ly + 12, "Legenda", 18, "#0f172a", bold=True)
items = [
    (C["vbat"], "VBAT (ruwe accu)"),
    (C["v5"], "5 V"),
    (C["v33"], "3,3 V"),
    (C["gnd"], "GND"),
    (C["i2c"], "I2C (SDA/SCL)"),
    (C["gnss"], "GNSS UART"),
    (C["ard"], "Arduino UART via TXB0104"),
    (C["rf"], "LoRa RF / keep-out"),
]
x = 60
for col, lab in items:
    line([(x, ly + 62), (x + 34, ly + 62)], col, 5)
    text(x + 42, ly + 55, lab, 15, "#334155")
    x += 300
text(60, ly + 88, "Kruising zonder stip = geen verbinding.  Bron: GEBRUIKER/data/componenten.md, "
                  "bestelschema-pcb.md, pcb-schets.md  (2026-10-06).",
     13, "#64748b")

img = img.resize((W, H), Image.LANCZOS)
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "pcb", "PCB-eindbeeld.png")
img.save(OUT)
print("OK", img.size)
