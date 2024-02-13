import pandas as pd
import main
import temp
def menu():
    print("1 - Zobrazit průměrnou teplotu pro zadaný rok")
    print("2 - Zobrazit minimální a maximální teplotu pro zadaný rok")
    print("3 - Zobrazit měsíční průměry pro zadaný rok")
    print("4 - Analyzovat teplotní trendy")
    print("5 - Analyzovat sezónní změny")
    print("6 - Detekovat teplotní anomálie")
    print("7 - Vykreslit průměrné roční teploty")
    print("8 - Vykreslit denní teplotní trendy")
    print("9 - Vykreslit minimální a maximální teploty pro konkrétní den")
    print("0 - Konec")
    vstup = input("Zadej akci:").upper()
    return vstup

def zvol_akci():
    while True:
        vyber = menu()
        if vyber == "1":
            temp.TemperatureAnalytics.get_average_temperature()
        if vyber == "2":
            pass
        if vyber == "3":
            pass
        if vyber == "4":
            pass
        if vyber == "5":
            pass
        if vyber == "6":
            pass
        if vyber == "7":
            pass
        if vyber == "8":
            pass
        if vyber == "9":
            pass
        if vyber == "0":
            print("Konec")
            break
        else:
            print("Nebylo zadano cislo")
            continue

zvol_akci()