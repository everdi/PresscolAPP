from django.shortcuts import render
from .models import Tutor
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Permission
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .forms import AddTutorForm
from django.views import generic
from alumnos.models import alumnos
import json
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            return render(request, 'log/in.html')
    else:
        return render(request, 'log/in.html')

def updateTutores(request):
    url = '/'
    if request.method == 'POST':
        slug = request.POST['slug']
        alm = alumnos.objects.get(slug = slug)
        tuto = json.loads(request.POST['alu_tutores'])
        alm.alu_tutores.clear()
        alm.save()
        for x in range(len(tuto)):
            tut = (tuto[x]['Usuario'])
            usu = User.objects.get(username = tut)
            tutor = Tutor.objects.get(tut_nombre = usu)
            alm.alu_tutores.add(tutor)
        alm.save()
        url='/addtutor/' + str(slug)

    return HttpResponseRedirect(url)

class addTutor(generic.FormView):
    template_name = 'padres/agregar.html'
    form_class = AddTutorForm
    success_url = reverse_lazy('reporteTutor')
    
    def form_valid(self, form):
        Usr = form.save()
        prm = Permission.objects.get(codename='is_tutorr')
        Usr.user_permissions.add(prm)
        tut = Tutor()
        tut.tut_nombre = Usr
        tut.tut_apellidos = form.cleaned_data['fname'] + ' ' + form.cleaned_data['lname'] + ' ' + form.cleaned_data['apellidoM']
        tut.tut_descripcion = form.cleaned_data['descrip']
        tut.tut_domicilio = form.cleaned_data['domicilio']
        tut.tut_numero = form.cleaned_data['telefono']
        tut.tut_parentesco = form.cleaned_data['parent']
        tut.save()
        return super(addTutor,self).form_valid(form)
        