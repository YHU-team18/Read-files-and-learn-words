# Django-on-Docker

Docker上でDjangoを実行するための各種スクリプト

## セットアップ手順

1. `git clone https://github.com/YHU-team18/Django-on-Docker.git`する。
1. `sh ./setup.sh`(Windows環境の場合は`./setup.sh`)する。
1. Webブラウザで`localhost:8000`にアクセスする。

## DBについて

DBには、PostgreSQLを使用しており、以下の通り設定されている。

```txt
DB = postgres
USER = db_user
PASSWORD = db_pass
```

これらを変更するには、`./yhu_t18/settings.py`, `./docker-compose.yaml`の両方を更新する必要がある。
