import menu
import main

class WeatherStatistics:
    def __init__(self, dataset):
        """
        Inicializuje instanci třídy WeatherStatistics s datasetem.
        param dataset: pandas DataFrame obsahující meteorologická data.
        """
        self.dataset = dataset

    def highest_temperature(self, year):
        """
        Vrátí nejvyšší teplotu zaznamenanou v zadaném roce.
        param year: Rok, pro který se má najít nejvyšší teplota.
        return: Nejvyšší teplota v zadaném roce.
        """
        annual_data = self.dataset[self.dataset['rok'] == year]
        highest_temp = annual_data['TMA'].max()
        return highest_temp

    def lowest_temperature(self, year):
        """
        Vrátí nejnižší teplotu zaznamenanou v zadaném roce.
        param year: Rok, pro který se má najít nejnižší teplota.
        return: Nejnižší teplota v zadaném roce.
                """
        annual_data = self.dataset[self.dataset['rok'] == year]
        lowest_temp = annual_data['TMI'].min()
        return lowest_temp

    def average_temperature(self, year):
        """
        Vypočítá a vrátí průměrnou teplotu pro zadaný rok.
        param year: Rok, pro který se má vypočítat průměrná teplota.
        return: Průměrná teplota v zadaném roce zaokrouhlená na dvě desetinná místa.
                """
        annual_data = self.dataset[self.dataset['rok'] == year]
        return round(annual_data['T-AVG'].mean(), 2)

    def monthly_averages(self, year):
        """
        Vypočítá průměrné měsíční teploty pro zadaný rok.
        param year: Rok, pro který se mají vypočítat měsíční průměry.
        return: pandas Series obsahující průměrné teploty pro každý měsíc v zadaném roce, zaokrouhlené na dvě desetinná místa.
              """
        annual_data = self.dataset[self.dataset['rok'] == year]
        monthly_avg = annual_data.groupby('měsíc')['T-AVG'].mean().round(2)
        return monthly_avg

    def temperature_trends(self, start_year, end_year):
        """
        Analyzuje teplotní trendy mezi zadanými roky.
        param start_year: Počáteční rok pro analýzu trendů.
        param end_year: Koncový rok pro analýzu trendů.
        return: pandas Series obsahující průměrné roční teploty pro každý rok v rozmezí, zaokrouhlené na dvě desetinná místa.
                """
        trend_data = self.dataset[(self.dataset['rok'] >= start_year) & (self.dataset['rok'] <= end_year)]
        annual_avg = trend_data.groupby('rok')['T-AVG'].mean().round(2)
        return annual_avg

