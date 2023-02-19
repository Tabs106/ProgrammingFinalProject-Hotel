# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:13:54 2023

@author: Utente
"""
import seaborn as sns
import matplotlib.pyplot as plt

class Countries:
    def __init__(self, hotel_data):
        self.bookings = hotel_data
   
    def country_stats(self):
        origin_counts = self.bookings['country'].value_counts(dropna=False)[:10].reset_index()
        origin_counts.rename(columns={'index':'country','country':'count'},inplace=True)
        
        return origin_counts
    
    def plot_top_countries(self, filename):
        y = self.country_stats()['country']
        x = self.country_stats()['count']
        
        ax = sns.barplot(x=x, y=y, color=sns.color_palette()[0])
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.xlabel('Country')
        plt.ylabel('Number of bookings per country')
        plt.title('Top 10 Guests by Country', fontsize=16)
        
        plt.savefig(filename)
        plt.close()
        
    def csv_saver(self, filename):
        origin_counts=self.country_stats()
        origin_counts.to_csv(filename)
        
class Families:
    def __init__(self, hotel_data):
        self.bookings = hotel_data
        
    def is_family(self, adults, children, babies):
        return (adults >= 1) & ((children >= 1) | (babies >= 1))
    
    def plot_families(self, filename):
        adults = self.bookings['adults']
        children = self.bookings['children']
        babies = self.bookings['babies']
        is_family = self.is_family(adults, children, babies)
        self.bookings['is_family'] = self.bookings.apply(lambda row: self.is_family(row['adults'], row['children'], row['babies']), axis=1)

        families= self.bookings['is_family'].sum()
        non_families = self.bookings.shape[0] - families
        
        values = [families, non_families]
        labels = ['Families', 'Non-families']
        
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        
        plt.savefig(filename)
        plt.close()
         
    def csv_saver(self, filename):
        adults = self.bookings['adults']
        children = self.bookings['children']
        babies = self.bookings['babies']
        is_family=self.is_family(adults, children, babies)
        is_family.to_csv(filename)
        
        
        
        
        
        