# 初回のみ必要
# import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('omw-1.4')

import PyPDF2
import re
from nltk.stem.wordnet import WordNetLemmatizer as WNL
from nltk.corpus import stopwords

wnl = WNL()
stop_words = stopwords.words('english')

def get_BoW(file_dir):
    ### file_dir: str
    ### returns a list of strings (lemmatized wrods)
    with open(file_dir, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        BoW = []
        # 各ページごとに文字列を単語へ分割、レマ化を行いリストへ保存
        for i in range(reader.getNumPages()):
            page = reader.getPage(0)
            raw_text = page.extractText()
            # 改行部分の処理としてハイフンと改行文字の除去を行う
            bar = raw_text.translate(str.maketrans({'-': None, '\n': None}))
            # 正規表現を用いて英単語以外の余計なものを除去する
            formatted_text = re.split(r'[^a-zA-Z]+', bar)
            # レマ化を行い単語がstop_wordsに含まれている場合はBoWには追加しない
            for word in formatted_text:
                lemmatized_word = wnl.lemmatize(word)
                if lemmatized_word not in stop_words:
                    BoW.append(lemmatized_word)
    return BoW