FROM python:3.11.9-slim


EXPOSE 8000


WORKDIR /app


RUN pip install --no-cache-dir \
    Django==5.2.17 \
    djangorestframework \
    "psycopg[binary]"


ENV PYTHONUNBUFFERED=1

