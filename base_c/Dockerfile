FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3-pip
COPY . /base_c
WORKDIR /base_c
RUN pip3 install flask virtualenv SQLAlchemy==1.2.8 Flask-RESTful==0.3.6 gunicorn==19.8.1 pymodm==0.4.0 Faker
RUN virtualenv --python=python3 venv
ENV FLASK_APP=base_c 
ENV PLATAFORMA_SETTINGS=../settings.cfg 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["python3", "run.py"]