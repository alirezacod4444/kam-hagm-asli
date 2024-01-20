#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "𝐇𝐞𝐥𝐥𝐨, \n\n𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 <b>𝐕𝐢𝐝𝐞𝐨 𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐨𝐫 𝐁𝐨𝐭 </b>. \n\n<b>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐛𝐢𝐠 𝐯𝐢𝐝𝐞𝐨 𝐟𝐢𝐥𝐞 𝐈 𝐰𝐢𝐥𝐥 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬 𝐢𝐭 𝐚𝐬 𝐬 𝐬𝐦𝐚𝐥𝐥 𝐯𝐢𝐝𝐞𝐨 𝐟𝐢𝐥𝐞!</b> \n\n𝐅𝐨𝐫 𝐛𝐮𝐲𝐢𝐧𝐠 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 👇🏼 \n\n♦️𝐎𝐰𝐧𝐞𝐫 : @iNsanePlay"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "⚡ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...\n"
    
    UPLOAD_START = "⚡ ᴜᴘʟᴏᴀᴅɪɴɢ ...\n"
    
    COMPRESS_START = "⚡ 𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐢𝐧𝐠 •••"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = ""

    COMPRESS_PROGRESS = "⏳ ETA: {} ⚙️ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\n@iNsanePlay"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
