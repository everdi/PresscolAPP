"""PresscolAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login
from alumnos.views import Index , AlumnoReporte, busquedaTurores,ReporteNoChafa, busquedaAlumno,Detail_ninja, Update_Alumno, Detail_Alumno, AgregarAlumConEstilo, EvaluarAlumno, EvaDiario, detalleEvalSem, detalleDiario, DiarioReporte, EvaluacionReporte, reporteEvaluacionAlumno, reporteDiarioAlumno

from padres.views import login, addTutor, tutorAsign,updateTutores, TutoresReporte, Detail_Tutor, ActualizarTutores

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^alumnos/agregar',AgregarAlumConEstilo.as_view(),name='alumnos_agregarxd'),
    url(r'login/', login, name='login'),
    url(r'^$',Index, name='index'),
    path('evaluar/<slug:slug>', EvaluarAlumno.as_view()),
    url(r'^padres/agregar', addTutor.as_view(), name="AddTutor"),
    path('addtutor/<slug:slug>', tutorAsign),
    path('Actualizar/Tutores', updateTutores),
    path('tutor/buscar', TutoresReporte.as_view(), name='reporteTutor'),
    path('detalles/tutor/<slug:slug>', Detail_Tutor),
    path('actualiza/tutor/<slug:slug>', ActualizarTutores),
    path('reporte/diarioalu/<slug:slug>', reporteDiarioAlumno),
    path('detalle/evaluacion/semanal/<slug:slug>', detalleEvalSem),
    path('detalle/evaluacion/diario/<slug:slug>', detalleDiario),
    url(r'^reporte/diario', DiarioReporte.as_view(),name="reporteDiario"),
    url(r'^reporte/evaluacion', EvaluacionReporte.as_view(),name="reporteEvaluacion"),
    path('reporte/evallu/<slug:slug>', reporteEvaluacionAlumno),
    path('detalles/<slug:slug>', Detail_Alumno.as_view()),
    path('evaluar/<slug:slug>', EvaluarAlumno.as_view()),
    path('diario/<slug:slug>', EvaDiario.as_view()),
    path('updateAlumno/<slug:slug>', Update_Alumno.as_view(), name="UpdateAlumno"),
    path('detalleAlumno/<slug:slug>', Detail_ninja.as_view(), name='detail_view' ),
    url(r'^alumnos/Buscar', busquedaAlumno, name='filtroAlumno'),
    url(r'^alumnos/paginador',ReporteNoChafa.as_view(),name='alumnos_pagina'),
    url(r'^tutores/busqueda',busquedaTurores,name='filtroTutores'),
    url(r'^alumnos/detalles',AlumnoReporte.as_view(),name='alumnos_reporte'),
    path('detalle/evaluacion/semanal/<slug:slug>', detalleEvalSem),

    ]

#para las fotos
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns     
    


