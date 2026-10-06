# -*- coding: utf-8 -*-
"""
Audit van de G-Stem Blender-mock-up.

Meet de echte afmetingen van alle objecten in de scene en vergelijkt ze met de
datasheet-waarden. Controleert ook:
  * of alle printonderdelen binnen de bordrand (100 x 75 mm) blijven;
  * of silkscreen-labels niet over (grote) componenten heen vallen;
  * of onderdelen in Z door elkaar prikken (interpenetratie).

Uitvoeren in de live Blender-sessie (na het bouwsript), of los:
    exec(open(r".../audit_gstem_mockup.py").read())
"""

import bpy
from mathutils import Vector

MM = 0.001
BOARD_W, BOARD_D = 100.0, 75.0
BOARD_T = 1.6

# naam -> (verwacht X, verwacht Y, verwacht Z) in mm, None = niet controleren
EXPECT = {
    "U1_xiao_pcb":     (17.8, 21.0, 1.2),
    "U1_kit_pcb":      (17.8, 21.0, 1.2),
    "U1_sx1262":       (11.6, 11.0, 2.95),
    "U6_bno085_pcb":   (25.6, 22.7, 1.6),
    "U7_bmp581_pcb":   (25.4, 17.8, 1.6),
    "U5_gnss_pcb":     (30.5, 65.0, 1.6),
    "U2_buck_pcb":     (22.0, 16.0, 1.2),
    "U4_txb_pcb":      (20.0, 18.0, 1.2),
    "J2_term_body":    (15.5, 12.0, 11.5),
    "J1_barrel_body":  (14.0, 9.0, 11.0),
    "ARD_pcb":         (68.58, 53.34, 1.6),
    "SRV0_body":       (23.0, 12.5, 22.5),
    "GA_puck":         (50.0, 50.0, 19.1),
    "C1_elco":         (5.0, 5.0, 11.0),
    "F1_ptc":          (4.6, 3.2, 1.1),
    "D1_tvs":          (5.4, 3.6, 2.2),
    "R1_res":          (6.3, 2.4, 2.4),
    "U3_ldo":          (2.9, 1.6, 1.1),
    "Draagprint":      (100.0, 75.0, 1.6),
}

# objecten die binnen de bordrand moeten blijven (printzijde)
ON_BOARD = [
    "Draagprint", "U1_kit_pcb", "U1_xiao_pcb", "U6_bno085_pcb",
    "U7_bmp581_pcb", "U5_gnss_pcb", "U2_buck_pcb", "U4_txb_pcb",
    "J2_term_body", "J1_barrel_body", "F1_ptc", "D1_tvs", "C1_elco",
    "U3_ldo", "R1_res", "D2_led", "ANT1_sma_base",
]

# paren die mogen "overlappen" (bedoelde stapeling)
ALLOWED = {frozenset(("U1_xiao_pcb", "U1_kit_pcb"))}


def world_bounds(ob):
    pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts),
                 min(p.z for p in pts))) / MM
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts),
                 max(p.z for p in pts))) / MM
    return lo, hi


def size(ob):
    lo, hi = world_bounds(ob)
    return hi - lo, lo, hi


def run():
    bpy.context.view_layer.update()
    errs = []
    warns = []

    print("=" * 72)
    print("A. AFMETINGEN (gemeten uit de scene, mm)")
    print("=" * 72)
    print("%-20s %-22s %-22s" % ("object", "gemeten X x Y x Z", "verwacht"))
    for name, exp in EXPECT.items():
        ob = bpy.data.objects.get(name)
        if ob is None:
            errs.append("ontbreekt: %s" % name)
            print("%-20s %s" % (name, "ONTBREEKT"))
            continue
        s, _, _ = size(ob)
        if ob.name == "C1_elco":          # cilinder: diameter, niet straal
            got = (s.x, s.y, s.z)
        else:
            got = (s.x, s.y, s.z)
        ok = all(abs(got[i] - exp[i]) < 0.35 for i in range(3))
        flag = "ok " if ok else "FOUT"
        print("%-20s %-22s %-22s %s" % (
            name,
            "%.2f x %.2f x %.2f" % got,
            "%.2f x %.2f x %.2f" % exp,
            flag))
        if not ok:
            errs.append("%s: gemeten %.2fx%.2fx%.2f, verwacht %.2fx%.2fx%.2f"
                        % (name, got[0], got[1], got[2],
                           exp[0], exp[1], exp[2]))

    print()
    print("=" * 72)
    print("B. BINNEN DE BORDRAND (X in [-50,50], Y in [-37.5,37.5])")
    print("=" * 72)
    for name in ON_BOARD:
        ob = bpy.data.objects.get(name)
        if ob is None:
            continue
        lo, hi = world_bounds(ob)
        over = []
        if lo.x < -BOARD_W / 2 - 0.01:
            over.append("links %.2f" % (lo.x + BOARD_W / 2))
        if hi.x > BOARD_W / 2 + 0.01:
            over.append("rechts %.2f" % (hi.x - BOARD_W / 2))
        if lo.y < -BOARD_D / 2 - 0.01:
            over.append("onder %.2f" % (lo.y + BOARD_D / 2))
        if hi.y > BOARD_D / 2 + 0.01:
            over.append("boven %.2f" % (hi.y - BOARD_D / 2))
        if over:
            print("%-20s BUITEN: %s" % (name, ", ".join(over)))
            errs.append("%s steekt buiten de bordrand (%s)"
                        % (name, ", ".join(over)))
        else:
            print("%-20s ok  (X %.1f..%.1f  Y %.1f..%.1f)"
                  % (name, lo.x, hi.x, lo.y, hi.y))

    print()
    print("=" * 72)
    print("C. OVERLAP TUSSEN PRINTONDERDELEN (X/Y)")
    print("=" * 72)
    boxes = {}
    for name in ON_BOARD:
        ob = bpy.data.objects.get(name)
        if ob:
            lo, hi = world_bounds(ob)
            boxes[name] = (lo, hi)
    keys = list(boxes)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            ab, bb = boxes[a], boxes[b]
            ox = min(ab[1].x, bb[1].x) - max(ab[0].x, bb[0].x)
            oy = min(ab[1].y, bb[1].y) - max(ab[0].y, bb[0].y)
            if ox > 0.05 and oy > 0.05:
                if a == "Draagprint" or b == "Draagprint":
                    continue          # onderdelen horen op de print te liggen
                if frozenset((a, b)) in ALLOWED:
                    print("(bedoeld)  %-18s <-> %-18s  X %.2f  Y %.2f"
                          % (a, b, ox, oy))
                    continue
                print("OVERLAP    %-18s <-> %-18s  X %.2f  Y %.2f"
                      % (a, b, ox, oy))
                errs.append("overlap %s <-> %s (X %.2f, Y %.2f)"
                            % (a, b, ox, oy))

    print()
    print("=" * 72)
    print("D. SILKSCREEN-LABELS OP DE PRINT")
    print("=" * 72)
    labels = [o for o in bpy.data.objects
              if o.type == 'FONT' and o.name.startswith("Silk_")]
    for lab in labels:
        own = lab.name[len("Silk_"):].upper()   # eigen component (bv. U6)
        lo, hi = world_bounds(lab)
        outs = []
        if lo.x < -BOARD_W / 2 - 0.01:
            outs.append("X<rand")
        if hi.x > BOARD_W / 2 + 0.01:
            outs.append("X>rand")
        if lo.y < -BOARD_D / 2 - 0.01:
            outs.append("Y<rand")
        if hi.y > BOARD_D / 2 + 0.01:
            outs.append("Y>rand")
        # tegen welke componenten botst dit label (in X/Y)?
        hits = []
        for name, (blo, bhi) in boxes.items():
            if name == "Draagprint" or name.upper().startswith(own):
                continue
            ox = min(hi.x, bhi.x) - max(lo.x, blo.x)
            oy = min(hi.y, bhi.y) - max(lo.y, blo.y)
            if ox > 0.2 and oy > 0.2:
                # alleen tellen als het component hoger is dan het label
                ob = bpy.data.objects.get(name)
                if ob and world_bounds(ob)[1].z > 1.9:
                    hits.append("%s(%.1fx%.1f)" % (name, ox, oy))
        msg = "%-24s X %.1f..%.1f  Y %.1f..%.1f" % (
            lab.name, lo.x, hi.x, lo.y, hi.y)
        if outs:
            msg += "  BUITEN RAND: %s" % ",".join(outs)
            errs.append("label %s buiten de bordrand" % lab.name)
        if hits:
            msg += "  BOTST MET: %s" % ", ".join(hits)
            warns.append("label %s valt over %s" % (lab.name, ", ".join(hits)))
        print(msg)

    print()
    print("=" * 72)
    print("E. Z-INTERPENETRATIE IN DE XIAO-STAPEL")
    print("=" * 72)
    stack = ["U1_sock_-1", "U1_sock_1", "U1_kit_pcb", "U1_sx1262",
             "U1_xiao_pcb", "U1_esp32_shield", "U1_usbc"]
    for n in stack:
        ob = bpy.data.objects.get(n)
        if ob:
            lo, hi = world_bounds(ob)
            print("%-20s Z %.2f .. %.2f" % (n, lo.z, hi.z))
    sock = bpy.data.objects.get("U1_sock_1")
    kit = bpy.data.objects.get("U1_kit_pcb")
    if sock and kit:
        _, st = world_bounds(sock)
        kl, _ = world_bounds(kit)
        gap = kl.z - st.z
        print("kit-onder (%.2f) - socket-top (%.2f) = %+.2f mm"
              % (kl.z, st.z, gap))
        if gap < -0.01:
            errs.append("U1_kit_pcb zakt %.2f mm in de sockets" % -gap)

    print()
    print("=" * 72)
    print("RESULTAAT")
    print("=" * 72)
    print("fouten: %d" % len(errs))
    for e in errs:
        print("  FOUT : %s" % e)
    print("waarschuwingen: %d" % len(warns))
    for w in warns:
        print("  WARN : %s" % w)
    return errs, warns


run()
