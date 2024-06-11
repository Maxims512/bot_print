import datetime
import product
import realDb

date = datetime.datetime(2024, 6, 10, 17, 50)

realDb.initDb()

today = realDb.getNow()
do = datetime.datetime(2024, 6, 11, 10)
posle = datetime.datetime(2024, 6, 11, 23)


realDb.addProduct(111, "продукт", 500, "sfg", "hht")



print(realDb.getAllProductsId())
realDb.productHandler()
print(realDb.getAllProductsId())




