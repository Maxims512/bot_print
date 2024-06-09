import requests
import vk_api, random, json
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from messageHandlers import FullMessage
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
        self.vk = self.vk_session.get_api()


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

                realDb.addPerson(user_id, name)


            if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['id'] != 0:

                user_id = event.object.message['from_id']
                name = (self.vk_session.method('users.get', {'user_id': user_id})[0]['first_name'] +
                        "_" + self.vk_session.method('users.get', {'user_id': user_id})[0]['last_name'])

                realDb.addPerson(user_id, name)
                answer = FullMessage.FullMessage(event.object)


                VkBot.send_message(self, answer.getUserId(), answer.getText(), answer.getKeyboard(), answer.getPhoto())
                ######################

                obj = event.object.message
                peer = obj['peer_id']



                if (event.type == VkBotEventType.MESSAGE_NEW and event.object.message['id'] != 0 and
                        event.object.message['text'].lower() == "посмотреть расписание стирок" and realDb.verifyPerson(peer)):

                    obj = event.object.message
                    peer = obj['peer_id']
                    result = json.loads(requests.post(self.vk.docs.getMessagesUploadServer(type='doc', peer_id=peer)['upload_url'],
                                                      files={'file': open('createPDF/washings.pdf', 'rb')}).text)
                    jsonAnswer = self.vk.docs.save(file=result['file'], title='Расписание стирок', tags=[])

                    self.vk.messages.send(
                        peer_id=peer,
                        random_id=0,
                        attachment=f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}"
                    )


