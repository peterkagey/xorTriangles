FROM amazon/aws-lambda-python:3.8

RUN pip install tweepy
RUN pip install Pillow -t .

COPY rows2.json ./
COPY rows3.json ./
COPY seed_maker.py ./
COPY triangle_grower.py ./
COPY triangle_drawer.py ./
COPY secrets.py ./
COPY twitter_connection.py ./
COPY app.py ./

CMD ["app.handler"]
