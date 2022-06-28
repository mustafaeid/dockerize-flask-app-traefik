FROM python:3.7-slim-stretch
COPY requirements.txt requirements.txt
RUN apt-get update -y && apt-get install mysql-server -y && apt-get install python-dev -y
RUN apt-get install libmariadbclient-dev -y && apt-get install gcc -y && pip install -r requirements.txt
COPY . app
WORKDIR /app
EXPOSE 5000
CMD flask run -h 0.0.0.0