from PDFtoBoW import get_BoW
from time import time
import json

file_dir1 = 'sample1.pdf' # Size of sample1: 441 words
file_dir2 = 'sample2.pdf' # Size of sample2: 552 words

# 処理時間を計測
s = time()
BoW1 = get_BoW(file_dir1)
g = time()
print('Test result on sample1:')
print(f'Processing time: {g-s:.4f} [s]')

s = time()
BoW2 = get_BoW(file_dir2)
g = time()
print('Test result on sample2:')
print(f'Processing time: {g-s:.4f} [s]')

# with open('test_BoW1.json', 'w') as f:
#     json.dump(BoW1, f, indent = 4)

# with open('test_BoW2.json', 'w') as f:
#     json.dump(BoW2, f, indent = 4)