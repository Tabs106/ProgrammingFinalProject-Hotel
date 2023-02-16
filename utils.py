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

        count_adr_city = self.bookings.groupby('hotel')['adr'].size()[0]
        count_adr_resort = self.bookings.groupby('hotel')['adr'].size()[1]

        sum_adr_city = self.bookings.groupby('hotel')['adr'].sum()[0]
        sum_adr_resort = self.bookings.groupby('hotel')['adr'].sum()[1]

        adr_stats = self.bookings.groupby('hotel')['adr'].describe().reset_index()
        adr_stats.loc[[0, 1], 'count'] = [sum_adr_city, sum_adr_resort]
        adr_stats.loc[[0, 1], 'percentage'] = [str(round((count_adr_city / len_data) * 100, 2)) + '%',
                                               str(round((count_adr_resort / len_data) * 100, 2)) + '%']
        adr_stats.rename(columns={'count': 'sum'}, inplace=True)

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

# Tabatha's codes here #
