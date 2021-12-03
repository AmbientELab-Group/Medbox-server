FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt && rm requirements.txt

RUN mkdir -p /staticfiles
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /usr/src/app && \ 
 chmod 755 /usr/src/app/
USER user

COPY ./app ./

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
