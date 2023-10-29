# stage1 as builder
FROM node:21-alpine3.17 as builder

# copy the package.json to install dependencies
COPY calculator/package.json calculator/package-lock.json ./

# Install the dependencies and make the folder
RUN npm install && mkdir /react-ui && mv ./node_modules ./react-ui

WORKDIR /react-ui

COPY ./calculator/ .

RUN npm run build


FROM nginx:alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /react-ui/build /usr/share/nginx/html

EXPOSE 3000 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]