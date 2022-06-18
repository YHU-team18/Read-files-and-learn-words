import os
from math import log
import PyPDF2
# 初回のみ必要
if not os.path.isfile('/root/nltk_data/corpora/wordnet'): # データが存在しない場合ダウンロードする
    import nltk
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('omw-1.4')
from nltk.stem.wordnet import WordNetLemmatizer as WNL
from nltk.corpus import stopwords

wnl = WNL()
stop_words = stopwords.words('english')

with open("words_by_frequency.txt", 'r') as f:
    words = f.read().split()

wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """スペースの入っていない未分割の単語文字列に対してスペースの位置を推測する
        Wikipediaの単語頻度データを利用: https://github.com/IlyaSemenov/wikipedia-word-frequency
    Args:
        s (_str_): 未分割の単語文字列
    Returns:
        _str_ : スペースによって分割された単語を含む文字列
    """
    def best_match(i): # Returns a pair of (match_cost, match_length)
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # コストのリスト
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # コストの最も低くなる分割を探す
    output = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        output.append(s[i-k:i])
        i -= k

    return " ".join(reversed(output))

def get_BoW(file_dir):
    """pdfファイルのパスを受け取り,BoWを返す
    Args:
        file_dir (_str_): PDFファイルのパス

    Returns: 
        _dict_: 英単語がkey,pdf内での出現回数がvalueになったdict
    """
    with open(file_dir, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        BoW = {}
        # 各ページごとに文字列を単語へ分割後,レマ化を行いリストへ保存
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            raw_text = page.extractText()
            # 改行部分の処理としてハイフンと改行文字の除去を行う
            bar = raw_text.translate(str.maketrans({'-': None, '\n': None}))
            for i in bar.split():
                # スペースで分割できなかった単語に対しての分割を行う
                candidate_words = infer_spaces(i).split()
                for word in candidate_words:
                    lemmatized_word = wnl.lemmatize(word)
                    if (lemmatized_word not in stop_words) and (len(lemmatized_word) > 1):
                        BoW.setdefault(lemmatized_word, 0)
                        BoW[lemmatized_word] += 1

    return BoW