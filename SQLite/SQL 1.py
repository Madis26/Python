__author__ = 'madis'

import sqlite3
import time
from datetime import datetime

def kasutaja_kuupaev():
    """Tahan saada kuupäevast alguse, et kasutada LIKE sql'is"""
    timestamp_listi = []
    kasutaja_sisestab = input("Sisesta kuupäev formaadis pp.kk.aaaa: ")
    kuupaeva_format = datetime.strptime(kasutaja_sisestab, "%d.%m.%Y")
    kuuapaev_timestamp = str((time.mktime(kuupaeva_format.timetuple())))

    for i in kuuapaev_timestamp:
        timestamp_listi.append(i)

    timestamp_algus = timestamp_listi[5]
    kuupaev = str("".join(timestamp_algus))
    return kuupaev

def siseta_kasutaja():
    kasutaja_sisestab_kasutaja = input("Sisesta autor: ")
    return kasutaja_sisestab_kasutaja

conn = sqlite3.connect('main.db')
c= conn.cursor()

def loen_baasist_ridu():
    sql = ("SELECT x.body_xml FROM messages x where x.timestamp LIKE '%s' and x.from_dispname LIKE '%s'" % (kasutaja_kuupaev() + '%', siseta_kasutaja()))
    for row in c.execute(sql):
        print(row)
    c.close()

#print (c.fetchone())
if __name__ == "__main__":
    print(loen_baasist_ridu())

