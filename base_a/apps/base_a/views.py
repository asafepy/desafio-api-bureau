from .models import Pessoa, Divida
from django.shortcuts import render
from .serializers import PessoaSerializer, DividaSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin


class PessoaViewSet(viewsets.ModelViewSet):

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class DividaViewSet(viewsets.ModelViewSet):

    queryset = Divida.objects.all()
    serializer_class = DividaSerializer
