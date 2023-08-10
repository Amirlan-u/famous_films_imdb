import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
d = df.pivot_table(index='Year',
                   values='Runtime (Minutes)',
                   aggfunc=['max', 'mean'])
d.plot(kind='bar', subplots=True)
plt.show()
