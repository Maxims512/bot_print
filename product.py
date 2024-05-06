class Product:
    __id = 0
    __price = 0
    __description = ""
    __photo = ""

    def __init__(self, id, price, description, photo):
        self.__id = id
        self.__price = price
        self.__description = description
        self.__photo = photo