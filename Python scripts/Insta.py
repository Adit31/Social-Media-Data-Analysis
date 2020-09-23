from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np

hashtag_list = ['business','lockdown','entertainment','currentaffairs','instadaily','newspaper','art','stayhome','style','trump','life','world','update','likeforlikes','s','moda','sport','photooftheday','upsc','meme','youtube','video','instanews','followforfollowback','beritaterkini','virus','hiphop','italia']
for hashtag in hashtag_list:
    browser = webdriver.Chrome('C:\\Users\\aditg\\Downloads\\chromedriver_win32\\chromedriver')
    browser.get('https://www.instagram.com/explore/tags/'+hashtag)
    Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    links=[]
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    links=[]
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('script', text=lambda t: t.startswith('window._sharedData'))
    page_json = script.string.split(' = ', 1)[1].rstrip(';')
    data = json.loads(page_json)
    for link in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
        links.append('https://www.instagram.com'+'/p/'+link['node']['shortcode']+'/')
    result=pd.DataFrame()
    for i in range(len(links)):
     try:
         page = urlopen(links[i]).read()
         data=bs(page, 'html.parser')
         body = data.find('body')
         script = body.find('script')
         raw = script.text.strip().replace('window._sharedData =', '').replace(';', '')
         json_data=json.loads(raw)
         posts =json_data['entry_data']['PostPage'][0]['graphql']
         posts= json.dumps(posts)
         posts = json.loads(posts)
         x = pd.DataFrame.from_dict(json_normalize(posts), orient='columns') 
         x.columns = x.columns.str.replace("shortcode_media.", "")
         result=result.append(x)
     except:
         np.nan
    result = result.drop_duplicates(subset = 'shortcode')
    result.index = range(len(result.index))
    result.to_csv('C:\\Users\\aditg\\Documents\\Projects\\Social Media Data Analysis\Instagram\\insta_data1.csv', mode = 'a', header = False)