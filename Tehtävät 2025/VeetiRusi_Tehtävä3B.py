lista = []

print("Ostoslista")
print("Kun olet valmis kirjoita 'valmis'")
while True:
    tuot = input("Tuote:")
    if tuot.lower() == "valmis":
        break
    lista.append(tuot)
lista.sort()
print("\nOstoslistasi:")
for tuot in lista:
    print(tuot)