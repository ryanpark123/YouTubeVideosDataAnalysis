import pandas as pd
import seaborn as sns

df = pd.read_csv('output/USvideos_clean.csv')

#category_counts = df['category_id'].value_counts()
#print(category_counts.head(10))

sns.scatterplot(x='views',y='likes', data=df)