#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "usage: $0 <environment_name>"
    exit 1
fi

ENV=$1

docker-compose -p $ENV -f docker-compose.yml stop
docker-compose -p $ENV -f docker-compose.yml rm --all -f
