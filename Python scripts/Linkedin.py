from selenium import webdriver
from time import sleep
import json
import re
from random import randint
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome('C:\\Users\\aditg\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.linkedin.com')
sleep(3)

username = driver.find_element_by_name('session_key')
username.send_keys('aditgoyal@hotmail.com')
sleep(1)

password = driver.find_element_by_name('session_password')
password.send_keys('*******')
sleep(1)

#sign_button = driver.find_element_by_class_name('signin-form__submit-btn')
#sign_button.click()
#sleep(randint(8,10))

from selenium.webdriver.common.keys import Keys
driver.get('https:www.google.com')
sleep(randint(2,4))
search_query = driver.find_element_by_name('q')
sleep(randint(1,2))

search_query.send_keys('site:linkedin.com/in ' + 'Adit Goyal')
search_query.send_keys(Keys.ENTER)
sleep(randint(1,2))

linkedin_urls = driver.find_elements_by_class_name('iUh30')
href_name = []

linkedin_urls = [url.text for url in linkedin_urls]
link = linkedin_urls[0].split('›',1)[1]
link = link.replace(' ','')
href_name.append(link)
print(href_name)
sleep(randint(3,7))

driver.get('https://www.linkedin.com/in/'+ href_name[0])

page_html = driver.page_source
page_soup = soup(page_html, "html.parser")
function = page_soup.findAll("h2",{"class":"mt1 t-18 t-black t-normal"})
comp = page_soup.find("ul",{"class":"pv-top-card--experience-list"})
print(function)
print(comp)

driver.quit()