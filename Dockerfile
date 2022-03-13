# syntax=docker/dockerfile:1
FROM python:3.8.9-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update \
  && apt-get install -y libpq-dev python3-dev gcc \
  && pip install --upgrade pip
RUN pip install -r requirements.txt && pip install -r requirements_dev.txt
COPY . /app/
