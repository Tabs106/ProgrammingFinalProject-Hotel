#by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe
import pandas as pd

from utils import Countries, Families

def analyse_country(data):
    country = Countries(data)
    country.plot_top_countries('Top_10_countries.pdf')
    country.csv_saver('Top_10_countries.csv')
    
def analyse_families(data):
    family = Families(data)
    family.plot_families('Families_or_not.pdf')
    family.csv_saver('Families_or_not.csv')
    
if __name__ == '__main__':
    hotel_data = pd.read_csv(r'hotel_bookings.csv', encoding='utf-8')
    analyse_country(hotel_data)
    analyse_families(hotel_data)
    
