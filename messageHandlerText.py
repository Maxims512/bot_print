import db
from vkBot import descriptionTime

def answer(message):
    text = "Я вас не понимаю"
    if (message == "записаться на стирку"):
        descriptionTime = False
        if (db.isFreeWashMashines):
            text = "Выберите удобное время"
        else:
            text = "К сожалению на ближайшую неделю все машинки заняты"

    if (message == "выставить товар"):
        descriptionTime = True
        text = "Введите описание товара"


    return text

