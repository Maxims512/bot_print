import datetime

import realDb


realDb.initDb()




realDb.addProduct(111, "uuuu")
id = realDb.getProductId("uuuu")
print(realDb.getProductPrice(id))

realDb.addProductPrice(id, 1000)

print(realDb.getProductPrice(id))


