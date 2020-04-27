FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./django-requirements.txt ./

RUN pip install -r django-requirements.txt && rm django-requirements.txt
