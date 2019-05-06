from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
# Create your models here.

class Padre(models.Model):
    tut_nombre = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    tut_apellidos = models.CharField(max_length = 150, null = True)
    tut_numero = models.CharField(max_length = 15, null = True)
    tut_parentesco = models.CharField(max_length = 15, null = True)
    tut_descripcion = models.CharField(max_length = 15, null = True)
    tut_domicilio = models.CharField(max_length = 400, null = True)
    
    
    def __str__(self):
        return self.tut_nombre.username
    
    class Meta:
        
        permissions = (
            ('is_tutorr', 'Is_Tutorr'),
        )