from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("ver-asistencias", views.getAsistencias, name="ver_asistencias"),
]
