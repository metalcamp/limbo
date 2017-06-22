# coding: UTF-8
import re
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote

import requests


def malica(searchterm):
    if searchterm == "spar":
        return "https://www.spar.si/aspiag_spar_si/sl_SI/aktualno/restavracija-interspar/tedenski-meni.html"

    elif searchterm == "sicilia":
        url = "https://www.malcajt.com/podravska/maribor/taverna-sicilia.html"
        return url

    elif searchterm == "toscana":
        url = "https://www.malcajt.com/podravska/maribor/toscana-maribor.html"
        return url


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!malica (.*)", text)
    if not match:
        return "Na voljo so jedilniki za sledeče restavracije: Sicilia, Spar, Toscana"

    searchterm = match[0]
    return malica(searchterm.encode("utf8").lower())

on_bot_message = on_message
