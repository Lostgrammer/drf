from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais
from .serializer import PaisSerializado

@api_view(['GET','POST'])
def pais(request):
    return Response('')

# Create your views here.
