import vk_api, random, json
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import messageHandlerKeyboard, createKeyboard
from config import token
from config import admin_id
#from main import MyLongPoll

class MyLongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)


class VkBot:
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = MyLongPoll(self.vk_session, admin_id)


    def send_message(self, recipient, message, link, keyboard=None):


        self.vk_session.method('messages.send', {
            'user_id': recipient,
            'message': message,
            'random_id': 0,
            'keyboard': keyboard,
        })


    def run(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.object.message
                user_id = msg['from_id']
                chat_id = msg['peer_id']

                text = msg['text'].lower()

                keyboard = messageHandlerKeyboard.mainProcessor(text)
                print(user_id)

                print(keyboard)
                if ((user_id == 346029605 or user_id == 16889713) and keyboard == None):
                    VkBot.send_message(self, user_id, "Я вас не понимаю", "")


                if ((user_id == 346029605 or user_id == 16889713) and keyboard != None):
                    VkBot.send_message(self, user_id, text, "", keyboard)

