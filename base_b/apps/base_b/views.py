from .models import Pessoa, Bem
from django.shortcuts import render
from .serializers import PessoaSerializer, BemSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin


class PessoaViewSet(viewsets.ModelViewSet):

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class BemViewSet(viewsets.ModelViewSet):

    queryset = Bem.objects.all()
    serializer_class = BemSerializer
