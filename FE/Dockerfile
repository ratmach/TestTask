FROM node:21-alpine3.17 as builder


RUN mkdir /react-ui
WORKDIR /react-ui

RUN mkdir ./public
RUN mkdir ./src
COPY ./calculator/public ./public
COPY ./calculator/src ./src
COPY ./calculator/tsconfig.json ./tsconfig.json
COPY ./calculator/package.json ./package.json
COPY ./calculator/package-lock.json ./package-lock.json
RUN npm install
RUN npm run build


FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /react-ui/build /usr/share/nginx/html

EXPOSE 3000 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]