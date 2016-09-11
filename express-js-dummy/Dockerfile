# https://github.com/mhart/alpine-node
# https://hub.docker.com/r/mhart/alpine-node/
# node 6.5.0 with npm 3.10.6 – 49.32 MB
FROM mhart/alpine-node:6.5.0

MAINTAINER android110909@gmail.com

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

WORKDIR express-js-dummy
ADD app.js .
ADD package.json .

RUN npm install

EXPOSE 3000
CMD ["node", "app.js"]

HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://127.0.0.1:3000/ || exit 1
