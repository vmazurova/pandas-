import pandas as pd
import temp
import temp


def load_data():
    data_path = 'data/klementinum.xlsx'
    data_sheet_name = 'data'
    temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)
    return temperature_data


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
    data = load_data()
    analytik = temp.WeatherStatistics(data)
    while True:
        vyber = menu()
        if vyber == "1":
            while True:
                try:
                    rok = int(input("Zadejte rok: "))
                    prumerna_teplota = analytik.average_temperature(rok)
                    print(f"Průměrná teplota v roce {rok} je: {prumerna_teplota}°C")
                    break
                except ValueError:
                    print("Nebylo zadano platne cislo, zadej znova")
                    break

        elif vyber == "2":
            while True:
                try:
                    rok = int(input("Zadej rok pro vypocet:"))
                    max_temp = analytik.highest_temperature(rok)
                    min_temp = analytik.lowest_temperature(rok)
                    print(f"Maximální teplota v roce {rok}: {max_temp}°C")
                    print(f"Minimální teplota v roce {rok}: {min_temp}°C")
                    break
                except ValueError:
                    print("Nebylo zadano platne cislo, zadej znova")
                    break

        elif vyber == "3":
            try:
                rok = int(input("Zadejte rok pro zobrazení měsíčních průměrů: "))
                monthly_avg = analytik.monthly_averages(rok)
                print(f"Měsíční průměrné teploty v roce {rok}:\n{monthly_avg}")
                break
            except ValueError:
                print("Nebylo zadáno platne cislo, napis znova.")
                break

        elif vyber == "4":
            try:
                start_year = int(input("Zadejte počáteční rok: "))
                end_year = int(input("Zadejte koncový rok: "))
                trends = analytik.temperature_trends(start_year, end_year)
                print(f"Teplotní trendy od roku {start_year} do roku {end_year}:\n{trends}")
                break
            except ValueError:
                print("Nebylo zadáno platne cislo, napis znova.")
                break
        elif vyber == "5":
            pass
        elif vyber == "6":
            pass
        elif vyber == "7":
            pass
        elif vyber == "8":
            pass
        elif vyber == "9":
            pass
        elif vyber == "0":
            print("Konec")
            break
        else:
            print("Nebylo zadano cislo")
            continue
