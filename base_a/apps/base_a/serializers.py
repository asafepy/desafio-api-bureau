from rest_framework import serializers
from .models import Pessoa, Divida


class DividaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Divida
        fields = ('company', 'value', 'status', 'contract')


class PessoaSerializer(serializers.ModelSerializer):

    dividas = DividaSerializer(many=True)

    class Meta:
        model = Pessoa
        fields = ('cpf', 'name', 'address', 'dividas')
