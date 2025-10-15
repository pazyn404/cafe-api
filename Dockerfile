FROM python:3.11-slim

WORKDIR /api
COPY dev/requirements.txt .
RUN pip install -r requirements.txt
