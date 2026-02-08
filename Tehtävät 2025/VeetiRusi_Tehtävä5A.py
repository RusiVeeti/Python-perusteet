from datetime import date, datetime

def päiv_joul(lpäiv):
    joulaat = date(lpäiv.year, 12, 24)
    if lpäiv > joulaat:
        joulaat = date(lpäiv.year + 1, 12, 24)
    return (joulaat - lpäiv).days

def vali():
    print("Valitse toiminto:")
    print("1. Kuinka monta päivää on jouluaattoon tästä hetkestä.")
    print("2. Kuinka monta päivää on jouluaattoon omasta syntymäpäivästäsi.")
    
    valinta = input("Anna valintasi (1 tai 2): ")
    
    if valinta == "1":
        tänään = date.today()
        päiv = päiv_joul(tänään)
        print(f"Jouluaattoon on {päiv} päivää.")
    
    elif valinta == "2":
        syntymä = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
        try:
            syntymä = datetime.strptime(syntymä, "%d.%m.%Y").date()
            päiviä = päiv_joul(syntymä)
            print(f"Jouluaattoon on {päiviä} päivää syntymäpäivästäsi.")
        except ValueError:
            print("Virheellinen päivämäärämuoto! Käytä muotoa pp.kk.vvvv.")
    else:
        print("Virheellinen valinta. Valitse 1 tai 2.")

vali()