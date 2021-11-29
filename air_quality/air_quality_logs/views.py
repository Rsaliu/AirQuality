from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BaseAuthentication, BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import LogSerializer
from .models import Logs

class LogViewset(viewsets.GenericViewSet,mixins.ListModelMixin,
    mixins.CreateModelMixin,mixins.UpdateModelMixin):
    serializer_class = LogSerializer
    queryset = Logs.objects.all()

# Create your views here.
