# by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# define plot parameters
order = ['City Hotel', 'Resort Hotel']
color = sns.color_palette()[0]


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
        data_wo = self.bookings.drop(self.bookings[self.bookings['adr'] > 5000].index)  # remove outlier adr

        plt.figure(figsize=(8, 6))
        ax = sns.violinplot(data=data_wo, x='hotel', y='adr', order=order, color=color);

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.xlabel('Hotel', fontsize=10)
        plt.ylabel('ADR', fontsize=10)
        plt.title('Distribution of ADR', fontsize=16)

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
        plt.xlabel('Hotel')
        plt.title('Reservation Status', fontsize=16)
        plt.legend(frameon=False)

        plt.savefig(filename)
        plt.close()

    def summary_csv(self, filename):
        reservation_data = self.compute_stats()
        reservation_data.to_csv(filename, index=False)


class LengthStats:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def compute_stats(self):
        self.bookings['full_length'] = self.bookings['stays_in_weekend_nights'] + self.bookings['stays_in_week_nights']
        length = self.bookings.loc[self.bookings['arrival_date'] >= '2016-01-01']
        return length

    def plot_fig(self, filename):
        plt.figure(figsize=(12, 8))
        l_data = self.compute_stats()
        x = self.bookings['arrival_date'].dt.month
        ax = sns.lineplot(x=x, y="full_length", hue="hotel", errorbar=None, data=l_data)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xticks([2, 4, 6, 8, 10, 12], ['Feb', 'Apr', 'Jun', 'Aug', 'Oct', 'Dec'])

        plt.xlabel("Month")
        plt.ylabel("Total number of nights")
        plt.title("Length of Stay", fontsize=16)
        plt.legend(frameon=False)

        plt.savefig(filename)
        plt.close()

    def summary_csv(self, filename):
        length_stay_16_17 = self.compute_stats()
        length_stay_16_17['year'] = length_stay_16_17['arrival_date'].dt.year
        length_stay_16_17['month'] = length_stay_16_17['arrival_date'].dt.month
        length_stay_16_17 = length_stay_16_17.groupby(['year', 'hotel', 'month'])['full_length'].mean()
        length_stay_16_17 = pd.DataFrame(length_stay_16_17).reset_index()
        length_stay_16_17.to_csv(filename)


class Countries:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def country_stats(self):
        origin_counts = self.bookings['country'].value_counts(dropna=False)[:10].reset_index()
        origin_counts.rename(columns={'index': 'country', 'country': 'count'}, inplace=True)

        return origin_counts

    def plot_top_countries(self, filename):
        y = self.country_stats()['country']
        x = self.country_stats()['count']

        ax = sns.barplot(x=x, y=y, color=color)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.ylabel('Country')
        plt.xlabel('Number of bookings per country')
        plt.title('Top 10 Countries by Number of Guests', fontsize=16)

        plt.savefig(filename)
        plt.close()

    def csv_saver(self, filename):
        origin_counts = self.country_stats()
        origin_counts.to_csv(filename)


class Families:
    def __init__(self, hotel_data):
        self.bookings = hotel_data

    def is_family(self, adults, children, babies):
        return (adults >= 1) & ((children >= 1) | (babies >= 1))

    def plot_families(self, filename):
        self.bookings['is_family'] = self.bookings.apply(
            lambda row: self.is_family(row['adults'], row['children'], row['babies']), axis=1)

        families = self.bookings['is_family'].value_counts()

        values = families
        labels = ['Non-families', 'Families']
        explode = (0, 0.1)
        plt.pie(values, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
        plt.title('Pie Chart of Families', fontsize=16)

        plt.savefig(filename)
        plt.close()
