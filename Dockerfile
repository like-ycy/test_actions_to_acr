FROM python:3.8.12

LABEL Author="wang"

ENV PYTHONUNBUFFERED 1

COPY ./exam /exam
COPY ./sources.list /etc/apt/sources.list

RUN apt update && apt install gcc make -y

WORKDIR /exam

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "uwsgi", "--ini", "/exam/uwsgi.ini" ]