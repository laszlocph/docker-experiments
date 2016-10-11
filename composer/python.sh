#!/usr/bin/env bash

docker build -t laszlocph/yaml-parser .
docker run --rm -it laszlocph/yaml-parser python composer.py compose --without=web,redis
