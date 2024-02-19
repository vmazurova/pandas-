import pandas as pd
import matplotlib.pyplot as plt

class TemperatureAnalyzer:
    def __init__(self, data):
        self.data = data

    def seasonal_changes(self):
        seasonal_data = self.data.groupby(self.data['měsíc']).mean()
        print("Seasonal Changes:")
        print(seasonal_data)

    def detect_temperature_anomalies(self):
        anomaly_threshold = 2
        mean_temp = self.data['T-AVG'].mean()
        anomalies = self.data[(self.data['T-AVG'] > mean_temp + anomaly_threshold * self.data['T-AVG'].std()) |
                              (self.data['T-AVG'] < mean_temp - anomaly_threshold * self.data['T-AVG'].std())]
        print("Temperature Anomalies:")
        print(anomalies)

    def plot_avg_temp(self, start_year, end_year):
        filtered_data = self.data[(self.data)["rok"] >= start_year & (self.data["rok"] <= end_year)]
        annual_avg_temp = filtered_data.groupby("rok")["T-AVG"].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(annual_avg_temp.index, annual_avg_temp.values, marker="o", linestyle="-", color="b")
        plt.title(f'Prumerne rocni teplotz mezi roky {start_year} a {end_year}')
        plt.xlabel("rok")
        plt.ylabel("prumerna teplota")
        plt.grid(True)
        # Set x-axis limits to the specified range of years
        plt.xlim(start_year, end_year)
        plt.show()

    def plot_daily_temperature_trends(self, year):
        # Filtrujeme data pro zadaný rok
        year_data = self.data[self.data['rok'] == year]

        # Vykreslení denních teplotních trendů pro zadaný rok
        plt.figure(figsize=(10, 6))
        plt.plot(year_data.index, year_data['TMI'], label='Min Teplota', color='blue')
        plt.plot(year_data.index, year_data['TMA'], label='Max Teplota', color='red')
        plt.xlabel('Datum')
        plt.ylabel('Teplota (°C)')
        plt.title(f'Denní teplotní trendy pro rok {year}')
        plt.legend()
        plt.grid(True)
        plt.show()




