import pandas as pd
import matplotlib.pyplot as plot
df = pd.read_csv('IMDB-Movie-Data.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#Зависит ли от даты выхода оцека фильма

df["Year"].fillna(-1, inplace=True)

print(round(df.groupby(by="Year")["Metascore", "Runtime (Minutes)"].mean(), 1))
g = df[(df["Director"] == 'Woody Allen')]["Metascore"]
df['Alexandre Aja'] = df["Director"] == 'Alexandre Aja'

a = df[df['Alexandre Aja'] & df['Actors']]['Metascore']
hn = df.groupby(by='Alexandre Aja')['Actors', 'Metascore']
print(hn.tail(5))
print(g)