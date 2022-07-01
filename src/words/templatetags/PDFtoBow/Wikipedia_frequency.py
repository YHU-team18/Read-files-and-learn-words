import os
import json

base_path = os.path.dirname(os.path.abspath(__file__))
Wikipedia_path = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/enwiki-20210820-words-frequency.txt'))
with open(Wikipedia_path, 'r')as f:
    Wikipedia_frequency = {}
    for line in f.readlines():
        word, frequency = line.split()
        Wikipedia_frequency[word] = int(frequency)

with open('Wikipedia_frequency.json', 'w')as f:
    json.dump(Wikipedia_frequency, f)