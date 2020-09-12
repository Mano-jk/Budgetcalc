FROM node:12.7-alpine AS build
COPY package.json package-lock.json ./
