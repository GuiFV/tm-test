FROM python:3.12-slim

RUN apt update

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "app:app"]