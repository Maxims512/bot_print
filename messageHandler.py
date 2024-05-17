import datetime

from dateBase import realDb
import createKeyboard


def getAnswer(message, lastMessage, fullMessage):
    text = getStartText()
    keyboard = getStartKeyboard()
    user_id = fullMessage.getUserId()
    if message == "стирка":
        keyboard = getStartWashingKeyboard()
        text = "Выберите дальнейшее действие"


    if message.lower() == "записаться на стирку":
        if (realDb.getCountWashFromPerson(user_id) == 2):
            fullMessage.setAnswer("Вы уже записаны на 2 стирки")
            fullMessage.setKeyboard(getStartKeyboard())
            return
        if len(realDb.getFreeWashingDay()) > 0:
            keyboard = getWashingDayKeyboard()
            text = "Выберите день"
        else:
            keyboard = getStartKeyboard()
            text = "На ближайшую неделю все стиральные машинки заняты"


  
    if (lastMessage == "записаться на стирку" and message.split(" ")[0] in ["понедельник", "вторник", "среда", "четверг", "пятница"]):
        date = message.split(" ")[1]
        day = date.split("_")[0]
        text = "Выберите время"
        keyboard = getFreeWashingTimeKeyboard(day)

    if (lastMessage != None and lastMessage.split(" ")[0] in ["понедельник", "вторник", "среда", "четверг", "пятница"] and
        message in ["11 : 00", "12 : 00", "13 : 00", "14 : 00", "15 : 00"]):
        dat = lastMessage.split(" ")[1]
        day = dat.split("_")[0]
        month = dat.split("_")[1]
        year = dat.split("_")[2]
        hour = message.split(" ")[0]
        date = datetime.datetime(int(year), int(month), int(day), int(hour))

        if (int(hour) in realDb.getFreeWashingTime(day) and realDb.getCountWashFromPerson(user_id) < 2):
            realDb.addWashing(user_id, date)
            text = f"Вы записались на стирку {lastMessage}, в {hour} часов"
            keyboard = getStartKeyboard()
        else:
            text = "К сожалению это время занято"
            keyboard = getStartKeyboard()

    if message == "посмотреть расписание стирок":
        text = "Тут будет пдф файл с расписанием на неделею"


    if message == "отменить стирку":
        if (len(realDb.getWashingTimeFromUser(user_id)) > 0):
            text = "Выберите время которое вам не подходит"
            keyboard = getWashingsFromUserKeyboard(user_id)
        else:
            text = "У вас нет активных стирок"

    if (lastMessage == "отменить стирку" and message.split(" ")[1].split(":")[0] in ["11", "12", "13", "14", "15"]):
        text = f"Вы отменили стирку {message}"


    fullMessage.setAnswer(text)
    fullMessage.setKeyboard(keyboard)





def getWashingsFromUserKeyboard(user_id):
    title = []
    for i in realDb.getWashingTimeFromUser(user_id):
        title.append(str(i[0]))
    keyboard = createKeyboard.createKeyboard(1, len(title), title)
    return keyboard


def getWashingDayKeyboard():
    title = realDb.getFreeWashingDay()
    if len(title)>0:
        keyboard = createKeyboard.createKeyboard(1,len(title), title)
        return keyboard
    else:
        return getStartWashingKeyboard()



def getFreeWashingTimeKeyboard(day):
    title = []
    freeWash = realDb.getFreeWashingTime(day)
    if len(freeWash)>0:
        for i in freeWash:
            title.append(str(i)+" : 00")


        keyboard = createKeyboard.createKeyboard(1, len(title), title)
        return keyboard
    else:
        return getStartWashingKeyboard()

def getStartWashingKeyboard():
    title = ["Записаться на стирку", "Посмотреть расписание стирок", "Отменить стирку"]
    keyboard = createKeyboard.createKeyboard(1, 3, title)

    return keyboard


def getStartKeyboard():
    title = ["Стирка", "Товары", "Мероприятия"]
    keyboard = createKeyboard.createKeyboard(1,4, title)

    return keyboard


def getEmpty():
    title = []
    keyboard = createKeyboard.createKeyboard(0,0,title)
    return keyboard






def getStartText():
    return "Я вас не понимаю"