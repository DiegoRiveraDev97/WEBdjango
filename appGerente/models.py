from django.db import models

# Create your models here.
class Heladeria (models.mode1):
    nombreHeladeria = models.CharField(max_length=100, null=False)
    nombreGerente = models.CharField(max_length=100, null=False)
    nitHeladeria = models.IntegerField(unique=True)
    correoGerente = models.CharField(max_length=100, null=False)
    cedulaGerente = models.IntegerField(null=False)
    ubicacionHeladeria = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.nombreHeladeria
    
