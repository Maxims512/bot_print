import datetime
import product
import realDb


realDb.initDb()




realDb.addEvent(111, "настолки", "")

realDb.addParticipantToEvent(222, 1)

print(realDb.getParticipantOfEvent(1))
print(realDb.userInEvent(222, 1))

realDb.deletePartipantOfEvent(222, 1)

print(realDb.userInEvent(222, 1))



