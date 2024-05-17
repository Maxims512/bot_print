import datetime

from dateBase import realDb
from create_table_fpdf2 import PDF

def createPdfFile(title):

    parapam = getSheludeFromDay(1)
    print(parapam)
    i = 0
    dayNextWeek = realDb.getNextWeek()
    day = int(dayNextWeek[i].split("_")[0])
    month = int(dayNextWeek[i].split("_")[1])
    year = int(dayNextWeek[i].split("_")[2])



    data = []


    monthNow = realDb.getMonth()
    yearNow = realDb.getYear()

    realDb.initDb()
    date1 = datetime.datetime(2024, 5, 17, 14)
    date2 = datetime.datetime(2024, 5, 17, 15)



    for i in range(6):
        data1 = []
        for j in range(5):
            data1.append("")
        data.append(data1)

    realDb.addPerson(111, "artem")
    realDb.addPerson(222, "lexa")
    realDb.addWashing(111, date1)
    realDb.addWashing(111, date2)
    realDb.addWashing(222, date2)
    realDb.addWashing(222, date1)

    for hour in range(11,16):
        #тут надо переделать под общую дату
        dateTime = datetime.datetime(yearNow, monthNow, day, hour)
        res = realDb.getWashingsFromTime(dateTime)
        data[hour-11] = res



    for i in range(5):
        mass = "Свободно"
        if len(data[i]) < 5:
            for j in range(5-len(data[i])):
                data[i].append(mass)






    pdf = PDF()
    pdf.add_font("Roboto", "", r"C:\Users\ivan8\Desktop\Bot kursovaya\createPDF\Roboto-Medium.ttf")

    pdf.add_page()
    pdf.set_font("Roboto", size=8)



    day = 0

    dow = realDb.getDow() - 1
    if (dow == 5 or dow == 6):
        day += 3
        dow = 0

    dayWeek = realDb.getFullNextWeek()
    nextWeek = []
    for i in realDb.getNextWeek():
        nextWeek.append(i.split("_")[0])

    pdf.create_table(table_data = data,title=dayWeek[0], cell_width='33', x_start=30, emphasize_data=["1", "2","3","4","5"])
    dow+=1
    if (dow == 5):
        dow = 0
        day+=3
    if (dow == 6):
        dow = 0
        day += 2
    day+=1

    pdf.create_table(table_data = data, title=dayWeek[1], cell_width='33', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 3
    if (dow == 6):
        dow = 0
        day += 2
    day += 1


    pdf.create_table(table_data = data,title=dayWeek[2], cell_width='33', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 3
    if (dow == 6):
        dow = 0
        day += 2
    day += 1

    pdf.create_table(table_data = data, title=dayWeek[3], cell_width='33', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 3
    if (dow == 6):
        dow = 0
        day += 2
    day += 1


    pdf.create_table(table_data = data,title=dayWeek[4], cell_width='33', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 3
    if (dow == 6):
        dow = 0
        day += 2
    day += 1



    pdf.output('table_class.pdf')




def getSheludeFromDay(dayPoSChetu):
    data = []
    dayNextWeek = realDb.getNextWeek()

    for i in range(5):
        data1 = []
        for j in range(5):
            data1.append("")
        data.append(data1)

    for hour in range(11,16):
        day = int(dayNextWeek[dayPoSChetu].split("_")[0])
        month = int(dayNextWeek[dayPoSChetu].split("_")[1])
        year = int(dayNextWeek[dayPoSChetu].split("_")[2])
        dateTime = datetime.datetime(year, month, day, hour)
        res = realDb.getWashingsFromTime(dateTime)
        data[hour-11] = res

    for i in range(5):
        mass = "Свободно"
        if len(data[i]) < 5:
            for j in range(5-len(data[i])):
                data[i].append(mass)

    return data

createPdfFile(0)