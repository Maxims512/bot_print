import datetime

import realDb

date4 = datetime.datetime(2010, 10, 21, 11)
date1 = datetime.datetime(2010, 10, 21, 12)
date2 = datetime.datetime(2010, 10, 21, 13)
date3 = datetime.datetime(2010, 10, 21, 14)

realDb.initDb()
realDb.addPerson(111)
realDb.addPerson(222)
realDb.addWashing(111, date1)
realDb.addWashing(111, date2)
realDb.addWashing(222, date3)
realDb.addWashing(222, date4)


print(realDb.getFreeWashingTime(21))