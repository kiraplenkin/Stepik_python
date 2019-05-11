import pandas as pd

df = pd.read_csv('Crimes.csv')

print(df['Primary Type'].value_counts()[:1])
