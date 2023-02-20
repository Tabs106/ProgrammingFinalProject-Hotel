#by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

#This section reads and cleans the given dataset, removing lines where it finds  blanks in important 
# information.

import pandas as pd


def replace_null(columnNames):
    #Replaces null values in given column to 0
    for c in columnNames:
        df[columnNames] = df[columnNames].fillna(0)

def drop_column(columnNames):
    #Removes the given columns
    for c in columnNames:
        df.drop(columnNames, axis=1, inplace=True)



#reads the csv
df = pd.read_csv('hotel_bookings.csv')

#replaces the null values in these columns to 0 as to not remove unintencional rows
replace_null(['agent','company','children'])

#removes all columns we will not be using 

#drops all rows that contain null variables
new_df = df.dropna()

#saves new data frame into csv file
new_df.to_csv('hotel_bookings_clean.csv',index=False)

