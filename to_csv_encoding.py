import os
import pandas as pd

'''configuration'''
file_dir = 'C:\\projects\\scraping_twitter\\twitter_scrap\\SchneiderKOREA'

def encoding(file):
    df = pd.read_csv(filepath_or_buffer=file)
    df.to_csv('./encoded_%s' %file, encoding='utf-8-sig')

os.chdir(file_dir)
file_list = os.listdir()

for f in os.listdir():
    encoding(f)