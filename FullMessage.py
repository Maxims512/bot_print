import messageHandlerKeyboard
import messageHandlerText
import db
class FullMessage:
    __userId = None
    __keyboard = None
    __answer = None
    __photo = None

    def setUserId(self, userId):
        self.__userId = userId
    def setAnswer(self, answer):
        self.__answer = answer
    def setKeyboard(self, keyboard):
        self.__keyboard = keyboard
    def setPhoto(self, photo):
        self.__photo = photo

    def getUserId(self):
        return self.__userId
    def getText(self):
        return self.__answer
    def getKeyboard(self):
        return self.__keyboard
    def getPhoto(self):
        return self.__photo



    def __init__(self, msgObject):
        photo = ""
        if (len(msgObject.message['attachments'])) > 0:
            photo = msgObject.message['attachments'][0]['photo']['sizes'][3]['url']

        if (photo != ""):
            self.setPhoto(photo)


        msg = msgObject.message
        userId = msg['from_id']
        chatId = msg['peer_id']


        userText = msg['text'].lower()
        lastMessage = userText

        self.setUserId(userId)
        self.setAnswer(messageHandlerText.answer(userText, lastMessage, self))
        self.setKeyboard(messageHandlerKeyboard.mainProcessor(userText))





