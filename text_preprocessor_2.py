import pickle
import os
import pandas as pd
import konlpy
import re


def tokenize_korean_text(text):
    text = re.sub(r'[^,.?!\w\s]', '',
                  text)  ## ,.?!와 문자+숫자+_(\w)와 공백(\s)만 남김  # 앞에 r을 붙여주면 deprecation warning이 안뜸 (raw string으로 declare)

    okt = konlpy.tag.Okt()
    Okt_morphs = okt.pos(text)  # stem=True로 설정하면 동사원형으로 바꿔서 return

    words = []
    for word, pos in Okt_morphs:
        if pos == 'Adjective' or pos == 'Verb' or pos == 'Noun':  # 이 경우에는 형용사, 동사, 명사만 남김
            words.append(word)

    words_str = ' '.join(words)
    return words_str

with open(r'C:\Users\ASH\Desktop\cmct\article_dir_dict.p', 'rb') as f :
    article_name_dict = pickle.load(f)

#article g9번 article_dict가 가장 용량이 큼
with open(r'C:\Users\ASH\Desktop\cmct\article\g9\article_dict.p', 'rb') as f :
    article_dict = pickle.load(f)

final_article_dict = {}
#article_dict // g1, g2, g3....의 값
for i in list(article_name_dict.keys()) :
    name_list = article_name_dict[i]
    final_article_dict[i] = []
    for k in name_list :
        answer = article_dict[k]
        final_article_dict[i].append(answer)

with open('C:/Users/ASH/Desktop/cmct/final_article_dict.p', 'wb') as f :
    pickle.dump(final_article_dict, f)

final_article_df = pd.DataFrame.from_dict(final_article_dict, orient='index')
final_article_df.to_csv('C:/Users/ASH/Desktop/cmct/final_article.csv')
final_article_df.to_excel('C:/Users/ASH/Desktop/cmct/final_article.xlsx')







