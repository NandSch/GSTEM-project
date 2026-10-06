#!/usr/bin/env python3
"""Bouwt het verbindingsschema van de G-Stem meetmodule.

Uitvoeren:  python documenten/build-verbindingsschema.py

Levert twee bestanden op vanuit een enkele definitie:
  * documenten/Verbindingsschema-GSTEM.drawio   (te openen/bewerken in draw.io)
  * documenten/Verbindingsschema-GSTEM.png      (afbeelding, 2x supersampled)

Bevat de volledige keten: accu/barrel -> bescherming -> buck 5 V -> LDO 3,3 V,
power-LED, XIAO ESP32S3 + LoRa, IMU, barometer, RTK-GNSS, level shifter,
uitbreidingsconnector, Arduino + servo's + servo-buck en de LoRa-adapter/laptop.

Bron: GEBRUIKER/data/componenten.md, bestelschema-pcb.md, beslissingen.md,
documenten/PCB-schets.md en Ontwerp-meetmodule.md.
"""

import os
import html
from xml.sax.saxutils import escape as xesc

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
DRAWIO = os.path.join(OUT_DIR, "Verbindingsschema-GSTEM.drawio")
PNG = os.path.join(OUT_DIR, "Verbindingsschema-GSTEM.png")

SCALE = 2
W, H = 1560, 1150

# ---------------------------------------------------------------- kleuren
COLORS = {
    "power":  dict(fill=(248, 206, 204), line=(184, 84, 80),  text=(90, 26, 22)),
    "v5":     dict(fill=(255, 230, 204), line=(216, 150, 0),  text=(122, 74, 0)),
    "v33":    dict(fill=(255, 242, 204), line=(200, 168, 60), text=(120, 95, 0)),
    "mcu":    dict(fill=(218, 232, 252), line=(108, 142, 191), text=(25, 55, 105)),
    "sensor": dict(fill=(213, 232, 212), line=(120, 170, 95), text=(35, 80, 30)),
    "comms":  dict(fill=(225, 213, 231), line=(150, 115, 166), text=(70, 40, 90)),
    "iface":  dict(fill=(218, 232, 252), line=(108, 142, 191), text=(25, 55, 105)),
    "gnd":    dict(fill=(240, 240, 240), line=(100, 100, 100), text=(40, 40, 40)),
    "note":   dict(fill=(255, 250, 205), line=(200, 180, 80), text=(80, 70, 20)),
}
EDGE = {
    "vbat": (192, 57, 43),
    "v5":   (230, 126, 34),
    "v33":  (201, 162, 39),
    "i2c":  (46, 117, 182),
    "uart": (46, 139, 87),
    "rf":   (112, 48, 160),
    "gnd":  (120, 120, 120),
    "ctrl": (150, 70, 45),
    "usb":  (60, 60, 60),
}

# ---------------------------------------------------------------- nodes
# id: (x, y, w, h, kind, label)
NODES = [
    ("BAT",  40, 40, 160, 54, "power",
     "Accu 2S LiPo\n7,4 V (max 8,4 V)\nXT60 / JST-XH"),
    ("J1",   40, 120, 160, 54, "power",
     "Barrel-connector\n(DC-jack adapter +\nschroefklem) - alternatief"),
    ("F1",   250, 80, 170, 54, "power",
     "PTC-zekering 2 A\nLittelfuse 1812L200/16"),
    ("TVS",  250, 180, 170, 54, "power",
     "TVS SMBJ10A\n(spikebeveiliging -> GND)"),
    ("U2",   470, 80, 180, 54, "v5",
     "Buck-converter\n7,4 V -> 5 V\n(losse module)"),
    ("C1",   470, 180, 180, 54, "v5",
     "Bulk-elco 100 uF/16 V\n(op de 5 V-rail -> GND)"),
    ("N5V",  700, 80, 150, 54, "v5", "5 V-rail"),
    ("LED",  700, 180, 150, 54, "v5",
     "Power-LED rood\n+ 330 Ohm -> GND"),
    ("U3",   900, 80, 180, 54, "v33",
     "LDO AP2112K-3.3\n5 V -> 3,3 V"),
    ("N33",  1130, 80, 150, 54, "v33", "3,3 V-rail"),

    ("U1",   380, 430, 260, 130, "mcu",
     "XIAO ESP32S3\n+ Wio-SX1262 (LoRa 868 MHz)\nSPI intern - 5 V in - 3V3 uit\nUSB-C - eigen LiPo-lader (niet gebruikt)"),
    ("ANTL", 380, 300, 260, 60, "comms",
     "LoRa-antenne via IPEX/U.FL ->\nSMA female bulkhead pigtail"),

    ("U4",   820, 290, 230, 64, "sensor",
     "BNO085 - 9-DoF IMU\nI2C 0x28/0x29 - sensorfusie"),
    ("U5",   820, 380, 230, 64, "sensor",
     "BMP581 - barometer\nI2C - druk + temperatuur"),
    ("U6",   820, 470, 230, 84, "sensor",
     "LC29H(DA) - RTK-GNSS\nUART - RTK-rover\n(NTRIP-correctie via laptop)"),
    ("ANTG", 1120, 470, 190, 84, "comms",
     "Actieve dual-band\nL1/L5 GNSS-antenne\nSMA - LNA + ground plane"),

    ("U7",   820, 640, 230, 70, "iface",
     "TXB0104 level shifter\nVCCA 3,3 V <-> VCCB 5 V"),
    ("J2",   820, 740, 230, 70, "iface",
     "J2 uitbreidingsconnector\n4-pins 3,5 mm schroefklem\nGND / +5 V / TX / RX"),
    ("A1",   820, 860, 230, 70, "iface",
     "Arduino Uno\n(mock-up controller, 5 V logica)"),
    ("SRV",  820, 960, 230, 70, "comms",
     "3x servo\nrolroer - hoogteroer - richtingsroer"),
    ("UBK",  1080, 960, 190, 70, "v5",
     "Aparte buck-converter\n5 V servo-voeding (BEC)"),

    ("ADPT", 380, 800, 260, 70, "comms",
     "LoRa-adapter\n2e XIAO ESP32S3 + Wio-SX1262\n(USB naar laptop)"),
    ("LAP",  380, 900, 260, 70, "mcu",
     "Laptopapplicatie\nkaart - code - API"),

    ("N1",   40, 300, 230, 64, "note",
     "Ontkoppeling op de print:\n100 nF + 10 uF per module\n+ 100 uF bulk op 5 V"),
    ("N2",   40, 390, 230, 64, "note",
     "Sockets: dual-wipe (XIAO),\nprecisie/turned-pin (vaste modules)\n-> modules blijven vervangbaar"),
    ("N3",   40, 480, 230, 64, "note",
     "I2C-pull-ups zitten al op de BNO085-\nen BMP581-breakouts; 2 reserve-\nfootprints op de print"),

    ("GNDB", 40, 1080, 1450, 36, "gnd",
     "GND - gemeenschappelijke ground (alle modules, connectoren, level shifter en servo-voeding)"),

    ("LEG",  1320, 620, 210, 330, "note",
     "LEGENDE\n\nrood - VBAT (ruwe accu)\noranje - 5 V-rail\ngeel - 3,3 V-rail\nblauw - I2C-bus\ngroen - UART\npaars - LoRa / RF\ngrijs streeplijn - GND\n\nPijlen tonen de richting\nvan voeding of data"),
]

TITLE = "G-STEM meetmodule - verbindingsschema (voeding, ESP32-S3, sensoren, interface)"
SUBTITLE = "schematisch, niet op schaal  |  bron: componenten.md, bestelschema-pcb.md, PCB-schets.md"

# ---------------------------------------------------------------- edges
# (id, src, tgt, pts, edgecolor, label, dashed)
EDGES = [
    ("e1",  "BAT",  "F1",   [(120, 94), (120, 107), (250, 107)], "vbat", "7,4 V", False),
    ("e2",  "J1",   "F1",   [(200, 147), (225, 147), (225, 80), (250, 80)], "vbat", "of barrel", False),
    ("e3",  "F1",   "U2",   [(420, 107), (470, 107)], "vbat", "VBAT (ruw)", False),
    ("e4",  "F1",   "TVS",  [(400, 107), (445, 107), (445, 207), (420, 207)], "vbat", "na zekering", False),
    ("e5",  "TVS",  "GNDB", [(335, 234), (335, 1080)], "gnd", "GND", True),
    ("e6",  "U2",   "C1",   [(560, 134), (560, 180)], "v5", "5 V", False),
    ("e7",  "C1",   "N5V",  [(650, 207), (675, 207), (675, 107), (700, 107)], "v5", "", False),
    ("e8",  "C1",   "GNDB", [(500, 234), (500, 280), (310, 280), (310, 1080)], "gnd", "GND", True),
    ("e9",  "N5V",  "LED",  [(775, 134), (775, 180)], "v5", "5 V", False),
    ("e10", "N5V",  "U3",   [(850, 107), (900, 107)], "v5", "5 V", False),
    ("e11", "LED",  "GNDB", [(775, 234), (775, 1080)], "gnd", "GND", True),
    ("e12", "U3",   "N33",  [(1080, 107), (1130, 107)], "v33", "3,3 V", False),

    ("e13", "N33",  "U4",   [(1205, 134), (1205, 270), (1060, 270), (1060, 322), (1050, 322)],
     "v33", "3,3 V-rail", False),
    ("e14", "N33",  "U5",   [(1205, 134), (1205, 270), (1060, 270), (1060, 412), (1050, 412)],
     "v33", "", False),
    ("e15", "N33",  "U6",   [(1205, 134), (1205, 270), (1060, 270), (1060, 512), (1050, 512)],
     "v33", "", False),
    ("e16", "N33",  "U7",   [(1205, 134), (1205, 270), (1060, 270), (1060, 675), (1050, 675)],
     "v33", "VCCA", False),

    ("e17", "N5V",  "U1",   [(730, 134), (730, 440), (640, 440)], "v5", "5 V", False),
    ("e18", "N5V",  "U7",   [(815, 134), (815, 675), (820, 675)], "v5", "VCCB 5 V", False),
    ("e19", "U7",   "J2",   [(935, 710), (935, 740)], "uart", "TX/RX 5 V", False),
    ("e20", "N5V",  "J2",   [(815, 675), (815, 760), (820, 760)], "v5", "+5 V", False),

    ("e21", "U1",   "U4",   [(640, 470), (760, 470), (760, 322), (820, 322)],
     "i2c", "I2C SDA/SCL 3,3 V", False),
    ("e22", "U1",   "U5",   [(640, 505), (780, 505), (780, 412), (820, 412)], "i2c", "", False),
    ("e23", "U1",   "U6",   [(640, 540), (800, 540), (800, 512), (820, 512)],
     "uart", "UART1 TX/RX 3,3 V", False),
    ("e24", "U1",   "U7",   [(585, 560), (585, 685), (820, 685)], "uart", "UART2 (3,3 V-zijde)", False),

    ("e25", "U1",   "ANTL", [(510, 430), (510, 360)], "rf", "IPEX -> SMA", False),
    ("e26", "U6",   "ANTG", [(1050, 530), (1120, 530)], "rf", "SMA actieve L1/L5", False),

    ("e27", "U1",   "ADPT", [(460, 560), (460, 800)], "rf", "LoRa 868 MHz (draadloos)", True),
    ("e28", "ADPT", "LAP",  [(510, 870), (510, 900)], "usb", "USB-A -> USB-C (serieel)", False),

    ("e29", "J2",   "A1",   [(935, 810), (935, 860)], "uart", "GND / +5 V / TX / RX kabel", False),
    ("e30", "A1",   "SRV",  [(935, 930), (935, 960)], "ctrl", "PWM 3x servo", False),
    ("e31", "UBK",  "SRV",  [(1080, 995), (1050, 995)], "v5", "5 V servo-voeding", False),
]

# expliciete labelposities voor de edges waar het midden van de langste
# lijn op een knoop of een andere lijn zou vallen
LABEL_AT = {
    "e3":  (452, 125),
    "e5":  (348, 700),
    "e8":  (298, 770),
    "e11": (800, 700),
    "e13": (1140, 258),
    "e16": (1078, 700),
    "e18": (782, 600),
    "e20": (770, 775),
    "e26": (1085, 566),
    "e30": (995, 945),
    "e31": (1180, 940),
}


# ================================================================ draw.io
DRAWIO_NODE_STYLE = (
    "rounded=1;whiteSpace=wrap;html=1;arcSize=6;fontSize=12;fontStyle=1;"
    "verticalAlign=middle;align=center;spacing=4;"
)
DRAWIO_EDGE_STYLE = (
    "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeWidth=2;"
    "endArrow=block;endFill=1;fontSize=11;labelBackgroundColor=#FFFFFF;"
)


def build_drawio():
    parts = []
    parts.append('<mxfile host="app.diagrams.net" agent="G-STEM build-verbindingsschema.py" '
                 'version="24.7.17" type="device">')
    parts.append('  <diagram id="gstem-verbindingsschema" name="Verbindingsschema">')
    parts.append('    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" '
                 'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                 f'pageWidth="{W}" pageHeight="{H}" math="0" shadow="0">')
    parts.append('      <root>')
    parts.append('        <mxCell id="0" />')
    parts.append('        <mxCell id="1" parent="0" />')

    # titel + ondertitel (vrije tekst)
    parts.append(
        f'        <mxCell id="title" value="{xesc(TITLE)}" '
        'style="text;html=1;fontSize=16;fontStyle=1;align=left;verticalAlign=middle;" '
        'vertex="1" parent="1"><mxGeometry x="40" y="6" width="1200" height="24" '
        'as="geometry" /></mxCell>')
    parts.append(
        f'        <mxCell id="subtitle" value="{xesc(SUBTITLE)}" '
        'style="text;html=1;fontSize=10;fontColor=#666666;align=left;verticalAlign=middle;" '
        'vertex="1" parent="1"><mxGeometry x="1060" y="12" width="460" height="20" '
        'as="geometry" /></mxCell>')

    for nid, x, y, w, h, kind, label in NODES:
        c = COLORS[kind]
        fill = "#%02X%02X%02X" % c["fill"]
        line = "#%02X%02X%02X" % c["line"]
        text = "#%02X%02X%02X" % c["text"]
        dashed = "dashed=1;" if kind == "note" else ""
        style = (DRAWIO_NODE_STYLE + f"fillColor={fill};strokeColor={line};"
                 f"fontColor={text};{dashed}")
        parts.append(
            f'        <mxCell id="{nid}" value="{xesc(label)}" style="{style}" '
            f'vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" '
            f'height="{h}" as="geometry" /></mxCell>')

    for eid, src, tgt, pts, ckey, label, dashed in EDGES:
        col = "#%02X%02X%02X" % EDGE[ckey]
        style = DRAWIO_EDGE_STYLE + f"strokeColor={col};fontColor={col};"
        if dashed:
            style += "dashed=1;"
        waypoints = "".join(
            f'<mxPoint x="{px}" y="{py}" />' for px, py in pts[1:-1])
        parts.append(
            f'        <mxCell id="{eid}" value="{xesc(label)}" style="{style}" '
            f'edge="1" parent="1" source="{src}" target="{tgt}">'
            f'<mxGeometry relative="1" as="geometry">'
            f'<Array as="points">{waypoints}</Array>'
            f'</mxGeometry></mxCell>')

    parts.append('      </root>')
    parts.append('    </mxGraphModel>')
    parts.append('  </diagram>')
    parts.append('</mxfile>')
    return "\n".join(parts) + "\n"


# ================================================================ PNG
FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"


def load_font(size, bold=False):
    path = FONT_BOLD if bold else FONT_PATH
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def wrap(text, font, max_px, draw):
    lines = []
    for raw in text.split("\n"):
        if not raw:
            lines.append("")
            continue
        words = raw.split(" ")
        cur = ""
        for w in words:
            test = w if not cur else cur + " " + w
            if draw.textlength(test, font=font) <= max_px or not cur:
                cur = test
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def dashed_polyline(draw, pts, color, width, dash=10, gap=7):
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        dx, dy = x2 - x1, y2 - y1
        dist = (dx * dx + dy * dy) ** 0.5
        if dist == 0:
            continue
        ux, uy = dx / dist, dy / dist
        pos = 0.0
        while pos < dist:
            end = min(pos + dash, dist)
            draw.line([(x1 + ux * pos, y1 + uy * pos), (x1 + ux * end, y1 + uy * end)],
                      fill=color, width=width)
            pos = end + gap


def solid_polyline(draw, pts, color, width):
    draw.line(pts, fill=color, width=width, joint="curve")


def arrowhead(draw, pts, color, size=9):
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    dist = (dx * dx + dy * dy) ** 0.5 or 1
    ux, uy = dx / dist, dy / dist
    px, py = -uy, ux
    tip = (x2, y2)
    left = (x2 - ux * size + px * size * 0.55, y2 - uy * size + py * size * 0.55)
    right = (x2 - ux * size - px * size * 0.55, y2 - uy * size - py * size * 0.55)
    draw.polygon([tip, left, right], fill=color)


def render_png():
    S = SCALE
    img = Image.new("RGB", (W * S, H * S), "white")
    d = ImageDraw.Draw(img)

    f_title = load_font(16 * S, bold=True)
    f_sub = load_font(9 * S)
    f_node = load_font(11 * S, bold=True)
    f_node_s = load_font(9 * S)
    f_edge = load_font(9 * S, bold=True)

    # titel
    d.text((40 * S, 6 * S), TITLE, font=f_title, fill=(25, 25, 25))
    d.text((1060 * S, 10 * S), SUBTITLE, font=f_sub, fill=(110, 110, 110))

    # verbindingen eerst (onder de knoppen)
    for eid, src, tgt, pts, ckey, label, dashed in EDGES:
        color = EDGE[ckey]
        ppts = [(x * S, y * S) for x, y in pts]
        if dashed:
            dashed_polyline(d, ppts, color, 2 * S, dash=11 * S, gap=8 * S)
        else:
            solid_polyline(d, ppts, color, 2 * S)
        arrowhead(d, ppts, color, size=9 * S)
        if label:
            # label op het midden van het langste segment
            best, bestlen = None, -1
            for (x1, y1), (x2, y2) in zip(ppts[:-1], ppts[1:]):
                ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if ln > bestlen:
                    bestlen, best = ln, ((x1 + x2) / 2, (y1 + y2) / 2)
            if best:
                tw = d.textlength(label, font=f_edge)
                th = f_edge.size
                lab = LABEL_AT.get(eid)
                lx, ly = (lab[0] * S, lab[1] * S) if lab else best
                d.rectangle([lx - tw / 2 - 3, ly - th / 2 - 2,
                             lx + tw / 2 + 3, ly + th / 2 + 2], fill="white")
                d.text((lx - tw / 2, ly - th / 2), label, font=f_edge, fill=color)

    # knoppen
    for nid, x, y, w, h, kind, label in NODES:
        c = COLORS[kind]
        box = [x * S, y * S, (x + w) * S, (y + h) * S]
        d.rounded_rectangle(box, radius=8 * S, fill=c["fill"],
                            outline=c["line"], width=2 * S)
        font = f_node if kind != "note" and kind != "gnd" else f_node_s
        maxw = (w - 14) * S
        lines = wrap(label, font, maxw, d)
        line_h = font.size + 2 * S
        total = line_h * len(lines)
        ty = (y * S + ((h * S - total) / 2))
        for i, ln in enumerate(lines):
            tw = d.textlength(ln, font=font)
            d.text((x * S + (w * S - tw) / 2, ty + i * line_h), ln,
                   font=font, fill=c["text"])

    img.save(PNG)
    return img.size


def main():
    with open(DRAWIO, "w", encoding="utf-8") as f:
        f.write(build_drawio())
    size = render_png()
    print("geschreven:", DRAWIO)
    print("geschreven:", PNG, "->", size)


if __name__ == "__main__":
    main()
