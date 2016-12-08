#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "usage: $0 <environment_name>"
    exit 1
fi

ENV=$1

ecs-cli configure --region eu-west-1 --cluster cluster01
ecs-cli compose --project-name $ENV --file docker-compose.$ENV.yml service stop
