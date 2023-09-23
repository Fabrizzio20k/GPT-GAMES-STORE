FROM node:alpine

WORKDIR /app

COPY package.json /app

RUN npm install -g serve

COPY . .

RUN npm run build

EXPOSE 8080