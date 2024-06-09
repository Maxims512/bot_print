import datetime
import product
import realDb


realDb.initDb()




realDb.addProduct(111, "ttt", 10)
id = realDb.getProductId("ttt")
print(realDb.getProductName(id))
print(realDb.getProductIdByUser(111))



