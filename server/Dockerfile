FROM debian:buster

WORKDIR ./home

RUN apt-get update -y

RUN apt-get install python3-pip -y

COPY . .

RUN pip3 install nba_api flask

RUN pip3 freeze > requirements.txt

RUN export FLASK_APP=app.py

EXPOSE 5000

#flask run --host=0.0.0.0