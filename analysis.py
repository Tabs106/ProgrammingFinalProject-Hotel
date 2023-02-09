# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:00:24 2023

@author: Hassanat Awodipe
"""

import pandas as pd
from utils import AdrStats, ReservationStatus


def analyse_adr(bookings):
    adr_stats = AdrStats(bookings)
    adr_stats.summary_csv('Submission/datasets/adr_summary.csv')
    adr_stats.plot_fig('Submission/plots/distribution_of_ADR.pdf')

    
def analyse_reservation_status(bookings):
    reservation_data = ReservationStatus(bookings)
    reservation_data.summary_csv('Submission/datasets/res_status.csv')
    reservation_data.plot_fig('Submission/plots/reservation status.pdf')
    
def all_analysis(bookings):
    analyse_adr(bookings)
    analyse_reservation_status(bookings)
    

if __name__ == "__main__":
    hotel_data = pd.read_csv(r'Submission/datasets/clean_hotel.csv', encoding='utf-8')
    all_analysis(hotel_data)
    
