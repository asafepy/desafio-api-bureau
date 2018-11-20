import django_filters
from .models import Pessoa

class PessoaFilter(django_filters.FilterSet):
    class Meta:
        model = Pessoa
        fields = ['cpf']