class Product:
    __id = 0
    __price = 0
    __description = ""
    __photo = ""

    def __init__(self, id, price, descriptiom, photo):
        self.__id = id
        self.__price = price
        self.__description = descriptiom
        self.__photo = photo