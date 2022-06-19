import os
from time import time
import json

from PDFtoBoW import get_BoW

base_path = os.path.dirname(os.path.abspath(__file__))
file_dir1 = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/sample1.pdf'))
# Size of sample1: 441 words
file_dir2 = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/sample2.pdf'))
# Size of sample2: 552 words

# 処理時間を計測
s1 = time()
BoW1 = get_BoW(file_dir1)
g1 = time()
print('Test result on sample1:')
print(f'Processing time: {g1-s1:.4f} [s]')

s2 = time()
BoW2 = get_BoW(file_dir2)
g2 = time()
print('Test result on sample2:')
print(f'Processing time: {g2-s2:.4f} [s]')

# 取得したBoW(dict)の内容をチェックするためにjsonファイルとして出力
# with open('test_BoW1.json', 'w') as f:
#     json.dump(BoW1, f, indent = 4)

# with open('test_BoW2.json', 'w') as f:
#     json.dump(BoW2, f, indent = 4)
