import pandas as pd

year = 2013
while True:
    globals()['result_%s' %year] = pd.read_csv('./result/scrap_result_%s.csv' %year)
    year += 1
    if year == 2022: break

df = result_2014[['date', 'name', 'tweet',]]
df.to_csv('./result/sample.csv')
print(df)