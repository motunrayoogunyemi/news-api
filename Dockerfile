FROM python:3.7-alpine
LABEL MAINTAINER="Motunrayo Ogunyemi"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers \
&& pip install --upgrade pip \
&& pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
