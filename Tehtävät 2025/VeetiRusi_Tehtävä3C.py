import random
import time

voittorivi=[6,9,18,23,31,33,38]
maara_nmr=len(voittorivi)
max_nmr=40
yrit=0

alku=time.time()

while True:
    yrit+=1
    rivi=[]
    while len(rivi) < maara_nmr:
        nro=random.randint(1, max_nmr)
        if nro not in rivi:
            rivi.append(nro)
    rivi.sort()
    if rivi==sorted(voittorivi):
        break

loppu=time.time()
aika=loppu-alku

print("\n    LOTTOTULOS ")
print(f"Voittorivi: {voittorivi}")
print(f"Sama rivi {yrit} arvauksella.")
print(f"Kulunut aika: {aika:.2f}s")
print(f"Kustannus 1€ = rivi: {yrit}€")