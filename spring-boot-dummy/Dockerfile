FROM anapsix/alpine-java:8_jdk

ARG user

WORKDIR spring-boot-dummy
ADD . .
RUN chown -R $user:$user .

USER $user
CMD sleep 1h