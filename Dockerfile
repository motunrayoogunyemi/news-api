FROM python:3.7-alpine
LABEL MAINTAINER="Motunrayo Ogunyemi"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    postgresql-dev
RUN apk add --no-cache gcc musl-dev linux-headers \
&& pip install --upgrade pip \
&& pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

RUN python app/manage.py crontab add