import createKeyboard
import db

def mainProcessor(message):
    keyboard = start()
    if (message == "начать"):
        keyboard = start()

    if (message == "записаться на стирку"):
        keyboard = checkWashingDay()

    if (message == "выставить товар"):
        keyboard = None

    return keyboard

def start():
    title = ["Записаться на стирку", "Отдать стирку", "Посмотреть товары", "Выставить товар", "Мероприятия"]
    keyboard = createKeyboard.createKeyboard(5,1, title)

    return keyboard

def laundryAppointment():
    if len(db.db.getFreeWashingTime())>0:
        return checkWashingDay()
    else:
        title = ["ЗАНЯТО", "ЗАНЯТО", "ЗАНЯТО", "ЗАНЯТО"]
        keyboard = createKeyboard.createKeyboard(2, 2, title)
    return keyboard

def getEmpty():
    title = []
    keyboard = createKeyboard.createKeyboard(0,0,title)
    return keyboard

def checkWashingDay():
    dab = db.db()
    if len(dab.getFreeWashingDay()) > 0:
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
        freeWashingDay = []
        for k in range(1,6):
            for i in dab.getFreeWashingDay():
                if (i == k):
                    freeWashingDay.append(days[k-1])
                    break


        keyboard = createKeyboard.createKeyboard(len(dab.getFreeWashingDay()), 1, freeWashingDay)
        return keyboard
    else:
        return getEmpty()


