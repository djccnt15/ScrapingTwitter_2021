import twint
import time
start = time.time() # count run time

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

    twint.run.Search(c) # scraping run

    years += 1 # loop control
    if years == 2020: break

    time.sleep(30) # sleep for none-aggressive

print("time :", time.time() - start) # count run time