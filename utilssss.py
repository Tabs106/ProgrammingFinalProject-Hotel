#by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

order = ['City Hotel', 'Resort Hotel']
color = sns.color_palette()[0]

class LengthStats:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def compute_stats(self):
        self.bookings['full_length'] = self.bookings['stays_in_weekend_nights']+self.bookings['stays_in_week_nights']
        length = self.bookings.loc[self.bookings['arrival_date_year'] >= 2016]
        return length

    def plot_fig(self, filename):
        plt.figure(figsize=(12,6))
        l_data = self.compute_stats()

        sns.lineplot(x="arrival_date_month", y="full_length",
            hue="hotel",ci=None,data=l_data);

        plt.xlabel("Month")
        plt.ylabel("Length of Stay")
        plt.title("Length of Stay")

        plt.savefig(filename)
        plt.close()
        
