import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('movies/imdb_top_1000.csv')
data['Gross'] = data['Gross'].str.replace(',', '').astype(float)

average_gross = data.groupby('Genre')['Gross'].mean()

plt.figure(figsize=(14, 6))
average_gross.plot(kind='bar', color='skyblue')
plt.title('Average Movie Gross by Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Average Gross in $')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

high_gross_genres = average_gross[average_gross > data['Gross'].quantile(0.75)]

plt.figure(figsize=(12, 6))
high_gross_genres.plot(kind='bar', color='skyblue')
plt.title('Average Movie Gross by Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Average Gross in $')
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.ticklabel_format(axis='y', style='plain')
plt.ylim(min(high_gross_genres) * 0.9, max(high_gross_genres) * 1.1)
plt.grid(axis='y')
plt.tight_layout()
plt.show()