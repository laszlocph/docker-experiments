#!/usr/bin/env bash

ecs-cli configure --region eu-west-1 --cluster cluster01
ENV="$(pwgen -A -s -1 4 | tr '[:upper:]' '[:lower:]')"

echo "Generating environment with id $ENV"

docker run --rm -it -u $(id -u):$(id -u) -v $(pwd):/composer/project laszlocph/composer compose --env $ENV

#https://docs.docker.com/compose/environment-variables/
export PORT=$(python get-port.py)

#inspired by https://docs.docker.com/compose/extends/
ecs-cli compose --project-name $ENV --file docker-compose.$ENV.yml service up

MACHINE_IP="TODO"

echo
echo "Environment $ENV is exposed on http://$MACHINE_IP:$PORT"
echo
ecs-cli compose --project-name $ENV --file docker-compose.$ENV.yml service ps
echo
