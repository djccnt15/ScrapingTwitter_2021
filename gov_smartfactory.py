import twint
import time
start = time.time()

'''scraping'''
years = 2013
while True:
    print('year %s scraping starts' %years)
    # Parameter setting
    c = twint.Config() # declare twint config
    c.Username = 'bizinfo1357'
    c.Store_csv = True
    c.Hide_output = False
    c.Since = ('%s-01-01' %years)
    c.Until = ('%s-12-31' %years)
    c.Output = ('./result/scrap_result_%s.csv' %years)

    twint.run.Search(c)

    years += 1
    time.sleep(30)
    if years == 2020: break

print("time :", time.time() - start)