#!/bin/sh

#cd "dirname $0"

# 念のため、終了
docker compose down
docker compose up
docker compose down
