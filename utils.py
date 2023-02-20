<<<<<<< HEAD
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

order = ['City Hotel', 'Resort Hotel']
color = sns.color_palette()[0]

# Tamsir's codes here #

class AdrStats:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def compute_stats(self):
        len_data = self.bookings.shape[0]

        count_city = self.bookings.groupby('hotel').size()[0]
        count_resort = self.bookings.groupby('hotel').size()[1]

        sum_adr_city = self.bookings.groupby('hotel')['adr'].sum()[0]
        sum_adr_resort = self.bookings.groupby('hotel')['adr'].sum()[1]

        adr_stats = self.bookings.groupby('hotel')['adr'].describe().reset_index()
        adr_stats.loc[[0, 1], 'percentage'] = [str(round((count_city / len_data) * 100, 2)) + '%',
                                               str(round((count_resort / len_data) * 100, 2)) + '%']
        adr_stats.loc[[0, 1], 'sum'] = [sum_adr_city, sum_adr_resort]

        return adr_stats

    def plot_fig(self, filename):
        data_wo = self.bookings.drop(self.bookings[self.bookings['adr'] > 5000].index)

        plt.figure(figsize=(8, 6))
        ax = sns.violinplot(data=data_wo, x='hotel', y='adr', order=order, color=color);

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.xlabel('Hotel', fontsize=10)
        plt.ylabel('ADR', fontsize=10)
        plt.title('Distribution of ADR', fontsize=16)
        plt.title('Distribution of ADR')

        plt.savefig(filename)
        plt.close()

    def summary_csv(self, filename):
        adr_stats = self.compute_stats()
        adr_stats.to_csv(filename, index=False)


class ReservationStatus:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def compute_stats(self):
        reservation_data = self.bookings.groupby(['hotel', 'reservation_status'],
                                                 as_index=False).size().sort_values(by=['hotel', 'size'],
                                                                                    ascending=False)

        return reservation_data

    def plot_fig(self, filename):
        plt.figure(figsize=(8, 6))

        ax = sns.countplot(data=self.bookings, x='hotel', hue='reservation_status', order=order)
        for container in ax.containers:
            ax.bar_label(container)
        ax.axes.get_yaxis().set_visible(False)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        plt.title('Reservation Status', fontsize=16)
        plt.legend(frameon=False)

        plt.savefig(filename)
        plt.close()

    def summary_csv(self, filename):
        reservation_data = self.compute_stats()
        reservation_data.to_csv(filename, index=False)

<<<<<<< HEAD

class CountryStats:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def countries_stats(self):
        origin_counts = self.bookings['country'].value_counts(dropna=False)[:10].reset_index()

        # change column name
        origin_counts.rename(columns={'index': 'country', 'country': 'count'}, inplace=True)
        return origin_counts

    def plot_top_countries(self, filename):
        plt.figure(figsize=(8, 6))

        y = self.countries_stats()['country']
        x = self.countries_stats()['count']
        ax = sns.barplot(x=x, y=y, color=color)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # plt.xlabel()
        # plt.ylabel()
        # plt.title()

        plt.savefig(filename)
        plt.close()

    def summary_csv(self, filename):
        top_10_countries = self.countries_stats()
        top_10_countries.to_csv(filename, index=False)


class Families:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def families_stats(self):
        is_family = []
        for adults, children, babies in zip(self.bookings['adults'], self.bookings['children'],
                                            self.bookings['children']):
            if (adults > 0) and (children > 0) and (babies > 0):
                family = 1
            elif (adults > 0) and (children > 0) and (babies < 0):
                family = 1
            elif (adults > 0) and (children < 0) and (babies > 0):
                family = 1
            else:
                family = 0
            is_family.append(family)

        self.bookings['families'] = is_family
        families = self.bookings['families'].value_counts()

        return families

    def plot_families(self, filename):

        plt.figure(figsize=(6,6))
        sizes = self.families_stats()
        explode = (0, 0.1)
        plt.pie(sizes, explode=explode, labels=['', 'Family'], autopct='%1.1f%%', shadow=True, startangle=90)
        plt.title('')

        plt.savefig(filename)
        plt.close()

=======
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
        
>>>>>>> main
=======
# Tabatha's codes here #
>>>>>>> f49e8656b7b7d6da3e66b54fed29d436601d35eb
