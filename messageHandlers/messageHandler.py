import datetime

import createPDF.table_class
from dateBase import realDb
from messageHandlers import createKeyboard

def getAnswer(message, lastMessage, fullMessage):
    text = getStartText()
    keyboard = getStartKeyboard()
    user_id = fullMessage.getUserId()
    print(lastMessage)
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
            createPDF.table_class.createPdfFile(0)
        else:
            text = "К сожалению это время занято"
            keyboard = getStartKeyboard()

    if message == "посмотреть расписание стирок":

        createPDF.table_class.createPdfFile(0)
        text = "Расписание стирок на ближайшую неделю:"


    if message == "отменить стирку":
        if (len(realDb.getWashingTimeFromUser(user_id)) > 0):
            text = "Выберите время которое вам не подходит"
            keyboard = getWashingsFromUserKeyboard(user_id)
        else:
            text = "У вас нет активных стирок"

    if (lastMessage == "отменить стирку" and message.count(" ") > -1 and len(message.split(" ")) > 1 and
            message.split(" ")[1].split(":")[0] in ["11", "12", "13", "14", "15"]):
        text = f"Вы отменили стирку {message}"
        year = int(message.split(" ")[0].split('-')[0])
        month = int(message.split(" ")[0].split('-')[1])
        day = int(message.split(" ")[0].split('-')[2])
        hour = int(message.split(" ")[1].split(':')[0])
        date = datetime.datetime(year, month, day, hour)
        realDb.deleteWashing(user_id, date)
        createPDF.table_class.createPdfFile(0)




    if (message == "товары"):
        text = "Выберите дальнейшее действие"
        keyboard = getStartProductKeyboard()

    if (lastMessage == "товары" and message == "выставить товар на продажу"):
        realDb.productHandler()
        if (len(realDb.getProductIdByUser(user_id))==10):
            text = "У вас уже есть 10 активных товаров"
            keyboard = getStartProductKeyboard()
        else:
            text = "Введите название товара (не более 50 символов)"
            keyboard = getEmptyKeyboard()

    if (lastMessage == "выставить товар на продажу" and len(message) < 50 and message not in["мероприятия", "товары",
        "посмотреть все товары", "удалить товар с продажи"]):
        if (not realDb.haveProductName(message)):
            realDb.addProduct(user_id, message)
            product_id = realDb.getProductId(message)
            keyboard = createCreateKeyboardTitle(f"Добавить цену:{product_id}")
            text = "Нажмите 'Добавить цену'"
        else:
            text = "Такой товар уже есть, введите другое название"
            keyboard = getStartProductKeyboard()

    if (message.split(":")[0] == "добавить цену" and realDb.haveProductIdWithoutPrice(message.split(":")[1])):
        text = "Введите цену товара (только число)"
        keyboard = getEmptyKeyboard()

    if (lastMessage != None and lastMessage.split(":")[0] == "добавить цену" and message.isnumeric()
            and int(message)<1000000 and realDb.haveProductIdWithoutPrice(lastMessage.split(":")[1])):
        product_id = lastMessage.split(":")[1]
        print(product_id)
        realDb.addProductPrice(product_id, int(message))
        keyboard = addProductPhotoKeyboard(product_id)
        text = "Выберите следующее действие"

    if (message.split(":")[0] == "добавить фото" and realDb.haveProductId(message.split(":")[1])):
        text = "Отправьте фото товара"
        keyboard = getEmptyKeyboard()

    if (lastMessage != None and lastMessage.split(":")[0] == "добавить фото"
            and realDb.haveProductId(lastMessage.split(":")[1])):
        product_id = lastMessage.split(":")[1]
        keyboard = addProductDescriptionKeyboard(product_id)
        text = f"Вы добавили фото товару {realDb.getProductName(product_id)}"

    if message.split(":")[0] == "оставить товар без фото" and realDb.haveProductId(message.split(":")[1]):
        product_id = message.split(":")[1]
        keyboard = addProductDescriptionKeyboard(product_id)
        text = "Выберите дальнейшее действие"

    if message.split(":")[0] == "добавить описание" and realDb.haveProductId(message.split(":")[1]):
        text = "Введите описание товара (не более 100 символов)"
        keyboard = getEmptyKeyboard()

    if (lastMessage != None and lastMessage.split(":")[0] == "добавить описание"
            and realDb.haveProductId(lastMessage.split(":")[1]) and len(message) <= 100):
        product_id = lastMessage.split(":")[1]
        realDb.addProductDescription(product_id, message)
        text = f"Вы добавили описание товару {realDb.getProductName(product_id)}"
        keyboard = getStartKeyboard()

    if message.split(":")[0] == "оставить товар без описания" and realDb.haveProductId(message.split(":")[1]):
        product_id = message.split(":")[1]
        text = f"Вы оставили товар {realDb.getProductName(product_id)} без описания"
        keyboard = getStartKeyboard()

    if (lastMessage == "товары" and message == "посмотреть все товары"):
        str1 = ""
        for i in realDb.getAllProductsId():
            prod = realDb.getProduct(i)
            if (prod.getPrice() > -1):
                str1+=prod.toString()

        if str1 == "":
            text = "Сейчас нет активных товаров"
        else:
            text = str1
        keyboard = getStartProductKeyboard()

    if message == "удалить товар с продажи":
        products_id = realDb.getProductIdByUser(user_id)
        if len(products_id)==0:
            text = "У вас нет активных товаров"
        else:
            str1 = ""
            for i in products_id:
                str1 += realDb.getProduct(i).toStringMini()
            str1+="Введите ID товара, который вы хотите удалить"
            keyboard = getEmptyKeyboard()
            text = str1

    if lastMessage == "удалить товар с продажи" and message.isnumeric():
        if int(message) in realDb.getProductIdByUser(user_id):
            text = f"Вы удалили товар {realDb.getProductName(message)}"
            realDb.deleteProduct(message)
            keyboard = getStartKeyboard()
        else:
            text = "Это не ваш товар"
            keyboard = getStartProductKeyboard()

    if message == "мероприятия":
        keyboard = getStartEventKeyboard()
        text = "Выберите дальнейшее действие"

    if message == "создать мероприятие":
        #тут проверка мероприятий и сделай все по плану товаров
        if realDb.getCountEventByUser(user_id) == 5:
            text = "У вас уже есть 5 активных мероприятий"
            keyboard = getStartEventKeyboard()
        else:
            text = "Введите название мероприятия (не более 50 символов)"
            keyboard = getEmptyKeyboard()




    if lastMessage == "создать мероприятие" and len(message)<=50 and \
        message not in ["мероприятия", "товары", "стирка", "создать мероприятие"]:
        realDb.addEvent(user_id, message)
        event_id = realDb.getEventId(message)
        keyboard = createCreateKeyboardTitle(f"Далее:{event_id}")
        text = "Нажмите далее"

    if (message != None and message.split(":")[0] == "далее"
            and realDb.haveEventId(message.split(":")[1]) and len(message) <= 100):
        text = "Введите время мероприятия в виде ЧАСЫ:МИНУТЫ (00:05)"
        keyboard = getEmptyKeyboard()

    if  (lastMessage != None and lastMessage.split(":")[0] == "далее"
            and realDb.haveEventId(lastMessage.split(":")[1]) and len(message) <= 100) and checkTime(message):
        today = realDb.getNow()[0][0]
        date = datetime.datetime(today.year, today.month, today.day, int(message[:2]), int(message[3:5]))
        realDb.addEventTime(lastMessage.split(":")[1], date)
        text = "Нажмите ввести место мероприятия"
        keyboard = createCreateKeyboardTitle(f"Ввести место мероприятия:{lastMessage.split(":")[1]}")

    if message.split(":")[0] == "ввести место мероприятия":
        text = "Введите место проведения мероприятия (не более 50 символов)"
        keyboard = getEmptyKeyboard()

    if lastMessage != None and lastMessage.split(":")[0] == "ввести место мероприятия" and len(message) <= 50:
        realDb.addEventPlace(lastMessage.split(":")[1], message)
        text = f"Вы создали мероприятие {realDb.getEvent(lastMessage.split(":")[1]).get_title()}"
        keyboard = getStartEventKeyboard()

    if message == "удалить мероприятие":
        if (realDb.getCountEventByUser(user_id) == 0):
            text = "У вас нет активных мероприятий"
            keyboard = getStartKeyboard()
        else:
            answer = ""
            for i in realDb.getUsersEvents(user_id):
                answer+=realDb.getEvent(i).toString()
            answer+="_________Введите ID мероприятия которое вы хотите удалить"
            text = answer
            keyboard = getEmptyKeyboard()

    if (lastMessage != None and lastMessage == "удалить мероприятие" and message.isnumeric()
            and int(message) in realDb.getUsersEvents(user_id)):
        text = f"Вы удалили мероприятие '{realDb.getEvent(message).get_title()}'"
        realDb.deleteEvent(message)
        keyboard = getStartKeyboard()

    if message == "посмотреть текущие мероприятия":
        events = realDb.getAllEventsId()
        if len(events) == 0:
            text = "Сейчас нет активных мероприятий"
            keyboard = getStartEventKeyboard()
        else:
            answer = ""
            for i in realDb.getAllEventsId():
                answer += realDb.getEvent(i).toString()
            answer += "Введите ID мероприятия на которое вы хотите записаться"
            text = answer
            keyboard = getStartEventKeyboard()

    if (lastMessage != None and lastMessage == "посмотреть текущие мероприятия" and message.isnumeric()
            and int(message) in realDb.getAllEventsId()):
        if realDb.userInEvent(user_id, message):
            text = f"Вы уже записаны на мероприятие {realDb.getEvent(message).get_title()}"
            keyboard = getStartEventKeyboard()
        else:
            realDb.addParticipantToEvent(user_id, message)
            text = f"Вы записались на мероприятие {realDb.getEvent(message).get_title()}"
            keyboard = getStartEventKeyboard()









    fullMessage.setAnswer(text)
    fullMessage.setKeyboard(keyboard)




def checkTime(time):
    if len(time)!=5:
        return False
    if time[2] != ":":
        return False
    if not (time[:2].isnumeric() and time[3:5].isnumeric()):
        return False
    hour = int(time[:2])
    minute = int(time[3:5])
    return (0<=hour<=24 and 0<=minute<=60)




def addEventDescriptionKeyboard(message):
    title = []
    title.append(f"Добавить описание мероприятия {message}")
    title.append("Оставить без описания")
    keyboard = createKeyboard.createKeyboard(1, 2, title)
    return keyboard

def addProductDescriptionKeyboard(product_id):
    title = []
    title.append(f"Добавить описание: {product_id}")
    title.append(f"Оставить товар без описания:{product_id}")
    keyboard = createKeyboard.createKeyboard(1,2, title)
    return keyboard

def addProductPhotoKeyboard(product_id):
    title = []
    title.append(f"Добавить фото: {product_id}")
    title.append(f"Оставить товар без фото:{product_id}")
    keyboard = createKeyboard.createKeyboard(1,2, title)
    return keyboard


def getStartEventKeyboard():
    title = ["Посмотреть текущие мероприятия", "Создать мероприятие", "Удалить мероприятие"]
    keyboard = createKeyboard.createKeyboard(1, 3, title)
    return keyboard

def createCreateKeyboardTitle(title):
    titles = []
    titles.append(title)
    keyboard = createKeyboard.createKeyboard(1, 1, titles)
    return keyboard

def getStartProductKeyboard():
    title = ["Посмотреть все товары", "Выставить товар на продажу", "Удалить товар с продажи"]
    keyboard = createKeyboard.createKeyboard(1, 3, title)
    return keyboard

def getWashingsFromUserKeyboard(user_id):
    title = []
    for i in realDb.getWashingTimeFromUser(user_id):
        title.append(str(i[0]))
    keyboard = createKeyboard.createKeyboard(1, len(title), title)
    return keyboard

def getWashingDayKeyboard():
    title = realDb.getFreeWashingDay()
    if len(title)>0:
        keyboard = createKeyboard.createKeyboard(1, len(title), title)
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
    keyboard = createKeyboard.createKeyboard(1, 4, title)

    return keyboard

def getEmptyKeyboard():
    title = []
    keyboard = createKeyboard.createKeyboard(0, 0, title)
    return keyboard

def getStartText():
    return "Я вас не понимаю"