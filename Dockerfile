FROM python:3.6-alpine

COPY ./p2/ /app/p2
COPY ./manage.py /app/
COPY ./requirements.txt /app/

RUN apk update && \
    apk add --no-cache openssl-dev libmagic build-base jpeg libffi-dev gcc musl-dev libgcc openssl-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev postgresql-dev && \
    pip install -U pip gunicorn --no-cache-dir && \
    pip install -r /app/requirements.txt  --no-cache-dir && \
    adduser -S p2 && \
    chown -R p2 /app

USER p2

WORKDIR /app/
