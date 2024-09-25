FROM python:3.12.6-alpine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt