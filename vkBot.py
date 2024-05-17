import vk_api, random
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import FullMessage
from dateBase import realDb
from configs.VKconfig import token
from configs.VKconfig import admin_id


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
        realDb.initDb()
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = MyLongPoll(self.vk_session, admin_id)


    def send_message(self, userId, message, keyboard=None, attachment = None):
        self.vk_session.method('messages.send', {
            'user_id' : userId,
            'message': message,
            'random_id': random.random(),
            'keyboard': keyboard,
            'attachment': attachment
        })

    def run(self):
        for event in self.longpoll.listen():


            if (event.type == VkBotEventType.MESSAGE_NEW and event.object.message['peer_id'] == 2000000001):
                user_id = event.object.message['from_id']
                name = (self.vk_session.method('users.get', {'user_id': user_id})[0]['first_name'] +
                        "_"+self.vk_session.method('users.get', {'user_id': user_id})[0]['last_name'])
                print(name)
                realDb.addPerson(user_id, name)


            if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['id'] != 0:



                answer = FullMessage.FullMessage(event.object)
                VkBot.send_message(self, answer.getUserId(), answer.getText(), answer.getKeyboard(), answer.getPhoto())
                ######################
                user_id = event.object.message['from_id']
                name = (self.vk_session.method('users.get', {'user_id': user_id})[0]['first_name'] +
                        "_" + self.vk_session.method('users.get', {'user_id': user_id})[0]['last_name'])
                print(name)
                realDb.addPerson(user_id, name)
