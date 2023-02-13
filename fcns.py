import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_countries(df, column_name):
    ###This function plots the bar plot of the top 10 values of a given column in a DataFrame#
    origin_counts = df['country'].value_counts(dropna=False)[:10]
    sns.barplot(x=origin_counts.index, y=origin_counts.values,color=sns.color_palette()[0])
    plt.xlabel('Country')
    plt.ylabel('Number of Guests')
    plt.title('Top 10 Guests by Country')
    plt.show()
    
def plot_families(df):
    def is_family(adults, children, babies):
        return adults >= 1 and (children >= 1 or babies >= 1)

df['is_family'] = df.apply(lambda row: is_family(row['adults'], row['children'], row['babies']), axis=1)

 families = df['is_family'].sum()

 non_families = df.shape[0] - families
 values = [families, non_families]

labels = ['Families', 'Non-families']
 plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()



