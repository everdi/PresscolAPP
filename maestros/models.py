from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
# Create your models here.

class Maestro(models.Model):
    pro_nombre = models.OneToOneField(User, on_delete= models.CASCADE, null = True)
    pro_nombres = models.CharField(max_length=80, default='s')
    pro_apellidoPaterno =models.CharField(max_length=70, default = 's')
    pro_apellidoMaterno = models.CharField(max_length=70, default = 's')
    pro_fechaNacimento = models.DateField(default = datetime.now, blank = True)
    
    def __str__(self):
        return str(self.pro_nombre.username)
    
    class Meta:
        
        permissions = (
            ('is_teacher', 'Is_Teacher'),
        )