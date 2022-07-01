# Read-files-and-learn-words

Read files and learn words(RFLW,仮称)は、PDF等のファイルを読み込ませることでファイル内に含まれる単語を(一般での)頻度別に学習できるWebアプリ  
Docker上でDjango,PostgreSQLを使用するWebアプリケーションになっている。

## セットアップ手順

1. `git clone https://github.com/YHU-team18/Read-files-and-learn-words.git`をして,`cd Read-files-and-learn-words`をする。
1. `sh start.sh`(Windows環境の場合は`./start.bat`)する。
1. Webブラウザで`localhost:8000/menu`にアクセスする。

### dev

1. `docker compose up -d`をした後に
1. `docker compose exec web sh dev.sh`でadminの追加をする. それ以降は上のセットアップと同じ.

## DBについて

DBには、PostgreSQLを使用しており、以下の通り設定されている。

```txt
DB = postgres
USER = db_user
PASSWORD = db_pass
```

これらを変更するには、`./yhu_t18/settings.py`, `./docker-compose.yaml`の両方を更新する必要がある。

# LICENCEについて

- このリポジトリは MIT License で提供しています.
- また,使用したデータやライブラリ,参考にした資料は`ThirdPartyNotices.txt`をご覧ください.
