from dateBase import realDb
class Event():
    def __init__(self, event_id, creator_id, title, place, date, participant):
        self.__event_id = event_id
        self.__creator_id = creator_id
        self.__title = title
        self.__place = place
        self.__date = date
        self.__participant = participant

    def toString(self):
        parti = ""
        if self.__participant != None:
            for i in self.__participant:
                parti += f"@id{i}({realDb.getUserName(i)}), "

        answer = (f"ID мероприятия: {self.__event_id}, Название: {self.__title}, Создатель: @id{self.__creator_id}({realDb.getUserName(self.__creator_id)}),"
                  f" Место: {self.__place}, Время: {self.__date}, Участники: {parti} ____________________________________")
        return answer


    def get_title(self):
        return self.__title


