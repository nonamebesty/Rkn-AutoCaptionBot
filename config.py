# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "0") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "autocaption")     
    DB_URL = os.environ.get("DB_URL", "")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b>{file_name}\n\nMain Movie Searching Group Join @Moviekoodu1\n\nOther Zee Tamil serials Join \nhttps://t.me/+VdExpPLNSLVlMTdl</b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgUAAxkBAAEE_7BnTLgJ5tXpO8uIQS2tqAhSkiIfXwAC_QADdKohVZYbzDX-1NJ_HgQ")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '880087645').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
