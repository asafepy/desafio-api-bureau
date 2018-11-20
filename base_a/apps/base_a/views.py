from .models import Pessoa, Divida
from django.shortcuts import render
from .serializers import PessoaSerializer, DividaSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin
from rest_framework.renderers import JSONRenderer
from .filters import PessoaFilter


class PessoaViewSet(viewsets.ModelViewSet):
    
    renderer_classes = (JSONRenderer, )
    filter_class = PessoaFilter
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class DividaViewSet(viewsets.ModelViewSet):
    
    renderer_classes = (JSONRenderer, )
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer
