print("Syötä numero 1:")
eka = float(input())
print("Syötä numero 2:")
toka = float(input())
print("summa=1, erotus=2, tulo=3, osamäärä=4")
lasku = int(input())
if lasku == 1:
    print("summa", (eka+toka))
elif lasku == 2:
    print("erotus", (eka-toka))
elif lasku == 3:
    print("tulo", (eka*toka))
elif lasku == 4:
    if eka !=0:
        print("osamäärä", (eka/toka))
    else:
        print("Nollaa ei voi jakaa")
else:
    print("Virheellinen valinta")