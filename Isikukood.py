__author__ = 'madispiigli'
#Isikukoodi genereerimise programm. Programm ei arvesta liigaastaga.


from datetime import datetime
import random


def getYear():
    year = random.choice(range(1800, 2199))
    return year
def getMonth():
    month = random.choice(range(1, 12))
    return month
def getDay():
    day = random.choice(range(1, 28))
    return day
def getBirthDay():
    birthDate = datetime(getYear(), getMonth(), getDay())
    return birthDate
def getGender():
    gender = str(random.choice(range(1,6)))
    return gender
def getNumber():
    number = str(random.choice(range(1, 999)))
    return number
def Sugu():
    if int(getGender()) % 2 == 0:
        return "N"
    else:
        return "M"

def getCode():
    kordaja1 = ['1','2','3','4','5','6','7','8','9','1']
    kordaja2 = ['3','4','5','6','7','8','9','1','2','3']
    summa = 0
    summa2 = 0
    for k, p in zip(kordaja1, isikukood()):
        summa = summa + (int(k) * int(p))
    for l, z in zip(kordaja2, isikukood()):
        summa2 = summa2 + (int(l) * int(z))
    kood = 0
    if summa % 11 < 10:
        kood = summa % 11
    elif summa % 11 >= 10:
        kood = summa2 % 11
    elif summa2 % 11 >= 10:
        kood = 0
    return str(kood)

def isikukood():
    """Isikukood, millel on kontrollkood puudu"""
    isiku_kood = []
    birthDate = str((getBirthDay().strftime('%y%m%d')))
    for k in getGender():
        isiku_kood.append(k)
    for i in birthDate:
        isiku_kood.append(i)
    for j in getNumber():
        isiku_kood.append(j)
    return isiku_kood

def isik():
    """Liidan isikukoodile kontrollkoodi juurde"""
    ssn = "".join(isikukood() + [getCode()])
    return ssn






if __name__ == "__main__":
    print(isik())