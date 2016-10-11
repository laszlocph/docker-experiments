#!/usr/bin/env bash
docker run -it --rm --network=host -v jenkins_home_1000:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker laszlocph/jenkins-with-sudo:latest
