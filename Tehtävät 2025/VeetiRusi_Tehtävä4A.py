import random

def LuoKayttajatunnus():

    max_nmr = 999

    etu=input("Etunimi:")
    suk=input("Sukunimi:")
    etu_k=etu[:3]
    suk_k=suk[:3]

    nro = F"{random.randint(1, max_nmr)}"
    
    return (etu_k.lower()+suk_k.lower()+nro)

print("Luo Käyttäjätunnus")
kayttajatunnus=LuoKayttajatunnus()
print("\nKäyttäjätunnus")
print(kayttajatunnus)