from bs4 import BeautifulSoup
import pprint
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

target_xpath_dict = {0 : '//*[@id="main_pack"]/div[2]/div/div/a[1]',
                     1 : '//*[@id="main_pack"]/div[2]/div/div/a[2]',
                     2 : '//*[@id="main_pack"]/div[2]/div/div/a[3]',
                     3 : '//*[@id="main_pack"]/div[2]/div/div/a[4]',
                     4 : '//*[@id="main_pack"]/div[2]/div/div/a[5]',
                     5 : '//*[@id="main_pack"]/div[2]/div/div/a[6]'}

#1 #소통 & 공공시설물
#2 : 소통 & 공공건축물
#3 : 소통 & 인프라
#4 : 소통 & 공공자산
#5 : 소통 & 공공기관
#6 : 공유가치 & 공공시설물
#7 : 공유가치 & 공공건축물
#8 : 공유가치 & 인프라
#9 : 공유가치 & 공공자산
#10 : 공유가치 & 공공기관
#11 : 사회적 가치 & 공공시설물
#12 : 사회적 가치 & 공공건축물
#13 : 사회적 가치 & 인프라
#14 : 사회적 가치 & 공공자산
#15 : 사회적 가치 & 공공기관
g_dict = {0 : 'https://search.naver.com/search.naver?where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98&sm=tab_opt&sort=2&photo=0&field=0&pd=13&ds=2022.09.27&de=2022.12.26&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0',
          1 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&oquery=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&tqi=hIEEmdprvhGssU0OinZssssstSN-046379&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          2 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&oquery=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&tqi=hIEE8sprvN8ss4FMbvNssssss94-070952&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          3 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%86%8C%ED%86%B5+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&oquery=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&tqi=hIEFksp0YiRssP3GS2ZssssssKV-038201&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          4 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&oquery=%EC%86%8C%ED%86%B5+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&tqi=hIEFmdp0YihssO7fIWRssssssfV-077102&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          5 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&oquery=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&tqi=hIEFpdp0J14sssJ%2B3NwssssstJZ-042430&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          6 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&oquery=%EC%86%8C%ED%86%B5+%26+%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&tqi=hIEFwwp0Yidss72QNllsssssslN-250008&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          7 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&oquery=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&tqi=hIEFGwp0J1ZssdjYMkCssssssnZ-061524&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          8 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&oquery=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&tqi=hIEosdp0JywssMLpN3GssssstfK-118453&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          9 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&oquery=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&tqi=hIEo4dp0J1ZssdUlOe0ssssssXN-017131&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          10 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&oquery=%EA%B3%B5%EC%9C%A0%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&tqi=hIEoMwp0YidssKveOzhssssstA4-496162&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          11 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98%26%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&oquery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&tqi=hIEokdp0YidssKdl%2BK0ssssstqK-166443&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          12 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&oquery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98%26%EA%B3%B5%EA%B3%B5%EC%8B%9C%EC%84%A4%EB%AC%BC&tqi=hIEoNdp0YihssOZwTrNssssssKC-369537&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          13 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&oquery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B1%B4%EC%B6%95%EB%AC%BC&tqi=hIEoAwp0Yidss7rL8LKssssssus-338525&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          14 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&oquery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EC%9D%B8%ED%94%84%EB%9D%BC&tqi=hIEoYdprvN8ss4ywts0sssssthl-107794&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1',
          15 : 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EA%B8%B0%EA%B4%80&oquery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B0%80%EC%B9%98+%26+%EA%B3%B5%EA%B3%B5%EC%9E%90%EC%82%B0&tqi=hIEo2sprvxsssCUQu1Zssssssh4-456368&nso=so%3Add%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=0&photo=0&sort=1'}

driver = webdriver.Chrome(r'C:\Users\ASH\Desktop\cmct\chromedriver.exe')
    #공유가치, 최신순, 3개월로 검색

g = 0

while g < 16 :
    driver.get(g_dict[g])
    driver.implicitly_wait(30)

    k = 0
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

            target_root = 'C:/Users/ASH/Desktop/cmct/g' + str(g) + '/' + str(k) + '.p'

            if len(answer_list) == 0 :
                pass
            else :
                with open(target_root, 'wb') as f :
                    pickle.dump(answer_list, f)
                print(g, 'root', k, ":", answer_list[0])

        except :
            print('error')

    g = g + 1