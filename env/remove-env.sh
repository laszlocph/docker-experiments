#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "usage: $0 <environment_name>"
    exit 1
fi

ENV=$1

eval "$(docker-machine env composeHost)"
docker-compose -p $ENV stop
docker-compose -p $ENV rm --all -f
