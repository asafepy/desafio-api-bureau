from .models import Pessoa, Bem
from django.shortcuts import render
from .serializers import PessoaSerializer, BemSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin
from rest_framework.renderers import JSONRenderer


class PessoaViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class BemViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
