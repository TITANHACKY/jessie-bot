from bot import telegram_bot
import gizoogle


update_id = None
while True:
    print("...")
    updates = telegram_bot().get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for msgs in updates:
            usr_id = msgs["message"]["chat"]["id"]
            try:
                usr_username = msgs["message"]["from"]["username"]
            except:
                usr_username = "User Name was Not Set."
            try:
                usr_fname = msgs["message"]["from"]["first_name"]
            except:
                usr_fname = ""
            try:
                usr_lname = msgs["message"]["from"]["last_name"]
            except:
                usr_lname = ""
            update_id = msgs["update_id"]
            try:
                message = msgs["message"]["text"]
                if(message=="/start"):
                    message = f"👋ʜᴇʏ @{usr_username}\n\n✦ɪ'ᴀᴍ ᴍɪss ᴊᴇssɪᴇ. ɪ ᴡᴀs ᴀ ᴘʏᴛʜᴏɴ ʙᴏᴛ ᴜsᴇᴅ ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ ᴜsᴇʀɴᴀᴍᴇ ғғɪʀsᴛɴᴀᴍᴇ ʟᴀsᴛɴᴀᴍᴇ ᴀɴᴅ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ʟɪɴᴋ\n\n✦ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡᴀs sᴛɪʟʟ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍᴇ sᴏ ᴛʜᴀᴛ ɪ'ʟʟ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘ's\n\n✦ʜɪᴛ /help ᴛᴏ ʟᴏᴀᴅ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs."
                elif(message=="/help"):
                    message = "ʜɪ I'ᴍ ᴀ sɪᴍᴘʟᴇ ᴘʏᴛʜᴏɴ ʙᴏᴛ ᴡɪᴛʜ ғᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:\n\n/id - ●ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ɪᴅ\n\n/uname - ●ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍʀ\n\n/name - ●ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ɴᴀᴍᴇ\n\n/fname - ●ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ғғɪʀsᴛɴᴀᴍᴇ\n\n/lname - ●ᴛᴏ ғɪɴᴅ ʏᴏᴜʀ ʟᴀsᴛɴᴀᴍᴇ\n\n/link - ●ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ʟɪɴᴋ\n\n/creator - ●ᴛᴏ ғɪɴᴅ ᴍʏ ᴄʀᴇᴀᴛᴏʀ"
                elif(message=="/id"):
                    message = f"🔹ɪᴅ: {usr_id}"
                elif(message=="/name"):
                    message = f"🔹ɴᴀᴍᴇ: {usr_fname} {usr_lname}"
                elif(message=="/uname"):
                    message = f"🔹ᴜsᴇʀɴᴀᴍᴇ: @{usr_username}"
                elif(message=="/fname"):
                    message = f"🔹ғɪʀsᴛɴᴀᴍᴇ: {usr_fname}"
                elif(message=="/lname"):
                    message = f"🔹ʟᴀsᴛ ɴᴀᴍᴇ:  {usr_lname}"
                elif(message=="/link"):
                    message = f"🔗https://t.me/{usr_username}"
                elif(message=="/creator"):
                    message = f"○Lᴀɴɢᴜᴀɢᴇ ᴜsᴇᴅ: ᴘʏᴛʜᴏɴ\n\n○ᴍʏ ᴍᴀsᴛᴇʀ: ᴘᴏᴏɴᴋᴀᴡɪɴ(@TITANHACKY)\n\n★sʜᴀʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ★"
                else:
                    message = gizoogle().text(message)
            except:
                message = gizoogle.text(message)

            to = msgs["message"]["chat"]["id"]
            reply = message
            telegram_bot().send_messages(reply, to)
