FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt && rm requirements.txt

RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /usr/src/app
USER user

COPY ./src ./
