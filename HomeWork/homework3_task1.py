# Напишите приложение, которое будет запрашивать у пользователя следующие данные
# в произвольном порядке, разделенные пробелом: Фамилия Имя Отчество датарождения номертелефона пол
#
# Форматы данных:
# фамилия имя отчество - строка
# датарождения - строка формата dd.mm.yyyy
# номертелефона - целое беззнаковое число без форматирования
# пол - символ латиницей f или m.
#
# Приложение должно проверить введенные данные по количеству.
# Если количество не совпадает с требуемым, вернуть код ошибки, обработать его и показать
# пользователю сообщение, что он ввел меньше и больше данных, чем требуется.
# Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры.
# Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы.
# Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано,
# пользователю выведено сообщение с информацией, что именно неверно.
# Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии,
# в него в одну строку должны записаться полученные данные, вида:
# <Фамилия> <Имя> <Отчество> <датарождения> <номертелефона> <пол>
# Однофамильцы должны записаться в один и тот же файл, в отдельные строки.
# Не забудьте закрыть соединение с файлом.
# При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано,
# пользователь должен увидеть стектрейс ошибки.

#import datetime
from datetime import datetime

class DataError(Exception):
    pass

def sortData(db):
    ndb = [0, 0, 0, 0, 0, 0]
    for i in range(0, len(db)):
        if db[i].find(".") == 2:
            ndb[3] = db[i]
            j = i
    # print(db)
    db.pop(j)
    # print(db)
    for i in range(0, len(db)):
        if db[i].isdigit():
            ndb[4] = db[i]
            j = i
    # print(db)
    db.pop(j)
    # print(db)
    for i in range(0, len(db)):
        if (len(db[i]) == 1):
            ndb[5] = db[i]
            j = i
    # print(db)
    db.pop(j)
    # print(db)
    for i in range(0, len(db)):
        if (len(db[i]) > 1):
            ndb[i] = db[i]
    return ndb

def check_date(day: int, month: int, year: int) -> bool:
    correctDate = None
    try:
        datetime.fromisoformat(f"{year}-{month:02}-{day:02}")
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate

data_str = input("Enter data in random order through the space:\n surname name patronymic, date of birth in the format dd.mm.yyyy, phone number, gender all through the space\n")
data = data_str.split(" ")

if len(data) != 6:
    raise DataError('Incorrect number of values entered')

ndata = sortData(data)
ndata_str = ' '.join(ndata)

try:
    cd = ndata[3].split(".")
    check_date(cd[0], cd[1], cd[2])
except ValueError:
    raise DataError("Invalid date format entered, it should be dd.mm.yyyy")

if not ndata[4].isdigit():
    raise DataError("Invalid phone number format entered")

if ndata[5] == "f" or ndata[5] == "m":
    pass
else:
    raise DataError("Invalid gender entered, it should be - m or f")

try:
    with open(ndata[0], 'a') as tofile:
        tofile.write(ndata_str+"\n")
except:
    raise DataError("Unable to write file")
