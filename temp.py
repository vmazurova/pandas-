

import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import menu
import main

data_path = 'data/klementinum.xlsx'
data_sheet_name = 'data'
temperature_data = pd.read_excel(data_path, sheet_name=data_sheet_name)

class TemperatureAnalytics:
    def __init__(self, data):
        self.data = data

    def get_average_temperature(self, year_in):
        year_in = input("Zadej rok pro vypocet rocniho prumeru")
        yearly_data = self.data[self.data['rok'] == year_in]
        return yearly_data['T-AVG'].mean()

    def get_max_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        max_temp = yearly_data['TMA'].max()
        date_of_max_temp = yearly_data[yearly_data['TMA'] == max_temp][['rok', 'měsíc', 'den']].iloc[0]
        return max_temp, date_of_max_temp

    def get_min_temperature(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        min_temp = yearly_data['TMI'].min()
        date_of_min_temp = yearly_data[yearly_data['TMI'] == min_temp][['rok', 'měsíc', 'den']].iloc[0]
        return min_temp, date_of_min_temp

    def get_monthly_averages(self, year):
        yearly_data = self.data[self.data['rok'] == year]
        return yearly_data.groupby('měsíc')['T-AVG'].mean()

    def analyze_temperature_trends(self, start_year, end_year):
        trend_data = self.data[(self.data['rok'] >= start_year) & (self.data['rok'] <= end_year)]
        annual_average_temperatures = trend_data.groupby('rok')['T-AVG'].mean()
        return annual_average_temperatures

    def plot_avg_temp(self, start_year, end_year):
        filtered_data = self.data[(self.data)["rok"] >= start_year & (self.data["rok"] <= end_year)]
        annual_avg_temp = filtered_data.groupby("rok")["T-AVG"].mean()
        from matplotlib import pyplot as plt
        plt.figure(figsize=(10,6))
        plt.plot(annual_avg_temp.index, annual_avg_temp.values, marker= "o", linestyle="-", color="b")
        plt.title(f'Prumerne rocni teplotz mezi roky {start_year} a {end_year}')
        plt.xlabel("rok")
        plt.ylabel("prumerna teplota")
        plt.grid(True)
        plt.show()




average_temp_2022 = TemperatureAnalytics.get_average_temperature()

