from dateBase import realDb
class Product:
    __product_id = 0
    __user_id = 0
    __title = ""
    __price = 0
    __date_of_creation = ""
    __description = ""
    __photo = ""

    def __init__(self, product_id, user_id, title, price, date, description, photo):
        self.__product_id = product_id
        self.__user_id = user_id
        self.__title = title
        self.__price = price
        self.__date_of_creation = date
        self.__description = description
        self.__photo = photo

    def getPrice(self):
        return self.__price
    def toString(self):
        answer = (f"ID продукта: {self.__product_id}, Название: {self.__title}, Цена: {self.__price}p,"
               f" Описание: {self.__description}, Фото: {self.__photo},"
               f" Продавец: @id{self.__user_id}({realDb.getUserName(self.__user_id)}),"
               f" Дата создания: {str(self.__date_of_creation)[:16]}____________________________________")
        return answer

    def toStringMini(self):
        answer = f"ID продукта: {self.__product_id}, Название: {self.__title}, Цена: {self.__price}p,____________"
        return answer