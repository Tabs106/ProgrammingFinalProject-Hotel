import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_countries(df, column_name, title, x_label, y_label):
    """This function plots the bar plot of the top 10 values of a given column in a DataFrame"""
    origin_counts = df[column_name].value_counts(dropna=False)
    sns.barplot(x=origin_counts.index[:10], y=origin_counts.values[:10])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
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


