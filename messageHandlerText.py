import db
import messageHandlerKeyboard

def answer(message, lastMessage, fullMessage):
    #тут сделаем проверки и будет добавлять клавы и работать с бд
    text = "Я вас не понимаю"
    if (message == "записаться на стирку"):
        if (db.isFreeWashMashines):
            text = "Выберите удобное время"
        else:
            text = "К сожалению на ближайшую неделю все машинки заняты"

    if (message == "выставить товар"):
        text = "Введите описание товара"


    return text

