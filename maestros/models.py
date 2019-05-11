from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from padres.models import Profesor
from alumnos.models import alumnos
from datetime import datetime
# Create your models here.

class grupos(models.Model):
    gru_clave = models.CharField(max_length = 10)
    gru_maestro = models.ForeignKey(Profesor, on_delete=models.CASCADE, blank=True, null=True, related_name="Maestro")
    gru_alumnos = models.ManyToManyField(alumnos)
    gru_salon = models.CharField(max_length = 10, default='')
    gru_grado = models.IntegerField(null=True)
    
    def __str__(self):
        return self.gru_clave
        
    
class DiarioTrabajo(models.Model):
    DT_maestro = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    DT_alumno = models.ForeignKey(alumnos, on_delete= models.CASCADE)
    DT_fecha = models.DateField(auto_now_add = True)
    DT_descripcion = models.TextField()
    DT_actividadApoyo = models.TextField()
    DT_necesidades = models.TextField()

    def __str__(self):
        return str(self.DT_alumno)
    