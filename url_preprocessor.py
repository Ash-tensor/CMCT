from bs4 import BeautifulSoup
import os
import pprint
import multiprocessing
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

def get_url_by_pickle_data(root) :
    try :
        temp = 0
        with open(root, 'rb') as f :
            temp = pickle.load(f)
        return temp
    except :
        return None

directory_list = []
i = 0
while i < 16 :
    temp_dir = 'g' + str(i)
    directory_list.append(temp_dir)
    i = i + 1

url_dictionary = {}

root_base = 'C:/Users/ASH/Desktop/cmct/'
for i in directory_list :
    url_dictionary[i] = []
    print(i)
    target_directory = os.listdir(root_base + i)
    #'C:/Users/ASH/Desktop/cmct/g0 << i까지 더해진 상태
    for k in target_directory :
        temp_list = get_url_by_pickle_data(root_base + i + '/' + k)
        url_dictionary[i].append(temp_list)

print(url_dictionary)
with open(root_base + 'url_dictionary.p', 'wb') as f :
    pickle.dump(url_dictionary, f)




