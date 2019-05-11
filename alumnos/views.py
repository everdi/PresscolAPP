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

def Index(request):
    user = request.user
    if user.is_active is True:
        if user.is_staff is False :
            if user.has_perm('padres.is_teacher'):
                yar = datetime.now().year
                today = date.today()
                wk = today.isocalendar()[1]
                inicio, fin = get_week_days(yar ,wk)
                prf = Profesor.objects.get(pro_nombre = user)
                grp = grupos.objects.select_related().filter(gru_maestro = prf)
                almGRUP = []
                for k in grp:
                    almGRUP.append({"Alumnos": k.gru_alumnos.all(), "Grupo": k.id})

                evaluacionesArray = []
                for j in range(len(almGRUP)):
                    kj = []
                    for hj in almGRUP[j]['Alumnos']:
                        kj.append(hj.id)

                    diarios = []
                    amevals = []
                    evalpos = []
                    

                    diar = DiarioTrabajo.objects.select_related().filter(DT_fecha = today).filter(DT_alumno__id__in = kj)
                    idDiar = []
                    aluDiar = []           
                    for ml in diar:
                        idDiar.append(ml.id)
                        aluDiar.append(ml.DT_alumno.id)

                    diarios.append({"Diario": idDiar, "Alumno": aluDiar})
                    evaluacionesArray.append({"Grupo": almGRUP[j]['Grupo'], "Alumnos": amevals, "EvalId": evalpos, "Diario": diarios})
                ctx = {"Perfil": prf, "Grupos": grp, "Evaluados": evaluacionesArray}
                print(ctx)
            if user.has_perm('padres.is_tutorr'):
                tur = Tutor.objects.get(tut_nombre = user)
                alm = alumnos.objects.filter(alu_tutores__in = [tur])
                ctx = {"Alumno":alm}        
            
            return render(request,'alumnos/index.html', ctx)
        else:
            return render(request,'alumnos/index.html')
        
    return render(request,'alumnos/index.html')
