from django.db import models


class Person(models.Model):
    __tablename__ = 'person'

    cpf = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __repr__(self):
        return f'<Person(cpf={self.cpf}, name={self.name})>'


class Divida(models.Model):
    __tablename__ = 'divida'

    company = models.CharField(max_length=100)
    value = models.IntegerField()
    status = models.CharField(max_length=100)
    contract = models.IntegerField()

    person_cpf = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __repr__(self):
        return f'<Divida(company={self.company}, value={self.value})>'
