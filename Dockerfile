FROM node AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm rebuild node-sass
RUN npm run build
