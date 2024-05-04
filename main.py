import vk_api, random, event
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from config import token
from config import admin_id
from event import Event

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



    def run(self):
        kolvo_obr=0
        online = True
        kap=False
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.object.message
                user_id = msg['from_id']
                chat_id = msg['peer_id']
                text = msg['text'].lower()

                print(text)
                print(user_id)

                mass=["обыкновенная","умная","маленькая","азартная","застенчивая","безумная","великая","горькая","грубая","добрая","жестокая", "идеальная","грустная","максимовская","отчисленная","деловая","бебровая","капибаровая", "саратовская",
                "ленивая", "прекрасная", "хайповая", "огромная", "загадочная"
                ]

                kapibara=["photo-206143282_457243339", "photo-206143282_457243708", "photo-206143282_457243628",
"photo-217365453_457239055", "photo-217365453_457239036", "photo-217365453_457239027", "photo-217285205_457239111", "photo-217285205_457239106", "photo-206143282_457243098", "photo-206143282_457241853", "photo-206143282_457242000", "photo-217285205_457239130", "photo-217285205_457239128", "photo-217285205_457239129", "photo-217285205_457239137", "photo-217285205_457239124", "photo-217285205_457239118","photo-217285205_457239112", "photo-217285205_457239102"]

                if (text.find("капибары прибежали") > -1):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    self.vk_session.method('messages.send', {
                        'user_id' : user_id,
                         'message' : f'@id{user_id}' + "(" +user_name+ ")" + " , капибары включены",
                         'random_id' : 0
                    })
                    kap=True


                if (text.find("капибары убежали") > -1 and (user_id==346029605 or user_id==285666872)):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    self.vk_session.method('messages.send', {
                        'user_id' : user_id,
                         'message' : f'@id{user_id}' + "(" +user_name+ ")" + " , капибары выключены",
                         'random_id' : 0
                    })
                    kap=False










                if ((text.find("печат") > -1 or text.find("копию") > -1) and online and text != "распечатаю" and text != "печатаю" and text.find("бумаг")>-1 and text.find("цвет")<=0):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    if (user_id!=346029605):
                        kolvo_obr+=1
                        print(user_id, admin_id)
                    self.vk_session.method('messages.send', {
                            'chat_id' : chat_id-2000000000,
                             'message' : f'@id{user_id}' + "(" +user_name+ ")" + " 312 комната, 3р лист(ч/б)" + "\n" + "Обращаться к @id346029605(Максим)",
                             'random_id' : 0
                        })


                if (text.find("капибарный сбор") > -1 and online and kap):
                    for i in range(1,len(kapibara)-1):
                        user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                        self.vk_session.method('messages.send', {
                            'chat_id' : chat_id-2000000000,
                             'message' : " ", 'attachment': kapibara[i-1],
                             'random_id' : 0
                        })



                if (text=="кто я" and kap):
                    chislo=random.randint(0, len(kapibara)-1)
                    print(chislo)
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    self.vk_session.method('messages.send', {
                        'chat_id' : chat_id-2000000000,
                         'message' : f'@id{user_id}' + "(" +user_name+ ")" + ", вы " + mass[random.randint(0, len(mass)-1)] + " капибарка", 'attachment': kapibara[chislo],
                         'random_id' : 0
                    })



                if ((text.find("печат") > -1 or text.find("копию") > -1 or text.find("ксерокоп") > -1) and online and text != "распечатаю" and text != "печатаю" and text.find("бумаг")==-1 and text.find("цвет")==-1):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    if (user_id!=346029605):
                        kolvo_obr+=1
                        print(user_id, admin_id)
                    self.vk_session.method('messages.send', {
                            'chat_id' : chat_id-2000000000,
                             'message' : f'@id{user_id}' + "(" +user_name+ ")" + ", 312 комната, 4р лист(ч/б)" + "\n" + "Пишите @id346029605(Максиму)",
                             'random_id' : 0
                        })

                if (text.find("включить") > -1 and (user_id==346029605) and online == False):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    online=True
                    self.vk_session.method('messages.send', {
                            'chat_id' : chat_id-2000000000,
                             'message' : ' бот включен, 4р лист, 312 комната',
                             'random_id' : 0
                        })



                if (text.find("выключить") > -1 and (user_id==346029605) and online):
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    online=False
                    self.vk_session.method('messages.send', {
                            'chat_id' : chat_id-2000000000,
                             'message' :  ' бот выключен'+"\n"+"Количество обращений: "+str(kolvo_obr),
                             'random_id' : 0

                        })





                if (user_id==284531728):
                    chislo2=random.randint(0, 10)
                    user_name = self.vk_session.method('users.get', {'user_id' : user_id})[0]['first_name']
                    self.vk_session.method('messages.send', {
                        'chat_id' : chat_id-2000000000,
                         'message' : f'@id{user_id}' + "(" +user_name+ ")" + " ПОЧУВСТВУЙ",
                         'attachment': "audio474499256_456829705_0bdf6d1e3aa670db54",

                         'random_id' : 0
                    })




if __name__ == '__main__':

    VkBot().run()