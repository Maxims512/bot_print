import createKeyboard
import db

def mainProcessor(message):
    keyboard = start()
    if (message.lower() == "начать"):
        keyboard = start()

    if (message.lower() == "записаться на стирку"):
        keyboard = laundryAppointment()

    if (message.lower() == "выставить товар"):
        keyboard = None

    return keyboard

def start():
    title = ["Записаться на стирку", "Посмотреть товары", "Выставить товар", "Посмотреть мероприятия"]
    keyboard = createKeyboard.createKeyboard(1,4, title)
    return keyboard

def laundryAppointment():
    if db.isFreeWashMashines:
        title = ["Тут будет свободное время для записи"]
        keyboard = createKeyboard.createKeyboard(1,1,title)
    else:
        title = ["ЗАНЯТО", "ЗАНЯТО", "ЗАНЯТО", "ЗАНЯТО"]
        keyboard = createKeyboard.createKeyboard(2, 2, title)

    return keyboard

