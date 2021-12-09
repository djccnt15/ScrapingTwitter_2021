import twint
import time
import os
start = time.time() # count run time

'''declare variable'''
username = 'SchneiderKOREA'
years = 2011

'''mkdir'''
try: os.mkdir(path='./twitter_scrap/%s' %username)
except: pass

'''scraping'''
while True:
    print('year %s scraping starts' %years)

    # Parameter setting
    c = twint.Config() # declare twint config
    c.Username = username
    c.Store_csv = True
    c.Hide_output = False
    c.Since = ('%s-01-01' %years)
    c.Until = ('%s-12-31' %years)
    c.Output = ('./twitter_scrap/%s/scrap_result_%s.csv' %(username, years))

    twint.run.Search(c) # scraping run

    years += 1 # loop control
    if years == 2021: break

    time.sleep(30) # sleep for none-aggressive scraping

print("time :", time.time() - start) # count run time