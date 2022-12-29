import pickle
import pprint
import pandas as pd

with open(r'C:\Users\ASH\Desktop\cmct\url_dictionary.p', 'rb') as f :
    url_dictionary = pickle.load(f)

print(url_dictionary.keys())

new_url_dictionary = {}
url_keys = url_dictionary.keys()

for i in url_keys :
    new_url_dictionary[i] = []
    k = url_dictionary[i]
    for j in k :
        for c in j :
            new_url_dictionary[i].append(c)

print(new_url_dictionary['g0'])



temp = pd.DataFrame.from_dict(new_url_dictionary, orient='index')
print(temp)

root_base = 'C:/Users/ASH/Desktop/cmct/'

with open(root_base + 'url_dictionary_preprocessed.p', 'wb') as f :
    pickle.dump(new_url_dictionary, f)
temp.to_csv(root_base + 'url_list.csv')
temp.to_excel(root_base + 'url_list.xlsx')
