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
# sample1.pdfの単語頻度、単語の意味のdictをそれぞれ取得
BoW_frequency1, BoW_meaning1 = get_BoW(file_dir1)
g1 = time()
print('Test result on sample1:')
print(f'Processing time: {g1-s1:.4f} [s]')

s2 = time()
# sample2.pdfの単語頻度、単語の意味のdictをそれぞれ取得
BoW_frequency2, BoW_meaning2 = get_BoW(file_dir2)
g2 = time()
print('Test result on sample2:')
print(f'Processing time: {g2-s2:.4f} [s]')

# 取得したBoW(dict)の内容をチェックするためにjsonファイルとして出力
# sample1.pdfの{'単語': 頻度}のdictを保存
# with open('sample1_frequency.json', 'w') as f:
#     json.dump(BoW_frequency1, f, indent = 4)
# sample2.pdfの{'単語': 頻度}のdictを保存
# with open('sample2_frequency.json', 'w') as f:
#     json.dump(BoW_frequency2, f, indent = 4)

# sample1.pdfの{'単語'; '辞書のエントリー'}のdictを保存
# with open('sample1_meaning.json', 'w', encoding = 'utf-8') as f:
#     json.dump(BoW_meaning1, f, indent = 4)
# sample2.pdfの{'単語'; '辞書のエントリー'}のdictを保存
# with open('sample2_meaning.json', 'w', encoding = 'utf-8') as f:
#     json.dump(BoW_meaning2, f, indent = 4)

# {'単語': '辞書のエントリー'}のBoWについてちゃんと対応できているかテスト
print(BoW_meaning1['activity'])
print(BoW_meaning2['attributive'])

