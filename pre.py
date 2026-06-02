import pandas as pd

df = pd.read_csv('netflix_titles.csv')

df.drop_duplicates(inplace=True)

df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Not Specified', inplace=True)
df['cast'].fillna('Not Specified', inplace=True)
df.dropna(subset=['date_added', 'rating'], inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'].str.strip())

df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0].strip())

df['runtime_minutes'] = df['duration'].apply(
    lambda x: int(x.split(' ')[0]) if 'min' in str(x) else int(x.split(' ')[0]) * 45
)

df.to_csv('netflix_final_clean.csv', index=False)
print("Cleaning complete! Saved as netflix_final_clean.csv")