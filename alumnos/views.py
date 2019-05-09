from django.shortcuts import render
from alumnos.models import alumnos
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView,DetailView, UpdateView, DetailView, FormView
from alumnos.forms import Alumno_Chido
from django.urls import reverse_lazy
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from padres.models import Tutor, Profesor

import string
from datetime import date, timedelta, datetime


# Create your views here.

class AgregarAlumConEstilo(FormView):
    template_name = "alumnos/crear.html"
    form_class = Alumno_Chido
    success_url = reverse_lazy('alumnos_reporte')
    
    def form_valid(self, form):
        alu = alumnos()
        alu.alu_nombre = form.cleaned_data['alu_nombre']
        alu.alu_genero = form.cleaned_data['alu_genero']
        alu.save()
        gen = form.cleaned_data['alu_genero']
        if gen == 'Masculino':
            alu.alu_foto = 'media/default/boy.png'
        else:
            alu.alu_foto = 'media/default/girl.jpg'
        alu.alu_tutores.set(form.cleaned_data['alu_tutores'])
        alu.alu_vigente = form.cleaned_data['alu_vigente']
        alu.alu_fechaIngreso = form.cleaned_data['alu_fechaIngreso']
        alu.alu_observaciones = form.cleaned_data['alu_observaciones']
        alu.slug =form.cleaned_data['slug']
        alu.save()
        return super(AgregarAlumConEstilo,self).form_valid(form)

