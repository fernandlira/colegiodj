from django.contrib import admin
from .models import Alumno, Curso, Asistencia, Nota, Comentario

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Asistencia)
admin.site.register(Nota)
admin.site.register(Comentario)
