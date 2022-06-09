FROM python:3.8-alpine
WORKDIR /mail
RUN apk add build-base
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
