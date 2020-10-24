import requests
import json
import configparser as cfg

class telegram_bot():
    def __init__(self):
        self.token = "" #Bot Tokent Here
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    #update function to get update from the bot
    def get_updates(self, offset=None):
        url = self.base_url+"/getUpdates?timeout=100"
        if offset:
            url = url+f"&offset={offset+1}"
        r=requests.get(url)
        return json.loads(r.content)

    #send message function to send message to user
    def send_messages(self, msg, chat_id):
        url = self.base_url+f"/sendMessage?chat_id={chat_id}&text={msg}"
        requests.get(url)
    
    #pin message
    def pin_message(self, chat_id, msg_id):
        pinmessage_url = self.base_url+f"/pinChatMessage?chat_id={chat_id}&message_id={msg_id}"
        requests.get(pinmessage_url)

    #unpin message
    def unpin_message(self, chat_id):
        unpinmessage_url = self.base_url+f"/unpinChatMessage?chat_id={chat_id}"
        requests.get(unpinmessage_url)

    #adminlist
    def admin_list(self, chat_id):
        adminlist_url = self.base_url+f"/getChatAdministrators?chat_id={chat_id}"
        r = requests.get(adminlist_url)
        return json.loads(r.content)


        


