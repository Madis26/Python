__author__ = 'madispiigli'
#Kirjutan isikukoodi faili. Andmed on valed. Pean Isikukoodi ülesannet paremaks kirjutama.

import Isikukood
import _csv
import csv

Forname = ""
Surname = ""
isikukood = []


cr = csv.reader(open("nimed.txt","r"))

def Kood():
    return Isikukood.isik()


def Forname():
    for row in cr:
        return row[0]

def Surname():
    for row in cr:
        return row[-1]

c = csv.writer(open("isikukood.csv", "w+"))

c.writerow(["SOCIAL_SECURITY_NUMBER","FORENAME","SURNAME","GENDER","DATE_OF_BIRTH"])


for i in range(10):
    c.writerow([Kood(),Forname(),Surname(),"M",str((Isikukood.getBirthDay().strftime('%d.%m.%Y')))])



