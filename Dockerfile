FROM python:3.7-slim-stretch
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app app
COPY migrations migrations
COPY microblog.py config.py ./
ENV FLASK_APP microblog.py
EXPOSE 5000
CMD flask run -h 0.0.0.0