#https://docs.docker.com/compose/environment-variables/
export PORT=$(python get-port.py)
echo "App is exposed on $PORT"

#inspired by https://docs.docker.com/compose/extends/
docker-compose -p "env_$(pwgen -s -1 4)" -f docker-compose.core.yml -f docker-compose.extra.yml up
