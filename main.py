# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import menu


data_path = 'data/klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu.zvol_akci()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
