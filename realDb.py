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
        cursor.execute(
            f"""INSERT INTO washingTime (user_id, date) values ({user_id}, '{date}');"""
        )

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
            """SELECT EXTRACT (DOW FROM NOW());"""
        )
        return (cursor.fetchone()[0]+7)%8


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
