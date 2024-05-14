import datetime

import realDb

realDb.initDb()
realDb.addPerson(111, "sdf")


print(realDb.verifyPerson(111))