FROM python:3.8.3-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python hello_kedro.py
