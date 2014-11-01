#Isikukoodi genereerimise programm. Programm ei arvesta liigaastaga.

import random

# Panin for tsükkli sisse, et korraga rohkem tulemusi saada testimiseks.
for turn in range(100):
  turn + 1
  

  #Defineerin 11 kohta isikukoodile.
  ik_1 = 0

  ik_2 = 0
  ik_3 = 0

  ik_4 = 0
  ik_5 = 0

  ik_6 = 0
  ik_7 = 0

  ik_8 = 0
  ik_9 = 0
  ik_10 = 0

  ik_11 = 0



  #Sugu
  ik_1 = random.randint(1,7)

  #Aasta
  ik_2 = random.randint(0,9)
  ik_3 = random.randint(0,9)

  # 30 päeva kuus
    # 04,06,11
    
  # 31 dpäeva kuus
    #01, 03, 05, 07, 08, 09, 10, 12
  
  # 28 päeva kuus
    #02

  #Kuu
  ik_4 = random.randint(0,1)
  if ik_4 == 0:
    ik_5 = random.randint(1,9)
  else:
    ik_5 = random.randint(0,2)

  #Päev
  if ik_5 == 1 or ik_5 == 3 or ik_5 == 5 or ik_5 == 7 or ik_5 == 8 or ik_5 == 9:
    ik_6 = random.randint(0,3)
    if ik_6 == 0:
      ik_7 = random.randint(1,9)
    elif ik_6 == 3:
      ik_7 = random.randint(0,1)
    else:
      ik_7 = random.randint(0,9)
  elif ik_5 == 4 or ik_5 == 6:
    ik_6 = random.randint(0,3)
    if ik_6 == 0:
      ik_7 = random.randint(1,9)
    elif ik_6 == 3:
      ik_7 = 0
    else:
      ik_7 = random.randint(0,9)
  elif ik_5 == 2:
    ik_6 = random.randint(0,2)
    if ik_6 == 0:
      ik_7 = random.randint(1,8)
  elif ik_4 == 1 and ik_5 == 1:
    ik_6 = random.randint(0,3)
    if ik_6 == 0:
      ik_7 = random.randint(1,9)
    elif ik_6 == 3:
      ik_7 = 0
    else:
      ik_7 = random.randint(0,9)
  elif ik_4 == 1 and ik_5 == 0 or ik_5 == 2:
    ik_6 = random.randint(0,3)
    if ik_6 == 0:
      ik_7 = random.randint(1,9)
    elif ik_6 == 3:
      ik_7 = random.randint(0,1)
    else:
      ik_7 = random.randint(0,9)
  elif ik_4 == 1 and ik_5 == 1:
    ik_6 = random.randint(0,3)
    if ik_6 == 0:
      ik_7 = random.randint(1,9)
    elif ik_6 == 3:
      ik_7 = 0
    else:
      ik_7 = random.randint(0,9)
    
    

  #Sequence Code
  ik_8 = random.randint(0,9)
  ik_9 = random.randint(0,9)
  ik_10 = random.randint(0,9)

  #Kontrollnumber
  #Algoritm:
    # Liidetakse kokku esimese kümne numbri korrutised igale arvule vastava
    # järjekorranumbriga (va 10. number, kus kordaja on taas 1) ning leitakse saadud
    # summast jääk jagamisel 11-ga. See jääk ongi kontrollnumber.
    # Kui jääk on võrdne kümnega, tehakse arvutus uuesti ning võetakse teguriteks, millega 
    #isikukoodi numbreid korrutada, vastavalt 3, 4, 5, 6, 7, 8, 9, 1, 2, 3. Leitaks jääk
    #jagamisel 11-ga. Ja see ongi kontrollnumber.

    #Kui jääk jälle võrdub 10ga, siis määratakse kontrollnumbriks 0.


  summa = 1 * ik_1 + 2 * ik_2 + 3 * ik_3 + 4 * ik_4 + 5 * ik_5 + 6 * ik_6 + 7 *ik_7 + 8 * ik_8 + 9 * ik_9 +  1 * ik_10
  if summa % 11 < 10:
    ik_11 = summa % 11

  elif summa % 11 == 10:
    summa1 = 3 * ik_1 + 4 * ik_2 + 5 * ik_3 + 6 * ik_4 + 7 * ik_5 + 8 * ik_6 + 9 *ik_7 + 1 * ik_8 + 2 * ik_9 +  3 * ik_10
    if summa1 % 11 < 10:
      ik_11 = summa1 % 11

    elif summa1 % 11 == 10:
      ik_11 = 0


  isikukood = "%s%s%s%s%s%s%s%s%s%s%s" % (ik_1,ik_2,ik_3,ik_4,ik_5,ik_6,ik_7,ik_8,ik_9,ik_10,ik_11)


  print ("Isikukood on: ", isikukood)




