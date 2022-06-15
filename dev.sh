docker compose down
docker-compose rm

docker compose up -d

# 下のコマンドでUser登録をするが,二回目以降はvolumeに情報があるため``DETAIL:  Key (username)=(name18) already exists.``となるため消しても問題ない.
# また,2回目以降はdev.shを使う必要性も薄い.

docker-compose exec web sh -c "echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('name18', 'userEmail', 'pass18')\" | python3 manage.py shell"

# 5個だけDBを勝手に登録する, もし登録したくない場合はここは省略しても良い
docker compose exec web python3 for_dev_CR.py 5

docker compose down
docker compose up
