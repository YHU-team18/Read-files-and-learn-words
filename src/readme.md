# About Files

```
.
├── manage.py
├── readme.md
├── templates
│   ├── add_word.html # PDFを介さないで,DBにWordを追加する. (AddWords classが対応(words/views.pyで確認できる))
│   ├── all_list.html
│   ├── base.html # 全てのhtmlに共通する雛形の形
│   ├── input_pdf.html
│   ├── menu.html
│   ├── quiz.html
│   ├── detail.html
│   └── update_i.html
├── words
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py # DBの型を指定しているクラスを定義するファイル
│   ├── tests.py
│   ├── urls.py # pathとclassの対応付等を設定をしているファイル
│   └── views.py # Classを定義しているファイル(urlの対応が書いてある)
└── yhu_t18
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
