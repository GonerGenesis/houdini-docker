FROM node:18-alpine

ENV NODE_ENV development

WORKDIR /usr/src/app

# ENV PATH /app/node_modules/.bin:$PATH
# ENV YARN_RC_FILENAME=.yarnrc.yml

COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "yarn.lock", "./"]
# Install Node modules
RUN yarn

COPY . .