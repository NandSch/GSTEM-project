from xml.etree.ElementTree import Element, SubElement, ElementTree
from pathlib import Path

# Script staat in documenten/scripts/; het resultaat hoort in documenten/pcb/.
OUT = Path(__file__).resolve().parent.parent / 'pcb' / 'Communicatie-overzicht-GSTEM.drawio'
mxfile = Element('mxfile', {
    'host': 'app.diagrams.net', 'agent': 'Pi coding agent',
    'version': '24.7.17', 'type': 'device',
})

STYLES = {
    'zoneBlue': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f9ff;strokeColor=#6c8ebf;strokeWidth=2;fontStyle=1;fontSize=16;align=left;verticalAlign=top;spacingTop=10;spacingLeft=12;',
    'zoneGreen': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#f3faf3;strokeColor=#82b366;strokeWidth=2;fontStyle=1;fontSize=16;align=left;verticalAlign=top;spacingTop=10;spacingLeft=12;',
    'zonePurple': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fbf5ff;strokeColor=#9673a6;strokeWidth=2;fontStyle=1;fontSize=16;align=left;verticalAlign=top;spacingTop=10;spacingLeft=12;',
    'zoneYellow': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fffaf0;strokeColor=#d6b656;strokeWidth=2;fontStyle=1;fontSize=16;align=left;verticalAlign=top;spacingTop=10;spacingLeft=12;',
    'app': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'external': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'service': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'radio': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'sensor': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'controller': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'power': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;strokeWidth=2;fontSize=12;align=left;verticalAlign=middle;spacing=8;',
    'mechanical': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;strokeWidth=2;fontSize=13;align=center;verticalAlign=middle;spacing=8;',
    'note': 'shape=note;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=12;align=left;verticalAlign=middle;spacing=8;',
    'terminal': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;strokeWidth=2;fontSize=12;align=center;verticalAlign=middle;spacing=6;',
}

def page(name, page_id, width, height):
    diagram = SubElement(mxfile, 'diagram', {'id': page_id, 'name': name})
    model = SubElement(diagram, 'mxGraphModel', {
        'dx': str(width), 'dy': str(height), 'grid': '1', 'gridSize': '10',
        'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1',
        'fold': '1', 'page': '1', 'pageScale': '1', 'pageWidth': str(width),
        'pageHeight': str(height), 'math': '0', 'shadow': '0',
    })
    root = SubElement(model, 'root')
    SubElement(root, 'mxCell', {'id': '0'})
    SubElement(root, 'mxCell', {'id': '1', 'parent': '0'})
    return root

def vertex(root, cid, label, x, y, w, h, style):
    cell = SubElement(root, 'mxCell', {
        'id': cid, 'value': label, 'style': STYLES.get(style, style),
        'vertex': '1', 'parent': '1',
    })
    SubElement(cell, 'mxGeometry', {
        'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h), 'as': 'geometry',
    })

def edge(root, cid, source, target, label, color, both=False, dashed=False, width=2):
    style = f'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth={width};strokeColor={color};fontColor=#333333;fontSize=12;labelBackgroundColor=#ffffff;endArrow=block;endFill=1;'
    if both:
        style += 'startArrow=block;startFill=1;'
    if dashed:
        style += 'dashed=1;dashPattern=6 4;'
    cell = SubElement(root, 'mxCell', {
        'id': cid, 'value': label, 'style': style, 'edge': '1', 'parent': '1',
        'source': source, 'target': target,
    })
    SubElement(cell, 'mxGeometry', {'relative': '1', 'as': 'geometry'})

# Pagina 1: volledige systeemarchitectuur en communicatie
r = page('Systeemcommunicatie', 'system-communication', 1700, 1040)
vertex(r, 'z_laptop', '<b>LAPTOP EN SOFTWARE</b><br>USB-ontvanger wordt als USB-stick gebruikt', 25, 80, 360, 770, 'zoneBlue')
vertex(r, 'z_receiver', '<b>USB-LoRa-ONTVANGER</b><br>tweede identieke XIAO-kit', 415, 210, 235, 390, 'zonePurple')
vertex(r, 'z_module', '<b>MEETTOESTEL</b><br>Draagprint met modules in 3D-geprinte behuizing met demping', 680, 80, 635, 770, 'zoneGreen')
vertex(r, 'z_aircraft', '<b>STILSTAANDE VLIEGTUIGMOCK-UP</b><br>Arduino Uno, roeren en servo’s', 1340, 170, 330, 630, 'zoneYellow')
# Verbindingen worden vóór de componentblokken toegevoegd zodat ze erachter liggen.
edge(r, 'e_api', 'app', 'external', 'Lokale API: metingen als JSON → extern programma<br>commando als CSV ← terug (transport nog te kiezen)', '#9673a6', both=True, dashed=True)
edge(r, 'e_ntrip', 'ntrip', 'app', 'Internet: NTRIP levert RTCM-correcties aan de app', '#d79b00')
edge(r, 'e_usb', 'app', 'receiver', 'USB-A ↔ USB-C<br>USB-serieel: telemetrie ↑ en commando’s ↓', '#3d85c6', both=True)
edge(r, 'e_lora', 'receiver', 'esp', 'LoRa, beoogd 868 MHz*<br>meetdata ↑ · CSV-commando’s + RTCM ↓', '#9673a6', both=True, width=3)
edge(r, 'e_app_ntrip_path', 'app', 'receiver', 'RTCM via USB-serieel ↓', '#d79b00', dashed=True)
edge(r, 'e_imu', 'imu', 'esp', 'I²C · SDA/SCL · 3,3 V-logica', '#2f75b5', both=True)
edge(r, 'e_baro', 'baro', 'esp', 'I²C · SDA/SCL · 3,3 V-logica', '#2f75b5', both=True)
edge(r, 'e_gnss', 'gnss', 'esp', 'UART: positie/metingen ↑<br>RTCM-correcties ↓ (route te valideren)', '#70ad47', both=True)
edge(r, 'e_gnss_ant', 'gnss_ant', 'gnss', 'GNSS RF · SMA', '#666666', both=True)
edge(r, 'e_lora_ant', 'esp', 'lora_ant', 'SX1262 RF · IPEX/U.FL → SMA', '#9673a6', both=True)
edge(r, 'e_receiver_ant', 'receiver', 'receiver_ant', 'LoRa RF', '#9673a6', both=True)
edge(r, 'e_uart_esp_shifter', 'esp', 'shifter', 'UART TX/RX · 3,3 V', '#70ad47', both=True)
edge(r, 'e_shifter_terminal', 'shifter', 'terminal', 'TX/RX · niveau 3,3 ↔ 5 V', '#70ad47', both=True)
edge(r, 'e_terminal_uno', 'terminal', 'uno', '4-aderige kabel: GND, +5 V, TX, RX<br>CSV-commando’s ESP → Uno; retourverkeer niet vastgelegd', '#70ad47', both=True)
edge(r, 'e_uno_servo', 'uno', 'servos', 'PWM-servosignalen<br>rolroeren · hoogteroer · richtingsroer', '#70ad47')
edge(r, 'e_buck_servo', 'servo_buck', 'servos', 'afzonderlijke servovoeding', '#d79b00')
# Laptopsoftware en netwerk
vertex(r, 'app', '<b>Laptopapplicatie</b><br>• verbindingsstatus USB + meettoestel<br>• kaart + live meetwaardentabel<br>• Code-modus: berekent CSV-commando’s<br>• API-modus: koppeling met extern programma<br>• opslag van meetdata/route (beoogd)', 50, 145, 310, 215, 'app')
vertex(r, 'external', '<b>Extern programma (optioneel)</b><br>Ontvangt live meetdata als JSON via de lokale API en kan een vrije CSV-commando-regel terugsturen.', 50, 410, 310, 110, 'external')
vertex(r, 'ntrip', '<b>NTRIP-correctiedienst</b><br>Internet op de laptop → RTCM-correcties naar de GNSS-rover<br>Provider nog te kiezen', 50, 570, 310, 105, 'service')
vertex(r, 'laptop_note', '<b>Op de laptop</b><br>USB-ontvanger wordt ingeplugd; de app start volgens de gebruikersspecificatie automatisch. De app controleert USB apart van geldige meetpakketten via LoRa.', 50, 715, 310, 105, 'note')
# USB-ontvanger
vertex(r, 'receiver', '<b>USB-LoRa-adapter</b><br>XIAO ESP32S3 + Wio-SX1262-kit<br>USB-serieel ↔ laptop<br>ontvangt meetdata en zendt downlink terug', 435, 300, 195, 145, 'radio')
vertex(r, 'receiver_ant', '<b>LoRa-antenne</b><br>bij de kit<br>ontvangerzijde', 445, 490, 175, 70, 'radio')
# Meettoestel: sensoren, rekenkern, antennes, uitgang en voeding
vertex(r, 'imu', '<b>9-DoF IMU</b><br>Adafruit BNO085<br>oriëntatie/beweging · I²C', 710, 175, 195, 90, 'sensor')
vertex(r, 'baro', '<b>Barometer</b><br>Adafruit BMP581<br>druk/temperatuur · I²C', 710, 305, 195, 90, 'sensor')
vertex(r, 'gnss', '<b>RTK-GNSS rover</b><br>Waveshare LC29H(DA) HAT<br>UART · positie/snelheid · RTCM-invoer', 710, 435, 195, 100, 'sensor')
vertex(r, 'gnss_ant', '<b>Actieve dual-band GNSS-antenne</b><br>L1/L5 · meegeleverd bij HAT', 710, 565, 195, 65, 'sensor')
vertex(r, 'esp', '<b>Meetcontroller + LoRa</b><br>XIAO ESP32S3 + Wio-SX1262-kit<br>leest sensoren, bundelt meetpakketten,<br>stuurt telemetrie via LoRa, geeft<br>besturingscommando’s door naar UART<br>en bewaakt lokaal de failsafe', 1010, 285, 250, 155, 'controller')
vertex(r, 'lora_ant', '<b>LoRa-antenne</b><br>kitantenne via U.FL/IPEX–SMA-pigtail<br>buiten de behuizing', 1040, 165, 195, 70, 'radio')
vertex(r, 'shifter', '<b>Level shifter</b><br>TXB0108-module volgens bestellijst*<br>3,3 V ↔ 5 V UART', 1005, 485, 135, 100, 'controller')
vertex(r, 'terminal', '<b>4-pins connector</b><br>3,5 mm · GND / +5 V / TX / RX', 1155, 485, 135, 100, 'terminal')
vertex(r, 'power', '<b>Voeding op draagprint</b><br>2S LiPo 7,4 V + barrel-invoer → 2 A PTC + TVS SMBJ10A → buck 5 V → 5 V-rail.<br>AP2112K-3.3 maakt een schone 3,3 V-rail voor sensoren/TXB0108. Gemeenschappelijke GND; bulk-elco 100 µF, ontkoppelcondensatoren en power-LED + 330 Ω.<br>Geen P-MOSFET-ompoolbeveiliging.', 705, 665, 585, 160, 'power')
# Arduino en servo's
vertex(r, 'uno', '<b>Arduino Uno</b><br>Ontvangt CSV via UART TX/RX en stelt servo’s in.<br>De exacte veldvolgorde en baudrate zijn nog niet vastgelegd.', 1400, 275, 210, 155, 'controller')
vertex(r, 'servos', '<b>Servo’s (3+)</b><br>• rolroeren (links/rechts)<br>• hoogteroer<br>• richtingsroer', 1385, 510, 240, 105, 'mechanical')
vertex(r, 'servo_buck', '<b>Aparte buck-converter</b><br>voeding servo’s<br>ingang/voedingsbron nog te controleren', 1395, 660, 220, 85, 'power')
vertex(r, 'airframe_note', '<b>3D-geprinte romp en stuurvlakken</b><br>Stilstaande demonstratie; geen vliegend/volledig functioneel vliegtuig.', 1370, 755, 275, 40, 'note')
vertex(r, 'legend1', '<b>Leeswijzer</b> — blauwe lijn: I²C · groene lijn: UART/CSV · paarse lijn: LoRa/RF · oranje lijn: voeding/correcties · pijlen in beide richtingen: bidirectioneel.', 25, 875, 1645, 55, 'note')
vertex(r, 'caveat1', '<b>Ontwerpstatus en aandachtspunten</b><br>* De actuele bestellijst gebruikt BNO085/BMP581 en een TXB0108-module; oudere projectnotities noemen BNO055/BMP390 en TXB0104. Variantsynchronisatie en definitieve modulekeuze moeten nog bevestigd worden. Pinout, 5 V-voeding van de Uno, servobuck-aansluiting, LoRa-pakketformaat/instellingen, API-transport, GNSS-correctieroute, CSV-veldvolgorde en baudrate zijn nog te valideren. 868 MHz is beoogd voor België, configuratie blijft open. Schematisch, niet op schaal.', 25, 940, 1645, 75, 'note')

# Pagina 2: elektrische details van draagprint en Arduino-koppeling
r = page('Draagprint en UART-detail', 'carrier-wiring', 1700, 1000)
vertex(r, 'z_carrier', '<b>DRAAGPRINT / MEETTOESTEL</b><br>Modules, interfaces en voedingsboom (schematisch, niet op schaal)', 25, 80, 1050, 830, 'zoneGreen')
vertex(r, 'z_mockup2', '<b>ARDUINO EN MOCK-UP</b><br>stilstaande demonstratie', 1100, 80, 570, 830, 'zoneYellow')
# Voedings- en datasporen
edge(r, 'p_bat_prot', 'battery', 'protection', '7,4 V VBAT', '#d79b00')
edge(r, 'p_prot_buck', 'protection', 'buck5', 'VBAT beschermd', '#d79b00')
edge(r, 'p_buck_5v', 'buck5', 'rail5', '5 V', '#d79b00')
edge(r, 'p_5v_esp', 'rail5', 'xiao', '5 V + GND', '#d79b00')
edge(r, 'p_5v_gnss', 'rail5', 'gnss2', '5 V + GND', '#d79b00')
edge(r, 'p_5v_lm', 'rail5', 'ldo', '5 V-in', '#d79b00')
edge(r, 'p_ldo_rail3', 'ldo', 'rail3', '3,3 V', '#d79b00')
edge(r, 'p_3v_imu', 'rail3', 'imu2', '3,3 V + GND', '#d79b00')
edge(r, 'p_3v_baro', 'rail3', 'baro2', '3,3 V + GND', '#d79b00')
edge(r, 'p_5v_shift', 'rail5', 'level2', '5 V / VCCB', '#d79b00')
edge(r, 'p_5v_terminal', 'rail5', 'terminal2', '5 V beschikbaar*', '#d79b00', dashed=True)
edge(r, 'd_imu_xiao', 'imu2', 'xiao', 'I²C · SDA/SCL · 3,3 V', '#2f75b5', both=True)
edge(r, 'd_baro_xiao', 'baro2', 'xiao', 'I²C · SDA/SCL · 3,3 V', '#2f75b5', both=True)
edge(r, 'd_gnss_xiao', 'gnss2', 'xiao', 'UART · GNSS-data / RTCM-correcties', '#70ad47', both=True)
edge(r, 'd_ant_gnss', 'gnss2', 'gnssant2', 'SMA / RF', '#666666', both=True)
edge(r, 'd_ant_lora', 'xiao', 'loraant2', 'SX1262 RF · U.FL/IPEX → SMA', '#9673a6', both=True)
edge(r, 'd_xiao_shifter', 'xiao', 'level2', 'UART TX/RX · 3,3 V', '#70ad47', both=True)
edge(r, 'd_shifter_terminal', 'level2', 'terminal2', 'UART TX/RX · 5 V-zijde', '#70ad47', both=True)
edge(r, 'd_terminal_uno', 'terminal2', 'uno2', '4 draden: GND / +5 V / TX / RX<br>UART; CSV-commando ESP → Uno', '#70ad47', both=True)
edge(r, 'd_uno_servos', 'uno2', 'servos2', 'servo/PWM-signalen', '#70ad47')
edge(r, 'p_buck_servos', 'servoBuck2', 'servos2', 'aparte servo-voeding', '#d79b00')
# Voeding, breakouts en interfaces
vertex(r, 'battery', '<b>2S LiPo-accu</b><br>7,4 V (max. 8,4 V)<br>+ barrel-aansluiting', 55, 150, 145, 80, 'power')
vertex(r, 'protection', '<b>Voedingsbescherming</b><br>PTC 2 A + TVS SMBJ10A<br>geen P-MOSFET', 235, 150, 165, 80, 'power')
vertex(r, 'buck5', '<b>Buck-converter</b><br>uitgang 5 V<br>losse module', 440, 150, 145, 80, 'power')
vertex(r, 'rail5', '<b>5 V-rail</b><br>common GND', 635, 150, 140, 80, 'power')
vertex(r, 'ldo', '<b>AP2112K-3.3</b><br>5 V → schone 3,3 V', 850, 150, 175, 80, 'power')
vertex(r, 'rail3', '<b>3,3 V-rail</b><br>common GND', 850, 270, 175, 70, 'power')
vertex(r, 'imu2', '<b>IMU-breakout</b><br>Adafruit BNO085*<br>I²C · 9-DoF sensorfusie', 65, 375, 190, 100, 'sensor')
vertex(r, 'baro2', '<b>Barometer-breakout</b><br>Adafruit BMP581*<br>I²C · druk/temperatuur', 65, 525, 190, 100, 'sensor')
vertex(r, 'gnss2', '<b>GNSS HAT</b><br>Waveshare LC29H(DA)<br>RTK-rover · UART · 5 V', 65, 695, 190, 105, 'sensor')
vertex(r, 'gnssant2', '<b>GNSS-antenne</b><br>actief dual-band L1/L5<br>meegeleverd', 300, 715, 175, 70, 'sensor')
vertex(r, 'xiao', '<b>XIAO ESP32S3 + Wio-SX1262</b><br>centrale meetcontroller + LoRa-radio<br>op sockets op de draagprint<br>SX1262 wordt intern via SPI aangestuurd', 470, 405, 260, 135, 'controller')
vertex(r, 'loraant2', '<b>LoRa-antenne</b><br>kitantenne via U.FL/IPEX–SMA-pigtail', 490, 590, 225, 70, 'radio')
vertex(r, 'level2', '<b>TXB0108-module*</b><br>UART-levelshifter<br>3,3 V ↔ 5 V', 790, 450, 140, 100, 'controller')
vertex(r, 'terminal2', '<b>4-pins 3,5 mm schroefklem</b><br>GND / +5 V / TX / RX', 935, 450, 120, 100, 'terminal')
vertex(r, 'boardparts', '<b>Overige draagprint-onderdelen</b><br>socketheaders; 100 µF bulk-elco; ontkoppelcondensatoren (100 nF + 10 µF/module); power-LED + 330 Ω; koperbanen, 4× M3-bevestiging en gemeenschappelijke GND. Controleer de pull-ups op BNO085/BMP581 en voorkom dubbele I²C-pull-ups.', 275, 255, 500, 90, 'note')
vertex(r, 'shell', '<b>Mechanisch</b><br>eigen 3D-geprinte behuizing met demping, M3-schroeven/afstandsbussen; LoRa-antenne buiten de behuizing.', 65, 830, 990, 55, 'note')
# Arduino, aparte servovoeding en stuurvlakken
vertex(r, 'uno2', '<b>Arduino Uno</b><br>5 V-logica; ontvangt CSV via UART TX/RX en genereert servo-signalen.', 1160, 280, 210, 145, 'controller')
vertex(r, 'servos2', '<b>Servo’s (3+)</b><br>rolroeren (links/rechts), hoogteroer, richtingsroer', 1430, 390, 205, 115, 'mechanical')
vertex(r, 'servoBuck2', '<b>Aparte buck-converter</b><br>voor servovoeding<br>bron/aansluiting nog te bevestigen', 1150, 585, 215, 90, 'power')
vertex(r, 'plane2', '<b>3D-geprinte vliegtuigmock-up</b><br>servobewegingen worden mechanisch overgebracht op de stuurvlakken.', 1395, 650, 245, 105, 'note')
vertex(r, 'unknown2', '<b>Controle vóór aansluiten</b><br>* De actuele bestellijst noemt BNO085/BMP581 en TXB0108; oudere notities noemen BNO055/BMP390 en TXB0104. Bevestig de definitieve varianten en breakout-pinnen.<br>De +5 V-pin op de connector is voorzien, maar de Uno-voeding, stroomlimiet en voorkomen van terugvoeding via USB moeten worden gecontroleerd. De servo’s krijgen een aparte buck; de voedingsbron daarvan moet worden afgestemd. Exacte baudrate/CSV-velden zijn nog open.', 25, 925, 1645, 65, 'note')

ElementTree(mxfile).write(OUT, encoding='utf-8', xml_declaration=True)
print(f'Wrote {OUT}')
