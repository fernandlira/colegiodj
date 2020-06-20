from django.contrib import admin
from .models import Profesor, Alumno, Curso

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Curso)
