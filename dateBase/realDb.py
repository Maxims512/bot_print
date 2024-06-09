import datetime

import psycopg2
from configs.dbConfig import host, user, password, db_name

def initDb():
    req1 = """DROP TABLE users;"""
    req2 = """DROP TABLE washingTime;"""
    req3 = "DROP TABLE products;"
    req4 = """CREATE TABLE users(
                user_id varchar(50) NOT NULL PRIMARY KEY,
                full_name varchar(50),
                last_message varchar(100));"""

    req5 = """CREATE TABLE washingTime(
                user_id varchar(50) NOT NULL,
                date timestamp NOT NUll);"""


    req6 = """CREATE TABLE products(
                product_id SERIAL PRIMARY KEY,
                user_id varchar(50) NOT NULL,
                title varchar(50) NOT NULL,
                price integer NOT NULL,
                date_of_creation timestamp NOT NUll,
                description varchar(200),
                link_of_photo varchar(200));"""



    request(req1)
    request(req2)
    request(req3)
    request(req4)
    request(req5)
    request(req6)


def request(req):
    ret = []
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            req
        )
        if req.find("SELECT") > -1:
            return cursor.fetchall()
    return ret


def getUserName(user_id):
    if (verifyPerson(user_id)):
        req = f"SELECT full_name FROM users WHERE user_id = '{user_id}'"
        return request(req)[0][0]
    else:
        return ""


def addPerson(user_id, name):
    if not verifyPerson(user_id):
        req = f"""INSERT INTO users (user_id, full_name) VALUES ({user_id}, '{name}');"""
        request(req)


def verifyPerson(user_id):
    req =  f"""SELECT COUNT(*) FROM users WHERE user_id = '{user_id}';"""
    return request(req)[0][0]>0


def addWashing(user_id, date):
    if (getCountWashFromPerson(user_id)<2):
        req = f"""INSERT INTO washingTime (user_id, date) values ('{user_id}', '{date}');"""
        request(req)


def getFreeWashingTime(day):
    req = f"""SELECT date FROM washingTime;"""
    washings = request(req)
    washingTime = {"11": "0", "12": "0", "13": "0", "14": "0", "15": "0"}
    for i in washings:
        if i[0].day == day:
            washingTime[str(i[0].hour)] = str(int(washingTime[str(i[0].hour)]) + 1)

    freeWashingTime = []
    for hour in range(11, 16):
        if (int(washingTime[str(hour)]) < 5):
            freeWashingTime.append(hour)

    return freeWashingTime


def getWashingTimeFromUser(user_id):
    req = f"""SELECT date FROM washingTime WHERE user_id = '{user_id}';"""
    return request(req)


def getFreeWashingDay():
    dow = getDow()
    freeWashingDay = []
    if dow == 0:
        dow = 7
    sat = (6 - dow)
    if sat < 0:
        sat = 7
    sun = 7 - dow
    k = 0
    o = 0
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
    for day in getNextWeek():
        if (len(getFreeWashingTime(day))>0 and k != sat and k != sun and k < 7 and o < 5):
            o+=1
            freeWashingDay.append(days[int((dow%7)%5)-1]+" "+day)
        k += 1
        dow+=1

    return freeWashingDay



def getFullNextWeek():
    dow = getDow()
    DaysWeek = []

    sat = (6 - dow)
    if sat < 0:
        sat = 7
    sun = 7 - dow
    k = 0
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]

    print(sat, sun)
    for day in getNextWeek():


        if (k != sat and k != sun and k < 7):
            DaysWeek.append(days[int((dow % 7) % 5) - 1] + " " + day)

        k += 1
        dow += 1

    return DaysWeek

def getCountWashFromTime(dateTime):
    req =  f"""SELECT COUNT(*) FROM washingTime WHERE date = '{dateTime}';"""
    return request(req)[0]


def getCountWashFromPerson(user_id):
    req =  f"""SELECT COUNT(*) FROM washingTime WHERE user_id = '{user_id}';"""
    return request(req)[0][0]

def getWashingsFromTime(date):
    req = (f"SELECT full_name FROM users JOIN washingTime ON users.user_id = washingTime.user_id AND washingTime.date = '{date}';")
    res = []
    mass = request(req)
    for i in mass:
        res.append(i[0])
    return res

def getNextWeek():
    nextWeek = []
    for i in range(7):
        req = f"""SELECT now()+'{i} day';"""
        nextWeek.append(str(request(req)[0][0].day) + "_" + str(request(req)[0][0].month) + "_" + str(request(req)[0][0].year))
    return nextWeek

def getNextWeekDateTime():
    nextWeek = []
    for i in range(7):
        req = f"""SELECT now()+'{i} day';"""
        date = datetime.datetime(request(req)[0][0].year, request(req)[0][0].month, request(req)[0][0].day)

        nextWeek.append(date)

    return nextWeek


def deleteWashing(user_id, dateTime):
    if getCountWashFromPerson(user_id) > 0:
        req = f"DELETE from washingTime WHERE user_id = '{user_id}' and date = '{dateTime}'"
        request(req)

def setLastMessage(user_id, message):
    if (not verifyPerson(user_id)):
        return
    elif (len(message) < 50):
        req = f"""UPDATE users SET last_message = '{message}' WHERE user_id = '{user_id}';"""
    else:
        req = f"""UPDATE users SET last_message = '{""}' WHERE user_id = '{user_id}';"""
    request(req)


def getLastMessage(user_id):
    req = f"""SELECT last_message FROM users WHERE user_id = '{user_id}';"""
    return request(req)[0][0]


def getDay():
    req = """SELECT NOW();"""
    return request(req)[0][0].day

def getMonth():
    req = """SELECT NOW();"""
    return request(req)[0][0].month


def getYear():
    req = """SELECT NOW();"""
    return request(req)[0][0].year

def getDow():
    req = """SELECT EXTRACT(dow FROM now()), date_part('dow', now()), now()::date;"""
    return int(request(req)[0][0])


def getNow():
    req =   """SELECT NOW();"""
    return request(req)

def getProductDescriptionProductId(product_id):
    req = f"SELECT description FROM products WHERE product_id = '{product_id}';"
    return request(req)

def addProduct(user_id, title, price=-1, description="", link_photo=""):
    today = getNow()[0][0]
    req = f"""INSERT INTO products (user_id, title, price, date_of_creation, description, link_of_photo) 
           values ('{user_id}', '{title}', '{price}', '{today}', '{description}', '{link_photo}');"""
    request(req)


def haveProductId(product_id):
    req = f"SELECT * FROM products WHERE product_id = '{product_id}';"
    return len(request(req)) > 0
def haveProductName(name):
    req = f"SELECT * FROM products WHERE title = '{name}';"
    return len(request(req))>0

def getProductId(name):
    req = f"SELECT product_id FROM products WHERE title = '{name}';"
    return request(req)[0][0]

def addProductPrice(product_id, price):
    req = f"UPDATE products SET price = '{price}' WHERE product_id = '{product_id}';"
    request(req)

def getProductName(product_id):
    req = f"SELECT title FROM products WHERE product_id = '{product_id}';"
    return request(req)[0][0]
def getProductPrice(product_id):
    req = f"SELECT price FROM products WHERE product_id = '{product_id}';"
    return request(req)[0][0]