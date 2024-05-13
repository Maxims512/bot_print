import datetime

import realDb

realDb.initDb()

date = datetime.datetime.now()
print(realDb.getDow())