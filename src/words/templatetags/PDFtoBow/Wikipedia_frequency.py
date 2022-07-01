import os
import json
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

base_path = os.path.dirname(os.path.abspath(__file__))
Wikipedia_path = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/enwiki-20210820-words-frequency.txt'))
with open(Wikipedia_path, 'r')as f:
    data = f.readlines()

# Wikipediaデータからstopwordを取り除く
stopword_removed_data = []
for line in data:
    word, frequency = line.split()
    if word not in stop_words:
        stopword_removed_data.append((word, frequency))

# stopwordを取り除いたWikipediaデータをminmax scalingする
scaled_Wikipedia_frequency = {}
x_max = int(stopword_removed_data[0][-1])
x_min = int(stopword_removed_data[-1][-1])
print(x_max)
print('word', stopword_removed_data[0][0])
print(x_min)
# for word, frequency in stopword_removed_data : # スケーリングを施す,範囲は[-10, 100]
    if word not in stop_words:
        sc_max = 100
        sc_min = -10
        scaled_frequency = (int(frequency) - x_min) / (x_max - x_min) * (sc_max - sc_min) + sc_min
        scaled_Wikipedia_frequency[word] = scaled_frequency

with open('Wikipedia_frequency.json', 'w')as f:
    json.dump(scaled_Wikipedia_frequency, f, indent=4)

