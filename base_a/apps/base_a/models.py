from django.db import models


class Pessoa(models.Model):
    __tablename__ = 'pessoa'

    cpf = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return 'Pessoa: Cpf=%s, Nome=%s' % (self.cpf, self.name)


class Divida(models.Model):
    __tablename__ = 'divida'

    company = models.CharField(max_length=100)
    value = models.IntegerField()
    status = models.CharField(max_length=100)
    contract = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa,
                               related_name='dividas',
                               on_delete=models.CASCADE)

    def __str__(self):
        return 'Divida: Compania=%s, Valor=%s' % (self.company, self.value)
