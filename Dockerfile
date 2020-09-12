FROM node:current-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
RUN npm install bulma
COPY . .
RUN npm rebuild node-sass
RUN npm run build
