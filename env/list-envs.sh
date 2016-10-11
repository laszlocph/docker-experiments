#!/usr/bin/env bash

eval "$(docker-machine env composeHost)"
docker ps
