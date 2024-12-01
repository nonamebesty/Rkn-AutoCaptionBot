# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "1923471")
    API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/a5545df4f5ce6ffaeaf98.jpg")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "0") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "autocaption")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://leecher:leecher@cluster0.606mkpi.mongodb.net/?retryWrites=true&w=majority")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b>{file_name}\n\n⚡️𝐉𝐎𝐈𝐍 𝐁𝐀𝐂𝐊𝐔𝐏 - @Techshyam007\n\n⚡️𝐉𝐎𝐈𝐍 𝐓𝐞𝐜𝐡𝐬𝐡𝐲𝐚𝐦 - @techshyaam</b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAKjYmZkRgOAtKRZ1d8LHnLAKUtus9noAAIjAAMoD2oUJ1El54wgpAY1BA")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '880087645').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
