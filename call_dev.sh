docker compose down
docker-compose rm

docker compose up -d

docker-compose exec web sh dev.sh

docker compose down
