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
    SESSION = os.environ.get("SESSION", "BQGYqWYAAq79U-wXJkQMdXXk6vO7XcJoQ5nQZMDjlExhKNhs87a7PyZqal_HWdY9nnrK0ovQyVLRUdHV8lUPKY1xvf_Q1BIpqPJ9M_INhUTK7BTNlEd7i_UB_VcsvZpoh_mpSQTuQDbkuQfn5KnMAqEV5u5isCqyg03gk2PgULwIdkhmGZA6YX4WNtPMlkzehl3Gz2fCYboik4Fre6TVRCycFCNRJak6M9iowuvd-pZU93WwwaaQqkvFGfHY0gq241JLle2apQSpoZAcRTkvV8tjXWYB8cuZT-S2XdYlA-mfJ_uEMTTFFShjVicVDONN_3OrbT7mJ9IlaIanzltho_UFe1sV0wAAAABKf7lXAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001927033569"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
