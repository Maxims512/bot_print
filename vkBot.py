import vk_api, random
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import FullMessage
import messageHandlerKeyboard
import FullMessage
from config import token
from config import admin_id


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


    def send_message(self, userId, message, keyboard=None, attachment = None):
        self.vk_session.method('messages.send', {
            'user_id': userId,
            'message': message,
            'random_id': random.random(),
            'keyboard': keyboard,
            'attachment':attachment
        })

    def run(self):
        for event in self.longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                answer = FullMessage.FullMessage(event.object)

                if ((event.object.message['from_id'] == 346029605 or event.object.message['from_id'] == 16889713)):
                    VkBot.send_message(self, answer.getUserId(), answer.getText(), answer.getKeyboard(), answer.getPhoto())


