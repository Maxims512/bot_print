import datetime

from dateBase import realDb
from createPDF.create_table_fpdf2 import PDF

def createPdfFile(title):

    pdf = PDF()
    pdf.add_font("Roboto", "", r"C:\Users\ivan8\Desktop\Bot kursovaya\createPDF\Roboto-Medium.ttf")

    pdf.add_page()
    pdf.set_font("Roboto", size=6)


    day = 0
    k=0
    nextWeek = realDb.getFullNextWeek()

    dow = realDb.getDow()


    print(day)
    pdf.create_table(table_data = getSheludeFromDay(day),title=nextWeek[k], cell_width='36', x_start=30)
    dow+=1
    if (dow == 5):
        dow = 0
        day+=2
    if (dow == 6):
        dow = 0
        day += 1
    day+=1
    k+=1
    print(day)
    pdf.create_table(table_data = getSheludeFromDay(day), title=nextWeek[k], cell_width='36', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 2
    if (dow == 6):
        dow = 0
        day += 1
    day += 1
    k+=1

    print(day)
    pdf.create_table(table_data = getSheludeFromDay(day),title=nextWeek[k], cell_width='36', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 2
    if (dow == 6):
        dow = 0
        day += 1
    day += 1
    k+=1

    print(day)
    pdf.create_table(table_data = getSheludeFromDay(day), title=nextWeek[k], cell_width='36', x_start=30)
    dow += 1
    if (dow == 5):
        dow = 0
        day += 2
    if (dow == 6):
        dow = 0
        day += 1
    day += 1
    k+=1

    print(day)
    pdf.create_table(table_data = getSheludeFromDay(day),title=nextWeek[k], cell_width='36', x_start=30)


    pdf.output('C:/Users/ivan8/Desktop/Bot kursovaya/createPDF/washings.pdf')
    print("Создали новый файл")

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