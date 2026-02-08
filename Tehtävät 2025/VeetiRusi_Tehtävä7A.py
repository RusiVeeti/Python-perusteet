print("Anna kaksi numeroa")

yk = int(input("Luku 1: "))
kak = int(input("Luku 2: "))

if yk>=kak:
    print("Ykkös luku on liian iso")

else:
    
    tul=(yk/kak)*100
    print(f"\n=>Luku {yk} on {tul:.0f}% luvusta {kak}")
    print(f"{tul:.0f}%")
    
    palk_pit = 20 
    tayt=int((tul/100)*palk_pit)
    
    palk="⚫"*tayt+"⚪"*(palk_pit-tayt)
    print(f"|{palk}|")