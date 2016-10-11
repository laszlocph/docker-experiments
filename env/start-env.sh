#!/usr/bin/env bash

MACHINE_IP="$(docker-machine ip composeHost)"
ENV="$(pwgen -s -1 4)"

#https://docs.docker.com/compose/environment-variables/
export PORT=$(python get-port.py)
echo "Environment $ENV is exposed on http://$MACHINE_IP:$PORT"

eval "$(docker-machine env composeHost)"

#inspired by https://docs.docker.com/compose/extends/
docker-compose -p $ENV -f docker-compose.yml up -d
