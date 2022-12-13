from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais
from .serializer import PaisSerializado

@api_view(['GET','POST'])
def pais(request):
    if request.method =='POST':  #ingresar datos
        #print(request.data) #
        serializer = PaisSerializado(data=request.data)
        #si se comprueba la serializacion guardamos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif(request.method=='GET'):  #pedir datos de pagina
        objr = Pais.objects.all()
        serializer = PaisSerializado(objr,many=True)
        return Response(serializer.data)

    return Response('')
# Create your views here.
