import datetime
import json
import string
import random
from faker import Faker

fake = Faker()

def char_generator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def char_digits_generator(size=50, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def name_generator():
    return fake.name()

def address_generator():
    return fake.address()

def company_generator():
    return fake.name()

def value_generator():
    return random.randrange(999)

def status_generator():
    return fake.name()

def contract_generator():
    return random.randrange(999)

def date_generator():
    return datetime.datetime.strptime(fake.date(), '%Y-%m-%d')

def datetime_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.__str__()

def person_trail_serializer(person_trail):
    person_dict = person_trail.to_son().to_dict()
    return json.loads(json.dumps(person_dict, default=datetime_serializer))