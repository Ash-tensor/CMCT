import pickle
import konlpy
import re


with open(r'C:\Users\ASH\Desktop\cmct\final_article_dict.p', 'rb') as f :
    final_article = pickle.load(f)

print(final_article.keys())