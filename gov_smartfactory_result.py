import pandas as pd
import numpy as np

'''load data'''
year = 2018
data_list = []
while True:
    globals()['result_%s' %year] = pd.read_csv('./twitter_scrap/scrap_result_%s.csv' %year)
    exec("result_%s = result_%s[['date', 'hashtags','tweet', 'link']]" %(year, year))
    exec('data_list.append(result_%s)' %year)
    year += 1
    if year == 2022: break
df = pd.concat(objs=data_list, ignore_index=True)

'''trimming data'''
df['tweet'] = df['tweet'].str.split(pat='http').str[0]
# delete useless links at the end of the tweet
df['tweet'] = df['tweet'] + df['hashtags']
df = df.drop(['hashtags'], axis=1)
print(df.describe())

# word replace
df['tweet'] = df['tweet'].str.replace('스마트 공장', '스마트공장')
df['tweet'] = df['tweet'].str.replace('스마트 제조', '스마트제조')

# stop words for deleting meaningless data
stopwords = [
    '맞팔',
    '동영상에',
    '동영상을',
    '좋아요 표시를 했습니다.',
    '@',
    '링크연결이 안되면 아래주소를 클릭해주세요.'
]
for i in stopwords:
    df = df[~df['tweet'].str.contains(i)]
print(df.describe())

'''sort dataframe'''
df = df.sort_values(by=['date'])
# print(df)

'''words count'''
df['smart_factory'] = df['tweet'].str.contains('스마트공장')
# df['smart_factory'] = df['smart_factory'].astype(int)

df['smart_manufacture'] = df['tweet'].str.contains('스마트제조')
# df['smart_manufacture'] = df['smart_manufacture'].astype(int)
# print(df)

'''save trimmed data'''
df.to_csv('./result/result.csv', index=False, encoding='utf-8-sig')

'''pivot table'''
df.date = pd.to_datetime(df.date)
df.date = df.date.dt.strftime('%Y-%m')
# date to year-month for pivoting
df = pd.get_dummies(data=df, columns=['smart_factory', 'smart_manufacture'])
# one hot encoding for avoid dimensional issue for pivoting

# pivoting smart factory
smart_factory = pd.pivot_table(
    data=df,
    values=['smart_factory_False', 'smart_factory_True'],
    index='date',
    aggfunc='sum',
    fill_value=0
)
smart_factory['True_ratio'] = smart_factory['smart_factory_True'] / \
    (smart_factory['smart_factory_False'] + smart_factory['smart_factory_True'])
# print(smart_factory)

# pivoting smart manufacture
smart_manufacture = pd.pivot_table(
    data=df,
    values=['smart_manufacture_False', 'smart_manufacture_True'],
    index='date',
    aggfunc='sum',
    fill_value=0
)
smart_manufacture['True_ratio'] = smart_manufacture['smart_manufacture_True'] / \
    (smart_manufacture['smart_manufacture_False'] + smart_manufacture['smart_manufacture_True'])
# print(smart_manufacture)

'''save pivot result'''
smart_factory.to_csv('./result/smart_factory_pivot.csv', encoding='utf-8-sig')
smart_manufacture.to_csv('./result/smart_manufacture_pivot.csv', encoding='utf-8-sig')