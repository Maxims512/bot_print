# import psycopg2
# from dbConfig import host, user, password, db_name, port
#
# conn = psycopg2.connect(host="localhost", database="postgres", user="postgres",
#                         password="1234", port=5432)
#
#
#
# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users (
#     id INT,
#     last_message VARCHAR(255)
# )""")
#
# conn.commit()
# cur.close()
# conn.close()

class db:
    __attr = {
        "person" : {},
        "washingTime" : {}
    }
    def __init__(self):
        self.__dict__ = self.__attr

    def addPerson(self, id):
        self.__attr["person"][str(id)] = ""

    def setLastMessage(self, id, message):
        self.__attr["person"][str(id)] = message

    def verifyPerson(self, id):

        if (str(id) in self.__attr["person"].keys()):
            return True
        else:
            return False

    def getLastMessage(self, id):
        if (str(id) in self.__attr["person"].keys()):
            return self.__attr["person"][str(id)]
        else:
            return ""

    def getFreeWashingDay(self):
        freeDays = []
        for day in range(1, 6):
            if (len(self.getFreeWashingTime(day))>0):
                freeDays.append(day)
        return freeDays

    # def getWashings(self, i):
    #     return self.__attr["washingTime"]


    def getFreeWashingTime(self, day):
        washingTime = self.__attr["washingTime"]
        freeWashingTime = []
        for time in range(11, 16):
            if (str(day)+"_"+str(time) not in washingTime.values()):
                freeWashingTime.append(str(day)+"_"+str(time))
        return freeWashingTime



    # def setWashings(self, id, washingTime):
    #     self.washingTime[id]= washingTime

