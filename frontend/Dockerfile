FROM node:alpine

WORKDIR /app

COPY package.json /app

RUN npm install -g serve
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000