num=[]

print("Syötä numero (tyhjä=lopettaa)")

while True:
    syot=input("")
    if syot=="":
        break
    numr=int(syot)
    num.append(numr)

järj=[]
while num:
    pien=num[0]
    for n in num:
        if n<pien:
            pien=n
    järj.append(pien)
    num.remove(pien)

print("Järjestetyt:", järj)