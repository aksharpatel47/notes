FROM node:12-alpine

WORKDIR /home/node

COPY index.js package-lock.json package.json ./

RUN npm i

CMD [ "node", "index.js" ]

