#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6039043446:AAHf8ODju2FpNFBXj7v2-MwC0HxpLAu_0wU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@sai_movies_update")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQGxRSAACtT62Vgw4WrpSTTksGRAeN5SNJz6k8gtsti5lgMfACzQ84_2jRozB95aBKyAoTOMgfCUuQCKSz-frS4AJB24M1ADfPUGpimbY7fcNzweu8kE4lTGIegVq5i-meTAPO02x7eeCEH0fOlX3VYH8yjv0OXc6i1UzCiLzGqnajTdpamMTiOt4Goel84FYrArsE1J0rbE7FXMVhJLLS0jM_mLKHCfxPPqJ8nUeuDYLTc_A9YKS6lLDHiMRHW9mh3m2DlN_0TwtqoYogZ0wynqimdt90pmBxgXDIvl8fU8YzZrplTEL59v_od7N1-Sz2yxK1kQqxERfRA9gtAwegweXlOwrgAAAABF5vF9AA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001795790118"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
