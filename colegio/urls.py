from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('ver-asistencias', views.getAsistencias, name='ver_asistencias'),
    path('ver-asistencia/<int:id>', views.getAsistencia, name='ver_asistencia_alumno'),
    path('<int:id>/comentar', views.makeComentario, name='justificacion_asistencias')
]
