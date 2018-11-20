from django.db import models


class Pessoa(models.Model):

    cpf = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    renda = models.CharField(max_length=100)

    def __str__(self):
        return 'Pessoa: Cpf=%s, Nome=%s' % (self.cpf, self.nome)


class Bem(models.Model):

    nome_bem = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa,
                               related_name='bens',
                               on_delete=models.CASCADE)

    def __str__(self):
        return 'Bem: Propriedade=%s, Pessoa=%s' % (self.nome_bem, self.pessoa.nome)
