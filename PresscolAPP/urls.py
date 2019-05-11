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
from alumnos.views import  AgregarAlumConEstilo, Index
from padres.views import login
#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^alumnos/agregar',AgregarAlumConEstilo.as_view(),name='alumnos_agregarxd'),
     url(r'login/', login, name='login'),
    url(r'^$',Index, name='index'),
    
    #url para alumnos 
    

]
