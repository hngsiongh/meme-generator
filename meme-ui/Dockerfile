# Multi-Stage Build

# Building Stage
FROM node:18.12.1-alpine3.16 as build-stage
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/
RUN npm run build

# For Production
FROM nginx:1.22.1
COPY --from=build-stage /app/build/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
