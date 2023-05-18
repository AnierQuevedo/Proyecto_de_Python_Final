from django.db import models


class Presa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    nivel_agua = models.FloatField()
    ph = models.FloatField()
    capacidad_maxima = models.FloatField()
    temperatura_agua = models.FloatField()
    fecha_ultima_revision = models.DateField()