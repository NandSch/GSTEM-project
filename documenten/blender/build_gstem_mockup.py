# -*- coding: utf-8 -*-
"""
G-Stem mock-up in Blender -- volledige opstelling van het meettoestel.

Bouwt (herhaalbaar) de draagprint met alle breakout-modules, de losse
printonderdelen, de antennes/bekabeling, de Arduino Uno met servo's en de
LoRa-ontvanger. Daarna een studio-opstelling met drie renders.

Eenheden: het script werkt in millimeters (MM = 0.001 m).
Werkt in Blender 5.x. Uitvoeren in de live sessie met:
    exec(open(r"...build_gstem_mockup.py").read())

Bron van maten: GEBRUIKER/data/componenten.md, bestelschema-pcb.md,
pcb-schets.md, pcb-ontwerp.md en de datasheets van de fabrikanten
(zie GEBRUIKER/data/gstem-hardware-afmetingen.md).
"""

import bpy
import bmesh
import math
import os
from mathutils import Vector, Euler

# =====================================================================
# 0. PARAMETERS EN AFMETINGEN (mm)
# =====================================================================
MM = 0.001

ROOT = r"C:/Users/Nand Schoovaerts/Documents/GSTEM-Project"
OUT_DIR = os.path.join(ROOT, "documenten", "blender", "renders")

# --- draagprint -------------------------------------------------------
BOARD_W = 100.0      # X
BOARD_D = 75.0       # Y
BOARD_T = 1.6        # dikte
CORNER_R = 3.0
HOLE_D = 3.2         # M3 vrij gat
HOLE_INSET = 4.0
BOARD_BOTTOM_Z = 0.0
BOARD_TOP_Z = BOARD_T
Z = BOARD_TOP_Z

# --- afmetingen per onderdeel (X, Y, Z in mm) -------------------------
DIM = {
    "xiao":     dict(w=17.8, d=21.0, t=1.2, sock=8.5),   # Seeed XIAO ESP32S3
    "sx1262":   dict(w=11.6, d=11.0, t=2.95),            # Wio-SX1262 module
    "carrier":  dict(w=17.8, d=21.0, t=1.2),             # kit-draagprint
    "bno085":   dict(w=25.6, d=22.7, t=1.6),             # Adafruit 4754
    "bmp581":   dict(w=25.4, d=17.8, t=1.6),             # Adafruit 6407 STEMMA QT
    "gnss":     dict(w=30.5, d=65.0, t=1.6),             # Waveshare LC29H HAT (gedraaid)
    "buck":     dict(w=22.0, d=16.0, t=7.0),
    "txb":      dict(w=20.0, d=18.0, t=3.5),             # TXB0108-breakout
    "term":     dict(w=15.5, d=12.0, t=11.5),            # DG250-3.5-04P
    "barrel":   dict(w=14.0, d=9.0,  t=11.0),            # DC-005
    "arduino":  dict(w=68.58, d=53.34, t=1.6),
    "servo":    dict(w=23.0, d=12.5, t=22.5),            # SG90
    "gnss_ant": dict(w=50.0, d=50.0, t=19.1),            # Waveshare L1/L5 puck
    "rx_xiao":  dict(w=17.8, d=21.0, t=1.2),
    "laptop":   dict(w=300.0, d=210.0, t=14.0),
}

COL_NAMES = ["00_Studio", "01_Board", "02_Modules", "03_Components",
             "04_Wiring", "05_Mockup"]

RENDER = os.environ.get("GSTEM_RENDER", "0") == "1"


# =====================================================================
# 1. HELPERS
# =====================================================================
def log(*a):
    print("[gstem]", *a)


def ensure_collection(name):
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col


def wipe():
    for name in COL_NAMES:
        col = bpy.data.collections.get(name)
        if col is not None:
            for ob in list(col.objects):
                bpy.data.objects.remove(ob, do_unlink=True)
            bpy.data.collections.remove(col)
    for name in ("Cube", "Camera", "Light"):
        ob = bpy.data.objects.get(name)
        if ob:
            bpy.data.objects.remove(ob, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights,
                 bpy.data.cameras, bpy.data.curves, bpy.data.images):
        for db in list(coll):
            if db.users == 0:
                coll.remove(db)


def move_to(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def new_mat(name, color, metallic=0.0, rough=0.5, emis=None,
            emis_str=0.0, alpha=1.0, coat=0.0):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")

    def setv(inp, val):
        if inp in bsdf.inputs:
            bsdf.inputs[inp].default_value = val

    setv("Base Color", (*color, 1.0))
    setv("Metallic", metallic)
    setv("Roughness", rough)
    setv("Alpha", alpha)
    setv("Coat Weight", coat)
    if emis is not None:
        setv("Emission Color", (*emis, 1.0))
        setv("Emission Strength", emis_str)
    if alpha < 1.0:
        mat.blend_method = 'BLEND'
    mat.diffuse_color = (*color, alpha)
    return mat


def set_mat(obj, mat):
    if mat is None:
        return
    if obj.type in ('MESH', 'CURVE'):
        obj.data.materials.clear()
        obj.data.materials.append(mat)


def bevel(obj, width, segments=2, angle=60):
    if width <= 0:
        return
    m = obj.modifiers.new("bevel", 'BEVEL')
    m.width = width * MM
    m.segments = segments
    m.limit_method = 'ANGLE'
    m.angle_limit = math.radians(angle)


def box(name, size, loc, rot=(0, 0, 0), mat=None, col=None, bev=0.0,
        segs=2):
    bpy.ops.mesh.primitive_cube_add(size=1.0)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = (size[0] * MM, size[1] * MM, size[2] * MM)
    bpy.ops.object.transform_apply(location=False, rotation=False,
                                   scale=True)
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    obj.rotation_euler = Euler([math.radians(a) for a in rot], 'XYZ')
    set_mat(obj, mat)
    bevel(obj, bev, segs)
    if col is not None:
        move_to(obj, col)
    return obj


def cyl(name, r, h, loc, rot=(0, 0, 0), verts=32, mat=None, col=None,
        bev=0.0):
    bpy.ops.mesh.primitive_cylinder_add(radius=r * MM, depth=h * MM,
                                        vertices=verts)
    obj = bpy.context.active_object
    obj.name = name
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    obj.rotation_euler = Euler([math.radians(a) for a in rot], 'XYZ')
    set_mat(obj, mat)
    bevel(obj, bev, 1)
    if col is not None:
        move_to(obj, col)
    return obj


def cone(name, r1, r2, h, loc, rot=(0, 0, 0), verts=32, mat=None, col=None):
    bpy.ops.mesh.primitive_cone_add(radius1=r1 * MM, radius2=r2 * MM,
                                    depth=h * MM, vertices=verts)
    obj = bpy.context.active_object
    obj.name = name
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    obj.rotation_euler = Euler([math.radians(a) for a in rot], 'XYZ')
    set_mat(obj, mat)
    if col is not None:
        move_to(obj, col)
    return obj


def sphere(name, r, loc, mat=None, col=None, scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r * MM, segments=24,
                                         ring_count=12)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False,
                                   scale=True)
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    set_mat(obj, mat)
    if col is not None:
        move_to(obj, col)
    return obj


def rounded_rect_prism(name, w, d, t, r, loc, mat=None, col=None,
                       corner_segs=8):
    pts = []
    hw, hd = w / 2.0 - r, d / 2.0 - r
    for (cx, cy), a0 in [((hw, hd), 0), ((-hw, hd), 90),
                         ((-hw, -hd), 180), ((hw, -hd), 270)]:
        for i in range(corner_segs + 1):
            a = math.radians(a0 + 90.0 * i / corner_segs)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    bm = bmesh.new()
    verts = [bm.verts.new((x * MM, y * MM, 0.0)) for x, y in pts]
    face = bm.faces.new(verts)
    ext = bmesh.ops.extrude_face_region(bm, geom=[face])
    nv = [g for g in ext["geom"] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=nv, vec=(0, 0, t * MM))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new(name, me)
    (col or bpy.context.scene.collection).objects.link(obj)
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    set_mat(obj, mat)
    return obj


def label(name, text, size, loc, rot=(0, 0, 0), mat=None, col=None,
          align='CENTER', extrude=0.02):
    bpy.ops.object.text_add()
    obj = bpy.context.active_object
    obj.name = name
    obj.data.body = text
    obj.data.size = size * MM
    obj.data.align_x = align
    obj.data.extrude = extrude * MM
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    obj.rotation_euler = Euler([math.radians(a) for a in rot], 'XYZ')
    set_mat(obj, mat)
    if col is not None:
        move_to(obj, col)
    return obj


def wire(name, pts, r, mat, col, res=4):
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(pts) - 1)
    for i, p in enumerate(pts):
        bp = sp.bezier_points[i]
        bp.co = Vector((p[0] * MM, p[1] * MM, p[2] * MM))
        bp.handle_left_type = bp.handle_right_type = 'AUTO'
    cu.bevel_depth = r * MM
    cu.bevel_resolution = res
    obj = bpy.data.objects.new(name, cu)
    col.objects.link(obj)
    set_mat(obj, mat)
    return obj


def empty(name, loc=(0, 0, 0), col=None):
    obj = bpy.data.objects.new(name, None)
    (col or bpy.context.scene.collection).objects.link(obj)
    obj.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
    obj.empty_display_size = 0.01
    return obj


def aim(obj, target):
    c = obj.constraints.new('TRACK_TO')
    c.target = target
    c.track_axis = 'TRACK_NEGATIVE_Z'
    c.up_axis = 'UP_Y'


def pin_row(name, cx, cy, count, pitch, horizontal, mat, col, z,
            pin=(0.64, 0.64, 0.8)):
    for i in range(count):
        off = (i - (count - 1) / 2.0) * pitch
        x = cx + (off if horizontal else 0.0)
        y = cy + (0.0 if horizontal else off)
        box("%s_%02d" % (name, i), pin, (x, y, z + pin[2] / 2.0),
            mat=mat, col=col)


def hide_col_render(name, hidden):
    col = bpy.data.collections.get(name)
    if col is None:
        return
    for ob in col.objects:
        ob.hide_render = hidden


# =====================================================================
# 2. SCENE + MATERIALEN
# =====================================================================
def setup_scene():
    sc = bpy.context.scene
    sc.unit_settings.system = 'METRIC'
    sc.unit_settings.scale_length = 1.0
    sc.unit_settings.length_unit = 'MILLIMETERS'
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = 64
    sc.cycles.use_denoising = True
    sc.render.film_transparent = False
    sc.render.resolution_x = 1600
    sc.render.resolution_y = 1200
    sc.render.image_settings.file_format = 'PNG'
    try:
        sc.view_settings.view_transform = 'AgX'
        sc.view_settings.look = 'AgX - Punchy'
    except Exception:
        pass


def build_materials():
    M = {}
    M["mask"] = new_mat("PCB_masker_groen", (0.021, 0.13, 0.052),
                        rough=0.38, coat=0.5)
    M["mask_bot"] = new_mat("PCB_masker_onder", (0.02, 0.09, 0.04),
                            rough=0.5)
    M["fr4"] = new_mat("FR4_zijde", (0.35, 0.30, 0.16), rough=0.65)
    M["gold"] = new_mat("HASL_pad", (0.72, 0.66, 0.42), metallic=1.0,
                        rough=0.30)
    M["copper"] = new_mat("Koper", (0.55, 0.30, 0.15), metallic=1.0,
                          rough=0.35)
    M["silkscreen"] = new_mat("Silkscreen_wit", (0.90, 0.90, 0.88),
                              rough=0.6)
    M["black_ic"] = new_mat("IC_zwart", (0.025, 0.025, 0.03), rough=0.35,
                            coat=0.3)
    M["pcb_blue"] = new_mat("PCB_blauw", (0.02, 0.09, 0.22), rough=0.35,
                            coat=0.4)
    M["pcb_black"] = new_mat("PCB_zwart", (0.02, 0.02, 0.022), rough=0.35,
                             coat=0.4)
    M["steel"] = new_mat("Metaal", (0.62, 0.63, 0.66), metallic=1.0,
                         rough=0.28)
    M["gold_pin"] = new_mat("Pin_verguld", (0.80, 0.68, 0.35),
                            metallic=1.0, rough=0.22)
    M["plastic_black"] = new_mat("Kunststof_zwart", (0.03, 0.03, 0.035),
                                 rough=0.45)
    M["plastic_white"] = new_mat("Kunststof_wit", (0.85, 0.85, 0.83),
                                 rough=0.45)
    M["plastic_grey"] = new_mat("Kunststof_grijs", (0.35, 0.36, 0.38),
                                rough=0.5)
    M["plastic_green"] = new_mat("Klem_groen", (0.05, 0.25, 0.10),
                                 rough=0.45)
    M["sma_gold"] = new_mat("SMA_verguld", (0.76, 0.62, 0.28),
                            metallic=1.0, rough=0.25)
    M["wire_red"] = new_mat("Draad_rood", (0.55, 0.02, 0.02), rough=0.5)
    M["wire_black"] = new_mat("Draad_zwart", (0.02, 0.02, 0.02), rough=0.5)
    M["wire_blue"] = new_mat("Draad_blauw", (0.04, 0.10, 0.45), rough=0.5)
    M["wire_yellow"] = new_mat("Draad_geel", (0.75, 0.62, 0.05), rough=0.5)
    M["wire_green"] = new_mat("Draad_groen", (0.05, 0.40, 0.12), rough=0.5)
    M["wire_white"] = new_mat("Draad_wit", (0.80, 0.80, 0.78), rough=0.5)
    M["cable_grey"] = new_mat("Kabel_grijs", (0.10, 0.10, 0.11), rough=0.45)
    M["led_red"] = new_mat("LED_rood", (0.65, 0.03, 0.03), rough=0.15,
                           emis=(1.0, 0.05, 0.02), emis_str=2.0, alpha=0.9)
    M["elco"] = new_mat("Elco", (0.10, 0.11, 0.13), rough=0.4)
    M["arduino"] = new_mat("Arduino_teal", (0.0, 0.22, 0.34), rough=0.38,
                           coat=0.3)
    M["servo_blue"] = new_mat("Servo_blauw", (0.05, 0.20, 0.45), rough=0.4)
    M["laptop"] = new_mat("Laptop_alu", (0.55, 0.56, 0.58), metallic=0.9,
                          rough=0.30)
    M["screen"] = new_mat("Scherm", (0.05, 0.07, 0.10), rough=0.15,
                          emis=(0.15, 0.35, 0.55), emis_str=0.8)
    M["table"] = new_mat("Tafel", (0.035, 0.037, 0.042), rough=0.65)
    M["antenna"] = new_mat("Antenne", (0.06, 0.06, 0.07), rough=0.42)
    M["antenna_puck"] = new_mat("Antenne_puck", (0.12, 0.12, 0.13),
                                rough=0.5)
    M["poly"] = new_mat("Polyester", (0.55, 0.30, 0.10), rough=0.3,
                        metallic=0.1)
    return M


# =====================================================================
# 3. DRAGPRINT
# =====================================================================
def build_board(M):
    col = ensure_collection("01_Board")
    b = rounded_rect_prism("Draagprint", BOARD_W, BOARD_D, BOARD_T, CORNER_R,
                           (0, 0, BOARD_BOTTOM_Z), M["mask"], col)
    b.data.materials.append(M["fr4"])
    b.data.materials.append(M["mask_bot"])

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = b
    b.select_set(True)
    for sx in (-1, 1):
        for sy in (-1, 1):
            c = cyl("cut", HOLE_D / 2.0, BOARD_T * 8,
                    ((BOARD_W / 2 - HOLE_INSET) * sx,
                     (BOARD_D / 2 - HOLE_INSET) * sy,
                     BOARD_BOTTOM_Z + BOARD_T / 2.0), verts=32)
            md = b.modifiers.new("cut", 'BOOLEAN')
            md.operation = 'DIFFERENCE'
            md.solver = 'EXACT'
            md.object = c
            bpy.ops.object.modifier_apply(modifier=md.name)
            bpy.data.objects.remove(c, do_unlink=True)
    for p in b.data.polygons:
        n = p.normal
        p.material_index = 0 if n.z > 0.5 else (2 if n.z < -0.5 else 1)

    box("Koper_onderlaag", (BOARD_W - 4, BOARD_D - 4, 0.05),
        (0, 0, BOARD_BOTTOM_Z - 0.03), mat=M["copper"], col=col)

    silk = M["silkscreen"]
    label("Silk_titel", "G-STEM  MEETTOESTEL", 2.6,
          (-22, 35.5, Z + 0.02), mat=silk, col=col, align='LEFT')
    label("Silk_rev", "draagprint  rev. A   100 x 75 mm", 1.4,
          (-22, 33.4, Z + 0.02), mat=silk, col=col, align='LEFT')
    label("Silk_m3", "M3", 1.6,
          (BOARD_W / 2 - HOLE_INSET - 6.5, BOARD_D / 2 - HOLE_INSET,
           Z + 0.02), mat=silk, col=col, align='LEFT')
    return b


# =====================================================================
# 4. LOSSE PRINTONDERDELEN
# =====================================================================
def build_components(M):
    col = ensure_collection("03_Components")
    silk = M["silkscreen"]

    # J1 -- barrel jack DC-005, opening naar -X
    bw, bd, bt = (DIM["barrel"]["w"], DIM["barrel"]["d"], DIM["barrel"]["t"])
    box("J1_barrel_body", (bw, bd, bt), (-43, 30.5, Z + bt / 2.0),
        mat=M["plastic_black"], col=col, bev=0.4)
    cyl("J1_barrel_pin", 1.05, 6.0, (-40, 30.5, Z + 5.5),
        rot=(0, 90, 0), mat=M["steel"], col=col)
    label("Silk_J1", "J1 PWR 7,4V", 1.3, (-44.5, 23.9, Z + 0.02), mat=silk,
          col=col)

    # F1 -- PTC 1812 (in de +-lijn na de connector)
    box("F1_ptc", (4.6, 3.2, 1.1), (-33, 34.5, Z + 0.55),
        mat=M["plastic_white"], col=col, bev=0.15)
    label("Silk_F1", "F1 2A", 1.2, (-33, 31.9, Z + 0.02), mat=silk, col=col)

    # D1 -- TVS SMBJ10A (DO-214AA)
    box("D1_tvs", (5.4, 3.6, 2.2), (-28, 34.5, Z + 1.1), mat=M["black_ic"],
        col=col, bev=0.15)
    label("Silk_D1", "D1 TVS", 1.2, (-28, 31.7, Z + 0.02), mat=silk,
          col=col)

    # U2 -- buck-converter module (gebruiker)
    uw, ud, uh = DIM["buck"]["w"], DIM["buck"]["d"], DIM["buck"]["t"]
    box("U2_buck_pcb", (uw, ud, 1.2), (-38, 15, Z + 0.6), mat=M["pcb_blue"],
        col=col, bev=0.2)
    cyl("U2_buck_ind", 4.0, 4.5, (-44, 11.5, Z + 3.5),
        mat=M["plastic_black"], col=col)
    box("U2_buck_ic", (4.0, 4.0, 1.6), (-34, 11, Z + 2.0),
        mat=M["black_ic"], col=col)
    box("U2_buck_cap", (3.0, 3.0, 3.0), (-30, 20, Z + 2.7),
        mat=M["elco"], col=col)
    label("Silk_U2", "U2 BUCK 5V", 1.3, (-34, 23.9, Z + 0.02), mat=silk,
          col=col)

    # C1 -- bulk-elco 100 uF / 16 V
    cyl("C1_elco", 2.5, 11.0, (-24, 13, Z + 5.5), mat=M["elco"], col=col)
    label("Silk_C1", "C1 100uF", 1.2, (-24, 16.0, Z + 0.02), mat=silk,
          col=col)

    # U3 -- LDO AP2112K-3.3 SOT-23-5
    box("U3_ldo", (2.9, 1.6, 1.1), (-24, 21.5, Z + 0.55), mat=M["black_ic"],
        col=col, bev=0.1)
    label("Silk_U3", "U3 3V3", 1.2, (-24, 23.0, Z + 0.02), mat=silk, col=col)

    # D2 -- power-LED + R1
    cyl("D2_led", 1.5, 1.4, (-24, 26, Z + 0.7), mat=M["led_red"], col=col)
    sphere("D2_led_dome", 1.5, (-24, 26, Z + 1.45), mat=M["led_red"],
           col=col, scale=(1, 1, 0.9))
    box("R1_res", (6.3, 2.4, 2.4), (-19.0, 26, Z + 1.2),
        mat=M["plastic_grey"], col=col)
    label("Silk_D2", "D2 LED", 1.2, (-24, 28.3, Z + 0.02), mat=silk, col=col)
    label("Silk_R1", "R1 330R", 1.2, (-19.0, 28.3, Z + 0.02), mat=silk,
          col=col)

    # U4 -- TXB0108 breakout (level shifter)
    tw, td, th = DIM["txb"]["w"], DIM["txb"]["d"], DIM["txb"]["t"]
    box("U4_txb_pcb", (tw, td, 1.2), (-10, -10, Z + 0.6),
        mat=M["pcb_black"], col=col, bev=0.2)
    box("U4_txb_ic", (5.0, 4.4, 1.2), (-10, -10, Z + 1.8),
        mat=M["black_ic"], col=col, bev=0.1)
    pin_row("U4_pins_a", -10, -10 - td / 2.0 + 1.0, 6, 2.54, True,
            M["gold_pin"], col, Z + 0.05, pin=(0.6, 0.9, 0.6))
    pin_row("U4_pins_b", -10, -10 + td / 2.0 - 1.0, 6, 2.54, True,
            M["gold_pin"], col, Z + 0.05, pin=(0.6, 0.9, 0.6))
    label("Silk_U4", "U4 TXB0108 3V3<->5V", 1.6, (-10, -0.5, Z + 0.02),
          mat=silk, col=col)

    # J2 -- 4-pins schroefklem 3,5 mm
    tx, ty, tz = DIM["term"]["w"], DIM["term"]["d"], DIM["term"]["t"]
    box("J2_term_body", (tx, ty, tz), (-14, -30, Z + tz / 2.0),
        mat=M["plastic_green"], col=col, bev=0.4)
    for j in range(4):
        px = -14 + (j - 1.5) * 3.5
        cyl("J2_screw_%d" % j, 1.4, 1.0, (px, -30, Z + tz - 0.4),
            mat=M["steel"], col=col)
    label("Silk_J2", "J2 UART GND 5V TX RX", 1.5, (-14, -37.0, Z + 0.02),
          mat=silk, col=col)

    label("Silk_keepout", "KEEP-OUT  LoRa 868 MHz", 1.4, (30, 36.3,
          Z + 0.02), mat=silk, col=col)
    return col


# =====================================================================
# 5. BREAKOUT-MODULES
# =====================================================================
def build_modules(M):
    col = ensure_collection("02_Modules")
    silk = M["silkscreen"]
    gp = M["gold_pin"]

    # ---- U1: XIAO ESP32S3 + Wio-SX1262 kit -------------------------
    cx, cy = 0, 20
    w, d, t, sh = (DIM["xiao"]["w"], DIM["xiao"]["d"], DIM["xiao"]["t"],
                   DIM["xiao"]["sock"])
    for sx in (-1, 1):
        box("U1_sock_%d" % sx, (2.54, 17.8, sh), (cx + sx * 7.62, cy,
            Z + sh / 2.0), mat=M["plastic_black"], col=col, bev=0.2)
        for i in range(7):
            yy = cy + (i - 3) * 2.54
            box("U1_pin_%d_%d" % (sx, i), (0.64, 0.64, sh),
                (cx + sx * 7.62, yy, Z + sh / 2.0), mat=gp, col=col)
    cw, cd, ct = (DIM["carrier"]["w"], DIM["carrier"]["d"],
                  DIM["carrier"]["t"])
    # de kit-draagprint rust OP de sockets (niet erin)
    base = Z + sh + ct
    box("U1_kit_pcb", (cw, cd, ct), (cx, cy, Z + sh + ct / 2.0),
        mat=M["pcb_black"], col=col, bev=0.2)
    sw, sd, st = (DIM["sx1262"]["w"], DIM["sx1262"]["d"], DIM["sx1262"]["t"])
    box("U1_sx1262", (sw, sd, st), (cx - 0.5, cy - 3.0, base + st / 2.0),
        mat=M["steel"], col=col, bev=0.3)
    box("U1_xiao_pcb", (w, d, t), (cx, cy, base + st + 0.4 + t / 2.0),
        mat=M["pcb_black"], col=col, bev=0.25)
    box("U1_esp32_shield", (12.0, 12.0, 2.0),
        (cx + 0.5, cy + 3.0, base + st + 0.4 + t + 1.0),
        mat=M["steel"], col=col, bev=0.2)
    box("U1_usbc", (7.6, 6.0, 3.0),
        (cx - 2.0, cy + d / 2.0 - 1.5, base + st + 0.4 + t + 0.4),
        mat=M["steel"], col=col, bev=0.3)
    cyl("U1_ipex", 1.4, 1.4, (cx + 6.0, cy - 6.0, base + st + 0.4 + t + 0.6),
        mat=M["sma_gold"], col=col, verts=16)
    label("Silk_U1", "U1 XIAO ESP32S3 + Wio-SX1262", 1.7,
          (cx, cy - 13.5, Z + 0.02), mat=silk, col=col)

    # ---- U6: BNO085 (IMU) ------------------------------------------
    bx, by = -34, -5
    w, d, t = DIM["bno085"]["w"], DIM["bno085"]["d"], DIM["bno085"]["t"]
    box("U6_bno085_pcb", (w, d, t), (bx, by, Z + 0.9 + t / 2.0),
        mat=M["pcb_blue"], col=col, bev=0.25)
    box("U6_bno085_ic", (5.0, 5.0, 2.6), (bx, by, Z + 0.9 + t + 1.3),
        mat=M["black_ic"], col=col, bev=0.15)
    cyl("U6_jst1", 1.5, 1.6, (bx + w / 2.0 - 1.0, by, Z + 0.9 + t + 0.8),
        mat=M["plastic_white"], col=col, verts=16)
    label("Silk_U6", "U6 BNO085", 1.3, (-34, -17.6, Z + 0.02),
          mat=silk, col=col)

    # ---- U7: BMP581 (barometer) ------------------------------------
    mx, my = -35, -27
    w, d, t = DIM["bmp581"]["w"], DIM["bmp581"]["d"], DIM["bmp581"]["t"]
    box("U7_bmp581_pcb", (w, d, t), (mx, my, Z + 0.9 + t / 2.0),
        mat=M["pcb_blue"], col=col, bev=0.25)
    box("U7_bmp581_ic", (2.6, 2.6, 1.0), (mx, my, Z + 0.9 + t + 0.5),
        mat=M["black_ic"], col=col, bev=0.1)
    label("Silk_U7", "U7 BMP581", 1.3, (-24.5, -18.6, Z + 0.02), mat=silk,
          col=col)

    # ---- U5: Waveshare LC29H(DA) RTK-GNSS HAT (gedraaid) -----------
    gx, gy = 34, -1
    w, d, t = DIM["gnss"]["w"], DIM["gnss"]["d"], DIM["gnss"]["t"]
    box("U5_gnss_pcb", (w, d, t), (gx, gy, Z + 0.9 + t / 2.0),
        mat=M["pcb_blue"], col=col, bev=0.3)
    # 2x20 GPIO-header langs de lange linkerrand
    for row in range(2):
        for i in range(20):
            box("U5_hdr_%d_%d" % (row, i), (0.64, 0.64, 2.6),
                (gx - w / 2.0 + 2.0 + row * 2.54,
                 gy - d / 2.0 + 3.0 + i * 2.54, Z + 0.9 + t + 1.3),
                mat=gp, col=col)
    box("U5_gnss_module", (12.0, 12.0, 2.2), (gx + 4.0, gy + 10.0,
        Z + 0.9 + t + 1.1), mat=M["steel"], col=col, bev=0.2)
    box("U5_usb", (7.0, 5.0, 3.0), (gx + 2.0, gy - d / 2.0 + 1.0,
        Z + 0.9 + t + 0.4), mat=M["steel"], col=col, rot=(0, 0, 90),
        bev=0.3)
    cyl("U5_ipex", 1.4, 1.4, (gx + w / 2.0 - 2.0, gy - d / 2.0 + 3.0,
        Z + 0.9 + t + 0.6), mat=M["sma_gold"], col=col, verts=16)
    label("Silk_U5", "U5 LC29H(DA) RTK-GNSS", 1.3, (34, 32.3,
          Z + 0.02), mat=silk, col=col)

    # ---- ANT1: SMA-bulkhead LoRa + antenne -------------------------
    cyl("ANT1_sma_base", 4.2, 3.0, (14, 32, Z + 1.5), mat=M["sma_gold"],
        col=col)
    cyl("ANT1_sma_thread", 3.2, 6.0, (14, 32, Z + 6.0), mat=M["sma_gold"],
        col=col)
    cone("ANT1_lora_ant", 6.5, 3.0, 180.0, (14, 32, Z + 8.0 + 90.0),
         mat=M["antenna"], col=col, verts=20)
    label("Silk_ANT1", "ANT1 LoRa", 1.3, (14, 26.3, Z + 0.02), mat=silk,
          col=col)
    return col


# =====================================================================
# 6. BEKABELING + MOCK-UP
# =====================================================================
def build_wiring(M):
    col = ensure_collection("04_Wiring")

    # IPEX (SX1262) -> SMA-bulkhead LoRa
    wire("W_ipex_sma", [(6.0, 14, Z + 22.0), (9, 24, Z + 14),
                        (12, 30, Z + 5), (14, 32, Z + 1.5)], 0.57,
         M["wire_black"], col)
    # IPEX (GNSS) -> externe L1/L5-antenne
    wire("W_gnss_coax", [(48.5, -34.0, Z + 2.5), (60, -44, Z + 5),
                         (80, -30, Z + 8), (92, 0, Z + 16),
                         (95, 24, Z + 30)], 0.57,
         M["wire_black"], col)
    # 4-aderige UART-kabel van de schroefklem naar de Arduino
    wire("W_uart", [(-14, -37, Z + 6), (-14, -52, Z + 4),
                    (-8, -70, Z + 3), (0, -84, Z + 5),
                    (0, -104, Z + 12)], 2.6, M["cable_grey"], col)
    return col


def build_mockup(M):
    col = ensure_collection("05_Mockup")
    silk = M["silkscreen"]

    # ---- Arduino Uno ------------------------------------------------
    ax, ay = 0, -105
    w, d, t = (DIM["arduino"]["w"], DIM["arduino"]["d"], DIM["arduino"]["t"])
    box("ARD_pcb", (w, d, t), (ax, ay, 4 + t / 2.0), mat=M["arduino"],
        col=col, bev=0.5)
    box("ARD_usb", (12.0, 16.0, 11.0), (ax - w / 2.0 + 3.0, ay - 4,
        4 + t + 5.5), mat=M["steel"], col=col, bev=0.4)
    cyl("ARD_jack", 5.0, 9.0, (ax - w / 2.0 + 4.0, ay + 16, 4 + t + 4.5),
        rot=(0, 90, 0), mat=M["plastic_black"], col=col)
    box("ARD_mcu", (35.0, 8.0, 4.0), (ax + 8, ay + 2, 4 + t + 2.0),
        mat=M["black_ic"], col=col, bev=0.2)
    box("ARD_hdr1", (54.0, 2.54, 8.5), (ax + 2, ay + d / 2.0 - 3,
        4 + t + 4.2), mat=M["plastic_black"], col=col)
    box("ARD_hdr2", (54.0, 2.54, 8.5), (ax + 2, ay - d / 2.0 + 3,
        4 + t + 4.2), mat=M["plastic_black"], col=col)
    label("ARD_silk", "ARDUINO UNO", 5.0, (ax + 8, ay - 8, 4 + t + 0.02),
          mat=silk, col=col)

    # ---- Servo's ----------------------------------------------------
    for i, sx in enumerate([-58, 0, 58]):
        bx, by = sx, -152
        w, d, t = (DIM["servo"]["w"], DIM["servo"]["d"], DIM["servo"]["t"])
        box("SRV%d_body" % i, (w, d, t), (bx, by, 4 + t / 2.0),
            mat=M["servo_blue"], col=col, bev=0.6)
        box("SRV%d_tab" % i, (w + 9.4, d - 2, 2.5), (bx, by - 5.0,
            4 + t - 4.0), mat=M["servo_blue"], col=col, bev=0.3)
        cyl("SRV%d_shaft" % i, 3.0, 4.0, (bx, by - 11.0, 4 + t + 1.0),
            mat=M["plastic_white"], col=col)
        box("SRV%d_horn" % i, (16.0, 3.0, 1.5), (bx, by - 11.0,
            4 + t + 3.5), mat=M["plastic_white"], col=col, bev=0.3)

    # ---- LoRa-ontvanger: tweede XIAO-kit op een voetje -------------
    rx, ry = -92, -28
    w, d, t = DIM["rx_xiao"]["w"], DIM["rx_xiao"]["d"], DIM["rx_xiao"]["t"]
    box("RX_holder", (22.0, 10.0, 32.0), (rx, ry - 2, 16.0),
        mat=M["plastic_grey"], col=col, bev=0.5)
    box("RX_pcb", (w, d, t), (rx, ry, 32 + t / 2.0), mat=M["pcb_black"],
        col=col, bev=0.25)
    box("RX_usbc", (7.6, 6.0, 3.0), (rx - 2.0, ry + d / 2.0 - 1.5,
        32 + t + 0.4), mat=M["steel"], col=col, bev=0.3)
    cyl("RX_sma", 3.2, 8.0, (rx + w / 2.0 + 4.0, ry, 32 + 1.5),
        rot=(0, 90, 0), mat=M["sma_gold"], col=col)
    cone("RX_ant", 5.5, 3.0, 150.0, (rx + 20.0, ry, 32 + 2.0),
         rot=(0, 90, 0), mat=M["antenna"], col=col, verts=18)
    label("RX_silk", "LoRa-ontvanger (2e XIAO)", 2.0, (rx, ry - 11,
          32 + t + 0.02), mat=silk, col=col)

    # ---- GNSS-antenne op een voetje --------------------------------
    gx, gy = 90, 44
    w, d, t = (DIM["gnss_ant"]["w"], DIM["gnss_ant"]["d"],
               DIM["gnss_ant"]["t"])
    cyl("GA_stand", 9.0, 30.0, (gx, gy, 15.0), mat=M["plastic_grey"],
        col=col)
    box("GA_puck", (w, d, t), (gx, gy, 30 + t / 2.0),
        mat=M["antenna_puck"], col=col, bev=1.2)
    cyl("GA_sma", 3.2, 8.0, (gx - w / 2.0 - 3.5, gy, 38.0),
        rot=(0, 90, 0), mat=M["sma_gold"], col=col)

    # ---- Laptop -----------------------------------------------------
    lx, ly, lz = 300, 155, 20
    w, d, t = (DIM["laptop"]["w"], DIM["laptop"]["d"], DIM["laptop"]["t"])
    box("LAP_base", (w, d, t), (lx, ly, lz - t / 2.0), rot=(0, 0, 205),
        mat=M["laptop"], col=col, bev=1.5)
    box("LAP_screen", (w, 6.0, 195.0), (lx - 62, ly + 62, lz + 95.0),
        rot=(0, 0, 205), mat=M["laptop"], col=col, bev=1.5)
    box("LAP_panel", (w - 34, 2.0, 165.0), (lx - 58, ly + 60, lz + 95.0),
        rot=(0, 0, 205), mat=M["screen"], col=col)
    return col


# =====================================================================
# 7. STUDIO, CAMERA'S, RENDERS
# =====================================================================
def setup_studio(M):
    col = ensure_collection("00_Studio")
    sc = bpy.context.scene
    w = bpy.data.worlds.get("GStemWorld") or bpy.data.worlds.new("GStemWorld")
    sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes.get("Background")
    bg.inputs[0].default_value = (0.010, 0.011, 0.014, 1.0)
    bg.inputs[1].default_value = 1.0
    box("Tafel", (1500, 1100, 30), (20, -60, -15 - BOARD_BOTTOM_Z),
        mat=M["table"], col=col, bev=4)

    tgt = empty("Studiodoel", (0, -20, 5), col)

    def light(name, loc, size, energy, color=(1.0, 1.0, 1.0)):
        bpy.ops.object.light_add(type='AREA')
        o = bpy.context.active_object
        o.name = name
        o.data.shape = 'SQUARE'
        o.data.size = size * MM
        o.data.energy = energy
        o.data.color = color
        o.location = (loc[0] * MM, loc[1] * MM, loc[2] * MM)
        move_to(o, col)
        aim(o, tgt)
        return o

    light("Key", (230, -320, 340), 420, 13)
    light("Fill", (-380, -240, 250), 700, 5.0, (0.92, 0.95, 1.0))
    light("Rim", (-60, 400, 320), 420, 9.0, (0.85, 0.9, 1.0))
    light("Top", (10, -40, 470), 700, 6.5)
    return tgt


def build_cameras(tgt, M):
    col = ensure_collection("00_Studio")
    cams = {}

    bpy.ops.object.camera_add()
    c = bpy.context.active_object
    c.name = "CAM_top"
    c.data.type = 'ORTHO'
    c.data.ortho_scale = 118 * MM
    c.data.clip_start = 0.01
    c.location = (0, 0, 700 * MM)
    move_to(c, col)
    cams["top"] = c

    t1 = empty("Doel_34", (15, -42, 5), col)
    bpy.ops.object.camera_add()
    c = bpy.context.active_object
    c.name = "CAM_34"
    c.data.lens = 50
    c.data.clip_start = 0.01
    c.location = (170 * MM, -285 * MM, 215 * MM)
    move_to(c, col)
    aim(c, t1)
    cams["iso"] = c

    t2 = empty("Doel_detail", (-25, 14, 6), col)
    bpy.ops.object.camera_add()
    c = bpy.context.active_object
    c.name = "CAM_detail"
    c.data.lens = 70
    c.data.clip_start = 0.01
    c.location = (-58 * MM, -64 * MM, 125 * MM)
    move_to(c, col)
    aim(c, t2)
    cams["detail"] = c
    return cams


def render_all(cams):
    os.makedirs(OUT_DIR, exist_ok=True)
    sc = bpy.context.scene

    hide_col_render("05_Mockup", True)
    hide_col_render("04_Wiring", True)
    sc.camera = cams["top"]
    sc.render.resolution_x, sc.render.resolution_y = 1400, 1050
    sc.render.filepath = os.path.join(OUT_DIR, "01_bovenaanzicht.png")
    bpy.ops.render.render(write_still=True)
    log("render klaar: 01_bovenaanzicht.png")

    sc.camera = cams["detail"]
    sc.render.resolution_x, sc.render.resolution_y = 1600, 1200
    sc.render.filepath = os.path.join(OUT_DIR, "03_detail_voeding.png")
    bpy.ops.render.render(write_still=True)
    log("render klaar: 03_detail_voeding.png")

    hide_col_render("05_Mockup", False)
    hide_col_render("04_Wiring", False)
    sc.camera = cams["iso"]
    sc.render.resolution_x, sc.render.resolution_y = 1800, 1250
    sc.render.filepath = os.path.join(OUT_DIR, "02_drie_kwart.png")
    bpy.ops.render.render(write_still=True)
    log("render klaar: 02_drie_kwart.png")


# =====================================================================
# 8. CONTROLE + MAIN
# =====================================================================
CHECK = ["U1_xiao_pcb", "U1_kit_pcb", "U5_gnss_pcb", "U6_bno085_pcb",
         "U7_bmp581_pcb", "U2_buck_pcb", "U4_txb_pcb", "J2_term_body",
         "J1_barrel_body", "ANT1_sma_base"]


def check_overlaps():
    bpy.context.view_layer.update()
    aabb = {}
    for name in CHECK:
        ob = bpy.data.objects.get(name)
        if ob is None:
            continue
        pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
        aabb[name] = (min(p.x for p in pts), min(p.y for p in pts),
                      max(p.x for p in pts), max(p.y for p in pts))
    bad = []
    keys = list(aabb)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = aabb[keys[i]], aabb[keys[j]]
            ox = min(a[2], b[2]) - max(a[0], b[0])
            oy = min(a[3], b[3]) - max(a[1], b[1])
            if ox > 0.001 and oy > 0.001:
                bad.append((keys[i], keys[j], round(ox * 1000, 1),
                            round(oy * 1000, 1)))
    for row in bad:
        log("OVERLAP", row)
    if not bad:
        log("geen overlap gevonden tussen de modules")
    return bad


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    wipe()
    setup_scene()
    M = build_materials()
    build_board(M)
    build_components(M)
    build_modules(M)
    build_wiring(M)
    build_mockup(M)
    tgt = setup_studio(M)
    cams = build_cameras(tgt, M)
    check_overlaps()
    blend = os.path.join(ROOT, "documenten", "blender", "gstem-mockup.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend)
    log("opgeslagen:", blend)
    if RENDER:
        render_all(cams)
    log("klaar")


main()
