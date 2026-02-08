print("Miinapeli")
print("ohjeet Liiku vasemmalle=1, suoraan=2 ja oikealle=3")
print("liiku")

import time

eka = int(input())
if eka == 1 or eka == 3:
    print("Räjähdit")
    print("Hävisit pelin")
    time.sleep(2)
    exit()
elif eka == 2:
    print("Liikuit eteenpäin")
    if  eka == 2:
        print("liiku")
elif eka == 4:
    print("Et astunut miinakentälle")
    if eka == 4:
        print("Voitit")
        time.sleep(3)
        exit()

toka = int(input())
if toka == 1:
    print("Liikuit eteenpäin")
    if  toka == 1:
        print("liiku")
elif toka == 2 or toka == 3:
    print("Räjähdit")
    print("Hävisit pelin")
    time.sleep(2)
    exit()

kol = int(input())
if kol == 1 or kol == 3:
    print("Räjähdit")
    print("Hävisit pelin")
    time.sleep(2)
    exit()
elif kol == 2:
    print("Liikuit eteenpäin")
    if  kol == 2:
        print("liiku")

nel = int(input())
if nel == 1 or nel == 2:
    print("Räjähdit")
    print("Hävisit pelin")
    time.sleep(2)
    exit()
elif nel == 3:
    print("Pääsit posi miinakentältä")
    if  nel == 3:
        print("Voitit")
        time.sleep(3)
        exit()
