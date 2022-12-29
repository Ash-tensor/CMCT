from bs4 import BeautifulSoup
import pprint
import requests
import re
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

with open(r'C:\Users\ASH\Desktop\cmct\url_dictionary_preprocessed.p', 'rb') as f :
    url_dictionary = pickle.load(f)

driver = webdriver.Chrome(r'C:\Users\ASH\Desktop\cmct\chromedriver.exe')
    #공유가치, 최신순, 3개월로 검색

print(url_dictionary['g0'][0])
print(type(url_dictionary['g0'][0]))
print(url_dictionary['g0'][0][:23])
driver.get(url_dictionary['g0'][0])
k = 0
article_dict = {}

list_dir = os.listdir('C:/Users/ASH/Desktop/cmct/article')
print(list_dir)
root_base = 'C:/Users/ASH/Desktop/cmct/article/'

for k in list_dir :
    for i in url_dictionary[k] :
        try :
            driver.get(i)
            driver.implicitly_wait(10)
            temp_name = driver.find_element(By.XPATH, '//*[@id="title_area"]').text
            article_content = driver.find_element(By.XPATH, '//*[@id="contents"]').text
            article_date = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span').text
            article_dict[temp_name] = [article_date, article_content]
            print(k, i)
        except :
            pass

    with open(root_base + k + '/article_dict.p', 'wb') as f:
        pickle.dump(article_dict, f)


#for i in url_dictionary['g0'] :
    #try :
        #driver.get(i)
        #driver.implicitly_wait(10)
        #temp_name = driver.find_element(By.XPATH, '//*[@id="title_area"]').text
        #article_content = driver.find_element(By.XPATH, '//*[@id="contents"]').text
        #article_date = driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span').text
        #article_dict[temp_name] = [article_date, article_content]
    #except :
        #pass


