from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Alumno

def home(request):
    return render(request, 'colegio/index.html',{})

def getAsistencias(request):
    alumnos = Alumno.objects.all()
    return render(request,'colegio/asistencias.html',{'alumnos':alumnos})