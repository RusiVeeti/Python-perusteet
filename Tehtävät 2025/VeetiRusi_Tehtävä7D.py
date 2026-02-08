txt=input("Anna teksti: ")

merklask={}
for merk in txt:
    if merk==" ":
        continue
    if merk in merklask:
        merklask[merk]+=1
    else:
        merklask[merk]=1

lista = []
for merk in merklask:
    lista.append([merk,merklask[merk]])

for i in range(len(lista)):
    for j in range(0,len(lista)-i-1):
        if lista[j][1]<lista[j+1][1]:
            lista[j],lista[j+1]=lista[j+1],lista[j]

top5={}
count=0
for i in range(5):
    top5[lista[i][0]] = lista[i][1]

print("Viisi yleisintä ja määrä:")
for merk in top5:
    print(f"'{merk}':{top5[merk]}")