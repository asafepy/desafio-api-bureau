import datetime
import string
import random
from faker import Faker

fake = Faker()

def char_fake(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def char_digits_fake(size=50, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def name_fake():
    return fake.name()

def address_fake():
    return fake.address()

def company_fake():
    return fake.name()

def value_fake():
    return random.randrange(999)

def status_fake():
    return fake.name()

def contract_fake():
    return random.randrange(999)

def date_fake():
    return fake.date()
