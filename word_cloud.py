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

print(communication_dict)

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(communication_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/communication.png')

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(social_value_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/social_value.png')

wc = WordCloud(font_path = 'malgun', width = 400, height = 400,
               scale = 2.0, max_font_size = 250)
gen = wc.generate_from_frequencies(share_value_dict)
plt.figure()
plt.imshow(gen)
wc.to_file(r'C:/Users/ASH/Desktop/cmct/wordcloud/share_value.png')