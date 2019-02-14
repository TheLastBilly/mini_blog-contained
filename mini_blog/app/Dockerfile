FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY . /usr/src/app/

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
