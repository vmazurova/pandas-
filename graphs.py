import pandas as pd
import matplotlib.pyplot as plt

class TemperatureAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze_seasonal_changes(self, year):
        # Filtrujeme data pro zadaný rok
        yearly_data = self.data[self.data['rok'] == year]

        # Vytvoříme sloupec s měsícem
        yearly_data.loc[:, 'měsíc'] = yearly_data['měsíc']

        # Seskupíme data podle měsíce a spočítáme průměrnou teplotu
        monthly_avg_temp = yearly_data.groupby('měsíc')['T-AVG'].mean()

        # Vykreslíme graf sezónních změn
        plt.plot(monthly_avg_temp.index, monthly_avg_temp.values, marker='o')
        plt.title(f"Sezónní změny teploty v roce {year}")
        plt.xlabel("Měsíc")
        plt.ylabel("Průměrná teplota (°C)")
        plt.xticks(range(1, 13),
                   ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září', 'říjen',
                    'listopad', 'prosinec'], rotation=45)
        plt.grid(True)
        plt.show()

    def detect_temperature_anomalies(self, start_year, end_year):
        anomaly_threshold = 2  # Práh pro detekci anomálií
        anomalies = pd.DataFrame()

        for year in range(start_year, end_year + 1):
            annual_data = self.data[self.data['rok'] == year]
            mean_temp = annual_data['T-AVG'].mean()
            std_temp = annual_data['T-AVG'].std()
            upper_threshold = mean_temp + anomaly_threshold * std_temp
            lower_threshold = mean_temp - anomaly_threshold * std_temp

            year_anomalies = annual_data[(annual_data['T-AVG'] > upper_threshold) | (annual_data['T-AVG'] < lower_threshold)]
            if not year_anomalies.empty:
                year_anomalies.loc[:, 'rok'] = year  # Přidání sloupce s rokem anomálie
                anomalies = pd.concat([anomalies, year_anomalies])

        return anomalies

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




