import os

if not os.path.isdir('/root/nltk_data/corpora/wordnet'): # データが存在しない場合ダウンロードする
    import nltk
    nltk.download('wordnet')
    nltk.download('stopwords')
    nltk.download('omw-1.4')
