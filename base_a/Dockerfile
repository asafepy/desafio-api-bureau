FROM python:3.6

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/base_a

ADD requirements.txt $WEBAPP_DIR/

RUN mkdir -p /var/log/gunicorn


WORKDIR $WEBAPP_DIR

RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/