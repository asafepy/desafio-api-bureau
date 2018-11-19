from rest_framework import serializers
from .models import Pessoa, Divida


class DividaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Divida
        fields = ('url', 'company', 'value', 'status', 'contract', 'pessoa')


class PessoaSerializer(serializers.HyperlinkedModelSerializer):

    dividas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pessoa
        fields = ('url', 'cpf', 'name', 'address', 'dividas')
