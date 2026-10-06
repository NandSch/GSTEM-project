---
tags: [gstem, data, communicatie, drawio, componenten]
aangemaakt: 2026-10-06
status: architectuuroverzicht
---

# Communicatie- en componentenschema

> [!info] Bestand
> Draw.io: `documenten/pcb/Communicatie-overzicht-GSTEM.drawio`  
> Herbouwbaar met `python documenten/scripts/build-communicatie-overzicht.py`.

Het schema bevat twee tabbladen:

1. **Systeemcommunicatie** — laptopapp, extern programma/API, NTRIP-correctiedienst, USB-LoRa-ontvanger, meettoestel, Arduino Uno en de servo-aangestuurde stilstaande vliegtuigmock-up.
2. **Draagprint en UART-detail** — voedingsboom, sensoraansluitingen, level shifter, uitbreidingsconnector, Arduino en servovoeding.

## Getoonde communicatie

- **IMU en barometer → ESP32-S3:** I²C (SDA/SCL, 3,3 V-logica).
- **RTK-GNSS ↔ ESP32-S3:** UART; meetgegevens naar de controller en RTCM-correcties in de richting van de rover.
- **Meetcontroller ↔ USB-ontvanger:** LoRa; telemetrie naar de laptop en commando's terug naar het toestel.
- **USB-ontvanger ↔ laptop:** USB-serieel, bidirectioneel.
- **Laptopapp ↔ extern programma:** meetdata als JSON; vrije CSV-commando-regel terug. De lokale API-techniek blijft open.
- **ESP32-S3 ↔ Arduino Uno:** UART TX/RX via een level shifter en vieraderige connector; de ESP stuurt CSV-commando's, de Uno bestuurt servosignalen.
- **Arduino Uno → servos:** PWM-/servosignalen; de servo's hebben een aparte buck-converter.

## Componentuitgangspunten

Het schema volgt de recentste **bestellijst** waar die afwijkt van oudere notities: BNO085, BMP581 en TXB0108-module. De bestellijst noemt de Waveshare LC29H(DA)-HAT, twee XIAO ESP32S3 + Wio-SX1262-kits, Arduino Uno, 2S LiPo, buck-converters, AP2112K-3.3, 2 A PTC, TVS SMBJ10A, antennes, sockets, connector, LED/weerstand en ontkoppelcondensatoren.

> [!warning] Nog te synchroniseren/valideren
> Oudere onderdelennotities vermelden BNO055/BMP390 en een TXB0104-IC in plaats van BNO085/BMP581 en de TXB0108-module uit de recentere bestellijst. Bevestig de definitieve uitvoeringen en pinouts vóór de KiCad-layout. Controleer ook hoe de Arduino Uno van 5 V wordt voorzien zonder ongewenste terugvoeding via USB, en welke bron de aparte servobuck gebruikt.

Andere open punten in het schema zijn de exacte LoRa-pakketinstellingen en frequentie, de doorvoer van NTRIP/RTCM via laptop en LoRa naar de rover, API-transport, UART-baudrate, CSV-veldvolgorde en details van de failsafe. Het schema is conceptueel en niet op schaal; het is geen productierijp elektrisch schema.

## Gerelateerd

- [[componenten]] — componentenlijst / BOM
- [[bestellijst]] — actuele bestelvarianten
- [[pcb-schets]] — draagprintschets en eindbeeld
- [[app-architectuur-besturing]] — softwarelagen, API en downlink
- [[besturing-en-commandos]] — commando's en voertuigkoppeling
- [[open-vragen]] — nog te bevestigen technische keuzes
- [[specificaties]] — vastgelegde afspraken
