#para que tranforme un modelo en json
#importamos del rest el serializer
from rest_framework import serializers
from .models import Pais
class PaisSerializado(serializers.ModelSerializer): #indicar que este serializer sea del modelo
    class Meta:
        model = Pais #de que modelo viene
        field = ('nombre','moneda') #campos del modelo
        read_only_fields = ('creado_en') #campo de solo lectura