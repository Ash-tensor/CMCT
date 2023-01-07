from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

target_file = r'C:\Users\ASH\Desktop\cmct\wordcloud\상위50위_키워드_데이터프레임.csv'
word_cloud_df = pd.read_csv(target_file)

print(word_cloud_df)

communication_df = word_cloud_df[word_cloud_df['키워드'] == '소통']
social_value_df = word_cloud_df[word_cloud_df['키워드'] == '사회적 가치']
share_value_df = word_cloud_df[word_cloud_df['키워드'] == '공유가치']

communication_df = communication_df[['단어', '빈도']]
social_value_df = social_value_df[['단어', '빈도']]
share_value_df = share_value_df[['단어', '빈도']]

print(communication_df)

communication_dict = {}
i = 0

def dataframe_to_dict(df) :
    i = 0
    answer_dict = {}
    while i < len(df) :
        dict_key = df['단어'].iloc[i]
        dict_answer = df['빈도'].iloc[i]
        answer_dict[dict_key] = dict_answer
        i = i + 1

    return answer_dict

communication_dict = dataframe_to_dict(communication_df)
social_value_dict = dataframe_to_dict(social_value_df)
share_value_dict = dataframe_to_dict(share_value_df)

del communication_dict['언론사']
del communication_dict['구독']
del communication_dict['통해']
del communication_dict['지난']
del communication_dict['아웃']
del communication_dict['링크']
del communication_dict['단지']
del communication_dict['오전']
del communication_dict['당선인']
del communication_dict['설명']
del communication_dict['지난해']
del communication_dict['후보']
del communication_dict['대한']
del communication_dict['대해']
del communication_dict['메인']
del communication_dict['이번']
del communication_dict['이동해']
del communication_dict['이재명']
del communication_dict['가지']
del communication_dict['추천']
del communication_dict['바로가기']
del communication_dict['분류']
del communication_dict['편집']
del communication_dict['페이지']
del communication_dict['경우']
del communication_dict['기자']
del communication_dict['뉴스']
del communication_dict['기사']
del communication_dict['위해']
del communication_dict['지금']
del communication_dict['바로']
del communication_dict['윤석열']
del communication_dict['무단']
del communication_dict['배포']
del communication_dict['민주당']
del communication_dict['후속']
del communication_dict['섹션']
del communication_dict['독자']

del share_value_dict['기자']
del share_value_dict['뉴스']
del share_value_dict['대한']
del share_value_dict['이번']
del share_value_dict['후속']
del share_value_dict['섹션']
del share_value_dict['페이지']
del share_value_dict['바로']
del share_value_dict['메인']
del share_value_dict['관련']
del share_value_dict['지난']
del share_value_dict['대해']
del share_value_dict['때문']
del share_value_dict['강추']
del share_value_dict['쏠쏠']
del share_value_dict['언론사']
del share_value_dict['구독']
del share_value_dict['위해']
del share_value_dict['아웃']
del share_value_dict['우리']
del share_value_dict['마련']
del share_value_dict['후보']
del share_value_dict['네이버']
del share_value_dict['기사']
del share_value_dict['통해']
del share_value_dict['지금']
del share_value_dict['대통령']
del share_value_dict['추천']
del share_value_dict['링크']
del share_value_dict['바로가기']
del share_value_dict['무단']
del share_value_dict['배포']
del share_value_dict['편집']
del share_value_dict['이동해']
del share_value_dict['프로필']
del share_value_dict['흥미진진']
del share_value_dict['라며']


del social_value_dict['구독']
del social_value_dict['뉴스']
del social_value_dict['지금']
del social_value_dict['민주당']
del social_value_dict['메인']
del social_value_dict['추천']
del social_value_dict['배포']
del social_value_dict['후속']
del social_value_dict['서울']
del social_value_dict['관련']
del social_value_dict['윤석열']
del social_value_dict['때문']
del social_value_dict['페이지']
del social_value_dict['이동해']
del social_value_dict['올해']
del social_value_dict['언론사']
del social_value_dict['기자']
del social_value_dict['위해']
del social_value_dict['우리']
del social_value_dict['기사']
del social_value_dict['대한']
del social_value_dict['지난']
del social_value_dict['이번']
del social_value_dict['바로가기']
del social_value_dict['아웃']
del social_value_dict['링크']
del social_value_dict['이재명']
del social_value_dict['바로']
del social_value_dict['후보']
del social_value_dict['해당']
del social_value_dict['섹션']
del social_value_dict['경우']
del social_value_dict['쏠쏠']
del social_value_dict['백배']


print(communication_dict)

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(communication_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/communication_refined.png')

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(social_value_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/social_value_refined.png')

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(share_value_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/share_value_refined.png')