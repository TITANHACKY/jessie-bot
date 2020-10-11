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
                usr_link = f"https://t.me/{usr_username}"
            except:
                usr_username = ""
                usr_link = ""
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
                if(message=="/start" or message=="/start@MissJessie_Bot"):
                    message = f"👋ʜᴇʏ @{usr_username}\n\n✦ɪ'ᴀᴍ ᴍɪss ᴊᴇssɪᴇ. ɪ ᴡᴀs ᴀ ᴘʏᴛʜᴏɴ ʙᴏᴛ ᴜsᴇᴅ ᴛᴏ ғɪɴᴅ  ᴜsᴇʀ ɪᴅ ᴜsᴇʀɴᴀᴍᴇ ғɪʀsᴛɴᴀᴍᴇ ʟᴀsᴛɴᴀᴍᴇ ᴀɴᴅ  ᴘʀᴏғɪʟᴇ ʟɪɴᴋ\n\n✦ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴀᴏ ᴛʜᴀᴛ ɪ ᴄᴀɴ ғɪɴᴅ ᴛʜᴇ ᴜsᴇʀ ᴅᴇᴛᴀɪʟs ʙʏ ᴊᴜsᴛ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴍᴇssᴀɢᴇ\n\n✦ɪʟʟ ᴡᴇʟᴄᴏᴍᴇ ɴᴇᴡ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘ\n\n✦ʜɪᴛ /help ᴛᴏ ʟᴏᴀᴅ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs."
                elif(message=="/help" or message=="/help@MissJessie_Bot"):
                    message = "ʜɪ I'ᴍ ᴀ sɪᴍᴘʟᴇ ᴘʏᴛʜᴏɴ ʙᴏᴛ ᴡɪᴛʜ ғᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:\n\n/info - ●ᴛᴏ ɢᴇᴛ ᴅᴇᴛᴀɪʟs\n\n/id - ●ᴛᴏ ғɪɴᴅ ɪᴅ\n\n/uname - ●ᴛᴏ ғɪɴᴅ ᴜsᴇʀɴᴀᴍʀ\n\n/name - ●ᴛᴏ ғɪɴᴅ ɴᴀᴍᴇ\n\n/fname - ●ᴛᴏ ғɪɴᴅ ғғɪʀsᴛɴᴀᴍᴇ\n\n/lname - ●ᴛᴏ ғɪɴᴅ ʟᴀsᴛɴᴀᴍᴇ\n\n/link - ●ᴛᴏ ɢᴇᴛ ᴘʀᴏғɪʟᴇ ʟɪɴᴋ\n\n/creator - ●ᴛᴏ ғɪɴᴅ ᴍʏ ᴄʀᴇᴀᴛᴏʀ"
                elif(message=="/id" or message=="/id@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        message = f"🔹ɪᴅ: {usr_id}"
                    except:
                        message = f"🔹ɪᴅ: {usr_id}"
                elif(message=="/name"or message=="/name@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_fname = msgs["message"]["reply_to_message"]["from"]["first_name"]
                        except:
                            usr_fname = ""
                        try:
                            usr_lname = msgs["message"]["reply_to_message"]["from"]["last_name"]
                        except:
                            usr_lname = ""
                        message = f"🔹ɴᴀᴍᴇ: {usr_fname} {usr_lname}"
                    except:
                        message = f"🔹ɴᴀᴍᴇ: {usr_fname} {usr_lname}"
                elif(message =="/info"or message=="/info@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_fname = msgs["message"]["reply_to_message"]["from"]["first_name"]
                        except:
                            usr_fname = ""
                        try:
                            usr_lname = msgs["message"]["reply_to_message"]["from"]["last_name"]
                        except:
                            usr_lname = ""
                        try:
                            usr_username = msgs["message"]["reply_to_message"]["from"]["username"]
                            usr_link = f"https://t.me/{usr_username}"
                        except:
                            usr_username = ""
                            usr_link = ""
                        message = f"☆ɪᴅ: {usr_id}\n\n☆ᴜsᴇʀɴᴀᴍᴇ: @{usr_username}\n\n☆ɴᴀᴍᴇ: {usr_fname}{usr_lname}\n\n☆ʟɪɴᴋ: {usr_link}"
                    except:
                        message = f"☆ɪᴅ: {usr_id}\n\n☆ᴜsᴇʀɴᴀᴍᴇ: @{usr_username}\n\n☆ɴᴀᴍᴇ: {usr_fname}{usr_lname}\n\n☆ʟɪɴᴋ: {usr_link}"
                elif(message=="/uname"or message=="/uname@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_username = msgs["message"]["reply_to_message"]["from"]["username"]
                            usr_link = f"https://t.me/{usr_username}"
                        except:
                            usr_username = ""
                            usr_link = ""
                        message = f"🔹ᴜsᴇʀɴᴀᴍᴇ: @{usr_username}"
                    except:
                        message = f"🔹ᴜsᴇʀɴᴀᴍᴇ: @{usr_username}"
                elif(message=="/fname"or message=="/fname@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_fname = msgs["message"]["reply_to_message"]["from"]["first_name"]
                        except:
                            usr_fname = ""
                        message = f"🔹ғɪʀsᴛɴᴀᴍᴇ: {usr_fname}"
                    except:
                        message = f"🔹ғɪʀsᴛɴᴀᴍᴇ: {usr_fname}"
                elif(message=="/lname"or message=="/lname@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_lname = msgs["message"]["reply_to_message"]["from"]["last_name"]
                        except:
                            usr_lname = ""
                        message = f"🔹ʟᴀsᴛ ɴᴀᴍᴇ:  {usr_lname}"
                    except:
                        message = f"🔹ʟᴀsᴛ ɴᴀᴍᴇ:  {usr_lname}"
                elif(message=="/link"or message=="/link@MissJessie_Bot"):
                    try:
                        usr_id = msgs["message"]["reply_to_message"]["from"]["id"]
                        try:
                            usr_username = msgs["message"]["reply_to_message"]["from"]["username"]
                            usr_link = f"https://t.me/{usr_username}"
                        except:
                            usr_username = ""
                            usr_link = ""
                        message = f"🔗ʟɪɴᴋ:\n\n{usr_link}"
                    except:
                        message = f"🔗ʟɪɴᴋ:\n\n{usr_link}"
                elif(message=="/creator"):
                    message = f"○Lᴀɴɢᴜᴀɢᴇ ᴜsᴇᴅ: ᴘʏᴛʜᴏɴ\n\n○ᴍʏ ᴍᴀsᴛᴇʀ: ᴘᴏᴏɴᴋᴀᴡɪɴ(@TITANHACKY)\n\n○ɢɪᴛʜᴜʙ ʟɪɴᴋ: https://github.com/TITANHACKY/jessie-bot\n\n○Iғ ʏᴏᴜ ᴄᴏᴘʏ ᴛʜᴇ ᴄᴏᴅᴇ ᴀᴛʟᴇᴀsᴛ ᴍᴇɴᴛɪᴏɴ ᴍʏ ɴᴀᴍᴇ ᴀɴʏᴡʜᴇʀᴇ ᴄᴏᴢ ɪ ʜᴀᴅ sᴛʀᴜɢɢʟᴇᴅ ᴀ ʟᴏᴛ ᴀɴᴅ ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ sᴘᴏɪʟ ɪᴛ.\n\n★sʜᴀʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ★"
                


                else:
                    message = ""

            except:
                try:
                    left_chat_member_fname = msgs["message"]["left_chat_member"]["first_name"]
                    message = f"ʙʏᴇ ʙʏᴇ {left_chat_member_fname}"
                except:
                    try:
                        new_chat_member_fname = msgs["message"]["new_chat_member"]["first_name"]
                        group = msgs["message"]["chat"]["title"]
                        message = f"ʜᴇʏ {new_chat_member_fname} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {group}"
                    except:
                        message = ""

                
            to = msgs["message"]["chat"]["id"]
            reply = message
            f=open("user_id.txt","a")
            f.write(str(usr_id)+"\n")
            f.close()
            telegram_bot().send_messages(reply, to)
            #support @TITANHACKY
