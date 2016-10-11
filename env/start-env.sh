#!/usr/bin/env bash

eval "$(docker-machine env -u)"

MACHINE_IP="$(docker-machine ip composeHost)"
ENV="$(pwgen -A -s -1 4 | tr '[:upper:]' '[:lower:]')"

echo "Generating environment with id $ENV"

docker run --rm -it -u $(id -u):$(id -u) -v $(pwd):/composer/project laszlocph/composer compose --env $ENV

#https://docs.docker.com/compose/environment-variables/
export PORT=$(python get-port.py)

eval "$(docker-machine env composeHost)"
#inspired by https://docs.docker.com/compose/extends/
docker-compose -p $ENV -f docker-compose.$ENV.yml up -d

echo
echo "Environment $ENV is exposed on http://$MACHINE_IP:$PORT"
echo
docker-compose -p $ENV ps
echo
docker ps
