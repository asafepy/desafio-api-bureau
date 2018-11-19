from .models import Person
from django.shortcuts import render
from .serializers import PersonSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin


class PersonViewSet(PermissionTokenLoginRequiredMixin,
                    viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
