FROM python:3.8.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers libressl-dev musl-dev libffi-dev\
    && pip install Pillow
RUN sudo apk add gcc musl-dev python3-dev libffi-dev openssl-dev
COPY . .