import pandas as pd
from collections import Counter

f = pd.read_csv("/Users/hanuri/Desktop/capstone_design/crawling_result.csv")
g = pd.read_csv("/Users/hanuri/Desktop/capstone_design/noun_list.csv", names=['noun', 'num'], encoding='euc-kr')

pd.set_option('display.max_colwidth', None)

nouns = g['noun']
nouns_list = nouns.values.tolist()

nouns1 = f['contents'].str.count(nouns_list[0])
noun1max = nouns1.max()
idx1 = list(filter(lambda x: nouns1[x] == noun1max, range(len(nouns1))))
link1 = f['link'][idx1]

nouns2 = f['contents'].str.count(nouns_list[1])
noun2max = nouns2.max()
idx2 = list(filter(lambda x: nouns2[x] == noun2max, range(len(nouns2))))
link2 = f['link'][idx2]

nouns3 = f['contents'].str.count(nouns_list[2])
noun3max = nouns3.max()
idx3 = list(filter(lambda x: nouns3[x] == noun3max, range(len(nouns3))))
link3 = f['link'][idx3]

nouns4 = f['contents'].str.count(nouns_list[3])
noun4max = nouns4.max()
idx4 = list(filter(lambda x: nouns4[x] == noun4max, range(len(nouns4))))
link4 = f['link'][idx4]

nouns5 = f['contents'].str.count(nouns_list[4])
noun5max = nouns5.max()
idx5 = list(filter(lambda x: nouns5[x] == noun5max, range(len(nouns5))))
link5 = f['link'][idx5]

links = [link1, link2, link3, link4, link5]
linkcc = pd.concat(links, ignore_index=False)

Counter(linkcc)

list = Counter(linkcc).most_common(3)

ix1 = f[f['link'] == list[0][0]].index
ix2 = f[f['link'] == list[1][0]].index
ix3 = f[f['link'] == list[2][0]].index

print(f['link'][ix1])
print(f['link'][ix2])
print(f['link'][ix3])
