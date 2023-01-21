#by Hassanat Awodipe, Tabatha Correa and Tamsir Jobe

#This section reads and cleans the given dataset, removing lines where it finds  blanks in important 
# information.

import pandas as pd

#reads the csv
df = pd.read_csv('salaries1.csv')

#drops all rows that contain null variables and sets to second var
df2 = df.dropna()
