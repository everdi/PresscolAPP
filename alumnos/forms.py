from django import forms
from alumnos.models import alumnos
from padres.models import Tutor
import datetime

class Alumno_Chido(forms.Form):
	alu_nombre = forms.CharField(label='Nombres:', widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
	alu_genero = forms.CharField(label='Genero:', widget=forms.TextInput(attrs={'class':'form-control'}))
	alu_tutores = forms.ModelMultipleChoiceField(queryset=Tutor.objects.all(),label='Tutores:')
	alu_vigente = forms.BooleanField(label='Vigente:', widget=forms.TextInput(attrs={'class':'form-control'}))
	alu_fechaIngreso = forms.DateField(label='Fecha de Ingreso:',initial=datetime.date.today, widget=forms.TextInput(attrs={'type':'date'}))
	alu_observaciones = forms.CharField(label='Observaciones:', widget=forms.TextInput(attrs={'class':'form-control'}))
	slug = forms.CharField(label='Slug:', widget=forms.TextInput(attrs={'class': 'form-control'}))

