from konlpy.tag import Okt
from collections import Counter
import csv
from wordcloud import WordCloud
from PIL import Image

def nouns():
    f = open("/Users/hanuri/Desktop/capstone_design/result/crawling_result.csv", 'r', encoding='utf-8')
    news = f.read()
    okt = Okt()
    noun = okt.nouns(news)
    for i, v in enumerate(noun):
        if len(v) < 2:
            noun.pop(i)

    count = Counter(noun)
    f.close
    noun_list = count.most_common(100)

    with open("/Users/hanuri/Desktop/capstone_design/result/noun_list.csv", "w", newline='', encoding='euc-kr') as f:
        csvw = csv.writer(f)
        for v in noun_list[:5]:
            csvw.writerow(v)

    wc = WordCloud(font_path='malgun', background_color='white', width=400, height=400, scale=2.0, max_font_size=250)
    cloud = wc.generate_from_frequencies(count)
    cloud.to_file('/Users/hanuri/Desktop/capstone_design/result/wordcloud.png')
