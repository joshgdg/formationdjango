# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /appli
COPY requirements.txt /appli/
RUN pip install -r requirements.txt
COPY . /appli/

