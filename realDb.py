import psycopg2
import datetime
from dbConfig import host, user, password, db_name

def initDb():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        cursor.execute(
            """DROP TABLE washingTime;"""
        )
        cursor.execute(
            """CREATE TABLE users(
                user_id varchar(50) NOT NULL PRIMARY KEY,
                last_message varchar(100));"""
        )
        cursor.execute(
            """CREATE TABLE washingTime(
                user_id varchar(50) NOT NULL,
                date timestamp NOT NUll);"""
        )

def addPerson(user_id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (user_id) VALUES ({user_id});"""
        )

def verifyPerson(user_id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT COUNT(*) FROM users WHERE user_id = '{user_id}';"""
        )
        return cursor.fetchone()[0]>0


def addWashing(user_id, date):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        if verifyPerson(user_id):
            cursor.execute(
                f"""INSERT INTO washingTime (user_id, date) values ('{user_id}', '{date}');"""
            )

def getFreeWashingTime(day):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT date FROM washingTime;"""
        )
        washings = cursor.fetchall()

    washingTime = {"11": "0", "12": "0", "13": "0", "14": "0", "15": "0"}
    for i in washings:
        if i[0].day == day:
            washingTime[str(i[0].hour)] = str(int(washingTime[str(i[0].hour)]) + 1)

    freeWashingTime = []
    for hour in range(11, 16):
        if (int(washingTime[str(hour)]) < 5):
            freeWashingTime.append(hour)

    return freeWashingTime



def getFreeWashingDay():
    freeWashingDay = []
    for day in getNextWeek():
        if (len(getFreeWashingTime(day))>0):
            freeWashingDay.append(day)
    return freeWashingDay





def getCountWashFromTime(dateTime):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT COUNT(*) FROM washingTime WHERE date = '{dateTime}';"""
        )
        return cursor.fetchone()[0]

def getCountWashFromPerson(user_id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT COUNT(*) FROM washingTime WHERE user_id = '{user_id}';"""
        )
        return cursor.fetchone()[0]

def getNextWeek():
    nextWeek = []
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now();"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'1 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'2 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'3 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'4 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'5 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'6 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT now()+'7 day';"""
        )
        nextWeek.append(cursor.fetchone()[0].day)
    return nextWeek




def setLastMessage(user_id, message):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        if (not verifyPerson(user_id)):
            return
        elif (len(message) < 50):
            cursor.execute(
                f"""UPDATE users SET last_message = '{message}' WHERE user_id = '{user_id}';"""
            )
        else:
            cursor.execute(
                f"""UPDATE users SET last_message = '{""}' WHERE user_id = '{user_id}';"""
            )

def getLastMessage(user_id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        if (verifyPerson(user_id)):
            cursor.execute(
                f"""SELECT last_message FROM users WHERE user_id = '{user_id}';"""
            )
            return cursor.fetchone()[0]
        else:
            return ""

def getDay():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT NOW();"""
        )
        return cursor.fetchone()[0].day

def getMonth():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT NOW();"""
        )
        return cursor.fetchone()[0].month


def getYear():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT NOW();"""
        )
        return cursor.fetchone()[0].year

def getDow():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT EXTRACT(dow FROM now()), date_part('dow', now()), now()::date;"""
        )
        return cursor.fetchone()[0]


def getNow():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT NOW();"""
        )
        return cursor.fetchone()
