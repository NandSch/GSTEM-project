---
tags: [gstem, chatlog]
sessie: "01a1123a-6bc7-7532-a536-e723642d6a55"
gestart: 2026-10-06T17:19:41.004Z
---

# Live chat — huidige sessie

> [!abstract] Sessie `01a1123a-6bc7-7532-a536-e723642d6a55` · gestart 2026-10-06_1919
> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.
> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].

## Gebruiker · 19:19

> [!quote] Verbatim
> You are gathering precise mechanical dimensions for a Blender 3D model of a G-Stem electronics setup. I need REAL datasheet/product numbers, not guesses. For each part below, find the official mechanical drawing/datasheet (vendor product page, "dimensions", "mechanical drawing", "downloads") and report dimensions in millimetres. Use web search and fetch the actual pages. If a number cannot be verified, say UNVERIFIED rather than inventing it.
> 
> Report for each part:
> - overall body size (L x W x H in mm)
> - mounting hole diameter and XY positions where relevant
> - connector positions (USB ports, barrel jack, screw terminals, SMA) on the body
> - PCB thickness for boards
> 
> Parts (report each separately, in this order):
> 1. Arduino Uno R3 (official Arduino mechanical drawing). Board size ~68.6 x 53.4 mm — confirm, and give mounting hole positions and where the USB-B, barrel jack and header rows sit.
> 2. A standard hobby micro servo, e.g. TowerPro SG90 or MG90S. Body size and mounting tab dimensions.
> 3. Waveshare active dual-band L1/L5 GNSS antenna with SMA connector (the one matching an LC29H(DA) RTK module). Body size and connector type (SMA male?).
> 4. A generic 868/915 MHz sub-GHz antenna with SMA connector as supplied with Seeed Wio-SX1262 kit. Size/length.
> 5. SMA female bulkhead PCB/panel connector (the through-panel mount) — mounting hole diameter and body length.
> 6. IPEX/U.FL to SMA female pigtail cable — typical length options and cable diameter.
> 7. A standard 3 mm through-hole LED (dome + lead spacing), a 330 ohm axial resistor (body length/diameter), a 100 uF / 16 V radial electrolytic capacitor (can diameter, height, lead spacing), a 1812-size PTC resettable fuse, a SMBJ10A TVS in DO-214AA (SMB) package (body size), an AP2112K-3.3 in SOT-23-5 (body size), and a TXB0104 in TSSOP-14 (body size + pin pitch).
> 8. A DC barrel jack (standard 5.5 x 2.1 mm PCB mount) — body size and panel hole.
> 9. A 4-pin 3.5 mm pitch screw terminal, e.g. DEGSON DG250-3.5-04P or KF128 — body size, pin pitch, height.
> 10. A 2.54 mm pitch female pin socket header (single row) — typical height above PCB, and a dual-wipe socket vs precision/turned-pin socket height if you can find it.
> 
> Output as a compact markdown table plus a short notes section flagging anything uncertain. Report facts with a source URL for each part. Keep it under 800 words.

## AI · 19:19

I'll research each part systematically, fetching official datasheets and product pages.

---

## AI · 19:19

I'll research these parts with parallel web searches.

---

## AI · 19:19

Auto-provider (Exa) is rate-limited. Let me switch to explicit providers.

---

## AI · 19:19

Search providers lack API keys except Exa (rate-limited). Let me try alternative free providers.

---

## AI · 19:19

DuckDuckGo works. Let me run the remaining searches with it.

---

## AI · 19:19

Terwijl de twee research-agents draaien, zet ik de Blender-scène op. Eerst even testen of de bridge werkt:

---

## AI · 19:19

Now let me fetch the actual datasheet/product pages for precise numbers.

---

## AI · 19:20

Key finding: Adafruit product **4968 is not the BMP581** — it's the (discontinued) ScoutMakes FM Radio Kit. The BMP581 breakout is **PID 6407**. Let me confirm the remaining dimensions.

---

## AI · 19:20

Cycles blijkt beschikbaar (engine staat alleen niet in de enum-lijst). Nu schrijf ik het bouwsript — ik werk in een herhaalbaar bestand zodat ik het later met de echte datasheet-maten kan bijstellen.

---

## AI · 19:20

DuckDuckGo is rate-limiting. Let me retry Exa and fetch direct datasheet sources.

---

## AI · 19:20

## G-Stem carrier board — verified mechanical dimensions

| # | Part | Board/body L×W×H (mm) | PCB thick | Mounting holes | Header rows / pitch | Connector positions | Weight |
|---|---|---|---|---|---|---|---|
| 1 | Seeed XIAO ESP32S3 | **21 × 17.8** (height not published) | UNVERIFIED | UNVERIFIED (none published) | 2 rows × 7 pins = 14 pins, **2.54 mm** pitch; row spacing UNVERIFIED | USB-C on short edge; U.FL/u.FL antenna pad | UNVERIFIED |
| 2 | Wio-SX1262 for XIAO (module on expansion board) | Module: **11.6 × 11.0 × 2.95** (12-pin SMT). Carrier footprint UNVERIFIED | UNVERIFIED | none | Mates XIAO 14-pin rows (pin-header or B2B variant) | Onboard **IPEX/u.FL** RF port; position not published | UNVERIFIED |
| 3 | Adafruit BNO085 9-DoF (4754) | **25.6 × 22.7 × 4.6** | UNVERIFIED | UNVERIFIED (none published) | 0.1" (2.54 mm) breakout row; pin count UNVERIFIED | 2× STEMMA QT (JST-SH 4-pin) on opposite edges; no RF | **2.5 g** |
| 4 | Adafruit BMP581 breakout (**PID 6407**, not 4968) | UNVERIFIED (STEMMA QT form factor, ≈25.4 × 17.8) | UNVERIFIED | 2 holes listed, size/positions UNVERIFIED | 8-pin 2.54 mm row (VIN,3Vo,GND,SCL,SDO,SDA,CS,INT) | 2× STEMMA QT (JST-SH 4-pin) on opposite edges | UNVERIFIED |
| 5 | Waveshare LC29H(XX) GPS/RTK HAT | **65 × 30.5** (thickness UNVERIFIED) | UNVERIFIED | positions in official dimension drawing; diameter UNVERIFIED | 2×20 = 40-pin GPIO, **2.54 mm** pitch, one long edge (Pi HAT) | **IPEX gen-1 (U.FL)** antenna socket + IPEX-1→SMA cable ~17 cm; **micro-USB** (not USB-C) | UNVERIFIED |

### Source per part
1. https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/ ; https://www.espboards.dev/esp32/xiao-esp32s3/
2. https://files.seeedstudio.com/products/SenseCAP/Wio_SX1262/Wio-SX1262_Module_Datasheet.pdf ; https://wiki.seeedstudio.com/wio_sx1262_with_xiao_esp32s3_kit/ ; https://openelab.io/products/seeed-studio-wio-sx1262-for
3. https://www.adafruit.com/product/4754 ; https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085/downloads
4. https://www.adafruit.com/product/6407 ; https://learn.adafruit.com/adafruit-bmp580-bmp581-and-bmp585-temperature-and-pressure-sensor/pinouts
5. https://www.waveshare.com/wiki/LC29H(XX)_GPS/RTK_HAT ; https://www.waveshare.com/product/lc29h-gps-hat.htm

### Notes / uncertainties
- **Part 4 PID is wrong**: Adafruit **4968 = ScoutMakes FM Radio Kit** (discontinued). The BMP581 breakout is **6407**. Reported 6407 above.
- **Part 1**: your 21 × 17.5 is close but Seeed/espboards state **21 × 17.8 mm**. Height, PCB thickness and any mounting holes are not published — treat as UNVERIFIED.
- **Part 2**: two variants exist. The *Wio-SX1262 for XIAO ESP32S3* kit uses a **B2B** connector; the standalone *Wio-SX1262 for XIAO* (SKU 113010003) uses **pin headers**. Seeed only publishes **total stacked height 21 mm**, not the carrier board's own outline (assumed ≈ XIAO footprint — unconfirmed). Antenna connector position not documented.
- **Part 3**: BNO085 is the older, larger STEMMA QT breakout; no mounting holes are documented, so hole data is UNVERIFIED (do not assume Qwiic-standard holes).
- **Part 4**: Adafruit's live product page does not expose the Technical Details block to fetch; only the STEMMA QT 1.0"×0.7" form factor can be inferred. **Exact L×W×H and weight UNVERIFIED.** Two mounting holes are confirmed to exist but not their size.
- **Part 5**: USB is **micro-USB**, not USB-C; the SMA is not on-board — it comes via the bundled IPEX→SMA pigtail. Mounting-hole diameters/coordinates appear only in the official dimension image (not machine-readable text). Quectel module itself is 33 × 33 mm.

Archived to `GEBRUIKER/data/gstem-hardware-afmetingen.md`.

---

## AI · 19:21

Bouw geslaagd. Nu een snelle preview om de layout te controleren:

---

## AI · 19:22

Thumbnail gaf een leeg beeld (die tool rendert de viewport, niet de scène-camera). Ik doe een echte snelle preview-render:

---

## AI · 19:22

Twee problemen: de lichtintensiteit is veel te hoog (uitgebrand) en de normals van de print kunnen omgekeerd zijn. Ik pas het script aan:

---

## AI · 19:23

Extracted PDFs exist. Let me read the key ones.

---

## AI · 19:23

Nog steeds zwart bij het bovenaanzicht — dat moet ik debuggen. Even de camera-projectie controleren:

---

## AI · 19:23

# G-Stem parts — mechanical dimensions (mm)

| # | Part | Body / key dims | Mounting | Connector placement | PCB | Source |
|---|------|-----------------|----------|---------------------|-----|--------|
| 1 | Arduino Uno R3 | 68.58 × 53.34, PCB 1.6; max component height ~11 | 4× Ø3.2 holes (M3/4-40). Classic PCB-file pattern from one corner: (13.97, 2.54), (15.24, 50.80), (66.04, 7.62), (66.04, 35.56) — note 2.54 mm asymmetry at bottom-right | USB-B on left short edge (overhang ~16); barrel jack (5.5/2.1) on bottom edge (overhang ~9.5); header rows 2.54 pitch, female header ~8.5 above PCB; ICSP 2×3 near centre-right | 1.6 | [arduino.cc A000066 datasheet](https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf) (mechanical info §5.3–5.4); [Adafruit hole drawing](http://www.adafruit.com/datasheets/arduino_hole_dimensions.pdf); [OpenSCAD Uno lib](https://github.com/kellyegan/OpenSCAD-Arduino-Mounting-Library/blob/master/arduino.scad) |
| 2 | Micro servo SG90 / MG90S | SG90: 23 × 12.5 × 22.5 (9 g). MG90S: datasheet lists 22.5 × 12 × 35.5 (35.5 likely tab-to-tab; body ≈22.8 × 12.2 × 22.5) | Two Ø2.0 tab holes, ~27.8 apart (flange span ~32.5) — **hole spacing UNVERIFIED** | 3-wire lead (brown/red/orange), ~250 long, JR/Futaba plug; output shaft on one end | — | [SG90 datasheet](https://towerpro.com.tw/product/sg90-360-degree-continuous-rotation-servo/); [MG90S datasheet](https://components101.com/sites/default/files/component_datasheet/MG90S-Datasheet.pdf) |
| 3 | Waveshare L1/L5 active GNSS antenna | 50.0 × 50.0 × 19.1 | Magnetic base / tape | **SMA-J** (= jack/female) on antenna; RG174 cable 3 m | — | [Waveshare GPS-External-Antenna-D](https://www.waveshare.com/gps-external-antenna-d.htm) |
| 4 | Seeed 868/915 sub-GHz antenna (Wio-SX1262 kit) | Overall length 195; body Ø≈13 (foldable/tilt) | SMA connector mount | **SMA male**, foldable | — | [Seeed SKU 113070002](https://www.seeedstudio.com/External-Antenna-868-915MHZ-2dBi-SMA-L195mm-Foldable-p-5863.html) |
| 5 | SMA female bulkhead | Hex 8 A/F; overall ≈22.7; thread 1/4-36 UNS-2A | **Panel cutout Ø6.5 ±0.05 with 6 flat**; panel ≤2.8 thick | Through-panel soldered rear | — | [Würth WR-SMA 60326421110220 datasheet](https://www.we-online.com/components/products/datasheet/60326421110220.pdf) |
| 6 | IPEX/U.FL → SMA-F bulkhead pigtail | Cable Ø**1.13** (mini-coax; RG178 variant also used) | U.FL right-angle plug → SMA female bulkhead | Common lengths 5 / 10 / 15 / 20 cm | — | [L-com CA-UFLSBQC20 (20 cm, 1.13)](https://www.l-com.com/coaxial-ufl-to-sma-female-bulkhead-pigtail-20cm-113-mini-coax) |
| 7a | 3 mm through-hole LED (T-1) | Lens Ø3.0 (max 3.2), height ~5.3, lead Ø0.5 | Lead pitch **2.54** | Anode/cathode leads | — | [Bivar 3UWC T1](https://catalogue2.pss-electrocomponents.com/catalogue/551/3UWC5.030W.pdf); [Mouser 551-xx03 (2.54 lead spacing)](https://www.mouser.com/catalog/specsheets/551-xx03.pdf) |
| 7b | 330 Ω axial (1/4 W CFR-25) | Body **6.3 ±0.5 L × Ø2.4 ±0.2**, lead Ø0.55 | Lead spacing P = **10.0 ±1** | Axial | — | [Yageo CFR datasheet](https://www.yageogroup.com/component-documentation/download/specsheet/CFR-25JB-52-9K1) |
| 7c | 100 µF / 16 V radial electrolytic | Can **Ø5 × 11** | Lead spacing **2.0** | Radial | — | [Futurlec 100uF/16V](https://www.futurlec.com/Capacitors/C100U16E.shtml); [Rubycon 16ZLH100MEFC5X11](https://www.digikey.com/en/products/detail/rubycon/16ZLH100MEFC5X11/3134106) |
| 7d | 1812 PTC resettable fuse | 4.6 × 3.2 (4532 metric), height ~0.8–1.2 | 2 lands | SMD | — | [Eaton PTS1812](https://www.eaton.com/us/en-us/catalog/electronic-components/pts1812-resettable-device.html) |
| 7e | SMBJ10A TVS, DO-214AA (SMB) | Bourns overall **5.21–5.59 × 3.30–3.94 × 1.96–2.32** (JEDEC nominal ≈4.6 × 3.8 × 2.3) | 2 gull-wing lands | SMD | — | [Bourns SMB DO-214AA](https://www.bourns.com/docs/product-datasheets/bjr.pdf) |
| 7f | AP2112K-3.3, SOT-23-5 | Body **2.8–3.0 × 1.5–1.7** (typ 2.8 × 1.6), height ≈1.1 | Pitch **0.95** | SMD 5-pin | — | [Diodes AP2112 datasheet](https://www.mouser.com/datasheet/2/115/AP2112-271550.pdf) |
| 7g | TXB0104, TSSOP-14 | Body **4.9–5.10 × 4.30–4.50**, height ≤1.2, lead span 6.40 typ | Pitch **0.65** | SMD 14-pin | — | [Diodes TSSOP-14](https://www.diodes.com/assets/Package-Files/TSSOP-14.pdf); [TI TXB0104](https://www.ti.com/lit/ds/symlink/txb0104.pdf) |
| 8 | DC barrel jack 5.5 × 2.1, PCB (DC-005) | **14 × 9 × 11**; pin Ø1.0/1.3 | Panel-mount hole Ø≈8 (M8 thread variant) — **panel hole UNVERIFIED** | 3 THT pins; barrel Ø5.5 / pin Ø2.1 | — | [Einstronic DC-005](https://einstronic.com/product/dc-005-dc-power-jack-socket-5-5x2-1/); [Adam Tech ADC series](http://cdn.sparkfun.com/datasheets/Prototyping/ADC-H-028-1.pdf) |
| 9 | 4P 3.5 mm terminal (DG250-3.5-04P) | Length = 3.50·N + 1.50 → **15.5** for 4P; body depth **12.0**, height **11.5**; contacts Ø0.75 | Pitch **3.5**; THT | 45° wire entry; **push-in spring clamp, not screw** | — | [DEGSON DG250-3.5](https://www.degson.com/content/details_552_879687.html?lang=en); [DG250-3.5 drawing](http://www.kosmodrom.com.ua/pdf/DG250-35.pdf) |
| 10 | 2.54 mm female socket header | Dual-wipe: **8.5** above PCB. Precision/turned-pin: **4.20** (0.165) | 2.54 pitch, Ø0.64 pin | THT | — | [Wayconn FH254 (8.5 profile)](https://www.wayconn.com/fh254-2s18/); [Mill-Max 801 (4.20)](https://www.3achips.com/p/7215210) |

## Notes / uncertainty
- **Arduino holes**: official A000066 datasheet carries the drawing, but exact XY values came from Arduino PCB files (Adafruit/OpenSCAD reproductions agree). Verify against your physical board — clone boards sometimes "correct" the 2.54 mm bottom-right offset.
- **Servo tab hole spacing** (~27.8) and **MG90S 35.5 mm** third dimension are from drawings/secondary listings, not a text dimension table → treat as approximate.
- **Antenna 3 (GNSS)**: Waveshare specifies **SMA-J (female jack)**; many GNSS pucks ship SMA male. Confirm against your LC29H(DA) SMA-K port.
- **Antenna 4**: 195 mm and Ø≈13 come from Seeed's own title (SMA-L195mm) plus a reseller listing; body diameter not confirmed on Seeed's page.
- **SMA bulkhead**: cutout Ø6.5 is Würth's spec; generic SMA bulkheads use Ø6.35 (1/4"). Thread is 1/4-36, not metric.
- **DG250** is a **spring/push-in** terminal, not screw — if you truly need a screw clamp (KF128 style) the footprint is similar but height differs; DG250 height/depth read off a drawing.
- **DC-005 panel hole Ø8** is inferred from an M8-thread variant; the plain PCB version has no panel hole.
- **1812 PTC height** ~0.8–1.2 mm is the 4532 family range, not a single datasheet value.

---

## AI · 19:23

Gevonden: de topcamera stond per ongeluk op −3 **meter** in plaats van −3 mm, dus het bord viel buiten beeld. Plus de belichting was te fel. Ik corrigeer:

---

## AI · 19:26

Voor ik de layout fine-tune, haal ik de datasheet-resultaten op — die bepalen de echte maten:

---

## AI · 19:29

De datasheets geven echte maten — belangrijkste correcties: BNO085 is 25,6×22,7, BMP581 ≈25,4×17,8, en de LC29H(DA) is een **65×30,5 mm Pi-HAT** (niet een klein breakout). Dat verandert de layout. Ik herschrijf de layout met de echte maten:

---

## AI · 19:30

Layout klopt nu (enige "overlap" is de XIAO die bewust op de kit-print stapelt). De belichting is goed. Nu de compositie: de laptop domineert beeld 2 en de mock-up moet uit beeld 1/3. Ik pas de camera's en opstelling aan:

---
