import realDb
import createKeyboard


def getAnswer(message, lastMessage, fullMessage):
    text = getStartText()
    keyboard = getStartKeyboard()
    if message.lower() == "стирка":
        freeWashingDay = realDb.getFreeWashingDay()




    fullMessage.setAnswer(text)
    fullMessage.setKeyboard(keyboard)




def getWashingDayKeyboard():
    todayDayWeek = realDb.getDow()
    freeWashingDay = realDb.getFreeWashingDay()
    title = []
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]





def getStartKeyboard():
    title = ["Стирка", "Товары", "Мероприятия"]
    keyboard = createKeyboard.createKeyboard(1,3, title)

    return keyboard


def getEmpty():
    title = []
    keyboard = createKeyboard.createKeyboard(0,0,title)
    return keyboard






def getStartText():
    return "Я вас не понял"