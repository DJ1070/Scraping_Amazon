import pandas as pd
import numpy as np

csv_filename = 'summary_monitor.csv'

df = pd.read_json('monitor_search_output.jsonl')

df['ASIN'] = df.url.str.split('/dp/').str[-1]
df['ASIN'] = df.ASIN.str.split('%2Fdp%2F').str[-1]
df['ASIN'] = df.ASIN.str.split('/').str[0]
df['ASIN'] = df.ASIN.str.split('%2F').str[0]

df = df.drop('url', axis = 1)

df = df[['ASIN', 'title', 'price', 'rating', 'review_count']]

df['rating'] = df['rating'].fillna(0)
df['price'] = df['price'].fillna(0)

df['rating'] = df['rating'].str.split( ).str[0]
df['price'] = df['price'].str.split('$').str[-1]

try:
    df['price'] = df['price'].str.replace(",","").astype(float)
    df['rating'] = df['rating'].replace(",","").astype(float)
except:
    pass

df.review_count = df.review_count.str.replace(',','')
df.review_count = pd.to_numeric(df.review_count)
df.review_count = df.review_count.fillna(0)
df.review_count = df.review_count.astype(int)

df.to_csv(csv_filename)
