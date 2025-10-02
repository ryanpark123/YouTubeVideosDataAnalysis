import pandas as pd

df = pd.read_csv('data/USvideos.csv')

# Drop duplicates
df = df.drop_duplicates()

# Parse data
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')
df['publish_time'] = pd.to_datetime(df['publish_time'])

# Fill missing tags with 'Unknown'
df['tags'] = df['tags'].fillna('Unknown')

# Export to clean csv
df.to_csv('output/USvideos_clean.csv', index=False)
print("Data cleaned!")

