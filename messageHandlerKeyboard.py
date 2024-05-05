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
    if len(db.db.getFreeWashingTime(1)) > 0:
        days = ["ПН", "ВТ", "СР", "ЧТ", "ПТ"]
        freeWashingDay = []
        for k in range(1,6):
            for i in db.db.getFreeWashingTime(1):
                if (i[0] == str(k)):
                    freeWashingDay.append(days[k-1])
                    break
                # if (i[0] == "2"):
                #     freeWashingDay.append("ВТ")
                # if (i[0] == "3"):
                #     freeWashingDay.append("СР")
                # if (i[0] == "4"):
                #     freeWashingDay.append("ЧТ")
                # if (i[0] == "5"):
                #     freeWashingDay.append("ПТ")




        keyboard = createKeyboard.createKeyboard(1,len(db.db.getFreeWashingTime(1)), freeWashingDay)
        return keyboard
    else:
        return getEmpty()

print(checkWashingDay())