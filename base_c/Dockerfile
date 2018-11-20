FROM python:3.6
EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/base_c/base_c

ADD requirements.txt $WEBAPP_DIR/

ADD . $WEBAPP_DIR/
WORKDIR $WEBAPP_DIR
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind=0.0.0.0:5000", "app:app"]