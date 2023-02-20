# by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

import pandas as pd
from utils import AdrStats, ReservationStatus, LengthStats, Countries, Families


def analyse_adr(data):
    adr_stats = AdrStats(data)
    adr_stats.summary_csv('Submission/datasets/adr_summary.csv')
    adr_stats.plot_fig('Submission/plots/distribution_of_ADR.pdf')


def analyse_reservation_status(data):
    reservation_data = ReservationStatus(data)
    reservation_data.summary_csv('Submission/datasets/res_status.csv')
    reservation_data.plot_fig('Submission/plots/reservation_status.pdf')


def analyse_top_countries(data):
    top_countries = Countries(data)
    top_countries.csv_saver('Submission/datasets/top_10_countries.csv')
    top_countries.plot_top_countries('Submission/plots/top_10_countries.pdf')


def analyse_families(data):
    families = Families(data)
    families.plot_families('Submission/plots/family_pie.pdf')


def analyse_length_stay(data):
    length = LengthStats(data)
    length.plot_fig('Submission/plots/length_of_stay.pdf')
    length.summary_csv('Submission/datasets/length_of_stay.csv')


def all_analysis(data):
    analyse_adr(data)
    analyse_reservation_status(data)
    analyse_length_stay(data)
    analyse_top_countries(data)
    analyse_families(data)


if __name__ == "__main__":
    hotel_data = pd.read_csv(r'Submission/datasets/clean_hotel.csv', encoding='utf-8')
    all_analysis(hotel_data)
