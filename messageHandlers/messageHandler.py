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
        text = "Введите название товара (не более 50 символов)"
        keyboard = getEmptyKeyboard()

    if (lastMessage == "выставить товар на продажу" and len(message) < 50):
        if (not realDb.haveProductName(message)):
            realDb.addProduct(user_id, message)
            product_id = realDb.getProductId(message)
            keyboard = createCreateKeyboardTitle(f"Добавить цену:{product_id}")
            text = "Нажмите 'Добавить цену'"
        else:
            text = "Такой товар уже есть, введите другое название"
            keyboard = getStartProductKeyboard()

    if (message.split(":")[0] == "добавить цену" and realDb.haveProductId(message.split(":")[1])):
        text = "Введите цену товара (только число)"
        keyboard = getEmptyKeyboard()

    if (lastMessage != None and lastMessage.split(":")[0] == "добавить цену" and message.isnumeric()
            and int(message)<1000000 and realDb.haveProductId(lastMessage.split(":")[1])):
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



    fullMessage.setAnswer(text)
    fullMessage.setKeyboard(keyboard)

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