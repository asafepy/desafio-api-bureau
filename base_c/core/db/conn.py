import os

from pymodm import connect


LOCALHOST_URL = 'mongodb://localhost:27017/base_c'
MONGO_URL = os.getenv('MONGO_URL', LOCALHOST_URL)


def get_connection():
    connect(MONGO_URL)
