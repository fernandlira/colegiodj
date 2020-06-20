from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Alumno, Asistencia, Profesor


def home(request):
    return render(request, "colegio/index.html", {})


def getAsistencias(request):
    alumnos = Alumno.objects.all()
    return render(request,'colegio/asistencias.html',{'alumnos':alumnos})

def getAsistencia(request, id=1):
    asistencias = Asistencia.objects.filter(alumno=id)
    alumno = Alumno.objects.get(pk=id)
    return render(request,'colegio/asistencia_estudiante.html',{'asistencias':asistencias,'alumno':alumno})
