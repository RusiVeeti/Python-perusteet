print("Anna sana")
san=input()

lop=""

for kir in san:
    if 'a'<=kir<= 'z':
        lop+=chr(ord(kir)-32)
    elif 'A'<=kir<= 'Z':
        lop+=chr(ord(kir)+32)
    else:
        lop+=kir

kään_san=""
for i in range(len(lop)-1,-1,-1):
    kään_san+=lop[i]

print(kään_san)