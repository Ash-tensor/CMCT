from bs4 import BeautifulSoup
import pprint
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

driver = webdriver.Chrome(r'C:\Users\ASH\Desktop\cmct\chromedriver.exe')
#공유가치, 최신순, 3개월로 검색
driver.get('https://search.naver.com/search.naver?where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98&sm=tab_opt&sort=2&photo=0&field=0&pd=13&ds=2022.09.27&de=2022.12.26&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0')
driver.implicitly_wait(30)

k = 0

target_xpath_dict = {0 : '//*[@id="main_pack"]/div[2]/div/div/a[1]',
                     1 : '//*[@id="main_pack"]/div[2]/div/div/a[2]',
                     2 : '//*[@id="main_pack"]/div[2]/div/div/a[3]',
                     3 : '//*[@id="main_pack"]/div[2]/div/div/a[4]',
                     4 : '//*[@id="main_pack"]/div[2]/div/div/a[5]',
                     5 : '//*[@id="main_pack"]/div[2]/div/div/a[6]'}

while k < 400 :
    try :
        answer_list = []
        if k == 0 :
            for_soup = driver.page_source
            soup = BeautifulSoup(for_soup, features = "html.parser")
            #sp_nws116 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)
            #sp_nws111 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)

            beta = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)')
            for i in beta :
                temp = i.get('href')
                answer_list.append(temp)

            k = k + 1

        elif k < 5 :
            driver.find_element(By.XPATH, target_xpath_dict[k]).click()
            driver.implicitly_wait(30)
            for_soup = driver.page_source
            soup = BeautifulSoup(for_soup, features = "html.parser")
            # sp_nws116 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)
            # sp_nws111 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)

            beta = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)')

            for i in beta:
                temp = i.get('href')
                answer_list.append(temp)

            k = k + 1

        else :
            driver.find_element(By.XPATH, target_xpath_dict[5]).click()
            driver.implicitly_wait(30)
            for_soup = driver.page_source
            soup = BeautifulSoup(for_soup, features = "html.parser")
            # sp_nws116 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)
            # sp_nws111 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)

            beta = soup.select('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)')

            for i in beta:
                temp = i.get('href')
                answer_list.append(temp)

            k = k + 1

        target_root = 'C:/Users/ASH/Desktop/cmct/sharedvalue/' + str(k) + '.p'

        if len(answer_list) == 0 :
            pass
        else :
            with open(target_root, 'wb') as f :
                pickle.dump(answer_list, f)
            print(k, ":", answer_list[0])

    except :
        print('error')



