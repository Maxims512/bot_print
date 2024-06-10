import datetime
import product
import realDb

date = datetime.datetime(2024, 6, 10, 17, 50)

realDb.initDb()

realDb.addEvent(111, "название", "место")

realDb.addEvent(111, "настолки", "")
realDb.addEvent(111, "25", "")
realDb.addEvent(111, "настки", "")

realDb.addEventPlace(2, "место")

realDb.addEventTime(2, date)

realDb.addParticipantToEvent(222, 2)

print(realDb.userInEvent(222, 2))
print(realDb.getParticipantOfEvent(2))





