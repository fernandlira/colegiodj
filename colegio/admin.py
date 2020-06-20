from django.contrib import admin
from .models import Alumno, Curso, Asistencia

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Asistencia)
