from rest_framework import serializers
from .models import Pessoa, Bem


class BemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bem
        fields = ('nome_bem',)
        

class PessoaSerializer(serializers.HyperlinkedModelSerializer):

    bens = BemSerializer(many=True)

    class Meta:
        model = Pessoa
        fields = ('cpf', 'nome', 'idade', 'renda', 'bens')
