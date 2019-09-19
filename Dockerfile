FROM python:3.7.4-stretch

ENV PYTHONWARNINGS ignore
ENV PYTHONUNBUFFERED 1
#ENV SECRET_KEY NOT_SO_SECRET_KEY

COPY requirements.txt .
RUN pip install -Ur requirements.txt --quiet

WORKDIR /webapps

EXPOSE 8000
