# -*- coding: utf-8 -*-
"""
Stelt het controleblad samen voor de G-Stem Blender-mock-up.

Leest de review-renders en de gemeten maten (review_metingen.json) en maakt
een geannoteerd blad: bovenaanzicht met maatlijnen en een 10 mm-raster,
voor- en zijaanzicht, een overzicht, en een tabel met gemeten versus
datasheet-maten.

> Let op: de map `documenten/blender/` (met de review-renders) is op 2026-10-06
> verwijderd. Dit script is bewaard als naslag maar kan pas opnieuw draaien als
> die renders teruggehaald zijn uit git (commit 28e4fae).

Uitvoeren:  python documenten/scripts/build-controleblad.py
"""

import json
import os
from PIL import Image, ImageDraw, ImageFont

# Script staat in documenten/scripts/.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REV = os.path.join(ROOT, "blender", "review")  # bron verwijderd; zie docstring
OUT = os.path.join(ROOT, "pcb", "review-mockup-controleblad.png")

DATE = "2026-10-06"
SHEET = (2400, 1700)
BG = (238, 236, 230)
INK = (28, 30, 34)
GREY = (120, 122, 126)
YEL = (255, 205, 60)
RED = (188, 42, 28)
GREEN = (24, 128, 62)

rep = json.load(open(os.path.join(REV, "review_metingen.json"),
                     encoding="utf-8"))


def font(size, bold=False):
    cands = ([r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\segoeuib.ttf"]
             if bold else
             [r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\segoeui.ttf"])
    for c in cands:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    try:
        return ImageFont.load_default(size)
    except Exception:
        return ImageFont.load_default()


F = {}


def get_f(k, size, bold=False):
    key = (k, size, bold)
    if key not in F:
        F[key] = font(size, bold)
    return F[key]


class Panel(object):
    """Zet mm-coordinaten om naar pixels van een gerenderd aanzicht."""

    def __init__(self, view, scale, ox, oy):
        v = rep["views"][view]
        self.ppm = v["px_per_mm"]
        self.rx, self.ry = v["res"]
        self.cx, self.cy = v["center"]
        self.s = scale
        self.ox, self.oy = ox, oy

    def px(self, a, b):
        x = self.ox + self.s * (self.rx / 2.0 + (a - self.cx) * self.ppm)
        y = self.oy + self.s * (self.ry / 2.0 - (b - self.cy) * self.ppm)
        return (x, y)

    @property
    def wh(self):
        return (int(self.rx * self.s), int(self.ry * self.s))


def label(d, xy, text, f, fill=INK, anchor="la", shadow=False):
    if shadow:
        d.text((xy[0] + 1, xy[1] + 1), text, font=f, fill=(0, 0, 0),
               anchor=anchor)
    d.text(xy, text, font=f, fill=fill, anchor=anchor)


def dim_h(d, p, y_mm, x1_mm, x2_mm, text, f, col=RED, tick=6):
    a = p.px(x1_mm, y_mm)
    b = p.px(x2_mm, y_mm)
    d.line([a, b], fill=col, width=2)
    for q in (a, b):
        d.line([(q[0], q[1] - tick), (q[0], q[1] + tick)], fill=col, width=2)
    m = ((a[0] + b[0]) / 2.0, a[1])
    tw = d.textlength(text, font=f)
    d.rectangle([m[0] - tw / 2 - 5, m[1] - 19, m[0] + tw / 2 + 5, m[1] - 1],
                fill=BG)
    d.text((m[0], m[1] - 10), text, font=f, fill=col, anchor="mm")


def dim_v(d, p, x_mm, y1_mm, y2_mm, text, f, col=RED, tick=6):
    a = p.px(x_mm, y1_mm)
    b = p.px(x_mm, y2_mm)
    d.line([a, b], fill=col, width=2)
    for q in (a, b):
        d.line([(q[0] - tick, q[1]), (q[0] + tick, q[1])], fill=col, width=2)
    m = (a[0], (a[1] + b[1]) / 2.0)
    d.rectangle([m[0] - 30, m[1] - 10, m[0] + 30, m[1] + 10], fill=BG)
    d.text((m[0], m[1]), text, font=f, fill=col, anchor="mm")


def main():
    sheet = Image.new("RGB", SHEET, BG)
    d = ImageDraw.Draw(sheet)

    # ---------------- kop ----------------
    d.rectangle([0, 0, SHEET[0], 78], fill=(30, 32, 36))
    d.text((40, 16), "G-STEM  draagprint  -  controleblad Blender-mock-up",
           font=get_f("t", 34, True), fill=(240, 240, 238))
    n_err = len(rep["errors"])
    n_lab = len(rep["bad_labels"]) + len(rep["label_conflicts"])
    n_ovl = len(rep["bad_overlaps"])
    ok = (n_err == 0 and n_lab == 0 and n_ovl == 0)
    d.text((SHEET[0] - 40, 26),
           "controle: %s   (%d maatafwijkingen, %d labelconflicten, "
           "%d overlap)   %s" % ("ALLES OK" if ok else "FOUTEN",
                                 n_err, n_lab, n_ovl, DATE),
           font=get_f("s", 20, True), fill=(120, 220, 150) if ok else
           (255, 140, 120), anchor="ra")

    # ---------------- bovenaanzicht ----------------
    top = Panel("top", 0.86, 50, 110)
    img = Image.open(os.path.join(REV, "top.png")).convert("RGB")
    img = img.resize(top.wh, Image.LANCZOS)
    sheet.paste(img, (int(top.ox), int(top.oy)))
    d.rectangle([top.ox, top.oy, top.ox + top.wh[0], top.oy + top.wh[1]],
                outline=(150, 148, 142), width=2)
    d.text((top.ox, top.oy + top.wh[1] + 8),
           "1. Bovenaanzicht (orthografisch, maatvast)",
           font=get_f("c", 20, True), fill=INK)

    # 10 mm-raster over de print
    for x in range(-50, 51, 10):
        a = top.px(x, -37.5)
        b = top.px(x, 37.5)
        d.line([a, b], fill=(255, 255, 255, 40), width=1)
    for y in range(-30, 31, 10):
        a = top.px(-50, y)
        b = top.px(50, y)
        d.line([a, b], fill=(255, 255, 255, 40), width=1)

    # bordafmetingen
    dim_h(d, top, -42.5, -50, 50, "100,0 mm", get_f("d", 19, True))
    dim_v(d, top, -55.5, -37.5, 37.5, "75,0", get_f("d", 18, True))

    # M3-gat detail
    hx, hy = 46.0, 33.5
    c = top.px(hx, hy)
    r = 1.6 * top.ppm * top.s
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], outline=YEL, width=3)
    r2 = 4 * top.ppm * top.s
    d.ellipse([c[0] - r2, c[1] - r2, c[0] + r2, c[1] + r2], outline=YEL,
              width=1)
    d.line([c, (c[0] - 120, c[1] - 90)], fill=YEL, width=2)
    label(d, (c[0] - 125, c[1] - 96),
          "4x M3:  Ø3,2  op 4 mm van de rand", get_f("a", 17, True),
          fill=(60, 50, 10), anchor="ra", shadow=False)

    # maatlijnen over de modules
    parts = {p["name"]: p for p in rep["parts"]}
    callouts = [
        ("Draagprint", True, True), ("U5_gnss_pcb", True, True),
        ("U6_bno085_pcb", True, True), ("U7_bmp581_pcb", True, False),
        ("U1_xiao_pcb", True, True), ("U2_buck_pcb", True, False),
        ("U4_txb_pcb", True, False), ("J2_term_body", True, False),
        ("J1_barrel_body", True, False), ("U3_ldo", False, False),
        ("C1_elco", False, False), ("F1_ptc", False, False),
        ("D1_tvs", False, False), ("U1_sx1262", False, False),
    ]
    for name, do_w, do_h in callouts:
        p = parts.get(name)
        if not p or name == "Draagprint":
            continue
        w, h = p["got"][0], p["got"][1]
        cx, cy = p["center"]
        f = get_f("m", 16, True)
        if do_w:
            dim_h(d, top, cy, cx - w / 2.0, cx + w / 2.0,
                  "%.1f" % w, f, col=YEL, tick=5)
        if do_h:
            dim_v(d, top, cx, cy - h / 2.0, cy + h / 2.0,
                  "%.1f" % h, f, col=YEL, tick=5)

    # ---------------- voor- en zijaanzicht ----------------
    fr = Panel("front", 0.70, 1330, 110)
    img = Image.open(os.path.join(REV, "front.png")).convert("RGB")
    sheet.paste(img.resize(fr.wh, Image.LANCZOS),
                (int(fr.ox), int(fr.oy)))
    d.rectangle([fr.ox, fr.oy, fr.ox + fr.wh[0], fr.oy + fr.wh[1]],
                outline=(150, 148, 142), width=2)
    d.text((fr.ox, fr.oy + fr.wh[1] + 8),
           "2. Vooraanzicht vanaf de voorzijde (X-Z)",
           font=get_f("c", 20, True), fill=INK)
    st = rep["stack"]
    htot = st.get("total_height_mm", 0)
    dim_v(d, fr, 52, 0, htot, "%.2f" % htot, get_f("d", 18, True))
    dim_h(d, fr, -12, -50, 50, "100,0 mm", get_f("d", 18, True))
    d.text((fr.ox, fr.oy + fr.wh[1] + 34),
           "XIAO-socket %.1f mm hoog; kit-draagprint rust op de sockets "
           "(gap %.1f mm); totale stapel %.2f mm"
           % (st["U1_sock_1"][1] - st["U1_sock_1"][0],
              st.get("kit_on_socket_gap", 0), htot),
           font=get_f("a", 17), fill=(40, 40, 44))

    sd = Panel("side", 0.70, 1330, 560)
    img = Image.open(os.path.join(REV, "side.png")).convert("RGB")
    sheet.paste(img.resize(sd.wh, Image.LANCZOS),
                (int(sd.ox), int(sd.oy)))
    d.rectangle([sd.ox, sd.oy, sd.ox + sd.wh[0], sd.oy + sd.wh[1]],
                outline=(150, 148, 142), width=2)
    d.text((sd.ox, sd.oy + sd.wh[1] + 8),
           "3. Zijaanzicht vanaf rechts (Y-Z)",
           font=get_f("c", 20, True), fill=INK)
    dim_h(d, sd, -12, -37.5, 37.5, "75,0 mm", get_f("d", 18, True))

    # ---------------- overzicht ----------------
    iso = Image.open(os.path.join(REV, "iso.png")).convert("RGB")
    iw = 1000
    ih = int(iso.height * iw / float(iso.width))
    if 980 + ih > SHEET[1] - 30:
        ih = SHEET[1] - 30 - 980
        iw = int(iso.width * ih / float(iso.height))
    sheet.paste(iso.resize((iw, ih), Image.LANCZOS), (1330, 980))
    d.rectangle([1330, 980, 1330 + iw, 980 + ih], outline=(150, 148, 142),
                width=2)
    d.text((1330, 980 + ih + 6), "4. Overzicht (print zonder toebehoren)",
           font=get_f("c", 20, True), fill=INK)

    # ---------------- tabel ----------------
    tx, ty = 60, 1090
    d.text((tx, ty - 34), "5. Gemeten maten tegenover de datasheet",
           font=get_f("c", 20, True), fill=INK)
    cols = [(tx, "onderdeel"), (tx + 300, "gemeten (mm)"),
            (tx + 560, "datasheet (mm)"), (tx + 830, "")]
    d.line([(tx, ty), (tx + 900, ty)], fill=INK, width=2)
    for cx0, name in cols:
        d.text((cx0, ty + 6), name, font=get_f("h", 17, True), fill=GREY)
    y = ty + 34
    rows = []
    for p in rep["parts"]:
        rows.append((p["name"], "%.1f x %.1f x %.1f" % tuple(p["got"]),
                     "%.1f x %.1f x %.1f" % tuple(p["exp"]), p["ok"]))
    rows.append(("-- XIAO-stapel", "kit op socket: %.1f mm" %
                 st.get("kit_on_socket_gap", 0), "0,0 mm (rust op socket)",
                 abs(st.get("kit_on_socket_gap", 0)) < 0.01))
    rows.append(("-- totale hoogte", "%.2f mm" % htot, "± 21 mm (incl. USB)",
                 True))
    for name, got, exp, ook in rows:
        if ook:
            d.ellipse([tx - 14, y + 4, tx - 2, y + 16], fill=GREEN)
        else:
            d.ellipse([tx - 14, y + 4, tx - 2, y + 16], fill=RED)
        d.text((tx, y), name, font=get_f("r", 16), fill=INK)
        d.text((tx + 300, y), got, font=get_f("r", 16), fill=INK)
        d.text((tx + 560, y), exp, font=get_f("r", 16), fill=GREY)
        if not ook:
            d.text((tx + 830, y), "AFWIJKING", font=get_f("r", 15, True),
                   fill=RED)
        d.line([(tx, y + 22), (tx + 900, y + 22)], fill=(205, 203, 197),
               width=1)
        y += 24

    # legenda
    ly = y + 16
    d.ellipse([tx, ly + 3, tx + 12, ly + 15], fill=GREEN)
    d.text((tx + 20, ly), "gemeten = datasheet", font=get_f("r", 16), fill=INK)
    d.ellipse([tx + 260, ly + 3, tx + 272, ly + 15], fill=YEL)
    d.text((tx + 280, ly), "maatlijn (mm)", font=get_f("r", 16), fill=INK)
    d.ellipse([tx + 470, ly + 3, tx + 482, ly + 15], fill=RED)
    d.text((tx + 490, ly), "buitenmaat / controle", font=get_f("r", 16),
           fill=INK)
    d.text((tx, ly + 30),
           "Alle maten in mm. De plaatsing van de onderdelen op de print is "
           "een VOORSTEL: de KiCad-layout bestaat nog niet.",
           font=get_f("r", 16, True), fill=(150, 40, 30))

    sheet.save(OUT)
    print("controleblad:", OUT, sheet.size)


main()
