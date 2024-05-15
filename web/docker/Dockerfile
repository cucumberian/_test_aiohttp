FROM python:3.11.9-slim-bookworm

ENV HOME_DIR /home/web/
ENV APP_DIR ${HOME_DIR}/app

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY . .

RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt
