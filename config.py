#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047745215:AAEPhzBcwCliwNV9wxoMSWo93WSvBQByQlc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@sai_movies_update")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQGxRSAAeWqibGHhOO0vjkM5dNc6NAabU7gaPxZDFUs0x1Qa39N4mdHfKG5QCPfo7zLH_M-xxZaJxLCO26_KD4ALRTvt_klxrVBeg_BsjSUxN9DituLxeoQY2Se0AnT4-bpLZu_4YbHQsT7NMoHWQm9krYPLTmXXVwTFaB36tnFnRhbPnuzmrcLBTyGvym8KDU6zCKsSvd1yqEDEGD0dW__IcJ2KXprotyZDmFHpOs-Ag8XlnryaIZONh5PTOJUtAD_XXKv_yTXTnl0QRsJyx2F0Gy4B4DStae83FoGEcKh7UVL4KUmzpnuve9x3yqeLhMuCFzNPUfIyyVxaL76Ex1BB8CPnCwAAAABF5vF9AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001927033569"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
