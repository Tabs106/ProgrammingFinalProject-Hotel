# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:25:31 2023

@author: Hassanat Awodipe
"""
import pandas as pd
from preprocessing import clean_data
from analysis import all_analysis


if __name__ == "__main__":
    hotel_data = pd.read_csv(r'hotel_bookings.csv', encoding='utf-8')
    clean_data(hotel_data)
    all_analysis(hotel_data)