from konlpy.tag import Okt
from collections import Counter
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

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
for v in noun_list:
    print(v)

with open("/Users/hanuri/Desktop/capstone_design/result/noun_list.csv", "w", newline='', encoding='euc-kr') as f:
    csvw = csv.writer(f)
    for v in noun_list[:5]:
        csvw.writerow(v)

wc = WordCloud(font_path='malgun', background_color='white', width=400, height=400, scale=2.0, max_font_size=250)
cloud = wc.generate_from_frequencies(count)

plt.figure()
plt.imshow(cloud)
plt.axis('off')
plt.savefig('/Users/hanuri/Desktop/capstone_design/wordcloud.png')
plt.show()
