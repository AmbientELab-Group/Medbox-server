FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./falcon-requirements.txt ./

RUN pip install -r falcon-requirements.txt && rm falcon-requirements.txt

RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /usr/src/app
USER user

CMD ["gunicorn", "-b", "0.0.0.0:8001", "main:app"]
