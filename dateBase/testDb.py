import datetime

import realDb

date = datetime.datetime(2024, 5, 15, 14)
date2 = datetime.datetime(2024, 5, 15, 15)

print(realDb.getNextWeek())



print(realDb.getNextWeekDateTime())