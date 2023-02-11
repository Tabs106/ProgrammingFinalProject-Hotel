import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_countries(df, column_name):
    """This function plots the bar plot of the top 10 values of a given column in a DataFrame"""
    origin_counts = df['country'].value_counts(dropna=False)[:10]
    sns.barplot(x=origin_counts.index, y=origin_counts.values,color=sns.color_palette()[0])
    plt.xlabel('Country')
    plt.ylabel('Number of Guests')
    plt.title('Top 10 Guests by Country')
    plt.show()
    
def plot_families(df):
    df['total_guests'] = df['adults'] + df['children'] + df['babies']
    df['families'] = (df['total_guests'] >= 2).astype(int)
    families_counts = df['families'].value_counts(dropna=False)
    sns.barplot(x=families_counts.index, y=families_counts.values)
    plt.xlabel('Family Bookings')
    plt.ylabel('Number of Bookings')
    plt.title('Number of Family Bookings')
    plt.show()   


