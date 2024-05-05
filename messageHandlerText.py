import db

def answer(message, lastMessage, fullMessage):
    #тут сделаем проверки и будет добавлять клавы и работать с бд
    text = "Я вас не понимаю"
    if (message == "записаться на стирку"):
        if (len(db.db.getFreeWashingTime(1))>0):
            text = "Выберите день"
        else:
            text = "К сожалению на ближайшую неделю все машинки заняты"

    if (message == "выставить товар"):
        text = "Введите описание товара"


    return text

