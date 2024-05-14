import realDb
import createKeyboard


def getAnswer(message, lastMessage, fullMessage):
    print(message)
    text = getStartText()
    keyboard = getStartKeyboard()
    if message.lower() == "записаться на стирку":

        if (realDb.getCountWashFromPerson(fullMessage.getUserId()) == 2):
            fullMessage.setAnswer("Вы уже записаны на 2 стирки")
            fullMessage.setKeyboard(getStartKeyboard())
        if len(realDb.getFreeWashingDay()) > 0:
            keyboard = getWashingDayKeyboard()
            text = "Выберите день"
        else:
            keyboard = getStartKeyboard()
            text = "На ближайшую неделю все стиральные машинки заняты"


    if (lastMessage == "Записаться на стирку" and message in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]):
        text = "Выберите время"



    fullMessage.setAnswer(text)
    fullMessage.setKeyboard(keyboard)




def getWashingDayKeyboard():
    title = realDb.getFreeWashingDay()
    keyboard = createKeyboard.createKeyboard(1,len(title), title)
    return keyboard





def getStartKeyboard():
    title = ["Записаться на стирку","Посмотреть расписание стирок", "Товары", "Мероприятия"]
    keyboard = createKeyboard.createKeyboard(1,4, title)

    return keyboard


def getEmpty():
    title = []
    keyboard = createKeyboard.createKeyboard(0,0,title)
    return keyboard






def getStartText():
    return "Я вас не понимаю"