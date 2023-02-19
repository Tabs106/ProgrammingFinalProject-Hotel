#by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

import pandas as pd
from utils import AdrStats, ReservationStatus, CountryStats, Families


def analyse_length_stay(data):
    length = LengthStats(data)
    length.plot_families('Submission/plots/family_pie.pdf')


def all_analysis(data):
    analyse_length_stay(data)


if __name__ == "__main__":
    hotel_data = pd.read_csv(r'Submission/datasets/hotel_bookings_clean.csv', encoding='utf-8')
    all_analysis(hotel_data)