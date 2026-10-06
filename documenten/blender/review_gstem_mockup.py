# -*- coding: utf-8 -*-
"""
Review-beelden + meetrapport voor de G-Stem Blender-mock-up.

Rendert technische orthografische aanzichten (boven, voor, zij) plus een
overzicht, en schrijft een JSON met alle gemeten maten zodat het controleblad
(PIL) de cijfers uit het model zelf kan overnemen.

Uitvoeren (headless, op het opgeslagen .blend):
    blender -b documenten/blender/gstem-mockup.blend \
            -P documenten/blender/review_gstem_mockup.py
"""

import bpy
import json
import math
import os
from mathutils import Vector, Euler

MM = 0.001
ROOT = r"C:/Users/Nand Schoovaerts/Documents/GSTEM-Project"
OUT = os.path.join(ROOT, "documenten", "blender", "review")
os.makedirs(OUT, exist_ok=True)

BOARD_W, BOARD_D, BOARD_T = 100.0, 75.0, 1.6

# (naam, X, Y, Z) verwacht volgens datasheet
EXPECT = {
    "Draagprint":      (100.0, 75.0, 1.6),
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
    "F1_ptc":          (4.6, 3.2, 1.1),
    "D1_tvs":          (5.4, 3.6, 2.2),
    "C1_elco":         (5.0, 5.0, 11.0),
    "U3_ldo":          (2.9, 1.6, 1.1),
    "R1_res":          (6.3, 2.4, 2.4),
}

ON_BOARD = ["U1_kit_pcb", "U1_xiao_pcb", "U6_bno085_pcb", "U7_bmp581_pcb",
            "U5_gnss_pcb", "U2_buck_pcb", "U4_txb_pcb", "J2_term_body",
            "J1_barrel_body", "F1_ptc", "D1_tvs", "C1_elco", "U3_ldo",
            "R1_res", "D2_led", "ANT1_sma_base"]

ALLOWED = {frozenset(("U1_xiao_pcb", "U1_kit_pcb"))}

# ---------------------------------------------------------------------
# camera's

VIEWS = {
    "top": dict(loc=(0, 0, 700), rot=(0, 0, 0), ortho=118.0,
                res=(1400, 1050), center=(0, 0)),
    "front": dict(loc=(0, -700, 12), rot=(90, 0, 0), ortho=130.0,
                  res=(1400, 560), center=(0, 12)),
    "side": dict(loc=(700, 0, 12), rot=(90, 0, 90), ortho=130.0,
                 res=(1400, 560), center=(0, 12)),
}


def world_bounds(ob):
    pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts),
                 min(p.z for p in pts))) / MM
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts),
                 max(p.z for p in pts))) / MM
    return lo, hi


def prepare():
    """Verberg de mock-up, de bekabeling, de tafel en de lange antenne."""
    for name in ("05_Mockup", "04_Wiring"):
        col = bpy.data.collections.get(name)
        if col:
            for ob in col.objects:
                ob.hide_render = True
    for name in ("Tafel", "ANT1_lora_ant", "Studiodoel", "Doel_34",
                 "Doel_detail"):
        ob = bpy.data.objects.get(name)
        if ob and ob.type != 'CAMERA':
            ob.hide_render = True
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_EEVEE'
    try:
        sc.eevee.taa_render_samples = 48
    except Exception:
        pass
    sc.render.image_settings.file_format = 'PNG'
    sc.render.film_transparent = False
    w = sc.world
    if w and w.use_nodes:
        bg = w.node_tree.nodes.get("Background")
        if bg:
            bg.inputs[0].default_value = (0.42, 0.43, 0.46, 1.0)


def make_views():
    col = bpy.data.collections.get("00_Studio")
    if col is None:
        col = bpy.data.collections.new("00_Studio")
        bpy.context.scene.collection.children.link(col)
    cams = {}
    for key, v in VIEWS.items():
        bpy.ops.object.camera_add()
        c = bpy.context.active_object
        c.name = "REV_%s" % key
        c.data.type = 'ORTHO'
        c.data.ortho_scale = v["ortho"] * MM
        c.data.clip_start = 0.01
        c.data.clip_end = 100.0
        c.location = tuple(p * MM for p in v["loc"])
        c.rotation_euler = Euler([math.radians(a) for a in v["rot"]], 'XYZ')
        for cc in list(c.users_collection):
            cc.objects.unlink(c)
        col.objects.link(c)
        cams[key] = (c, v)
    # overzichtsbeeld (perspectief)
    tgt = bpy.data.objects.get("Doel_rev")
    if tgt is None:
        tgt = bpy.data.objects.new("Doel_rev", None)
        bpy.context.scene.collection.objects.link(tgt)
    tgt.location = (0, -8 * MM, 5 * MM)
    bpy.ops.object.camera_add()
    c = bpy.context.active_object
    c.name = "REV_iso"
    c.data.lens = 55
    c.data.clip_start = 0.01
    c.location = (150 * MM, -235 * MM, 185 * MM)
    con = c.constraints.new('TRACK_TO')
    con.target = tgt
    con.track_axis = 'TRACK_NEGATIVE_Z'
    con.up_axis = 'UP_Y'
    for cc in list(c.users_collection):
        cc.objects.unlink(c)
    col.objects.link(c)
    cams["iso"] = (c, dict(res=(1600, 1100)))
    return cams


def render(cams):
    sc = bpy.context.scene
    for key in ("top", "front", "side", "iso"):
        c, v = cams[key]
        rx, ry = v["res"]
        sc.camera = c
        sc.render.resolution_x, sc.render.resolution_y = rx, ry
        sc.render.filepath = os.path.join(OUT, "%s.png" % key)
        bpy.ops.render.render(write_still=True)
        print("[review] gerenderd:", key)


def measure():
    bpy.context.view_layer.update()
    rep = {"board": {"w": BOARD_W, "d": BOARD_D, "t": BOARD_T},
           "parts": [], "stack": {}, "labels": [], "overlaps": [],
           "label_conflicts": [], "views": {}}

    for key, v in VIEWS.items():
        rep["views"][key] = {
            "res": list(v["res"]), "ortho_scale": v["ortho"],
            "center": list(v["center"]),
            "px_per_mm": v["res"][0] / v["ortho"],
        }

    for name, exp in EXPECT.items():
        ob = bpy.data.objects.get(name)
        if not ob:
            continue
        lo, hi = world_bounds(ob)
        got = (hi.x - lo.x, hi.y - lo.y, hi.z - lo.z)
        ctr = ((lo.x + hi.x) / 2.0, (lo.y + hi.y) / 2.0)
        rep["parts"].append({
            "name": name,
            "got": [round(g, 2) for g in got],
            "exp": list(exp),
            "ok": all(abs(got[i] - exp[i]) < 0.35 for i in range(3)),
            "center": [round(ctr[0], 2), round(ctr[1], 2)],
            "z": [round(lo.z, 2), round(hi.z, 2)],
        })

    # stapel
    for n in ("U1_sock_1", "U1_kit_pcb", "U1_sx1262", "U1_xiao_pcb",
              "U1_esp32_shield"):
        ob = bpy.data.objects.get(n)
        if ob:
            lo, hi = world_bounds(ob)
            rep["stack"][n] = [round(lo.z, 2), round(hi.z, 2)]
    ob = bpy.data.objects.get("U1_esp32_shield")
    if ob:
        rep["stack"]["total_height_mm"] = round(world_bounds(ob)[1].z, 2)
    ob = bpy.data.objects.get("U1_kit_pcb")
    if ob:
        sk = bpy.data.objects.get("U1_sock_1")
        rep["stack"]["kit_on_socket_gap"] = round(
            world_bounds(ob)[0].z - world_bounds(sk)[1].z, 2)

    # alle echte onderdelen op de print (voor labelcontrole)
    boxes_all = {}
    for col_name in ("01_Board", "02_Modules", "03_Components"):
        c = bpy.data.collections.get(col_name)
        if not c:
            continue
        for ob in c.objects:
            if ob.type != 'MESH' or ob.name.startswith(("Draagprint",
                                                      "Koper_")):
                continue
            boxes_all[ob.name] = world_bounds(ob)

    # top-level onderdelen (voor de overlapcontrole)
    boxes = {}
    for name in ON_BOARD:
        ob = bpy.data.objects.get(name)
        if ob:
            boxes[name] = world_bounds(ob)

    lab_objs = [o for o in bpy.data.objects
                if o.type == 'FONT' and o.name.startswith("Silk_")]
    for lab in lab_objs:
        own = lab.name[len("Silk_"):].upper()
        lo, hi = world_bounds(lab)
        entry = {"name": lab.name,
                 "box": [round(lo.x, 1), round(hi.x, 1),
                         round(lo.y, 1), round(hi.y, 1)],
                 "outside": [], "hits": []}
        if lo.x < -BOARD_W / 2 - 0.01:
            entry["outside"].append("links")
        if hi.x > BOARD_W / 2 + 0.01:
            entry["outside"].append("rechts")
        if lo.y < -BOARD_D / 2 - 0.01:
            entry["outside"].append("onder")
        if hi.y > BOARD_D / 2 + 0.01:
            entry["outside"].append("boven")
        for name, (blo, bhi) in boxes_all.items():
            if name.upper().startswith(own):
                continue
            if (min(hi.x, bhi.x) - max(lo.x, blo.x) > 0.2 and
                    min(hi.y, bhi.y) - max(lo.y, blo.y) > 0.2 and
                    bhi.z > 1.9):
                entry["hits"].append(name)
        rep["labels"].append(entry)

    # label tegen label
    slabs = []
    for lab in lab_objs:
        lo, hi = world_bounds(lab)
        for n2, (lo2, hi2) in slabs:
            ox = min(hi.x, hi2.x) - max(lo.x, lo2.x)
            oy = min(hi.y, hi2.y) - max(lo.y, lo2.y)
            if ox > 0.05 and oy > 0.05:
                rep["label_conflicts"].append(
                    {"a": lab.name, "b": n2,
                     "ox": round(ox, 2), "oy": round(oy, 2)})
        slabs.append((lab.name, (lo, hi)))

    # overlappingen tussen top-level onderdelen
    keys = list(boxes)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            ab, bb = boxes[a], boxes[b]
            ox = min(ab[1].x, bb[1].x) - max(ab[0].x, bb[0].x)
            oy = min(ab[1].y, bb[1].y) - max(ab[0].y, bb[0].y)
            if ox > 0.05 and oy > 0.05:
                rep["overlaps"].append({
                    "a": a, "b": b, "ox": round(ox, 2), "oy": round(oy, 2),
                    "intended": frozenset((a, b)) in ALLOWED})
    return rep


def main():
    prepare()
    cams = make_views()
    render(cams)
    rep = measure()
    rep["errors"] = [p for p in rep["parts"] if not p["ok"]]
    rep["bad_labels"] = [l for l in rep["labels"]
                         if l["outside"] or l["hits"]]
    rep["bad_overlaps"] = [o for o in rep["overlaps"] if not o["intended"]]
    rep["all_labels_ok"] = (not rep["bad_labels"] and
                             not rep["label_conflicts"])
    path = os.path.join(OUT, "review_metingen.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    print("[review] metingen:", path)
    print("[review] fouten:", len(rep["errors"]),
          "| labels met botsing:", len(rep["bad_labels"]),
          "| label-label:", len(rep["label_conflicts"]),
          "| overlap:", len(rep["bad_overlaps"]))


main()
