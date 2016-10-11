#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "usage: $0 <environment_name>"
    exit 1
fi

ENV=$1

eval "$(docker-machine env composeHost)"
docker-compose -p $ENV -f docker-compose.$ENV.yml stop
docker-compose -p $ENV -f docker-compose.$ENV.yml rm --all -f
