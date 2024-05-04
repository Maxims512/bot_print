class Event():
    def __init__(self, id, id_creator, name, date, place, date_creation, description):
        self.__id = id
        self.__id_creator = id_creator
        self.__name = name
        self.__date = date
        self.__place = place
        self.__date_creation = date_creation
        self.__description = description
        self.__place = place
        self.__date_creation = date_creation

    def __str__(self):
        return f'{self.__name}: {self.__date} - {self._place}: {self.__date_creation}'

    def get_id(self):
        return self.__id

    def get_id_creator(self):
        return self.__id_creator

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_place(self):
        return self.__place

    def get_date_creation(self):
        return self.__date_creation

    def get_description(self):
        return self.__description

    id = property(get_id)
    id_creator = property(get_id_creator)
    name = property(get_name)
    data = property(get_date)
    place = property(get_place)
    date_creation = property(get_date_creation)
    description = property(get_description)
