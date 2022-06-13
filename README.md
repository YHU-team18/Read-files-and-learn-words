# Read-files-and-learn-words

Read files and learn words(RFLW,仮称)は、PDF等のファイルを読み込ませることでファイル内に含まれる単語を(一般での)頻度別に学習できるWebアプリ  
Docker上でDjango,PostgreSQLを使用するWebアプリケーションになっている。

## セットアップ手順

1. `git clone https://github.com/YHU-team18/Read-files-and-learn-words.git`する。
1. `sh ./Read-files-and-learn-words/setup.sh`(Windows環境の場合は`./Read-files-and-learn-words/setup.bat`)する。
1. Webブラウザで`localhost:8000`にアクセスする。

## DBについて

DBには、PostgreSQLを使用しており、以下の通り設定されている。

```txt
DB = postgres
USER = db_user
PASSWORD = db_pass
```

これらを変更するには、`./yhu_t18/settings.py`, `./docker-compose.yaml`の両方を更新する必要がある。
