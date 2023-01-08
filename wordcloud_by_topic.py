from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

target_file = r'C:\Users\ASH\Desktop\cmct\wordcloud\상위50위_키워드_데이터프레임.csv'
word_cloud_df = pd.read_csv(target_file)

communication_df = word_cloud_df[word_cloud_df['키워드'] == '소통']
social_value_df = word_cloud_df[word_cloud_df['키워드'] == '사회적 가치']
share_value_df = word_cloud_df[word_cloud_df['키워드'] == '공유가치']

communication_df = communication_df[['단어', '빈도', 'topic']]
social_value_df = social_value_df[['단어', '빈도', 'topic']]
share_value_df = share_value_df[['단어', '빈도', 'topic']]


communication_df_t1 = communication_df[communication_df['topic'] == 'topic1']
communication_df_t2 = communication_df[communication_df['topic'] == 'topic2']
communication_df_t3 = communication_df[communication_df['topic'] == 'topic3']
communication_df_t4 = communication_df[communication_df['topic'] == 'topic4']

communication_df_list = [communication_df_t1, communication_df_t2, communication_df_t3,
                         communication_df_t4]

social_value_df_t1 = social_value_df[social_value_df['topic'] == 'topic1']
social_value_df_t2 = social_value_df[social_value_df['topic'] == 'topic2']
social_value_df_t3 = social_value_df[social_value_df['topic'] == 'topic3']
social_value_df_t4 = social_value_df[social_value_df['topic'] == 'topic4']

social_value_df_list = [social_value_df_t1, social_value_df_t2, social_value_df_t3,
                        social_value_df_t4]

share_value_df_t1 = share_value_df[share_value_df['topic'] == 'topic1']
share_value_df_t2 = share_value_df[share_value_df['topic'] == 'topic2']
share_value_df_t3 = share_value_df[share_value_df['topic'] == 'topic3']
share_value_df_t4 = share_value_df[share_value_df['topic'] == 'topic4']

share_value_df_list = [share_value_df_t1, share_value_df_t2, share_value_df_t3,
                       share_value_df_t4]

def dataframe_to_dict(df) :
    i = 0
    answer_dict = {}
    while i < len(df) :
        dict_key = df['단어'].iloc[i]
        dict_answer = df['빈도'].iloc[i]
        answer_dict[dict_key] = dict_answer
        i = i + 1

    return answer_dict

communication_dict_list = []

for k in communication_df_list :
    temp = dataframe_to_dict(k)
    communication_dict_list.append(temp)

share_value_dict_list = []

for k in share_value_df_list :
    temp = dataframe_to_dict(k)
    share_value_dict_list.append(temp)

social_value_dict_list = []

for k in social_value_df_list :
    temp = dataframe_to_dict(k)
    social_value_dict_list.append(temp)

for i in communication_dict_list:
    print(i)

del_list = ['언론사', '구독', '통해', '지난', '아웃', '링크', '단지', '오전', '당선인', '설명',
            '지난해', '후보', '대한', '대해', '메인', '이번', '이동해', '이재명', '가지', '추천',
            '바로가기', '분류', '편집', '페이지', '경우', '기자', '뉴스', '기사', '위해', '지금',
            '바로', '윤석열', '무단', '배포', '민주당', '후속', '섹션', '독자', '기자', '뉴스',
            '대한', '이번', '후속', '섹션', '페이지', '바로', '메인', '관련', '지난',
            '대해', '때문', '강추', '쏠쏠', '언론사', '구독', '위해', '아웃', '우리', '마련',
            '후보', '네이버', '기사', '통해', '지금', '대통령', '추천', '링크', '바로가기', '무단',
            '배포', '편집', '이동해', '프로필', '흥미진진', '라며', '구독', '뉴스', '지금', '민주당',
            '메인', '추천', '배포', '후속', '서울', '관련', '윤석열', '때문', '페이지', '이동해', '올해',
            '언론사', '기자', '위해', '우리', '기사', '대한', '지난', '이번', '바로가기', '아웃',
            '링크', '이재명', '바로', '후보', '해당', '섹션', '경우', '쏠쏠', '백배']


for i in communication_dict_list :
    for k in del_list :
        try :
            del i[k]
        except :
            pass

for i in communication_dict_list :
    print(i)

for i in social_value_dict_list :
    print(i)

for i in social_value_dict_list :
    for k in del_list :
        try :
            del i[k]
        except :
            pass

for i in social_value_dict_list :
    print(i)

for i in share_value_dict_list:
    print(i)

for i in share_value_dict_list :
    for k in del_list :
        try :
            del i[k]
        except :
            pass

for i in share_value_dict_list :
    print(i)

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
c= 1
for i in communication_dict_list :
    gen = wc.generate_from_frequencies(i)
    plt.figure()
    plt.imshow(gen)
    wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/communication' + str(c) + '.png')
    c = c + 1

c = 1
for i in share_value_dict_list :
    gen = wc.generate_from_frequencies(i)
    plt.figure()
    plt.imshow(gen)
    wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/share_value' + str(c) + '.png')
    c = c + 1

c = 1
for i in social_value_dict_list :
    gen = wc.generate_from_frequencies(i)
    plt.figure()
    plt.imshow(gen)
    wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/social_value' + str(c) + '.png')
    c = c + 1