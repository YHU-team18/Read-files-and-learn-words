import os
from time import time
import json
from PDFtoBoW import get_BoW
from PDFtoBoW import get_meaning
from PDFtoBoW import get_Wikipedia_frequency
from PDFtoBoW import get_IPA

base_path = os.path.dirname(os.path.abspath(__file__))
file_dir1 = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/sample1.pdf'))
# Size of sample1: 441 words
file_dir2 = os.path.normpath(os.path.join(base_path, '../PDFtoBoW/sample2.pdf'))
# Size of sample2: 552 words

# 処理時間を計測
s1 = time()
# sample1.pdfの単語頻度、単語の意味のdictをそれぞれ取得
sample1_frequency = get_BoW(file_dir1)
sample1_meaning = get_meaning(file_dir1)
sample1_Wikipedia_frequency = get_Wikipedia_frequency(file_dir1)
sample1_IPA = get_IPA(file_dir1)
g1 = time()
print(f'Processing time on {file_dir1}: {g1-s1:.4f} [s]')

s2 = time()
# sample2.pdfの単語頻度、単語の意味のdictをそれぞれ取得
sample2_frequency = get_BoW(file_dir2)
sample2_meaning = get_meaning(file_dir2)
sample2_Wikipedia_frequency = get_Wikipedia_frequency(file_dir2)
sample2_IPA = get_IPA(file_dir2)
g2 = time()
print(f'Processing time on {file_dir2}: {g2-s2:.4f} [s]')

# 取得したBoW(dict)の内容をチェックするためにjsonファイルとして出力
# sample1.pdfの{'単語': 頻度}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample1_frequency.json'), 'w') as f:
    json.dump(sample1_frequency, f, indent = 4)
# sample2.pdfの{'単語': 頻度}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample2_frequency.json'), 'w') as f:
    json.dump(sample2_frequency, f, indent = 4)

# sample1.pdfの{'単語'; '辞書のエントリー'}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample1_meaning.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample1_meaning, f, indent = 4)
# sample2.pdfの{'単語'; '辞書のエントリー'}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample2_meaning.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample2_meaning, f, indent = 4)

# sample1.pdfの{'単語'; Wikipediaデータでの頻度}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample1_Wikipedia_frequency.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample1_Wikipedia_frequency, f, indent = 4)
# sample2.pdfの{'単語'; Wikipediaデータでの頻度}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample2_Wikipedia_frequency.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample2_Wikipedia_frequency, f, indent = 4)

# sample1.pdfの{'単語'; 'IPAの文字列'}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample1_IPA.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample1_IPA, f, indent = 4)
# sample2.pdfの{'単語'; 'IPAの文字列'}のdictを保存
with open(os.path.join(base_path, '../PDFtoBoW/test_results/sample2_IPA.json'), 'w', encoding = 'utf-8') as f:
    json.dump(sample2_IPA, f, indent = 4)

# {'単語': '辞書のエントリー'}のBoWについてちゃんと対応できているかテスト
print(sample1_meaning['activity'])
print(sample2_meaning['attributive'])

# IPAについてちゃんと出力できているかテスト
print(sample1_IPA['activity'])
print(sample2_IPA)

# 頻度データにスケーリングを処理したものが正しく出力されているかテスト
print(sample2_Wikipedia_frequency['attributive'])

