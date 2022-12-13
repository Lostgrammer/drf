from django.db import models

#agregando modelos de la drf app
class Pais(models.Model):
    nombre = models.CharField(max_length=20)
    moneda = models.CharField(max_length=20)
    creado_en = models.DateTimeField(auto_now_add=True) #para que se agregue cada vez que se crea un nuevo dato

