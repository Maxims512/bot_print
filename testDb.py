import datetime

import realDb

date = datetime.datetime(2010, 10, 21, 13)
date2 = datetime.datetime(2010, 10, 20, 13)

realDb.initDb()

realDb.setLastMessage(111, "")

print(realDb.getLastMessage(111))