from rest_framework import serializers
from .models import Pessoa, Bem


class BemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bem
        fields = ('url', 'nome_bem', 'pessoa')
        

class PessoaSerializer(serializers.HyperlinkedModelSerializer):

    bens = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pessoa
        fields = ('url', 'cpf', 'nome', 'idade', 'renda', 'bens')
