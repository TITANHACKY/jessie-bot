import requests
import json
import configparser as cfg

class telegram_bot():
    def __init__(self):
        self.token = #mention your bot token here
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


