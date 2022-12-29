import os
import pickle
import pprint
import pandas as pd

with open(r'C:\Users\ASH\Desktop\cmct\article\g9\article_dict.p', 'rb') as f :
    article_dict = pickle.load(f)

#g15에서 g14를 빼야함

list_dir = os.listdir('C:/Users/ASH/Desktop/cmct/article')

series_dict = {}

for target in list_dir :
    temp = os.path.getsize('C:/Users/ASH/Desktop/cmct/article/'
                + target + '/article_dict.p',)
    series_dict[target] = temp

#순서는 그냥 list_dir대로 하면 되겠네

print(series_dict.keys())

series_dict_list = list(series_dict.keys())
article_dir_dict = {}

root_base = 'C:/Users/ASH/Desktop/cmct/article/'

i = 0
while i < len(series_dict.keys()) - 1 :
    with open(root_base + series_dict_list[i + 1] + '/article_dict.p', 'rb') as f :
        g0 = pickle.load(f)
    with open(root_base + series_dict_list[i] + '/article_dict.p', 'rb') as f :
        g1 = pickle.load(f)

    g0 = list(g0.keys())
    g1 = list(g1.keys())

    temp = set(g0) - set(g1)

    article_dir_dict[series_dict_list[i + 1]] = temp
    i = i + 1

with open('C:/Users/ASH/Desktop/cmct/'+ 'article_dir_dict.p', 'wb') as f :
    pickle.dump(article_dir_dict, f)

a = pd.DataFrame.from_dict(article_dir_dict, orient='index')
a.to_csv('C:/Users/ASH/Desktop/cmct/article_dir_dict.csv')
a.to_excel('C:/Users/ASH/Desktop/cmct/article_dir_dict.xlsx')