---
tags: [gstem, data, communicatie, drawio, componenten]
aangemaakt: 2026-10-06
status: historisch architectuuroverzicht; hardwaredetail verouderd
---

# Communicatie- en componentenschema

> [!warning] Hardwaredetail vervangen — 2026-10-09
> De systeemcommunicatie blijft bruikbare context, maar het tabblad **Draagprint en UART-detail** toont de vervallen carrier-PCB en socketmontage. Gebruik dat tabblad niet als actuele montage-instructie. De gebruiker verbindt en soldeert de modules nu zelf en monteert ze aan een 3D-geprinte behuizing. Zie [bedrading-en-behuizing](bedrading-en-behuizing.md).
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

De actuele componentkeuzes staan in [bestellijst](bestellijst.md) en [componenten](componenten.md): BNO085, BMP581, TXB0108-breakout, XIAO ESP32S3 + Wio-SX1262-kits en de nog te bevestigen LC29HDA-breakout. De oude afbeelding bevat ook sockets en een carrier-PCB; die zijn vervallen. De elektrische functies van voedingsbescherming, LDO, antennes, connectoren, LED en ontkoppeling worden opnieuw ingepast in de handbedrade uitvoering.

> [!warning] Nog te synchroniseren/valideren
> De draw.io-hardwareweergave is niet bijgewerkt naar de nieuwe montageaanpak. Werk de pinout en handbedrade aansluitingen uit voordat de tekening als actuele bedradingsreferentie wordt gebruikt. Controleer ook hoe de Arduino Uno van 5 V wordt voorzien zonder ongewenste terugvoeding via USB, en welke bron de aparte servobuck gebruikt.

Andere open punten in het schema zijn de exacte LoRa-pakketinstellingen en frequentie, de doorvoer van NTRIP/RTCM via laptop en LoRa naar de rover, API-transport, UART-baudrate, CSV-veldvolgorde en details van de failsafe. Het schema is conceptueel en niet op schaal; het is geen productierijp elektrisch schema.

## Gerelateerd

- [componenten](componenten.md) — componentenlijst / BOM
- [bestellijst](bestellijst.md) — actuele bestelvarianten
- [bedrading-en-behuizing](bedrading-en-behuizing.md) — actuele bedrade montage
- [pcb-schets](pcb-schets.md) — historische draagprintschets en eindbeeld
- [app-architectuur-besturing](app-architectuur-besturing.md) — softwarelagen, API en downlink
- [besturing-en-commandos](besturing-en-commandos.md) — commando's en voertuigkoppeling
- [open-vragen](open-vragen.md) — nog te bevestigen technische keuzes
- [specificaties](specificaties.md) — vastgelegde afspraken
