import pandas as pd
import numpy as np

'''declare variable'''
username = 'SchneiderKOREA'
year = 2011
last_year = 2018

'''load data'''
data_list = []
while True:
    globals()['result_%s' %year] = pd.read_csv('./twitter_scrap/%s/encoded_scrap_result_%s.csv' %(username, year))
    exec("result_%s = result_%s[['date', 'hashtags','tweet', 'link', 'replies_count', 'retweets_count']]" %(year, year))
    exec('data_list.append(result_%s)' %year)
    year += 1
    if year == last_year + 1: break
df = pd.concat(objs=data_list, ignore_index=True)
df.to_csv('./result/result_%s.csv' %username, encoding='utf-8-sig')

'''pivot table'''
df.date = pd.to_datetime(df.date)
df.date = df.date.dt.strftime('%Y-%m')
# date to year-month for pivoting

'''pivoting'''
pivot = pd.pivot_table(
    data=df,
    values=['replies_count', 'retweets_count'],
    index='date',
    aggfunc='sum',
    fill_value=0
)
pivot.to_csv('./result/pivot_%s.csv' %username)