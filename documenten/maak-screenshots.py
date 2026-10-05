# -*- coding: utf-8 -*-
"""
Maakt schermafbeeldingen van de webdemo in GSTEMAPPPREVIEWWEB.

Gebruik:  python documenten/maak-screenshots.py
Resultaat: documenten/afbeeldingen/*.png

De demo wordt via een lokale http-server geserveerd zodat de kaart en
de scripts laden. Er wordt gebruik gemaakt van de Chrome die op de pc staat.
"""

import os
import subprocess
import sys
import time

from playwright.sync_api import sync_playwright

HIER = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HIER)
WEB = os.path.join(PROJECT, "GSTEMAPPPREVIEWWEB")
UIT = os.path.join(HIER, "afbeeldingen")
POORT = 8765
BASIS = f"http://127.0.0.1:{POORT}/index.html"

os.makedirs(UIT, exist_ok=True)


def start_server():
    return subprocess.Popen(
        [sys.executable, "-m", "http.server", str(POORT), "--directory", WEB],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def shot(page, naam, volledige_pagina=False, element=None):
    pad = os.path.join(UIT, naam)
    if element is not None:
        element.screenshot(path=pad)
    else:
        page.screenshot(path=pad, full_page=volledige_pagina)
    print("geschreven:", pad)


def main():
    server = start_server()
    time.sleep(1.0)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            page = browser.new_page(
                viewport={"width": 1600, "height": 1000},
                device_scale_factor=2,
            )

            # 1. Eerste scherm (setup-popup), wacht tot beide vakjes aan staan
            page.goto(BASIS, wait_until="load")
            page.wait_for_timeout(5000)
            shot(page, "01-setup-scherm.png")

            # Popup sluiten via OK
            page.click("#ok-btn")
            page.wait_for_timeout(500)

            # 2. Kaartscherm + live data
            page.evaluate("window.location.hash = '#page-kaart'")
            page.wait_for_timeout(7000)  # kaarttegels laden
            shot(page, "02-kaartscherm.png")

            # 3. Rechterpaneel met meetwaarden
            shot(page, "03-meetwaarden.png", element=page.query_selector("aside.right-section"))

            # 4. Codescherm
            page.click("a.island-btn[href='#page-code']")
            page.wait_for_timeout(1500)
            shot(page, "04-codescherm.png")

            # 5. Variabelenpaneel (ingangen/uitgangen)
            shot(page, "05-variabelen.png", element=page.query_selector("aside.code-side"))

            # 6. API-simulatie actief
            page.click(".var-group:has(.var-badge:has-text('API')) .var-item")
            page.wait_for_timeout(500)
            shot(page, "06-api.png", element=page.query_selector("aside.code-side"))

            # 7. Upload-knop met hint
            shot(page, "07-uploaden.png", element=page.query_selector(".upload-info"))

            browser.close()
    finally:
        server.terminate()


if __name__ == "__main__":
    main()
