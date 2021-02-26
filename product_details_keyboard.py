import pandas as pd
import numpy as np
import re
from pandas.io.json import json_normalize

csv_filename = 'product_details_keyboard.csv'
csv_bought_together = 'items_bought_together_keyboard.csv'
csv_customer_reviews = 'links_to_customer_reviews_keyboard.csv'
txt_customer_reviews = 'links_to_customer_reviews_keyboard.txt'

df = pd.read_json('keyboard_product_output.jsonl')

df = df.dropna(axis=0, how='all')

df.link_to_all_reviews = 'https://www.amazon.com/' + df.link_to_all_reviews

df.reset_index(drop=True, inplace = True)

# Extraction of all specifications in nested JSON-dicts to be used for building additional columns 
  
new_columns = []
for i in range(len(df)):
    if df.product_summary[i] is not None:
        product_sum = df.product_summary[i]
        x = len(product_sum)  
        for j in range(x):
            new_columns.append(product_sum[j]['info'])
    if df.product_tech_spec[i] is not None:
        product_tech = df.product_tech_spec[i]
        y = len(product_tech)  
        for j in range(y):
            new_columns.append(product_tech[j]['info'])
    if df.product_addl_info[i] is not None:
        product_add = df.product_addl_info[i]
        z = len(product_add)  
        for j in range(z):
            new_columns.append(product_add[j]['info'])

for i in range(len(new_columns)):
    if new_columns[i] is not None:
        new_columns[i] = new_columns[i].lower()

new_columns = set(new_columns) 
new_columns = list(new_columns)
try:
    new_columns.remove(None)
except:
    pass

for i in new_columns:
    df[i] = i
    df[i] = ''

for i in range(len(df)):
    if df.product_summary[i] is not None:
        psc = []
        product_sum = df.product_summary[i]
        product_sum = pd.DataFrame(product_sum)
        product_sum = product_sum.transpose()
        psc_len = len(product_sum.columns)  # collecting number of columns in product_sum / items in df.product_summary
        for j in range(psc_len):            # getting item / column names
            psc.append(product_sum[j][0])
        for k in range(len(psc)):           # setting item / column names in lower cases for transfer of values into correct df columns
            if psc[k] is not None:
                psc[k] = psc[k].lower()
        product_sum.columns = product_sum.iloc[0] # Turns row 1 into column names
        product_sum = product_sum.drop('info') # Drops row 1
        product_sum.columns = psc
        for l in psc: 
            try:
                df[l][i] = product_sum[l]['value']
            except:
                continue
    if df.product_tech_spec[i] is not None:
        ptc = []
        product_tec = df.product_tech_spec[i]
        product_tec = pd.DataFrame(product_tec)
        product_tec = product_tec.transpose()
        ptc_len = len(product_tec.columns)  # collecting number of columns in product_tec / items in df.product_tech_spec
        for j in range(ptc_len):            # getting item / column names
            ptc.append(product_tec[j][0])
        for k in range(len(ptc)):           # setting item / column names in lower cases for transfer of values into correct df columns
            if ptc[k] is not None:
                ptc[k] = ptc[k].lower()
        product_tec.columns = product_tec.iloc[0] # Turns row 1 into column names
        product_tec = product_tec.drop('info') # Drops row 1
        product_tec.columns = ptc
        for l in ptc:   ## What does this loop through??? I need the column name, but I have to stay within one row!!!
            try:
                df[l][i] = product_tec[l]['value']
            except:
                continue
    if df.product_addl_info[i] is not None:
        pac = []
        product_add = df.product_addl_info[i]
        product_add = pd.DataFrame(product_add)
        product_add = product_add.transpose()
        pac_len = len(product_add.columns)  # collecting number of columns in product_tec / items in df.product_tech_spec
        for j in range(pac_len):            # getting item / column names
            pac.append(product_add[j][0])
        for k in range(len(pac)):           # setting item / column names in lower cases for transfer of values into correct df columns
            if pac[k] is not None:
                pac[k] = pac[k].lower()
        product_add.columns = product_add.iloc[0] # Turns row 1 into column names
        product_add = product_add.drop('info') # Drops row 1
        product_add.columns = pac
        for l in pac: 
            try:
                df[l][i] = product_add[l]['value']
            except:
                continue

df.rename(columns = {'asin' : 'ASIN'}, inplace = True)

for i in range(len(df)):
    if df['customer reviews'][i] is not None:
        try:
            res = [re.findall(r'(\d+).(\d+) out of 5 stars', df['customer reviews'][i])[0] ]
            a = res[0][0]
            b = res[0][1]
            c = float(a+'.'+b)
            df['customer reviews'][i] = c
        except:
            pass

df.rename(columns = {'customer reviews' : 'rating'}, inplace = True)

df = df.drop(['product_summary', 'product_tech_spec', 'product_addl_info'], axis = 1)

for i in range(len(df)):
    if df.rating[i] == '':        
        df.rating[i] = 0

df['rating'] = df.rating.astype(float)

for i in range(len(df)):
    if df.name[i] is None:
        df = df.drop([i], axis = 0)

df = df.drop_duplicates('name', keep = 'first')

df.reset_index(drop=True, inplace=True)

df_keyboard_customer_reviews_link = df.link_to_all_reviews
df_keyboard_customer_reviews_link = df_keyboard_customer_reviews_link.dropna()
df_keyboard_customer_reviews_link.reset_index(drop=True, inplace = True)

df_keyboard_bought_together = df[['ASIN', 'name', 'freq_bought', 'freq_bought_link']]

df.to_csv(csv_filename)
df_keyboard_customer_reviews_link.to_csv(csv_customer_reviews) # actually not necessary anymore since there's being a txt-file created
df_keyboard_bought_together.to_csv(csv_bought_together)

f = open(txt_customer_reviews, 'w+')
for i in range(len(df_keyboard_customer_reviews_link)):
    f.write(df_keyboard_customer_reviews_link[i])
    f.write('\n')
f.close()

df2 = pd.read_csv(csv_filename)
df2